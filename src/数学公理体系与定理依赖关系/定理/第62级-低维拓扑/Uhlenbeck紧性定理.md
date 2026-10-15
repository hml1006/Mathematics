# Uhlenbeck 紧性定理

> **一句话大白话**：只要一族联络的"弯曲程度"（曲率的 $L^2$ 范数）被一致控制，就能通过规范变换把它们局部摆正，使其在一个个小区块上规矩收敛，至多在有限个点上曲率浓缩成"泡泡"炸开。
>
> **小例子**：$S^4$ 上一列 $SU(2)$ 联络若满足 $\|F_{A_i}\|_{L^2}\le C$，则存在规范等价子列在离开有限点集处 $W^{1,2}_{\mathrm{loc}}$ 弱收敛，且曲率测度 $|F_{A_i}|^2\,dv$ 弱收敛为极限曲率测度与若干 Dirac 质量之和。

## 一、定理介绍

> **前置依赖**：主丛上的联络与曲率、Sobolev 空间 $W^{k,p}$ 及其紧嵌入、规范变换与 Coulomb 规范、椭圆算子的 $L^p$ 正则性估计、Hodge 分解与弱紧性。

Uhlenbeck 紧性定理（Uhlenbeck compactness theorem）是 Karen Uhlenbeck 于 1982 年在研究四维 Yang–Mills 方程时建立的基本结论，它回答了一个核心问题：一族联络在什么条件下"除有限个奇点外"收敛。

困难在于联络 $A$ 本身不是规范不变量，直接谈收敛没有几何意义——同一几何构型可有无穷多个规范等价的联络表示。Uhlenbeck 的洞察是：只要曲率 $F_A$ 的能量 $\|F_A\|_{L^2}^2$ 一致有界，就能先在局部选取 Coulomb 规范 $d^*A=0$，把联络化为椭圆方程的解，从而用 Sobolev 估计重新获得对 $A$ 本身的控制；若能量集中在少数点上，则这些点成为极限的奇异点，其损失的能量以 Dirac 质量的形式记录在曲率测度中。这一"除有限点外紧"的性质是 Donaldson 不变量的定义基础，也是四维流形微分拓扑的核心工具。

## 二、原理思路

1. **规范固定（gauge fixing）**：在曲率能量足够小的球上，存在规范变换使 $d^*A=0$。此时 $A$ 满足椭圆方程 $\Delta A=d^*F_A+\{\text{$A$ 的二次项}\}$，由 Calderón–Zygmund 估计与临界 Sobolev 嵌入 $W^{1,2}\hookrightarrow L^4$ 得到 $\|A\|_{W^{1,2}}\le C\|F_A\|_{L^2}$，即"小曲率蕴含小联络"。
2. **有限覆盖**：曲率总能量有界，故曲率超过阈值 $\epsilon_0$ 的位置只能落在有限多个小球的并里；其余区域被"好球"覆盖，每个好球上都有规范控制。
3. **规范拼接**：在相邻好球的交集上，两个局部规范相差一个规范变换，用过渡函数把局部规范拼成整体规范 $g_i$。
4. **弱紧与爆破**：在 $M$ 挖去有限个集中点后，$W^{1,2}$ 局部弱紧给出收敛子列；曲率测度在集中点处产生原子。

## 三、定理的严格表述

设 $P\to M$ 为紧致可定向 Riemann 流形 $M^4$ 上的主 $G$-丛，$G$ 为紧 Lie 群，$\mathfrak g$ 为其 Lie 代数。$A$ 为 $P$ 上的联络，$F_A\in\Omega^2(M;\mathrm{ad}\,P)$ 为其曲率。

**定理 1（Coulomb 规范定理，Uhlenbeck 规范固定）.** 存在仅依赖 $G$ 与 $M$ 局部几何的常数 $\epsilon_0>0$，使得若联络 $A$ 在测地球 $B_r(x)$ 上满足 $\|F_A\|_{L^2(B_r(x))}\le\epsilon_0$，则存在规范变换 $g$（定义于 $B_r(x)$ 上，取值于 $G$），使 $\tilde A=g\cdot A$ 满足 Coulomb 规范条件

