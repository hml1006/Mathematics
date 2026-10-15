# 多重 Riemann 积分与换元公式

> **一句话大白话**：把一元积分"分割—求和—取极限"的想法搬到高维，就是多重 Riemann 积分；而**换元公式**说，做变量替换 $\boldsymbol x=\Phi(\boldsymbol u)$ 时体积微元要按 Jacobi 行列式缩放：$d\boldsymbol x=|\det D\Phi|\;d\boldsymbol u$。
>
> **小例子**：极坐标 $\boldsymbol x=(r\cos\theta,\,r\sin\theta)$ 的行列式为 $r$，于是圆盘上的积分 $\iint_{\text{圆}}f\,dA=\int_0^{2\pi}\!\!\int_0^{R}f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$，多出来的 $r$ 正是行列式因子。

## 一、定理介绍

> **前置依赖**：积分中值定理、Jacobi行列式与Jacobi公式、微积分基本定理。

**多重 Riemann 积分**：对有界闭区域 $R\subseteq\mathbb R^n$ 与有界函数 $f$，作分割 $\mathcal P=\{R_k\}$、在每格取 $\boldsymbol\xi_k$ 作 Riemann 和，若当分割直径 $\|\mathcal P\|\to0$ 时极限存在且唯一，则记
$$
\int_R f(\boldsymbol x)\,d\boldsymbol x=\lim_{\|\mathcal P\|\to0}\sum_k f(\boldsymbol\xi_k)\,\mathrm{vol}(R_k).
$$
**换元公式**（变量替换）：设 $\Phi:U\to V$ 为开集间的 $C^1$ 微分同胚，$f$ 在 $V$ 上可积，则
$$
\int_{V}f(\boldsymbol x)\,d\boldsymbol x=\int_{U}f(\Phi(\boldsymbol u))\,\big|\det D\Phi(\boldsymbol u)\big|\,d\boldsymbol u .
$$
它是 Reynolds 输运定理把"随时间变动的区域"拉回"固定参考区域"时的理论依据。

## 二、原理思路

换元公式的实质是"局部体积如何缩放"。$\Phi$ 在每点 $\boldsymbol u$ 附近近似等于线性映射 $D\Phi(\boldsymbol u)$，而线性映射 $A$ 把体积放大 $|\det A|$ 倍（可由初等行变换与行列式的乘性看出）。于是把 $U$ 分割成足够小的立方体：在每个小立方体上，$\Phi$ 与 $D\Phi$ 的偏差被一致性（$D\Phi$ 的一致连续性）压得任意小，误差项随分割变细趋于零，求和取极限即得公式。

## 三、定理的严格表述

**（换元公式）** 设 $U,V\subseteq\mathbb R^n$ 为开集，$\Phi:U\to V$ 为 $C^1$ 双射且 $\det D\Phi(\boldsymbol u)\ne0\ (\boldsymbol u\in U)$，$f:V\to\mathbb R$ 可积。则 $(f\circ\Phi)\,|\det D\Phi|$ 在 $U$ 上可积，且
$$
\int_V f\,d\boldsymbol x=\int_U (f\circ\Phi)\,\big|\det D\Phi\big|\,d\boldsymbol u .
$$

## 四、证明过程

1. **线性情形**。设 $\Phi=T$ 为线性映射，矩阵 $A$，$R_0=[0,1]^n$ 为单位立方体。可逆矩阵可写成有限个初等矩阵之积 $A=E_1E_2\cdots E_m$。逐类验证体积效应：置换行/列有 $|\det E|=1$ 且保体积；把某行乘以 $c$ 有 $|\det E|=|c|$ 并把体积放大 $|c|$ 倍；把某行的倍数加到另一行有 $\det E=1$ 且由 Cavalieri 原理保体积。故每步都满足 $\mathrm{vol}(E S)=|\det E|\,\mathrm{vol}(S)$，逐步相乘得
   $$
   \mathrm{vol}(A R)=|\det A|\,\mathrm{vol}(R)\qquad(\text{任意可测区域 }R).
   $$
   其中用到 $\det(AB)=\det A\det B$。

2. **局部线性化**。对 $\boldsymbol u_0\in U$，由 $C^1$ 可微性
   $$
   \Phi(\boldsymbol u)=D\Phi(\boldsymbol u_0)(\boldsymbol u-\boldsymbol u_0)+\boldsymbol r(\boldsymbol u),\qquad \boldsymbol r(\boldsymbol u)=o\big(|\boldsymbol u-\boldsymbol u_0|\big).
   $$
   因 $D\Phi$ 在紧集上一致连续，取分割使每格立方体 $Q$ 的直径 $<\delta$，则可保证 $\boldsymbol r$ 在 $Q$ 上满足 $|\boldsymbol r|\le\varepsilon\,\mathrm{diam}(Q)$，且 $\varepsilon$ 与 $Q$ 位置无关。

