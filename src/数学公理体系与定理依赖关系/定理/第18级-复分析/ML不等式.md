# ML 不等式

> **一句话大白话**：复变函数沿曲线积分的模，不超过"曲线上函数的最大模"乘以"曲线总长度"——积分是"长度乘大小"的量级估计。
>
> **小例子**：$f(z)=1$，$\gamma$ 为半径 $R$ 的半圆，则 $\left|\oint_\gamma dz\right|=0\le M L=1\cdot\pi R$。

## 介绍

ML 不等式（亦称 ML 估计）是复积分最基本的估计工具：若 $f$ 在曲线 $\gamma$ 上满足 $|f(z)|\le M$，且 $\gamma$ 的长度为 $L$，则

$$
\left|\int_\gamma f(z)\,dz\right|\le M L
$$

它把积分的大小估计转化为两个几何量——曲线的长度与函数的模上界，是复分析中"用估计代替精确计算"的标准手法。

ML 不等式在柯西积分公式、刘维尔定理、儒歇定理、最大模原理等核心定理的证明中反复出现：为了证明某个积分趋于零，只需说明被积函数有界而曲线长度趋于零。其中 $M$ 表示"Maximum"，$L$ 表示"Length"，故得名。

## 分析

**前置依赖**：复积分的定义（沿曲线取和的极限）、曲线的长度与可求长性、复数模的三角不等式

**定理内容**：设 $\gamma$ 是可求长曲线，$f$ 在 $\gamma$ 上连续且存在常数 $M\ge0$ 使 $|f(z)|\le M$ 对一切 $z\in\gamma$ 成立。记 $L$ 为 $\gamma$ 的长度，则

$$
\left|\int_\gamma f(z)\,dz\right|\le M L
$$

**数学内涵**：
- 结论对任意可求长曲线成立，不要求 $f$ 解析。
- 若 $\gamma$ 是长度为 $L$ 的圆弧、$|f|\le M$，则积分模不超过 $ML$；当 $|f|\equiv M$ 且 $f\,dz$ 的辐角沿曲线恒定（如 $\int_\gamma \frac{dz}{z}$ 的圆弧情形）时可接近等号。

## 思考过程

复积分定义为黎曼和的极限：$\int_\gamma f\,dz=\lim\sum_k f(\zeta_k)(z_k-z_{k-1})$。对每个黎曼和取模，用三角形不等式：

$$
\left|\sum_k f(\zeta_k)\Delta z_k\right|\le\sum_k|f(\zeta_k)|\,|\Delta z_k|\le M\sum_k|\Delta z_k|
$$

而 $\sum_k|\Delta z_k|$ 是折线弧长的和，它不超过曲线总长 $L$。于是每个黎曼和都被 $ML$ 控制住，取极限即得结论。这说明 ML 不等式本质上是"三角形不等式 + 长度定义"的直接产物。

## 证明过程

**步骤 1：用黎曼和逼近积分。** 设 $\gamma$ 的参数表示为 $z(t)$，$t\in[\alpha,\beta]$，取分割 $\alpha=t_0<t_1<\cdots<t_n=\beta$ 与介点 $\tau_k\in[t_{k-1},t_k]$，令 $\zeta_k=z(\tau_k)$、$\Delta z_k=z(t_k)-z(t_{k-1})$。则

$$
\int_\gamma f(z)\,dz=\lim_{\max_k\Delta t_k\to0}\sum_{k=1}^n f(\zeta_k)\,\Delta z_k
$$

**步骤 2：对黎曼和用三角形不等式。** 对每个 $n$，

$$
\left|\sum_{k=1}^n f(\zeta_k)\Delta z_k\right|\le\sum_{k=1}^n |f(\zeta_k)|\,|\Delta z_k|\le M\sum_{k=1}^n|\Delta z_k|
$$

**步骤 3：用折线长不超过曲线长。** 因 $|\Delta z_k|=\big|z(t_k)-z(t_{k-1})\big|\le\int_{t_{k-1}}^{t_k}|z'(t)|\,dt$（当 $z$ 为 $C^1$ 时由微积分基本定理与模的积分不等式），求和得

$$
\sum_{k=1}^n|\Delta z_k|\le\int_\alpha^\beta|z'(t)|\,dt=L
$$

对一般可求长曲线，折线长的上确界即为弧长 $L$，同样得 $\sum_k|\Delta z_k|\le L$。

**步骤 4：取极限。** 于是每个黎曼和的模不超过 $ML$。由步骤 1，$\int_\gamma f\,dz$ 是该极限，模函数连续，故

$$
\left|\int_\gamma f(z)\,dz\right|=\lim_{n\to\infty}\left|\sum_{k=1}^n f(\zeta_k)\Delta z_k\right|\le M L
$$

$\square$

**推论（常用形式）**：若 $\gamma$ 是以 $z_0$ 为心、半径 $R$ 的圆周，$|f(z)|\le M$ 在其上成立，则 $\left|\oint_\gamma f(z)\,dz\right|\le 2\pi R M$。该形式在刘维尔定理与儒歇定理的证明中反复使用。

## 课堂问答

**老师**：复积分怎么做到"不精确计算就能估计大小"？

**学生**：结论：$\left|\int_\gamma f(z)\,dz\right|\le ML$，$M$ 是 $|f|$ 在曲线 $\gamma$ 上的上界，$L$ 是曲线长。理由就是三角不等式加弧长定义：黎曼和取模有 $\left|\sum f(\zeta_k)\Delta z_k\right|\le\sum|f(\zeta_k)|\,|\Delta z_k|\le M\sum|\Delta z_k|\le ML$，取极限即得。注意只要 $f$ 连续、$\gamma$ 可求长即可，不要求 $f$ 解析。

**老师（追问）**：什么时候能取到等号？

**学生**：需要 $|f|\equiv M$ 且 $f\,dz$ 的辐角沿曲线恒定。最常用的形式是圆周：$\left|\oint_{|z-z_0|=R}f(z)\,dz\right|\le 2\pi R M$。一个常见误区是把 $\left|\int f\,dz\right|$ 与 $\int|f|\,|dz|$ 混为一谈，正确做法是先对有限黎曼和取模、再取极限。

**老师（拓展）**：ML 估计在复分析里扮演什么角色？

**学生**：它是把"积分趋于零"转化为"长度乘上界趋于零"的标准工具：柯西积分公式挖小圆时让 $\varepsilon\to0$，儒歇定理、刘维尔定理都靠它把 $M/R\to0$。

## 相关条目

- [柯西积分公式](./柯西积分公式.md)：其证明用 ML 不等式说明"挖去奇点后的小圆"上的积分趋于零。
- [柯西积分定理](./柯西积分定理.md)：复积分基本定理，ML 不等式是估计积分大小的常用工具。
