# Donsker 定理

> **一句话大白话**：只要样本独立同分布、方差有限，那么"随机游走的阶梯图"放大后用连续时间去看，就和布朗运动的图像几乎一模一样；同样地，"经验分布函数的偏差曲线"放大后就是一条布朗桥——极限分布不再依赖原分布的具体形状。
>
> **小例子**：掷硬币记 $\pm1$，把前 $k$ 次和的阶梯图按 $\sqrt n$ 缩放，得到一条随机折线；$n$ 很大时它与布朗运动在 $\mathcal C[0,1]$ 上的分布几乎无法区分。这就是"泛函中心极限定理"。

## 一、定理介绍

> **前置依赖**：中心极限定理、连续映射定理、Glivenko-Cantelli定理、Brown运动的存在性、概率论公理（Kolmogorov 公理）、经验分布函数、Brown桥

Donsker 定理（Donsker 1951，又称**泛函中心极限定理** / functional central limit theorem、**不变原理** / invariance principle）是把经典中心极限定理从"单个随机变量"提升到"整条随机函数"的定理。它断言：独立同分布随机变量序列的部分和过程，经过适当的重标度与线性插值，在连续函数空间 $\mathcal C[0,1]$（配一致范数）上**弱收敛**到标准布朗运动。

$$
S_n(t)=\frac{1}{\sqrt n}\sum_{k=1}^{\lfloor nt\rfloor}X_k+(\text{线性插值})\ \Longrightarrow\ B(t)\quad\text{于 }\mathcal C[0,1].
$$

它的意义在于"分布无关性"（distribution-free）：极限过程 $B$ 与 $X_i$ 的具体分布无关，只要均值 $0$、方差 $1$ 有限。因此任何"连续泛函"的极限分布也就与具体分布无关——这正是 Kolmogorov–Smirnov 统计量、Cramér–von Mises 统计量等非参数检验能够查表的原因。

**经验过程版本**是 Donsker 定理在统计中最常用的形式：设 $X_1,X_2,\dots$ 独立同分布，分布函数为 $F$，经验分布函数为 $F_n$，定义经验过程

$$
\alpha_n(t)=\sqrt n\bigl(F_n(t)-F(t)\bigr),\qquad t\in\mathbb R .
$$

则（在 $F$ 连续或更一般的 Donsker 类条件下）$\alpha_n$ 在 $\ell^\infty(\mathbb R)$ 上弱收敛于**布朗桥** $\mathbb G\circ F$，其中 $\mathbb G$ 是标准布朗桥。这一步把"分布函数的整体偏差"变成了布朗桥，从而可以推导出整族非参数统计量的渐近分布与置信带。

## 二、原理思路

弱收敛（$\Rightarrow$，即依分布收敛）在 Polish 空间上由 Prokhorov 定理刻画：**有限维分布收敛 + 胎紧性（tightness）$\iff$ 弱收敛**。Donsker 定理的证明就沿这条路线：

**1. 有限维分布收敛。** 固定 $0\le t_1<\cdots<t_d\le1$，向量 $\bigl(S_n(t_1),\dots,S_n(t_d)\bigr)$ 的各分量是"部分和"的线性组合。由经典中心极限定理与 Cramér–Wold 定理，该向量依分布收敛到多元正态 $\bigl(B(t_1),\dots,B(t_d)\bigr)$——协方差为 $\min(t_i,t_j)$。这一步只用到中心极限定理与布朗运动的有限维分布（后者由[Brown运动的存在性](./Brown运动的存在性.md)给出）。

**2. 胎紧性。** 需要证明：对任意 $\varepsilon>0$，存在紧集 $K\subseteq\mathcal C[0,1]$ 使 $\sup_n P(S_n\notin K)<\varepsilon$。由 Arzelà–Ascoli，紧集由"一致有界 + 等度连续"刻画，故只需控制增量：

$$
P\Bigl(\sup_{|s-t|\le\delta}|S_n(s)-S_n(t)|\ge\eta\Bigr)\ \le\ \text{（与 }n\text{ 无关的小量）}.
$$

