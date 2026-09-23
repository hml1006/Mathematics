# Ulam 胎紧定理

> **一句话大白话**：波兰空间上的每个概率测度都是"胎紧"的——无论精度要求多高，总能找到一个固定的紧集，把全部质量（除任意小的一点点之外）装进去；顺带地，每个 Borel 集都能被里面的大紧集和外面的大开集"夹"住。
>
> **小例子**：$\mathbb R$ 上的标准正态分布是胎紧的：对每个 $\epsilon>0$，取 $K=[-R,R]$ 使 $\mathbb P(|X|>R)<\epsilon$。同理，$\mathbb R$ 上任何概率测度都可以用有限个小区间把质量集中起来，因为这些区间的并是闭且有界的，从而紧。

## 介绍

在 $\sigma$-有限测度空间中，"正则性"是说一个测度可以被好的集合（紧集、开集）逼近。Ulam 胎紧定理断言：**波兰空间（可分的完备度量空间）上的每个有限 Borel 测度都是正则的**，其中"从内部逼近"用的集合正是紧集——这一性质称为**胎紧**（tight）。定理的核心是著名的一行构造

$$K=\bigcap_{m\ge1}\overline{\bigcup_{i\le N_m}B\big(x_i^{(m)},1/m\big)},$$

即"用可数多个半径不断变小的球层层套住"，得到的集合闭且有界（全有界），在完备空间里就是紧的；每一次套取造成的质量损失可以预先分配成 $\epsilon/2^m$，总损失小于 $\epsilon$。

胎紧性为什么重要？因为概率测度空间在弱拓扑下不是自动紧的，而 Prokhorov 定理指出"弱相对紧 $\Leftrightarrow$ 胎紧"，于是"找收敛子列"这一拓扑问题被转化为"为全族找同一个大紧集"这一可操作问题。此外，胎紧性（加上正则性）是 Riesz 表示定理中"$\sigma$-光滑正线性泛函由测度表示"的技术前提，也是随机过程弱收敛理论的起点。

需要注意的是，**可分性与完备性缺一不可**：在不可分空间上（如 $[0,1]$ 上赋予离散 $\sigma$-代数之外的病态空间）存在非胎紧的概率测度；在不完备空间上有"质量跑到洞里"的例子。

## 分析

**前置依赖**：波兰空间（可分完备度量空间）、Borel 测度、测度的连续性（从下、从上）、度量空间中"闭集 + 全有界 $\Leftrightarrow$ 紧"、距离函数 $x\mapsto d(x,A)$ 的 Lipschitz 连续性、$\lambda$-系统（Dynkin 系统）与单调类定理。

**定理内容**：设 $S$ 是波兰空间，$\mu$ 是 $S$ 上的有限 Borel 测度（特别地，概率测度）。则

**(1) 胎紧性**：对每个 $\epsilon>0$，存在紧集 $K\subseteq S$ 使 $\mu(K)>\mu(S)-\epsilon$。

**(2) 内正则性（对紧集）**：对每个 Borel 集 $A$ 与每个 $\epsilon>0$，存在紧集 $K\subseteq A$ 使 $\mu(A\setminus K)<\epsilon$。

**(3) 正则性**：对每个 Borel 集 $A$，

$$\mu(A)=\sup\{\mu(K):K\subseteq A,\ K\ \text{紧}\}=\inf\{\mu(G):G\supseteq A,\ G\ \text{开}\}.$$

**证明策略**：先由可分性取可数球覆盖、由测度的连续性从下取有限子覆盖，构造出满足 (1) 的紧集 $K$。再用 $K$ 把任意闭集 $A$ 从内部用紧集 $A\cap K$ 逼近，得到"闭集 $\Rightarrow$ 内正则"。然后证明"内正则集"全体构成 $\sigma$-代数（对可数并、可数交封闭 + 补集），从而含一切 Borel 集，得到 (2)。最后由 (2) 应用于补集得外正则，得到 (3)。

## 思考过程

