# Morse函数与Morse引理

> **一句话大白话**：Morse 函数是"每个临界点都不退化"的光滑函数；Morse 引理说，在这种临界点附近总能换一套坐标，把函数变成最朴素的"二次型平方和"——就像把任意弯曲的碗在局部抚平成标准抛物面。
>
> **小例子**：$f(x,y)=x^2-y^2$ 在原点是非退化鞍点，取坐标即可写成 $u^2-v^2$；而 $f(x,y)=x^2$ 的临界点整条 $x=0$ 上的点都退化（Hessian 奇异），Morse 引理不适用。

## 介绍

Morse 函数与 Morse 引理（Morse Lemma）是 Morse 理论的基石，由 Marston Morse 在 1920 年代创立。设 $f:M\to\mathbb R$ 是光滑流形上的光滑函数，临界点 $p$（即 $\mathrm d f_p=0$）称为**非退化的**，若其 Hessian 二次型在局部坐标下可逆。$f$ 称为 Morse 函数，若所有临界点都非退化。

Morse 引理断言：在非退化临界点 $p$ 的附近，存在局部坐标 $(x_1,\dots,x_n)$ 且 $x(p)=0$，使得

$$
f(x)=f(p)-x_1^2-\cdots-x_k^2+x_{k+1}^2+\cdots+x_n^2.
$$

其中 $k$ 称为该临界点的 Morse 指标（等于 Hessian 的负惯性指数），由 Sylvester 惯性定律决定，与坐标选取无关。

其地位在于：它把任意光滑函数在临界点附近的复杂形态**标准化**，只保留"有几个下降方向、几个上升方向"这一离散信息。由此 Kuhn–Morse 理论把流形的拓扑（同调、Betti 数、Euler 特征、把手分解）与 Morse 函数的临界点个数及指标联系起来，也是 Witten 用超对称量子力学重证 Morse 不等式的出发点。

## 分析

光滑流形与局部坐标、隐函数定理、Taylor 展开与 Hadamard 引理、Hessian 二次型与 Sylvester 惯性定律、二次型的合同标准形、切空间与临界点。

**定理内容**（Morse 引理）：设 $f$ 在 $p$ 处有非退化临界点，则存在 $p$ 的开邻域 $U$、同胚（实为微分同胚的坐标变换）$x:U\to\mathbb R^n$，$x(p)=0$，使得对所有 $x\in U$

$$
f=f(p)-\sum_{i=1}^{k}x_i^2+\sum_{i=k+1}^{n}x_i^2,
$$

其中 $k$（$0\le k\le n$）是 Hessian 的负惯性指数，称为 Morse 指标。

**依赖的概念**：临界点、非退化性、Hessian、Hadamard 引理、惯性指数、局部坐标变换。

## 思考过程

Morse 引理的证明有两个技术支点。第一是 **Hadamard 引理**：任何在原点附近光滑、且 $f(0)=0$ 的函数都可以写成"二次型形式"

$$
f(x)=\sum_{i,j=1}^{n}x_ix_j\,a_{ij}(x),
$$

其中 $a_{ij}$ 光滑且对称，$a_{ij}(0)=\frac12\,\partial_i\partial_j f(0)$。这一步把"到处都是高阶项"的 Taylor 余项整理成一个光滑的二次型，Hessian 非退化就变成了"矩阵 $A(0)=(a_{ij}(0))$ 可逆"。

第二是 **配方法**：既然 $A(0)$ 可逆，就有某个对角元 $a_{11}(0)\ne0$（必要时先作线性坐标变换）。于是可以把含 $x_1$ 的全部项凑成一个完全平方 $a_{11}(x)\big(x_1+\sum_{j>1}c_j(x)x_j\big)^2$，其余部分只含 $x_2,\dots,x_n$。把方括号设为新坐标 $y_1$，这是局部微分同胚（因 $a_{11}(0)\ne0$），问题就降一维。归纳 $n$ 次即得对角形式，最后伸缩坐标把系数变成 $\pm1$，负号个数由惯性定律固定为 $k$。

## 证明过程

**步骤 1：归一化与 Hadamard 引理。**

经平移与坐标变换可设 $p=0$、$f(0)=0$、$\mathrm df_0=0$。对 $t\in[0,1]$ 记 $g(t)=f(tx)$，则

$$
f(x)=g(1)-g(0)=\int_0^1 g'(t)\,\mathrm dt=\int_0^1\sum_i x_i\,\partial_i f(tx)\,\mathrm dt=\sum_i x_i\,b_i(x),
$$

其中 $b_i(x)=\int_0^1\partial_i f(tx)\,\mathrm dt$ 光滑。对 $b_i$ 再作一次同样分解（用 $b_i(0)=\partial_i f(0)=0$）：

$$
b_i(x)=\sum_j x_j\int_0^1\partial_j b_i(sx)\,\mathrm ds=\sum_j x_j\,a_{ij}(x).
$$

于是

$$
f(x)=\sum_{i,j}x_ix_j\,a_{ij}(x),\qquad a_{ij}(x)=\int_0^1\!\!\int_0^1 t\,\partial_i\partial_j f(tsx)\,\mathrm ds\,\mathrm dt.
$$

