# Plünnecke 不等式

> **一句话大白话**：若 $A$ 加一个小集 $B$ 规模只膨胀了 $K$ 倍（$|A+B|\le K|A|$），则任何 $m,n$ 次的和差 $mB-nB$ 都能被同一常数 $K$ 的幂控制：$|mB-nB|\le K^{m+n}|A|$。"一次控制传到底"。
>
> **小例子**：若 $|A+B|\le2|A|$，则 $|2B|\le2^2|A|$、$|B-B|\le2^2|A|$ 等。加性结构在小和集下稳定保持。

## 一、定理介绍

> **前置依赖**：Plünnecke-Ruzsa 图、Plünnecke-Ruzsa 引理、Ruzsa 三角不等式、差集嵌入、数学归纳法原理。

Plünnecke（1970）用图论（Plünnecke-Ruzsa 图）提出并证明：$|A+B|\le K|A|$ 蕴含对一切 $m,n\ge0$ 有 $|mB-nB|\le K^{m+n}|A|$。这是小和集的结构性关键不等式，也是加性组合"增长论"的枢纽。

## 二、原理思路

用 Plünnecke-Ruzsa 层状图：顶点为各层 $A+jB$，边为 $x\to x+b$（$b\in B$）。核心引理是：存在 $X\subseteq A$ 使对一切 $j$，$|X+jB|\le K^j|X|$（$X$ 是最"抗胀"子集）。再结合 Ruzsa 三角不等式与差集嵌入，把 $|mB-nB|$ 用 $|X+jB|$ 表示并导出 $K^{m+n}$ 界。

## 三、定理的严格表述

设 $A,B$ 是阿贝尔群的有限子集，$|A+B|\le K|A|$。则对任何非负整数 $m,n$：
$$|mB-nB|\le K^{m+n}|A|,$$
其中 $mB=B+\cdots+B$（$m$ 次），$mB-nB$ 为差集。

## 四、证明过程

**证明（Plünnecke-Ruzsa 方法，概要）：**

**步骤 1：约化。** 因 $mB-nB\subseteq(m+n)B$ 方向嵌入，只需证明关键的增长引理与 $|mB-nB|$ 控制（对称处理 $m=n$）。$\blacksquare$

**步骤 2：Plünnecke 图。** 有向图 $G=(V,E)$，$V=\bigcup_{j\ge0}(A+jB)$，边 $x\to x+b$（$b\in B$），第 $j$ 层为 $A+jB$。$\blacksquare$

**步骤 3：层层控制。** 由 $|A+B|\le K|A|$，经 Plünnecke-Ruzsa 引理存在 $X\subseteq A$ 使对每个 $j\ge0$：$|X+jB|\le K^j|X|$。$\blacksquare$

**步骤 4：差集嵌入。** 用归纳 + Ruzsa 把 $|mB-nB|$ 化为 $|X+jB|$ 型，或直接用扩张引理的归纳证明：设 $A'$ 非空且 $|A'+jB|\le K^j|A'|$ 对 $j=0,1$ 成立，可归纳传至所有 $j$。$\blacksquare$

**步骤 5：得到上界。** 结合步骤 3 与对 $n$ 的对称处理（或再嵌差集），最终 $|mB-nB|\le K^{m+n}|A'|\le K^{m+n}|A|$。$\square$

**注：** 精确证明需 Plünnecke 图的 combinatorial lemma（对任意满足边条件的层状图存在"准平方儿"子族流）与归纳；此处为核心结构与概流程。

## 五、应用与意义

Plünnecke 不等式是小和集理论的核心，直接导出加性结构中"多步和集不易膨胀"的结果，是 Freiman 定理、sum-product 定理与和扌和差分增长研究所依赖的支柱。它连接 Plünnecke-Petridis（Petridis 新证明含完全精确）、Minkowski 与调和分析，是现代 additive combinatorics 与 arithmetic combinatorics 里最被熟练运用的不等式，也在 additive number theory 的稀疏结构估计 (如 multisets, Bourgain 方法) 中起到引擎作用。

## 课堂问答

**老师**：若 $A$ 加一个小集 $B$ 只膨胀 $K$ 倍，能推多远？

**学生**：$|A+B|\le K|A|$ 蕴含对任意 $m,n\ge 0$ 有 $|mB-nB|\le K^{m+n}|A|$。这用 Plünnecke–Ruzsa 层状图：顶点分层为 $A+jB$，边 $x\to x+b$（$b\in B$）；核心引理是存在"最抗胀"子集 $X\subseteq A$ 使 $|X+jB|\le K^j|X|$ 对所有 $j$ 成立，再用差集嵌入与 Ruzsa 三角把 $|mB-nB|$ 用 $|X+jB|$ 表示，导出 $K^{m+n}$ 界。

**老师（追问）**：为什么能一次控制"传到底"？

**学生**：因为层状图的膨胀是"每加一层 $B$ 至多乘 $K$"，增长引理保证存在一个子集把一次增长固化为所有层的界；再由差集嵌入把它接到 $mB-nB$。误区：常数指数写成 $K^{m+n-1}$ 之类，正确的是 $K^{m+n}$（$m=n=0$ 时即 $1$）。

**老师（拓展）**：它与前面那条引理是什么关系？

**学生**：Plünnecke 不等式与 Ruzsa 三角不等式合起来就是 Plünnecke–Ruzsa 引理；它体现"每加一个小集合的成本恰是因子 $K$"，是 Freiman 定理与和集增长论的核心引擎。注意它对非阿贝尔群不成立，需 Petridis 版本。
