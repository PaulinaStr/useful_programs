# Rzut ukośny — od kinematyki Galileusza do ruchu z oporem powietrza

*Raport obliczeniowy i przykład wykorzystania Markdown w dokumentacji naukowej.*

**Temat:** dwuwymiarowy ruch masy w jednorodnym polu grawitacyjnym.  
**Metoda:** rozwiązania analityczne, symulacja numeryczna w Pythonie i interpretacja wykresów.  
**Charakter danych:** przykład modelowy dla $v_0 = 33\,\mathrm{m/s}$ oraz $\alpha = 45^\circ$; wszystkie wykresy przedstawiają obliczenia numeryczne, a nie pomiary laboratoryjne.

Galileusz stwierdził, że 
> ruchy składowe w rzucie ukośnym są od siebie niezależne. 

Newton stwierdził, że
> przyspieszenie ciała wynika z wypadkowej działających sił. 

Połączenie tych zasad pozwala opisać tor lotu ciała. W tym raporcie pokazujemy, jak położenie, prędkość i energia zmieniają się w czasie oraz jak na zasięg i wysokość wpływa opór powietrza proporcjonalny do kwadratu prędkości.

Współrzędne położenia $(x, y)$ opisują gdzie znajduje się ciało, a składowe prędkości $(v_x, v_y)$ określają, jak szybko i w którym kierunku się przemieszcza.

## Spis treści

