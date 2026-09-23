# Arzelà–Ascoli 定理

> **一句话大白话**：一列连续函数能抽出"一致收敛"子列，当且仅当它们一致有界且"震动幅度一致地小"（等度连续）。
>
> **小例子**：$\{f_n(t)=t^n\}$ 在 $[0,1]$ 上一致有界，但不一致等度连续，故不能抽出**一致**收敛子列（其逐点极限在 $t=1$ 处为 $1$、其余为 $0$，不连续）。

## 介绍

在有限维空间里，"有界闭集是紧集"（Bolzano–Weierstrass）保证了有界序列必有收敛子列。函数空间是无穷维的，一致有界远不足以保证这一性质：还需要控制函数之间的"局部变化速度"，即**等度连续**。Arzelà–Ascoli 定理给出了 $C(K)$（$K$ 紧致）中相对紧性的完整判据：

$$\mathcal{F}\ \text{相对紧}\quad\Longleftrightarrow\quad\mathcal{F}\ \text{一致有界且等度连续}.$$

它是将"逐点紧性"提升为"一致紧性"的桥梁，也是常微分方程解的存在性（Peano/Euler 折线法）、复分析正规族理论（Montel 定理）、以及各类紧嵌入定理（如 Sobolev 紧嵌入的部分情形）的共同机制。

## 分析

**前置依赖**：紧致性、一致收敛与一致连续性、完备度量空间（$C(K)$ 在 $\sup$ 范数下完备）、Cantor 对角线法、紧度量空间的可分性（存在可数稠密集）。

**定理内容**：设 $(K,d)$ 是紧度量空间，$\mathcal{F}\subset C(K)$（配 $\sup$ 范数 $\|f\|_\infty=\sup_K|f|$）。则 $\mathcal{F}$ 相对紧（即闭包 $\overline{\mathcal{F}}$ 紧，等价于每个序列有在 $C(K)$ 中收敛的子列）当且仅当

1. **一致有界**：$\sup_{f\in\mathcal{F}}\|f\|_\infty<\infty$；
2. **等度连续**：对每个 $\epsilon>0$，存在 $\delta>0$ 使
$$d(x,y)<\delta\ \Longrightarrow\ |f(x)-f(y)|<\epsilon\qquad\text{对一切 }f\in\mathcal{F}.$$

## 思考过程

充分性（构造收敛子列）是定理的实质。思路分三步：

1. **降到可数点**：紧度量空间可分，取可数稠密集 $\{x_j\}$。每个 $f\in\mathcal{F}$ 在这可数点上的取值构成一个有界数列（一致有界），故用对角线法可从任一序列抽出子列，使其在**每个** $x_j$ 处收敛；
2. **把逐点收敛升级为一致收敛**：这一步正需要等度连续。给定 $\epsilon$，用等度连续把 $K$ 用有限个 $x_j$ 的小邻域覆盖；在同一小邻域内的两点上，任意两个函数值相差至多 $2\epsilon$ 加上 $x_j$ 处的差；
3. **极限连续**：一致收敛的极限保持连续性。

必要性较简单：相对紧蕴含一致有界（用有限个 $\epsilon$-球覆盖闭包），而等度连续则用"闭包中每个函数的（一致）连续性 + 有限覆盖"得到。

## 证明过程

**步骤 1：必要性。**

设 $\mathcal{F}$ 相对紧，$\overline{\mathcal{F}}$ 紧。

**（1a）一致有界**：在 $C(K)$ 中，$\epsilon=1$ 的球族覆盖紧集 $\overline{\mathcal{F}}$，故存在 $g_1,\dots,g_m\in C(K)$ 使
$$\overline{\mathcal{F}}\subset\bigcup_{i=1}^m\{g:\|g-g_i\|_\infty<1\}.$$
于是对 $f\in\mathcal{F}$，取 $i$ 使 $\|f-g_i\|_\infty<1$，得 $\|f\|_\infty\le1+\max_i\|g_i\|_\infty$，一致有界。

**（1b）等度连续**：给定 $\epsilon>0$，取 $g_1,\dots,g_m\in C(K)$ 使 $\overline{\mathcal{F}}\subset\bigcup_i\{g:\|g-g_i\|_\infty<\epsilon/3\}$。每个 $g_i$ 在紧度量空间 $K$ 上一致连续，故存在 $\delta_i>0$ 使 $d(x,y)<\delta_i\Rightarrow|g_i(x)-g_i(y)|<\epsilon/3$。取 $\delta=\min_i\delta_i>0$。则对 $f\in\mathcal{F}$，取 $i$ 使 $\|f-g_i\|_\infty<\epsilon/3$，当 $d(x,y)<\delta$ 时
$$|f(x)-f(y)|\le|f(x)-g_i(x)|+|g_i(x)-g_i(y)|+|g_i(y)-f(y)|<\frac{\epsilon}{3}+\frac{\epsilon}{3}+\frac{\epsilon}{3}=\epsilon.$$
故 $\mathcal{F}$ 等度连续。

**步骤 2：充分性——先在对角线上取收敛子列。**

