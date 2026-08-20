# Zeta函数函数方程

> **一句话大白话**：$\zeta$ 函数不只定义在 $\mathrm{Re}\,s>1$ 的级数里，通过一个对称式（交换 $s\leftrightarrow 1-s$）就能解析延拓到整个复平面，且在 $s=1/2$ 左右手完全对称。
>
> **小例子**：$\xi(s)=\dfrac12s(s-1)\pi^{-s/2}\Gamma\!\left(\dfrac{s}{2}\right)\zeta(s)$ 满足 $\xi(s)=\xi(1-s)$，正是这个 $\xi$ 的零点等价于 $\zeta$ 在临界带的零点。

## 介绍

Riemann Zeta 函数的函数方程是 $\zeta(s)$ 在复平面上的基本对称性，由 Riemann 在其 1859 年的论文中证明。函数方程将 $\zeta(s)$ 与 $\zeta(1-s)$ 联系起来，从而将右半平面 $\operatorname{Re}(s) > 1$ 上的信息反射到左半平面 $\operatorname{Re}(s) < 0$。结合解析延拓，函数方程是研究 Zeta 函数零点分布和素数定理的关键工具。

## 分析

**前置依赖**：Riemann Zeta 函数、Gamma 函数、解析延拓、余元公式。

**定理内容**：对 $s \in \mathbb{C}\setminus\{0, 1\}$，
$$\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s)$$

等价形式（对称形式）：
$$\xi(s) = \frac{1}{2} s(s-1) \pi^{-s/2} \Gamma\left(\frac{s}{2}\right) \zeta(s)$$
满足 $\xi(s) = \xi(1-s)$。

**数学内涵**：
- 函数方程揭示了 $\zeta(s)$ 关于直线 $\operatorname{Re}(s) = 1/2$ 的对称性。
- 结合 $\zeta(s)$ 在 $s = -2, -4, -6, \ldots$ 处的平凡零点可由 $\sin(\pi s/2)$ 因子直接看出。
- 非平凡零点关于 $\operatorname{Re}(s) = 1/2$ 对称分布。

**证明策略**：
1. 利用 Jacobi theta 函数 $\theta(x) = \sum_{n=-\infty}^\infty e^{-\pi n^2 x}$ 的变换公式 $\theta(x) = \frac{1}{\sqrt{x}} \theta(1/x)$。
2. 将 $\zeta(s)$ 表示为 Mellin 变换 $\zeta(s) = \frac{1}{\Gamma(s)} \int_0^\infty \frac{x^{s-1}}{e^x - 1} dx$。
3. 通过围道积分或 Poisson 求和公式推导函数方程。

## 思考过程

函数方程是 $\zeta(s)$ 最深刻的性质之一。它表明 $\zeta(s)$ 在 $s$ 和 $1-s$ 处的值由 Gamma 因子和三角因子相关联。这种对称性来源于 theta 函数的模性质，反映了整数点格在傅里叶变换下的自对偶性。

Riemann 引入的 $\xi(s)$ 函数是整函数，其零点恰好是 $\zeta(s)$ 的非平凡零点。$\xi(s) = \xi(1-s)$ 的对称性使得这些零点关于 $\operatorname{Re}(s) = 1/2$ 对称分布——这正是 Riemann 假设的几何背景。

## 证明过程

**定理**（函数方程）：对 $s \in \mathbb{C}\setminus\{0, 1\}$，
$$\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s)$$

**证明**：

### 1. Theta 函数变换

定义 Jacobi theta 函数 $\theta(x) = \sum_{n=-\infty}^\infty e^{-\pi n^2 x}$，$x > 0$。由 Poisson 求和公式，
$$\theta(x) = \frac{1}{\sqrt{x}} \theta\left(\frac{1}{x}\right)$$

### 2. 积分表示

定义 $\psi(x) = \sum_{n=1}^\infty e^{-\pi n^2 x}$，则 $\theta(x) = 1 + 2\psi(x)$，变换公式给出：
$$2\psi(x) + 1 = \frac{1}{\sqrt{x}}(2\psi(1/x) + 1)$$

### 3. 与 Zeta 函数的联系

利用 Gamma 函数的积分表示：
$$\pi^{-s/2} \Gamma\left(\frac{s}{2}\right) \zeta(s) = \int_0^\infty x^{s/2-1} \psi(x) dx$$

将积分拆分为 $[0, 1]$ 和 $[1, \infty)$，对 $[0, 1]$ 部分应用 $\psi$ 的变换公式，得到：
$$\int_0^1 x^{s/2-1} \psi(x) dx = \frac{1}{s-1} - \frac{1}{s} + \int_1^\infty x^{-s/2-1/2} \psi(x) dx$$

### 4. 对称形式

代入得：
$$\pi^{-s/2} \Gamma\left(\frac{s}{2}\right) \zeta(s) = \frac{1}{s(s-1)} + \int_1^\infty (x^{s/2-1/2} + x^{-s/2}) \psi(x) \frac{dx}{x}$$

右边在 $s \mapsto 1-s$ 下不变，故
$$\xi(s) := \frac{1}{2} s(s-1) \pi^{-s/2} \Gamma\left(\frac{s}{2}\right) \zeta(s) = \xi(1-s)$$

### 5. 导出标准形式

利用 Gamma 函数的倍角公式和余元公式，从 $\xi(s) = \xi(1-s)$ 导出：
$$\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s)$$

$\square$

**推论**：$\zeta(s)$ 在 $s = -2, -4, -6, \ldots$ 处有零点（平凡零点），且 $\zeta(-2n) = 0$。

**证明**：由函数方程，$\sin(\pi s/2)$ 因子在 $s = -2n$ 处为零，且 $\Gamma(1-s)$ 无极点，故 $\zeta(-2n) = 0$。$\square$