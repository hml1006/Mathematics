# Morrey不等式

> **一句话大白话**：当可积指数 $p$ 超过空间维数 $n$ 时，$W^{1,p}$ 函数不仅可积，而且自动连续，甚至以确定的指数 Hölder 连续——"高出维数的那部分可积性"被兑换成了光滑性。

> **小例子**：取 $n=1$、$p=2$，则 $W^{1,2}(a,b)$ 中每个函数都是 $\gamma=\frac12$ 阶的 Hölder 连续函数：$|u(x)-u(y)|\le C|x-y|^{1/2}\|u\|_{W^{1,2}}$，这正是"导数平方可积蕴涵函数连续"的量化版本。

## 介绍

Morrey 不等式由美国数学家 Charles B. Morrey, Jr. 于 1940 年代在研究变分问题与椭圆型方程弱解的正则性时提出。"为什么弱解能是经典解"是当时的核心困惑：椭圆方程只保证 $u\in W^{1,2}$，但物理上期待连续甚至光滑的解。Morrey 发现，若空间维数 $n<p$（即 Sobolev 嵌入的次临界情形），那么 $W^{1,p}$ 中的函数可以逐点定义且 Hölder 连续，从而弱解自动成为经典解。这条不等式把"可积性"与"连续性"这两个看似无关的概念用一个指数 $\gamma=1-n/p$ 定量地联系起来，是 Sobolev 嵌入定理最精细的一支。它的意义在于给出正则性与可积指数之间的换算公式，是椭圆正则性、Navier-Stokes 方程与变分法的核心工具。

## 分析

**前置依赖**：Sobolev空间定义、Sobolev嵌入定理、Hölder不等式、Poincaré不等式、积分估计与极坐标变换。

**定理内容**：设 $n<p\le\infty$，$\Omega\subseteq\mathbb{R}^n$ 为区域，$u\in W^{1,p}(\Omega)$。则存在常数 $C=C(n,p)$，使对几乎处处的 $x,y\in\Omega$ 成立

$$
|u(x)-u(y)|\le C\,|x-y|^{\,1-n/p}\,\|\nabla u\|_{L^{p}(\Omega)},
$$

从而可修改 $u$ 于零测集上使其成为 $\gamma=1-\frac np$ 阶 Hölder 连续函数，且嵌入连续：

$$
\|u\|_{C^{0,\gamma}(\Omega)}\le C\,\|u\|_{W^{1,p}(\Omega)}.
$$

**关键条件**：必须有 $p>n$。$p<n$ 时 $W^{1,p}$ 函数一般无界（如 $|x|^{-\alpha}$ 型函数），$p=n$ 时结论同样失效，可见 $1-n/p>0$ 是全部推导的支点。

## 思考过程

证明不能直接对 $u$ 做泰勒展开（弱导数只是 $L^p$ 函数），于是改用"沿射线积分"：把 $u(x)-u(y)$ 通过一维微积分基本定理写成梯度的积分，再压缩到球上做平均。难点有二：一是 $u(x)$ 本身没有点值，需先用光滑函数逼近，把不等式对 $C^1$ 函数证好，再在 $W^{1,p}$ 中取极限取下点值；二是余项 $|z-x|^{1-n}$ 的奇性在 $n>1$ 时不可积，必须靠 $p>n$ 才能用 Hölder 不等式把 $p$ 次幂吸收掉，恰好换来指数 $1-n/p$。

## 证明过程

**步骤 1：先证光滑情形。** 设 $u\in C^1(\Omega)$，$B=B(x,r)\subseteq\Omega$。对任意 $z\in B$，由微积分基本定理

$$
u(x)-u(z)=-\int_0^1\frac{d}{dt}u\bigl(x+t(z-x)\bigr)\,dt=-\int_0^1\nabla u\bigl(x+t(z-x)\bigr)\cdot(z-x)\,dt.
$$

对 $z$ 在 $B$ 上取平均，得

$$
\left|u(x)-\fint_B u\right|\le\frac1{|B|}\int_B\int_0^1\bigl|\nabla u\bigl(x+t(z-x)\bigr)\bigr|\,|z-x|\,dtdz.
$$