$$
d^*\tilde A=0
$$

以及整体估计

$$
\|\tilde A\|_{W^{1,2}(B_{r/2}(x))}\le C\,\|F_A\|_{L^2(B_r(x))},
$$

其中 $C=C(G)$ 与球半径 $r$ 无关。

**定理 2（Uhlenbeck 紧性）.** 设 $\{A_i\}$ 为 $P$ 上一列联络，满足一致能量界

$$
\sup_i\ \|F_{A_i}\|_{L^2(M)}\le C_0<+\infty .
$$

则存在规范变换 $\{g_i\}$、子列（不失一般性仍记作 $A_i$）、有限点集 $S=\{x_1,\dots,x_l\}\subset M$、以及 $M\setminus S$ 上的联络 $A_\infty$，使得

$$
g_i\cdot A_i \rightharpoonup A_\infty
\qquad\text{在 } W^{1,2}_{\mathrm{loc}}(M\setminus S)\ \text{中弱收敛},
$$

并且曲率测度满足

$$
|F_{A_i}|^2\,dv \rightharpoonup |F_{A_\infty}|^2\,dv+\sum_{j=1}^{l}m_j\,\delta_{x_j},
$$

其中爆破质量 $m_j\ge0$ 且

$$
\sum_{j=1}^{l}m_j\le \liminf_{i\to\infty}\|F_{A_i}\|_{L^2(M)}^2-\|F_{A_\infty}\|_{L^2(M\setminus S)}^2 .
$$

进一步，若 $A_i$ 为反自对偶（$F_{A_i}^+=0$）且能量有界，则 $A_\infty$ 亦为反自对偶，且 $S$ 中的每个点是极限联络的"可去奇点或泡泡点"，泡泡本身是 $S^4$ 上的反自对偶联络。

## 四、证明过程

**步骤 1：Coulomb 规范的椭圆估计.** 给定联络 $A$，先作规范变换使 $d^*A=0$。在 Coulomb 规范下 $A$ 满足

$$
\Delta A=d^*F_A+*\!\left(*F_A\wedge A\right)+\text{（$A$ 的二次项）},
$$

其中 $\Delta=d^*d+dd^*$ 是 Hodge–de Rham Laplacian。由 Calderón–Zygmund $L^p$ 估计（$p=2$ 情形）

$$
\|A\|_{W^{1,2}}\le C\bigl(\|F_A\|_{L^2}+\|A\wedge A\|_{L^2}\bigr).
$$

在四维临界情形 $W^{1,2}\hookrightarrow L^4$，再由 Hölder 不等式 $\|A\wedge A\|_{L^2}\le \|A\|_{L^4}^2\le C'\|A\|_{W^{1,2}}^2$，得

$$
\|A\|_{W^{1,2}}\le C_1\bigl(\|F_A\|_{L^2}+\|A\|_{W^{1,2}}^2\bigr).
$$

当 $\|F_A\|_{L^2}\le\epsilon_0$ 足够小、使得 $C_1\|A\|_{W^{1,2}}\le\frac12$ 成立时，二次项可被左端吸收，于是

$$
\|A\|_{W^{1,2}}\le 2C_1\|F_A\|_{L^2}.
$$

这就得到定理 1。关键在于 $\epsilon_0$ 与 $C_1$ 只依赖 $G$ 与 $M$ 的局部几何（内射半径、曲率界），与球的大小无关，因此可用于有限覆盖。