**紧集从哪来？** 在一般度量空间中构造紧集只有一条路：**全有界 + 完备**。全有界意味着"对每个 $\delta>0$，可被有限多个半径 $\delta$ 的球覆盖"。可分性恰好保证对每个固定的半径 $1/m$，空间可被**可数**多个球覆盖；再用测度对递增并的连续性，从可数覆盖中只留有限多个，就损失了任意小的质量。把这些"有限覆盖的闭包"对 $m=1,2,3,\dots$ 求交，就得到一个集合 $K$：它对每个 $m$ 都被有限多个半径 $1/m$ 的球覆盖，故全有界；它是闭的，故在完备空间中是紧的。

**为什么"每次损失 $\epsilon/2^m$"是合法的？** 因为 $\sum_m\epsilon/2^m=\epsilon$。这要求我们**同时**控制所有 $m$；而每个 $m$ 的损失都可以独立地取到 $\epsilon/2^m$ 以内，这是可分性给出的自由度。

**怎样从"空间本身胎紧"推到"每个 Borel 集都能被紧集从内部逼近"？** 对闭集直接做：$A$ 闭，取全空间里的大紧集 $K$，则 $A\cap K$ 是紧集（闭集与紧集之交），且 $A\setminus(A\cap K)\subseteq S\setminus K$，质量损失继承下来。

对一般 Borel 集，需要用集合系的论证。定义

$$\mathcal{R}=\{A\in\mathcal B(S):\ A\ \text{与}\ A^c\ \text{都能被紧集从内部逼近}\}.$$

$\mathcal{R}$ 对补集封闭是定义带来的对称性；对**可数并**封闭是因为"可数并的内正则性"直接成立；对**可数交**封闭则因为内正则集的有限交与可数交仍然内正则（用 Heine–Borel 式的估计：先对前 $N$ 个各留一点误差，再把尾部整体丢掉）。由于闭集属于 $\mathcal{R}$（闭集内正则已证，补集是开集也内正则 —— 而开集可以写成可数个闭集的递增并，故由可数并封闭性也内正则），$\mathcal{R}$ 是含一切闭集的 $\sigma$-代数，只能是 $\mathcal B(S)$。

**外正则性从哪来？** 把 (2) 用在补集上：$A$ 的补集 $A^c$ 内有紧集 $K$ 使 $\mu(A^c\setminus K)<\epsilon$，则 $G=K^c$ 是开集、包含 $A$，且 $\mu(G\setminus A)=\mu(A^c\setminus K)<\epsilon$。

## 证明过程

**步骤 1：构造胎紧的紧集（证明 (1)）。**

设 $\mu(S)>0$；固定 $\epsilon>0$。

因 $S$ 可分，对每个 $m\ge1$，取可数稠密集 $\{x_i^{(m)}\}_{i\ge1}$，则 $S=\bigcup_{i\ge1}B(x_i^{(m)},1/m)$。由测度的连续性从下（递增并），

$$\lim_{N\to\infty}\mu\Big(\bigcup_{i=1}^{N}B(x_i^{(m)},1/m)\Big)=\mu(S),$$

故存在 $N_m$ 使

$$\mu\Big(A_m\Big)>\mu(S)-\frac{\epsilon}{2^m},\qquad A_m:=\bigcup_{i=1}^{N_m}B\big(x_i^{(m)},1/m\big).$$

令

$$K:=\bigcap_{m\ge1}\overline{A_m}.$$

**$K$ 是闭集**：任意多个闭集之交闭。**$K$ 全有界**：给定 $\delta>0$，取 $m$ 充分大使得 $2/m<\delta$。因为

$$K\subseteq\overline{A_m}\subseteq\bigcup_{i\le N_m}\overline{B\big(x_i^{(m)},1/m\big)}\subseteq\bigcup_{i\le N_m}B\big(x_i^{(m)},2/m\big),$$

故 $K$ 被有限多个半径 $2/m<\delta$ 的球覆盖，即全有界。**因 $S$ 完备，闭且全有界蕴含紧**，故 $K$ 紧。

