# 一阶线性 ODE 通解公式

## 介绍

一阶线性常微分方程通解公式是微分方程理论中最基本的结果之一，给出了形如 $y'+p(x)y=q(x)$ 的方程显式通解。该公式由 Leibniz 在 17 世纪末期提出，是常数变易法（Variation of Parameters）的典型应用，在物理、工程、生物模型等领域有广泛应用。

## 分析

**前置依赖**：常数变易法、一阶微分方程、积分因子法

**定理内容**：一阶线性常微分方程
$$y'+p(x)y=q(x)$$
的通解为
$$y=e^{-\int p(x)\,dx}\left(\int q(x)e^{\int p(x)\,dx}\,dx+C\right)$$
其中 $C$ 为任意常数。

**数学内涵**：该公式表明一阶线性 ODE 的解空间由一个特解加上齐次方程的通解构成。积分因子 $\mu(x)=e^{\int p(x)dx}$ 将方程转化为恰当微分方程，使得左边成为 $(y\mu)'$ 的形式。

**证明策略**：引入积分因子 $\mu(x)=e^{\int p(x)dx}$，将原方程乘以 $\mu(x)$ 后化为 $(y\mu)'=q\mu$，然后直接积分。

## 思考过程

解一阶线性 ODE 的核心思想是"化归"——通过引入积分因子将非恰当方程变为恰当方程。积分因子的构造源于观察到 $(y\mu)'=y'\mu+y\mu'$，若令 $\mu'=p\mu$，则左边恰好是 $(y\mu)'$，从而将问题转化为简单的积分运算。

## 证明过程

**定理**：一阶线性微分方程 $y'+p(x)y=q(x)$ 的通解为
$$y=e^{-\int p(x)\,dx}\left(\int q(x)e^{\int p(x)\,dx}\,dx+C\right)$$

**证明**：

考虑方程
$$y'+p(x)y=q(x)$$

引入积分因子 $\mu(x)=e^{\int p(x)\,dx}$，则
$$\mu'(x)=p(x)e^{\int p(x)\,dx}=p(x)\mu(x)$$

将原方程两边乘以 $\mu(x)$：
$$\mu(x)y'+p(x)\mu(x)y=\mu(x)q(x)$$

注意到左边恰好是 $(\mu y)'$ 的展开：
$$\frac{d}{dx}(\mu y)=\mu'y+\mu y'=p\mu y+\mu y'$$

因此
$$\frac{d}{dx}(\mu y)=\mu q$$

两边积分：
$$\mu y=\int \mu(x)q(x)\,dx+C$$

代入 $\mu(x)=e^{\int p(x)dx}$：
$$e^{\int p(x)dx}y=\int q(x)e^{\int p(x)dx}\,dx+C$$

解得
$$y=e^{-\int p(x)dx}\left(\int q(x)e^{\int p(x)dx}\,dx+C\right)$$

$\square$