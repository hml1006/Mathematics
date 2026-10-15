# Gelfand-Mazur 定理

> **一句话大白话**：在一个每个非零元都可逆的复 Banach 代数（复 Banach 可除代数）里，除了单位元的倍数之外再没有任何别的元素——这样的代数只能就是复数域 $\mathbb C$。
>
> **小例子**：$\mathbb C$ 本身显然满足条件。反之，若试图在 $\mathbb C$ 上再"扩张"出一个含单位元的 Banach 可除代数，$a\in A$ 的谱 $\sigma(a)$ 非空会逼出某个 $a-\lambda I=0$，即 $a=\lambda I$，扩张失败。

## 一、定理介绍

> **前置依赖**：含单位元的复 Banach 代数、可逆元与谱 $\sigma(a)$、谱的非空性（Liouville 定理与预解算子的无穷远衰减）、Neumann 级数、算子范数与 $\|I\|=1$、极大理想与商代数

Gelfand–Mazur 定理（由 Israel Gelfand 与 Stanisław Mazur 于 1938 年证明）是 Banach 代数理论的第一批基本定理之一。它断言：**含单位元的复 Banach 代数若是一个可除代数（每个非零元可逆），则它同构且等距同构于 $\mathbb C$**。换言之，在复 Banach 代数这一层次上，除法结构无法再被"扩张"。

这一定理形式上简单，却是 Gelfand 谱理论的枢纽：对交换含单位 Banach 代数 $A$ 的任一极大理想 $M$，商代数 $A/M$ 是含单位 Banach 可除代数，由 Gelfand–Mazur 定理 $A/M\cong\mathbb C$，于是得到**特征标** $\varphi:A\to\mathbb C$，进而得到 Gelfand 变换与极大理想空间 $\mathfrak M_A$。由此，交换 Banach 代数被实现为极大理想空间上的连续函数代数，这是算子代数、调和分析与泛函演算的基本框架。

值得注意的是，定理中"复数域"不可替换为实数域：Frobenius 定理表明，$\mathbb R$ 上的有限维可除代数恰有 $\mathbb R,\mathbb C,\mathbb H$（四元数），它们是 $\mathbb R$ 上的 Banach 代数且可除，但都不等距同构于 $\mathbb C$。这里 $\mathbb H$ 甚至不交换，说明复结构是关键。

## 二、原理思路

证明只有两步，但第一步（谱非空）是核心。

1. **谱非空**：对任意 $a\in A$，若 $\sigma(a)=\emptyset$，则预解算子 $R(\lambda)=(\lambda I-a)^{-1}$ 在整个 $\mathbb C$ 上解析（整函数）。当 $|\lambda|>\|a\|$ 时 $\|R(\lambda)\|\le(|\lambda|-\|a\|)^{-1}\to0$，故 $R$ 有界。由 Liouville 定理 $R$ 必为常数，但它在无穷远处趋于 $0$，即 $R\equiv0$，这与 $R(\lambda)$ 恒可逆（非零）矛盾。所以 $\sigma(a)\ne\emptyset$。

2. **强制取标量**：任取 $\lambda\in\sigma(a)$。由 $\sigma$ 的定义，$a-\lambda I$ 不可逆。由可除性假设，不可逆元素只能是 $0$，故 $a-\lambda I=0$，即 $a=\lambda I$。由于 $a\in A$ 任意，$A=\mathbb C I$，于是 $A$ 与 $\mathbb C$ 同构；取 $\|I\|=1$ 时该同构为等距。

## 三、定理的严格表述

**（Gelfand–Mazur 定理）** 设 $A$ 是含单位元 $I$ 的复 Banach 代数，且 $A$ 是**可除代数**，即
$$\forall a\in A,\quad a\ne0\ \Longrightarrow\ a\ \text{可逆}.$$
则对任意 $a\in A$，存在唯一的 $\lambda\in\mathbb C$ 使
$$a=\lambda I,$$
从而映射
$$\mathbb C\longrightarrow A,\qquad \lambda\longmapsto\lambda I$$
是 Banach 代数的同构，且若 $\|I\|=1$ 则它是等距同构：$\|\lambda I\|=|\lambda|$。

**推论（Gelfand 理论的基础）**：设 $B$ 是交换含单位元的复 Banach 代数，$M\subseteq B$ 是极大理想。则商代数 $B/M$ 是含单位元的复 Banach 可除代数，故 $B/M\cong\mathbb C$。于是存在唯一的连续代数同态（**特征标**）$\varphi_M:B\to\mathbb C$ 使 $\ker\varphi_M=M$。由此 $B$ 通过
$$\widehat{b}(\varphi)=\varphi(b),\qquad \varphi\in\mathfrak M_B$$
嵌入极大理想空间 $\mathfrak M_B$ 上的连续函数代数。

