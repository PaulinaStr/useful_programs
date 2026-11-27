# Raport z symulacji rzutu ukośnego — od modelu idealnego do oporu aerodynamicznego

*Raport obliczeniowy i analiza numeryczna ruchu w dwóch wymiarach.*

**Temat:** dwuwymiarowy ruch punktu materialnego rzuconego pod kątem do poziomu.  
**Metoda:** rozwiązania analityczne, całkowanie numeryczne (RK45 w SciPy) i interpretacja wykresów.  
**Charakter danych:** obliczenia modelowe dla spersonalizowanych parametrów ($v_0 = 33\,\mathrm{m/s}$, $\alpha = 45^\circ$).

Galileusz wykazał, że
> ruch rzuconego ciała można rozłożyć na dwa niezależne ruchy: jednostajny w poziomie oraz jednostajnie przyspieszony w pionie.

Newton uzupełnił ten obraz, wskazując, że
> w rzeczywistym ośrodku na poruszające się ciało działa siła oporu, która zaburza symetrię toru i rozprasza energię mechaniczną.

Połączenie tych praw pozwala zestawić klasyczną parabolę balistyczną z rzeczywistą krzywą balistyczną. W tym raporcie wyprowadzamy równania ruchu, analizujemy przemiany energii oraz badamy wpływ oporu aerodynamicznego proporcjonalnego do kwadratu prędkości.

---

## Spis treści

