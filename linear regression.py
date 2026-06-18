# Sample data
X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(X)
sumX = sum(X)
sumY = sum(y)
sumXY = sum([X[i] * y[i] for i in range(n)])
sumX2 = sum([X[i] ** 2 for i in range(n)])

# Calculate slope (m) and intercept (b)
m = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX ** 2)
b = (sumY - m * sumX) / n

print("Slope (m):", m)
print("Intercept (b):", b)

# Predictions
print("Predicted values:")
for i in range(n):
    y_pred = m * X[i] + b
    print(f"x={X[i]} -> y={y_pred}")
