import matplotlib.pyplot as plt
import numpy as np

# Constants
num_samples = 200
r = 1

# Noise
noise_mean = 0     
noise_std_dev = 0.1
noise_theta = np.random.normal(noise_mean, noise_std_dev, num_samples)
noise_r = np.random.normal(noise_mean, noise_std_dev, num_samples)

theta = np.random.uniform(0, 2 * np.pi, num_samples)

# Generate x and y
x = np.cos(theta+ noise_theta) * (r + noise_r)
y = np.sin(theta+ noise_theta) * (r + noise_r)


# Create a plot
plt.scatter(x, y, label='circle', color='b')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter of Noisy Circle')

# Show the plot
plt.show()