**步骤 2：曲率集中点至多有限.** 固定阈值 $\epsilon_0/2$（来自步骤 1）。对序列 $\{A_i\}$，用 Vitali 型覆盖引理选出互不相交的球 $\{B_{\rho_k}(x_k)\}$，使得曲率在 $\bigcup_k B_{\rho_k}(x_k)$ 上集中。因为每个这样的球满足 $\|F_{A_i}\|_{L^2(B_{\rho_k})}\ge\epsilon_0/2$，能量加和得

$$
\#\{k\}\cdot\frac{\epsilon_0^2}{4}\le\|F_{A_i}\|_{L^2(M)}^2\le C_0^2,
$$

故这样的球至多 $\lfloor 4C_0^2/\epsilon_0^2\rfloor$ 个。令 $S$ 为其中心点的极限集（取子列收敛），$S$ 有限。定义"好区域" $M\setminus S$：其上任意紧集可被有限多个曲率小于 $\epsilon_0$ 的球覆盖。

**步骤 3：好球上取规范并拼接.** 在 $M\setminus S$ 的每个好球上依定理 1 选取 Coulomb 规范，得到局部联络 $\tilde A_{i}^{(\alpha)}$ 与统一的 $W^{1,2}$ 界 $2C_1C_0$。相邻好球 $U_\alpha,U_\beta$ 的交集上，$\tilde A_i^{(\alpha)}$ 与 $\tilde A_i^{(\beta)}$ 是同一联络的两个 Coulomb 表示，故

$$
\tilde A_i^{(\beta)}=g_{\alpha\beta}\cdot\tilde A_i^{(\alpha)}
$$

对某过渡函数 $g_{\alpha\beta}:U_\alpha\cap U_\beta\to G$；由 $d^*$ 条件可解出 $g_{\alpha\beta}$ 且其在紧集上有统一 $W^{1,2}$（或 $W^{2,2}$）界。沿覆盖的"树形"结构把 $\alpha$ 逐个连接到基准球，用 $g_{\alpha\beta}$ 修正局部规范，最终得到整体定义于 $M\setminus S$ 上的规范变换 $g_i$，使 $g_i\cdot A_i$ 在每个紧集上有统一 $W^{1,2}$ 界。

**步骤 4：弱紧与子列.** 设 $K\subset M\setminus S$ 为紧集。由步骤 3，$\|g_i\cdot A_i\|_{W^{1,2}(K)}\le 2C_1C_0$ 一致有界。由 $W^{1,2}(K)$ 的自反性与 Banach–Alaoglu 定理，存在子列在 $W^{1,2}(K)$ 中弱收敛到某联络 $A_\infty^{(K)}$。用 $K$ 的可数 exhaustion（$K_1\subset K_2\subset\cdots$）作对角线抽取，得到在整个 $M\setminus S$ 上 $W^{1,2}_{\mathrm{loc}}$ 弱收敛的联络 $A_\infty$。

**步骤 5：曲率测度的极限.** 测度 $\mu_i=|F_{A_i}|^2\,dv$ 非负且总质量 $\le C_0^2$，故存在子列弱收敛到某有限 Radon 测度 $\mu$。在 $M\setminus S$ 的任一紧集 $K$ 上，$g_i\cdot A_i\rightharpoonup A_\infty$ 于 $W^{1,2}(K)$，由临界嵌入 $W^{1,2}\hookrightarrow L^4$ 的紧性（$K$ 有界维数 4，嵌入为 Rellich–Kondrachov 紧嵌入）可得 $A_i\to A_\infty$ 于 $L^4(K)$，从而 $F_{g_i\cdot A_i}\to F_{A_\infty}$ 于 $L^2(K)$，即

$$
\mu|_{M\setminus S}=|F_{A_\infty}|^2\,dv .
$$

由于曲率是规范不变的（$|F_{g\cdot A}|=|F_A|$），$\mu_i$ 与规范选取无关。故 $\mu-|F_{A_\infty}|^2\,dv$ 支撑在有限集 $S$ 上，必有形式 $\sum_j m_j\delta_{x_j}$，$m_j\ge0$。

