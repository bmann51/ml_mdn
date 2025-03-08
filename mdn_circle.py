import matplotlib.pyplot as plt
import numpy as np

num_samples = 200

# Generate sample data
x = np.random.uniform(-1, 1, num_samples)

# Noise
noise_mean = 0     
noise_std_dev = 0.1
noise = np.random.normal(noise_mean, noise_std_dev, num_samples)


sign = np.random.choice([-1, 1], num_samples)
y = sign * np.sqrt(1-x**2) + noise


# Create a plot
plt.scatter(x, y, label='circle', color='b')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter of Noisy Circle')

# Show the plot
plt.show()
