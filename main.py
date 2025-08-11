import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Figure ve line oluşturma
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Eksen limitleri
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)

# X değerleri
x = np.linspace(0, 2 * np.pi, 100)

# Başlangıç fonksiyonu
def init():
    line.set_data([], [])
    return line,

# Frame güncelleme fonksiyonu
def update(frame):
    y = np.cos(x + 2 * np.pi * frame / 100)
    line.set_data(x, y)
    return line,

# Animasyonu başlat
ani = FuncAnimation(fig, update, init_func=init, frames=100, interval=25, blit=True)

plt.show()
