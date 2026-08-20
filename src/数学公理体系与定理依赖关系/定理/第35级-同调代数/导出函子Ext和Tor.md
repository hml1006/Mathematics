# 导出函子Ext和Tor

> **一句话大白话**：有些测量工具（Hom、张量积）用了不"保精确"，会漏掉精度的尾巴；导出函子就是把这条尾巴系统地"算到底"，得到一组修正项 Ext 与 Tor，正如把一条误差链一口气垒到尽头。
>
> **小例子**：对短正合列 $0\to A\to B\to C\to0$，Hom 不再正合，漏出的部分正是 $\mathrm{Ext}^1$ 一环接一环串成的长正合列；张量积的对应尾巴由 $\mathrm{Tor}_n$ 接住。

## 介绍

$\operatorname{Ext}$ 和 $\operatorname{Tor}$ 是同调代数中最重要的导出函子，它们分别由 Hom 函子和张量积函子导出。$\operatorname{Ext}^n_R(A, B)$ 衡量了 Hom 函子 $\operatorname{Hom}_R(A, -)$ 或 $\operatorname{Hom}_R(-, B)$ 的右导出，而 $\operatorname{Tor}_n^R(A, B)$ 衡量了张量积函子 $(-) \otimes_R B$ 或 $A \otimes_R (-)$ 的左导出。这两个函子在模论、代数拓扑、代数几何和表示论中具有核心地位，提供了丰富的同调不变量。

## 分析

**前置依赖**：模论、投射分解与内射分解、导出函子、正合列。

**数学内涵**：

- **$\operatorname{Ext}$ 的定义**：对 $R$-模 $A$ 和 $B$，
  - 取 $A$ 的投射分解 $P_\bullet \to A \to 0$，则 $\operatorname{Ext}^n_R(A, B) = H^n(\operatorname{Hom}_R(P_\bullet, B))$。
  - 取 $B$ 的内射分解 $0 \to B \to I^\bullet$，则 $\operatorname{Ext}^n_R(A, B) = H^n(\operatorname{Hom}_R(A, I^\bullet))$。
  - 两种定义自然同构。

- **$\operatorname{Tor}$ 的定义**：对右 $R$-模 $A$ 和左 $R$-模 $B$，
  - 取 $A$ 的投射分解 $P_\bullet \to A \to 0$，则 $\operatorname{Tor}_n^R(A, B) = H_n(P_\bullet \otimes_R B)$。
  - 取 $B$ 的投射分解 $Q_\bullet \to B \to 0$，则 $\operatorname{Tor}_n^R(A, B) = H_n(A \otimes_R Q_\bullet)$。
  - 两种定义自然同构。

**证明策略**：利用投射分解和内射分解的链同伦唯一性，证明定义与分解选取无关，并建立平衡函子（balanced functor）的同构。

## 思考过程

$\operatorname{Ext}$ 和 $\operatorname{Tor}$ 的构造思路是：Hom 函子是左正合的但不是右正合的，张量积函子是右正合的但不是左正合的。为了弥补这个"缺失"，我们通过投射分解或内射分解来"解析"模，然后用同调来测量非正合的程度。

例如，短正合列 $0 \to A \to B \to C \to 0$ 诱导出 $\operatorname{Ext}$ 的长正合列：
$$
0 \to \operatorname{Hom}(C, M) \to \operatorname{Hom}(B, M) \to \operatorname{Hom}(A, M) \to \operatorname{Ext}^1(C, M) \to \cdots
$$

以及 $\operatorname{Tor}$ 的长正合列：
$$
\cdots \to \operatorname{Tor}_1(A, M) \to \operatorname{Tor}_1(B, M) \to \operatorname{Tor}_1(C, M) \to A \otimes M \to B \otimes M \to C \otimes M \to 0
$$

## 证明过程

### $\operatorname{Ext}$ 的定义与良定性

