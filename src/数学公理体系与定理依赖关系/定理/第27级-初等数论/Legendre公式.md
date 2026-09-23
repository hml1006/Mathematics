# Legendre 公式

> **一句话大白话**：想知道素数 $p$ 在 $n!$ 里"埋"了多少个因子，就数 $1$ 到 $n$ 中有多少个数是 $p$ 的倍数、多少个数是 $p^2$ 的倍数、多少个数是 $p^3$ 的倍数……层层加起来。

> **小例子**：取 $n=10$、$p=3$，则 $\lfloor10/3\rfloor+\lfloor10/9\rfloor=3+1=4$；确实 $10!=3628800=2^8\cdot3^4\cdot5^2\cdot7$，$3$ 的指数是 $4$。

## 介绍

Legendre 公式（Legendre's formula）给出阶乘 $n!$ 的素因子分解中任一素数 $p$ 的指数：$\nu_p(n!)=\sum_{k\ge1}\lfloor n/p^k\rfloor$，由 Legendre 于 1808 年提出。它是初等数论中处理"阶乘的整除性"的标准工具。

公式的直接用途包括：判定二项式系数的整性并估计其素因子指数、给出素数计数函数的初等上下界（Bertrand 素数定理的 Erdős 初等证明就使用它）、计算 $n!$ 末尾零的个数（即 $\nu_5(n!)$ 的情形）、以及 $p$ 进赋值 $\nu_p$ 在各种组合恒等式中的运算。它也是 $p$ 进分析中"取值于整数环的赋值"的最基本算法。

## 分析

**前置依赖**：带余除法、算术基本定理、数学归纳法原理。

**定理内容**：设 $p$ 是素数，$n$ 是正整数，$\nu_p(m)$ 表示正整数 $m$ 的素因子分解中 $p$ 的指数。则

$$\nu_p(n!)=\sum_{k=1}^{\infty}\Big\lfloor\frac{n}{p^k}\Big\rfloor,$$

其中只有有限项非零（当 $p^k>n$ 时 $\lfloor n/p^k\rfloor=0$，故右边是有限和）。

**推论（二项式系数）**：由 $\nu_p$ 的可加性，

$$\nu_p\binom{n}{m}=\sum_{k\ge1}\Big(\Big\lfloor\frac{n}{p^k}\Big\rfloor-\Big\lfloor\frac{m}{p^k}\Big\rfloor-\Big\lfloor\frac{n-m}{p^k}\Big\rfloor\Big)\ge0 .$$

特别地 $\nu_p\binom{2n}{n}=\sum_{k\ge1}\big(\lfloor2n/p^k\rfloor-2\lfloor n/p^k\rfloor\big)$，且对任意实数 $y$ 有 $2y-2\lfloor y\rfloor\in\{0,1\}$，故每个求和项只取 $0$ 或 $1$。

**意义**：$\nu_p(n!)$ 是 $1,\dots,n$ 中所有整数所含 $p$ 的"总个数"；而 $\lfloor n/p^k\rfloor$ 恰是被 $p^k$ 整除的数的个数。按"被 $p$ 的几次幂整除"分层计数再求和，就是公式的全部内容。

## 思考过程

同一件事有两种看法，得到同一个式子。

第一种是"逐个数计数"：每个整数 $m\le n$ 都贡献指数 $\nu_p(m)$，而 $\nu_p(m)$ 等于满足 $p^k\mid m$ 的 $k\ge1$ 的个数，因为 $m$ 的素因子分解里 $p$ 出现 $\nu_p(m)$ 次时，$p^1,\dots,p^{\nu_p(m)}$ 恰好都整除 $m$。于是

$$\nu_p(n!)=\sum_{m=1}^{n}\#\{k\ge1:\ p^k\mid m\}=\sum_{k\ge1}\#\{m\le n:\ p^k\mid m\},$$

交换求和次序（有限项，合法）；而由带余除法，$1,\dots,n$ 中 $p^k$ 的倍数恰有 $\lfloor n/p^k\rfloor$ 个。把各层计数相加即得公式。

第二种是"逐层剥因子"：设 $n=qp+r$（$0\le r<p$）。$1,\dots,n$ 中 $p$ 的倍数有 $q$ 个，每个至少提供一个 $p$；把它们的因子 $p$ 全部剥掉，剩下的部分总和恰好是 $q!$ 的因子结构贡献，于是 $\nu_p(n!)=q+\nu_p(q!)$。把它写成递推并对 $\lfloor n/p\rfloor$ 归纳展开，即得 $\lfloor n/p\rfloor+\lfloor n/p^2\rfloor+\cdots$。

## 证明过程

