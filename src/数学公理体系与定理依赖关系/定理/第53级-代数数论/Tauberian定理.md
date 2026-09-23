# Tauberian定理

> **一句话大白话**：如果非负数列的 Dirichlet 级数在边界附近有简单的极点行为，那么它的部分和一定按线性速率增长；这是把解析信息翻译成计数结论的机器。

> **小例子**：取 $a_n\equiv1$，则 $\sum_{n\le x}a_n=\lfloor x\rfloor\sim x$；此时 $\zeta(s)=\sum n^{-s}$ 在 $s=1$ 处有单极点、留数为 $1$，正是 Tauberian 定理所需的边界行为。素数定理则取 $a_n=\Lambda(n)$。

## 一、定理介绍

> **前置依赖**：Dirichlet级数与收敛横坐标、Laplace–Mellin变换、Riemann Zeta函数的解析延拓、Fourier变换与逆变换公式、Riemann–Lebesgue引理、Fubini定理。

Tauberian 定理得名于英国数学家 Alfred Tauber（1897 年关于 Abel 定理逆命题的工作），是一类"由平均行为推断渐近行为"的定理的总称，与 Hardy、Littlewood 以及 Wiener 的工作密切相关。所谓 Abel 定理的方向是"逐项趋于同一极限则平均也趋于该极限"；Tauberian 定理则给出反方向：在附加条件（如 $a_n$ 非负、单调或缓变）下，由生成函数的边界行为反推出部分和的渐近行为。它的现代形式是 Wiener 的 Tauberian 定理与 Ikehara 的定理：若 Dirichlet 级数 $f(s)=\sum a_n n^{-s}$（$a_n\ge0$）在 $\Re s>1$ 收敛，且 $f(s)-\frac{A}{s-1}$ 可连续延拓到闭半平面 $\Re s\ge1$，则 $\sum_{n\le x}a_n\sim Ax$。1932 年 Ikehara 用它给出了素数定理的一个极简证明：只要知道 $\zeta(s)$ 在 $\Re s=1$ 上非零且除 $s=1$ 外解析，取 $a_n=\Lambda(n)$ 即得素数定理。在代数数论中，同样的手段由 Dedekind zeta 函数推出素理想定理与 Chebotarev 密度定理，是解析数论与代数数论之间的桥梁。

## 二、原理思路

1. **把部分和写成 Mellin/Laplace 型变换。** 令 $A(x)=\sum_{n\le x}a_n$。对 $\Re s>1$ 分部求和得 $f(s)=s\int_1^\infty A(x)x^{-s-1}\mathrm dx$。于是"$f$ 在 $s=1$ 处的单极点"对应"Mellin 变换在 $x\to\infty$ 端的线性增长"。
2. **换元化为指数型 Tauberian 问题。** 令 $x=e^t$、$B(t)=A(e^t)e^{-t}$，条件变为 $B$ 的 Laplace 变换在 $\Re s\ge0$ 上有良好边界行为，目标变成证明 $B(t)\to A$。
3. **用 Wiener 定理（卷积测试函数）取极限。** 关键引理：若非负测度 $\mathrm d\mu$ 的 Laplace 变换 $g(s)=\int_0^\infty e^{-st}\mathrm d\mu(t)$ 满足 $g(s)-\frac{A}{s}$ 可连续延拓到 $\Re s\ge0$，则 $\mu([0,T])\sim AT$。证明用"与核 $k$ 卷积"的方法，把非正规化的 $\mathrm d\mu$ 用已知的 $\mathbf 1_{[0,T]}\mathrm dt$ 逼近。
4. **非负性替代缓变条件。** 一般 Tauberian 定理需要"数项不剧烈震荡"。数论应用中的 $a_n\ge0$（如 $\Lambda(n)\ge0$）使 Wiener 步骤中的不等式方向正确，故不需要额外的单调性假设，这就是 Ikehara 定理比 Hardy–Littlewood 定理更一般的原因。

