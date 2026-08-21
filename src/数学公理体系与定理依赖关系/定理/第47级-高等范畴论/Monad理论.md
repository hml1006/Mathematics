# Monad理论

> **一句话大白话**：Monad 是"带单位律的结合运算"在范畴上的抽象：$T^2\to T$ 配上单位 $1\to T$；很多看起来很不同的代数结构（群、拓扑、布尔代数）都能照此递归成"某 monad 的代数"。
>
> **小例子**：$\mathbf{Set}$ 上的幂集 Monad $\mathcal P$ 的代数恰是被"并"运算装点好的 $\sqcup$-半格；进而 Kleisli 范畴给出"副作用/效应"的计算模型。

## 介绍

Monad（单子）是范畴论中一个核心概念，它描述了一个范畴上的"自函子"配备两种自然变换（乘法与单位）所构成的代数结构。Monad理论源于1960年代Huber、Kleisli和Eilenberg-Moore等人对"同调代数中的导出函子"的研究。一个Monad $\mathbf{T} = (T, \eta, \mu)$ 由自函子 $T: \mathcal{C} \to \mathcal{C}$、单位自然变换 $\eta: \mathrm{Id}_{\mathcal{C}} \Rightarrow T$ 和乘法自然变换 $\mu: T^2 \Rightarrow T$ 组成，满足结合律和单位律。Monad 理论提供了将代数结构（如群、环、模）统一处理的语言，也是函数式编程中处理副作用的基础。

## 分析

**前置依赖**：自函子与自然变换、伴随函子、三角恒等式、Kleisli 范畴与 Eilenberg-Moore 范畴。

**定理的精确表述**：范畴 $\mathcal{C}$ 上的一个 **Monad** 由三元组 $(T, \eta, \mu)$ 构成，其中：
- $T: \mathcal{C} \to \mathcal{C}$ 是函子，
- $\eta: \mathrm{Id}_{\mathcal{C}} \Rightarrow T$ 是自然变换（单位），
- $\mu: T \circ T \Rightarrow T$ 是自然变换（乘法），

满足以下交换图：

**结合律**：
$$
\begin{CD}
T^3 @>{T\mu}>> T^2 \\
@V{\mu T}VV @VV{\mu}V \\
T^2 @>{\mu}>> T
\end{CD}
$$

**单位律**：
$$
\begin{CD}
T @>{T\eta}>> T^2 @<{\eta T}<< T \\
@| @VV{\mu}V @| \\
T @= T @= T
\end{CD}
$$

**依赖的概念**：函子、自然变换、伴随函子、Kleisli范畴、Eilenberg-Moore范畴。

**核心结果**：
- 每个伴随对 $(F, G, \eta, \varepsilon)$ 诱导一个Monad $(G \circ F, \eta, G\varepsilon F)$。
- 反之，每个Monad可以分解为伴随对（通过Kleisli范畴或Eilenberg-Moore范畴），且这种分解在某种意义下是极端的。
- **Monad的同范畴定理**：对任意Monad $\mathbf{T}$，Eilenberg-Moore范畴 $\mathcal{C}^{\mathbf{T}}$ 是使得 $\mathcal{C} \to \mathcal{D}$ 分解通过 $U^{\mathbf{T}}: \mathcal{C}^{\mathbf{T}} \to \mathcal{C}$ 的泛解。

## 思考过程

Monad理论的核心洞察是：许多代数结构都可以通过一个自函子上的"代数运算"来刻画。例如，群可以用集合上的自由群Monad来刻画；环可以用自由环Monad来刻画；甚至幂集Monad可以刻画完全格。

Monad与伴随函子之间的深刻联系体现在：
1. 从伴随函子出发，复合 $G \circ F$ 自然形成一个Monad。
2. 反过来，给定Monad，可以构造其Kleisli范畴（最自由的分解）和Eilenberg-Moore范畴（最严格的分解），两者都给出原始Monad的伴随分解。

这种"伴随-单子对应"是范畴论中最优美的结果之一。

## 证明过程