**注（实数域的反例）**：$\mathbb C$ 作为 $\mathbb R$-Banach 代数仍是可除的但不与 $\mathbb R$ 同构；四元数代数 $\mathbb H$ 是 $\mathbb R$ 上的可除 Banach 代数（甚至每个非零元可逆），且不同构于 $\mathbb C$。因此定理中"复"字不可去。

## 四、证明过程

**步骤 1：$a-\lambda I$ 在 $|\lambda|>\|a\|$ 时可逆。**

对 $a\in A$、$|\lambda|>\|a\|$，有 $\|a/\lambda\|<1$。Neumann 级数
$$\sum_{n=0}^{\infty}\left(\frac{a}{\lambda}\right)^{n}$$
在范数下绝对收敛，其和 $s\in A$ 满足
$$s\left(I-\frac{a}{\lambda}\right)=\left(I-\frac{a}{\lambda}\right)s=I,$$
故 $I-a/\lambda$ 可逆且 $\left(I-a/\lambda\right)^{-1}=\sum_{n\ge0}(a/\lambda)^n$。于是
$$(\lambda I-a)^{-1}=\frac{1}{\lambda}\left(I-\frac{a}{\lambda}\right)^{-1}=\frac{1}{\lambda}\sum_{n=0}^{\infty}\left(\frac{a}{\lambda}\right)^{n},$$
且
$$\left\|(\lambda I-a)^{-1}\right\|\le\frac{1}{|\lambda|}\cdot\frac{1}{1-\|a\|/|\lambda|}=\frac{1}{|\lambda|-\|a\|}.$$
因此 $\rho(a)\supseteq\{|\lambda|>\|a\|\}$，即 $\sigma(a)\subseteq\{|\lambda|\le\|a\|\}$。

**步骤 2：预解映射是解析的。**

由步骤 1 的 Neumann 级数，$\lambda\mapsto R(\lambda)=(\lambda I-a)^{-1}$ 在 $|\lambda|>\|a\|$ 上可展为收敛幂级数，故解析。在 $\rho(a)$ 的一般点 $\lambda_0$，由预解恒等式
$$R(\lambda)-R(\lambda_0)=(\lambda_0-\lambda)R(\lambda)R(\lambda_0)$$
可得当 $|\lambda-\lambda_0|<\|R(\lambda_0)\|^{-1}$ 时
$$R(\lambda)=\sum_{n=0}^{\infty}(-1)^{n}(\lambda-\lambda_0)^{n}R(\lambda_0)^{n+1},$$
故 $R$ 在 $\rho(a)$ 上处处解析。又由步骤 1，$\|R(\lambda)\|\to0\ (\lambda\to\infty)$。

**步骤 3：谱非空。**

反设 $\sigma(a)=\emptyset$，则 $\rho(a)=\mathbb C$，$R$ 是整函数。由步骤 1，$|\lambda|>\|a\|$ 时 $\|R(\lambda)\|\le(|\lambda|-\|a\|)^{-1}\le1$（对 $|\lambda|\ge\|a\|+1$）；而 $\{|\lambda|\le\|a\|+1\}$ 是紧集，$R$ 在其上连续，故有界。于是 $R$ 是整函数且有界，由 Liouville 定理 $R\equiv$ 常数。但步骤 1 给出 $\|R(\lambda)\|\to0$，故该常数为 $0$，即 $R(\lambda)=0$。然而 $R(\lambda)=(\lambda I-a)^{-1}$ 作为可逆元不可能为 $0$（$R(\lambda)(\lambda I-a)=I\ne0$），矛盾。故 $\sigma(a)\ne\emptyset$。

**步骤 4：可除性强制 $a$ 为标量。**

由步骤 3 取 $\lambda\in\sigma(a)$。由谱的定义，$a-\lambda I$ 不可逆。由可除性假设，$A$ 中唯一的不可逆元是 $0$，故
$$a-\lambda I=0,\qquad\text{即}\qquad a=\lambda I.$$

**步骤 5：唯一性与等距性。**

$\lambda$ 唯一：若 $\lambda I=\mu I$ 且 $\lambda\ne\mu$，则 $(\lambda-\mu)I=0$，$I=0$，与含单位元矛盾。