**步骤 6：质量不等式.** 对任意包含 $S$ 的小开邻域 $U$，把总质量分解为 $U$ 内与 $U$ 外两部分。由测度弱收敛的下半连续性与步骤 5，

$$
\liminf_i\|F_{A_i}\|_{L^2}^2=\liminf_i\mu_i(M)\ge\mu(M)=|F_{A_\infty}|^2(M\setminus S)+\sum_j m_j,
$$

即得质量不等式。当 $U$ 收缩到 $S$ 时等式对应的极限存在，爆破质量即能量缺口。

**步骤 7：反自对偶情形.** 若 $F_{A_i}^+=0$，则 $F_{A_i}=\frac12*F_{A_i}$ 的 $L^2$ 范数与 $F_{A_i}$ 相同。由步骤 4 的收敛与 $F^+$ 的连续性，$F_{A_\infty}^+=0$，故极限仍反自对偶。$S$ 中每点的小球在极小化能量后经共形紧化给出 $S^4$ 上的反自对偶联络，即"泡泡"，其能量为 $8\pi^2 k$（$k\in\mathbb Z$ 为瞬子数）。$\square$

**注.** 步骤 1 中 $\epsilon_0$ 与半径无关是全部论证得以成立的关键；若没有 Coulomb 规范，联络的 $W^{1,2}$ 范数无法由曲率控制，弱紧性便无从谈起。

## 五、应用与意义

- **模空间紧化**：反自对偶联络模空间 $\mathcal M$ 的紧化正是"除有限点外收敛"，Uhlenbeck 定理使 $\overline{\mathcal M}$ 的奇点结构可控，从而 Donaldson 不变量良定义。
- **四维流形**：Donaldson 对角化定理、光滑结构的存在性与唯一性研究均以该紧性定理为技术前提。
- **拼接与构造**：反自对偶解与近似解可通过规范固定的局部估计逐块拼接（gluing），用于构造新型解与计算不变量。
- **一般理论**：与 Sacks–Uhlenbeck 关于调和映射的 bubble 分析、Gromov 紧性、Seiberg–Witten 理论同属"能量集中与紧化"的范式，是几何分析的基本工具。

## 课堂问答

**老师**：为什么曲率 $L^2$ 有界就能得到除有限点外收敛？

**学生**：结论：因为规范固定把曲率控制转成联络控制。在曲率小的球上存在规范使 $d^*A=0$，此时 $A$ 满足椭圆方程 $\Delta A=d^*F_A+\{A\wedge A\}$，由 Calderón–Zygmund 估计与临界嵌入 $W^{1,2}\hookrightarrow L^4$ 得 $\|A\|_{W^{1,2}}\le C\|F_A\|_{L^2}$，即小曲率蕴含小联络。

**老师（追问）**：能量集中点为什么有限？

**学生**：坏球的每个曲率能量 $\ge\epsilon_0/2$，而总能量 $\le C_0^2$，故坏球个数 $\le4C_0^2/\epsilon_0^2$，其中心极限点集 $S$ 有限。$M\setminus S$ 上被好球覆盖，可拼接规范取 $W^{1,2}$ 子列，且曲率测度满足 $|F_{A_i}|^2\,dv\rightharpoonup|F_{A_\infty}|^2\,dv+\sum_jm_j\delta_{x_j}$，损失能量以 Dirac 质量记在集中点。

**老师（拓展）**：ASA 情形为什么给出泡泡？

**学生**：若 $F_{A_i}^+=0$，极限仍反自对偶。在坏点处作尺度 $r_k\to0$ 的吹起，四维 Yang–Mills 能量在共形伸缩下不变，得 $S^4$ 上的反自对偶联络，能量为 $8\pi^2k$（$k$ 为瞬子数）。剩余能量小于 $\epsilon$ 时该点实为可去奇点，否则浓缩成泡泡。这正是模空间紧化的图景，是 Donaldson 不变量良定义的技术前提。
