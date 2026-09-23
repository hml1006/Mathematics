# Poisson括号与Jacobi恒等式

> **一句话大白话**：Poisson 括号把两个物理量"配对"出第三个量，它衡量的是它们生成的流彼此"拧"得多厉害；Jacobi 恒等式则保证这种配对不会自相矛盾，让所有物理量井然有序地构成一个李代数的乘法表。
>
> **小例子**：对位置与动量，$\{q_i,p_j\}=\delta_{ij}$、$\{q_i,q_j\}=\{p_i,p_j\}=0$；角动量分量满足 $\{L_x,L_y\}=L_z$，其三循环和恰为零，这正是量子力学 $[L_x,L_y]=i\hbar L_z$ 的经典原型。

## 介绍

Poisson 括号（Poisson bracket）是经典力学中描述物理量之间代数关系的基本运算，由 Siméon Denis Poisson 于 1809 年在研究摄动理论时引入。在辛流形 $(M,\omega)$ 上，对光滑函数 $f,g$ 定义

$$
\{f,g\}=\omega(X_f,X_g),
$$

其中 $X_f$ 是由 $\iota_{X_f}\omega=\mathrm{d}f$ 确定的 Hamilton 向量场。在局部正则坐标 $(q,p)$ 下它化为教科书形式

$$
\{f,g\}=\sum_{i=1}^n\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right).
$$

Jacobi 恒等式（Jacobi identity）断言此括号满足三循环求和为零：

$$
\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0.
$$

它使 $\big(C^\infty(M),\{\ ,\ \}\big)$ 成为一个无穷维李代数，是 Hamilton 力学与量子力学对应的代数骨架：经典 Poisson 括号与量子对易子的"$\{\cdot,\cdot\}\to\frac{1}{i\hbar}[\cdot,\cdot]$"对应正是 Dirac 量化规则的表述。

## 分析

辛流形与闭的非退化 2-形式、Hamilton 向量场、外微分与 Cartan 公式、乘积求导法则、李括号与向量场的自然性。

**定理内容**：设 $(M,\omega)$ 为辛流形，$\{f,g\}=\omega(X_f,X_g)$。则括号 $\{\ ,\ \}$ 是 $\mathbb R$-双线性的、反称的，并且在每个变量上是导子（满足 Leibniz 法则）；更重要的是对一切 $f,g,h\in C^\infty(M)$ 成立 Jacobi 恒等式

$$
\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0.
$$

等价刻画：$\omega$ 闭（$\mathrm{d}\omega=0$）当且仅当 Jacobi 恒等式成立。

**依赖的概念**：辛形式、Hamilton 向量场、Poisson 双向量、导子、三循环求和 $\mathrm{Jac}(f,g,h)$。

## 思考过程

有两条互补的路线。**路线一（坐标硬算）**：在 Darboux 坐标下直接展开。由于括号对每个变量都是导子，而一切光滑函数可由坐标函数 $q_i,p_j$ 经加、乘生成，因此只要在坐标函数上验证 Jacobi 恒等式即可——而在坐标函数上括号取值仅为常数 $0$ 或 $\delta_{ij}$，三循环和显然为零。这一"先验证生成元、再用导性延拓"的策略把无穷多项的硬算压缩成几次检查。

**路线二（几何不变式）**：用 Cartan 公式把 Jacobi 三循环和识别为 $\mathrm{d}\omega$ 在三个 Hamilton 向量场上的一次求值：

$$
\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=\mathrm{d}\omega(X_f,X_g,X_h).
$$

于是 Jacobi 恒等式与辛形式的闭性完全等价，这揭示了"辛"的本质：它不是坐标条件，而是一条代数自洽性。

## 证明过程

**步骤 1：括号的基本性质。**

由 $\omega$ 的双线性与反称性，$\{\ ,\ \}$ 双线性且反称。又 $X_f$ 对 $f$ 是线性的，且 $X_{fg}=fX_g+gX_f$（因为 $\mathrm{d}(fg)=f\,\mathrm{d}g+g\,\mathrm{d}f$，而 $\iota$ 对函数是 $C^\infty$-线性的），据此

$$
\{f,gh\}=\omega(X_f,gX_h+hX_g)=g\{f,h\}+h\{f,g\},
$$

即括号在每个变量上满足 Leibniz 法则（是导子）。

**步骤 2：在正则坐标下写出括号并正定其结构。**

