# minimax 不等式

> **一句话大白话**：在"我先选还是你先选"的问题里，先选的人只能占便宜——先取最小再取最大（$\sup\inf$）永远不超过先取最大再取最小（$\inf\sup$）；凸凹结构下两者恰好相等，于是对偶、博弈都能"换序"。
>
> **小例子**：取 $f(x,y)=(x-y)^2$，$x,y\in[0,1]$。对固定 $y$ 有 $\inf_x f=0$，故 $\sup_y\inf_x f=0$；而对固定 $x$，$\sup_y f=\max(x^2,(1-x)^2)$，其最小值在 $x=1/2$ 处为 $1/4$。于是 $0\le1/4$，不等号严格——缺少凸凹结构时等号确实不成立。

## 一、定理介绍

> **前置依赖**：弱极小极大不等式、凸函数与凸集、确界原理、凸集分离定理。

minimax 不等式指关于"取极值换序"的一整套结论，最核心的是两条：一般情形下的**不等式** $\sup_y\inf_x f(x,y)\le\inf_x\sup_y f(x,y)$（它只用到量词逻辑，不需要任何结构假设），以及凸-凹-紧条件下的**等式**（von Neumann–Sion 极小极大定理）。这条不等式在优化中扮演双重角色：把 Lagrange 函数 $L(x,\lambda,\nu)$ 代入、让 $x$ 取极小、让乘子取极大，不等式的一端就是**弱对偶性** $d^*\le p^*$；而等号成立时就是**强对偶性** $p^*=d^*$。在博弈论中，两端分别是"行玩家的保障值"与"列玩家的保障值"，等号即博弈值存在。本条目给出不等式的完整证明，并在有限维（矩阵博弈）情形给出强形式的完整证明，最后陈述一般的 Sion 定理及其证明要点。

## 二、原理思路

1. 不等号方向完全由量词决定：对每个固定的点 $(x,y)$ 有 $\inf_x f\le f(x,y)\le\sup_y f$，沿两个方向各取一次确界即得 $\sup_y\inf_x f\le\inf_x\sup_y f$。
2. 反向不等式的困难在于：$\inf_x\sup_y f$ 允许每个 $x$ 配一个不同的 $y$，而 $\sup_y\inf_x f$ 要求一个"公共的 $y$"同时对付所有 $x$；把分散的见证合并为一个公共见证，正是凸性/凹性与紧性的用武之地。
3. 对固定 $y$，$x\mapsto f(x,y)$ 的下水平集是凸集；对固定 $x$，$y\mapsto f(x,y)$ 的（凹函数）下水平集也是凸集，这些凸集给了分离定理或不动点论证的原料。
4. 有限矩阵博弈情形可以用**凸集分离定理**直接完成：把"列玩家能否把收益压到 $v$ 以下"翻译成两个不相交凸集的可分离性，分离泛函归一化后就是一个行玩家的混合策略。
5. 一般情形（Sion 定理）用 KKM 型不动点/有限交论证替代分离，本质仍是"把有限个见证用凸组合黏成公共见证"。

## 三、定理的严格表述

设 $X,Y$ 为非空集合，$f:X\times Y\to\mathbb R$。

**定理 1（minimax 不等式）**：

$$
\sup_{y\in Y}\inf_{x\in X}f(x,y)\le\inf_{x\in X}\sup_{y\in Y}f(x,y).
$$

**定理 2（有限矩阵博弈的极小极大定理）**：设 $A\in\mathbb R^{m\times n}$，$\Delta_m,\Delta_n$ 分别为 $\mathbb R^m,\mathbb R^n$ 中的概率单纯形。则

$$
\max_{q\in\Delta_n}\min_{p\in\Delta_m}p^{\top}Aq
=\min_{p\in\Delta_m}\max_{q\in\Delta_n}p^{\top}Aq .
$$

共同值称为该零和博弈的**值**。

**定理 3（Sion 极小极大定理）**：设 $X\subseteq\mathbb R^n$、$Y\subseteq\mathbb R^m$ 为非空紧凸集，$f:X\times Y\to\mathbb R$ 连续，且对每个 $y\in Y$，$f(\cdot,y)$ 在 $X$ 上凸；对每个 $x\in X$，$f(x,\cdot)$ 在 $Y$ 上凹。则

$$
\min_{x\in X}\max_{y\in Y}f(x,y)=\max_{y\in Y}\min_{x\in X}f(x,y).
$$

## 四、证明过程

**定理 1 的证明。** 对任意 $x\in X$、$y\in Y$，由下确界与上确界的定义，

$$
\inf_{x'\in X}f(x',y)\le f(x,y)\le\sup_{y'\in Y}f(x,y').
$$

固定 $y$，左端只依赖 $y$，于是对一切 $x$ 有 $\sup_{y'}f(x,y')\ge\inf_{x'}f(x',y)$；两边对 $x$ 取下确界（下确界保持不等号），再对 $y$ 取上确界（左端已不含 $y$）即得定理 1。

**定理 2 的证明。** 记 $v:=\max_{q\in\Delta_n}\min_{p\in\Delta_m}p^{\top}Aq=\max_q\min_i(Aq)_i$，由 $\Delta_n$ 紧与 $q\mapsto\min_i(Aq)_i$ 连续，最大值可达（确界原理 + 紧集上连续函数取到极值）。

