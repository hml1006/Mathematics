# Gödel 第二不完全性定理

> **一句话大白话**：任何一致且足够强的形式系统，连自己"自身的无矛盾性"这句话都证明不了——$\mathcal{F}$ 不能证明 $\text{Con}_\mathcal{F}$。换言之，"我永远不可能自己证明我自己是清白的"。
>
> **小例子**：令 $\text{Con}_\mathcal{F}=\lnot\text{Prov}_\mathcal{F}(\ulcorner\bot\urcorner)$（"矛盾不可证"）。若 $\mathcal{F}$ 能证自身一致，则能证 $\text{Con}_\mathcal{F}$；但可证性条件与第一不完全性合起来推出 $\text{Con}_\mathcal{F}\leftrightarrow G$（$G$ 不可证），矛盾。故 $\mathcal{F}\nvdash\text{Con}_\mathcal{F}$。

## 一、定理介绍

> **前置依赖**：Gödel第一不完全性定理、Hilbert-Bernays可证性条件、对角化引理、可证性谓词、PA的表达能力。

Gödel 第二不完全性定理是首不完备定理的深化：不仅存在不可判定的算术语句，系统中"自身一致性" $\text{Con}_\mathcal{F}$ 也恰恰不可证明。它是 Hilbert 纲领（在系统内证明系统一致）的终极致命伤，标定了"自箱自证的一致性"不可能。

## 二、原理思路

证明依赖 Hilbert-Bernays **可证性条件**：证明谓词 $\text{Prov}_\mathcal{F}$ 满足三条内化规则（前面内化、可证性封闭、可证性的可证性）。在系统内形式化第一不完全性证明，推出 $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\to\lnot\text{Con}_\mathcal{F}$，从而 $\text{Con}_\mathcal{F}\to\lnot\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\leftrightarrow G$。若 $\mathcal{F}\vdash\text{Con}_\mathcal{F}$ 则 $\mathcal{F}\vdash G$，与第一定理矛盾。

## 三、定理的严格表述

**定理（Gödel 第二不完全性定理）**：任何包含 Peano 算术的一致形式系统 $\mathcal{F}$ 不能证明自身的一致性，即 $\mathcal{F}\nvdash\text{Con}_\mathcal{F}$，其中 $\text{Con}_\mathcal{F}=\lnot\text{Prov}_\mathcal{F}(\ulcorner\bot\urcorner)$。

**可证性条件（Hilbert-Bernays）**：
1. 若 $\mathcal{F}\vdash A$，则 $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner A\urcorner)$；
2. $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner A\to B\urcorner)\to(\text{Prov}_\mathcal{F}(\ulcorner A\urcorner)\to\text{Prov}_\mathcal{F}(\ulcorner B\urcorner))$；
3. $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner A\urcorner)\to\text{Prov}_\mathcal{F}(\ulcorner\text{Prov}_\mathcal{F}(\ulcorner A\urcorner)\urcorner)$。

## 四、证明过程

**证明**：令 $G$ 满足 $\mathcal{F}\vdash G\leftrightarrow\lnot\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)$。

**步骤1（形式化）**：在 $\mathcal{F}$ 中形式化第一定理的论证：
- 由条件3，$\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\to\text{Prov}_\mathcal{F}(\ulcorner\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\urcorner)$。
- 由 $G$ 定义等价形式 $G\to(\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\to\bot)$，用条件2 得 $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\to\text{Prov}_\mathcal{F}(\ulcorner\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\to\bot\urcorner)$。
- 用条件2 结合上两者得 $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\to\text{Prov}_\mathcal{F}(\ulcorner\bot\urcorner)$，即 $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\to\lnot\text{Con}_\mathcal{F}$。
- 取逆否，得 $\mathcal{F}\vdash\text{Con}_\mathcal{F}\to\lnot\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)$；由 $G$ 定义 $\lnot\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)\leftrightarrow G$，故
$$
\mathcal{F}\vdash\text{Con}_\mathcal{F}\to G.
$$

**步骤2（导出矛盾）**：若 $\mathcal{F}\vdash\text{Con}_\mathcal{F}$，则 $\mathcal{F}\vdash G$，但由第一不完全性定理（$\mathcal{F}$ 一致故 $G$ 不可证）矛盾。

因此 $\mathcal{F}\nvdash\text{Con}_\mathcal{F}$。$\square$

## 五、应用与意义

Gödel 第二不完全性定理直接终结了 Hilbert 纲领中"系统内证明系统一致"的构想，是数学基础与哲学的分水岭。它使 Gentzen 用超穷序数（$\varepsilon_0$）在系统外证明 PA 一致的方案成为必要，也在逻辑、人工智能与哲学上引发关于数学知识的本质、证明资源与"真与可证分离"的持久讨论。