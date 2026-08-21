# Yoneda 引理

> **一句话大白话**：要研究函子 $F$ 在对象 $A$ 上的值 $F(A)$，只需看所有"从代表对象 $A$ 出发"的自然变换——两者一一对应：$\text{对象} A$ 上函子 $F$ 的"全部数据"都藏在自然变换 $\text{Hom}(A,-)\Rightarrow F$ 里。
>
> **小例子**：设 $A$ 是群论中的某个群、$F$ 是"取元素集"的函子。Yoneda 引理说"所有从 $\text{Hom}(A,-)$ 到 $F$ 的自然变换"恰好同构于 $F(A)$——用 $A$ 的观点看 $F$ 就掌握了大局。

## 一、定理介绍

> **前置依赖**：自然变换、Hom函子、函子与范畴公理、函子范畴、双射与自然性验证。

Yoneda 引理是范畴论最重要的基础定理之一。它断言：对共变函子 $F:\mathcal{C}\to\textbf{Set}$ 与对象 $A\in\mathcal{C}$，存在自然双射
$$
\text{Nat}(\text{Hom}_\mathcal{C}(A,-),F)\cong F(A).
$$
它使每个对象 $A$ 都完全由其"映射出一个 Hom函子"刻画，奠定米田嵌入、表示理论、伴随性与可表函子的一切根基。

## 二、原理思路

证明构造两个互逆映射。前向 $\Phi$ 把自然变换 $\eta$ 送到 $\eta_A(\text{id}_A)\in F(A)$（"在恒等单元处求值"）。反向 $\Psi$ 把 $x\in F(A)$ 送到自然变换 $\Psi(x)_B(f)=F(f)(x)$（用 $F$ 沿态射搬移 $x$）。验证 $\Psi(x)$ 的自然性靠函子 $F$ 的复合性，验证互逆性靠自然变换的交换图。

## 三、定理的严格表述

**定理（Yoneda 引理）**：令 $\mathcal{C}$ 是范畴，$F:\mathcal{C}\to\textbf{Set}$ 是共变函子。对任意 $A\in\mathcal{C}$，映射
$$
\Phi:\text{Nat}(\text{Hom}_\mathcal{C}(A,-),F)\to F(A),\quad \eta\mapsto\eta_A(\text{id}_A)
$$
是双射，且在 $A$ 与 $F$ 中自然。

## 四、证明过程

**证明**：

**步骤1（构造 $\Phi$）**：$id_A\in\text{Hom}_\mathcal{C}(A,A)$，故 $\eta_A(\text{id}_A)\in F(A)$。

**步骤2（构造 $\Psi:F(A)\to\text{Nat}(\text{Hom}(A,-),F)$）**：对 $x\in F(A)$，定义 $\Psi(x)_B(f)=F(f)(x)$（$f:A\to B$）。验证自然性：对 $g:B\to C$，左边 $F(g)\circ\Psi(x)_B(f)=F(g\circ f)(x)$，右边 $\Psi(x)_C(g\circ f)=F(g\circ f)(x)$，相等，故 $\Psi(x)$ 是自然变换。

**步骤3（互逆）**：对 $\eta$、$f:A\to B$，由自然性图
$$
\eta_B(f)=\eta_B\circ\text{Hom}(A,f)(\text{id}_A)=F(f)\circ\eta_A(\text{id}_A)=F(f)(\Phi(\eta))=\Psi(\Phi(\eta))_B(f),
$$
故 $\Psi(\Phi(\eta))=\eta$。对 $x$，$\Phi(\Psi(x))=\Psi(x)_A(\text{id}_A)=F(\text{id}_A)(x)=x$。故互逆，双射成立。

**步骤4（自然性，米田嵌入）**：双射对 $A,F$ 的自然性可直接验证。特别地，$Y(A)=\text{Hom}_\mathcal{C}(-,A)$ 给出满忠实嵌入 $Y:\mathcal{C}\to\textbf{Set}^{\mathcal{C}^{\text{op}}}$。$\square$

## 五、应用与意义

Yoneda 引理是"范畴论第一原理"：它证明对象可由 Hom 函子完全刻划（米田嵌入），从而抽象结构可由"与其他对象的态射关系"还原。它支撑表示理论、随伴性的各种构造、极限表示定理，并渗透到代数几何、拓扑学、理论计算机科学（Cayley 表示、Yoneda 视角的功能程序）之中。
## 相关条目

- [Yoneda 引理（第47级-高等范畴论）](../第47级-高等范畴论/Yoneda引理.md)：与本条目为同一定理，另收录于第47级-高等范畴论，可交叉参考。
