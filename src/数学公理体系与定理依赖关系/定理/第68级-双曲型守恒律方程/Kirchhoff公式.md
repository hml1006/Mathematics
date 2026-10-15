# Kirchhoff 公式

> **一句话大白话**：三维波动方程的解可以显式写出来——时刻 $t$、位置 $x$ 处的值只取决于初值在以 $x$ 为心、半径 $ct$ 的球面上的积分（含时间的导数项），波以速度 $c$ 沿球面恰好经过，过后不留余波。

> **小例子**：取初值 $g\equiv 0$、初速度 $h$ 只在原点附近的一小块内非零，则 $u(x,t)$ 只当 $|x|=ct$ 时才可能非零，清晰地体现了有限传播速度与 Huygens 无后效原理。

## 一、定理介绍

> **前置依赖**：波动方程与dAlembert公式、波动方程与能量估计、球面平均与散度定理（Green 公式）、Euler–Poisson–Darboux 方程。

Kirchhoff 于 1883 年给出了三维波动方程的显式积分表示，其思想源头是 Poisson 关于球面平均的技巧。公式把解化为初值在球面上的平均值及其时间导数，是 d'Alembert 公式在三维空间中的对应物。与一维情形不同，三维解没有"余波"：初值的扰动经过之后，空间某点重新回到静止，这就是著名的 Huygens 原理。Kirchhoff 公式不仅是波动方程适定性的直接证明工具，也是回声定位、地震波成像与电磁辐射等问题的数学基础。

## 二、原理思路

1. 对解 $u(\cdot,t)$ 作球面平均 $\bar u(r,t)$，利用散度定理把 $\Delta u$ 的平均化为对 $r$ 的二阶常微分算子，得到只含一个空间变量的 Euler–Poisson–Darboux 方程。
2. 令 $\tilde u(r,t)=r\bar u(r,t)$，把 Euler–Poisson–Darboux 方程化为标准的一维波动方程 $\tilde u_{tt}=c^2\tilde u_{rr}$。
3. 用一维的 d'Alembert 公式解出 $\tilde u$，再令 $r\to 0$ 并用导数取极限，将球面平均的极限还原为 $u(x,t)$，即得 Kirchhoff 公式。

## 三、定理的严格表述

考虑三维波动方程的初值问题

$$
u_{tt}=c^2\Delta u,\qquad x\in\mathbb{R}^3,\ t>0,
$$

$$
u(x,0)=g(x),\qquad u_t(x,0)=h(x),\qquad x\in\mathbb{R}^3,
$$

其中波速 $c>0$，初值满足 $g\in C^3(\mathbb{R}^3)$、$h\in C^2(\mathbb{R}^3)$。则其古典解由 **Kirchhoff 公式**给出：

$$
u(x,t)=\frac{\partial}{\partial t}\!\left(\frac{1}{4\pi c^2 t}\int_{\partial B(x,ct)}g(y)\,dS(y)\right)+\frac{1}{4\pi c^2 t}\int_{\partial B(x,ct)}h(y)\,dS(y),
$$

其中 $B(x,ct)$ 是以 $x$ 为心、半径 $ct$ 的球，$\partial B(x,ct)$ 为其球面，$dS$ 为面积元。

## 四、证明过程

**步骤 1（球面平均满足 Euler–Poisson–Darboux 方程）。** 对 $r>0$ 定义球面平均
$$
\bar u(x;r,t)=\frac{1}{4\pi r^2}\int_{\partial B(x,r)}u(y,t)\,dS(y).
$$
对 $\Delta u$ 作球面平均并用散度定理换到体积分，可得 $\overline{\Delta u}=(\partial_r^2+\tfrac{2}{r}\partial_r)\bar u$。由 $u_{tt}=c^2\Delta u$ 得
$$
\bar u_{tt}=c^2\!\left(\bar u_{rr}+\frac{2}{r}\bar u_r\right)=\frac{c^2}{r^2}\bigl(r^2\bar u_r\bigr)_r.
$$

**步骤 2（化为一维波动方程）。** 令 $\tilde u(r,t)=r\,\bar u(r,t)$。由乘积求导
$$
\tilde u_{rr}=2\bar u_r+r\,\bar u_{rr},\qquad\text{即}\qquad \frac{\tilde u_{rr}}{r}=\bar u_{rr}+\frac{2}{r}\bar u_r.
$$
代入步骤 1 的结果，得 $r>0$ 时
$$
\tilde u_{tt}=c^2\tilde u_{rr},\qquad \tilde u(0,t)=0,
$$
后者因 $\bar u$ 有界而成立。初值对应为
$$
\tilde u(r,0)=r\,M_g(r),\qquad \tilde u_t(r,0)=r\,M_h(r),
$$
其中 $M_g(r),M_h(r)$ 分别表示 $g,h$ 在 $\partial B(x,r)$ 上的平均。

