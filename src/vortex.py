import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import sin, cos

# --- beads2d vector field ---
class beads2d(object):
    def __init__(self):
        pass

    def sample(self, x, y, t):
        u = -2 * y + (2 * sin(t)) / 3
        v = +2 * x - (2 * cos(t)) / 3
        return u, v

# Create the field
field = beads2d()

# Grid parameters
xdim, ydim, tdim = 10, 10, 512
x = np.linspace(-2, 2, xdim)
y = np.linspace(-2, 2, ydim)
X, Y = np.meshgrid(x, y, indexing='ij')

# Precompute corelines
t_values = np.linspace(0, 2 * np.pi, tdim)
true_coreline = []
for t in t_values:
    U, V = field.sample(X, Y, t)
    speed = np.sqrt(U**2 + V**2)
    min_idx = np.argmin(speed)
    i, j = np.unravel_index(min_idx, U.shape)
    true_coreline.append([x[i], y[j], t])
true_coreline = np.array(true_coreline)

fixed_coreline = np.array([[0.0, 0.0, t] for t in t_values])

# Initial vector field at t=0
t0 = 0.0
U0, V0 = field.sample(X, Y, t0)

# Setup the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
quiver = ax.quiver(X, Y, U0, V0)
true_dot, = ax.plot([], [], 'bo', label='True Coreline')   # blue dot
fixed_dot, = ax.plot([], [], 'go', label='Fixed Coreline') # green dot

ax.set_title("Vortex Vector Field with Corelines")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(loc='upper right')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])

# Add slider
slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])
time_slider = Slider(slider_ax, 'Time (t)', 0.0, 2 * np.pi, valinit=t0)

# Update function for slider
def update(val):
    t = time_slider.val
    U, V = field.sample(X, Y, t)
    quiver.set_UVC(U, V)

    # Interpolate the corelines
    idx = np.searchsorted(t_values, t)
    if idx >= len(t_values):
        idx = len(t_values) - 1

    # Update coreline markers
    true_dot.set_data([true_coreline[idx, 0]], [true_coreline[idx, 1]])
    fixed_dot.set_data([fixed_coreline[idx, 0]], [fixed_coreline[idx, 1]])


    fig.canvas.draw_idle()

# Connect slider
time_slider.on_changed(update)

plt.show()