设 $\mathcal{F}$ 一致有界且等度连续。因 $K$ 紧度量，$K$ 可分：存在可数稠密集 $\{x_1,x_2,\dots\}\subset K$。

取任意序列 $(f_n)\subset\mathcal{F}$。证明它有一致收敛子列。

**对角线法**：对 $x_1$，数列 $(f_n(x_1))$ 有界，故有收敛子列；对该子列再在 $x_2$ 处抽收敛子列；如此逐层抽取，得嵌套子列
$$(f_{n})\supset(f_{1,n})\supset(f_{2,n})\supset\cdots$$
使 $(f_{j,n})_n$ 在 $x_1,\dots,x_j$ 处收敛。取对角序列 $g_n=f_{n,n}$，则对每个固定的 $j$，$g_n$（$n\ge j$）是 $(f_{j,n})$ 的子列，故 $(g_n(x_j))_n$ 对每个 $j$ 收敛。

**步骤 3：充分性——升级为一致收敛（Cauchy 判据）。**

断言 $(g_n)$ 在 $C(K)$ 中是 Cauchy 列。给定 $\epsilon>0$，由等度连续取 $\delta>0$ 使 $d(x,y)<\delta\Rightarrow|f(x)-f(y)|<\epsilon$ 对一切 $f\in\mathcal{F}$。

由 $K$ 紧与 $\{x_j\}$ 稠密，可取有限个 $x_{j_1},\dots,x_{j_r}$ 使
$$K\subset\bigcup_{i=1}^{r}B(x_{j_i},\delta).$$
（理由：$\{B(x_j,\delta)\}_{j}$ 是开覆盖，紧性给出有限子覆盖。）

对每个 $i$，数列 $(g_n(x_{j_i}))_n$ 收敛，故是 Cauchy 列，存在 $N_i$ 使 $n,m\ge N_i$ 时 $|g_n(x_{j_i})-g_m(x_{j_i})|<\epsilon$。取 $N=\max_iN_i$。

任取 $x\in K$，取 $i$ 使 $d(x,x_{j_i})<\delta$。当 $n,m\ge N$ 时，由等度连续（$g_n,g_m\in\mathcal{F}$）
$$|g_n(x)-g_m(x)|\le|g_n(x)-g_n(x_{j_i})|+|g_n(x_{j_i})-g_m(x_{j_i})|+|g_m(x_{j_i})-g_m(x)|<\epsilon+\epsilon+\epsilon=3\epsilon.$$
故 $(g_n)$ 在 $\sup$ 范数下是 Cauchy 列。

**步骤 4：充分性——极限的连续性与结论。**

$C(K)$ 在 $\sup$ 范数下完备，故 $(g_n)$ 一致收敛到某 $g\in C(K)$。于是 $\mathcal{F}$ 的任一序列有在 $C(K)$ 中收敛的子列，即 $\mathcal{F}$ 相对紧。

（$g$ 的连续性由一致收敛保持：$|g(x)-g(y)|\le2\|g-g_n\|_\infty+|g_n(x)-g_n(y)|$。）

**步骤 5：等度连续条件的必要性（反例说明）。**

在 $[0,1]$ 上取 $f_n(t)=t^n$。则 $\|f_n\|_\infty\le1$ 一致有界；但等度连续失败：对 $\epsilon=\frac12$ 与任意 $\delta>0$，取 $x=(1-\frac\delta2)$ 附近的点与 $y=1$，当 $n$ 充分大时 $|f_n(x)-f_n(y)|\approx1>\epsilon$，而 $|x-y|<\delta$。故定理不适用；事实上 $(f_n)$ 的一致收敛子列不存在（其逐点极限 $g(1)=1$、$g(t)=0\ (t<1)$ 不连续，而一致收敛的极限必连续）。

**步骤 6：在复分析中的应用（Montel 定理）。**

设 $\Omega\subset\mathbb{C}$ 为区域，$\mathcal{F}$ 为 $\Omega$ 上局部一致有界的全纯函数族。对任意紧集 $K\subset\Omega$，取 $r>0$ 使 $K$ 的 $r$-邻域含于 $\Omega$。由 Cauchy 估计，对 $z,w\in K$ 与 $f\in\mathcal{F}$，
$$|f(z)-f(w)|\le\sup_K|f'|\cdot|z-w|\le\frac{M}{r}|z-w|,$$
其中 $M=\sup_{f\in\mathcal{F}}\sup_{\partial K_r}|f|<\infty$。故 $\mathcal{F}$ 在 $K$ 上等度连续且一致有界，由 Arzelà–Ascoli 定理在 $K$ 上相对紧；再用对角线法沿紧集穷竭序列 $K_1\subset K_2\subset\cdots$ 抽取子列，即得局部一致收敛子列——这正是 Montel 定理的证明骨架。

## 相关条目

- [Montel定理](./Montel定理.md)：把等度连续性作为"局部有界 ⇒ 正规族"的技术核心。
- [Weierstrass一致收敛定理](./Weierstrass一致收敛定理.md)：一致收敛子列的极限保持全纯性，是正规族理论另一半。
- [Bloch定理](./Bloch定理.md)：极值函数的存在性由正规族 + Arzelà–Ascoli 保证。
