import numpy as np
import matplotlib.pyplot as plt

# Parametry spersonalizowane
v0 = 33.0  # m/s
alpha_deg = 45.0
alpha = np.radians(alpha_deg)
g = 9.81

# 1. Rzut ukośny BEZ oporu powietrza
t_max = (2 * v0 * np.sin(alpha)) / g
t = np.linspace(0, t_max, 500)
x_no_drag = v0 * np.cos(alpha) * t
y_no_drag = v0 * np.sin(alpha) * t - 0.5 * g * t**2

# Wykres bez oporu
plt.figure(figsize=(8, 4))
plt.plot(x_no_drag, y_no_drag, label='Rzut bez oporu', color='blue')
plt.title('Rzut ukośny bez oporu powietrza (v0 = 33 m/s, alfa = 45°)')
plt.xlabel('Zasięg x [m]')
plt.ylabel('Wysokość y [m]')
plt.grid(True)
plt.legend()
plt.savefig('wykres_bez_oporu.png', bbox_inches='tight', dpi=300)
plt.close()

# 2. Rzut ukośny Z oporem powietrza (metoda numeryczna)
dt = 0.001
k = 0.05  # współczynnik oporu
x_list, y_list = [0.0], [0.0]
vx = v0 * np.cos(alpha)
vy = v0 * np.sin(alpha)
x, y = 0.0, 0.0

while y >= 0:
    v = np.sqrt(vx**2 + vy**2)
    ax = -k * v * vx
    ay = -g - k * v * vy
    
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    
    if y >= 0:
        x_list.append(x)
        y_list.append(y)

# Wykres z oporem
plt.figure(figsize=(8, 4))
plt.plot(x_no_drag, y_no_drag, label='Bez oporu', color='blue', linestyle='--')
plt.plot(x_list, y_list, label='Z oporem powietrza', color='red')
plt.title('Porównanie rzutu ukośnego z oporem i bez oporu')
plt.xlabel('Zasięg x [m]')
plt.ylabel('Wysokość y [m]')
plt.grid(True)
plt.legend()
plt.savefig('wykres_z_oporem.png', bbox_inches='tight', dpi=300)
plt.close()

print("Wykresy zostały wygenerowane pomyślnie!")