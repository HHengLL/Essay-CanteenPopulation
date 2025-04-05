import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 定义函数表达式
def func(x, h, σ, μ, k):
    gaussian = (1 / (σ * np.sqrt(2 * np.pi))) * np.exp(-(x - μ)**2 / (2 * σ**2))
    return (h + gaussian) * k

# 设置参数（示例值）
h = 0
σ = 4
μ = 10
k = 1000

# 定义积分区间 [a, b]
a = 0
b = 20

# ----------------------------
# 1. 使用 SciPy 计算定积分
# ----------------------------
# 对 func(x) 在区间 [a, b] 上积分
# 注意：quad 要求函数参数为 (x, h, σ, μ, k)
integral_value, error = quad(func, a, b, args=(h, σ, μ, k))

print(f"积分结果: {integral_value:.4f} (±{error:.2e})")

# ----------------------------
# 2. 绘制函数图像及积分区域
# ----------------------------
# 生成 x 值（用于绘图）
x_plot = np.linspace(a, b, 500)
y_plot = func(x_plot, h, σ, μ, k)

# 创建画布和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制总人数准线
plt.axhline(y=1000, color='black', linestyle='--', linewidth=1.5, label='BorderLine')

# 绘制 func(x) 曲线
ax.plot(x_plot, y_plot, label=f'func(x): h={h}, σ={σ}, μ={μ}, k={k}', color='blue')

# 填充积分区域（可视化积分结果）
ax.fill_between(x_plot, y_plot, alpha=0.2, color='blue', label=f'IntArea ≈ {integral_value:.2f}')

# ----------------------------
# 3. 绘制第二条函数（例如累积积分曲线）
# ----------------------------
# 定义累积积分函数：从 a 到 x 的积分
def cumulative_integral(x):
    return np.array([quad(func, a, xi, args=(h, σ, μ, k))[0] for xi in x])

# 计算累积积分值（注意：此步骤较慢，需逐点计算）
y_cumulative = cumulative_integral(x_plot)

# 绘制累积积分曲线
ax.plot(x_plot, y_cumulative, label='IntCurve', color='red', linestyle='--')

# 添加标签和图例
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('func(x) and its Integral curve')
ax.legend()

# 显示图像
plt.grid(True)
plt.show()