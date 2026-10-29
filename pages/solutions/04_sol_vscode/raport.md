# Raport: Symulacja rzutu ukośnego

## 1. Wstęp i założenia początkowe
Celem niniejszego raportu jest analiza ruchu ciała rzuconego ukośnie w polu grawitacyjnym Ziemi. Badany jest przypadek ruchu idealnego (w próżni, bez oporu powietrza) oraz ruchu z uwzględnieniem siły oporu powietrza.

Zgodnie z wytycznymi zadania, parametry początkowe dla mojego numeru indeksu wynoszą:
* **Prędkość początkowa ($v_0$):** [33] m/s
* **Kąt początkowy ($\alpha$):** [76]°
* **Przyspieszenie ziemskie ($g$):** $9.81\ \text{m/s}^2$

---

## 2. Model matematyczny: Rzut ukośny bez oporu powietrza

W próżni na ciało działa wyłącznie siła grawitacji. Równania ruchu w układzie kartezjańskim przyjmują postać:

$$x(t) = v_0 \cdot \cos(\alpha) \cdot t$$

$$y(t) = v_0 \cdot \sin(\alpha) \cdot t - \frac{1}{2} g t^2$$

---

## 3. Model matematyczny: Rzut ukośny z oporem powietrza

Uwzględniając siłę oporu powietrza proporcjonalną do prędkości ($\mathbf{F}_{op} = -b \mathbf{v}$), równania stają się układem równań różniczkowych, które najwygodniej rozwiązać numerycznie za pomocą Pythona.

---

## 4. Symulacja numeryczna i wykresy

Poniżej znajduje się skrypt w języku Python generujący trajektorię ruchu:

```python
import numpy as np
import matplotlib.pyplot as plt

# Parametry początkowe
v0 = 12.0  # zmień na swoje dwie pierwsze cyfry indeksu
alpha_deg = 45.0  # zmień na swoje dwie ostatnie cyfry indeksu
alpha = np.radians(alpha_deg)
g = 9.81

# Czas symulacji
t_max = (2 * v0 * np.sin(alpha)) / g
t = np.linspace(0, t_max, 500)

# Rzut bez oporu
x = v0 * np.cos(alpha) * t
y = v0 * np.sin(alpha) * t - 0.5 * g * t**2

# Wykres
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Bez oporu powietrza', color='blue')
plt.title('Tor ruchu w rzucie ukośnym')
plt.xlabel('Zasięg x [m]')
plt.ylabel('Wysokość y [m]')
plt.grid(True)
plt.legend()
plt.savefig('wykres_tor.png')
plt.show()