**步骤 3（用 d'Alembert 公式求解）。** 把 $\tilde u(\cdot,0)$ 与 $\tilde u_t(\cdot,0)$ 按奇函数方式延拓到 $r<0$，记 $F(s)=sM_g(|s|)$、$H(s)=sM_h(|s|)$，它们都是奇函数。由波动方程与dAlembert公式，
$$
\tilde u(r,t)=\frac{F(r+ct)+F(r-ct)}{2}+\frac{1}{2c}\int_{r-ct}^{r+ct}H(s)\,ds.
$$

**步骤 4（令 $r\to0$ 得到 Kirchhoff 公式）。** 因球面平均 $\bar u$ 连续延拓到 $r=0$ 且等于 $u(x,t)$，故
$$
u(x,t)=\lim_{r\to 0}\bar u(r,t)=\lim_{r\to 0}\frac{\tilde u(r,t)}{r}=\partial_r\tilde u(0,t).
$$
对步骤 3 的表达式关于 $r$ 求导并取 $r=0$，利用 $F$ 奇、$F'$ 偶以及 $H(ct)-H(-ct)=2H(ct)=2ct\,M_h(ct)$，得
$$
\partial_r\tilde u(0,t)=F'(ct)+\frac{1}{2c}\cdot 2ct\,M_h(ct)=F'(ct)+t\,M_h(ct).
$$
又 $F'(ct)=\partial_t\bigl[t\,M_g(ct)\bigr]$，且
$$
t\,M_g(ct)=\frac{1}{4\pi c^2 t}\int_{\partial B(x,ct)}g\,dS,\qquad t\,M_h(ct)=\frac{1}{4\pi c^2 t}\int_{\partial B(x,ct)}h\,dS.
$$
代回即得
$$
u(x,t)=\frac{\partial}{\partial t}\!\left(\frac{1}{4\pi c^2 t}\int_{\partial B(x,ct)}g\,dS\right)+\frac{1}{4\pi c^2 t}\int_{\partial B(x,ct)}h\,dS.
$$
$\square$

## 五、应用与意义

- **有限传播速度**：公式显示 $u(x,t)$ 只依赖初值在球面 $\partial B(x,ct)$ 上的值，给出有限传播速度的定量表达。
- **Huygens 无后效原理**：三维情况扰动过后不留余波，而奇数维波动方程普遍具有这一性质。
- **降维法**：对二维情形令初值与 $x_3$ 无关，对 $x_3$ 积分即得 Poisson 公式，可理解二维波"拖尾"现象的来源。
- **反问题基础**：球面平均表示是球形 Radon 变换的原型，支撑 CT 成像、地震勘探与声源定位等反演方法。

## 课堂问答

**老师**：Kirchhoff 公式把三维波动方程的解写成了什么？请给出表达式的结构。

**学生**：$u(x,t)=\frac{\partial}{\partial t}\left(\frac{1}{4\pi c^2t}\int_{\partial B(x,ct)}g\,dS\right)+\frac{1}{4\pi c^2t}\int_{\partial B(x,ct)}h\,dS$，其中 $g=u(x,0)$、$h=u_t(x,0)$。解在 $(x,t)$ 的值只依赖初值在球面 $\partial B(x,ct)$ 上的平均值与其时间导数，体现波恰以速度 $c$ 沿球面到达。

**老师（追问）**：这个公式的推导主线索是什么？奇延拓在哪里起作用？

**学生**：三步。先对解作球面平均，用散度定理把 $\Delta u$ 的平均化为 $\bar u_{rr}+\frac2r\bar u_r$，得到 EPD 方程；再令 $\tilde u=r\bar u$ 化为一维波动方程 $\tilde u_{tt}=c^2\tilde u_{rr}$、$\tilde u(0,t)=0$；最后把 $\tilde u$ 的初值 $F(s)=sM_g(|s|)$、$H(s)=sM_h(|s|)$ 奇延拓，用 d'Alembert 公式求解。奇性既保证 $r=0$ 处的边界条件，又使极限 $r\to0$ 还原出 $u(x,t)=\partial_r\tilde u(0,t)$。

**老师（拓展）**：维数如何影响解的"余波"？二维为什么不同？

**学生**：奇数维波动方程满足 Huygens 无后效原理：扰动过后不留余波。三维公式只出现球面 $\partial B(x,ct)$ 上的值，球面扫过后 $g,h$ 不再贡献，$u$ 回到静止。二维情形可令初值与 $x_3$ 无关、对 $x_3$ 积分得到 Poisson 公式，解依赖球盘内部初值，出现"拖尾"。常见误区是忽略 $\partial_t$ 作用在含 $t$ 的球面平均上：它除了给出 $\frac{1}{4\pi c^2t}$ 因子外还贡献额外项。

## 相关条目

- [波动方程与能量估计](./波动方程与能量估计.md)：能量方法给出波动方程解的有界性，与显式公式互为补充。
- [守恒律方程基本理论](./守恒律方程基本理论.md)：波动方程是线性双曲系统的原型，与守恒律理论同源。
- [波动方程与dAlembert公式](../第40级-偏微分方程/波动方程与dAlembert公式.md)：一维情形下的对应显式解，是本公式的出发点。