这由极大不等式（maximal inequality，例如 Ottaviani 不等式或 Kolmogorov 型不等式）给出：对增量的四阶矩（或二阶矩加截断）作估计，得到 $\delta\to0$ 时上确界概率可以任意小。

**3. 识别极限。** 由 1、2 及 Prokhorov 定理，$S_n$ 有弱收敛子列，且极限过程的高斯性与有限维分布由步骤 1 完全确定，故极限必为布朗运动（教科书中"有限维分布相同 + 连续轨道"唯一确定法则，或直接用 $\mathcal C[0,1]$ 上的 Prokhorov 度量与有限维分布的唯一性）。因此整个序列弱收敛到 $B$。

**4. 泛函的分布收敛。** 若 $\Phi:\mathcal C[0,1]\to\mathbb R$ 连续（对一致范数），由连续映射定理 $\Phi(S_n)\Rightarrow\Phi(B)$；对经验过程版本，取 $\Phi(\alpha)=\sup_t|\alpha(t)|$ 得 Kolmogorov–Smirnov 统计量的极限分布（Kolmogorov 分布），取 $\Phi(\alpha)=\int\alpha^2\mathrm dF$ 得 Cramér–von Mises 统计量的极限分布。

## 三、定理的严格表述

**（Donsker 定理，部分和形式）** 设 $X_1,X_2,\dots$ 独立同分布，$\mathbb E X_1=0$、$\operatorname{Var}X_1=1$。定义 $S_0=0$、$S_k=X_1+\cdots+X_k$，并由

$$
S_n(t)=\frac{1}{\sqrt n}\Bigl(S_{\lfloor nt\rfloor}+(nt-\lfloor nt\rfloor)X_{\lfloor nt\rfloor+1}\Bigr),\qquad 0\le t\le1
$$

（线性插值）定义随机元 $S_n\in\mathcal C[0,1]$。则

$$
S_n\ \Longrightarrow\ B\quad\text{在 }\mathcal C[0,1]\text{ 中（配一致范数 }\|\cdot\|_\infty\text{）},
$$

其中 $B$ 是标准布朗运动。特别地，对任意连续泛函 $\Phi:\mathcal C[0,1]\to\mathbb R$，$\Phi(S_n)\Rightarrow\Phi(B)$。

**（经验过程形式 / Donsker 定理）** 设 $X_1,X_2,\dots$ 独立同分布，分布函数 $F$，经验分布函数 $F_n(t)=\frac1n\sum_{i=1}^n\mathbf 1_{\{X_i\le t\}}$。设 $\mathcal F$ 是由 $F$ 生成的 Donsker 类（例如 $F$ 连续时，$\mathcal F=\{1_{(-\infty,t]}:t\in\mathbb R\}$ 即为其一例）。则经验过程

$$
\alpha_n(t)=\sqrt n\bigl(F_n(t)-F(t)\bigr)
$$

作为 $\ell^\infty(\mathbb R)$ 中的随机元，弱收敛于布朗桥复合：

$$
\alpha_n\ \Longrightarrow\ \mathbb G\circ F,\qquad \mathbb G\ \text{为标准布朗桥（}\mathbb G(t)=B(t)-tB(1)\text{）}.
$$

**（推论：Kolmogorov–Smirnov 统计量）** 若 $F$ 连续，则

$$
D_n=\sup_{t\in\mathbb R}\bigl|F_n(t)-F(t)\bigr|\ \Longrightarrow\ \sup_{0\le u\le1}|\mathbb G(u)|,
$$

右端的分布就是 Kolmogorov 分布 $K(x)=1-2\sum_{k\ge1}(-1)^{k-1}\mathrm e^{-2k^2x^2}$。

**（推论：Cramér–von Mises 统计量）** 若 $F$ 连续，则 $n\int(F_n-F)^2\,\mathrm dF\Rightarrow\int_0^1\mathbb G(u)^2\,\mathrm du$，其分布由 Kac–Siegert 型级数给出。

**（推论：Cramér–Wold 到连续映射）** 上述泛函形式的收敛，是"把统计量的渐近分布化归为布朗桥/布朗运动泛函分布"的通用机制；只要统计量是经验过程的连续泛函，其极限分布即为对应布朗桥泛函的分布。

