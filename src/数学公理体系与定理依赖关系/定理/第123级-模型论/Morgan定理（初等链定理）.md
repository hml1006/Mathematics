# Morgan 定理（初等链定理）

> **一句话大白话**：如果你有一串逐个"初等包含"的结构 $\mathfrak{A}_0\preccurlyeq\mathfrak{A}_1\preccurlyeq\cdots$，那么它们的并集（取极限）仍然是每个结构与这个并集的初等扩张——链条的每一项都保持初等关系地嵌进并集。
>
> **小例子**：逐层膨胀的模型阶梯 $\mathfrak{A}_\alpha$，每一层都是下一层的初等子结构。定理保证：把整条链并起来得到的 $\mathfrak{A}$，对每一层 $\mathfrak{A}_\alpha$ 依然有 $\mathfrak{A}_\alpha\preccurlyeq\mathfrak{A}$——拼接无限链条不会破坏初等性。

## 一、定理介绍

> **前置依赖**：初等子结构与初等扩张、Tarski-Vaught判别法、超穷归纳、模型理论基本概念、并（极限）结构。

Morgan 定理（初等链定理，Elementary Chain Theorem）是模型论中构造初等扩张与"取极限结构"的基本工具。当一族结构组成初等链（沿序数指标逐层初等包含）时，定理保证链并仍是每个成员的初等扩张。它是超穷构造初等扩张、构造饱和模型和代数中模型完备性论证的中坚。

## 二、原理思路

证明本质是对公式复杂度进行归纳。关键是"向上方向"的 $\exists$ 情形：若 $\mathfrak{A}=\bigcup_\alpha\mathfrak{A}_\alpha $ 中某个 $\exists x\psi(x,\bar b)$ 为真（$\bar b\in A_\alpha$），则见证 $b$ 落在某 $\mathfrak{A}_\beta$（$\beta\ge\alpha$）中；利用 $\mathfrak{A}_\beta\preccurlyeq\mathfrak{A}$ 与 $\mathfrak{A}_\alpha\preccurlyeq\mathfrak{A}_\beta$ 逐步"拉回"见证到 $\mathfrak{A}_\alpha$。实践中常用等价的 **Tarski-Vaught 判别法** 使论证更清晰，并对序数指标做超穷归纳。

## 三、定理的严格表述

**定理（它有不同于普通包含的初等链）**：设 $\{\mathfrak{A}_\alpha\}_{\alpha<\delta}$ 是初等链（对 $\alpha<\beta<\delta$ 有 $\mathfrak{A}_\alpha\preccurlyeq\mathfrak{A}_\beta$），$\mathfrak{A}=\bigcup_{\alpha<\delta}\mathfrak{A}_\alpha$。则对任意 $\alpha<\delta$，$\mathfrak{A}_\alpha\preccurlyeq\mathfrak{A}$。

**Tarski-Vaught 判别法**：$\mathfrak{B}\subseteq\mathfrak{A}$ 是初等子结构当且仅当对任意 $\mathcal{L}$-公式 $\varphi(x,\bar y)$ 与 $\bar b\in B$，若 $\mathfrak{A}\models\exists x\varphi(x,\bar b)$，则存在 $c\in B$ 使 $\mathfrak{A}\models\varphi(c,\bar b)$。

## 四、证明过程

**证明（用 Tarski-Vaught 判别法）**：

固定 $\alpha$，对 $\mathfrak{A}_\alpha\subseteq\mathfrak{A}$ 加深应用判别法。设 $\varphi(x,\bar y)$ 为 $\mathcal{L}$-公式，$\bar b\in A_\alpha$，且 $\mathfrak{A}\models\exists x\varphi(x,\bar b)$。则存在某 $\beta$ 与 $c\in A_\beta$ 使 $\mathfrak{A}\models\varphi(c,\bar b)$。取 $\beta\ge\alpha$：由归纳构造知 $\mathfrak{A}_\beta\preccurlyeq\mathfrak{A}$（对 $\overline A_\beta$ 中元素成立），故 $\mathfrak{A}_\beta\models\exists x\varphi(x,\bar b)$。

又 $\mathfrak{A}_\alpha\preccurlyeq\mathfrak{A}_\beta$，故 $\mathfrak{A}_\alpha\models\exists x\varphi(x,\bar b)$，即存在 $c'\in A_\alpha$ 使 $\mathfrak{A}_\alpha\models\varphi(c',\bar b)$。再由 $\mathfrak{A}_\alpha\preccurlyeq\mathfrak{A}$ 对 $\overline A_\alpha$ 元素成立，得 $\mathfrak{A}\models\varphi(c',\bar b)$。

于是 Tarski-Vaught 条件满足，$\mathfrak{A}_\alpha\preccurlyeq\mathfrak{A}$。$\square$

## 五、应用与意义

初等链定理是模型论构造性工具的基石：用于构建初等成员的并、构造满足可控性质的链、证明模型完备性（$\mathfrak{A}\subseteq\mathfrak{B}$ 时用链逼近）、构造可数饱和模型以及稳定理论中的各类构造。它把"无穷晋升"与"初等包含"无缝衔接，使得模型论能处理超穷步长的构造。