**定理**（伴随诱导Monad）：设 $F: \mathcal{C} \to \mathcal{D}$ 和 $G: \mathcal{D} \to \mathcal{C}$ 是伴随对 $F \dashv G$，伴随元为 $\eta: \mathrm{Id}_{\mathcal{C}} \Rightarrow G \circ F$ 和 $\varepsilon: F \circ G \Rightarrow \mathrm{Id}_{\mathcal{D}}$。则 $(T = G \circ F, \eta, \mu = G\varepsilon F)$ 构成 $\mathcal{C}$ 上的一个Monad。

**证明**：

**步骤 1：验证 $\mu$ 是自然变换。**

$\mu = G\varepsilon F: G \circ F \circ G \circ F \Rightarrow G \circ F$。由于 $\varepsilon$ 是自然变换，$G\varepsilon F$ 也是自然变换（函子复合保持自然性）。

**步骤 2：验证结合律。**

需要证明 $\mu \circ T\mu = \mu \circ \mu T$。在对象层面，对任意 $X \in \mathcal{C}$，

$$
\begin{CD}
GFGFGF(X) @>{GFG\varepsilon F(X)}>> GFGF(X) \\
@V{G\varepsilon FGF(X)}VV @VV{G\varepsilon F(X)}V \\
GFGF(X) @>{G\varepsilon F(X)}>> GF(X)
\end{CD}
$$

由 $\varepsilon$ 的自然性，对 $\varepsilon_{F(X)}: FGF(X) \to F(X)$，有交换图：

$$
\begin{CD}
FGFGF(X) @>{FGF(\varepsilon_X)}>> FGF(X) \\
@V{\varepsilon_{FGF(X)}}VV @VV{\varepsilon_{F(X)}}V \\
FGF(X) @>{F(\varepsilon_X)}>> F(X)
\end{CD}
$$

应用 $G$ 即得结合律成立。

**步骤 3：验证单位律。**

需要证明 $\mu \circ T\eta = \mathrm{id}_T$ 和 $\mu \circ \eta T = \mathrm{id}_T$。

对任意 $X$，$T\eta_X = G(\varepsilon_{F(X)}) \circ G(F(\eta_X))$。由三角恒等式 $\varepsilon F \circ F\eta = \mathrm{id}_F$，有

$$
\mu_X \circ T\eta_X = G(\varepsilon_{F(X)}) \circ G(F(G(\varepsilon_{F(X)}))) \circ G(F(\eta_X)) = G(\varepsilon_{F(X)}) \circ G(\varepsilon_{FGF(X)}) \circ GFG(\eta_X) = \mathrm{id}_{GF(X)}.
$$

类似地可验证另一条单位律。$\square$

**定理**（Eilenberg-Moore构造）：每个Monad $\mathbf{T} = (T, \eta, \mu)$ 在 $\mathcal{C}$ 上诱导一个伴随对 $F^{\mathbf{T}} \dashv U^{\mathbf{T}}$，其中 $U^{\mathbf{T}}: \mathcal{C}^{\mathbf{T}} \to \mathcal{C}$ 是遗忘函子，$F^{\mathbf{T}}: \mathcal{C} \to \mathcal{C}^{\mathbf{T}}$ 是自由函子。

**证明概要**：
- $\mathcal{C}^{\mathbf{T}}$ 的对象是 $\mathbf{T}$-代数 $(A, a: T(A) \to A)$，满足 $a \circ \eta_A = \mathrm{id}_A$ 和 $a \circ T(a) = a \circ \mu_A$。
- $U^{\mathbf{T}}(A, a) = A$，$F^{\mathbf{T}}(A) = (T(A), \mu_A)$。
- 伴随由 $\eta$ 和余单位 $\varepsilon_{(A,a)} = a: T(A) \to A$ 给出。
- 该Monad恰好是 $U^{\mathbf{T}} \circ F^{\mathbf{T}}$。$\square$

**推论**（Kleisli构造）：存在另一个极端的分解，Kleisli范畴 $\mathcal{C}_{\mathbf{T}}$ 以 $\mathcal{C}$ 的对象为对象，从 $A$ 到 $B$ 的态射是 $\mathcal{C}$ 中的态射 $A \to T(B)$。