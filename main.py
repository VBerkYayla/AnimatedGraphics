import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figures and lines
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# We take some limits on the x and y axis.
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.1, 1.1)

# It is x values
x = np.linspace(0, 2 * np.pi, 100)

# İnitial value
def init():
    line.set_data([], [])
    return line,

# We update the frame
def update(frame):
    y = np.cos(x + 2 * np.pi * frame / 100)
    line.set_data(x, y)
    return line,

# Now, we start the animation so we see the animated graphics.
ani = FuncAnimation(fig, update, init_func=init, frames=100, interval=25, blit=True)

plt.show()
