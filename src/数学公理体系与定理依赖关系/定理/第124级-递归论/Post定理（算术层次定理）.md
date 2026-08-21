# Post 定理（算术层次定理）

> **一句话大白话**：Post 定理把"算术层次"（$\Sigma^0_n,\Pi^0_n,\Delta^0_n$）与"相对计算的递归可枚举层"统一起来：升高一层恰好等同于"转到上一层的可枚举相对类"，并用 Turing 跳变刻画 $\Delta^0_n$。
>
> **小例子**：$\Delta^0_1$ 恰好是可计算集；$\Sigma^0_1$ 恰好是 c.e.（递归可枚举）集；$\Delta^0_2$ 恰好是在空集的跳变 $\varnothing'$ 下可计算的集。Post 定理把这些一一对上。

## 一、定理介绍

Post 定理（Post's Theorem）是递归论中连接**算术层次**与**Turing 归约/跳变**的桥梁。它以精确等价方式表明：$\Sigma^0_{n+1}$ 是某 $\Pi^0_n$ 集的可枚举投影；$\Delta^0_{n+1}$ 是相对于跳变 $\varnothing^{(n)}$ 可计算的集类；$\Sigma^0_{n+1}$ 是相对于 $\varnothing^{(n)}$ 的 c.e. 集类。它让层次与相对计算互相转化。

## 二、原理思路

$n=0$ 的基础步：$\Sigma^0_1$ 即"存在 $y$ 使可计算谓词成立"的集合，正好是 c.e. 集；$\Delta^0_1=\Sigma^0_1\cap\Pi^0_1$，一个集与其补都 c.e. 当且仅当可计算。对一般 $n$ 用归纳：把 $A\in\Sigma^0_{n+1}$ 化为 $\exists y\langle x,y\rangle\in B$（$B\in\Pi^0_n$），由归纳假设 $B\le_T\varnothing^{(n)}$，从而 $A$ 是相对于 $\varnothing^{(n)}$ 的可枚举集，再归约回 $\Sigma^0_{n+1}$。

## 三、定理的严格表述

**定理（Post 定理）**：

1. $A\in\Sigma^0_{n+1}$ 当且仅当 $A$ 是某个 $\Pi^0_n$ 集合的可枚举投影（$A=\{x:\exists y\,\langle x,y\rangle\in B\}$ 对某 $B\in\Pi^0_n$）。
2. $A\in\Delta^0_{n+1}$ 当且仅当 $A\le_T\varnothing^{(n)}$（$\varnothing^{(n)}$ 为空集的 $n$ 次 Turing 跳变）。
3. $\Sigma^0_{n+1}$ 恰好是相对于 $\varnothing^{(n)}$ 的 c.e. 集构成的类。

## 四、证明过程

**证明**：

**第一部分（$n=0$ 基础步）**：$A\in\Sigma^0_1$ 当且仅当存在可计算谓词 $R(x,y)$ 使 $A=\{x:\exists yR(x,y)\}$。（$\Rightarrow$）令 $B=\{\langle x,y\rangle:R(x,y)\}\in\Delta^0_0\subseteq\Pi^0_0$，则 $A$ 是 $B$ 的投影。（$\Leftarrow$）若 $A=\{x:\exists y\langle x,y\rangle\in B\}$ 且 $B\in\Pi^0_0=\Delta^0_0$ 由可计算 $R$ 定义，则 $A$ 由 $\exists yR(x,y)$ 定义，故 $A\in\Sigma^0_1$。

**第二部分（$n=0$）**：$A\in\Delta^0_1$ 当且仅当 $A$ 与 $\mathbb{N}\setminus A$ 都 c.e.，当且仅当 $A$ 可计算（即 $A\le_T\varnothing^{(0)}$）。

**一般 $n$ 的归纳**：假设定理对 $n$ 成立。$A\in\Sigma^0_{n+1}$ 当且仅当 $A=\{x:\exists y\langle x,y\rangle\in B\}$ 对某 $B\in\Pi^0_n$。由归纳假设 $B\le_T\varnothing^{(n)}$。故判定 $x\in A$ 等价于在 $\varnothing^{(n)}$ 下搜索 $y$，即 $A$ 是相对于 $\varnothing^{(n)}$ 的 c.e. 集。由 $n=0$ 的结果，相对于 $\varnothing^{(n)}$ 的 $\Sigma^0_1$ 类恰为 $\Sigma^0_{n+1}$。归纳完成。$\square$

**推论**：算术层次严格递增——对每个 $n$，$\Sigma^0_n\subsetneq\Sigma^0_{n+1}$ 且 $\Pi^0_n\subsetneq\Pi^0_{n+1}$。

## 五、应用与意义

Post 定理把"公式定义的复杂度"（算术层次）与"计算复杂度的相对级别"（Turing 跳变）统一刻画，是递归论中层次结构理论的核心。它用于构造恰好落在某层次（如 $\Sigma^0_2$ 非 $\Pi^0_2$）的集合、判断集合层次、以及说明 $\Delta^0_{n+1}$ 与跳变的关系，也为分析算术真值、不可判定性提供了精确定量工具。