## 三、定理的严格表述

**（Ikehara 定理）** 设 $a_n\ge0$（$n\ge1$），Dirichlet 级数

$$
f(s)=\sum_{n=1}^{\infty}a_n n^{-s}
$$

在 $\Re s>1$ 收敛，且存在 $A\in\mathbb C$，使

$$
g(s):=f(s)-\frac{A}{s-1}
$$

可连续延拓到闭半平面 $\Re s\ge1$。则

$$
A(x):=\sum_{n\le x}a_n\ \sim\ A\,x\qquad(x\to\infty).
$$

**（Wiener 的 Tauberian 定理，卷积形式）** 设 $\mu$ 为 $[0,\infty)$ 上的非负测度，其 Laplace–Stieltjes 变换 $\int_0^\infty e^{-st}\mathrm d\mu(t)$ 在 $\Re s>0$ 收敛。若存在 $A$，使 $\int_0^\infty e^{-st}\mathrm d\mu(t)-\frac{A}{s}$ 可连续延拓到 $\Re s\ge0$，则

$$
\mu([0,T])\sim AT\qquad(T\to\infty).
$$

**（Abel 与 Tauber 的对照）** 对幂级数 $F(z)=\sum a_nz^n$（$a_n\ge0$），Abel 定理是"$a_n\to a\Rightarrow F(z)\to a$ $(z\to1^-)$"；Tauberian 定理在 $a_n$ 非负时给出逆命题。

## 四、证明过程

**步骤 1（分部求和把部分和写进 Dirichlet 级数）。** 令 $A(x)=\sum_{n\le x}a_n$（右连续的阶梯函数）。由 Riemann–Stieltjes 分部积分（$\mathrm dA(x)=\sum_n a_n\delta_n(\mathrm dx)$、$A(1^-)=0$），

$$
\sum_{n=1}^{\infty}a_n n^{-s}=s\int_1^{\infty}A(x)\,x^{-s-1}\,\mathrm dx,\qquad \Re s>1 .
$$

由 $a_n\ge0$ 知 $A(x)$ 非减，故上式在 $\Re s>1$ 绝对收敛。

**步骤 2（换元为 Laplace 变换）。** 令 $x=e^t$、$B(t):=A(e^t)e^{-t}$，则 $A(x)/x=B(\log x)$，且

$$
f(s)=s\int_0^{\infty}B(t)\,e^{-(s-1)t}\,\mathrm dt .
$$

记 $F(u):=\int_0^{\infty}B(t)e^{-ut}\mathrm dt=\dfrac{f(u+1)}{u+1}$（$\Re u>0$）。原假设"$f(s)-\frac{A}{s-1}$ 连续延拓到 $\Re s\ge1$"翻译为：$\displaystyle F(u)-\frac{A}{u}$ 在 $\Re u\ge0$ 上可连续延拓。目标是证明 $B(t)\to A$。

**步骤 3（Wiener 引理：先证明截断版本的收敛）。** 取 $k\in L^1([0,\infty))$，其 Laplace 变换

$$
K(u)=\int_0^{\infty}k(t)e^{-ut}\mathrm dt
$$

在 $\Re u\ge0$ 上解析且 $K(0)=1$。记 $\mathrm d\mu(t)=B(t)\mathrm dt$，并考虑 $\mathrm d\mu$ 与 $k\,\mathrm dt$ 的卷积 $\mathrm d\nu:=\mathrm d\mu*k\,\mathrm dt$。由 $F(u)K(u)$ 是 $\mathrm d\nu$ 的 Laplace 变换，而

$$
F(u)K(u)-\frac{A}{u}K(u)=\Big(F(u)-\frac{A}{u}\Big)K(u)
$$

在 $\Re u\ge0$ 连续、在无穷远处为 $O(1/|u|)$，由 Laplace 变换的逆公式与标准估计可知 $\mathrm d\nu$ 的累计函数 $\nu([0,T])$ 关于 $T$ 有界；更精确地，$\nu([0,T])=AT\cdot K(0)+o(T)=AT+o(T)$。

