# Farkas引理

> **一句话大白话**：对一个线性方程组，"存在非负解"与"存在一个把右端项打成负数的对偶非负向量"这两件事恰好一件成立、另一件必然不成立。

> **小例子**：取 $A=\begin{pmatrix}1\\-1\end{pmatrix}$、$b=\begin{pmatrix}1\\1\end{pmatrix}$。方程 $x=b_1$ 与 $-x=b_2$ 要求 $x=1$ 且 $x=-1$，无非负解。取 $y=(1,1)$，则 $A^{\top}y=1-1=0\ge0$ 而 $b^{\top}y=1+1=2>0$；改取 $y=(-1,-1)$ 即得 $b^{\top}y=-2<0$，正是引理断言的那条"不可行证书"。

## 一、定理介绍

> **前置依赖**：凸锥、Hahn-Banach几何形式、Carathéodory定理、线性规划的对偶理论、线性规划基本定理。

Farkas 引理由匈牙利数学家 Gyula Farkas（1847–1930）在 1902 年发表的论文《Theorie der einfachen Ungleichungen》（简单不等式理论）中提出。Farkas 的本职工作是理论物理，他在研究力学系统的平衡条件、特别是 Fourier 关于机械系统约束的讨论时，遇到了如下问题：一组齐次线性不等式的非负组合何时能表示某个给定线性形式？这一纯粹的代数问题促使他建立了后来被称为"择一定理"（theorem of the alternative）的原型。

这个引理之所以重要，是因为它给出了线性规划对偶理论的基石。线性规划的基本问题是：在约束 $Ax\ge b$、$x\ge0$ 下最大化 $c^{\top}x$，其最优性可以用"存在非负乘子 $y$ 使 $A^{\top}y\ge c$、$b^{\top}y\le c^{\top}x$"来刻画，而这正是 Farkas 引理的直接推论。Von Neumann、Dantzig、Gale 等人在 20 世纪 40–50 年代把 Farkas 引理重新发现并系统化，Gale 的"择一定理"与 Motzkin 定理、Gordan 定理共同构成线性不等式的可解性理论。今天，Farkas 引理在运筹学中用于生成不可行性证书（infeasibility certificate），在计算几何中用于判定点是否落在凸锥内，在组合优化中用于刻画多面体的面结构。

## 二、原理思路

1. 把问题的左侧 $\{Ax:x\ge0\}$ 看成 $\mathbb{R}^{m}$ 中的一个集合。由于 $x$ 取遍非负象限而 $A$ 只有有限列，这个集合恰是矩阵 $A$ 各列的非负组合全体，即一个**有限生成凸锥** $C$。

2. 有限生成凸锥是闭集。于是"$b\notin C$"时，可以把点 $b$ 与闭凸集 $C$ 分离开：存在非零向量 $w$ 使 $\langle w,c\rangle\le\gamma<\langle w,b\rangle$ 对一切 $c\in C$ 成立。

3. 利用 $C$ 是锥（对正数倍封闭）这一额外结构，把上一步的分离加强为"锥式分离"：$\langle w,c\rangle\le0$ 对一切 $c\in C$ 且 $\langle w,b\rangle>0$；取 $y=-w$ 并把 $c$ 取为 $A$ 的各列，即得 $A^{\top}y\ge0$、$b^{\top}y<0$。

## 三、定理的严格表述

设 $A\in\mathbb{R}^{m\times n}$、$b\in\mathbb{R}^{m}$。则以下两个命题**恰有一个**成立：

$$
\text{(I)}\quad\exists\,x\in\mathbb{R}^{n},\ x\ge0,\ \text{使得 }Ax=b ;
$$

$$
\text{(II)}\quad\exists\,y\in\mathbb{R}^{m},\ \text{使得 }A^{\top}y\ge0\ \text{且}\ b^{\top}y<0 .
$$

等价地，$b$ 属于锥 $C=\{Ax:x\ge0\}$ 当且仅当不存在满足 $A^{\top}y\ge0$、$b^{\top}y<0$ 的 $y$；后者即"$b\notin C$"的代数证书。

## 四、证明过程

**步骤 1（$C$ 是有限生成凸锥）。** 令 $C=\{Ax:x\ge0\}$。若 $c_1,c_2\in C$ 与 $\lambda\ge0$，则 $c_1=A x_1$、$c_2=Ax_2$，$x_1,x_2\ge0$，于是 $\lambda c_1+c_2=A(\lambda x_1+x_2)$ 且 $\lambda x_1+x_2\ge0$，故 $\lambda c_1+c_2\in C$。又 $0\in C$。因此 $C$ 是凸锥，且由 $A$ 的有限个列向量生成，是有限生成凸锥。

