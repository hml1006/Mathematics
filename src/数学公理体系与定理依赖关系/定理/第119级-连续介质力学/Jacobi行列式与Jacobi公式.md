# Jacobi 行列式与 Jacobi 公式

> **一句话大白话**：把一个可逆线性变换（或光滑坐标变换）的"体积缩放倍数"记成一个行列式，就叫 Jacobi（雅可比）行列式；**Jacobi 公式**则给出这个行列式随时间变化的求导法则：$\dfrac{d}{dt}\det A=\det A\cdot\operatorname{tr}\big(A^{-1}\dot A\big)$。
>
> **小例子**：取 $A(t)=\begin{pmatrix}e^{t}&0\\0&e^{-t}\end{pmatrix}$，则 $\det A=1$ 为常数，而 $A^{-1}\dot A=\operatorname{diag}(1,-1)$ 的迹为 $0$，故 $\frac{d}{dt}\det A=1\cdot0=0$，与 $\det A\equiv1$ 一致。

## 一、定理介绍

> **前置依赖**：行列式的Leibniz公式、矩阵的迹、可逆矩阵等价条件。

设 $F:\Omega\subseteq\mathbb R^n\to\mathbb R^n$ 可微，**Jacobi 矩阵**为 $DF(\boldsymbol x)=\big(\partial F_i/\partial x_j\big)_{ij}$，**Jacobi 行列式**为 $J_F(\boldsymbol x)=\det DF(\boldsymbol x)$，它度量 $F$ 在 $\boldsymbol x$ 处的局部体积伸缩率（即换元公式中的体积因子）。**Jacobi 公式**是行列式的求导恒等式：对可微的可逆矩阵族 $A(t)$，
$$
\frac{d}{dt}\det A(t)=\det A(t)\cdot\operatorname{tr}\!\big(A(t)^{-1}\dot A(t)\big).
$$
更一般地，对不必可逆的 $A$，有 $\dfrac{d}{dt}\det A=\operatorname{tr}\big(\operatorname{adj}(A)\,\dot A\big)$，其中 $\operatorname{adj}(A)$ 为伴随矩阵。

## 二、原理思路

把行列式按 **Leibniz 公式** 展开为 $n!$ 项乘积之和，用乘积法则逐项求导。每一项恰好是"把某一行（列）替换成该行的导数、其余不动"所得矩阵的行列式，于是总和可写成这些行列式之和；再按被求导的那一行展开，系数正是伴随矩阵的余子式，从而合并为 $\operatorname{tr}(\operatorname{adj}(A)\dot A)$。当 $A$ 可逆时用 $\operatorname{adj}(A)=\det A\cdot A^{-1}$ 化为 Jacobi 公式。由此还能得到 $(\ln|\det A|)'=\operatorname{tr}(A^{-1}\dot A)$，这正是 Reynolds 输运定理中体积膨胀率的来源。

## 三、定理的严格表述

**（Jacobi 公式）** 设 $A(t)$ 为 $n\times n$ 实（或复）矩阵族，在每个 $t$ 处对 $t$ 可微。
1. 一般形式：$\dfrac{d}{dt}\det A=\operatorname{tr}\big(\operatorname{adj}(A)\,\dot A\big)$。
2. 可逆形式：当 $\det A(t)\ne0$ 时，$\dfrac{d}{dt}\det A=\det A\cdot\operatorname{tr}\big(A^{-1}\dot A\big)$。

## 四、证明过程

1. **Leibniz 展开**。记 $a_1,\dots,a_n$ 为 $A$ 的行向量，由行列式的 Leibniz 公式
   $$
   \det A=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^{n}a_{i\sigma(i)} .
   $$
2. **逐行求导**。对上式用乘积法则，并利用行列式对每一行的多重线性性（每次只对一行求导、其余行不动）：
   $$
   \frac{d}{dt}\det A=\sum_{k=1}^{n}\det\big(a_1,\dots,a_{k-1},\dot a_k,a_{k+1},\dots,a_n\big),
   $$
   即 \(\sum_k\) 覆盖“把第 $k$ 行换成其导数”的所有情形。
