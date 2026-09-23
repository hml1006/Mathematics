# 凸集与 Mazur 定理

> **一句话大白话**：弱收敛比强收敛"虚"，但对凸集而言两者其实一样严：一个弱收敛的序列，总能通过取适当的"加权平均"（凸组合）把它拉回范数意义下的强收敛。
>
> **小例子**：在 $\ell^2$ 中标准正交基 $e_n\rightharpoonup0$ 弱收敛却 $\lVert e_n\rVert=1$ 不强收敛；但凸组合 $\frac1N\sum_{n=1}^N e_n$ 的范数为 $N^{-1/2}\to0$，正体现了 Mazur 定理。

## 一、定理介绍

> **前置依赖**：Hahn–Banach 延拓定理、Hahn–Banach 几何形式（分离定理）、Banach–Alaoglu 定理、Krein–Milman 定理、弱拓扑与凸集概念。

Mazur 定理（Mazur's theorem）由波兰数学家 Stanisław Mazur 于 1933 年证明，是 Banach 空间几何理论的基石之一。它有两层内容：其一是"凸集在弱拓扑与范数拓扑下闭性一致"——凸集弱闭当且仅当范数闭；其二是"弱收敛列的凸组合强收敛"——若 $x_n$ 弱收敛于 $x$，则 $x$ 落在 $\{x_n\}$ 的凸包范数闭包中，且存在凸组合 $y_k=\sum_n\lambda_n^{(k)}x_n$ 使 $\lVert y_k-x\rVert\to0$。

该定理的动机来自变分法的"直接方法"（direct method in the calculus of variations）：在 Banach 空间中，能量泛函的极小化列通常只能保证弱收敛，而弱极限未必落在约束集内、也未必使泛函取极小值。Mazur 定理说明，只要约束集是凸闭的，弱极限仍在其内；只要泛函凸且弱下半连续，弱极限就是极小元。

Mazur 定理的意义在于把"弱收敛"与"强收敛"这两套语言在凸性假设下打通，是凸优化、变分不等式、PDE 弱解理论、对偶理论反复使用的工具，也与 Krein–Milman 定理、Banach–Alaoglu 定理共同构成自反空间几何的骨架。

## 二、原理思路

1. **化归为凸包闭性**：记 $C=\overline{\operatorname{conv}}\{x_n\}$，只需证明弱极限 $x$ 属于这个范数闭凸集。

2. **反证与严格分离**：若 $x\notin C$，则由 Hahn–Banach 几何形式（第二分离定理），闭凸集 $C$ 与紧凸集 $\{x\}$ 可被一张超平面严格分离。

3. **用弱收敛取矛盾**：分离超平面给出泛函 $f\in X^*$ 使 $f$ 在 $C$ 上有上界 $\gamma<f(x)$，但 $x_n\in C$ 且 $f(x_n)\to f(x)$，取极限得 $f(x)\leq\gamma$，矛盾。

4. **逼近列给出凸组合**：既然 $x\in\overline{\operatorname{conv}}$，逐次选取距 $x$ 小于 $1/k$ 的凸包元素，即得所需的有限凸组合序列。

## 三、定理的严格表述

**定理（Mazur）**：设 $X$ 是实 Banach 空间，$(x_n)\subset X$ 弱收敛于 $x$（记 $x_n\rightharpoonup x$），即对每个 $f\in X^*$ 有 $f(x_n)\to f(x)$。则
$$x\in\overline{\operatorname{conv}}\{x_n\}^{\,\lVert\cdot\rVert}.$$
更强的结论：对每个 $\varepsilon>0$，存在有限凸组合 $\sum_{n=1}^{N}\lambda_n x_n$（$\lambda_n\geq0$，$\sum\lambda_n=1$）使
$$\Big\lVert x-\sum_{n=1}^{N}\lambda_n x_n\Big\rVert<\varepsilon .$$

**推论 1（凸集的弱闭性）**：设 $C\subset X$ 为非空凸集，则 $C$ 在弱拓扑下闭当且仅当它在范数拓扑下闭。等价地，凸集的弱闭包等于其范数闭包。

**推论 2（弱下半连续凸泛函的极小元）**：设 $X$ 自反，$C\subset X$ 非空弱紧凸集，$J:X\to\mathbb R$ 凸且在弱拓扑下下半连续，则 $J$ 在 $C$ 上取到最小值。若 $J$ 严格凸，最小元唯一。

## 四、证明过程

**步骤 1（化归）。** 令
$$C=\overline{\operatorname{conv}}\{x_n\},$$
即 $\{x_n\}$ 的所有有限凸组合构成的集合的范数闭包。凸包的闭包仍为闭凸集，故 $C$ 是范数闭凸集。要证 $x\in C$。

**步骤 2（反设并严格分离）。** 反设 $x\notin C$。因 $C$ 闭凸、$\{x\}$ 紧凸且 $C\cap\{x\}=\varnothing$，由 Hahn–Banach 几何形式（严格分离定理），存在 $f\in X^*$ 与实数 $\alpha$ 使
$$f(z)<\alpha<f(x)\qquad \forall\, z\in C.$$
注意 $x_n\in C$ 对一切 $n$ 成立，故令 $\gamma=\sup_{z\in C}f(z)$ 便有 $\gamma\leq\alpha<f(x)$，且
$$f(x_n)\leq\gamma\qquad \forall\, n.$$