**步骤 2（$C$ 是闭集）。** 记 $A$ 的列为 $a_1,\dots,a_n$，则 $C=\left\{\sum_{j=1}^{n}x_j a_j:x_j\ge0\right\}$。由凸锥的 Carathéodory 定理，$C$ 中每个元素都可写成至多 $m$ 个线性无关列向量的非负组合。把 $\{1,\dots,n\}$ 的所有至多 $m$ 元的子集记为 $S_1,\dots,S_{N}$（有限多个），对每个 $S_r$ 令 $C_r=\left\{\sum_{j\in S_r}x_j a_j:x_j\ge0\right\}$。当 $\{a_j\}_{j\in S_r}$ 线性无关时，$C_r$ 是闭集（映射 $x\mapsto\sum_{j\in S_r}x_j a_j$ 在该坐标子空间上是到其像的同胚）；否则 $C_r$ 可继续分解。于是 $C=\bigcup_{r}C_r$ 是有限个闭集的并，故 $C$ 闭。

**步骤 3（点与闭凸锥的分离）。** 若 $b\notin C$，由凸集分离定理（点与闭凸集分离），存在 $w\ne0$ 与实数 $\gamma$ 使

$$
\langle w,c\rangle\le\gamma<\langle w,b\rangle\qquad\text{对一切 }c\in C .
$$

**步骤 4（锥式加强）。** 因 $0\in C$，取 $c=0$ 得 $\gamma\ge0$。又对任意 $c\in C$ 与 $t>0$，由锥性 $tc\in C$，于是

$$
t\,\langle w,c\rangle=\langle w,tc\rangle\le\gamma\qquad\Longrightarrow\qquad \langle w,c\rangle\le\frac{\gamma}{t}\quad\text{对一切 }t>0 .
$$

令 $t\to\infty$ 得 $\langle w,c\rangle\le0$ 对一切 $c\in C$。于是 $\sup_{c\in C}\langle w,c\rangle\le0$，又 $0\in C$ 知该上确界为 $0$，故可取 $\gamma=0$，即

$$
\langle w,c\rangle\le0\ \ (c\in C),\qquad \langle w,b\rangle>0 .
$$

**步骤 5（化为矩阵形式）。** 取 $y=-w\ne0$，则上两式变为

$$
\langle y,c\rangle\ge0\ \ (c\in C),\qquad \langle y,b\rangle<0 .
$$

在第一个不等式中取 $c=A e_j$（$e_j$ 为标准基向量，$e_j\ge0$），得 $\langle y,a_j\rangle\ge0$ 对每个列 $a_j$ 成立，等价于 $A^{\top}y\ge0$；第二个不等式即 $b^{\top}y<0$。这就证明了：$b\notin C$ 时命题 (II) 成立。

**步骤 6（两者不能同时成立）。** 设 (I) 与 (II) 同时成立，即 $Ax=b$、$x\ge0$、$A^{\top}y\ge0$、$b^{\top}y<0$。则

$$
b^{\top}y=(Ax)^{\top}y=x^{\top}\left(A^{\top}y\right)=\sum_{j=1}^{n}x_j\left(A^{\top}y\right)_j\ge0 ,
$$

因为 $x_j\ge0$ 且 $(A^{\top}y)_j\ge0$。这与 $b^{\top}y<0$ 矛盾。故 (I)、(II) 至多一个成立；结合步骤 5，恰有一个成立。$\square$

## 五、应用与意义

- 线性规划对偶：强对偶定理、互补松弛条件的证明都以 Farkas 引理为工具；最优解的对偶变量可解释为资源的影子价格。
- 不可行性证书：当线性可行性问题 $Ax=b$、$x\ge0$ 无解时，引理给出的 $y$ 是一份可快速验证的证书，是单纯形法与内点法中"证明无解"的标准手段。
- 组合优化：用于刻画多面体的面、证明整数规划松弛的紧性，以及最大流最小割等定理的对偶证明。
- 计算几何：判定点是否在有限生成锥或凸包内，等价于求解 Farkas 型线性系统。

## 相关条目

- [凸锥与凸集分离定理](./凸锥与凸集分离定理.md)：把分离定理专门化到凸锥，是 Farkas 引理证明的直接工具。
- [线性规划强对偶定理](./线性规划强对偶定理.md)：以 Farkas 引理为核心证明对偶间隙为零。
- [最大流最小割定理](./最大流最小割定理.md)：网络流中的对偶结论，可由 Farkas 型论证导出。
- [分支定界算法的收敛性](./分支定界算法的收敛性.md)：剪枝依赖线性松弛的对偶界。
- [凸集分离定理](../第109级-优化理论/凸集分离定理.md)：本引理的几何来源。
- [线性规划的对偶定理](../第109级-优化理论/线性规划的对偶定理.md)：对偶可行性与最优性的系统理论。
- [线性规划基本定理](../第66级-数学优化与凸优化/线性规划基本定理.md)：多面体顶点最优性的基础结果。
- [凸多面体理论](../第70级-离散几何与凸几何/凸多面体理论.md)：有限生成锥与多面体的结构理论。
