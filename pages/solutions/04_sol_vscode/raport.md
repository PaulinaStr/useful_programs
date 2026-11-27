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

Współrzędne położenia $(x, y)$ opisują, gdzie znajduje się ciało, a składowe prędkości $(v_x, v_y)$ określają, jak szybko i w którym kierunku się przemieszcza.

## Spis treści

1. [Cel i model fizyczny](#1-cel-i-model-fizyczny)
2. [Równania ruchu i ich rozwiązanie](#2-równania-ruchu-i-ich-rozwiązanie)
3. [Przykład liczbowy i przebiegi czasowe](#3-przykład-liczbowy-i-przebiegi-czasowe)
4. [Energia i przestrzeń fazowa](#4-energia-i-przestrzeń-fazowa)
5. [Rzut z oporem powietrza](#5-rzut-z-oporem-powietrza)
6. [Kod i odtwarzanie wykresów](#6-kod-i-odtwarzanie-wykresów)
7. [Wnioski](#7-wnioski)
8. [Dalsza lektura](#8-dalsza-lektura)

---

## 1. Cel i model fizyczny

Dlaczego ciało rzucone pod kątem zakreśla parabolę, a bezwładność i grawitacja sprawiają, że wraca ono na ziemię? Siła grawitacji nadaje stałe przyspieszenie pionowe, podczas gdy ruch poziomy pozostaje jednostajny w modelu idealnym. Powstaje zakrzywiony tor lotu.

Celem raportu jest opisanie położenia, składowych prędkości oraz energii ciała, a także sprawdzenie, jak zmieniają się one po dodaniu aerodynamicznego oporu powietrza.

### 1.1. Założenia

- Ruch odbywa się w dwuwymiarowej płaszczyźnie pionowej $(x, y)$.
- Masa $m$ jest stała, a przyspieszenie ziemskie $g$ nie zmienia się z wysokością.
- W modelu idealnym pomijamy opory ruchu.
- W modelu rzeczywistym przyjmujemy siłę oporu proporcjonalną do kwadratu prędkości.

Współrzędna $x$ oznacza zasięg poziomy, a $y$ wysokość nad poziomem wyrzutu.

![Schemat dwuwymiarowego rzutu ukośnego: kąt alfa, prędkość początkowa oraz rozkład wektorów](files/rzut/schemat.png)

*Rysunek 1. Ciało wystrzelone z prędkością początkową pod kątem alfa. Schemat nie zachowuje skali.*

### 1.2. Symbole i jednostki

| Symbol | Znaczenie | Jednostka SI |
| :--- | :--- | :---: |
| $m$ | masa ciała | $\mathrm{kg}$ |
| $v_0$ | początkowa prędkość | $\mathrm{m/s}$ |
| $\alpha$ | kąt rzutu względem poziomu | $\mathrm{deg}$ ($\mathrm{rad}$) |
| $x, y$ | współrzędne położenia | $\mathrm{m}$ |
| $v_x, v_y$ | składowe prędkości | $\mathrm{m/s}$ |
| $g$ | przyspieszenie ziemskie ($\approx 9{,}81$) | $\mathrm{m/s^2}$ |
| $R$ | całkowity zasięg rzutu | $\mathrm{m}$ |
| $H$ | maksymalna wysokość | $\mathrm{m}$ |

---

## 2. Równania ruchu i ich rozwiązanie

### 2.1. Druga zasada Newtona

Z drugiej zasady Newtona w układzie kartezjańskim otrzymujemy:
$$m\frac{d^2x}{dt^2}=0, \qquad m\frac{d^2y}{dt^2}=-mg.$$

Po uwzględnieniu warunków początkowych ($x(0)=0, y(0)=0$, $\dot{x}(0)=v_0\cos\alpha, \dot{y}(0)=v_0\sin\alpha$):
$$x(t)=v_0t\cos\alpha, \qquad y(t)=v_0t\sin\alpha-\frac{1}{2}gt^2.$$

### 2.2. Równanie trajektorii i parametry ruchu

Eliminując czas $t$ z równań ruchu, otrzymujemy równanie toru w postaci jawnej:
$$y(x)=x\operatorname{tg}\alpha-\frac{g}{2v_0^2\cos^2\alpha}x^2.$$

Całkowity czas lotu $T_{\mathrm{lot}}$, maksymalna wysokość $H$ oraz zasięg $R$ wynoszą:
$$T_{\mathrm{lot}}=\frac{2v_0\sin\alpha}{g}, \qquad H=\frac{v_0^2\sin^2\alpha}{2g}, \qquad R=\frac{v_0^2\sin(2\alpha)}{g}.$$

---

## 3. Przykład liczbowy i przebiegi czasowe

Przyjmujemy parametry z numeru indeksu: $v_0=33{,}0\,\mathrm{m/s}$, $\alpha=45^\circ$, oraz $g=9{,}81\,\mathrm{m/s^2}$.

| Wielkość | Wartość | Interpretacja |
| :--- | ---: | :--- |
| Prędkość początkowa $v_0$ | $33{,}0\,\mathrm{m/s}$ | moduł prędkości startowej |
| Kąt rzutu $\alpha$ | $45{,}0^\circ$ | optymalny kąt dla zasięgu |
| Składowa pozioma $v_{x0}$ | $23{,}33\,\mathrm{m/s}$ | stała prędkość pozioma |
| Składowa pionowa $v_{y0}$ | $23{,}33\,\mathrm{m/s}$ | początkowa prędkość pionowa |
| Czas lotu $T_{\mathrm{lot}}$ | $4{,}76\,\mathrm{s}$ | całkowity czas do upadku |
| Maksymalna wysokość $H$ | $27{,}76\,\mathrm{m}$ | wierzchołek trajektorii |
| Zasięg rzutu $R$ | $111{,}04\,\mathrm{m}$ | odległość lądowania |

![Przebiegi zmienności położenia i składowych prędkości w funkcji czasu](files/rzut/polozenie_predkosc.png)

*Rysunek 2. Wspólna oś czasu przedstawiająca zmianę współrzędnych oraz prędkości.*

---

## 4. Energia i przestrzeń fazowa

W modelu idealnym energia mechaniczna układu jest zachowana:
$$E = E_k + E_p = \frac{1}{2}m(v_x^2 + v_y^2) + mgy = \mathrm{const}.$$
W najwyższym punkcie trajektorii prędkość pionowa $v_y=0$, a energia potencjalna osiąga maksimum.

---

## 5. Rzut z oporem powietrza

Uwzględniając siłę oporu proporcjonalną do kwadratu prędkości $\vec{F}_{\mathrm{op}}=-b v \vec{v}$, układ równań staje się nieliniowy i jest rozwiązywany numerycznie za pomocą solvera `solve_ivp`.

![Porównanie trajektorii w modelu idealnym i z oporem powietrza](files/rzut/porownanie_opor.png)

*Rysunek 3. Wpływ oporu powietrza na skrócenie zasięgu i obniżenie maksymalnej wysokości lotu.*

---

## 6. Kod i odtwarzanie wykresów

Wykresy wykonano w Pythonie. Poniższy skrypt generuje wszystkie niezbędne pliki graficzne.

```python
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

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

v0, alpha_deg, g = 33.0, 45.0, 9.81
alpha = np.radians(alpha_deg)

def zapisz(fig, nazwa):
    fig.savefig(OUT / f"{nazwa}.png", dpi=180)
    plt.close(fig)

# 1. Schemat
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.set(xlim=(-2, 40), ylim=(-2, 35))
ax.axis("off")
ax.plot([0, 38], [0, 0], color=INK, lw=1.4)
ax.annotate("", xy=(25, 25), xytext=(0, 0), arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 2.5})
ax.text(14, 14, f"$v_0 = {v0}\\,\\mathrm{{m/s}}$", color=BLUE, fontsize=12)
ax.set_title("Schemat rzutu ukośnego", loc="left")
zapisz(fig, "schemat")

# 2. Ruch idealny
T_lot = (2 * v0 * np.sin(alpha)) / g
t = np.linspace(0, T_lot, 500)
x = v0 * np.cos(alpha) * t
y = v0 * np.sin(alpha) * t - 0.5 * g * t**2
vx = v0 * np.cos(alpha) * np.ones_like(t)
vy = v0 * np.sin(alpha) - g * t

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True, layout="constrained")
axes[0].plot(t, y, color=BLUE)
axes[0].set_ylabel("Wysokość y [m]")
axes[0].set_title("Współrzędna pionowa i składowe prędkości w czasie", loc="left")
axes[1].plot(t, vx, color=BLUE, label="$v_x$")
axes[1].plot(t, vy, color=ORANGE, label="$v_y$")
axes[1].set(xlabel="Czas t [s]", ylabel="Prędkość [m/s]")
axes[1].legend(loc="upper right")
zapisz(fig, "polozenie_predkosc")

# 3. Z oporem
b_m = 0.01
def rhs(czas, stan):
    px, py, vx, vy = stan
    v = np.hypot(vx, vy)
    return [vx, vy, -b_m * v * vx, -g - b_m * v * vy]

sol = solve_ivp(rhs, (0, T_lot * 1.2), [0, 0, v0*np.cos(alpha), v0*np.sin(alpha)],
                t_eval=np.linspace(0, T_lot * 1.2, 600))
idx = sol.y[1] >= 0

fig, ax = plt.subplots(figsize=(9, 4.5), layout="constrained")
ax.plot(x, y, color=BLUE, label="Bez oporu")
ax.plot(sol.y[0][idx], sol.y[1][idx], color=ORANGE, ls="--", label="Z oporem powietrza")
ax.set(xlabel="Zasięg x [m]", ylabel="Wysokość y [m]", title="Porównanie trajektorii")
ax.legend(loc="upper right")
zapisz(fig, "porownanie_opor")
print("Wykresy wygenerowano pomyślnie!")