1. [Cel i model fizyczny](#1-cel-i-model-fizyczny)
2. [Równania ruchu bez oporu powietrza](#2-równania-ruchu-bez-oporu-powietrza)
3. [Przykład liczbowy i trajektoria](#3-przykład-liczbowy-i-trajektoria)
4. [Rzut z oporem powietrza](#4-rzut-z-oporem-powietrza)
5. [Energia i przestrzeń fazowa](#5-energia-i-przestrzeń-fazowa)
6. [Kod i odtwarzanie wykresów](#6-kod-i-odtwarzanie-wykresów)
7. [Wnioski](#7-wnioski)
8. [Dalsza lektura](#8-dalsza-lektura)

---

## 1. Cel i model fizyczny

Dlaczego ciało rzucone pod kątem zakreśla parabolę, a przy uwzględnieniu oporu powietrza jego zasięg i maksymalna wysokość maleją? Grawitacja nadaje stałe przyspieszenie pionowe, podczas gdy opór płynu (powietrza) hamuje ciało w kierunku przeciwnym do wektora prędkości.

Celem raportu jest wyznaczenie trajektorii, prędkości oraz zasięgu rzutu w modelu idealnym oraz w obecności siły oporu proporcjonalnej do kwadratu prędkości dla parametrów wynikających z numeru indeksu ($v_0 = 33\,\mathrm{m/s}$, $\alpha = 45^\circ$).

### 1.1. Założenia

- Ruch odbywa się w płaszczyźnie pionowej $(x, y)$.
- Przyspieszenie ziemskie $g = 9{,}81\,\mathrm{m/s^2}$ jest stałe i skierowane w dół.
- W modelu idealnym pomijamy opory ruchu.
- W modelu realistycznym siła oporu powietrza jest proporcjonalna do kwadratu prędkości: $\vec{F}_{\mathrm{op}} = -\frac{1}{2}\rho C_d A v \vec{v}$.

![Schemat rzutu ukośnego: punkt startu, kąt alfa, prędkość początkowa v0 oraz rozkład na składowe](files/rzut/schemat_rzutu.png)

*Rysunek 1. Schemat wektorowy rzutu ukośnego dla wartości początkowych. Schemat nie zachowuje skali.*

### 1.2. Symbole i jednostki

| Symbol | Znaczenie | Jednostka SI |
| :--- | :--- | :---: |
| $m$ | masa ciała | $\mathrm{kg}$ |
| $v_0$ | początkowa prędkość | $\mathrm{m/s}$ |
| $\alpha$ | kąt rzutu względem poziomu | $\mathrm{deg}$ ($\mathrm{rad}$) |
| $x, y$ | współrzędne położenia | $\mathrm{m}$ |
| $v_x, v_y$ | składowe prędkości | $\mathrm{m/s}$ |
| $g$ | przyspieszenie ziemskie | $\mathrm{m/s^2}$ |
| $R$ | zasięg rzutu | $\mathrm{m}$ |
| $H$ | maksymalna wysokość | $\mathrm{m}$ |

---

## 2. Równania ruchu bez oporu powietrza

### 2.1. Druga zasada Newtona

W układzie kartezjańskim, pomijając opory, równania ruchu mają postać:
$$m \ddot{x} = 0, \qquad m \ddot{y} = -mg.$$

Po dwukrotnym scalakowaniu i uwzględnieniu warunków początkowych ($x(0)=0, y(0)=0$, $\dot{x}(0)=v_0\cos\alpha, \dot{y}(0)=v_0\sin\alpha$):
$$x(t) = v_0 t \cos\alpha,$$
$$y(t) = v_0 t \sin\alpha - \frac{1}{2}gt^2.$$

### 2.2. Zasięg i maksymalna wysokość

Eliminując czas $t$, otrzymujemy równanie trajektorii:
$$y(x) = x \operatorname{tg}\alpha - \frac{g}{2v_0^2 \cos^2\alpha} x^2.$$

Maksymalna wysokość $H$ oraz całkowity zasięg rzutu $ُمْ$ wynoszą odpowiednio:
$$H = \frac{v_0^2 \sin^2\alpha}{2g}, \qquad R = \frac{v_0^2 \sin(2\alpha)}{g}.$$

---

## 3. Przykład liczbowy i trajektoria

Dla przyjętych danych ($v_0 = 33\,\mathrm{m/s}$, $\alpha = 45^\circ$, $g = 9{,}81\,\mathrm{m/s^2}$) otrzymujemy następujące wartości modelowe:

| Wielkość | Wartość | Interpretacja |
| :--- | ---: | :--- |
| Prędkość początkowa $v_0$ | $33{,}0\,\mathrm{m/s}$ | moduł prędkości w chwili $t=0$ |
| Kąt rzutu $\alpha$ | $45{,}0^\circ$ ($\pi/4\,\mathrm{rad}$) | optymalny kąt dla maksymalnego zasięgu |
| Składowa pozioma $v_{x0}$ | $23{,}33\,\mathrm{m/s}$ | początkowa prędkość pozioma |
| Składowa pionowa $v_{y0}$ | $23{,}33\,\mathrm{m/s}$ | początkowa prędkość pionowa |
| Czas lotu $T_{\text{lot}}$ | $3{,}37\,\mathrm{s}$ | całkowity czas do powrotu na $y=0$ |
| Maksymalna wysokość $H$ | $27{,}76\,\mathrm{m}$ | wierzchołek paraboli |
| Zasięg rzutu $R$ | $111{,}04\,\mathrm{m}$ | odległość lądowania |

![Wykres trajektorii ruchu idealnego w płaszczyźnie xy](files/rzut/trajektoria.png)

*Rysunek 2. Trajektoria rzutu ukośnego w modelu bez oporu powietrza.*

---

## 4. Rzut z oporem powietrza

### 4.1. Układ równań z oporem aerodynamicznym

Jeśli uwzględnimy siłę oporu proporcjonalną do kwadratu prędkości $\vec{F}_{\mathrm{op}} = -b v \vec{v}$ (gdzie $b = \frac{1}{2}\rho C_d A$), równania ruchu przyjmują postać nieliniową:
$$\ddot{x} = -\frac{b}{m} v \dot{x}, \qquad \ddot{y} = -g - \frac{b}{m} v \dot{y},$$
gdzie $v = \sqrt{\dot{x}^2 + \dot{y}^2}$. Układ ten nie posiada analitycznego rozwiązania w funkcjach analitycznych i wymaga całkowania numerycznego.

![Porównanie trajektorii bez oporu i z oporem powietrza](files/rzut/porownanie_opor.png)

*Rysunek 3. Wpłyv oporu powietrza na zasięg i wysokość rzutu (symulacja dla przykładowego współczynnika oporu).*

---

## 5. Energia i przestrzeń fazowa

W modelu bez oporu całkowita energia mechaniczna $E = E_k + E_p = \frac{1}{2}m(v_x^2 + v_y^2) + mgy$ jest zachowana. Obecność oporu powietrza powoduje monotoniczny spadek energii mechanicznej układu w czasie wskutek pracy sił niekonserwatywnych.

---

## 6. Kod i odtwarzanie wykresów

Wykresy wygenerowano za pomocą poniższego skryptu w języku Python przy użyciu bibliotek `numpy`, `matplotlib` oraz `scipy`.

### Skrypt Python (`generuj_wykresy_rzut.py`)

```python
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from scipy.integrate import solve_ivp

# Konfiguracja katalogu i stylu
OUT = Path("files/rzut")
OUT.mkdir(parents=True, exist_ok=True)
BLUE, ORANGE, GREEN, INK = "#2463A6", "#D47722", "#168578", "#233044"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.titleweight": "bold",
    "axes.labelcolor": INK, "text.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.18,
    "lines.linewidth": 2.3, "figure.facecolor": "white",
})

# Dane z indeksu
v0 = 33.0
alpha_deg = 45.0
alpha = np.radians(alpha_deg)
g = 9.81
m = 1.0  kg (masa modelowa)

def zapisz(fig, nazwa):
    fig.savefig(OUT / f"{nazwa}.png", dpi=180)
    if plt.get_backend().lower() != "agg":
        plt.show()
    plt.close(fig)

# 1. Rysunek schematu
fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
ax.set(xlim=(-2, 40), ylim=(-2, 35))
ax.axis("off")
ax.annotate("", xy=(30, 25), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.5))
ax.text(16, 14, f"$v_0 = {v0}\\,\\mathrm{{m/s}}$", color=BLUE, fontsize=12, rotation=35)
ax.plot([0, 35], [0, 0], color=INK, lw=1.2)
ax.set_title("Schemat rzutu ukośnego", loc="left")
zapisz(fig, "schemat_rzutu")

# 2. Obliczenia analityczne i trajektoria idealna
T_lot = (2 * v0 * np.sin(alpha)) / g
t = np.linspace(0, T_lot, 500)
x = v0 * np.cos(alpha) * t
y = v0 * np.sin(alpha) * t - 0.5 * g * t**2

fig, ax = plt.subplots(figsize=(9, 4.5), layout="constrained")
ax.plot(x, y, color=BLUE, label="Model idealny")
ax.set(xlabel="Zasięg x [m]", ylabel="Wysokość y [m]", title="Trajektoria rzutu ukośnego")
ax.legend(loc="upper right")
zapisz(fig, "trajektoria")

# 3. Symulacja z oporem powietrza (solve_ivp)
b_m = 0.02  # współczynnik b/m
def rhs(t, state):
    px, py, vx, vy = state
    v = np.hypot(vx, vy)
    ax_acc = -b_m * v * vx
    ay_acc = -g - b_m * v * vy
    return [vx, vy, ax_acc, ay_acc]

sol = solve_ivp(rhs, (0, T_lot * 1.1), [0, 0, v0*np.cos(alpha), v0*np.sin(alpha)],
                t_eval=np.linspace(0, T_lot * 1.1, 600))

# Odcięcie po uderzeniu w ziemię (y >= 0)
idx = sol.y[1] >= 0
x_op = sol.y[0][idx]
y_op = sol.y[1][idx]

fig, ax = plt.subplots(figsize=(9, 4.5), layout="constrained")
ax.plot(x, y, color=BLUE, label="Bez oporu")
ax.plot(x_op, y_op, color=ORANGE, ls="--", label="Z oporem powietrza")
ax.set(xlabel="Zasięg x [m]", ylabel="Wysokość y [m]", title="Porównanie trajektorii z oporem powietrza")
ax.legend(loc="upper right")
zapisz(fig, "porownanie_opor")

print("Wszystkie wykresy wygenerowano pomyślnie!")