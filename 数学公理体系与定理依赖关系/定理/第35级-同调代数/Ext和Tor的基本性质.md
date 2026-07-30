# Ext和Tor的基本性质

## 介绍

$\operatorname{Ext}$ 和 $\operatorname{Tor}$ 作为同调代数中最基本的导出函子，具有丰富的代数性质。这些性质包括长正合列、维数转移、系数变换、交换性和直和分解等，为计算和应用这两个函子提供了系统的方法。掌握这些基本性质是利用同调代数工具解决代数问题的基础。

## 分析

**前置依赖**：导出函子 $\operatorname{Ext}$ 和 $\operatorname{Tor}$ 的定义、投射分解、内射分解、正合列。

**数学内涵**：

**$\operatorname{Ext}$ 的基本性质**：
1. **长正合列**：短正合列诱导 $\operatorname{Ext}$ 的长正合列。
2. **维数迁移**：$\operatorname{Ext}^n_R(A, B) \cong \operatorname{Ext}^{n-1}_R(\Omega A, B)$，其中 $\Omega A$ 是 $A$ 的 syzygy 模。
3. **系数变换**：环同态诱导 $\operatorname{Ext}$ 的自然变换。
4. **直和与直积**：$\operatorname{Ext}^n_R(\bigoplus A_i, B) \cong \prod \operatorname{Ext}^n_R(A_i, B)$，$\operatorname{Ext}^n_R(A, \prod B_i) \cong \prod \operatorname{Ext}^n_R(A, B_i)$。
5. **$\operatorname{Ext}^1$ 与扩张**：$\operatorname{Ext}^1_R(A, B)$ 一一对应于 $B$ 被 $A$ 的扩张等价类。

**$\operatorname{Tor}$ 的基本性质**：
1. **长正合列**：短正合列诱导 $\operatorname{Tor}$ 的长正合列。
2. **对称性**：$\operatorname{Tor}_n^R(A, B) \cong \operatorname{Tor}_n^R(B, A)$（对交换环）。
3. **维数迁移**：$\operatorname{Tor}_n^R(A, B) \cong \operatorname{Tor}_{n-1}^R(\Omega A, B)$。
4. **直和**：$\operatorname{Tor}_n^R(\bigoplus A_i, B) \cong \bigoplus \operatorname{Tor}_n^R(A_i, B)$。
5. **平坦模的刻画**：$B$ 是平坦模当且仅当 $\operatorname{Tor}_1^R(-, B) = 0$。

**证明策略**：利用投射分解和内射分解的函子性，通过链复形的同调长正合列推导。

## 思考过程

$\operatorname{Ext}$ 和 $\operatorname{Tor}$ 的性质可以看作 Hom 和张量积性质的推广。例如，Hom 对直和是"反变"的：$\operatorname{Hom}(\bigoplus A_i, B) \cong \prod \operatorname{Hom}(A_i, B)$，这个性质通过导出函子提升到 $\operatorname{Ext}$ 的所有维数。

维数迁移是计算 $\operatorname{Ext}$ 和 $\operatorname{Tor}$ 的重要技巧：通过反复取 syzygy 模，可以将高维计算化归为低维计算。

$\operatorname{Ext}^1(A, B)$ 与扩张的对应关系是最直观的几何解释——它刻画了通过 $B$ 扩张 $A$ 的所有可能方式。

## 证明过程

### 性质 1：长正合列

**定理 1**：对 $R$-模的短正合列 $0 \to A \to B \to C \to 0$ 和任意 $R$-模 $M$，有长正合列：
$$
\begin{aligned}
0 &\to \operatorname{Hom}_R(C, M) \to \operatorname{Hom}_R(B, M) \to \operatorname{Hom}_R(A, M) \\
&\to \operatorname{Ext}^1_R(C, M) \to \operatorname{Ext}^1_R(B, M) \to \operatorname{Ext}^1_R(A, M) \\
&\to \operatorname{Ext}^2_R(C, M) \to \cdots
\end{aligned}
$$

**证明**：取 $M$ 的内射分解 $0 \to M \to I^0 \to I^1 \to \cdots$，将短正合列作用于 $\operatorname{Hom}_R(-, I^\bullet)$ 得到短正合列的链复形，取上同调即得长正合列。$\square$

### 性质 2：维数迁移