3. **识别余子式**。把第 $k$ 项按第 $k$ 行展开：$\det(\dots,\dot a_k,\dots)=\sum_{j}\dot a_{kj}\,C_{kj}$，其中 $C_{kj}$ 为元素 $a_{kj}$ 的代数余子式，而 $C_{kj}=\operatorname{adj}(A)_{jk}$。于是
   $$
   \frac{d}{dt}\det A=\sum_{k,j}\operatorname{adj}(A)_{jk}\,\dot a_{kj}=\operatorname{tr}\!\big(\operatorname{adj}(A)\,\dot A\big).
   $$
4. **可逆情形**。当 $\det A\ne0$ 时 $A$ 可逆（可逆矩阵等价条件），且 $\operatorname{adj}(A)=\det A\cdot A^{-1}$，代入第 3 步得
   $$
   \frac{d}{dt}\det A=\det A\cdot\operatorname{tr}\!\big(A^{-1}\dot A\big).
   $$
   两边除以 $\det A$ 得 $\big(\ln|\det A|\big)'=\operatorname{tr}(A^{-1}\dot A)$。

5. **推论（体积膨胀率）**。令 $A(t)=D\boldsymbol\chi(\boldsymbol X,t)$ 为变形梯度，$J=\det A$。由链式法则 $\dot A=(\nabla_{\boldsymbol x}\boldsymbol v)A$。利用迹的循环性
   $$
   \operatorname{tr}\!\big(A^{-1}(\nabla_{\boldsymbol x}\boldsymbol v)A\big)=\operatorname{tr}(\nabla_{\boldsymbol x}\boldsymbol v)=\nabla_{\boldsymbol x}\cdot\boldsymbol v ,
   $$
   故 $\dot J=J\,\nabla_{\boldsymbol x}\cdot\boldsymbol v$，即 Euler 体积膨胀公式：体积微元的相对膨胀率等于速度散度。它把“随体体积的变化”化为“速度场的散度”，是 Reynolds 输运定理的核心一步。$\blacksquare$

## 五、应用与意义

- **换元公式**：多重积分的变量替换以 $|\det D\Phi|$ 为体积因子，本公式给出该因子的代数来源（见多重 Riemann 积分与换元公式）。
- **流动的几何**：$\dot J=J\,\nabla\cdot\boldsymbol v$ 说明不可压缩流动 $(\nabla\cdot\boldsymbol v=0)$ 恰好保持体积，是连续介质运动学的基石。
- **一般工具**：Jacobi 公式在微分方程、李群（$\det e^{X}=e^{\operatorname{tr}X}$ 的推广）与矩阵分析中被广泛使用。

## 课堂问答

**老师**：Jacobi 公式 $\frac{d}{dt}\det A=\det A\cdot\mathrm{tr}(A^{-1}\dot A)$ 怎么证？

**学生**：先按 Leibniz 公式把行列式展成 $n!$ 项乘积之和，用乘积法则逐项求导，每项恰是"把某一行换成其导数"的行列式，求和后按该行展开，系数是代数余子式，即
$$
\frac{d}{dt}\det A=\mathrm{tr}\big(\mathrm{adj}(A)\,\dot A\big).
$$
当 $A$ 可逆时用 $\mathrm{adj}(A)=\det A\cdot A^{-1}$ 即得可逆形式。

**老师（追问）**：它和 Reynolds 输运定理有什么关系？

**学生**：它是 Euler 体积膨胀公式的来源。取 $A=D\boldsymbol\chi$ 为变形梯度、$J=\det A$，由 $\dot A=(\nabla_{\boldsymbol x}\boldsymbol v)A$ 与迹的循环性得
$$
\dot J=J\,\mathrm{tr}(\nabla_{\boldsymbol x}\boldsymbol v)=J\,\nabla_{\boldsymbol x}\cdot\boldsymbol v,
$$
即体积微元的相对膨胀率等于速度散度，正是输运定理中对 $J$ 求导那一步。

**老师（拓展）**：本可逆公式还能读出什么？

**学生**：两边除以 $\det A$ 得 $(\ln|\det A|)^\prime=\mathrm{tr}(A^{-1}\dot A)$，对矩阵李群即 $\det e^{X}=e^{\mathrm{tr}X}$ 的微分版本；不可逆时必须退回伴随矩阵形式 $\mathrm{tr}(\mathrm{adj}(A)\dot A)$，不能除以 $\det A$。