**步骤 3（弱收敛给出矛盾）。** 由 $x_n\rightharpoonup x$ 与 $f\in X^*$ 得 $f(x_n)\to f(x)$。对不等式 $f(x_n)\leq\gamma$ 取上极限，得
$$f(x)=\lim_{n\to\infty}f(x_n)\leq\gamma<f(x),$$
矛盾。故 $x\notin C$ 不成立，即 $x\in C$。

**步骤 4（构造凸组合逼近列）。** 由 $x\in\overline{\operatorname{conv}}\{x_n\}$，对每个 $k\geq1$ 存在 $y_k\in\operatorname{conv}\{x_n\}$ 使 $\lVert y_k-x\rVert<1/k$。按凸包的定义，$y_k$ 可写成有限凸组合
$$y_k=\sum_{n=1}^{N_k}\lambda_n^{(k)}x_n,\qquad \lambda_n^{(k)}\geq0,\quad \sum_{n=1}^{N_k}\lambda_n^{(k)}=1 .$$
于是 $\lVert y_k-x\rVert\to0$，即存在凸组合序列在范数下强收敛于 $x$。

**步骤 5（凸集弱闭性的推论）。** 弱拓扑比范数拓扑粗，其闭集族更大，故弱闭必范数闭。反之设 $C$ 凸且范数闭，取 $C$ 中弱收敛列 $x_n\rightharpoonup x$；把步骤 1 至步骤 3 应用于该序列得 $x\in\overline{\operatorname{conv}}\{x_n\}\subset C$（因为 $C$ 凸闭，包含所有 $x_n$ 的凸包及其闭包）。故 $C$ 弱序列闭；对凸集而言弱序列闭等价于弱闭，从而 $C$ 弱闭。这证明推论 1。

**步骤 6（极小元的存在性，直接方法）。** 设 $X$ 自反，$C$ 非空弱紧凸，$J$ 凸且弱下半连续。取极小化列 $x_n\in C$ 使 $J(x_n)\to m:=\inf_{C}J$。由 $C$ 弱紧，存在子列 $x_{n_k}\rightharpoonup x$ 且 $x\in C$。由弱下半连续性，
$$J(x)\leq\liminf_{k\to\infty}J(x_{n_k})=m .$$
另一方面 $x\in C$ 给出 $J(x)\geq m$，故 $J(x)=m$。若 $J$ 严格凸且 $x,y$ 都是最小元，则 $J\big(\tfrac{x+y}2\big)<\tfrac12J(x)+\tfrac12J(y)=m$，与 $m$ 为下确界矛盾，故最小元唯一。$\square$

**注**：步骤 2 的严格分离也可由 Hahn–Banach 延拓定理直接构造，这正是凸分析中"闭凸集等于半空间之交"的来源。若去掉自反性，弱紧性一般失效（如 $C^0[0,1]$ 的单位球），推论 2 不再成立。

## 五、应用与意义

- **变分法直接方法**：把"极小化列的弱极限"转化为"真正的极小元"，是椭圆方程、凸优化、最优控制解存在性证明的标准两步（弱紧 + 弱下半连续）。
- **凸优化的存在唯一性**：凸目标在凸约束下，弱紧性给存在性，严格凸给唯一性，无需任何可微性假设。
- **弱解与极限通过**：在 PDE 中把弱收敛的近似解升级为强收敛（或借助凸性把弱极限代回方程），Mazur 定理保证凸约束在极限下保持。
- **对偶理论**：与 Hahn–Banach 分离、Fenchel 对偶、Krein–Milman 定理配合，用于刻画凸集与凸锥、证明对偶间隙为零。
- **Banach 空间几何**：凸集弱闭性准则是研究自反性、弱序列完备性与 Banach–Alaoglu 定理应用的基本工具。

## 相关条目

- [对偶变分原理](./对偶变分原理.md)：以凸性与弱拓扑为语言，Mazur 定理是其取极限论证的基础。
- [Ekeland变分原理](./Ekeland变分原理.md)：把近似极小点升级为近似临界点，与 Mazur 定理同为变分法的"取极限"工具。
- [山路引理](./山路引理.md)：在非凸情形下借助 (PS) 条件恢复紧性的对照例子。
- [Hahn-Banach几何形式](../第31级-泛函分析/Hahn-Banach几何形式.md)：提供证明步骤 2 所需的严格分离定理。
- [Hahn-Banach延拓定理](../第31级-泛函分析/Hahn-Banach延拓定理.md)：分离定理的分析形式，弱收敛的定义依赖其对偶空间。
- [Banach-Alaoglu定理](../第31级-泛函分析/Banach-Alaoglu定理.md)：与自反性配合给出弱紧性，是推论 2 的前提。
- [Krein-Milman定理](../第31级-泛函分析/Krein-Milman定理.md)：从凸集的端点刻画凸集，与凸集弱闭性准则互补。
