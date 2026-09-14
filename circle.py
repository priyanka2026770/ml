import math

# 1. Ask the user how many points to enter
n = int(input("How many points do you want to enter? "))

# 2. Collect points dynamically after running the code
data = []
print("Enter your points as 'x, y' (e.g., 3.5, -2.1):")
for i in range(n):
    point_str = input(f"Point {i + 1}: ")
    x, y = map(float, point_str.split(','))
    data.append([x, y])

# 3. Find the centroid (mean X and mean Y)
mean_x = sum(p[0] for p in data) / len(data)
mean_y = sum(p[1] for p in data) / len(data)

# 4. Center points around origin (0, 0)
centered_data = [[p[0] - mean_x, p[1] - mean_y] for p in data]

# 5. Find maximum distance from origin
max_distance = max(math.hypot(p[0], p[1]) for p in centered_data)

# 6. Scale all points inside unit circle (r <= 1)
fitted_data = [[p[0] / max_distance, p[1] / max_distance] for p in centered_data]

# Output results
print("\n--- Fitted Points inside Unit Circle ---")
for i, point in enumerate(fitted_data):
    print(f"Point {i + 1}: [{point[0]:.4f}, {point[1]:.4f}]")

import matplotlib.pyplot as plt

# Extract x and y coordinates
x_vals = [p[0] for p in fitted_data]
y_vals = [p[1] for p in fitted_data]

# Plot points
plt.figure(figsize=(6, 6))
plt.scatter(x_vals, y_vals, color='blue', label='Fitted Points')

# Draw unit circle boundary (r = 1)
circle = plt.Circle((0, 0), 1, color='red', fill=False, linestyle='--', label='Unit Circle (r=1)')
plt.gca().add_patch(circle)

# Adjust axes limits and aspect ratio
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.gca().set_aspect('equal')
plt.grid(True)
plt.legend()
plt.show()