**步骤 1：$\nu_p$ 的刻画与可加性。** 由算术基本定理，每个正整数 $m$ 唯一地写为 $m=\prod_{p}p^{\nu_p(m)}$，且 $\nu_p(ab)=\nu_p(a)+\nu_p(b)$。由此立得

$$p^k\mid m\iff k\le\nu_p(m),\qquad\text{故}\qquad \nu_p(m)=\#\{k\ge1:\ p^k\mid m\}.$$

（乘性关系：$m$ 被 $p^k$ 整除等价于分解式中 $p$ 的指数至少为 $k$。）

**步骤 2：交换求和次序。** 对 $m=1,\dots,n$ 求和并使用步骤 1：

$$\nu_p(n!)=\sum_{m=1}^{n}\nu_p(m)=\sum_{m=1}^{n}\sum_{k\ge1}\mathbf 1_{p^k\mid m}=\sum_{k\ge1}\sum_{m=1}^{n}\mathbf 1_{p^k\mid m}.$$

两个和式都只有有限项非零（外层当 $p^k>n$ 时内层为零），交换次序合法。

**步骤 3：数出 $p^k$ 的倍数。** 固定 $k\ge1$，由带余除法写 $n=qp^k+r$，其中 $q=\lfloor n/p^k\rfloor$、$0\le r<p^k$。区间 $1,\dots,n$ 中 $p^k$ 的倍数正是 $p^k,2p^k,\dots,qp^k$，共 $q$ 个，即

$$\#\{m\le n:\ p^k\mid m\}=\Big\lfloor\frac{n}{p^k}\Big\rfloor .$$

代回步骤 2 即得 $\nu_p(n!)=\sum_{k\ge1}\lfloor n/p^k\rfloor$。

**步骤 4：递推形式的证明（另一条路线）。** 设 $n=qp+r$（$0\le r<p$）。$1,\dots,n$ 中 $p$ 的倍数为 $p,2p,\dots,qp$，其余数不含因子 $p$，故

$$\nu_p(n!)=\sum_{i=1}^{q}\nu_p(ip)=q+\sum_{i=1}^{q}\nu_p(i)=\Big\lfloor\frac np\Big\rfloor+\nu_p\Big(\Big\lfloor\frac np\Big\rfloor!\Big).$$

对 $n$ 用数学归纳法（强归纳）：由于 $q=\lfloor n/p\rfloor<n$（$p\ge2$），归纳假设给出 $\nu_p(q!)=\sum_{j\ge1}\lfloor q/p^j\rfloor=\sum_{k\ge2}\lfloor n/p^k\rfloor$，代入即得公式，与步骤 3 一致。

**步骤 5：二项式系数推论。** 由 $\binom{n}{m}=\dfrac{n!}{m!\,(n-m)!}$ 与 $\nu_p$ 的可加性，

$$\nu_p\binom{n}{m}=\sum_{k\ge1}\Big(\Big\lfloor\frac{n}{p^k}\Big\rfloor-\Big\lfloor\frac{m}{p^k}\Big\rfloor-\Big\lfloor\frac{n-m}{p^k}\Big\rfloor\Big).$$

由不等式 $\lfloor x+y\rfloor\ge\lfloor x\rfloor+\lfloor y\rfloor$ 逐项取 $x=m/p^k$、$y=(n-m)/p^k$ 知每项非负，故右端 $\ge0$（这与"组合数是整数"相容）。取 $m=n$ 得 $\nu_p\binom{2n}{n}=\sum_{k\ge1}(\lfloor2n/p^k\rfloor-2\lfloor n/p^k\rfloor)$；而 $2y-2\lfloor y\rfloor\in\{0,1\}$ 对任意实数 $y$ 成立，故每一项为 $0$ 或 $1$——这正是"$\binom{2n}{n}$ 的素因子指数都很小"，是 Bertrand 素数定理初等证明的关键性质。

**步骤 6：应用举例。** $n!$ 的十进制末尾零的个数等于 $\min(\nu_2(n!),\nu_5(n!))=\nu_5(n!)=\sum_{k\ge1}\lfloor n/5^k\rfloor$（因为 $\nu_5\le\nu_2$）。例如 $n=100$ 时 $\lfloor100/5\rfloor+\lfloor100/25\rfloor=20+4=24$。

## 相关条目

- [Bertrand素数定理](./Bertrand素数定理.md)：其 Erdős 初等证明用本公式控制 $\binom{2n}{n}$ 的素因子指数。
- [算术基本定理](./算术基本定理.md)：公式的表述与证明都以唯一分解为基础。
- [欧拉函数公式](./欧拉函数公式.md)：同为由素因子分解给出的算术函数显式公式。