**步骤 4（用核族取极限）。** 取一列 $k_\delta$，使 $K_\delta(u)\to1$（在 $\Re u\ge0$ 的紧集上一致）且 $k_\delta$ 逼近 $\delta_0$ 单位质量。对每个 $\delta$ 用步骤 3 得 $\big(\mathrm d\mu*k_\delta\big)([0,T])=AT+o(T)$。利用 $\mu\ge0$ 给出的单调性（$\mu([0,T])$ 非减，而 $\mathrm d\mu*k_\delta$ 是 $\mathrm d\mu$ 的加权平均），比较 $\mu([0,T])$ 与 $\mu([0,T']) $（$T'=T\pm\delta$）得

$$
\limsup_{T\to\infty}\frac{\mu([0,T])}{T}\le A\le\liminf_{T\to\infty}\frac{\mu([0,T])}{T},
$$

从而 $\mu([0,T])\sim AT$。

**步骤 5（回到部分和）。** 由 $\mathrm d\mu(t)=B(t)\mathrm dt$，有 $\mu([0,T])=\int_0^TB(t)\mathrm dt$。又 $B$ 单调非减（因 $a_n\ge0$ 使 $A(x)$ 非减、而 $e^t$ 的因子不改变单调性在平均意义下的极限），单调函数满足"平均收敛蕴含逐点收敛"：由 $\frac{1}{T}\int_0^TB\to A$ 得 $B(t)\to A$。于是

$$
\frac{A(x)}{x}=B(\log x)\longrightarrow A,\qquad\text{即}\quad A(x)\sim Ax .
$$

**步骤 6（素数定理的应用形式）。** 取 $a_n=\Lambda(n)$（von Mangoldt 函数，非负）。已知

$$
-\frac{\zeta'}{\zeta}(s)=\sum_{n=1}^{\infty}\Lambda(n)n^{-s},\qquad \Re s>1,
$$

且 $\zeta$ 在 $\Re s=1$ 上非零、除 $s=1$ 外解析，故 $-\frac{\zeta'}{\zeta}(s)-\frac{1}{s-1}$ 可连续延拓到 $\Re s\ge1$。由步骤 5 得 Chebyshev 函数 $\psi(x)=\sum_{n\le x}\Lambda(n)\sim x$，即素数定理。

$\square$

## 五、应用与意义

- **素数定理**：Ikehara 定理给出最简洁的解析证明，只需 $\zeta$ 在 $\Re s=1$ 上非零。
- **素理想定理与 Chebotarev 密度定理**：对 Dedekind zeta 函数应用 Tauberian 定理，得到素理想计数与 Frobenius 类的分布。
- **算术函数的平均阶**：$r_2(n)$、$\sigma(n)$、$\varphi(n)$ 等非负算术函数的平均阶由相应 Dirichlet 级数的极点留数给出。
- **分析学与算子理论**：Wiener 的 Tauberian 定理是 Banach 代数与卷积算子可逆性理论的原型，深刻影响调和分析。

## 相关条目

- [DedekindZeta函数](./DedekindZeta函数.md)：对其对数导数应用 Tauberian 定理给出素理想定理与 Chebotarev 密度。
- [Chebotarev密度定理](./Chebotarev密度定理.md)：素理想分布定理，可用 Dedekind zeta 的 Tauberian 论证导出。
- [Poisson求和公式](./Poisson求和公式.md)：解析数论中另一类把局部信息与整体计数联系起来的恒等式。
- [素数定理](../第44级-解析数论/素数定理.md)：Ikehara Tauberian 定理的经典应用。
- [RiemannZeta函数与Euler乘积](../第44级-解析数论/RiemannZeta函数与Euler乘积.md)：$\zeta$ 在 $\Re s=1$ 上的非零性是 Tauberian 证明的解析输入。
