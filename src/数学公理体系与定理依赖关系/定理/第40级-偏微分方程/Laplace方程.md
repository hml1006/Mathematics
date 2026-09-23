# Laplace 方程

> **一句话大白话**：$\Delta u=0$ 描述一种"处处取邻居平均值"的平衡态——每一点既没有源也没有汇，函数值恰好等于它周围一圈的平均值，所以它内部鼓不出任何极值高峰。
>
> **小例子**：$u(x,y)=x^2-y^2$ 满足 $u_{xx}+u_{yy}=2-2=0$，是调和函数；而 $u(x,y)=x^2+y^2$ 有 $\Delta u=4\ne0$，就不是。

## 介绍

Laplace 方程 $\Delta u=0$ 是最基本、最重要的二阶线性偏微分方程，其中

$$\Delta u=\sum_{i=1}^n\frac{\partial^2 u}{\partial x_i^2}=\operatorname{div}(\nabla u)$$

称为 Laplace 算子，满足该方程的函数称为调和函数。它刻画无源的稳态场：静电势、稳态温度、不可压无旋流体的势函数、引力势都满足 Laplace 方程，因此它是椭圆型方程的典范。

Laplace 方程有三个刻画其"刚性"的基本性质：**平均值性质**（函数值等于球面/球上的平均）、**最大值原理**（内部无极值）、**基本解**（点源的响应），三者共同推出 Dirichlet 问题解的唯一性，并成为 Poisson 方程、Green 函数、调和分析（Fourier 变换、位势理论）的理论起点。它也是椭圆型方程最大值原理与二阶线性 PDE 分类中"椭圆型"的标准样例。

## 分析

**前置依赖**：高斯散度定理、方向导数与梯度的关系、克莱罗定理、叠加原理

**方程与基本解**：

$$\Delta u=0\quad(\text{在 }\Omega\text{ 内}),\qquad \Phi(x)=\begin{cases}-\dfrac{1}{2\pi}\log|x|, & n=2,\\[2mm] \dfrac{1}{(n-2)\omega_n\,|x|^{n-2}}, & n\ge3,\end{cases}$$

其中 $\omega_n$ 是 $\mathbb R^n$ 中单位球面的面积，$\Phi$ 称为 Laplace 算子的基本解，满足 $\Delta\Phi=0$ 于 $\mathbb R^n\setminus\{0\}$。

**定理内容**：

1. **平均值性质**：设 $u\in C^2(\Omega)$ 调和，$B(x,r)\subseteq\Omega$，则
   $$u(x)=\frac{1}{|\partial B(x,r)|}\oint_{\partial B(x,r)}u\,dS=\frac{1}{|B(x,r)|}\int_{B(x,r)}u\,dV.$$
2. **最大值原理**：调和函数在区域内部不能取到最大值或最小值，除非它是常数。
3. **唯一性**：设 $\Omega$ 有界，$u\in C^2(\Omega)\cap C(\overline\Omega)$ 满足 $\Delta u=0$ 于 $\Omega$、$u|_{\partial\Omega}=g$，则 $u$ 唯一。

**关键要点**：

- 调和性等价于"球面上的平均值等于中心值"，这是最本质的刻画；
- 由平均值性质立刻得到最大值原理，无需 Hopf 引理；
- 基本解的奇性集中在原点，正是它使 $-\Delta$ 具有 Green 函数表示；
- 方程是线性的，故叠加原理成立：调和函数的线性组合仍调和。

## 思考过程

关键工具是高斯散度定理。它把"体积分内部的 $\Delta u$"翻译成"穿过边界的通量"，而调和条件 $\Delta u=0$ 正说明通量为零。于是沿半径方向的通量守恒，平均值也就与半径无关。

具体地，记球面平均

$$\phi(r)=\frac{1}{|\partial B(x,r)|}\oint_{\partial B(x,r)}u\,dS.$$

对 $r$ 求导会把导数移到 $u$ 上：$\phi'(r)$ 恰好等于法向通量 $\oint_{\partial B(x,r)}\frac{\partial u}{\partial n}\,dS$ 除以面积。由散度定理，这个通量等于 $\int_{B(x,r)}\Delta u\,dV=0$。因此 $\phi$ 是常数；再令 $r\to0$，由 $u$ 的连续性得 $\phi(r)\equiv u(x)$。这就是平均值性质。

有了平均值性质，最大值原理就顺理成章：若 $u$ 在内部点 $x_0$ 取最大值，则它不小于以 $x_0$ 为心的任何球面值，而平均值又要等于 $u(x_0)$，于是球面上处处取到最大值；再用连通性传播，$u$ 恒为常数。

## 证明过程

**步骤 1：球面平均的导数。** 设 $u$ 调和。对球面 $\partial B(x,r)$ 用参数化 $x+r\xi$（$|\xi|=1$），$dS=r^{n-1}d\sigma(\xi)$，其中 $\sigma$ 是单位球面测度。于是

$$\phi(r)=\frac{1}{\omega_n}\oint_{|\xi|=1}u(x+r\xi)\,d\sigma(\xi),\qquad |\partial B(x,r)|=\omega_n r^{n-1}.$$

