# Cauchy-Riemann 方程

## 介绍

Cauchy-Riemann 方程（柯西-黎曼方程）是复分析中最基本的判别条件，给出了复变函数可微（解析）的充要条件。该方程由 d'Alembert 在 18 世纪中期研究流体力学时首次发现，后由 Cauchy 和 Riemann 系统发展，成为复分析理论的基石。它在复变函数的可微性判定、共形映射、调和函数等研究中具有核心地位。

## 分析

**前置依赖**：偏导数定义、复变函数概念

**定理内容**：设复变函数 $f(z)=u(x,y)+iv(x,y)$ 在区域 $D$ 内有定义，其中 $z=x+iy$，$u,v$ 是实值函数。则 $f$ 在 $z_0=x_0+iy_0$ 处可微（解析）当且仅当 $u,v$ 在 $(x_0,y_0)$ 处可微且满足 Cauchy-Riemann 方程
$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$$

**数学内涵**：Cauchy-Riemann 方程反映了复可微与实可微的本质区别。复可微要求极限 $\lim_{\Delta z\to 0}(f(z_0+\Delta z)-f(z_0))/\Delta z$ 与 $\Delta z$ 趋近于 $0$ 的方向无关。这一条件等价于 $f$ 作为映射 $\mathbb{R}^2\to\mathbb{R}^2$ 的 Jacobi 矩阵具有 $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ 的特殊形式，对应复数的乘法结构。

**证明策略**：从复导数定义出发，分别令 $\Delta z$ 沿实轴方向（$\Delta y=0$）和虚轴方向（$\Delta x=0$）趋近于零，比较两个极限表达式，得到 C-R 方程。

## 思考过程

复可微比实可微要求更强：实可微只要求函数在一点附近可被线性逼近，而复可微还要求这个线性逼近是复线性的（即乘以一个复数）。复线性变换在 $\mathbb{R}^2$ 中对应的是旋转加缩放，其 Jacobi 矩阵必须满足 C-R 方程。换言之，C-R 方程保证了 $f$ 在无穷小尺度上是一个共形映射（保角变换）。

## 证明过程

**定理**：设 $f(z)=u(x,y)+iv(x,y)$ 在区域 $D$ 内有定义，则 $f$ 在 $z_0=x_0+iy_0$ 处可微当且仅当 $u,v$ 在 $(x_0,y_0)$ 处可微且满足
$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$$

**证明**：

**必要性**：设 $f$ 在 $z_0$ 处可微，导数为 $f'(z_0)$。令 $\Delta z=\Delta x+i\Delta y$，则
$$f'(z_0)=\lim_{\Delta z\to 0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}$$

先取 $\Delta z$ 沿实轴方向（$\Delta y=0$，$\Delta x\to 0$）：
$$f'(z_0)=\lim_{\Delta x\to 0}\frac{u(x_0+\Delta x,y_0)-u(x_0,y_0)}{\Delta x}+i\lim_{\Delta x\to 0}\frac{v(x_0+\Delta x,y_0)-v(x_0,y_0)}{\Delta x}=\frac{\partial u}{\partial x}+i\frac{\partial v}{\partial x}$$

再取 $\Delta z$ 沿虚轴方向（$\Delta x=0$，$\Delta y\to 0$）：
$$f'(z_0)=\lim_{\Delta y\to 0}\frac{u(x_0,y_0+\Delta y)-u(x_0,y_0)}{i\Delta y}+i\lim_{\Delta y\to 0}\frac{v(x_0,y_0+\Delta y)-v(x_0,y_0)}{i\Delta y}$$

由于 $1/i=-i$，化简得
$$f'(z_0)=-i\frac{\partial u}{\partial y}+\frac{\partial v}{\partial y}=\frac{\partial v}{\partial y}-i\frac{\partial u}{\partial y}$$

比较实部和虚部：
$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad \frac{\partial v}{\partial x}=-\frac{\partial u}{\partial y}$$

即得 C-R 方程。

**充分性**：设 $u,v$ 在 $(x_0,y_0)$ 处可微且满足 C-R 方程。由可微性，
$$\Delta u=\frac{\partial u}{\partial x}\Delta x+\frac{\partial u}{\partial y}\Delta y+\varepsilon_1,\quad \Delta v=\frac{\partial v}{\partial x}\Delta x+\frac{\partial v}{\partial y}\Delta y+\varepsilon_2$$
其中 $\varepsilon_1,\varepsilon_2=o(|\Delta z|)$。利用 C-R 方程，可得
$$\frac{\Delta f}{\Delta z}=\frac{\partial u}{\partial x}+i\frac{\partial v}{\partial x}+\frac{\varepsilon_1+i\varepsilon_2}{\Delta z}$$
取极限 $\Delta z\to 0$ 即得 $f'(z_0)$ 存在。

$\square$