取 $a_{ij}$ 对称化后，有 $a_{ij}(0)=\frac12\partial_i\partial_j f(0)$，故矩阵 $A(0)=(a_{ij}(0))$ 恰好是 $\frac12\mathrm{Hess}_0 f$，非退化。

**步骤 2：线性变换使对角元非零。**

$A(0)$ 可逆，故存在 $v$ 使 $v^{\mathrm T}A(0)v\ne0$。取线性坐标变换把 $v$ 变到第一个基向量，则新坐标下仍成立同型的二次型分解且 $a_{11}(0)\ne0$。以下设 $a_{11}(0)\ne0$，从而在原点某邻域内 $a_{11}(x)\ne0$。

**步骤 3：完成平方。**

把二次型按 $x_1$ 分组：

$$
f(x)=a_{11}(x)\left(x_1+\sum_{j>1}\frac{a_{1j}(x)}{a_{11}(x)}x_j\right)^2+\sum_{i,j>1}\tilde a_{ij}(x)\,x_ix_j,
$$

其中 $\tilde a_{ij}=a_{ij}-\dfrac{a_{i1}a_{1j}}{a_{11}}$ 光滑（在 $a_{11}\ne0$ 处）。令

$$
y_1=\sqrt{|a_{11}(x)|}\Big(x_1+\sum_{j>1}\tfrac{a_{1j}(x)}{a_{11}(x)}x_j\Big),\qquad y_j=x_j\ (j>1).
$$

因 $a_{11}(0)\ne0$，映射 $x\mapsto y$ 在原点的 Jacobi 行列式非零，由逆映射定理它是局部微分同胚。

**步骤 4：降维与归纳。**

在新坐标下

$$
f(x)=\mathrm{sgn}(a_{11}(0))\,y_1^2+\tilde f(y_2,\dots,y_n),
$$

其中 $\tilde f$ 是 $(y_2,\dots,y_n)$ 的光滑函数，且由 $0$ 是 $f$ 的临界点知 $0$ 也是 $\tilde f$ 的临界点，其 Hessian 为 $A$ 在 $x_1$-方向消去后剩下的 $(n-1)\times(n-1)$ 主子式对应部分，仍然非退化。对 $n$ 归纳，得

$$
f=\sum_{i=1}^n \mathrm{sgn}(a^{(i)}_{ii}(0))\,z_i^2
$$

（必要时对每个坐标作伸缩 $z_i\mapsto |a_{ii}|^{-1/2}z_i$ 使系数变为 $\pm1$）。

**步骤 5：符号个数不变。**

所得形式 $-z_1^2-\cdots-z_k^2+z_{k+1}^2+\cdots+z_n^2$ 中负系数个数 $k$ 等于 Hessian 的负惯性指数。由 Sylvester 惯性定律，惯性指数在任意可逆线性变换下不变；而任意两个光滑坐标变换在原点的微分都是可逆线性变换，故 $k$ 与坐标选取无关。$\square$

**推论**：非退化临界点是孤立的；且 Morse 函数是 $C^\infty$ 拓扑下的通有（generic，即在 $C^\infty$ 中稠密）性质，故流形上总存在 Morse 函数。

## 课堂问答

**老师**：Morse 引理把 $f$ 局部化为平方和，负号个数 $k$ 为什么与坐标无关？

**学生**：结论：$k$ 等于 Hessian 的负惯性指数。理由：先由 Hadamard 引理写成 $f=x_ix_j a_{ij}(x)$，$a_{ij}(0)=\frac12\partial_i\partial_j f(0)$；完成平方后所用坐标变换的微分是可逆线性变换，由 Sylvester 惯性定律负系数个数不变。常见误区：以为 $k$ 依赖配方技巧。

**老师（追问）**：配方法为何能逐维降下去且保持非退化？

**学生**：因 $a_{11}(0)\ne0$（必要时先作线性变换保证），令 $y_1=\sqrt{|a_{11}|}(x_1+\sum_{j>1}\frac{a_{1j}}{a_{11}}x_j)$ 的 Jacobi 非零，是局部微分同胚；剩下 $(n-1)$ 元函数的 Hessian 是原 Hessian 去掉该方向的主子式，仍非退化，故可归纳。

**老师（拓展）**：Morse 引理在物理里最典型的用途是什么？

**学生**：把非退化临界点邻域化为谐振子（Witten 的 Morse 理论）。$k$ 个下降方向贡献 $+t$、$n-k$ 个上升方向贡献 $-t$，零能态计数给出 Morse 不等式 $c_k\ge b_k$。

## 相关条目

- [Witten的Morse理论](./Witten的Morse理论.md)：用 de Rham 复形的形变与超对称量子力学重推 Morse 不等式，其局部计算以 Morse 引理为出发点。
- [Hamiltonian力学与辛几何](./Hamiltonian力学与辛几何.md)：Morse 函数常被用作辛流形上的 Hamilton 函数，其临界点对应平衡位置。