**步骤 2：化简为带奇性的积分。** 作变量替换 $\zeta=x+t(z-x)$ 并缩放回单位球，可得

$$
\left|u(x)-\fint_{B(x,r)}u\right|\le C(n)\int_{B(x,r)}\frac{|\nabla u(\zeta)|}{|\zeta-x|^{n-1}}\,d\zeta.
$$

再写成极坐标，令 $\rho=|\zeta-x|$：

$$
\int_{B(x,r)}\frac{|\nabla u(\zeta)|}{|\zeta-x|^{n-1}}\,d\zeta=\int_0^r\rho^{\,1-n}\left(\int_{\partial B(x,\rho)}|\nabla u|\,d\sigma\right)d\rho .
$$

**步骤 3：用 Hölder 不等式提取指数。** 记 $p'=\frac{p}{p-1}$。由 Hölder 不等式

$$
\int_{B(x,r)}\frac{|\nabla u(\zeta)|}{|\zeta-x|^{n-1}}\,d\zeta\le\|\nabla u\|_{L^p(B)}\left(\int_{B(x,r)}|\zeta-x|^{(1-n)p'}\,d\zeta\right)^{1/p'}.
$$

而 $(1-n)p'+n>0$ 当且仅当 $p>n$，此时内层积分为 $C(n,p)\,r^{\,n/p'-(n-1)}=C(n,p)\,r^{\,1-n/p}$，故

$$
\left|u(x)-\fint_{B(x,r)}u\right|\le C(n,p)\,\|\nabla u\|_{L^p(B(x,r))}\,r^{\,1-n/p}.
$$

**步骤 4：比较两点。** 设 $x,y\in\Omega$，$r=|x-y|$，取 $B=B(x,r)$。则

$$
|u(x)-u(y)|\le\left|u(x)-\fint_{B}u\right|+\left|\fint_{B}u-\fint_{B(y,2r)}u\right|+\left|\fint_{B(y,2r)}u-u(y)\right|.
$$

中间项用同样的积分表示估计，可归并到 $B(x,2r)$ 上的平均，三段给出同一量级，得到

$$
|u(x)-u(y)|\le C(n,p)\,\|\nabla u\|_{L^p(B(x,2r))}\,|x-y|^{\,1-n/p}.
$$

**步骤 5：由稠密性延拓到 $W^{1,p}$。** 对一般 $u\in W^{1,p}(\Omega)$，取光滑函数列 $u_m\to u$ 于 $W^{1,p}$。步骤 4 说明 $\{u_m\}$ 在 $C^{0,\gamma}$ 中一致有界且等度连续，由 Arzelà–Ascoli 型收敛可取出子列在 $C^{0,\gamma}$ 中收敛到某连续函数 $\tilde u$；而 $W^{1,p}$ 收敛蕴涵子列几乎处处收敛，故 $\tilde u=u$ 几乎处处，于是 $u$ 可被修改为 Hölder 连续并满足同一不等式。

**步骤 6：得到嵌入常数。** 把步骤 4 的局部估计叠加到 $\Omega$ 上，并补上 $\|u\|_{L^p}$ 项，即得

$$
\|u\|_{C^{0,\gamma}(\Omega)}=\|u\|_{L^\infty}+\sup_{x\neq y}\frac{|u(x)-u(y)|}{|x-y|^{\gamma}}\le C(n,p,\Omega)\,\|u\|_{W^{1,p}(\Omega)}.
$$

证毕。

## 相关条目

- [Sobolev嵌入定理](./Sobolev嵌入定理.md)：Morrey 不等式正是 $p>n$ 情形下最精细的嵌入结论。
- [Sobolev空间定义](./Sobolev空间定义.md)：本不等式的作用对象与范数的来源。
- [Poincaré不等式](./Poincaré不等式.md)：同属 Sobolev 空间的积分估计，常与 Morrey 估计配合使用。
- [Hölder不等式](../第17级-实分析/Hölder不等式.md)：步骤 3 提取指数 $1-n/p$ 的关键工具。
- [Fréchet-Kolmogorov紧性准则](./Fréchet-Kolmogorov紧性准则.md)：讨论 $W^{1,p}$ 到 $C^{0,\gamma}$ 的紧嵌入时使用。
