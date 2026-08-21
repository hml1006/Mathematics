# Gödel 第一不完全性定理

> **一句话大白话**：任何足够强（能表达算术）且一致的形式系统，总有一条语句 $G$ 既不能被证明也不能被证伪——$G$ 自己说"我不可证"，两条路都走不通，于是系统不完备。
>
> **小例子**：造一句自指句 $G$："$G$ 不可证明"。若系统能证 $G$，则 $G$ 说错、系统不一致；若系统能证 $\lnot G$，则 $G$ 其实是对的（确实不可证）、系统证错。故 $G$ 在系统中既不可证也不可否证。

## 一、定理介绍

> **前置依赖**：对角化（自指）引理、Gödel编码与算术化、可证性谓词与算术可表示性、原始递归函数、ω一致性。

Gödel 第一不完全性定理是 20 世纪数学基础最深刻的成果之一：任何包含 Peano 算术的一致可公理化形式系统 $\mathcal{F}$ 都是不完全的——存在算术语句 $G$ 使 $\mathcal{F}\nvdash G$ 且 $\mathcal{F}\nvdash\lnot G$。它终结了 Hilbert 关于"全部数学真理可公理化"的乐观期望。

## 二、原理思路

证明核心是**对角化引理**：对任何含自由变元 $x$ 的公式 $\phi(x)$，存在语句 $\psi$ 使 $\mathcal{F}\vdash\psi\leftrightarrow\phi(\ulcorner\psi\urcorner)$。利用算术的自指能力构造 $G$，使 $G\leftrightarrow\lnot\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)$（"$G$ 不可证"）。再分别反设 $\mathcal{F}\vdash G$ 与 $\mathcal{F}\vdash\lnot G$，导出矛盾（后者需 $\omega$ 一致性，Rosser 后来改进为仅需一致性）。

## 三、定理的严格表述

**定理（Gödel 第一不完全性定理）**：任何包含 Peano 算术的一致可公理化形式系统 $\mathcal{F}$ 都是不完全的，即存在算术语句 $G$ 使 $\mathcal{F}\nvdash G$ 且 $\mathcal{F}\nvdash\lnot G$。

**引理（对角化引理）**：对任何只含一个自由变元 $x$ 的公式 $\phi(x)$，存在语句 $\psi$ 使 $\mathcal{F}\vdash\psi\leftrightarrow\phi(\ulcorner\psi\urcorner)$。

## 四、证明过程

**对角化引理的证明**：设 $\text{sub}(m,n)$ 为"$m$ 是 $\chi(x)$ 的 Gödel 数时 $\text{sub}(m,n)$ 是 $\chi(\bar n)$ 的 Gödel 数"的原始递归函数。定义 $\theta(x)=\exists y(\text{sub}(x,x)=y\land\phi(y))$，令 $p=\ulcorner\theta(x)\urcorner$，则 $\psi=\theta(\bar p)$。于是 $\ulcorner\psi\urcorner=\text{sub}(p,p)$，从而
$$
\mathcal{F}\vdash\psi\leftrightarrow\exists y(\text{sub}(\bar p,\bar p)=y\land\phi(y))\leftrightarrow\phi(\text{sub}(\bar p,\bar p))\leftrightarrow\phi(\ulcorner\psi\urcorner).
$$
引理证毕。

**定理证明**：

**步骤1**：令 $\text{Prov}_\mathcal{F}(x)=\exists y\text{Proof}_\mathcal{F}(x,y)$（可证谓词）。由对角化引理取 $\phi(x)=\lnot\text{Prov}_\mathcal{F}(x)$，得 Gödel 语句 $G$：
$$
\mathcal{F}\vdash G\leftrightarrow\lnot\text{Prov}_\mathcal{F}(\ulcorner G\urcorner).
$$

**步骤2（$G$ 不可证）**：反设 $\mathcal{F}\vdash G$，则 $\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)$ 真，由算术可表示性 $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)$；由 $G$ 定义得 $\mathcal{F}\vdash\lnot G$，与一致性矛盾。故 $\mathcal{F}\nvdash G$。

**步骤3（$\lnot G$ 不可证）**：反设 $\mathcal{F}\vdash\lnot G$，则由 $G$ 定义 $\mathcal{F}\vdash\text{Prov}_\mathcal{F}(\ulcorner G\urcorner)$，即 $\mathcal{F}\vdash\exists y\text{Proof}_\mathcal{F}(\ulcorner G\urcorner,y)$。若 $\mathcal{F}$ 是 $\omega$ 一致的，则存在实际 $n$ 使 $\text{Proof}_\mathcal{F}(\ulcorner G\urcorner,\bar n)$ 真，即 $G$ 实际可证，与步骤2矛盾。故 $\mathcal{F}\nvdash\lnot G$。

综上 $G$ 不可判定，$\mathcal{F}$ 不完备。$\square$

## 五、应用与意义

Gödel 第一不完全性定理深刻揭示了形式系统的能力边界：一致而足够强的一阶系统必然不完备。它影响数理逻辑（证明论、递归论）、数学哲学（形式主义与直觉主义之争）乃至人工智能论（"可计算证明的局限"）。与第二不完全性定理共同构成对"自足公理化数学"的根本性否定。