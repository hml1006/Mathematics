# Yoneda引理

## 介绍

Yoneda引理（Yoneda Lemma）是范畴论中最基本的定理之一，由日本数学家米田信夫（Nobuo Yoneda）提出。该引理断言：对任意局部小范畴 $\mathcal{C}$ 中的对象 $A$ 和任意函子 $F: \mathcal{C} \to \mathbf{Set}$，从 $A$ 出发的 Hom 函子 $\mathrm{Hom}_{\mathcal{C}}(A, -)$ 到 $F$ 的自然变换全体与集合 $F(A)$ 之间存在一一对应。Yoneda引理揭示了范畴中的对象完全由其与其它对象的关系决定，这一深刻的洞察贯穿了整个现代数学。

## 分析

**定理的精确表述**：设 $\mathcal{C}$ 是局部小范畴，$A$ 是 $\mathcal{C}$ 的对象，$F: \mathcal{C} \to \mathbf{Set}$ 是任意函子。则存在双射

$$
\mathrm{Nat}(\mathrm{Hom}_{\mathcal{C}}(A, -), F) \cong F(A),
$$

其中 $\mathrm{Nat}(-, -)$ 表示自然变换的集合。该双射由以下映射给出：

$$
\Phi: \mathrm{Nat}(\mathrm{Hom}_{\mathcal{C}}(A, -), F) \to F(A), \quad \Phi(\eta) = \eta_A(\mathrm{id}_A).
$$

**依赖的概念**：范畴、函子、自然变换、Hom 函子、局部小范畴。

**证明策略**：构造 $\Phi$ 及其逆映射 $\Psi$ 并验证它们是互逆的。逆映射 $\Psi: F(A) \to \mathrm{Nat}(\mathrm{Hom}_{\mathcal{C}}(A, -), F)$ 定义为：对每个 $x \in F(A)$，定义自然变换 $\Psi(x): \mathrm{Hom}_{\mathcal{C}}(A, -) \Rightarrow F$，其在对象 $B$ 处的分量 $\Psi(x)_B: \mathrm{Hom}_{\mathcal{C}}(A, B) \to F(B)$ 由 $f \mapsto F(f)(x)$ 给出。

## 思考过程

Yoneda引理的证明之所以简洁而深刻，其核心在于考虑恒等映射 $\mathrm{id}_A$ 的特殊地位。对任意自然变换 $\eta: \mathrm{Hom}_{\mathcal{C}}(A, -) \Rightarrow F$，$\eta_A(\mathrm{id}_A)$ 是 $F(A)$ 中的一个元素，这给出了从自然变换到 $F(A)$ 的映射。

反过来，给定 $x \in F(A)$，如何构造一个自然变换？对于任意 $f: A \to B$，我们需要 $\mathrm{Hom}_{\mathcal{C}}(A, B)$ 中的元素 $f$ 映射到 $F(B)$ 中的某个元素。自然性条件要求 $F(f)(\eta_A(\mathrm{id}_A)) = \eta_B(f)$，这迫使我们定义 $\eta_B(f) = F(f)(x)$。这个构造是自然的，因为它完全由函子 $F$ 的作用决定。

关键洞察是：**自然变换完全由它在恒等映射上的值决定**。这体现了范畴论中"关系决定对象"的核心思想——对象 $A$ 通过其与所有其他对象的关系（即 $\mathrm{Hom}_{\mathcal{C}}(A, -)$）来刻画，而自然变换则忠实地传递了这些关系。

## 证明过程

**定理**（Yoneda引理）：设 $\mathcal{C}$ 是局部小范畴，$A \in \mathrm{Ob}(\mathcal{C})$，$F: \mathcal{C} \to \mathbf{Set}$ 是函子。则

$$
\mathrm{Nat}(\mathrm{Hom}_{\mathcal{C}}(A, -), F) \cong F(A).
$$

**证明**：

**步骤 1：定义映射 $\Phi$。**

定义 $\Phi: \mathrm{Nat}(\mathrm{Hom}_{\mathcal{C}}(A, -), F) \to F(A)$ 为

$$
\Phi(\eta) = \eta_A(\mathrm{id}_A).
$$

**步骤 2：定义映射 $\Psi$。**

定义 $\Psi: F(A) \to \mathrm{Nat}(\mathrm{Hom}_{\mathcal{C}}(A, -), F)$ 为：对每个 $x \in F(A)$，对任意对象 $B \in \mathcal{C}$，定义 $\Psi(x)_B: \mathrm{Hom}_{\mathcal{C}}(A, B) \to F(B)$ 为

$$
\Psi(x)_B(f) = F(f)(x).
$$

**步骤 3：验证 $\Psi(x)$ 是自然变换。**

对任意态射 $g: B \to C$，需要验证自然性方块交换：

$$
\begin{CD}
\mathrm{Hom}_{\mathcal{C}}(A, B) @>{\Psi(x)_B}>> F(B) \\
@V{\mathrm{Hom}_{\mathcal{C}}(A, g)}VV @VV{F(g)}V \\
\mathrm{Hom}_{\mathcal{C}}(A, C) @>{\Psi(x)_C}>> F(C)
\end{CD}
$$

对任意 $f: A \to B$，有

$$
\Psi(x)_C \circ \mathrm{Hom}_{\mathcal{C}}(A, g)(f) = \Psi(x)_C(g \circ f) = F(g \circ f)(x) = F(g) \circ F(f)(x) = F(g) \circ \Psi(x)_B(f).
$$

故自然性成立。

**步骤 4：验证 $\Phi \circ \Psi = \mathrm{id}_{F(A)}$。**

对任意 $x \in F(A)$，

$$
\Phi(\Psi(x)) = \Psi(x)_A(\mathrm{id}_A) = F(\mathrm{id}_A)(x) = \mathrm{id}_{F(A)}(x) = x.
$$

**步骤 5：验证 $\Psi \circ \Phi = \mathrm{id}_{\mathrm{Nat}(H, F)}$。**

对任意 $\eta \in \mathrm{Nat}(\mathrm{Hom}_{\mathcal{C}}(A, -), F)$，设 $x = \eta_A(\mathrm{id}_A)$。对任意 $B$ 和任意 $f: A \to B$，由自然性，下图交换：

$$
\begin{CD}
\mathrm{Hom}_{\mathcal{C}}(A, A) @>{\eta_A}>> F(A) \\
@V{\mathrm{Hom}_{\mathcal{C}}(A, f)}VV @VV{F(f)}V \\
\mathrm{Hom}_{\mathcal{C}}(A, B) @>{\eta_B}>> F(B)
\end{CD}
$$

于是

$$
\Psi(x)_B(f) = F(f)(x) = F(f)(\eta_A(\mathrm{id}_A)) = \eta_B \circ \mathrm{Hom}_{\mathcal{C}}(A, f)(\mathrm{id}_A) = \eta_B(f).
$$

故 $\Psi(x) = \eta$，即 $\Psi \circ \Phi = \mathrm{id}$。$\square$

**推论**（Yoneda嵌入）：$\mathrm{Hom}_{\mathcal{C}}(A, -) \cong \mathrm{Hom}_{\mathcal{C}}(B, -)$ 当且仅当 $A \cong B$。即，Hom 函子完全决定了对象。