由步骤 4，$A=\{\lambda I:\lambda\in\mathbb C\}$。映射 $\Phi(\lambda)=\lambda I$ 是双射、保持加法与乘法、保持单位，故为代数同构。若把 $A$ 的范数取为标准范数（$\|I\|=1$，可通过对范数作等价替换实现），则
$$\|\Phi(\lambda)\|=\|\lambda I\|=|\lambda|\,\|I\|=|\lambda|,$$
故 $\Phi$ 是等距同构。因此 $A\cong\mathbb C$ 作为含单位复 Banach 代数（等距同构意义下）。$\square$

**步骤 6：推出极大理想版本的推论。**

设 $B$ 交换含单位、$M$ 为极大理想。$M$ 是闭双边理想（理想闭包仍是真理想，否则 $M$ 的闭包为 $B$ 与极大性矛盾）。商代数 $B/M$ 含单位、是交换 Banach 代数，且由 $M$ 极大知 $B/M$ 只有平凡理想，故是可除代数。由定理 $B/M\cong\mathbb C$。复合 $B\to B/M\xrightarrow{\ \cong\ }\mathbb C$ 即为特征标 $\varphi_M$，$\ker\varphi_M=M$。$\square$

## 五、应用与意义

**理论意义**：
1. **Gelfand 谱理论**：Gelfand–Mazur 定理给出交换 Banach 代数的"特征标存在性"，从而建立 Gelfand 变换 $b\mapsto\widehat{b}$ 与极大理想空间 $\mathfrak M_B$，把交换 Banach 代数表示为连续函数代数。
2. **$C^*$-代数结构**：交换 $C^*$-代数由 Gelfand 变换等距同构于 $C_0(X)$（Gelfand–Naimark 交换版本），其基础即 Gelfand–Mazur 定理。
3. **泛函演算**：由 Gelfand 变换得到连续函数演算与谱映射定理的另一种证明。

**应用领域**：
1. **算子代数**：用于刻画交换 von Neumann 代数（$L^\infty(X,\mu)$）与交换 $C^*$-代数，是 GNS 构造与谱理论的起点。
2. **调和分析**：群代数 $L^1(G)$ 的极大理想空间给出对偶群 $\widehat G$，其间 Gelfand–Mazur 保证特征标（即群同态 $G\to\mathbb T$）的存在。
3. **数值分析**：用于证明 Banach 代数谱半径与迭代收敛理论的代数基础。
4. **函数论与代数学**：Frobenius 定理（实可除代数的分类）与 Gelfand–Mazur 定理共同刻画了"可除的 Banach 代数"这一范畴。

**推广与相关结果**：
- **Gelfand–Mazur 的实版本**：$\mathbb R$ 上的可除 Banach 代数可有 $\mathbb R,\mathbb C,\mathbb H$ 等，非唯一。
- **非结合情形**：在 Jordan–Banach 代数中有相应的"Gelfand–Mazur 型"定理（如 Wright–Youngson 定理），断言某些不可逆元结构的唯一性。
- **局部凸版本**：在局部凸可除代数中定理不总成立，说明 Banach 范数的完备性不可缺。

## 课堂问答

**老师**：复 Banach 可除代数凭什么只能是 $\mathbb C$，关键在哪一步？

**学生**：结论：$A$ 等距同构于 $\mathbb C$。关键在谱非空：若 $\sigma(a)=\emptyset$，预解算子 $R(\lambda)=(\lambda I-a)^{-1}$ 是整函数，且 $|\lambda|>\|a\|$ 时 $\|R(\lambda)\|\le(|\lambda|-\|a\|)^{-1}\to0$ 故有界，由 Liouville 定理得 $R\equiv0$，与 $R(\lambda)$ 可逆矛盾。

**老师（追问）**：为什么取 $\lambda\in\sigma(a)$ 就能逼 $a$ 是标量？

**学生**：因为 $\lambda\in\sigma(a)$ 意味着 $a-\lambda I$ 不可逆，可除性假设说不可逆元只能为 $0$，于是 $a-\lambda I=0$，即 $a=\lambda I$。常见误区：把"复"字去掉，实域上四元数 $\mathbb H$ 就是可除 Banach 代数却不同构于 $\mathbb C$。

**老师（拓展）**：这条定理怎么成为 Gelfand 理论的枢纽？

**学生**：结论：它给出交换 Banach 代数的特征标。对极大理想 $M$，$B/M$ 是含单位可除 Banach 代数，故 $B/M\cong\mathbb C$，得到特征标 $\varphi_M$，进而 Gelfand 变换 $b\mapsto\widehat b$ 把 $B$ 实现为极大理想空间上的连续函数代数。
