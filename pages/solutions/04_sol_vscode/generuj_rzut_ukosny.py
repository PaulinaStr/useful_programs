# -*- coding: utf-8 -*-
"""Generowanie wykresów do raportu o rzucie ukośnym."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


OUT = Path("files/rzut_ukosny")
OUT.mkdir(parents=True, exist_ok=True)

BLUE, ORANGE, GREEN = "#2463A6", "#D47722", "#168578"
PURPLE, INK = "#8455A4", "#233044"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.labelcolor": INK,
    "text.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.18,
    "lines.linewidth": 2.3,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})


g = 9.81
x0, y0 = 0.0, 1.5
v0 = 20.0
alfa = np.deg2rad(40.0)
vx0 = v0 * np.cos(alfa)
vy0 = v0 * np.sin(alfa)
m = 0.50
c = 0.006


def zapisz(fig, nazwa):
    fig.savefig(OUT / f"{nazwa}.png", dpi=180)
    if plt.get_backend().lower() != "agg":
        plt.show()
    plt.close(fig)


# Model bez oporu.
T_bez = (vy0 + np.sqrt(vy0**2 + 2.0 * g * y0)) / g
zasieg_bez = x0 + vx0 * T_bez
wz_bez = y0 + vy0**2 / (2.0 * g)
t_bez = np.linspace(0.0, T_bez, 1001)
x_bez = x0 + vx0 * t_bez
y_bez = y0 + vy0 * t_bez - 0.5 * g * t_bez**2
vx_bez = np.full_like(t_bez, vx0)
vy_bez = vy0 - g * t_bez


# Model z kwadratowym oporem powietrza:
# dv/dt = -c/m * |v| * v + (0, -g).
def rhs(t, stan):
    x, y, vx, vy = stan
    predkosc = np.hypot(vx, vy)
    ax = -(c / m) * predkosc * vx
    ay = -g - (c / m) * predkosc * vy
    return [vx, vy, ax, ay]


def osiagnieto_podloze(t, stan):
    return stan[1]


osiagnieto_podloze.terminal = True
osiagnieto_podloze.direction = -1


sol = solve_ivp(
    rhs,
    (0.0, 10.0),
    [x0, y0, vx0, vy0],
    t_eval=np.linspace(0.0, 10.0, 2001),
    events=osiagnieto_podloze,
    rtol=1e-10,
    atol=1e-12,
)

t_op = sol.t
x_op, y_op, vx_op, vy_op = sol.y
if sol.t_events[0].size:
    T_op = sol.t_events[0][0]
    indeks_op = np.searchsorted(t_op, T_op, side="left")
    t_op = t_op[:indeks_op + 1]
    x_op = x_op[:indeks_op + 1]
    y_op = y_op[:indeks_op + 1]
    vx_op = vx_op[:indeks_op + 1]
    vy_op = vy_op[:indeks_op + 1]
    zasieg_op = x_op[-1]
else:
    raise RuntimeError("Numeryczna symulacja nie osiągnęła podłoża.")


print(f"Bez oporu: zasięg={zasieg_bez:.3f} m, lot={T_bez:.3f} s, wznios={wz_bez:.3f} m")
print(f"Z oporem: zasięg={zasieg_op:.3f} m, lot={T_op:.3f} s")


# Schemat układu.
fig, ax = plt.subplots(figsize=(10, 4.2), layout="constrained")
ax.set(xlim=(-1.0, 22.0), ylim=(-0.2, 10.0))
ax.plot([-1.0, 22.0], [0.0, 0.0], color=INK, lw=2)
ax.scatter([0.0], [y0], s=180, color=ORANGE, edgecolor=INK, zorder=3)
ax.annotate("", xy=(vx0 * 0.45, y0 + vy0 * 0.45),
            xytext=(0.0, y0),
            arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 2.5})
ax.plot([0.0, 0.0], [0.0, y0], "--", color="#64748B", lw=1)
ax.text(vx0 * 0.30, y0 + vy0 * 0.53,
        r"$\vec v_0$", color=ORANGE, fontsize=17)
ax.annotate("", xy=(4.5, y0),
            xytext=(0.0, y0),
            arrowprops={"arrowstyle": "<|-|>", "color": INK})
ax.text(2.25, y0 - 0.7, r"$\alpha$", ha="center", fontsize=15)
ax.annotate("", xy=(0.0, -0.05), xytext=(0.0, y0),
            arrowprops={"arrowstyle": "<->", "color": INK})
ax.text(-0.8, y0 / 2, r"$y_0$", va="center")
ax.text(11.0, 0.55, "podłoże", ha="center")
ax.axis("off")
ax.set_title("Model rzutu ukośnego", loc="left")
zapisz(fig, "schemat")


# Porównanie trajektorii.
fig, ax = plt.subplots(figsize=(10, 6), layout="constrained")
ax.plot(x_bez, y_bez, color=BLUE, label="Bez oporu")
ax.plot(x_op, y_op, color=ORANGE, label="Z oporem kwadratowym")
ax.scatter([x0], [y0], color=INK, zorder=4, label="Początek")
ax.axhline(0.0, color=INK, lw=1)
ax.set(
    xlabel="Położenie poziome x [m]",
    ylabel="Położenie pionowe y [m]",
    title="Porównanie trajektorii",
)
ax.legend()
zapisz(fig, "trajektorie")


# Składowe prędkości.
fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True, layout="constrained")
axes[0].plot(t_bez, vx_bez, color=BLUE, label="Bez oporu")
axes[0].plot(t_op, vx_op, color=ORANGE, label="Z oporem")
axes[0].set(ylabel=r"$v_x$ [m/s]", title="Składowe prędkości")
axes[0].legend()

axes[1].plot(t_bez, vy_bez, color=BLUE, label="Bez oporu")
axes[1].plot(t_op, vy_op, color=ORANGE, label="Z oporem")
axes[1].axhline(0.0, color=INK, lw=0.8)
axes[1].set(xlabel="Czas t [s]", ylabel=r"$v_y$ [m/s]")
axes[1].legend()
zapisz(fig, "predkosci")


# Przyspieszenia na podstawie pochodnych prędkości.
def gradient_numeryczny(y, t):
    return np.gradient(y, t)


ax_op = gradient_numeryczny(vx_op, t_op)
ay_op = gradient_numeryczny(vy_op, t_op)
ax_bez = np.zeros_like(t_bez)
ay_bez = -g * np.ones_like(t_bez)

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True, layout="constrained")
axes[0].plot(t_bez, ax_bez, color=BLUE, label="Bez oporu")
axes[0].plot(t_op, ax_op, color=ORANGE, label="Z oporem")
axes[0].set(ylabel=r"$a_x$ [m/s²]", title="Składowe przyspieszenia")
axes[0].legend()

axes[1].plot(t_bez, ay_bez, color=BLUE, label="Bez oporu")
axes[1].plot(t_op, ay_op, color=ORANGE, label="Z oporem")
axes[1].axhline(-g, color=INK, lw=0.8, ls="--", label=r"$-g$")
axes[1].set(xlabel="Czas t [s]", ylabel=r"$a_y$ [m/s²]")
axes[1].legend()
zapisz(fig, "przyspieszenia")


# Energia mechaniczna i energia stracona przez opór.
Ep_bez = m * g * y_bez
Ek_bez = 0.5 * m * (vx_bez**2 + vy_bez**2)

Ep_op = m * g * y_op
Ek_op = 0.5 * m * (vx_op**2 + vy_op**2)

fig, ax = plt.subplots(figsize=(10, 5.2), layout="constrained")
ax.plot(t_bez, Ep_bez + Ek_bez, color=BLUE, label="Całkowita bez oporu")
ax.plot(t_op, Ep_op + Ek_op, color=ORANGE, label="Całkowita z oporem")
ax.plot(t_op, Ep_op, color=GREEN, ls="--", label="Potencjalna z oporem")
ax.plot(t_op, Ek_op, color=PURPLE, ls="--", label="Kinetyczna z oporem")
ax.set(
    xlabel="Czas t [s]",
    ylabel="Energia [J]",
    title="Energia mechaniczna i jej zmiana",
)
ax.legend(ncol=2)
zapisz(fig, "energia")


# Zasięgi dla kilku początkowych kątów przy stałej prędkości.
katy = np.deg2rad(np.linspace(5.0, 85.0, 17))
zasiegi_bez = []
zasiegi_op = []

for kat in katy:
    vx_i = v0 * np.cos(kat)
    vy_i = v0 * np.sin(kat)
    T_i = (vy_i + np.sqrt(vy_i**2 + 2.0 * g * y0)) / g
    zasiegi_bez.append(x0 + vx_i * T_i)

    def rhs_kat(t, stan):
        x, y, vx, vy = stan
        predkosc = np.hypot(vx, vy)
        return [
            vx,
            vy,
            -(c / m) * predkosc * vx,
            -g - (c / m) * predkosc * vy,
        ]

    sol_i = solve_ivp(
        rhs_kat,
        (0.0, 10.0),
        [x0, y0, vx_i, vy_i],
        events=osiagnieto_podloze,
        rtol=1e-9,
        atol=1e-11,
    )
    if sol_i.t_events[0].size:
        zasiegi_op.append(sol_i.y_events[0][0, 0])
    else:
        zasiegi_op.append(np.nan)

fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
ax.plot(np.rad2deg(katy), zasiegi_bez, color=BLUE, marker="o",
        markevery=2, label="Bez oporu")
ax.plot(np.rad2deg(katy), zasiegi_op, color=ORANGE, marker="s",
        markevery=2, label="Z oporem")
ax.axvline(40.0, color=INK, lw=1.0, ls="--", alpha=0.6,
           label=r"Kąt analizowany: $40^\circ$")
ax.set(
    xlabel=r"Kąt początkowy $\alpha$ [°]",
    ylabel="Zasięg [m]",
    title="Zasięg w zależności od kątu",
)
ax.legend()
zapisz(fig, "zasieg_od_kata")
