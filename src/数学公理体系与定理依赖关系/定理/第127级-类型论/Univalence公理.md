# Univalence 公理

> **一句话大白话**：同构的类型在类型论里可以看成一回事——$(A\simeq B)\simeq(A=_\mathcal{U}B)$。"两个类型有结构等价"就等于"它们相等"，把同构提升为相等。
>
> **小例子**：布尔类型 $\mathbf{bool}$ 与 $\mathbf{unit}\sqcup\mathbf{unit}$ 之间天然同构。Univalence 说这种同构本身就可当作类型论里 $\mathbf{bool}=_\mathcal{U}(\mathbf{unit}\sqcup\mathbf{unit})$ 的一个证路——于是"被同构事物可以平等对待"在类型论中变成可操作的相等代换。

## 一、定理介绍

> **前置依赖**：恒等类型与J规则、等价（同伦等价）定义、HoTT路径概念、类型宇宙（$\mathcal{U}$）、一致性的单纯集模型。

Univalence 公理（Voevodsky，2009）是类型论（尤其同伦类型论 HoTT）中一项深刻而现代的公理：
$$
(A\simeq B)\simeq(A=_\mathcal{U}B),
$$
即"等价 $(A\simeq B)$"与"在宇宙 $\mathcal{U}$ 中的相等 $(A=_\mathcal{U}B)$"构成等价。它极大扩展了类型论的表达能力，使证明在结构等价下可代换，是同构经济学与数学结构观念的革新。

## 二、原理思路

构造从相等到等价的映射 $\text{IdToEquiv}:(A=_\mathcal{U}B)\to(A\simeq B)$：由 J 规则，对 $p:A=_\mathcal{U}B$ 取 $\text{IdToEquiv}(p)=J(\lambda X.\,(A\simeq X),\text{id}_A,B,p)$。Univalence 公理断言 $\text{IdToEquiv}$ 本身是等价（具双射逆函子），从而有逆 $\text{EquivToId}$。一致性由 Voevodsky 在单纯集模型中验证。

## 三、定理的严格表述

**定理（Univalence 公理，Voevodsky 2009）**：Univalence 公理与 Martin-Löf 类型论一致，且断言
$$
(A\simeq B)\simeq(A=_\mathcal{U}B)
$$
其中 $\mathcal{U}$ 是类型宇宙，$A\simeq B$ 表示 $A$ 与 $B$ 之间存在等价。

## 四、证明过程

**证明（构造 $\text{IdToEquiv}$）**：

**步骤1（定义 $\text{IdToEquiv}$）**：对 $A,B:\mathcal{U}$，定义
$$
\text{IdToEquiv}:(A=_\mathcal{U}B)\to(A\simeq B),\quad
\text{IdToEquiv}(p)=J(\lambda X.\,(A\simeq X),\,\text{id}_A,\,B,\,p).
$$

**步骤2（Univalence 公理）**：断言 $\text{IdToEquiv}$ 本身是等价，即
$$
\text{ua}:\text{IsEquiv}(\text{IdToEquiv}),
$$
从而存在逆映射 $\text{EquivToId}:(A\simeq B)\to(A=_\mathcal{U}B)$。

**步骤3（一致性）**：Voevodsky 证明 Univalence 公理在单纯集模型（Simplicial Set Model）中成立，从而与 MLTT 一致。$\square$

**推论**：Univalence 意味着"等价的类型可交换"（同构的即可等同），极大扩展了类型论的表达能力。

## 五、应用与意义

Univalence 是现代数学形式化与同伦类型论的核心理论支点：它使"结构保持同构的对象不可区分"这一朴素原则成为可代换的相等，简化了大量"重写/等价代换"证明，支撑 HoTT 中从初等对象到高阶结构的重新组织，并深刻影响范畴论、代数拓扑（路径、同伦等价）与定理助手的形式化实践。