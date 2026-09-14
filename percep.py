X = [
    [1, 2],
    [1, 0],
    [0, 3],
    [2, 1],
    [2, 0]
]
y = [1, 0, 0, 1, 1]

# initialization
w1 = 0.0     
w2 = 0.0      
b = 0.0       
eta = 0.1     

# Outer Loop: Run for 10 Epochs
for epoch in range(1, 11):
    print(" Epoch", epoch, "")
    
    # Inner Loop: Go through each sample
    for i in range(len(X)):
        x1 = X[i][0]
        x2 = X[i][1]
        target = y[i]
        
        #Calculate(z)
        z = (w1 * x1) + (w2 * x2) + b
        if z >= 0:
            y_hat = 1
        else:
            y_hat = 0
            
        #Calculate Error
        error = target - y_hat
        
        #Update Weights and Bias
        w1 = w1 + (eta * error * x1)
        w2 = w2 + (eta * error * x2)
        b = b + (eta * error)
        print("Sample", i + 1, "| Target:", target, "| Predicted:", y_hat, "| Weights:", w1, w2, "| Bias:", b)

#Final Results
print("\nFinal Results After 10 Epochs:")
print("w1 =", w1)
print("w2 =", w2)
print("b =", b)
