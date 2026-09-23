# 行列式的 Leibniz 公式

> **一句话大白话**：$n$ 阶行列式就是"从每行每列各取一个数相乘、乘上排列的符号，再把所有取法加起来"——一张写尽所有划法的总账。
>
> **小例子**：二阶时 $\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$，正是两个排列 $(1,2)$ 与 $(2,1)$ 各自带符号的乘积之和。

## 介绍

行列式的 Leibniz 公式用置换群把行列式写成显式求和：从每一行、每一列各取一个元素相乘，乘上该取法对应排列的符号，再对所有排列求和。它是行列式最本质的展开式，二阶、三阶行列式的对角线法则都是它的特例。

公式以戈特弗里德·莱布尼茨命名，他将行列式与置换的奇偶性联系起来。用现代语言说：行列式是"对列（或行）多重线性且交替"的函数，且把单位矩阵映为 $1$；Leibniz 公式正是这样一个函数，于是由唯一性它必等于行列式。

它使得行列式的许多代数性质（乘积定理、交替性、展开定理）都可以通过置换的符号运算直接证明，也是多重线性代数中"交替张量"概念的原型。

## 分析

**前置依赖**：置换与逆序数（排列的符号 $\operatorname{sgn}$）、行列式的公理化定义（对每行多重线性、交替、单位矩阵取 $1$）、置换群的群运算、$\mathbb S_n$ 的元素个数为 $n!$

**定理内容**：设 $A=(a_{ij})$ 为 $n\times n$ 矩阵，$\mathbb S_n$ 为 $n$ 元置换全体，$\operatorname{sgn}(\sigma)$ 为置换 $\sigma$ 的符号，则

$$
\det A=\sum_{\sigma\in\mathbb S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^n a_{i,\sigma(i)}
$$

**数学内涵**：
- 求和共 $n!$ 项，每项由"每行每列恰取一个元素"的一种取法构成。
- 置换 $\sigma$ 表示在第 $i$ 行取第 $\sigma(i)$ 列的元素。

## 思考过程

与其从公理出发逐项展开（那需要处理大量递归），不如反过来：先定义右端函数 $F(A)=\sum_\sigma\operatorname{sgn}(\sigma)\prod_i a_{i,\sigma(i)}$，再验证它满足行列式公理化定义的三条要求——对每一行线性、交换两行变号、$F(I)=1$。而"多重线性 + 交替 + 规范"的函数是唯一的，因此 $F$ 就是 $\det$。

验证三条性质都归结为置换符号的性质：对每一行线性，是因为每个乘积对每一行都是一次；交换两行时，把置换右乘一个对换，符号变号，从而整和变号。

## 证明过程

**步骤 1：定义 $F$。** 对 $n\times n$ 矩阵 $A$，令

$$
F(A)=\sum_{\sigma\in\mathbb S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^n a_{i,\sigma(i)}
$$

**步骤 2：对每一行线性。** 固定除第 $r$ 行外的所有元素，考察 $F$ 对第 $r$ 行的依赖。每一乘积 $\prod_i a_{i,\sigma(i)}$ 中恰含第 $r$ 行的一个元素 $a_{r,\sigma(r)}$，其余因子与第 $r$ 行无关。故每个乘积对第 $r$ 行是线性的，有限和也是线性的。因此 $F$ 对每一行线性。

**步骤 3：交替性。** 设 $A'$ 是把 $A$ 的第 $r$ 行与第 $s$ 行（$r<s$）交换后得到的矩阵，交换列标记号即在每一乘积中把 $a_{r,\sigma(r)}$ 与 $a_{s,\sigma(s)}$ 互换，等价于把求和指标 $\sigma$ 换成 $\tau=\sigma\circ(r\,s)$（$r\,s$ 表示对换），其中 $a_{i,\tau(i)}$ 恰为 $A'$ 中第 $i$ 行第 $\tau(i)$ 列的元素。因 $\operatorname{sgn}(\tau)=\operatorname{sgn}(\sigma\circ(r\,s))=-\operatorname{sgn}(\sigma)$，且 $\sigma\mapsto\sigma\circ(r\,s)$ 是 $\mathbb S_n$ 上的双射，

$$
F(A')=\sum_{\sigma}\operatorname{sgn}(\sigma)\prod_i a'_{i,\sigma(i)}=\sum_{\tau}\operatorname{sgn}(\tau\circ(r\,s))\prod_i a_{i,(\tau\circ(r\,s))(i)}
$$

令 $\sigma=\tau\circ(r\,s)$，则 $\operatorname{sgn}(\sigma)=-\operatorname{sgn}(\tau)$，故

$$
F(A')=-\sum_{\tau}\operatorname{sgn}(\tau)\prod_i a_{i,\tau(i)}=-F(A)
$$

于是 $F$ 交替。

**步骤 4：规范。** 取 $A=I$，则 $a_{i,\sigma(i)}=\delta_{i,\sigma(i)}$，乘积 $\prod_i\delta_{i,\sigma(i)}$ 仅当 $\sigma=\mathrm{id}$ 时为 $1$，否则为 $0$。故

$$
F(I)=\operatorname{sgn}(\mathrm{id})\cdot 1=1
$$

**步骤 5：唯一性。** 由行列式的基本定理：若函数 $D$ 对每一行多重线性且交替，则 $D(A)=D(I)\det A$，即这样的函数由其在单位矩阵上的取值唯一确定。$F$ 满足前两条且 $F(I)=1$，而行列式 $\det$ 亦满足，故 $F=\det$，即 Leibniz 公式成立。$\square$

**补充（二阶验证）**：$n=2$ 时，$\mathbb S_2=\{\mathrm{id},(1\,2)\}$，$\operatorname{sgn}(\mathrm{id})=1$，$\operatorname{sgn}((1\,2))=-1$，故

$$
\det\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}=a_{11}a_{22}-a_{12}a_{21}
$$

与对角线法则一致。

## 相关条目

- [行列式的交替多重线性性](./行列式的交替多重线性性.md)：Leibniz 公式定义的函数正是交替多重线性函数的典型例子。
- [楔积的结合律](./楔积的结合律.md)：外代数的构造与 Leibniz 公式给出的行列式定义一脉相承。
