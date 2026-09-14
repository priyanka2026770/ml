# 1. Dataset setup
X = [
    [1, 2],
    [1, 0],
    [0, 3],
    [2, 1],
    [2, 0]
]
y = [1, 0, 0, 1, 1]

# 2. Parameter initialization
w1 = 0.0
w2 = 0.0
b = 0.0
eta = 0.1

# 3. Training loop (10 Epochs)
for epoch in range(1, 11):
    for i in range(len(X)):
        x1 = X[i][0]
        x2 = X[i][1]
        target = y[i]

        # Calculate net input (z) and prediction
        z = (w1 * x1) + (w2 * x2) + b
        y_hat = 1 if z >= 0 else 0

        # Calculate error and update parameters
        error = target - y_hat
        w1 = w1 + (eta * error * x1)
        w2 = w2 + (eta * error * x2)
        b = b + (eta * error)

print(f"Final Weights: w1 = {w1:.2f}, w2 = {w2:.2f}")
print(f"Final Bias: b = {b:.2f}\n")

# ---------------------------------------------------------
# 4. Terminal-Based ASCII Graph (Pure Python)
# ---------------------------------------------------------
# Define grid dimensions for plotting
y_min, y_max = -1, 4
x_min, x_max = -1, 4

print("=== PERCEPTRON GRAPH IN TERMINAL ===")
print("O = Class 1 | X = Class 0 | / = Decision Boundary | . = Empty\n")

# Render row by row (from top y to bottom y)
for x2 in range(y_max, y_min - 1, -1):
    row_str = f"{x2:2d} | "
    for x1 in range(x_min, x_max + 1):
        char = " . "
        
        # 1. Check if a dataset point exists at (x1, x2)
        point_found = False
        for i in range(len(X)):
            if X[i][0] == x1 and X[i][1] == x2:
                char = " O " if y[i] == 1 else " X "
                point_found = True
                break
        
        # 2. If no data point, check if boundary line passes near this grid cell
        if not point_found and w2 != 0:
            # Calculate boundary line value x2_line = -(w1*x1 + b)/w2
            x2_line = -(w1 * x1 + b) / w2
            if abs(x2 - x2_line) < 0.6:
                char = " / "
                
        row_str += char
    print(row_str)

# Print x-axis border and labels
print("     " + "-" * 21)
print("      " + "  ".join(str(x) for x in range(x_min, x_max + 1)))
print("x2 ^")
print("   +---> x1")