3. **单格体积对比**。设 $Q$ 以 $\boldsymbol u_0$ 为中心。由第 2 步的误差估计，$\Phi(Q)$ 与线性像 $D\Phi(\boldsymbol u_0)Q$ 的对称差体积为 $o(\mathrm{vol}(Q))$，结合第 1 步得
   $$
   \mathrm{vol}\big(\Phi(Q)\big)=\big|\det D\Phi(\boldsymbol u_0)\big|\,\mathrm{vol}(Q)\,\big(1+o(1)\big).
   $$

4. **Riemann 和取极限**。把 $\int_V f$ 的 Riemann 和按像区 $\Phi(Q_k)$ 单元写出，用第 3 步换成 $U$ 上的和：
   $$
   \sum_k f\big(\Phi(\boldsymbol u_k)\big)\,\mathrm{vol}\big(\Phi(Q_k)\big)=\sum_k f\big(\Phi(\boldsymbol u_k)\big)\,\big|\det D\Phi(\boldsymbol u_k)\big|\,\mathrm{vol}(Q_k)\,\big(1+o(1)\big).
   $$
   因 $f\circ\Phi\cdot|\det D\Phi|$ 连续有界，误差因子 $1+o(1)$ 随 $\|\mathcal P\|\to0$ 一致趋于 $1$；由积分中值定理控制每格取值误差，两端极限相同，即得换元公式。

5. **推论**。取 $\Phi$ 为极坐标（因子 $r$）或球坐标（因子 $\rho^2\sin\varphi$）变换，即得常用体积因子；取 $\Phi$ 为运动映射 $\boldsymbol\chi(\cdot,t)$，则 $|J(\boldsymbol X,t)|=|\det D\boldsymbol\chi|$ 正是 Reynolds 输运定理中被积函数所乘的 Jacobi 行列式。$\blacksquare$

## 五、应用与意义

- **变动区域的求导**：Reynolds 输运定理先把 $V(t)$ 拉回固定参考区域 $V_0$，再在积分号内求导，其合法性完全依赖本公式。
- **坐标变换**：极坐标、柱坐标、球坐标下的重积分计算是物理与工程中最常用的实例。
- **测度观点**：公式说明 $C^1$ 微分同胚把 Lebesgue 测度按 $|\det D\Phi|$ 变换，是几何测度论与流形积分的起点。

## 课堂问答

**老师**：换元公式里那个 $|\det D\Phi|$ 到底是哪来的？

**学生**：它是局部体积缩放因子。$\Phi$ 在每点附近近似线性映射 $D\Phi$，而线性映射把体积放大 $|\det A|$ 倍，故
$$
\int_V f\,dx=\int_U (f\circ\Phi)\,|\det D\Phi|\,du .
$$
极坐标多出的因子 $r$、球坐标的 $\rho^2\sin\varphi$ 都是它的特例。

**老师（追问）**：线性情形为什么体积就按 $|\det A|$ 缩放？

**学生**：把可逆矩阵写成初等矩阵之积：置换行列式绝对值为 $1$ 且保体积；某行乘 $c$ 时行列式为 $c$、体积放大 $|c|$ 倍；某行倍数加到另一行为行列式 $1$、由 Cavalieri 原理保体积。逐步相乘再用 $\det(AB)=\det A\det B$，即得 $\mathrm{vol}(AR)=|\det A|\,\mathrm{vol}(R)$。

**老师（拓展）**：非线性情形怎么把误差抹掉？

**学生**：靠 $D\Phi$ 的一致连续。取分割使每格直径 $<\delta$，则余项 $\boldsymbol r=o(|\boldsymbol u-\boldsymbol u_0|)$ 在整格上一致地被 $\varepsilon\,\mathrm{diam}(Q)$ 控制，于是
$$
\mathrm{vol}\big(\Phi(Q)\big)=|\det D\Phi(\boldsymbol u_0)|\,\mathrm{vol}(Q)\,(1+o(1)),
$$
误差因子随分割变细一致趋于 $1$，Riemann 和两端极限相同。这正是 Reynolds 输运定理把动区域拉回固定区域的依据。
