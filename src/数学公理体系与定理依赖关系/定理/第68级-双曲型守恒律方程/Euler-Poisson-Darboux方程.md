# Euler-Poisson-Darboux 方程

> **一句话大白话**：把波动方程的解在球面上取平均，得到的函数满足一个带 $\frac{1}{r}$ 奇异系数的方程，这就是 Euler–Poisson–Darboux 方程；作代换 $z=r\bar u$ 后它退化为最普通的一维波动方程，于是可直接用 d'Alembert 公式求出显式解。

> **小例子**：三维波动方程的球面平均 $\bar u(r,t)$ 满足 $\bar u_{tt}=c^2\bigl(\bar u_{rr}+\frac{2}{r}\bar u_r\bigr)$；令 $z=r\bar u$ 得 $z_{tt}=c^2z_{rr}$，从而 $\bar u$ 有显式公式。

## 一、定理介绍

> **前置依赖**：球面平均与散度定理、分部积分与散度定理、波动方程与dAlembert公式、二阶线性PDE分类。

Euler–Poisson–Darboux（EPD）方程是波动方程在球面平均作用下的像。对 $\mathbb{R}^n$ 中波动方程的解 $u$ 取半径为 $r$ 的球面平均，对 $\Delta u$ 的球面平均使用散度定理，可把拉普拉斯算子化为只含 $r$ 的二阶常微分算子：

$$
\text{球面平均}\bigl(\Delta u\bigr)=\frac{1}{r^{\,n-1}}\frac{\partial}{\partial r}\left(r^{\,n-1}\frac{\partial \bar u}{\partial r}\right)
=\bar u_{rr}+\frac{n-1}{r}\bar u_r .
$$

于是球面平均满足

$$
\bar u_{tt}=c^2\left(\bar u_{rr}+\frac{n-1}{r}\bar u_r\right).
$$

当 $n=3$ 时即经典形式 $\bar u_{tt}=c^2\bigl(\bar u_{rr}+\frac{2}{r}\bar u_r\bigr)$。更一般地，形如 $u_{tt}+\frac{k}{t}u_t=c^2\Delta u$ 的方程（称为广义 EPD 方程）也属于同类。方程在 $r=0$ 处奇异，但通过 $z=r\,\bar u$ 可化为一维波动方程，从而获得显式解——这正是 Kirchhoff 公式的核心步骤。

## 二、原理思路

1. **导出 EPD**：球面平均把 $\Delta u$ 的球面平均写成 $\bigl(r^{\,n-1}\bar u_r\bigr)_r/r^{\,n-1}$，代回 $u_{tt}=c^2\Delta u$ 即得 EPD 方程。
2. **消去奇异系数**：令 $z(r,t)=r\,\bar u(r,t)$，由乘积求导关系 $\bar u_{rr}+\frac{2}{r}\bar u_r=\frac{z_{rr}}{r}$，EPD 方程化为 $z_{tt}=c^2z_{rr}$。
3. **奇延拓解一维问题**：把初值 $z(r,0)=r\varphi(r)$、$z_t(r,0)=r\psi(r)$ 按奇函数延拓到 $r<0$，用 d'Alembert 公式写出 $z$，再除以 $r$ 得到 $\bar u$ 的显式解。

## 三、定理的严格表述

设 $c>0$，$\varphi,\psi\in C^2[0,\infty)$。考虑 $r>0$ 上的初值问题

$$
\bar u_{tt}=c^2\left(\bar u_{rr}+\frac{2}{r}\bar u_r\right),\qquad
\bar u(r,0)=\varphi(r),\qquad \bar u_t(r,0)=\psi(r),
$$

并设 $\bar u(r,t)$ 在 $r=0$ 处保持有界。

**定理（EPD 方程的显式解）**：上述问题的解由下式给出。当 $r>ct$ 时

$$
\bar u(r,t)=\frac{(r+ct)\varphi(r+ct)+(r-ct)\varphi(r-ct)}{2r}
+\frac{1}{2cr}\int_{r-ct}^{\,r+ct}s\,\psi(s)\,ds ,
$$

当 $0<r<ct$ 时