**定理 2**：设 $0 \to K \to P \to A \to 0$ 是正合列，其中 $P$ 是投射模，则对 $n \ge 1$：
$$
\operatorname{Ext}^n_R(A, B) \cong \operatorname{Ext}^{n-1}_R(K, B)
$$

**证明**：取 $A$ 的投射分解 $P_\bullet \to A$，则 $P_\bullet$ 与 $P$ 拼接后得到 $K$ 的投射分解。由 $\operatorname{Ext}$ 的定义直接计算可得。$\square$

类似地，对 $\operatorname{Tor}$ 有：
$$
\operatorname{Tor}_n^R(A, B) \cong \operatorname{Tor}_{n-1}^R(K, B)
$$

### 性质 3：$\operatorname{Ext}$ 与直和、直积

**定理 3**：对任意 $R$-模族 $\{A_i\}_{i \in I}$ 和模 $B$，
$$
\operatorname{Ext}^n_R\left(\bigoplus_{i \in I} A_i, B\right) \cong \prod_{i \in I} \operatorname{Ext}^n_R(A_i, B)
$$

**证明**：直和的投射分解是各投射分解的直和，$\operatorname{Hom}(\bigoplus A_i, B) \cong \prod \operatorname{Hom}(A_i, B)$ 诱导出复形的同构，取上同调即得。$\square$

### 性质 4：$\operatorname{Ext}^1$ 与扩张的分类

**定理 4**：$\operatorname{Ext}^1_R(A, B)$ 与 $B$ 被 $A$ 的扩张（即短正合列 $0 \to B \to E \to A \to 0$）的等价类一一对应。

**证明概要**：

（$\Rightarrow$）给定 $\xi \in \operatorname{Ext}^1_R(A, B)$，取 $A$ 的投射分解 $P_1 \to P_0 \to A \to 0$，则 $\xi$ 由 $f: P_1 \to B$ 表示。构造推出图可得扩张 $0 \to B \to E \to A \to 0$。

（$\Leftarrow$）给定扩张 $0 \to B \to E \to A \to 0$，其诱导的长正合列给出边界映射 $\operatorname{Hom}(B, B) \to \operatorname{Ext}^1(A, B)$，$\operatorname{id}_B$ 的像即为对应的 $\operatorname{Ext}$ 类。

两种映射互逆，且保持等价关系。$\square$

### 性质 5：$\operatorname{Tor}$ 的对称性

**定理 5**：对交换环 $R$ 上的模 $A$ 和 $B$，
$$
\operatorname{Tor}_n^R(A, B) \cong \operatorname{Tor}_n^R(B, A)
$$

**证明**：取 $A$ 的投射分解 $P_\bullet \to A$ 和 $B$ 的投射分解 $Q_\bullet \to B$，构造双复形 $P_\bullet \otimes_R Q_\bullet$，两个谱序列分别收敛到 $\operatorname{Tor}_\bullet^R(A, B)$ 和 $\operatorname{Tor}_\bullet^R(B, A)$，由极限的唯一性得同构。$\square$

### 性质 6：平坦模的刻画

**定理 6**：$R$-模 $B$ 是平坦模当且仅当 $\operatorname{Tor}_1^R(-, B) = 0$，当且仅当对所有 $n \ge 1$，$\operatorname{Tor}_n^R(-, B) = 0$。

**证明**：若 $B$ 平坦，则 $(-) \otimes_R B$ 正合，故其左导出函子为零。反之，若 $\operatorname{Tor}_1^R(-, B) = 0$，则对任意短正合列 $0 \to A' \to A \to A'' \to 0$，由长正合列：
$$
\operatorname{Tor}_1^R(A'', B) \to A' \otimes B \to A \otimes B \to A'' \otimes B \to 0
$$
由于 $\operatorname{Tor}_1^R(A'', B) = 0$，$(-) \otimes_R B$ 保持正合性，故 $B$ 平坦。$\square$

### 性质 7：系数变换

**定理 7**：设 $\varphi: R \to S$ 是环同态，$A$ 是 $R$-模，$B$ 是 $S$-模，则：
$$
\operatorname{Ext}^n_R(A, B) \cong \operatorname{Ext}^n_S(S \otimes_R A, B)
$$
其中 $B$ 通过限制视为 $R$-模。

**应用**：这些基本性质构成了同调代数计算的基础，广泛应用于代数拓扑、代数几何和表示论中。$\square$