# Sperner定理

> **一句话大白话**：一个集合 $[n]$ 的"子集大家庭"里，最宽的"互不包含"的一族有多大？恰好是最中间那一层——大小为 $\lfloor n/2\rfloor$ 的全部子集，共 $\binom{n}{\lfloor n/2\rfloor}$ 个。
>
> **小例子**：$n=4$ 时最大反链是全部 $2$ 元子集，共 $\binom42=6$ 个；断言说任何一族两两互不包含的子集最多 $\le6$ 个，且这一层能达到该大小。

## 一、定理介绍

Sperner 定理刻画 $2^{[n]}$ 中最大反链的大小，是最经典的极值集合论结果。它由 LYM 不等式直接推出，也是许多包含/反链类极值问题的原型。

## 二、原理思路

核心是 **LYM 不等式**：对反链 $\mathcal{F}$，
$$
\sum_{A\in\mathcal{F}}\frac1{\binom{n}{|A|}}\le1.
$$
证明用双计数：遍历 $2^{[n]}$ 的所有极大链（对应 $n!$ 个排列），反链等价于任一条极大链至多含 $\mathcal{F}$ 中一个集合。$A$ 出现在 $|A|!(n-|A|)!$ 条极大链中，统计极大链被"占用"的总数 $\le n!$，两边除以 $n!$ 即得。因中间二项式系数最大，$\frac{|\mathcal{F}|}{\binom{n}{\lfloor n/2\rfloor}}\le1$。

## 三、定理的严格表述

（Sperner 定理）设 $[n]=\{1,\dots,n\}$。则 $2^{[n]}$（按包含偏序）中最大反链的大小为 $\binom{n}{\lfloor n/2\rfloor}$。

## 四、证明过程

**证：**

1. **极大链。** 每个排列 $\pi=(\pi_1,\dots,\pi_n)$ 给出极大链 $C_\pi=\{\{\pi_1\},\{\pi_1,\pi_2\},\dots,\{\pi_1,\dots,\pi_n\}\}$，$2^{[n]}$ 的极大链与 $n!$ 个排列一一对应。

2. **占用计数。** 集合 $A\in\mathcal{F}$ 出现在 $|A|!(n-|A|)!$ 条极大链中（$A$ 的元素先排、补集后排）。

3. **反链约束。** $\mathcal{F}$ 是反链，任一条极大链至多含 $\mathcal{F}$ 中一个集合，故 $\sum_{A\in\mathcal{F}}|A|!(n-|A|)!\le n!$。

4. **LYM。** 两边除以 $n!$：$\sum_{A\in\mathcal{F}}\frac1{\binom{n}{|A|}}\le1$。

5. **取最值。** $m=\lfloor n/2\rfloor$ 时 $\binom{n}{m}\ge\binom{n}{k}$ 对一切 $k$。故
   $$
   \frac{|\mathcal{F}|}{\binom{n}{m}}\le\sum_A\frac1{\binom{n}{|A|}}\le1\quad\Longrightarrow\quad|\mathcal{F}|\le\binom{n}{\lfloor n/2\rfloor}.
   $$

6. **紧性。** 取 $\mathcal{F}=\{A:|A|=\lfloor n/2\rfloor\}$（同层互不包含），大小为 $\binom{n}{\lfloor n/2\rfloor}$。$\square$

## 五、应用与意义

Sperner 定理确立了"中等层是最大反链"这一极值原则，是极值集合论（Erdős–Ko–Rado、Trace 不等式等）的范式。LYM 方法与双计数在射影几何的 Erdős–Moser 问题、组合优化的容量估计及排序算法（部分序的线性扩展计数）中都有广泛应用。