**定义 1**：设 $R$ 是环，$A$ 和 $B$ 是左 $R$-模。取 $A$ 的投射分解 $P_\bullet \to A \to 0$，定义
$$
\operatorname{Ext}^n_R(A, B) = H^n(\operatorname{Hom}_R(P_\bullet, B)), \quad n \ge 0
$$

**定理 1**：$\operatorname{Ext}^n_R(A, B)$ 的定义与投射分解的选取无关。

**证明**：设 $P_\bullet \to A$ 和 $P'_\bullet \to A$ 是两个投射分解。由比较引理，存在链映射 $f_\bullet: P_\bullet \to P'_\bullet$ 提升恒等映射 $\operatorname{id}_A$，且任意两个这样的提升链同伦。由链同伦诱导上同调群上的相同映射，故 $H^n(\operatorname{Hom}_R(P_\bullet, B)) \cong H^n(\operatorname{Hom}_R(P'_\bullet, B))$。$\square$

**定义 2**（对偶定义）：取 $B$ 的内射分解 $0 \to B \to I^\bullet$，定义
$$
\operatorname{Ext}^n_R(A, B) = H^n(\operatorname{Hom}_R(A, I^\bullet)), \quad n \ge 0
$$

**定理 2**：两种定义自然同构。

**证明**：通过构造双复形的谱序列或直接利用比较引理证明。$\square$

### $\operatorname{Tor}$ 的定义与良定性

**定义 3**：设 $R$ 是环，$A$ 是右 $R$-模，$B$ 是左 $R$-模。取 $A$ 的投射分解 $P_\bullet \to A \to 0$，定义
$$
\operatorname{Tor}_n^R(A, B) = H_n(P_\bullet \otimes_R B), \quad n \ge 0
$$

**定理 3**：$\operatorname{Tor}_n^R(A, B)$ 的定义与投射分解的选取无关。

**证明**：类似于 $\operatorname{Ext}$ 的情形，由比较引理和链同伦唯一性可得。$\square$

### 基本性质

**定理 4**（长正合列）：对短正合列 $0 \to A \to B \to C \to 0$ 和模 $M$，有长正合列：
$$
\begin{aligned}
\cdots \to \operatorname{Ext}^n_R(C, M) &\to \operatorname{Ext}^n_R(B, M) \to \operatorname{Ext}^n_R(A, M) \\
&\to \operatorname{Ext}^{n+1}_R(C, M) \to \cdots
\end{aligned}
$$

**证明**：取 $M$ 的内射分解 $0 \to M \to I^\bullet$，将短正合列作用于 $\operatorname{Hom}_R(-, I^\bullet)$ 得到短正合列的链复形，取上同调即得长正合列。$\square$

**定理 5**（低阶项）：
- $\operatorname{Ext}^0_R(A, B) \cong \operatorname{Hom}_R(A, B)$
- $\operatorname{Tor}_0^R(A, B) \cong A \otimes_R B$
- $\operatorname{Ext}^1_R(A, B)$ 分类了 $B$ 被 $A$ 的扩张
- $\operatorname{Tor}_1^R(A, B)$ 衡量了张量积的非正合性

### 计算示例

**例 1**：对于 Abel 群（$\mathbb{Z}$-模）：
- $\operatorname{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/n\mathbb{Z}, \mathbb{Z}) \cong \mathbb{Z}/n\mathbb{Z}$
- $\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m\mathbb{Z}, \mathbb{Z}/n\mathbb{Z}) \cong \mathbb{Z}/\gcd(m,n)\mathbb{Z}$

**例 2**：对于域 $k$ 上的向量空间，$\operatorname{Ext}^n_k(V, W) = 0$ 对 $n \ge 1$，$\operatorname{Tor}_n^k(V, W) = 0$ 对 $n \ge 1$。

**应用**：$\operatorname{Ext}$ 和 $\operatorname{Tor}$ 是代数拓扑中万有系数定理和 Künneth 公式的基础，也是代数几何中凝聚层上同调的基本工具。$\square$