# Tauber 定理

> **一句话大白话**：Tauber 定理是"Abel 极限的反向题"——通常由"部分和的极限"能推出"加权平均的极限"；Tauber 定理说，只要加上一条系数"不太大"的条件，反过来也成立：加权平均的极限能倒推出部分和的极限。

> **小例子**：$\sum_{n\ge0}(-1)^n x^n=\frac{1}{1+x}\to\frac12$（$x\to1^-$），但部分和 $1-1+1-\cdots$ 发散。Tauber 定理指出问题出在条件 $na_n\to0$ 不满足（这里 $|a_n|=1$）。若换成 $a_n=(-1)^n/n$，条件满足，则部分和收敛到同一极限。

## 一、定理介绍

> **前置依赖**：Abel 求和与幂级数、Taylor 级数与收敛半径、Dirichlet 级数、极限与上极限（概念）。

Tauber 定理（Tauberian theorems）是一类"反 Abel 型"定理的总称，由 Alfred Tauber 于 1897 年开启，经 Littlewood（1910）、Hardy–Littlewood、Karamata（1931）与 Wiener（1932）系统发展。Abel 定理是容易的方向：若级数 $\sum a_n$ 收敛到 $S$，则 $\sum a_nx^n\to S$（$x\to1^-$）。Tauber 定理给出反向结论所需的"附加条件"：例如若 $\sum a_nx^n\to S$ 且 $na_n\to0$，则 $\sum a_n$ 收敛到 $S$。提出它的动机是：加权求和的极限往往容易从解析函数得到，而数论真正关心的是不加权的部分和（如素数计数），因此需要一类能把"Abel 极限"升级为"普通极限"的定理。Tauber 理论因此成为解析数论、概率极限定理（Karamata 型）与泛函分析（Wiener 定理）的公共基础。

## 二、原理思路

1. Abelian 方向：由 $\sum a_nx^n$ 的收敛性与 $1-x^n\to0$，把部分和 $s_N$ 与幂级数值 $f(x)$ 作差。
2. Tauberian 方向：选取最优的 $x=x_N=e^{-1/N}$，使 $x_N^N=e^{-1}$ 与规模匹配；把 $f(x_N)-s_N$ 拆成"低阶项"与"尾项"，用 Tauber 条件 $na_n\to0$ 分别估计。低阶项用 $1-e^{-n/N}\le n/N$ 控制，尾项用 $|a_n|\le\epsilon/n$ 控制。
3. 对数论版本（Karamata）：对非负系数的 Dirichlet 级数，用单调性把"平均收敛"升级为"逐点收敛"，得到 $\sum_{n\le x}a_n\sim Ax$。

## 三、定理的严格表述

**（Littlewood–Hardy–Littlewood Tauber 定理）** 设实数列 $\{a_n\}_{n\ge0}$ 满足 $\sum_{n\ge0}a_nx^n\to S$（$x\to1^-$）且 Tauber 条件
$$
n\,a_n\longrightarrow 0\qquad(n\to\infty)
$$
（更弱地，只需 $a_n=O(1/n)$）。则级数 $\sum_{n\ge0}a_n$ 收敛且
$$
\sum_{n=0}^{\infty}a_n=S .
$$

**（Karamata 型，用于数论）** 设 $a_n\ge0$，且存在 $A>0$ 使当 $s\to1^+$ 时
$$
\sum_{n\ge1}a_nn^{-s}\sim\frac{A}{s-1}.
$$
则
$$
\sum_{n\le x}a_n\sim A\,x\qquad(x\to\infty).
$$

**（Wiener 型，一般形式）** 设 $\phi\in L^1(\mathbb{R})$ 且其傅里叶变换 $\hat\phi$ 处处不为零。若 $f$ 有界且 $f*\phi(x)\to A\int\phi$（$x\to\infty$），则对任意 $g\in L^1$ 有 $f*g(x)\to A\int g$。

## 四、证明过程

**证明（先证幂级数版本）：**

**步骤 1：Abel 方向（准备）。** 设 $\sigma_N=\sum_{n=0}^{N}a_n$、$f(x)=\sum_{n=0}^{\infty}a_nx^n$。对 $x\in(0,1)$，
$$
f(x)-\sigma_N=\sum_{n=0}^{N}a_n(x^n-1)-\sum_{n=N+1}^{\infty}a_nx^n .
$$
故
$$
|\sigma_N-f(x)|\le\Big|\sum_{n=0}^{N}a_n(1-x^n)\Big|+\Big|\sum_{n=N+1}^{\infty}a_nx^n\Big| .
$$