1. [Cel i model fizyczny](#1-cel-i-model-fizyczny)
2. [Równania ruchu i wyprowadzenia analityczne](#2-równania-ruchu-i-wyprowadzenia-analityczne)
3. [Wyniki liczbowe i przebiegi czasowe](#3-wyniki-liczbowe-i-przebiegi-czasowe)
4. [Energia mechaniczna i składowe prędkości](#4-energia-mechaniczna-i-składowe-prędkości)
5. [Rzut ukośny z oporem powietrza](#5-rzut-ukośny-z-oporem-powietrza)
6. [Portret fazowy ruchu pionowego](#6-portret-fazowy-ruchu-pionowego)
7. [Kod źródłowy odtwarzający wykresy](#7-kod-źródłowy-odtwarzający-wykresy)
8. [Wnioski i lista kontrolna](#8-wnioski-i-lista-kontrolna)

---

## 1. Cel i model fizyczny

Dlaczego kamień rzucony pod kątem zakreśla w próżni idealną parabolę, podczas gdy lot piłki czy pocisku w powietrzu jest wyraźnie krótszy i niesymetryczny? W modelu idealnym jedyną siłą działającą na ciało jest stała siła ciężkości. W rzeczywistości ośrodek stawia opór rosnący wraz z szybkością obiektu.

Celem raportu jest wyprowadzenie równań ruchu dla rzutu ukośnego, wyznaczenie parametrów lotu dla zadanych warunków początkowych oraz porównanie toru idealnego z trajektoriami uwzględniającymi opór powietrza.

### 1.1. Założenia modelu

- Ruch odbywa się w płaszczyźnie pionowej $(x, y)$, gdzie $y = 0$ oznacza poziom gruntu.
- Ciało traktujemy jako punkt materialny o stałej masie $m = 1{,}0\,\mathrm{kg}$.
- Przyspieszenie ziemskie jest stałe i wynosi $g = 9{,}81\,\mathrm{m/s^2}$.
- W modelu idealnym pomijamy opory powietrza oraz krzywiznę Ziemi.
- W modelu rzeczywistym uwzględniamy opór kwadratowy $\vec{F}_{\mathrm{op}} = -c \, v \, \vec{v}$, gdzie współczynnik oporu wynosi $c = 0{,}05\,\mathrm{kg/m}$.

### 1.2. Symbole i jednostki

| Symbol | Znaczenie | Jednostka SI |
| :--- | :--- | :---: |
| $v_0$ | prędkość początkowa | $\mathrm{m/s}$ |
| $\alpha$ | kąt rzutu względem poziomu | $\mathrm{rad}$ ($\mathrm{^\circ}$) |
| $x, y$ | współrzędna pozioma i pionowa | $\mathrm{m}$ |
| $v_x, v_y$ | składowe wektora prędkości | $\mathrm{m/s}$ |
| $g$ | przyspieszenie ziemskie | $\mathrm{m/s^2}$ |
| $Z$ | zasięg maksymalny rzutu | $\mathrm{m}$ |
| $H_{\max}$ | maksymalna wysokość lotu | $\mathrm{m}$ |
| $t_c$ | całkowity czas lotu | $\mathrm{s}$ |
| $c$ | współczynnik oporu aerodynamicznego | $\mathrm{kg/m}$ |
| $E_k, E_p, E$ | energia kinetyczna, potencjalna i całkowita | $\mathrm{J}$ |

---

## 2. Równania ruchu i wyprowadzenia analityczne

### 2.1. Zasada niezależności ruchów

W układzie bez oporów powietrza na ciało działa wyłącznie siła ciężkości $\vec{F}_g = (0, -mg)$. Z drugiej zasady dynamiki Newtona otrzymujemy układ równań różniczkowych:

$$m\ddot{x} = 0, \qquad m\ddot{y} = -mg.$$

Dla warunków początkowych $x(0) = 0$, $y(0) = 0$ oraz składowych prędkości $v_{0x} = v_0\cos\alpha$, $v_{0y} = v_0\sin\alpha$, dwukrotne całkowanie po czasie daje równania kinematyczne:

$$x(t) = v_0 \cos(\alpha) \cdot t,$$

$$y(t) = v_0 \sin(\alpha) \cdot t - \frac{1}{2} g t^2.$$

### 2.2. Równanie toru, czas lotu, wysokość i zasięg

Wyznaczając czas $t = \frac{x}{v_0\cos\alpha}$ z pierwszego równania i podstawiając do drugiego, otrzymujemy równanie trajektorii $y(x)$:

$$y(x) = x \tan\alpha - \frac{g}{2 v_0^2 \cos^2\alpha} x^2.$$

Jest to równanie paraboli z ramionami skierowanymi w dół. Z warunku $y(t_c) = 0$ (dla $t_c > 0$) wyznaczamy **całkowity czas lotu**:

$$t_c = \frac{2 v_0 \sin\alpha}{g}.$$

Podstawiając $t_c$ do równania na $x(t)$, otrzymujemy **zasięg rzutu**:

$$Z = x(t_c) = \frac{v_0^2 \sin(2\alpha)}{g}.$$

W najwyższym punkcie toru składowa pionowa prędkości zeruje się ($v_y = 0$), co następuje w chwili $t_w = t_c / 2$. Stąd **wysokość maksymalna** wynosi:

$$H_{\max} = y(t_w) = \frac{v_0^2 \sin^2\alpha}{2g}.$$

**Kontrola jednostek:** wyrażenie $v_0^2 / g$ ma wymiar $\frac{\mathrm{m^2/s^2}}{\mathrm{m/s^2}} = \mathrm{m}$, co zgadza się z jednostką zasięgu i wysokości.

---

## 3. Wyniki liczbowe i przebiegi czasowe

Zgodnie z wymaganiami zadania przyjęto wartości wyznaczone na podstawie numeru indeksu (`337645`): $v_0 = 33{,}0\,\mathrm{m/s}$ oraz $\alpha = 45^\circ$ ($\frac{\pi}{4}\,\mathrm{rad}$). Kąt $45^\circ$ jest kątem optymalnym, maksymalizującym zasięg w próżni ($\sin 90^\circ = 1$).

| Wielkość | Wzór | Wartość obliczona | Interpretacja |
| :--- | :--- | ---: | :--- |
| Składowa $v_{0x}$ | $v_0\cos 45^\circ$ | $23{,}33\,\mathrm{m/s}$ | stała prędkość pozioma |
| Składowa $v_{0y}$ | $v_0\sin 45^\circ$ | $23{,}33\,\mathrm{m/s}$ | początkowa prędkość wznoszenia |
| Czas lotu $t_c$ | $2v_{0y}/g$ | $4{,}76\,\mathrm{s}$ | czas od startu do upadku |
| Wysokość $H_{\max}$ | $v_{0y}^2/(2g)$ | $27{,}75\,\mathrm{m}$ | osiągana w chwili $t = 2{,}38\,\mathrm{s}$ |
| Zasięg $Z$ | $v_0^2/g$ | $111{,}01\,\mathrm{m}$ | maksymalny dystans w próżni |

![Trajektoria rzutu ukośnego oraz wykresy współrzędnych x(t) i y(t)](wykresy/rzut_idealny.png)

*Rysunek 1. Po lewej: symetryczna parabola toru ruchu. Po prawej: liniowy wzrost współrzędnej $x(t)$ oraz paraboliczny przebieg wysokości $y(t)$.*

---

## 4. Energia mechaniczna i składowe prędkości

W modelu bez oporów powietrza układ jest zachowawczy. Energia kinetyczna i potencjalna ulegają ciągłej przemianie, lecz ich suma pozostaje stała:

$$E = E_k(t) + E_p(t) = \frac{1}{2}m(v_x^2 + v_y^2) + mgy = \frac{1}{2}mv_0^2 = \mathrm{const}.$$

Dla masy modelowej $m = 1{,}0\,\mathrm{kg}$ energia całkowita wynosi $E = 544{,}50\,\mathrm{J}$. W najwyższym punkcie toru ($y = H_{\max}$) energia potencjalna osiąga maksimum $E_p = 272{,}25\,\mathrm{J}$, a energia kinetyczna nie spada do zera, ponieważ ciało wciąż porusza się w poziomie z prędkością $v_x = v_{0x}$ ($E_k = \frac{1}{2}mv_{0x}^2 = 272{,}25\,\mathrm{J}$).

![Przemiany energii oraz składowe wektora prędkości w czasie](wykresy/energia_i_predkosc.png)

*Rysunek 2. Po lewej: zasada zachowania energii mechanicznej w rzucie idealnym. Po prawej: stała składowa $v_x$ i liniowo malejąca składowa $v_y$.*

---

## 5. Rzut ukośny z oporem powietrza

### 5.1. Równania różniczkowe z oporem kwadratowym

Przy dużych prędkościach (rzędu kilkudziesięciu $\mathrm{m/s}$) dominuje opór aerodynamiczny proporcjonalny do kwadratu wartości prędkości $v = \sqrt{v_x^2 + v_y^2}$:

$$\vec{F}_{\mathrm{op}} = -c \, v \, \vec{v} = \left(-c\sqrt{v_x^2+v_y^2}\,v_x, \; -c\sqrt{v_x^2+v_y^2}\,v_y\right).$$

Układ równań ruchu staje się sprzężony i nieliniowy:

$$\ddot{x} = -\frac{c}{m}\sqrt{\dot{x}^2 + \dot{y}^2}\,\dot{x},$$

$$\ddot{y} = -g - \frac{c}{m}\sqrt{\dot{x}^2 + \dot{y}^2}\,\dot{y}.$$

Układ ten nie posiada elementarnego rozwiązania analitycznego, dlatego rozwiązano go numerycznie metodą Rungego-Kutty (funkcja `solve_ivp` z biblioteki `scipy.integrate`).

### 5.2. Porównanie trajektorii dla różnych współczynników oporu

![Porównanie toru lotu dla różnych współczynników oporu powietrza](wykresy/porownanie_oporu.png)

*Rysunek 3. Wpływ oporu aerodynamicznego na zasięg i kształt krzywej balistycznej. Wraz ze wzrostem współczynnika $c$ ramię opadające staje się coraz bardziej strome.*

| Model | Współczynnik $c$ | Zasięg $Z$ | Wysokość $H_{\max}$ | Skrócenie zasięgu |
| :--- | :---: | ---: | ---: | ---: |
| Brak oporu | $0{,}000\,\mathrm{kg/m}$ | $111{,}01\,\mathrm{m}$ | $27{,}75\,\mathrm{m}$ | $0\%$ |
| Słaby opór | $0{,}015\,\mathrm{kg/m}$ | $61{,}42\,\mathrm{m}$ | $19{,}85\,\mathrm{m}$ | $-44{,}7\%$ |
| Średni opór | $0{,}050\,\mathrm{kg/m}$ | $31{,}85\,\mathrm{m}$ | $12{,}45\,\mathrm{m}$ | $-71{,}3\%$ |
| Silny opór | $0{,}120\,\mathrm{kg/m}$ | $16{,}92\,\mathrm{m}$ | $7{,}48\,\mathrm{m}$ | $-84{,}8\%$ |

---

## 6. Portret fazowy ruchu pionowego

Analiza przestrzeni fazowej $(y, v_y)$ pozwala wyraźnie dostrzec różnicę między układem zachowawczym a dyssypatywnym. W rzucie bez oporu krzywa fazowa jest idealnie symetryczna względem osi $v_y = 0$ — prędkość uderzenia w ziemię ma tę samą wartość bezwzględną co prędkość początkowa ($v_y(t_c) = -23{,}33\,\mathrm{m/s}$). W obecności oporu powietrza energia jest nieodwracalnie tracona, przez co ciało uderza w podłoże ze znacznie mniejszą prędkością pionową.

![Portret fazowy ruchu w pionie](wykresy/portret_fazowy.png)

*Rysunek 4. Portret fazowy $(y, v_y)$. Utrata energii powoduje zawężenie krzywej i mniejszą wartość prędkości końcowej przy powrocie do $y = 0$.*

---

## 7. Kod źródłowy odtwarzający wykresy

Wszystkie wykresy zamieszczone w raporcie zostały wygenerowane lokalnie w środowisku Visual Studio Code za pomocą poniższego skryptu w języku Python (`symulacja.py`).

```python
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

OUT = Path("pages/solutions/04_sol_vscode/wykresy")
OUT.mkdir(parents=True, exist_ok=True)

BLUE, ORANGE, GREEN, PURPLE, INK = "#2463A6", "#D47722", "#168578", "#8455A4", "#233044"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 13, "axes.titleweight": "bold",
    "axes.labelcolor": INK, "text.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.18,
    "lines.linewidth": 2.3, "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

v0, alpha_deg, g, m = 33.0, 45.0, 9.81, 1.0
alpha = np.radians(alpha_deg)
vx0, vy0 = v0 * np.cos(alpha), v0 * np.sin(alpha)

def zapisz(fig, nazwa):
    fig.savefig(OUT / f"{nazwa}.png", dpi=180)
    plt.close(fig)

# 1. Rzut idealny
t_lotu = 2 * vy0 / g
t = np.linspace(0, t_lotu, 1000)
x, y = vx0 * t, vy0 * t - 0.5 * g * t**2
vx, vy = np.full_like(t, vx0), vy0 - g * t

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), layout="constrained")
axes[0].plot(x, y, color=BLUE, label="Tor ruchu y(x)")
axes[0].scatter([x[np.argmax(y)]], [np.max(y)], color=ORANGE, zorder=3, label=f"H_max = {np.max(y):.2f} m")
axes[0].set(xlabel="Zasięg x [m]", ylabel="Wysokość y [m]", title="Trajektoria rzutu (bez oporu)")
axes[0].legend()
axes[1].plot(t, x, color=BLUE, label="x(t)")
axes[1].plot(t, y, color=ORANGE, label="y(t)")
axes[1].set(xlabel="Czas t [s]", ylabel="Położenie [m]", title="Współrzędne w funkcji czasu")
axes[1].legend()
zapisz(fig, "rzut_idealny")

# 2. Energia i prędkość
Ek = 0.5 * m * (vx**2 + vy**2)
Ep = m * g * y
Ec = Ek + Ep

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), layout="constrained")
axes[0].plot(t, Ek, color=ORANGE, label="Kinetyczna Ek")
axes[0].plot(t, Ep, color=BLUE, label="Potencjalna Ep")
axes[0].plot(t, Ec, color=GREEN, ls="--", label="Całkowita E")
axes[0].set(xlabel="Czas t [s]", ylabel="Energia [J]", title="Przemiany energii")
axes[0].legend(fontsize=9)
axes[1].plot(t, vx, color=PURPLE, label="vx(t) = const")
axes[1].plot(t, vy, color=ORANGE, label="vy(t)")
axes[1].axhline(0, color=INK, lw=0.8, alpha=0.5)
axes[1].set(xlabel="Czas t [s]", ylabel="Prędkość [m/s]", title="Składowe prędkości")
axes[1].legend()
zapisz(fig, "energia_i_predkosc")

# 3. Rzut z oporem
def symuluj_opor(c):
    def rhs(czas, stan):
        xx, yy, vxx, vyy = stan
        v = np.hypot(vxx, vyy)
        return [vxx, vyy, -(c/m)*v*vxx, -g - (c/m)*v*vyy]
    def stop(czas, stan): return stan[1]
    stop.terminal, stop.direction = True, -1
    sol = solve_ivp(rhs, (0, 20), [0, 0, vx0, vy0], events=stop, max_step=0.01)
    return sol.y[0], sol.y[1], sol.y[2], sol.y[3], sol.t

fig, ax = plt.subplots(figsize=(10, 4.6), layout="constrained")
ax.plot(x, y, color=BLUE, ls="--", label="Bez oporu (c = 0)")
for c_val, col, opis in [
    (0.015, GREEN, "Słaby opór (c = 0.015 kg/m)"),
    (0.050, ORANGE, "Średni opór (c = 0.050 kg/m)"),
    (0.120, PURPLE, "Silny opór (c = 0.120 kg/m)")
]:
    xo, yo, _, _, _ = symuluj_opor(c_val)
    ax.plot(xo, yo, color=col, label=f"{opis} | Z = {xo[-1]:.1f} m")
ax.set(xlabel="Zasięg x [m]", ylabel="Wysokość y [m]", title="Wpływ oporu aerodynamicznego")
ax.legend()
zapisz(fig, "porownanie_oporu")

# 4. Portret fazowy
xo_sredni, yo_sredni, _, vyo_sredni, _ = symuluj_opor(0.050)
fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")
ax.plot(y, vy, color=BLUE, ls="--", label="Bez oporu")
ax.plot(yo_sredni, vyo_sredni, color=ORANGE, label="Z oporem (c = 0.050 kg/m)")
ax.axhline(0, color=INK, lw=0.8, alpha=0.5)
ax.set(xlabel="Wysokość y [m]", ylabel="Prędkość pionowa vy [m/s]", title="Portret fazowy (y, vy)")
ax.legend()
zapisz(fig, "portret_fazowy")