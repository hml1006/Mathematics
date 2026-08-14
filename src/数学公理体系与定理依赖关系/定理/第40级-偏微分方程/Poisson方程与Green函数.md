# Poisson 方程与 Green 函数

## 介绍

Poisson 方程 $\Delta u = f$ 是最经典的椭圆型偏微分方程之一，描述了许多物理现象中的稳态场（如静电场、引力场、温度场）。Green 函数法是求解 Poisson 方程边值问题的基本工具，其核心思想是利用点源解（即 Green 函数）和叠加原理构造任意源分布下的解。Green 函数方法不仅具有理论价值，也是数值方法（如边界元法）的基础。

## 分析

**前置依赖**：散度定理、Delta 函数、卷积、调和函数、最大值原理、Laplace 方程。

**定理内容**：考虑有界区域 $\Omega \subset \mathbb{R}^n$ 上的 Dirichlet 问题
$$\begin{cases}
-\Delta u = f, & x \in \Omega \\
u = g, & x \in \partial\Omega
\end{cases}$$
Green 函数 $G(x,y)$ 定义为对固定的 $y \in \Omega$，满足
$$\begin{cases}
-\Delta_x G(x,y) = \delta(x-y), & x \in \Omega \\
G(x,y) = 0, & x \in \partial\Omega
\end{cases}$$
其中 $\delta$ 是 Dirac Delta 函数。

则解可表示为
$$u(x) = \int_\Omega G(x,y) f(y) \, dy - \int_{\partial\Omega} \frac{\partial G}{\partial n_y}(x,y) \, g(y) \, dS_y$$

**基本解**：在 $\mathbb{R}^n$ 中，Laplace 算子的基本解为
$$\Phi(x) = \begin{cases}
-\frac{1}{2\pi}\log|x|, & n = 2 \\
\frac{1}{n(n-2)\alpha_n}\frac{1}{|x|^{n-2}}, & n \ge 3
\end{cases}$$
其中 $\alpha_n$ 是 $n$ 维单位球体积。

**数学内涵**：Green 函数方法将 PDE 边值问题转化为积分方程问题。Green 函数 $G(x,y)$ 表示在 $y$ 处的单位点源在 $x$ 处产生的响应，而积分表达式则是叠加原理的直接体现。

**证明策略**：利用散度定理（Green 第二恒等式）和 Delta 函数的筛选性质，将 PDE 转化为积分表示。然后利用基本解和边界校正函数构造 Green 函数。

## 思考过程

Green 函数法的核心思想是"基本解 + 叠加"。首先求解无界区域中点源产生的响应（基本解），然后通过边界校正（即添加调和函数使得边界条件满足）得到有界区域中的 Green 函数。

对于 Poisson 方程，基本解 $\Phi(x-y)$ 满足 $-\Delta_x \Phi(x-y) = \delta(x-y)$。利用 Green 第二恒等式：
$$\int_\Omega (u\Delta v - v\Delta u) \, dx = \int_{\partial\Omega} \left(u\frac{\partial v}{\partial n} - v\frac{\partial u}{\partial n}\right) dS$$
取 $v(y) = G(x,y)$，代入 $-\Delta u = f$ 和 $-\Delta_y G = \delta(x-y)$，即可得到积分表示公式。

## 证明过程

**定理**（Green 函数表示公式）：设 $\Omega \subset \mathbb{R}^n$ 是有界光滑区域，$u \in C^2(\overline{\Omega})$ 是 Poisson 方程 $-\Delta u = f$ 的解，则对任意 $x \in \Omega$，
$$u(x) = \int_\Omega G(x,y) f(y) \, dy - \int_{\partial\Omega} \frac{\partial G}{\partial n_y}(x,y) \, u(y) \, dS_y$$

**证明**：

**步骤 1**：Green 第二恒等式。对任意 $u,v \in C^2(\overline{\Omega})$，
$$\int_\Omega (u\Delta v - v\Delta u) \, dy = \int_{\partial\Omega} \left(u\frac{\partial v}{\partial n} - v\frac{\partial u}{\partial n}\right) dS_y$$

**步骤 2**：取 $v(y) = G(x,y)$，则 $-\Delta_y G(x,y) = \delta(x-y)$ 在 $\Omega$ 中成立，且 $G(x,y) = 0$ 在 $\partial\Omega$ 上。代入 Green 恒等式：
$$\int_\Omega [u(y)(-\delta(x-y)) - G(x,y)(-f(y))] \, dy = \int_{\partial\Omega} \left[u(y)\frac{\partial G}{\partial n_y}(x,y) - 0\right] dS_y$$

**步骤 3**：由 Delta 函数的筛选性质，$\int_\Omega u(y)\delta(x-y) \, dy = u(x)$，故
$$-u(x) + \int_\Omega G(x,y) f(y) \, dy = \int_{\partial\Omega} u(y)\frac{\partial G}{\partial n_y}(x,y) \, dS_y$$

**步骤 4**：整理得
$$u(x) = \int_\Omega G(x,y) f(y) \, dy - \int_{\partial\Omega} u(y)\frac{\partial G}{\partial n_y}(x,y) \, dS_y$$
代入 Dirichlet 边界条件 $u|_{\partial\Omega} = g$ 即得所需公式。$\square$

**定理**（Green 函数的对称性）：Green 函数是对称的，即 $G(x,y) = G(y,x)$ 对所有 $x,y \in \Omega$，$x \neq y$ 成立。

**证明**：对固定的 $x_1, x_2 \in \Omega$，取 $u(y) = G(x_1,y)$，$v(y) = G(x_2,y)$。在 $\Omega \setminus (B_\varepsilon(x_1) \cup B_\varepsilon(x_2))$ 上应用 Green 第二恒等式，令 $\varepsilon \to 0$，结合边界条件 $G|_{\partial\Omega} = 0$，即得 $G(x_1,x_2) = G(x_2,x_1)$。$\square$

**例**（半空间 $\mathbb{R}^3_+$ 上的 Green 函数）：对上半空间 $\mathbb{R}^3_+ = \{x \in \mathbb{R}^3 \mid x_3 > 0\}$，Green 函数为
$$G(x,y) = \frac{1}{4\pi|x-y|} - \frac{1}{4\pi|x - \tilde{y}|}$$
其中 $\tilde{y} = (y_1, y_2, -y_3)$ 是 $y$ 关于边界平面的反射像。$\square$