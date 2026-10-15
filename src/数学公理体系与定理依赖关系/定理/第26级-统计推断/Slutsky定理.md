# Slutsky 定理

> **一句话大白话**：一个"收敛到极限分布"的序列，与一个"收敛到常数"的序列作和、积、商，结果仍按连续映射的方式收敛到相应结果——随机分母可以放心换成常数。
>
> **小例子**：若 $X_n\xrightarrow{d}N(0,1)$ 且 $Y_n\xrightarrow{p}1$，则 $X_n/Y_n\xrightarrow{d}N(0,1)$，这正是用样本标准差替换总体标准差构造 $t$ 统计量的依据。

## 介绍

Slutsky 定理由苏联数学家 Evgeny Slutsky 于 1925 年提出，是概率极限理论中"拼装收敛"的基本工具。它使得我们只需分别知道某一部分的依分布极限与另一部分的依概率极限（且极限为常数），就能确定复合序列的极限分布。

这一定理在大样本统计中极其常用。$t$ 统计量、Wald 统计量、Delta 方法以及似然比的渐近分布，都需要在"分子依分布收敛、分母依概率收敛到常数"的场景下得出结论，Slutsky 定理正是把这两类收敛焊接起来的桥梁。

从技术上看，Slutsky 定理的核心事实是：当一部分的极限退化为常数时，各自的收敛会自动提升为联合收敛，从而可以自由使用连续性映射定理。

## 分析

**前置依赖**：依分布收敛、依概率收敛、连续映射定理、Lévy 连续性定理（特征函数刻画依分布收敛）、依分布收敛蕴含紧性

**定理内容**：设 $X_n\xrightarrow{d}X$，$Y_n\xrightarrow{p}c$，其中 $c$ 为常数。则

1. $X_n+Y_n\xrightarrow{d}X+c$；
2. $X_nY_n\xrightarrow{d}cX$；
3. 若 $c\ne0$，则 $X_n/Y_n\xrightarrow{d}X/c$。

更一般地，此时联合收敛成立：$(X_n,Y_n)\xrightarrow{d}(X,c)$。

**关键要点**：

- 结论只要求其中一个变量收敛到常数；若 $X_n\to_dX$、$Y_n\to_dY$ 而 $Y$ 非常数，则一般不能断言 $X_n+Y_n\to_dX+Y$（缺少联合收敛）；
- 证明的关键引理是"依分布收敛 + 依概率收敛到 $0$ 仍依分布收敛"；
- 乘积与商的情形通过把 $Y_n-c$（或 $1/Y_n-1/c$）视为依概率收敛到 $0$ 的扰动来处理。

## 思考过程

关键观察是：当一部分收敛到常数时，联合收敛自动成立。于是问题归结为两步。第一步，先建立引理：若 $X_n\xrightarrow{d}X$ 且 $W_n\xrightarrow{p}0$，则 $X_n+W_n\xrightarrow{d}X$。这一步用特征函数最方便，因为特征函数的模被 $W_n$ 的"小性"控制，而依概率收敛到 $0$ 恰好能逐点压住特征函数之差。

第二步，把和、积、商都改写成"主项 + 依概率到零的扰动"：和是 $X_n+(Y_n-c)+c$；积是 $cX_n+X_n(Y_n-c)$；商则用一个"截断"技巧把 $1/Y_n$ 在 $|Y_n|>\delta$ 上换成依概率收敛到 $1/c$ 的量。这样就都能套用引理或乘积结论，而不需要证明原序列的联合收敛。

## 证明过程

**引理**：若 $X_n\xrightarrow{d}X$ 且 $W_n\xrightarrow{p}0$，则 $X_n+W_n\xrightarrow{d}X$。

**引理的证明**：由 Lévy 连续性定理，只需证特征函数逐点收敛。对固定 $t\in\mathbb R$，

$$\big|\varphi_{X_n+W_n}(t)-\varphi_{X_n}(t)\big|=\big|\mathbb E\big[e^{itX_n}(e^{itW_n}-1)\big]\big|\le\mathbb E\big|e^{itW_n}-1\big|\le\mathbb E\big[\min(|t|\,|W_n|,\,2)\big].$$

对任意 $\delta>0$，把期望按事件 $\{|W_n|\le\delta\}$ 与 $\{|W_n|>\delta\}$ 拆开，得

$$\mathbb E\big[\min(|t|\,|W_n|,2)\big]\le|t|\delta+2\,\mathbb P(|W_n|>\delta).$$

由于 $W_n\xrightarrow{p}0$，$\limsup_n\mathbb E|e^{itW_n}-1|\le|t|\delta$；令 $\delta\downarrow0$ 得该上极限为 $0$。又 $\varphi_{X_n}(t)\to\varphi_X(t)$，故 $\varphi_{X_n+W_n}(t)\to\varphi_X(t)$，即 $X_n+W_n\xrightarrow{d}X$。$\blacksquare$

**步骤 1：证明 (1)。** 写 $X_n+Y_n=X_n+(Y_n-c)+c$。因 $Y_n\xrightarrow{p}c$，有 $W_n:=Y_n-c\xrightarrow{p}0$，由引理 $X_n+W_n\xrightarrow{d}X$。再由连续性映射定理（映射 $x\mapsto x+c$ 连续），$X_n+Y_n=(X_n+W_n)+c\xrightarrow{d}X+c$。

**步骤 2：扰动项依概率到零。** 先证 $X_n(Y_n-c)\xrightarrow{p}0$。由 $X_n\xrightarrow{d}X$ 知 $\{X_n\}$ 紧，故对任意 $\eta>0$ 存在 $M$ 使 $\sup_n\mathbb P(|X_n|>M)\le\eta$。对任意 $\epsilon>0$，

