from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
# Function Expression
def func(x):
    return (h + (1 / (σ * np.sqrt(2 * np.pi)) * np.exp(-(x - μ)**2 / (2 * σ**2))) ) * k

# Variables
k = 200
h = 0
σ = 3
μ = 10

#numpy
x = np.linspace(0,20,1000)

integral = np.trapz(func(x),x)
print(integral)

plt.figure(figsize=(8, 4))  # 设置图像大小
plt.plot(x,func(x),label="f(x)", color="blue", linewidth=2)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of Population Distribution")
plt.legend()  # 显示图例
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()