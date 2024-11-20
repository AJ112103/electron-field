import numpy as np
import matplotlib.pyplot as plt

q = 1.6e-19       # Charge of the particle (Coulombs)
m = 9.11e-31      # Mass of the particle (kg)
B = 1.0           # Magnetic field strength (Tesla)
v = 1e6           # Initial speed of the particle (m/s)
theta = np.pi / 4 # Angle between velocity and magnetic field (radians)

num_points = 1000     # Number of points for the plot
time_end = 2e-7       # Total simulation time (seconds)
t = np.linspace(0, time_end, num_points)  # Time array

v_parallel = v * np.sin(theta)  # Parallel to B
v_perpendicular = v * np.cos(theta)  # Perpendicular to B

omega = q * B / m  # Angular frequency (rad/s)

# Radius of the circular motion
radius = m * v_perpendicular / (q * B)

x = radius * np.cos(omega * t)       # x-coordinate
z = radius * np.sin(omega * t)       # z-coordinate
y = v_parallel * t                   # y-coordinate (linear motion)

fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection='3d')

ax.plot3D(x, y, z, label='Helical Path', color='blue')
ax.set_title('Helical Path of Charged Particle in Magnetic Field', fontsize=14)
ax.set_xlabel('X (m)', fontsize=12)
ax.set_ylabel('Y (m)', fontsize=12)
ax.set_zlabel('Z (m)', fontsize=12)
ax.legend()

plt.show()
