import numpy as np
import matplotlib.pyplot as plt

# Define parameters
a = 0.1  # Example value for 'a'
num_steps = 20000  # Number of time steps

# Initialize arrays for x, y, z
x = np.zeros(num_steps)
y = np.zeros(num_steps)
z = np.zeros(num_steps)

# Set initial conditions
x[0] = 0.01  # Initial condition for x
y[0] = 1.0  # Initial condition for y
z[0] = 1.0  # Initial condition for z

# Iterate to compute the values at each time step
for t in range(num_steps - 1):
    x[t + 1] = -y[t]
    y[t + 1] = -z[t]
    z[t + 1] = a * y[t] + np.sin(x[t])

# Focus on the last 3000 points
x_last = x[-500:]
y_last = y[-500:]
z_last = z[-500:]

# Create a 2D plot in the x-z plane
plt.figure(figsize=(8, 6))
plt.plot(x_last, z_last, lw=0.5)
plt.xlabel('X')
plt.ylabel('Z')
plt.title('Phase Space (X-Z Plane) - Last 3000 Points')
plt.grid(True)
plt.show()

#new comment added