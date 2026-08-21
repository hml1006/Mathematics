# Runge-Kutta方法稳定性

> **一句话大白话**：把微分方程用多步"加权斜率"递推（Runge-Kutta），前提是别让数值越算越炸——稳定性保证了用合适步长（通常受ODE刚度限制）时误差不放大，像掌舵确保小船不翻。
>
> **小例子**：对 $y'=\lambda y$ 用前向欧拉，需步长 $h$ 满足 $|1+\lambda h|\le1$（稳定区）；而隐式RK可无条件稳定；步长超了稳定域，误差就会随步数"指数爆走"。

## 介绍

Runge-Kutta方法（Runge–Kutta Methods）是求解常微分方程初值问题 $y' = f(t, y)$ 最广泛使用的一类数值方法。Runge-Kutta方法通过在每一步内计算多个中间阶段的斜率来获得高阶精度，其经典形式包括 RK4（四阶 Runge-Kutta）。Runge-Kutta方法的稳定性分析是数值分析的关键内容，它决定了方法在求解刚性方程时的适用性。稳定性分析通常通过将方法应用于线性测试方程 $y' = \lambda y$（$\lambda \in \mathbb{C}$）来研究，得到稳定性函数 $R(z)$ 和稳定性区域。

## 分析

**前置依赖**：常微分方程初值问题、Runge-Kutta 方法与 Butcher 表、线性测试方程 $y'=\lambda y$、$e^z$ 的 Padé 逼近、$A$-稳定性与 $L$-稳定性概念。

**定义**：将 Runge-Kutta 方法应用于测试方程 $y' = \lambda y$，$y(0) = 1$，得到 $y_{n+1} = R(h\lambda) y_n$，其中 $R(z)$ 是方法的**稳定性函数**。方法的**绝对稳定性区域**为 $\{z \in \mathbb{C} : |R(z)| \le 1\}$。

**常见 Runge-Kutta 方法的稳定性函数**：
- **显式 Euler**：$R(z) = 1 + z$。
- **经典 RK4**：$R(z) = 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24}$。
- **隐式 Euler**：$R(z) = \frac{1}{1-z}$，$A$-稳定。
- **隐式中点法**：$R(z) = \frac{1+z/2}{1-z/2}$，$A$-稳定。
- **Gauss-Legendre 方法**（$s$ 级）：$R(z) = \frac{P_s(z)}{P_s(-z)}$，其中 $P_s$ 是 $s$ 次 shifted Legendre 多项式，$A$-稳定。

**依赖的概念**：常微分方程、刚性方程、稳定性函数、$A$-稳定性、$L$-稳定性。

**核心概念**：
- **$A$-稳定性**：$\{z \in \mathbb{C} : \mathrm{Re}(z) \le 0\} \subseteq S$，即左半平面包含在稳定性区域中。
- **$L$-稳定性**：$A$-稳定且 $\lim_{z \to \infty} |R(z)| = 0$。

## 思考过程

Runge-Kutta 方法的稳定性分析的核心是将非线性问题局部线性化，考虑测试方程 $y' = \lambda y$。对于刚性方程，$\lambda$ 的实部负且绝对值很大，因此要求步长 $h$ 满足 $h\lambda$ 落在稳定性区域中。

显式 Runge-Kutta 方法的稳定性区域是有界的（有限区域），因此对刚性方程需要很小的步长，计算效率低。隐式 Runge-Kutta 方法（如向后 Euler、Gauss-Legendre 方法）具有更大的稳定性区域，甚至 $A$-稳定，适合求解刚性方程。

稳定性函数 $R(z)$ 实际上是方法对 $y' = \lambda y$ 的数值解与精确解 $e^{\lambda t}$ 的比值，因此 $R(z)$ 是 $e^z$ 的有理逼近。

## 证明过程

**定理**（Runge-Kutta 方法的稳定性函数）：设 $s$ 级 Runge-Kutta 方法由 Butcher 表 $(A, b, c)$ 给出，将其应用于 $y' = \lambda y$，则 $y_{n+1} = R(h\lambda) y_n$，其中

$$
R(z) = 1 + z b^T (I - zA)^{-1} \mathbf{1},
$$

$\mathbf{1} = (1, 1, \ldots, 1)^T$。

**证明**：

**步骤 1：Runge-Kutta 方法的一般形式。**

$s$ 级 Runge-Kutta 方法为

$$
k_i = f\left(t_n + c_i h, y_n + h \sum_{j=1}^s a_{ij} k_j\right), \quad i = 1, \ldots, s,
$$
$$
y_{n+1} = y_n + h \sum_{i=1}^s b_i k_i.
$$

**步骤 2：应用于测试方程。**

对 $f(t, y) = \lambda y$，有

$$
k_i = \lambda \left(y_n + h \sum_{j=1}^s a_{ij} k_j\right), \quad i = 1, \ldots, s.
$$

写成向量形式：$k = \lambda y_n \mathbf{1} + h\lambda A k$，其中 $k = (k_1, \ldots, k_s)^T$。

**步骤 3：求解 $k$。**

整理得 $(I - h\lambda A) k = \lambda y_n \mathbf{1}$，故 $k = \lambda y_n (I - h\lambda A)^{-1} \mathbf{1}$。

**步骤 4：计算 $y_{n+1}$。**

$$
y_{n+1} = y_n + h b^T k = y_n + h\lambda y_n b^T (I - h\lambda A)^{-1} \mathbf{1} = y_n \left(1 + z b^T (I - zA)^{-1} \mathbf{1}\right),
$$

其中 $z = h\lambda$。因此 $R(z) = 1 + z b^T (I - zA)^{-1} \mathbf{1}$。$\square$

**推论**（显式 Runge-Kutta 的稳定性）：若 $A$ 是严格下三角矩阵（显式方法），则 $R(z)$ 是 $z$ 的多项式，次数不超过 $s$。因此显式 Runge-Kutta 方法的稳定性区域有界，不是 $A$-稳定的。

**推论**（隐式 Runge-Kutta 的稳定性）：若 $A$ 是满矩阵（隐式方法），$R(z)$ 是有理函数。Gauss-Legendre 方法的 $R(z)$ 是 $e^z$ 的 Padé 逼近，且是 $A$-稳定的。

**例**（RK4 的稳定性区间）：对经典 RK4，$R(z) = 1 + z + z^2/2 + z^3/6 + z^4/24$。在实轴上，$|R(z)| \le 1$ 当且仅当 $z \in [-2.785, 0]$。因此步长必须满足 $h\lambda \in [-2.785, 0]$ 对 $\lambda < 0$。