最后估计质量：由递增并的次可加性，

$$\mu(S\setminus K)=\mu\Big(\bigcup_{m\ge1}\big(S\setminus\overline{A_m}\big)\Big)\le\sum_{m\ge1}\mu\big(S\setminus\overline{A_m}\big)\le\sum_{m\ge1}\mu(S\setminus A_m)<\sum_{m\ge1}\frac{\epsilon}{2^m}=\epsilon .$$

（用到了 $\mu(S\setminus\overline{A_m})\le\mu(S\setminus A_m)$。）故 $\mu(K)>\mu(S)-\epsilon$。(1) 得证。

**步骤 2：闭集的内正则性。**

设 $A\subseteq S$ 闭，$\epsilon>0$。由步骤 1 取紧集 $K$ 使 $\mu(S\setminus K)<\epsilon$。则 $A\cap K$ 紧（紧集的闭子集），$A\cap K\subseteq A$，且

$$\mu\big(A\setminus(A\cap K)\big)=\mu(A\setminus K)\le\mu(S\setminus K)<\epsilon .$$

**步骤 3：开集的内正则性。**

设 $U\subseteq S$ 开。由距离函数的连续性，$U=\bigcup_{m\ge1}F_m$，其中

$$F_m=\Big\{x\in S:\ d(x,U^c)\ge\frac1m\Big\}$$

（约定 $d(x,\varnothing)=+\infty$，此时所有 $F_m=S$）；每个 $F_m$ 是闭集，且 $F_m\uparrow U$。由步骤 2，每个 $F_m$ 内正则；而递增并的极限由测度的连续性从下处理：给定 $\epsilon$，取 $m$ 使 $\mu(U\setminus F_m)<\epsilon/2$，再取紧集 $K_m\subseteq F_m\subseteq U$ 使 $\mu(F_m\setminus K_m)<\epsilon/2$，则 $\mu(U\setminus K_m)<\epsilon$。故开集内正则。

**步骤 4：一切 Borel 集的内正则性（证明 (2)）。**

定义

$$\mathcal{R}:=\Big\{A\in\mathcal B(S):\ \forall\epsilon>0\ \exists K\ \text{紧},\ K\subseteq A,\ \mu(A\setminus K)<\epsilon\Big\},$$

即 $\mathcal{R}$ 为全体"内正则"的 Borel 集。下面证明 $\mathcal R=\mathcal B(S)$。

**(i) $\mathcal R$ 对可数并封闭**：设 $A_i\in\mathcal R$，$A=\bigcup_iA_i$。给定 $\epsilon$，对每个 $i$ 取紧集 $K_i\subseteq A_i$ 使 $\mu(A_i\setminus K_i)<\epsilon/2^i$。取 $N$ 使 $\mu\big(\bigcup_{i>N}A_i\big)<\epsilon$（由连续性从下）。令 $K=\bigcup_{i\le N}K_i$，它是有限个紧集之并，故紧，且 $K\subseteq A$。又

$$A\setminus K\subseteq\Big(\bigcup_{i\le N}(A_i\setminus K_i)\Big)\cup\Big(\bigcup_{i>N}A_i\Big),$$

故 $\mu(A\setminus K)<\sum_{i\le N}\epsilon/2^i+\epsilon<2\epsilon$。由 $\epsilon$ 任意，$A\in\mathcal R$。

**(ii) $\mathcal R$ 对可数交封闭**：设 $A_i\in\mathcal R$，$A=\bigcap_iA_i$。对每个 $i$ 取紧集 $K_i\subseteq A_i$ 使 $\mu(A_i\setminus K_i)<\epsilon/2^i$。令 $K=\bigcap_{i\le N}K_i$（有限交，紧）对某个待定 $N$。则 $K\subseteq A$，且

$$A\setminus K=\Big(\bigcap_iA_i\Big)\setminus\Big(\bigcap_{i\le N}K_i\Big)\subseteq\bigcup_{i\le N}\big(A_i\setminus K_i\big),$$