## 四、证明过程

**步骤 1：有限维分布收敛。**

固定 $0\le t_1<\cdots<t_d\le1$。由于 $\lfloor nt\rfloor/n\to t$，且 $X_k$ 均值 $0$、方差 $1$，经典中心极限定理给出

$$
\frac{S_{\lfloor nt\rfloor}}{\sqrt n}=\frac{1}{\sqrt n}\sum_{k\le\lfloor nt\rfloor}X_k\ \Longrightarrow\ N(0,t)
$$

（对 $t>0$；$t=0$ 时退化为 $0$）。更一般地，任一线性组合 $\sum_{j=1}^d a_j S_n(t_j)$ 可写成 $\frac{1}{\sqrt n}\sum_k c_kX_k+o_P(1)$，其方差收敛到 $\sum_{j,j'}a_ja_{j'}\min(t_j,t_{j'})$，故由 Cramér–Wold 定理

$$
\bigl(S_n(t_1),\dots,S_n(t_d)\bigr)\ \Longrightarrow\ \bigl(B(t_1),\dots,B(t_d)\bigr),
$$

即有限维分布收敛到布朗运动的对应分布（布朗运动的协方差 $\mathbb E B(s)B(t)=\min(s,t)$，见[Brown运动的存在性](./Brown运动的存在性.md)）。

**步骤 2：胎紧性（增量估计）。**

由 Arzelà–Ascoli 定理，$\mathcal C[0,1]$ 的紧集由一致有界与等度连续刻画。为得胎紧性，只需证

$$
\lim_{\delta\to0}\limsup_{n\to\infty}P\Bigl(\omega_{S_n}(\delta)\ge\eta\Bigr)=0,\qquad\forall\eta>0,
$$

其中 $\omega_{S_n}(\delta)=\sup_{|s-t|\le\delta}|S_n(s)-S_n(t)|$ 是连续模。用最大不等式：对 $X_k$ 作截断 $Y_k=X_k\mathbf 1_{\{|X_k|\le M\sqrt n\}}$ 并控制尾概率（由 $\mathbb E X_1^2<\infty$ 保证截断误差可任意小），再对截断增量用 Kolmogorov 型最大不等式

$$
P\Bigl(\max_{k\le m}\Bigl|\sum_{i\le k}Y_i-\frac km\sum_{i\le m}Y_i\Bigr|\ge\lambda\Bigr)\ \le\ \frac{C}{\lambda^2}\sum_{i\le m}\mathbb E Y_i^2 ,
$$

得到 $\mathbb E\bigl[\omega_{S_n}(\delta)^2\bigr]\le C\delta$（在归一化尺度下）型估计。由 Chebyshev 不等式与 $\delta\to0$，得上式成立，故 $\{S_n\}$ 胎紧。（等价地，若能验证 Petrov–Ottaviani 型条件 $P(|S_n(t+h)-S_n(t)|\ge\lambda)\le C\lambda^{-4}h^{2}$ 型界，可更快得到胎紧。）

**步骤 3：整体弱收敛。**

由步骤 1（有限维分布收敛）与步骤 2（胎紧），Prokhorov 定理给出：序列 $\{S_n\}$ 的每个子列都有弱收敛的进一步子列，且所有极限过程具有相同的有限维分布（由步骤 1）。在 $\mathcal C[0,1]$ 上，轨道连续的随机过程由其有限维分布唯一确定（取 $\mathbb Q\cap[0,1]$ 上的可数稠密子集，由连续性与 Kolmogorov 扩张定理拼出），故所有极限过程的法则都等于同一法则，即布朗运动的法则。于是

$$
S_n\ \Longrightarrow\ B\quad\text{于 }\mathcal C[0,1].
$$

**步骤 4：经验过程形式。**

设 $U_i=F(X_i)$，则 $U_i$ 独立同分布且服从 $\mathrm{Unif}[0,1]$（当 $F$ 连续；一般情形用分位数变换与技术性处理），且 $F_n(t)=\frac1n\sum_i\mathbf 1_{\{U_i\le F(t)\}}$。因此 $\alpha_n(t)=\sqrt n\bigl(\hat F_n(F(t))-F(t)\bigr)$，其中 $\hat F_n$ 是 $U_i$ 的经验分布函数。于是只需处理均匀分布情形。

对均匀分布，令 $G_n(u)=\sqrt n(\hat F_n(u)-u)$，$u\in[0,1]$。$\{G_n(u)\}$ 是"部分和过程"的连续化：$\hat F_n(u)$ 是计数过程，其增量由二项分布驱动，可用步骤 1–3 完全相同的论证（有限维 CLT + 最大不等式胎紧）得

$$
G_n\ \Longrightarrow\ \mathbb G\quad\text{于 }\ell^\infty[0,1],
$$

$\mathbb G$ 为标准布朗桥。这是因为有限维分布收敛到多元正态、协方差为 $\min(u,v)-uv$（恰为布朗桥的协方差），而胎紧性由二项增量的最大不等式（如 Bernstein 不等式 $\mathbb E\,$ 指数型界）给出。最后把 $u$ 换成 $F(t)$，即得 $\alpha_n=\sqrt n(\hat F_n(F(\cdot))-F(\cdot))\Rightarrow\mathbb G\circ F$：复合映射 $u\mapsto F(t)$ 单调连续，把 $[0,1]$ 上的一致收敛逐点拉回，由逐步刻画（a.s. 的 Skorokhod 表示 + 单调复合的连续性）完成。

由[Glivenko–Cantelli定理](./Glivenko-Cantelli定理.md)，$\sup_t|F_n(t)-F(t)|\to0$ a.s.，这保证了 $\alpha_n$ 的轨道在 $\ell^\infty$ 中可取（有界性），也是 Donsker 类条件 $\mathcal F$ 的最基本前提。

**步骤 5：连续泛函的分布（K–S 与 CvM）。**

由步骤 4 与连续映射定理（在 $\ell^\infty$ 上对一致范数连续的泛函）：

$$
\sup_t\bigl|\alpha_n(t)\bigr|\ \Longrightarrow\ \sup_{u\in[0,1]}\bigl|\mathbb G(u)\bigr|,\qquad
\int\alpha_n^2\,\mathrm dF\ \Longrightarrow\ \int_0^1\mathbb G(u)^2\,\mathrm du .
$$

第一个极限分布即 Kolmogorov 分布 $K(x)=1-2\sum_{k\ge1}(-1)^{k-1}\mathrm e^{-2k^2x^2}$（由布朗桥的反射原理与 $\sup|\mathbb G|$ 的分布公式得到），第二个即 Cramér–von Mises 极限分布。$\square$

## 五、应用与意义

**1. 非参数检验的分布无关性。** Kolmogorov–Smirnov 检验、Cramér–von Mises 检验、Anderson–Darling 检验的临界值都来自 Donsker 定理给出的布朗桥泛函分布；这使得检验表与样本分布的具体形状无关。

**2. 经验过程与统计学习。** 经验过程的弱收敛（Donsker 类、熵条件、Vapnik–Chervonenkis 理论）是经验风险最小化泛化界、$M$-估计与 bootstrap 理论的核心工具；Glivenko–Cantelli（大数定律）与 Donsker（中心极限）是这一套理论的两个支柱。

**3. Brown 桥与置信带。** K–S 型置信带、经验分位数过程的置信区间（Bahadur 表示）都建在布朗桥之上。

**4. 不变原理与随机游走应用。** 部分和形式的 Donsker 定理给出随机游走（排队系统、保险风险模型、随机游走极值）的重标度极限，是应用概率论中"用布朗运动替代离散模型"的合法性依据。

**5. 推广。** 有多种方向的推广：相依数据的 Donsker 定理（混合序列、鞅差序列）、高维与函数型数据的 Donsker 定理、抽象 Donsker 定理（Dudley 的 $\ell^\infty$ 版本，用度量熵刻画 Donsker 类）、bootstrap 的 Donsker 定理（Efron 经验 bootstrap 在 $\ell^\infty$ 中收敛于同一布朗桥）。
