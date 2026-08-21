# Mayer-Vietoris序列

> **一句话大白话**：要把整个空间 $X$ 拆成两片 $U$、$V$，各自和自己重叠区 $U\cap V$ 的洞都数清了，Mayer-Vietoris 序列就能像拉链一样把整个 $X$ 的洞一次拼出来——"局部知道，全局算得"。
>
> **小例子**：把环面拆成两片，再用该序列的长正合列计算，可拼出 $H_1(T^2)\cong\mathbb{Z}^2$、$H_2(T^2)\cong\mathbb{Z}$，比硬算整环面简单得多。

## 介绍

Mayer-Vietoris 序列是代数拓扑中计算同调群的最重要工具之一，由 Walther Mayer 和 Leopold Vietoris 在 20 世纪 20 年代末独立发现。它断言：若拓扑空间 $X$ 表示为两个开子集 $U$ 和 $V$ 的并，则 $U$、$V$、$U \cap V$ 和 $X$ 的同调群之间存在一个长正合序列。这个序列提供了从局部同调信息计算全局同调信息的系统方法，是计算各种空间（如球面、环面、射影空间等）同调群的核心工具。

## 分析

**前置依赖**：奇异链复形与边缘算子、短正合序列与蛇形引理、链同伦等价、细分引理

**定理的精确表述**：设 $X$ 是拓扑空间，$U, V \subset X$ 是开集，满足 $X = U \cup V$。则存在长正合序列

$$
\cdots \xrightarrow{\partial_*} H_n(U \cap V) \xrightarrow{(i_*, j_*)} H_n(U) \oplus H_n(V) \xrightarrow{k_* - l_*} H_n(X) \xrightarrow{\partial_*} H_{n-1}(U \cap V) \xrightarrow{} \cdots
$$

其中：

- $i: U \cap V \hookrightarrow U$，$j: U \cap V \hookrightarrow V$ 是包含映射；
- $k: U \hookrightarrow X$，$l: V \hookrightarrow X$ 是包含映射；
- $\partial_*$ 是连接同态（边缘同态）。

**链复形层面的序列**：在链复形层面，有短正合序列

$$
0 \to C_n(U \cap V) \xrightarrow{\varphi} C_n(U) \oplus C_n(V) \xrightarrow{\psi} C_n(U + V) \to 0,
$$

其中 $\varphi(x) = (i_\#(x), -j_\#(x))$，$\psi(x, y) = k_\#(x) + l_\#(y)$。由蛇形引理，这诱导出同调群的长正合序列。

**关键要点**：

- Mayer-Vietoris 序列是同调论中"加法原理"的体现——全局信息 = 局部信息之和 - 交的信息。
- 序列在奇异同调、胞腔同调、上同调等各种同调理论中都成立。
- 连接同态 $\partial_*$ 的几何意义：将一个闭链分解为 $U$ 部分和 $V$ 部分，然后取边界。
- 序列是正合的，即每个同态的像等于下一个同态的核。

## 思考过程

Mayer-Vietoris 序列的证明基于链复形层面的短正合序列和蛇形引理：

1. 在奇异链层面，$C_n(U \cap V)$ 可以嵌入到 $C_n(U) \oplus C_n(V)$ 中，映射为 $x \mapsto (i_\#(x), -j_\#(x))$。

2. $C_n(U) \oplus C_n(V)$ 可以映射到 $C_n(U) + C_n(V)$（由 $U$ 和 $V$ 中的奇异单形生成的链子群），映射为 $(x, y) \mapsto k_\#(x) + l_\#(y)$。

3. 关键点是 $C_n(U) + C_n(V)$ 与 $C_n(X)$ 的关系——通过"细分"技巧，可以证明包含映射 $C_n(U) + C_n(V) \hookrightarrow C_n(X)$ 是链同伦等价，因此它们有相同的同调群。

4. 由蛇形引理，链复形的短正合序列诱导出同调群的长正合序列。

## 证明过程

**证明**：我们给出 Mayer-Vietoris 序列的证明概要。

**步骤 1**：定义链复形子群。令 $C_n(U + V) = C_n(U) + C_n(V) \subset C_n(X)$，即由 $U$ 和 $V$ 中的奇异单形生成的链子群。由于 $\partial(C_n(U)) \subset C_{n-1}(U)$ 和 $\partial(C_n(V)) \subset C_{n-1}(V)$，$\{C_n(U + V)\}$ 构成 $C_*(X)$ 的子链复形。

**步骤 2**：短正合序列。定义 $\varphi: C_n(U \cap V) \to C_n(U) \oplus C_n(V)$ 为 $\varphi(x) = (i_\#(x), -j_\#(x))$。定义 $\psi: C_n(U) \oplus C_n(V) \to C_n(U + V)$ 为 $\psi(x, y) = k_\#(x) + l_\#(y)$。则

$$
0 \to C_n(U \cap V) \xrightarrow{\varphi} C_n(U) \oplus C_n(V) \xrightarrow{\psi} C_n(U + V) \to 0
$$

是短正合序列。

**步骤 3**：链同伦等价。需要证明包含映射 $C_n(U + V) \hookrightarrow C_n(X)$ 诱导同调群同构。这通过"细分引理"（subdivision lemma）证明：对任意奇异单形 $\sigma: \Delta^n \to X$，通过反复细分，可以将 $\sigma$ 表示为 $U$ 和 $V$ 中奇异单形的和（模边界）。因此 $H_n(U + V) \cong H_n(X)$。

**步骤 4**：应用蛇形引理。由链复形的短正合序列，得到同调群的长正合序列：

$$
\cdots \xrightarrow{\partial_*} H_n(U \cap V) \xrightarrow{\varphi_*} H_n(U) \oplus H_n(V) \xrightarrow{\psi_*} H_n(U + V) \xrightarrow{\partial_*} H_{n-1}(U \cap V) \xrightarrow{} \cdots
$$

利用 $H_n(U + V) \cong H_n(X)$，即得 Mayer-Vietoris 序列。$\square$

**应用**：

1. **球面 $S^n$ 的同调群**：令 $U = S^n \setminus \{N\}$（北极），$V = S^n \setminus \{S\}$（南极）。$U$ 和 $V$ 同伦于点，$U \cap V$ 同伦于 $S^{n-1}$。由 Mayer-Vietoris 序列，用归纳法可得 $H_k(S^n) = \mathbb{Z}$ 当 $k = 0$ 或 $n$，否则为 $0$。

2. **环面 $T^2$ 的同调群**：将 $T^2$ 分解为两个开环带的并，利用序列计算得 $H_0 = \mathbb{Z}$，$H_1 = \mathbb{Z} \oplus \mathbb{Z}$，$H_2 = \mathbb{Z}$。

3. **楔积 $X \vee Y$**：$H_n(X \vee Y) \cong H_n(X) \oplus H_n(Y)$ 对 $n > 0$，$H_0(X \vee Y) \cong \mathbb{Z}$。