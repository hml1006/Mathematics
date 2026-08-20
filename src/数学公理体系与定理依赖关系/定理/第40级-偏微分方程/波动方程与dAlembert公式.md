# 波动方程与 d'Alembert 公式

> **一句话大白话**：一维波动方程的解就是"两列波，一左一右、原样跑开"的拼接——弦上的任何扰动都分解成一列向左、一列向右，速度固定，互不干扰。
>
> **小例子**：$u_{tt}=c^2u_{xx}$ 的解写作 $u(t,x)=F(x-ct)+G(x+ct)$；d'Alembert 公式用初值 $u(0,x),\partial_tu(0,x)$ 定出 $F,G$，如初始静止时 $u(t,x)=\tfrac12[\phi(x-ct)+\phi(x+ct)]$。

## 介绍

波动方程 $u_{tt} = c^2 \Delta u$ 是描述振动和波传播现象的基本双曲型偏微分方程。d'Alembert 公式给出了波动方程在一维情形的显式解，由法国数学家 Jean le Rond d'Alembert 在 1747 年发现。该公式揭示了波沿特征线传播的本质，是理解波动方程特征理论和 Huygens 原理的基础。

## 分析

**前置依赖**：特征线法、二阶线性 PDE、叠加原理、Fourier 变换、球面平均法。

**定理内容**：一维波动方程 Cauchy 问题
$$\begin{cases}
u_{tt} - c^2 u_{xx} = 0, & x \in \mathbb{R}, t > 0 \\
u(x,0) = \varphi(x), & u_t(x,0) = \psi(x)
\end{cases}$$
的解由 d'Alembert 公式给出：
$$u(x,t) = \frac{\varphi(x+ct) + \varphi(x-ct)}{2} + \frac{1}{2c} \int_{x-ct}^{x+ct} \psi(y) \, dy$$

**对三维波动方程**：三维波动方程 $u_{tt} = c^2 \Delta u$ 的 Cauchy 问题解由 Kirchhoff 公式给出：
$$u(x,t) = \frac{1}{4\pi c^2 t^2} \int_{\partial B(x,ct)} \varphi(y) \, dS(y) + \frac{1}{4\pi c^2 t} \int_{\partial B(x,ct)} \psi(y) \, dS(y)$$

**数学内涵**：d'Alembert 公式表明：
- 解由初始位移 $\varphi$ 和初始速度 $\psi$ 共同决定。
- 波沿特征线 $x \pm ct = \text{const}$ 传播，传播速度为 $c$。
- 一维波有"后尾"效应（Huygens 原理在奇数维 $n \ge 3$ 成立，在一维不成立）。

**证明策略**：一维情形通过将波动方程分解为两个一阶输运方程（特征分解）或直接通过变量代换 $\xi = x+ct$，$\eta = x-ct$ 化为标准型求解。

## 思考过程

波动方程 $u_{tt} = c^2 u_{xx}$ 的特征线为 $x \pm ct = \text{const}$。引入特征坐标 $\xi = x+ct$，$\eta = x-ct$，则方程化为
$$u_{\xi\eta} = 0$$
这可以通过链式法则验证。积分两次得 $u = f(\xi) + g(\eta) = f(x+ct) + g(x-ct)$，其中 $f,g$ 是任意光滑函数。代入初值条件即可解出 $f,g$，得到 d'Alembert 公式。

物理上，$f(x+ct)$ 表示向左传播的波，$g(x-ct)$ 表示向右传播的波。d'Alembert 公式表明，初始位移分裂为左右两半传播，初始速度的效应则通过积分体现。

## 证明过程

**定理**（d'Alembert 公式）：一维波动方程 Cauchy 问题的解由 d'Alembert 公式给出。

**证明**：

**步骤 1**：特征分解。作变量代换
$$\xi = x + ct,\quad \eta = x - ct$$
则 $u(x,t) = v(\xi,\eta)$。由链式法则：
$$u_x = v_\xi + v_\eta,\quad u_{xx} = v_{\xi\xi} + 2v_{\xi\eta} + v_{\eta\eta}$$
$$u_t = c(v_\xi - v_\eta),\quad u_{tt} = c^2(v_{\xi\xi} - 2v_{\xi\eta} + v_{\eta\eta})$$
代入波动方程 $u_{tt} = c^2 u_{xx}$ 得
$$c^2(v_{\xi\xi} - 2v_{\xi\eta} + v_{\eta\eta}) = c^2(v_{\xi\xi} + 2v_{\xi\eta} + v_{\eta\eta})$$
化简得 $v_{\xi\eta} = 0$。

**步骤 2**：求解 $v_{\xi\eta} = 0$。先对 $\eta$ 积分得 $v_\xi = f'(\xi)$，再对 $\xi$ 积分得
$$v(\xi,\eta) = f(\xi) + g(\eta)$$
其中 $f,g$ 是任意光滑函数。因此
$$u(x,t) = f(x+ct) + g(x-ct)$$

**步骤 3**：代入初值条件。在 $t=0$ 时，
$$u(x,0) = f(x) + g(x) = \varphi(x)$$
$$u_t(x,0) = cf'(x) - cg'(x) = \psi(x)$$

**步骤 4**：求解 $f,g$。对第二式积分得
$$f(x) - g(x) = \frac{1}{c} \int_0^x \psi(y) \, dy + C$$
联立第一式解得
$$f(x) = \frac{1}{2}\varphi(x) + \frac{1}{2c} \int_0^x \psi(y) \, dy + \frac{C}{2}$$
$$g(x) = \frac{1}{2}\varphi(x) - \frac{1}{2c} \int_0^x \psi(y) \, dy - \frac{C}{2}$$

**步骤 5**：代入 $u(x,t) = f(x+ct) + g(x-ct)$ 得
$$u(x,t) = \frac{\varphi(x+ct) + \varphi(x-ct)}{2} + \frac{1}{2c} \int_{x-ct}^{x+ct} \psi(y) \, dy$$
其中常数 $C$ 相互抵消。$\square$

**推论**（依赖区间与影响区域）：
- 点 $(x,t)$ 的解依赖于初始区间 $[x-ct, x+ct]$ 上的数据，称为依赖区间。
- 初始点 $x_0$ 处的数据影响区域 $\{(x,t) \mid |x-x_0| \le ct\}$，即特征锥。
- 波以有限速度 $c$ 传播，这体现了双曲型方程的特征性质。