**步骤 2：选取 $x=x_N=e^{-1/N}$。** 令 $x_N=e^{-1/N}\to1^-$，由假设 $f(x_N)\to S$。只需证 $\sigma_N-f(x_N)\to0$。

**步骤 3：估计第一项（低阶项）。** 对 $0\le n\le N$，$1-x_N^{n}=1-e^{-n/N}\le\frac nN$。又由 Tauber 条件 $na_n\to0$，令 $M_N=\sup_{n\le N}|na_n|$，则 $M_N\to0$，且
$$
\Big|\sum_{n=0}^{N}a_n(1-x_N^n)\Big|\le\sum_{n=0}^{N}|a_n|\frac nN=\frac1N\sum_{n=0}^{N}|na_n|\le M_N\frac{N+1}{N}\longrightarrow0 .
$$

**步骤 4：估计第二项（尾项）。** 由 $na_n\to0$，对 $\epsilon>0$ 存在 $M$，使 $n\ge M$ 时 $|a_n|\le\epsilon/n$。取 $N\ge M$，则
$$
\Big|\sum_{n=N+1}^{\infty}a_nx_N^n\Big|\le\sum_{n=N+1}^{\infty}|a_n|e^{-n/N}
\le\epsilon\sum_{n=N+1}^{\infty}\frac1n e^{-n/N}\le\epsilon\int_{N}^{\infty}\frac{e^{-t/N}}{t}dt=\epsilon\int_1^{\infty}\frac{e^{-u}}{u}du\le C\epsilon .
$$
（对 $M\le n\le N$ 等有限项，由 $n>N$ 部分的连续性亦可并入估计；$C=\int_1^\infty e^{-u}u^{-1}du<\infty$。）

**步骤 5：合并。** 由步骤 3–4，$\limsup_{N\to\infty}|\sigma_N-f(x_N)|\le C\epsilon$，令 $\epsilon\to0$ 得 $\sigma_N-f(x_N)\to0$。故
$$
\sigma_N=f(x_N)+\big(\sigma_N-f(x_N)\big)\longrightarrow S+0=S .
$$
级数收敛到 $S$。$\square$

**Karamata 型证明概要：** 设 $A(x)=\sum_{n\le x}a_n$。由非负性与 Abel 求和，$f(s)=\sum a_nn^{-s}=s\int_1^\infty A(x)x^{-s-1}dx$；条件 $f(s)\sim\frac{A_0}{s-1}$ 说明 $s\int_1^\infty(A(x)/x-? )$ 的奇性为单极点。对任意 $0<\lambda<\mu<1$ 用 $A$ 单调性夹逼 $\frac{A(\lambda x)}{x}\le\frac{A(x)}{x}\le\frac{A(\mu x)}{x}$，再对两端用部分积分把 $f$ 的渐近代入并令 $\lambda,\mu\to1$，即得 $A(x)\sim A_0x$。这与 Ikehara–Wiener 定理的步骤 5 完全一致，其核心仍是"单调性把平均收敛升级为逐点收敛"。$\square$

## 五、应用与意义

- 它是素数定理、素数分布类结果的技术关键：解析函数在 $s=1$ 的奇性经 Tauber 定理转为部分和渐近。
- Karamata 型定理是概率论中重尾分布、正则变化与极限定理（如大偏差、更新定理）的基本工具。
- Wiener 的 Tauber 定理是现代调和分析与 Banach 代数方法的开端，其"傅里叶变换不消失"条件刻画了可 Tauber 化性。
- 在算法分析与组合渐近中，Tauber 型结论用于由生成函数奇性估计系数和。
- 它揭示了 Abel 求和与普通求和之间"差多少"的精确条件，是发散级数可和性理论的基石。

## 相关条目

- [Ikehara-Wiener Tauber 定理](./Ikehara-WienerTauber定理.md)：本定理在非负系数 Dirichlet 级数上的强力形式。
- [素数定理](./素数定理.md)：其最后一步正是调用 Tauber 型结论。
- [Dirichlet 算术级数定理](./Dirichlet算术级数定理.md)：对各特征 $L$-函数应用 Tauber 型结论得等分布。
- [Mellin 变换](./Mellin变换.md)：把部分和与解析函数联系起来的技术语言。
- [Dirichlet L 函数](../第44级-解析数论/DirichletL函数.md)：Tauber 型结论在算术级数中的另一应用场景。
- [素数定理（第44级-解析数论）](../第44级-解析数论/素数定理.md)：与本级条目为同一定理，含 Tauber 定理的另一处引用，可交叉参考。