*方向一（$\le$，弱不等式）*：对任意 $p,q$ 有 $\min_i(Aq)_i\le p^{\top}Aq\le\max_j(A^{\top}p)_j$，先对 $p$ 取 max、再对 $q$ 取 min 得

$$
v=\max_{q}\min_{i}(Aq)_i\le\min_{p}\max_{j}(A^{\top}p)_j=\min_{p\in\Delta_m}\max_{q\in\Delta_n}p^{\top}Aq .
$$

*方向二（$\ge$）*：只需证存在 $p^*\in\Delta_m$ 使 $(A^{\top}p^*)_j\le v$ 对一切 $j$ 成立。反设不然，即对每个 $p\in\Delta_m$ 都存在 $j$ 使 $(A^{\top}p)_j>v$。令

$$
D:=\{A^{\top}p:p\in\Delta_m\}\subseteq\mathbb R^n,\qquad
E:=\{t\in\mathbb R^n:t_j\le v\ \forall j\}=v\mathbf 1-\mathbb R^n_+,
$$

则 $D$ 是紧凸集、$E$ 是闭凸集且 $D\cap E=\varnothing$。由凸集分离定理（强分离形式），存在 $u\in\mathbb R^n\setminus\{0\}$ 与实数 $c$ 使

$$
\sup_{t\in E}\langle u,t\rangle<c<\inf_{d\in D}\langle u,d\rangle .
$$

因 $E=v\mathbf 1-\mathbb R^n_+$ 无界而 $\sup_{t\in E}\langle u,t\rangle$ 有限，必有 $u\ge0$（否则沿 $-\mathbb R^n_+$ 的某方向泛函值趋向 $+\infty$）；把 $u$ 归一化使 $\sum_i u_i=1$，即 $u\in\Delta_n$。此时

$$
\sup_{t\in E}\langle u,t\rangle=\Bigl\langle u,v\mathbf 1-\mathbb R^n_+\Bigr\rangle_{\sup}=v .
$$

于是 $\min_p\langle u,A^{\top}p\rangle=\inf_{D}\langle u,\cdot\rangle>v$，即

$$
\min_{i}(Au)_i=\min_{p\in\Delta_m}u^{\top}Ap>v=\max_{q\in\Delta_n}\min_i(Aq)_i,
$$

但 $u\in\Delta_n$ 本身是一个合法的 $q$，矛盾。故这样的 $p^*$ 存在，方向二得证。两个方向合并即得定理 2。

**定理 3 的证明要点。** $\le$ 方向仍是定理 1。$\ge$ 方向（构造公共的 $x^*$）可用如下标准论证：对 $\gamma>\max_y\min_x f$，由定理 1 的记号可知对每个 $y$ 存在 $x$ 使 $f(x,y)<\gamma$；把 $x\mapsto f(x,y)$ 的下水平集 $\{x:f(x,y)\le\gamma\}$（闭凸）作为一族闭凸集，用**有限交性质**论证其交非空：若有限个这样的集合交为空，则对相应有限个 $y_1,\dots,y_m$ 与任意凸组合 $y=\sum\lambda_jy_j$，由凹性 $f(x,y)\ge\sum\lambda_jf(x,y_j)$ 与凸性 $f\bigl(\sum\lambda_ix_i,y\bigr)\le\sum\lambda_if(x_i,y)$ 可导出与"每个 $y$ 都有见证 $x$"矛盾；由 $X$ 的紧性，全部约束相容，得到 $x^*$ 满足 $f(x^*,y)\le\gamma$ 对一切 $y$，再令 $\gamma\downarrow\max_y\min_x f$ 即得。这一"黏合见证"的论证通常以 KKM（Knaster–Kuratowski–Mazurkiewicz）引理或等价的 Brouwer 不动点定理形式陈述；细化的推导可参见 [极小极大定理](./极小极大定理.md) 中对 von Neumann 原始证明的整理。

## 五、应用与意义

- **对偶理论**：把 $f$ 取为 Lagrange 函数，定理 1 即弱对偶 $d^*\le p^*$；定理 3 的等号版本在凸性与 Slater 条件下给出强对偶，见 [凸优化对偶理论](./凸优化对偶理论.md)。
- **博弈论**：定理 2 说明有限零和博弈的混合策略值唯一存在，双方的最优策略分别由 $p^*,q^*$ 给出；它是纳什均衡存在性在零和情形的定量版本。
- **稳健与鲁棒优化**：最坏情形目标 $\min_x\max_{\xi\in\Xi}f(x,\xi)$ 在 $f$ 凸-凹时等于 $\max_{\xi}\min_x f(x,\xi)$，于是可把难解的 $\min\max$ 换成较易的 $\max\min$。
- **统计决策与在线学习**：最坏风险的下界、遗憾界中 $\sup\inf$ 与 $\inf\sup$ 的互换都以此为依据。

## 相关条目

- [弱极小极大不等式](./弱极小极大不等式.md)：定理 1 的另一表述，并含逐点论证的细节。
- [函数的逐点不等式](./函数的逐点不等式.md)：定理 1 所依赖的确界引理。
- [极小极大定理](./极小极大定理.md)：von Neumann 原始形式的完整梳理。
