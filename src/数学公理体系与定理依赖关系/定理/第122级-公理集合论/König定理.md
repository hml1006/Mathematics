# König 定理

> **一句话大白话**：如果对每个 $i$ 都有 $\kappa_i<\lambda_i$，那么这些 $\kappa_i$ 的和严格小于这些 $\lambda_i$ 的积——"每一项都小，加起来仍然小于各项都大的乘积"。它把 Cantor 定理 $\kappa<2^\kappa$ 推广到更一般的基数和/积情形。
>
> **小例子**：对可数个 $\kappa_i=\aleph_0$ 与 $\lambda_i=2^{\aleph_0}$，定理给出 $\aleph_0\cdot\aleph_0=\aleph_0<\prod_{i}2^{\aleph_0}$，从而蕴含连续统的共尾性不可数：$\operatorname{cf}(2^{\aleph_0})>\aleph_0$。

## 一、定理介绍

> **前置依赖**：Cantor定理（$\kappa<2^\kappa$）、基数算术（和与积）、对角线论证、共尾性（$\operatorname{cf}$）概念、选择公理。

König 定理是基数算术中一个深刻且重要的严格不等式。经典 Cantor 定理表明 $\kappa<2^\kappa$；König 定理将之加强并推广为：一族基数，只要每个 $\kappa_i$ 严格小于相应的 $\lambda_i$，则其和严格小于其积。它是推导若干基数不等式的关键引擎。

## 二、原理思路

直观上，$\sum\kappa_i$ 的每个要素只能放进 $\prod\lambda_i$ 的一个"维度"，而 $\prod\lambda_i$ 有那么多可选取值，选择空间巨大。"等式不成立"的证明用对角线思想：假设双射 $h$ 存在，让每个 $S_i=\{h(\alpha,i)(i):\alpha<\kappa_i\}$ 因 $\kappa_i<\lambda_i$ 而无法覆盖 $\lambda_i$，从而挑出一个偏离所有 $S_i$ 的"对角线函数" $g$，与 $h$ 的满射性矛盾。

## 三、定理的严格表述

**定理（König）**：若对每个 $i\in I$ 有 $\kappa_i<\lambda_i$，则
$$
\sum_{i\in I}\kappa_i < \prod_{i\in I}\lambda_i.
$$

**推论**：$\kappa<2^\kappa$（Cantor 定理），且 $\operatorname{cf}(2^{\aleph_0})>\aleph_0$。

## 四、证明过程

**证明**：

**第一步：证明 $\sum\kappa_i\le\prod\lambda_i$**。对每个 $i$，因 $\kappa_i<\lambda_i$ 存在单射 $f_i:\kappa_i\to\lambda_i$。定义 $F:\bigcup_{i\in I}(\kappa_i\times\{i\})\to\prod_{i\in I}\lambda_i$：对 $(x,i)\in\kappa_i\times\{i\}$，$F(x,i)$ 为仅在坐标 $i$ 取值 $f_i(x)$、其余坐标取 $0$ 的函数。$F$ 是单射，故 $\sum\kappa_i\le\prod\lambda_i$。

**第二步：证明不可能是相等**。反设存在双射 $h:\bigcup_{i\in I}(\kappa_i\times\{i\})\to\prod_{i\in I}\lambda_i$。对每个 $i$，令：
$$
S_i=\{h(\alpha,i)(i)\mid \alpha<\kappa_i\}\subseteq\lambda_i.
$$
因 $\kappa_i<\lambda_i$ 且 $|S_i|\le\kappa_i$，故 $S_i\subsetneq\lambda_i$，可取 $\beta_i\in\lambda_i\setminus S_i$。定义 $g\in\prod_{i\in I}\lambda_i$ 为 $g(i)=\beta_i$。由于 $h$ 是满射，存在 $(\alpha,i)$ 使 $h(\alpha,i)=g$。则 $g(i)=h(\alpha,i)(i)\in S_i$，但由构造 $g(i)=\beta_i\notin S_i$，矛盾。

故 $\sum\kappa_i<\prod\lambda_i$。$\square$

## 五、应用与意义

König 定理在基数理论中用途广泛：推出 Cantor 定理、证明 $\kappa<\kappa^{\operatorname{cf}(\kappa)}$、证明连续统的共尾性不可数、以及一系列有关 $\aleph_\omega$ 等奇异基数的性质。它是继 Cantor 定理之后基数"严格增长"的最有力工具，也是选择公理下基数算术的支柱之一。