$$
\bar u(r,t)=\frac{(r+ct)\varphi(r+ct)+(ct-r)\varphi(ct-r)}{2r}
+\frac{1}{2cr}\int_{ct-r}^{\,ct+r}s\,\psi(s)\,ds .
$$

**推论（化为一维波动方程）**：若 $\bar u$ 满足上式 EPD 方程，则 $z(r,t)=r\,\bar u(r,t)$ 在 $r>0$ 上满足

$$
z_{tt}=c^2 z_{rr},\qquad z(0,t)=0 .
$$

## 四、证明过程

**步骤 1（球面平均满足 EPD 方程）。** 记球面平均
$$
\bar u(r,t)=\frac{1}{|\partial B_r|}\int_{\partial B(x,r)}u(y,t)\,dS(y),
$$
由球面平均与散度定理中的结论 $\overline{\Delta u}=\bar u_{rr}+\frac{n-1}{r}\bar u_r$，对 $u_{tt}=c^2\Delta u$ 两侧取球面平均（$t$ 的导数与球面平均可交换）即得 EPD 方程。三维情形 $n=3$ 即 $\bar u_{tt}=c^2\bigl(\bar u_{rr}+\frac{2}{r}\bar u_r\bigr)$。

**步骤 2（化为标准一维波动方程）。** 令 $z=r\bar u$。由乘积求导

$$
z_{r}=r\bar u_r+\bar u,\qquad z_{rr}=2\bar u_r+r\bar u_{rr},
$$

故

$$
\frac{z_{rr}}{r}=\bar u_{rr}+\frac{2}{r}\bar u_r .
$$

将 EPD 方程右端换为 $c^2\dfrac{z_{rr}}{r}$，并注意 $z_{tt}=r\bar u_{tt}$，得

$$
z_{tt}=c^2 z_{rr},\qquad r>0 .
$$

由 $\bar u$ 在 $r=0$ 有界知 $z(0,t)=0$，这正是奇延拓所要求的边界条件。

**步骤 3（奇延拓与 d'Alembert 公式）。** 记 $\Phi(s)=s\,\varphi(|s|)$、$\Psi(s)=s\,\psi(|s|)$，二者都是 $\mathbb{R}$ 上的奇函数且在 $s=0$ 连续。由波动方程与dAlembert公式，$z$ 的奇延拓解为

$$
z(r,t)=\frac{\Phi(r+ct)+\Phi(r-ct)}{2}+\frac{1}{2c}\int_{r-ct}^{\,r+ct}\Psi(s)\,ds .
$$

**步骤 4（还原 $\bar u$）。** 当 $r>ct$ 时 $r-ct>0$，于是 $\Phi(r\pm ct)=(r\pm ct)\varphi(r\pm ct)$，且积分上下限均为正，直接得到第一个公式。

当 $0<r<ct$ 时 $r-ct<0$，由 $\Phi$ 的奇性 $\Phi(r-ct)=(r-ct)\varphi(ct-r)$；又因 $\Psi$ 为奇函数，对第二项作代换 $s\mapsto -s$ 得

$$
\int_{r-ct}^{\,r+ct}\Psi(s)\,ds=\int_{0}^{\,r+ct}\Psi(s)\,ds+\int_{ct-r}^{\,0}\Psi(-u)\,du
=\int_{ct-r}^{\,ct+r}s\,\psi(s)\,ds .
$$

把两式代回 $z$ 并除以 $r$，即得第二个公式。$\square$

## 五、应用与意义

- **Kirchhoff 公式的枢纽**：三维波动方程的显式解正是借助 EPD 方程与 $z=r\bar u$ 的代换得到，EPD 方程因此是 Huygens 无后效原理的代数化表达。
- **降维工具**：把 $n$ 维（或分数维）球面平均问题统一化归为常微分方程，是研究波动方程、热方程与色散方程的通用手段。
- **广义 EPD 方程**：$u_{tt}+\frac{k}{t}u_t=c^2\Delta u$ 出现在广义相对论、共形几何与奇异摄动问题中，其可解性取决于参数 $k$ 的取值。
- **反问题与成像**：球面平均算子及其逆是球形 Radon 变换的原型，直接支撑 CT 成像与地震波反演。