$$\mathbb P\big(|X_n(Y_n-c)|>\epsilon\big)\le\mathbb P(|X_n|>M)+\mathbb P\big(|Y_n-c|>\epsilon/M\big)\le\eta+\mathbb P\big(|Y_n-c|>\epsilon/M\big).$$

令 $n\to\infty$ 再由 $\eta$ 任意小，得 $X_n(Y_n-c)\xrightarrow{p}0$。

**步骤 3：证明 (2)。** 写 $X_nY_n=cX_n+X_n(Y_n-c)$。由连续性映射定理 $cX_n\xrightarrow{d}cX$；由步骤 2 扰动项依概率到零，故由引理 $X_nY_n\xrightarrow{d}cX$。

**步骤 4：证明 (3)。** 设 $c\ne0$，取 $\delta\in(0,|c|)$。因 $Y_n\xrightarrow{p}c$，有 $\mathbb P(|Y_n|>\delta)\to1$。定义

$$Z_n=\frac{1}{Y_n}\,\mathbf 1_{\{|Y_n|>\delta\}}.$$

则在 $\{|Y_n|>\delta\}$ 上 $Z_n=1/Y_n$，且由连续性映射定理（$y\mapsto1/y$ 在 $|y|>\delta$ 上连续）$Z_n\xrightarrow{p}1/c$。对任意有界连续函数 $f$，

$$\mathbb E\big[f(X_n/Y_n)\big]=\mathbb E\big[f(X_nZ_n)\mathbf 1_{\{|Y_n|>\delta\}}\big]+\mathbb E\big[f(X_n/Y_n)\mathbf 1_{\{|Y_n|\le\delta\}}\big],$$

末项被 $\|f\|_\infty\,\mathbb P(|Y_n|\le\delta)\to0$ 控制。对第一项应用 (2)（把 $Y_n$ 换成 $Z_n$、常数换成 $1/c$）得 $X_nZ_n\xrightarrow{d}X/c$。故对一切有界连续 $f$ 有 $\mathbb E[f(X_n/Y_n)]\to\mathbb E[f(X/c)]$，即 $X_n/Y_n\xrightarrow{d}X/c$。$\square$

**步骤 5：联合收敛（附注）。** 上述论证实际可强化：由上述引理配合特征函数

$$\varphi_{(X_n,Y_n)}(s,t)=\mathbb E\big[e^{isX_n+itY_n}\big]=\mathbb E\big[e^{isX_n}e^{it(Y_n-c)}\big]e^{itc}\xrightarrow[n\to\infty]{}\varphi_X(s)e^{itc},$$

即得 $(X_n,Y_n)\xrightarrow{d}(X,c)$（$\mathbb E[e^{isX_n}e^{it(Y_n-c)}]-\mathbb E[e^{isX_n}]\to0$ 的论证与引理相同）。

## 课堂问答

**老师**：Slutsky 定理在算什么？它为什么要求"其中一个的极限是常数"？

**学生**：结论：若 $X_n\xrightarrow{d}X$、$Y_n\xrightarrow{p}c$（$c$ 为常数），则 $X_n+Y_n\xrightarrow{d}X+c$、$X_nY_n\xrightarrow{d}cX$、且 $c\neq0$ 时 $X_n/Y_n\xrightarrow{d}X/c$。要求极限为常数，是为了让 $(X_n,Y_n)\xrightarrow{d}(X,c)$ 的联合收敛自动成立，从而能套用连续映射。

**老师（追问）**：关键引理"$X_n\xrightarrow{d}X$ 且 $W_n\xrightarrow{p}0\Rightarrow X_n+W_n\xrightarrow{d}X$"怎么证？和、积、商如何归约到它？

**学生**：用 Lévy 连续性定理看特征函数，$|\varphi_{X_n+W_n}(t)-\varphi_{X_n}(t)|\leq E\min(|t||W_n|,2)\leq|t|\delta+2P(|W_n|>\delta)$，先令 $n\to\infty$ 再令 $\delta\downarrow0$ 即为零。和：$X_n+Y_n=X_n+(Y_n-c)+c$；积：$X_nY_n=cX_n+X_n(Y_n-c)$，其中 $X_n(Y_n-c)\xrightarrow{p}0$（用 $\{X_n\}$ 的紧性）；商：取截断 $Z_n=\frac1{Y_n}\mathbf 1_{\{|Y_n|>\delta\}}$，把随机倒数换成依概率收敛到 $1/c$ 的量。

**老师（拓展）**：若 $X_n\xrightarrow{d}X$、$Y_n\xrightarrow{d}Y$ 而 $Y$ 非常数，$X_n+Y_n$ 还依分布收敛到 $X+Y$ 吗？

**学生**：一般不成立！缺的是联合收敛，$X_n$ 与 $Y_n$ 的依赖结构会破坏和的极限。反例：取 $X_n=Z$、$Y_n=-Z$（$Z\sim N(0,1)$），两者分别依分布收敛到 $N(0,1)$ 与 $-N(0,1)$，但 $X_n+Y_n=0$ 却"应当"收敛到 $N(0,2)$，矛盾。Slutsky 定理之所以在统计中频繁使用，正因为分母（如 $S/\sigma$）恰好依概率收敛到常数。

## 相关条目

- [Delta方法](./Delta方法.md)：其证明把 $\sqrt n(g(\hat\theta)-g(\theta))$ 的随机斜率换成常数，正是 Slutsky 定理的应用。
- [似然比检验渐近分布](./似然比检验渐近分布.md)：渐近正态性推导中同样用 Slutsky 定理处理随机分母。
