# Jensen 不等式

> **一句话大白话**：凸函数"在平均处取值"不超过"取值的平均"——先平均再代入，绝不比代入后再平均更大。
>
> **小例子**：取 $\varphi(x)=x^2$，得 $\mathbb E[X^2]\ge(\mathbb E[X])^2$，即方差非负；取 $\varphi(x)=-\log x$，得算术-几何平均不等式。

## 介绍

Jensen 不等式（Jensen's inequality）由丹麦数学家 Johan Jensen 于 1906 年提出，是凸分析中最基本的不等式之一。它断言凸函数与期望（或加权平均）的方向关系：凸函数在均值处的取值不超过该函数取值的均值。

Jensen 不等式在概率论、统计学、信息论与分析中无处不在。由它可直接推出方差非负、算术-几何-调和平均不等式、$L^p$ 范数的凸性、Kullback–Leibler 散度的非负性以及矩母函数的对数凸性等一大批基本结论，是许多估计与界估计的起点。

它的条件版本 $\varphi(\mathbb E[X\mid\mathcal G])\le\mathbb E[\varphi(X)\mid\mathcal G]$ 也是条件期望理论中的常用工具，例如用于证明条件方差非负。

## 分析

**前置依赖**：凸函数与支撑超平面（次梯度）的存在性、期望的单调性与线性、条件期望的性质

**定理内容**：设 $\varphi:\mathbb R\to\mathbb R$ 是凸函数，$X$ 是可积随机变量且 $\varphi(X)$ 可积，则

$$\varphi\big(\mathbb E[X]\big)\le\mathbb E\big[\varphi(X)\big].$$

更一般地，对任意子 $\sigma$-代数 $\mathcal G$，

$$\varphi\big(\mathbb E[X\mid\mathcal G]\big)\le\mathbb E\big[\varphi(X)\mid\mathcal G\big]\qquad\text{a.s.}$$

**关键要点**：

- 凸性是本质假设；若 $\varphi$ 为凹函数，不等号反向；
- 若 $\varphi$ 严格凸，则等号成立当且仅当 $X$ 在相应 $\sigma$-代数上几乎必然为常数；
- 有等价的"支撑线"形式：对每个 $x_0$，存在 $\lambda$ 使对一切 $x$ 有 $\varphi(x)\ge\varphi(x_0)+\lambda(x-x_0)$。

## 思考过程

证明的核心是"支撑线"技巧，它把非线性问题化为线性问题。凸函数 $\varphi$ 在点 $\mu=\mathbb E[X]$ 处存在一条支撑仿射函数

$$\ell(x)=\varphi(\mu)+\lambda(x-\mu),$$

它满足对整个实轴 $\ell(x)\le\varphi(x)$，且在 $\mu$ 处与 $\varphi$ 相切，即 $\ell(\mu)=\varphi(\mu)$。几何上，这条直线位于凸函数图像的下方并贴着它。

既然 $\ell\le\varphi$ 处处成立，就有 $\ell(X)\le\varphi(X)$；取期望并利用 $\mathbb E[\ell(X)]=\ell(\mathbb E[X])$（期望的线性，且 $\mathbb E[X]=\mu$）就得到结论。之所以能这样"抄近路"，正是因为存在一条全局低于 $\varphi$ 而在均值处取等的直线——这就是凸性的分析意义。

## 证明过程

**步骤 1：支撑线的存在。** 设 $\mu=\mathbb E[X]$ 有限。取 $\lambda$ 为 $\varphi$ 在 $\mu$ 处的一个次梯度，即 $\lambda\in\partial\varphi(\mu)$，于是对一切 $x\in\mathbb R$，

$$\varphi(x)\ge\varphi(\mu)+\lambda(x-\mu).$$

（当 $\varphi$ 可微时取 $\lambda=\varphi'(\mu)$；一般凸函数的次梯度集合非空，故这样的 $\lambda$ 一定存在。）

**步骤 2：代入随机变量。** 令 $\ell(x)=\varphi(\mu)+\lambda(x-\mu)$，则对随机变量 $X$ 有

$$\varphi(X)\ge\ell(X)=\varphi(\mu)+\lambda(X-\mu).$$

**步骤 3：取期望。** 由期望的单调性与线性，并注意 $\mathbb E[X-\mu]=0$，

$$\mathbb E[\varphi(X)]\ge\mathbb E[\ell(X)]=\varphi(\mu)+\lambda\,\mathbb E[X-\mu]=\varphi(\mu)=\varphi(\mathbb E[X]).$$

**步骤 4：条件版本。** 对条件期望重复步骤 1–3：在 $\mathcal G$-可测意义下，$\mathbb E[X\mid\mathcal G]$ 起 $\mu$ 的作用，$\lambda$ 取为 $\mathcal G$-可测的次梯度，于是

$$\varphi\big(\mathbb E[X\mid\mathcal G]\big)\le\mathbb E\big[\varphi(X)\mid\mathcal G\big]\qquad\text{a.s.}$$

两边再取期望即回到无条件版本。$\square$

**推论**：

1. 取 $\varphi(x)=x^2$ 得 $\mathbb E[X^2]\ge(\mathbb E[X])^2$；
2. 取 $\varphi(x)=-\log x$（$x>0$）得 $\mathbb E[\log X]\le\log\mathbb E[X]$，即算术-几何平均不等式；
3. 取 $\varphi(x)=e^{x}$ 得矩母函数的对数凸性：$\log\mathbb E[e^{tX}]$ 关于 $t$ 是凸函数。

## 课堂问答

**老师**：$\varphi\big(\mathbb E[X]\big)$ 与 $\mathbb E[\varphi(X)]$ 哪个大？

**学生**：凸函数下前者不超过后者，即 $\varphi\big(\mathbb E[X]\big)\le\mathbb E\big[\varphi(X)\big]$；凹函数则反向。取 $\varphi(x)=x^2$ 立刻得 $\mathbb E[X^2]\ge(\mathbb E[X])^2$，即方差非负。

**老师（追问）**：证明为什么只需一条直线？

**学生**：因为凸函数在 $\mu=\mathbb E[X]$ 处有支撑仿射函数 $\ell(x)=\varphi(\mu)+\lambda(x-\mu)$，满足 $\ell\le\varphi$ 且在 $\mu$ 处取等；对 $\ell(X)\le\varphi(X)$ 取期望并用线性即得结论。

**老师（拓展）**：等号何时成立？

**学生**：只有当 $X$ 几乎必然取常值（无条件时即 $X=\mathbb E[X]$ 几乎必然）且 $\varphi$ 严格凸时才取等，否则一般严格。条件版本 $\varphi(\mathbb E[X\mid\mathcal G])\le\mathbb E[\varphi(X)\mid\mathcal G]$ 同样成立。

## 相关条目

- [马尔可夫不等式](./马尔可夫不等式.md)：同为矩条件导出的基本概率不等式。
- [全期望公式](./全期望公式.md)：条件 Jensen 不等式通过取期望归约到无条件形式。