（若 $x\in A$ 但 $x\notin\bigcap_{i\le N}K_i$，则存在 $i\le N$ 使 $x\notin K_i$，而 $x\in A_i$，故 $x\in A_i\setminus K_i$。）于是 $\mu(A\setminus K)\le\sum_{i\le N}\epsilon/2^i<\epsilon$，与 $N$ 无关。故 $A\in\mathcal R$。

**(iii) $\mathcal R$ 对补集封闭**：设 $A\in\mathcal R$，即存在紧集 $K\subseteq A$ 使 $\mu(A\setminus K)<\epsilon$。由步骤 3，开集 $K^c\supseteq A^c$ 内正则：存在紧集 $L\subseteq K^c$ 使 $\mu(K^c\setminus L)<\epsilon$。因 $K^c\setminus A^c=K^c\cap A=A\setminus K$，故

$$\mu\big(A^c\setminus L\big)=\mu\big(K^c\setminus L\big)-\mu\big(K^c\setminus(L\cup A^c)\big)\le\mu(K^c\setminus L)<\epsilon .$$

且 $L\subseteq K^c\subseteq A^c$ 紧。故 $A^c\in\mathcal R$。

**(iv) $\mathcal R$ 含一切闭集**：由步骤 2，闭集内正则，故属于 $\mathcal R$（注意 $\mathcal R$ 的定义只要求集合本身内正则，因此闭集显然属于 $\mathcal R$）。

由 (i)(ii)(iii)，$\mathcal R$ 是含一切闭集的 $\sigma$-代数，故 $\mathcal R\supseteq\sigma(\text{闭集})=\mathcal B(S)$；结合 $\mathcal R\subseteq\mathcal B(S)$ 得 $\mathcal R=\mathcal B(S)$。这就证明了 (2)。

**步骤 5：外正则性（证明 (3)）。**

设 $A\in\mathcal B(S)$，$\epsilon>0$。由步骤 4 应用于补集 $A^c$，存在紧集 $K\subseteq A^c$ 使 $\mu(A^c\setminus K)<\epsilon$。令 $G=K^c$，它是开集、$G\supseteq A$，且

$$\mu(G\setminus A)=\mu(K^c\cap A)=\mu\big(A\cap K^c\big)=\mu(A^c\setminus K)<\epsilon .$$

于是在外正则意义下 $\mu(A)=\inf\{\mu(G):G\supseteq A\ \text{开}\}$，结合步骤 4 的内正则性即得 (3)。$\square$

**推论 1（概率测度形式）**：若 $\mu$ 是概率测度，则对每个 $\epsilon>0$ 存在紧集 $K$ 使 $\mu(K)>1-\epsilon$：这正是 Prokhorov 定理中"胎紧"的定义，也是 Kolmogorov 扩张定理构造的路径测度能够取弱收敛子列的前提。

**推论 2（$\sigma$-光滑性）**：设 $f_j\in C_b(S)$，$f_j\downarrow0$ 逐点，则 $\int f_j\,d\mu\to0$。证明：给定 $\eta>0$，由胎紧取紧集 $K$ 使 $\mu(K^c)<\eta$；在紧集 $K$ 上由 Dini 定理 $f_j\to0$ 一致，故对大的 $j$ 有 $\sup_Kf_j<\eta$，于是 $\int f_j\,d\mu\le\sup_Kf_j+\|f_1\|_\infty\eta\to0$。这条性质是 Riesz 表示定理中"$C_b$ 上的正线性泛函由测度表示"的关键一步。

## 相关条目

- [紧性准则](./紧性准则.md)：Prokhorov 定理以本定理为出发点（"紧 $\Rightarrow$ 胎紧"与单个测度胎紧）。
- [Portmanteau定理](./Portmanteau定理.md)：提供开集的测度下半连续性，用于把胎紧性升级为弱相对紧。
- [Kolmogorov扩张定理](./Kolmogorov扩张定理.md)：扩张定理给出的路径测度在本定理保证下才具备弱收敛子列。
