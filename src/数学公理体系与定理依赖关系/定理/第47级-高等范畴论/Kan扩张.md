# Kan扩张

> **一句话大白话**：把"只在某个子范畴/小图上定义的函子"最优地"延伸"到更大的范畴，且带一个万有性质——它是范畴里最一般的"归纳/极限"操作，几乎所有构造（$\lim$、$\operatorname{colim}$、米田、伴随）都可以编码成 Kan 扩张。
>
> **小例子**：左 Kan 扩张 $\operatorname{Lan}_K F$ 给出从 $C$ 延伸 $F$ 的最左候选；而"沿箭头求余极限"正是沿米田嵌入的那类 Kan 扩张，涵盖大量经典构造。

## 介绍

Kan扩张（Kan Extension）是范畴论中一个极为重要的概念，由 Daniel M. Kan 提出。它提供了一种统一的方式来"延伸"一个函子沿着另一个函子，是范畴论中许多构造（如伴随函子、极限、Yoneda嵌入等）的通用框架。粗略地说，给定函子 $F: \mathcal{A} \to \mathcal{E}$ 和 $K: \mathcal{A} \to \mathcal{B}$，$F$ 沿 $K$ 的左Kan扩张是一个函子 $\mathrm{Lan}_K F: \mathcal{B} \to \mathcal{E}$ 以及一个自然变换 $\eta: F \Rightarrow \mathrm{Lan}_K F \circ K$，使得该构造满足泛性质。Kan扩张的普遍性使其被称为"范畴论中所有概念之母"。

## 分析

**前置依赖**：函子与自然变换、逗号范畴、余极限、伴随函子。

**定理的精确表述**：设 $F: \mathcal{A} \to \mathcal{E}$ 和 $K: \mathcal{A} \to \mathcal{B}$ 是函子。$F$ 沿 $K$ 的**左Kan扩张**是一个对 $(\mathrm{Lan}_K F, \eta)$，其中 $\mathrm{Lan}_K F: \mathcal{B} \to \mathcal{E}$ 是函子，$\eta: F \Rightarrow \mathrm{Lan}_K F \circ K$ 是自然变换，且满足泛性质：对任意函子 $G: \mathcal{B} \to \mathcal{E}$ 和自然变换 $\alpha: F \Rightarrow G \circ K$，存在唯一的自然变换 $\beta: \mathrm{Lan}_K F \Rightarrow G$ 使得 $\alpha = \beta_K \circ \eta$。

**对偶地**，**右Kan扩张** $(\mathrm{Ran}_K F, \varepsilon)$ 满足 $\varepsilon: \mathrm{Ran}_K F \circ K \Rightarrow F$ 的泛性质。

**依赖的概念**：函子、自然变换、伴随函子、极限、余极限。

**证明策略**：当 $\mathcal{E}$ 余完备时，左Kan扩张可以通过余极限显式构造：$\mathrm{Lan}_K F(B) = \mathrm{colim}_{K(A) \to B} F(A)$。类似地，右Kan扩张通过极限构造。

## 思考过程

Kan扩张的核心思想是"沿函子延伸"。考虑一个简单的例子：设 $\mathcal{A}$ 是单点范畴，$K: \mathcal{A} \to \mathcal{B}$ 将唯一的对象映到 $B_0 \in \mathcal{B}$，$F: \mathcal{A} \to \mathcal{E}$ 将唯一的对象映到 $E_0 \in \mathcal{E}$。则左Kan扩张 $\mathrm{Lan}_K F$ 将对象 $B$ 映到 $\mathrm{colim}_{B_0 \to B} E_0$，这实际上给出了从 $B_0$ 到 $B$ 的态射的"余积"。

更一般地，左Kan扩张通过"沿着 $K$ 的像推前"来构造，而右Kan扩张则通过"沿着 $K$ 的像拉回"来构造。这种构造在代数拓扑中特别有用，例如在奇异同调理论中，奇异单形函子就是某种Kan扩张。

## 证明过程

**定理**（Kan扩张的存在性）：设 $\mathcal{A}$ 是小范畴，$\mathcal{B}$ 是范畴，$\mathcal{E}$ 是余完备范畴。则对任意函子 $F: \mathcal{A} \to \mathcal{E}$ 和 $K: \mathcal{A} \to \mathcal{B}$，左Kan扩张 $\mathrm{Lan}_K F$ 存在。

**证明**：

**步骤 1：定义 $\mathrm{Lan}_K F$ 在对象上的作用。**

对任意 $B \in \mathcal{B}$，考虑逗号范畴 $(K \downarrow B)$，其对象为对 $(A, f: K(A) \to B)$，态射为保持交换图的 $\mathcal{A}$ 中态射。定义函子 $\Phi_B: (K \downarrow B) \to \mathcal{E}$ 为 $\Phi_B(A, f) = F(A)$，$\Phi_B(h) = F(h)$。

由于 $\mathcal{E}$ 余完备，可定义

$$
\mathrm{Lan}_K F(B) = \mathrm{colim}_{(K \downarrow B)} F(A) = \mathrm{colim}\, \Phi_B.
$$

**步骤 2：定义 $\mathrm{Lan}_K F$ 在态射上的作用。**

对 $g: B \to B'$，$g$ 诱导了函子 $g_*: (K \downarrow B) \to (K \downarrow B')$，由 $(A, f) \mapsto (A, g \circ f)$ 给出。于是有诱导态射

$$
\mathrm{Lan}_K F(g) = \mathrm{colim}\, \Phi_B \to \mathrm{colim}\, \Phi_{B'}.
$$

这由余极限的泛性质唯一确定。

**步骤 3：定义自然变换 $\eta$。**

对每个 $A \in \mathcal{A}$，考虑 $K(A) \in \mathcal{B}$。有余极限的包含映射

$$
\iota_A: F(A) \to \mathrm{Lan}_K F(K(A)) = \mathrm{colim}_{(K \downarrow K(A))} F(A')
$$

对应于 $(A, \mathrm{id}_{K(A)})$ 这个对象。这给出了 $\eta_A: F(A) \to \mathrm{Lan}_K F \circ K(A)$。

**步骤 4：验证泛性质。**

设 $G: \mathcal{B} \to \mathcal{E}$ 和 $\alpha: F \Rightarrow G \circ K$ 是自然变换。对每个 $B \in \mathcal{B}$，我们需要构造 $\beta_B: \mathrm{Lan}_K F(B) \to G(B)$ 使得对每个 $(A, f: K(A) \to B)$，下图交换：

$$
\begin{CD}
F(A) @>{\alpha_A}>> G(K(A)) \\
@V{\iota_{(A,f)}}VV @VV{G(f)}V \\
\mathrm{Lan}_K F(B) @>{\beta_B}>> G(B)
\end{CD}
$$

由余极限的泛性质，存在唯一的 $\beta_B$ 使得整个图表交换。可以验证 $\beta$ 是自然变换且满足 $\alpha = \beta_K \circ \eta$。$\square$

**注**：对偶地，若 $\mathcal{E}$ 完备，则右Kan扩张存在，由极限构造：

$$
\mathrm{Ran}_K F(B) = \lim_{(B \downarrow K)} F(A).
$$

**推论**：左Kan扩张是左伴随的推广。具体地，$F: \mathcal{A} \to \mathcal{E}$ 沿 $K: \mathcal{A} \to \mathcal{B}$ 的左Kan扩张存在当且仅当 $\mathrm{Lan}_K(-)$ 是 $- \circ K$ 的左伴随。