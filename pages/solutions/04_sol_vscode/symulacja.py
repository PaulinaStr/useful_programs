import numpy as np
import matplotlib.pyplot as plt

# Parametry początkowe z Twojego indeksu
v0 = 33.0  
alpha_deg = 76.0  
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