对 $r$ 求导（被积函数关于 $r$ 的光滑性使求导可移入积分号）：

$$\phi'(r)=\frac{1}{\omega_n}\oint_{|\xi|=1}\nabla u(x+r\xi)\cdot\xi\,d\sigma(\xi)=\frac{1}{|\partial B(x,r)|}\oint_{\partial B(x,r)}\frac{\partial u}{\partial n}\,dS,$$

这里 $\partial u/\partial n=\nabla u\cdot\xi$ 是沿外法向 $\xi$ 的方向导数，上式最后一步用了面积元换算。

**步骤 2：用散度定理得 $\phi$ 为常数。** 由高斯散度定理与 $\Delta u=\operatorname{div}(\nabla u)=0$，

$$\oint_{\partial B(x,r)}\frac{\partial u}{\partial n}\,dS=\int_{B(x,r)}\operatorname{div}(\nabla u)\,dV=\int_{B(x,r)}\Delta u\,dV=0.$$

代入步骤 1 得 $\phi'(r)=0$ 对一切 $0<r<\operatorname{dist}(x,\partial\Omega)$ 成立，故 $\phi(r)$ 为常数。

**步骤 3：确定常数。** 由 $u$ 在 $x$ 处连续，当 $r\to0$ 时 $u(x+r\xi)\to u(x)$ 关于 $\xi$ 一致，故

$$\phi(r)\xrightarrow[r\to0]{}\frac{1}{\omega_n}\oint_{|\xi|=1}u(x)\,d\sigma(\xi)=u(x).$$

因此 $\phi(r)\equiv u(x)$，即球面平均值等于中心值。

**步骤 4：化为球上平均。** 利用极坐标 $dV=s^{n-1}ds\,d\sigma(\xi)$ 与步骤 3，

$$\int_{B(x,r)}u\,dV=\int_0^r\oint_{\partial B(x,s)}u\,dS\,ds=\int_0^r u(x)\,|\partial B(x,s)|\,ds=u(x)\int_0^r\omega_n s^{n-1}ds=u(x)\,|B(x,r)|.$$

两边除以 $|B(x,r)|$ 得球上平均也等于 $u(x)$，平均值性质得证。

**步骤 5：最大值原理。** 设 $u$ 非常数且在 $x_0\in\Omega$ 取最大值 $M$。取 $r>0$ 使 $\overline{B(x_0,r)}\subseteq\Omega$。由平均值性质，

$$M=u(x_0)=\frac{1}{|B(x_0,r)|}\int_{B(x_0,r)}u\,dV\le\frac{1}{|B(x_0,r)|}\int_{B(x_0,r)}M\,dV=M.$$

不等号取等号（被积函数连续且处处 $\le M$）迫使 $u\equiv M$ 于 $B(x_0,r)$。于是集合 $\{u=M\}$ 在 $\Omega$ 中既开又闭，由 $\Omega$ 连通得 $u\equiv M$，与非常数矛盾。故非常数调和函数在内部取不到最大值；对最小值用 $-u$ 同理。$\square$

**步骤 6：Dirichlet 问题解的唯一性。** 设 $u_1,u_2$ 是同一 Dirichlet 问题的两个解，令 $w=u_1-u_2$。由线性性 $\Delta w=0$ 于 $\Omega$、$w|_{\partial\Omega}=0$。由最大值原理与最小值原理，$w$ 在 $\overline\Omega$ 上的最大值与最小值都在边界上取到，而边界上 $w=0$，故 $0\le w\le0$，即 $w\equiv0$。于是 $u_1=u_2$。$\square$

**步骤 7：基本解的调和性。** 设 $n\ge3$，$v(r)=r^{2-n}$（$r=|x|>0$）。径向函数的 Laplacian 为 $v''+\frac{n-1}{r}v'$（混合偏导可交换由克莱罗定理保证）。计算

$$v'(r)=(2-n)r^{1-n},\qquad v''(r)=(2-n)(1-n)r^{-n},$$

$$v''(r)+\frac{n-1}{r}v'(r)=(n-1)(n-2)r^{-n}-(n-1)(n-2)r^{-n}=0.$$

故 $\Phi=C\,|x|^{2-n}$ 在 $\mathbb R^n\setminus\{0\}$ 上调和；$n=2$ 时同理 $\Delta\log|x|=0$。这正是基本解"只在原点奇异"的来源。$\square$

## 相关条目

- [椭圆型方程最大值原理](./椭圆型方程最大值原理.md)：Laplace 方程作为一致椭圆算子的特例，其极值性质的一般化。
- [Poisson方程与Green函数](./Poisson方程与Green函数.md)：以基本解与叠加原理求解 $\Delta u=f$ 的边值问题。
- [二阶线性PDE分类](./二阶线性PDE分类.md)：Laplace 方程是椭圆型的标准范例。
- [高斯散度定理](../第12级-多变量微积分/高斯散度定理.md)：平均值性质证明的核心工具。
