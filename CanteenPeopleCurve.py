from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# Function expression
def func(x):
    return (h + (1 / (σ * np.sqrt(2 * np.pi)) * np.exp(-(x - μ)**2 / (2 * σ**2))) ) * k

# Variables
h = 0.001
σ = 6
μ = 18
k = 1000

# Range
lowValue = 0
highValue = 30

# Integral value calculate
integralValue, error = quad(func, lowValue, highValue)
print(f"Integral value between 0 - 30: {integralValue:.4f} (error:±{error:.2e})")

# Integrate every 30s
print("Segmental Integral value every 30':")
lowRange = float(0)
highRange = float(0.5)
for i in range(0,60):
    segIntegral, segError = quad(func, lowRange, highRange)
    lowRange = lowRange + 0.5
    highRange = highRange + 0.5
    print(f"Range between {lowRange} and {highRange}: {segIntegral:.4f} (error:±{segError:.2e})")

# Generate X values
x_plot = np.linspace(lowValue, highValue, 500)
y_plot = func(x_plot)

# Canva and axis
fig, ax = plt.subplots(figsize=(10, 6))

# BorderLine of total population
plt.axhline(y=1000, color="black", linestyle="--", linewidth=1.5, label="BorderLine")

# Curve of Function
ax.plot(x_plot, y_plot, label=f"func(x): h={h}, σ={σ}, μ={μ}, k={k}", color="blue")

# Integral Curve & Area
def cumulative_integral(x):
    return np.array([quad(func, lowValue, xi)[0] for xi in x])
y_cumulative = cumulative_integral(x_plot)

ax.plot(x_plot, y_cumulative, label="IntCurve", color="red", linestyle="--")
ax.fill_between(x_plot, y_plot, alpha=0.2, color="blue", label=f"IntArea ≈ {integralValue:.2f}")

# Canva output
ax.set_xlabel("Time")
ax.set_ylabel("Population")
ax.set_title("Graph of people distribute by time")
ax.legend()
plt.grid(True)
plt.show()