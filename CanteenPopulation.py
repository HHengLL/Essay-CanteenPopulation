from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# Function expression
def func(x):
    return (h + (1 / (σ * np.sqrt(2 * np.pi)) * np.exp(-(x - μ)**2 / (2 * σ**2))) ) * k

# Variables
h = 0
σ = 4
μ = 15
k = 1000

# Range
lowValue = 0
highValue = 30

# Integral
integral_value, error = quad(func, lowValue, highValue)
print(f"Integral value between 0 - 30: {integral_value:.4f} (error:±{error:.2e})")

# Generate X values
x_plot = np.linspace(lowValue, highValue, 500)
y_plot = func(x_plot)

# Canva and axis
fig, ax = plt.subplots(figsize=(10, 6))

# BorderLine of total population
plt.axhline(y=1000, color='black', linestyle='--', linewidth=1.5, label='BorderLine')

# Curve of Function
ax.plot(x_plot, y_plot, label=f'func(x): h={h}, σ={σ}, μ={μ}, k={k}', color='blue')

# Integral Curve & Area
def cumulative_integral(x):
    return np.array([quad(func, lowValue, xi)[0] for xi in x])
y_cumulative = cumulative_integral(x_plot)

ax.plot(x_plot, y_cumulative, label='IntCurve', color='red', linestyle='--')
ax.fill_between(x_plot, y_plot, alpha=0.2, color='blue', label=f'IntArea ≈ {integral_value:.2f}')

# Canva output
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('func(x) and its Integral curve')
ax.legend()
plt.grid(True)
plt.show()