取 Darboux 坐标 $(q_1,\dots,q_n,p_1,\dots,p_n)$，$\omega=\sum_i \mathrm{d}q_i\wedge\mathrm{d}p_i$。则

$$
X_f=\sum_i\left(\frac{\partial f}{\partial p_i}\frac{\partial}{\partial q_i}-\frac{\partial f}{\partial q_i}\frac{\partial}{\partial p_i}\right),\qquad
\{f,g\}=\sum_i\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right).
$$

由此立刻得到基本括号关系

$$
\{q_i,q_j\}=0,\qquad \{p_i,p_j\}=0,\qquad \{q_i,p_j\}=\delta_{ij}.
$$

**步骤 3：定义 Jacobiator 并证明它是每个变量的导子。**

令

$$
\mathrm{Jac}(f,g,h)=\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}.
$$

对固定的 $g,h$，映射 $f\mapsto\mathrm{Jac}(f,g,h)$ 是三块之和：$\{f,\{g,h\}\}$ 是 $f$ 的导子（步骤 1）；$\{g,\{h,f\}\}=\{g,\cdot\}\circ\{h,\cdot\}(f)$ 是"导子的复合减去..."，逐项展开可验证它同样关于 $f$ 满足 Leibniz 法则；$\{h,\{f,g\}\}$ 同理。故 $\mathrm{Jac}$ 在第一个变量上是导子；由 $\mathrm{Jac}$ 的反称对称性，它在三个变量上都各是导子。

**步骤 4：在坐标函数上验证。**

只需代入生成元。取 $f=g=h=q_i$：三项均为 $\{q_i,0\}=0$。取 $f=g=q_i,\ h=p_j$：

$$
\{q_i,\{q_i,p_j\}\}+\{q_i,\{p_j,q_i\}\}+\{p_j,\{q_i,q_i\}\}=\{q_i,\delta_{ij}\}+\{q_i,-\delta_{ij}\}+0=0.
$$

其余各种组合（三个坐标两两相同或互异）都因基本括号是常数（$0$ 或 $\delta$）而使三循环和为零。故 $\mathrm{Jac}$ 在所有 $(q_i,p_j)$ 的三元组上取零。

**步骤 5：由导性延拓到一切光滑函数。**

固定 $g,h$，$D(f)=\mathrm{Jac}(f,g,h)$ 是导子且在 $q_i,p_j$ 上为零。导子满足乘法法则，故 $D$ 在 $q_i,p_j$ 生成的多项式代数上为零；又 $D$ 是局部算子（由括号的局部性），在每个坐标卡内用 Weierstrass 逼近/单位分解，$D$ 在一切 $C^\infty$ 函数上为零。于是对任意 $f,g,h$ 有 $\mathrm{Jac}(f,g,h)=0$，即 Jacobi 恒等式。

**步骤 6：几何等价刻画。**

用外微分的整体公式：对三个向量场 $X_f,X_g,X_h$，

$$
\mathrm{d}\omega(X_f,X_g,X_h)=X_f\,\omega(X_g,X_h)-X_g\,\omega(X_f,X_h)+X_h\,\omega(X_f,X_g)-\omega([X_f,X_g],X_h)+\omega([X_f,X_h],X_g)-\omega([X_g,X_h],X_f).
$$

利用 $[X_f,X_g]=-X_{\{f,g\}}$（Hamilton 向量场的李括号对应 Poisson 括号）与 $X_f\{g,h\}=-\{f,\{g,h\}\}$（符号取决于约定），前四项与后三项合并即得

$$
\mathrm{d}\omega(X_f,X_g,X_h)=\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}.
$$

因 $\omega$ 非退化，$\mathrm{d}\omega=0$ 当且仅当对一切 $X_f,X_g,X_h$ 右端为零，即 Jacobi 恒等式成立。$\square$

**推论**：$X_{\{f,g\}}=-[X_f,X_g]$，即 Poisson 括号对 Hamilton 向量场给出李括号；Hamilton 向量场的全体构成一个李代数。

## 相关条目

- [Hamiltonian力学与辛几何](./Hamiltonian力学与辛几何.md)：系统讲述辛形式、Hamilton 向量场与正则方程。
- [Noether定理](./Noether定理.md)：连续对称导出的守恒量，其两两 Poisson 括号给出对称群（李代数）的结构常数。
