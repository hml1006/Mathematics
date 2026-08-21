# Rice 定理

> **一句话大白话**：只要你想判定的"程序行为性质"不是平凡的（即既不是所有程序都满足、也不是所有程序都不满足），那么"哪些程序有这样的性质"这个集合就一定是不可计算的——程序的任何非平凡行为性质都不可判定。
>
> **小例子**：下列集合都不可计算：$\{e:\varphi_e \text{ 是全函数}\}$、"$\varphi_e$ 是常数函数"、"$\varphi_e$ 的定义域无限"。它们都是程序的非平凡行为性质，Rice 定理一次性判了死刑。

## 一、定理介绍

> **前置依赖**：停机问题的不可判定性、多一归约（$m$-归约）、s-m-n定理、部分可计算函数的指标化（$\varphi_e$）、通用函数。

Rice 定理是无界递归论中最具洞察力的结论之一：程序的部分可计算函数性质，只要是"非平凡的"（性质对应的函数类 $\mathcal{C}$ 非空也非全体），则判定该性质的所有程序指标集合 $I(\mathcal{C})=\{e:\varphi_e\in\mathcal{C}\}$ 都不可计算。它把停机问题不可判定的结论推广到任一非平凡程序性质。

## 二、原理思路

证明通过把停机问题归约（$\le_m$）到 $I(\mathcal{C})$。取 $g\in\mathcal{C}$（非平凡类非空），不改失一般性假设 $f_\bot$（处处无定义）不在 $\mathcal{C}$。构造可计算 $f$：对输入 $x$，$f(x)$ 是对应"若 $\varphi_x(x)$ 停机则表现为 $g$，否则表现为 $f_\bot$"的函数指标。则 $x\in K\iff f(x)\in I(\mathcal{C})$，即 $K\le_m I(\mathcal{C})$，故 $I(\mathcal{C})$ 不可计算。

## 三、定理的严格表述

**定理（Rice 定理）**：设 $\mathcal{C}$ 是部分可计算函数的非平凡类（$\varnothing\subsetneq\mathcal{C}\subsetneq\{\text{全体部分可计算函数}\}$）。则 $I(\mathcal{C})=\{e\mid \varphi_e\in\mathcal{C}\}$ 是不可计算的。

## 四、证明过程

**证明（通过停机问题的归约）**：

设 $\mathcal{C}$ 非平凡，不失一般性假设 $f_\bot\notin\mathcal{C}$（否则考虑补类）。因 $\mathcal{C}$ 非空，取 $g\in\mathcal{C}$，索引记为 $e_g$。

证 $K\le_m I(\mathcal{C})$。对输入 $x$，定义可计算函数 $f$ 使 $f(x)$ 是如下函数的索引：
$$
\varphi_{f(x)}(y)\simeq\begin{cases}
g(y), & \varphi_x(x)\downarrow,\\
\uparrow, & \varphi_x(x)\uparrow.
\end{cases}
$$
即 $\varphi_{f(x)}$ 模拟 $\varphi_x(x)$：若停机则运行 $g(y)$，否则永不停机。

**验证**：
- 若 $x\in K$，则 $\varphi_x(x)\downarrow$，$\varphi_{f(x)}=g\in\mathcal{C}$，故 $f(x)\in I(\mathcal{C})$。
- 若 $x\notin K$，则 $\varphi_x(x)\uparrow$，$\varphi_{f(x)}=f_\bot\notin\mathcal{C}$，故 $f(x)\notin I(\mathcal{C})$。

故 $x\in K\iff f(x)\in I(\mathcal{C})$，即 $K\le_m I(\mathcal{C})$。由 $K$ 不可计算，$I(\mathcal{C})$ 不可计算。$\square$

## 五、应用与意义

Rice 定理为"绝大多数程序性质不可判定"提供了统一依据：终止性、全函数性、常数性、定义域构造、与某函数相等与否等均不可判定。它也刻画了不可判定性的"索引-语义"界限——任何仅由函数行为（而非语法）定义的非平凡性质都超出可计算判定范围。这深刻影响编译器优化、程序分析与形式验证领域对"能/不能自动判定"的认知。