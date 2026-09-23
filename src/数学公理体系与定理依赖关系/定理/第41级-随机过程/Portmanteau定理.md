# Portmanteau 定理

> **一句话大白话**：概率测度的弱收敛有好几种等价说法——对一切有界连续函数积分收敛、开集的测度下极限不等式、闭集的测度上极限不等式、以及对"边界为 null 集"的集合测度收敛——它们是同一件事的五张面孔。
>
> **小例子**：$\mu_n=\delta_{1/n}$ 在 $\mathbb R$ 上弱收敛到 $\delta_0$。开集 $(0,1)$ 满足 $\liminf\mu_n((0,1))=1\ge\mu((0,1))=0$；闭集 $\{0\}$ 满足 $\limsup\mu_n(\{0\})=0\le\mu(\{0\})=1$；而 $\{0\}$ 不是 $\mu$-连续集，因为它有 $\mu(\partial\{0\})=\mu(\{0\})=1>0$，故它的测度不收敛。

## 介绍

设 $S$ 是度量空间（典型情形：波兰空间），$\mu_n,\mu$ 是 $S$ 上的 Borel 概率测度。弱收敛（weak convergence，记作 $\mu_n\Rightarrow\mu$）的定义是

$$\int_S f\,d\mu_n\xrightarrow[n\to\infty]{}\int_S f\,d\mu\qquad\text{对一切 }f\in C_b(S),$$

即测度在连续有界函数上的"泛函"收敛。这个定义在证明中往往不好直接用：检验量 $C_b(S)$ 太大，而"测度本身"是集合函数，我们希望有一族**集合**形式的等价条件，最好还能把"开集/闭集"这种拓扑信息用上。

Portmanteau 定理（名字来自法语的"portemanteau"，衣帽架，取"把许多等价条件挂在一起"之意）正是这样一座桥梁。它把弱收敛翻译成五种彼此等价的陈述，其中包括开集的**下极限不等式**、闭集的**上极限不等式**，以及"测度在 $\mu$-连续集（边界测度为零的集合）上收敛"。

推论是极其有用的：证明一个序列弱收敛时，只需在最方便的版本下工作；证明紧性定理（Prokhorov）时，"$\nu\mapsto\nu(G)$ 对开集下半连续"这样的语句直接来自 (b)；而"连续集上测度收敛"是导出极限分布唯一性、Skorokhod 表示、以及各种极限定理的标准接口。

## 分析

**前置依赖**：弱收敛的定义（对 $C_b(S)$ 积分收敛）、Borel 测度的定义与 $\sigma$-可加性、单调收敛与控制收敛定理、单调类定理、集合边界 $\partial A=\overline{A}\setminus\mathring A$、距离函数 $x\mapsto d(x,A)$ 的连续性（Lipschitz）、度量空间中的 Urysohn 型构造。

**定理内容**：设 $(S,d)$ 是度量空间，$\mu_n,\mu$ 是其上的 Borel 概率测度。则以下六条彼此等价：

**(a)** $\mu_n\Rightarrow\mu$：对一切 $f\in C_b(S)$ 有 $\int f\,d\mu_n\to\int f\,d\mu$；

**(b)** 对一切开集 $G\subseteq S$ 有 $\displaystyle\liminf_{n\to\infty}\mu_n(G)\ge\mu(G)$；

**(c)** 对一切闭集 $F\subseteq S$ 有 $\displaystyle\limsup_{n\to\infty}\mu_n(F)\le\mu(F)$；

**(d)** 对一切满足 $\mu(\partial A)=0$ 的集合 $A$（称为 $\mu$-连续集）有 $\mu_n(A)\to\mu(A)$；

**(e)** 对一切有界一致连续函数 $f$ 有 $\int f\,d\mu_n\to\int f\,d\mu$；

**(f)** 对一切有界 Lipschitz 函数 $f$ 有 $\int f\,d\mu_n\to\int f\,d\mu$。

此外，(b) 蕴含对一切紧集 $K$ 有 $\limsup_n\mu_n(K)\le\mu(K)$（把 (c) 用在紧集上）。

**证明策略**：按 $(a)\Rightarrow(b)\Rightarrow(c)\Rightarrow(d)\Rightarrow(a)$ 闭合主循环，其中 $(a)\Rightarrow(b)$ 用开集的"内部逼近"构造一列递增到 $1_G$ 的有界连续函数；$(d)\Rightarrow(a)$ 用"阶梯函数夹逼"把连续函数夹在有限个 $\mu$-连续集上取常值的函数之间；$(a)\Rightarrow(e)\Rightarrow(f)$ 是包含关系；$(f)\Rightarrow(a)$（或 $(e)\Rightarrow(a)$）用函数型单调类定理：把"积分收敛"的函数集合看作一个含代数、对逐点有界单调极限封闭的向量空间。

## 思考过程

**为什么开集要用下极限而不是极限？** 因为弱收敛只控制连续函数，而 $1_G$ 不连续。把 $1_G$ 从**下方**用连续函数逼近是容易的：令 $f_k(x)=\min\big(1,\,k\cdot d(x,G^c)\big)$，它在 $G$ 内取 $1$、在 $G$ 外取 $0$ 的边界上连续地过渡，且 $k\to\infty$ 时 $f_k\uparrow 1_G$。于是 $\mu_n(G)\ge\int f_k\,d\mu_n\to\int f_k\,d\mu$，再让 $k\to\infty$ 用单调收敛即得 $\liminf\mu_n(G)\ge\mu(G)$。从**上方**逼近 $1_G$ 则做不到（$1_G$ 不是上半连续），这就是"下极限"的来源。闭集的情形完全对称：取补集即得。

**连续集条件为什么自然？** 令 $\mathring A$ 为内部、$\overline A$ 为闭包。对任意 $A$，

$$\mu(\mathring A)\le\liminf_n\mu_n(\mathring A)\le\liminf_n\mu_n(A)\le\limsup_n\mu_n(A)\le\limsup_n\mu_n(\overline A)\le\mu(\overline A).$$

当 $\mu(\partial A)=0$ 时 $\mu(\mathring A)=\mu(\overline A)=\mu(A)$，链条被两端夹死，$\mu_n(A)$ 被迫收敛。这解释了三明治结构的合理性；也说明缺少 $\mu(\partial A)=0$ 时确实可能不收敛（例如 $\mu_n=\delta_{1/n}$、$A=\{0\}$）。

**$(d)\Rightarrow(a)$ 的关键是把连续函数"离散化"**。给定 $f\in C_b(S)$，$0\le f\le M$，把值域 $[0,M]$ 切成一串区间。若分割点 $t_i$ 都满足 $\mu(f^{-1}\{t_i\})=0$，则每个 $A_i=f^{-1}((t_{i-1},t_i])$ 都是 $\mu$-连续集（因为对连续函数，$\partial f^{-1}((a,b])\subseteq f^{-1}\{a\}\cup f^{-1}\{b\}$）。这样 $f$ 就被两个在 $\mu$-连续集上取常值的阶梯函数 $g\le f\le h$ 夹住，而 $\int(h-g)d\mu$ 可以随分割变细而任意小。由 (d)，$\int g\,d\mu_n\to\int g\,d\mu$、$\int h\,d\mu_n\to\int h\,d\mu$，夹逼即得 $\int f\,d\mu_n\to\int f\,d\mu$。

**为什么 (e) 或 (f) 竟然也等价于 (a)？** 因为"一个函数族上的收敛"可以靠单调类定理传播。令 $\mathcal{C}$ 为所有使 $\int f\,d\mu_n\to\int f\,d\mu$ 成立的有界 Borel 函数 $f$ 的集合。它是一个向量空间，包含常数；若 (e) 成立，则它包含有界一致连续函数全体 $\mathcal{A}$，而 $\mathcal{A}$ 是含 $1$、对逐点乘积封闭的代数，且 $\sigma(\mathcal{A})=\mathcal{B}(S)$（因为每个开球可由 $d(\cdot,x_0)$ 这种一致连续函数描述）；又 $\mathcal{C}$ 对逐点有界单调极限封闭（控制收敛定理 + 一致估计）。由函数型单调类定理，$\mathcal{C}$ 含一切有界 Borel 函数，特别含 $C_b(S)$，即 (a)。这说明弱收敛可以被"任意足够丰富的函数族"检验。

## 证明过程

**(a) $\Rightarrow$ (b)。** 设 $G\subseteq S$ 开。记 $d(x,G^c)=\inf\{d(x,y):y\notin G\}$（若 $G^c=\varnothing$ 则约定 $d(x,G^c)=+\infty$）。对 $k\ge1$ 定义

$$f_k(x)=\min\big(1,\ k\,d(x,G^c)\big).$$

每个 $f_k$ 是 $1$-Lipschitz 函数的截断，故 $f_k\in C_b(S)$ 且 $0\le f_k\le1$。若 $x\in G$，则 $d(x,G^c)>0$，故 $f_k(x)=1$ 对充分大的 $k$ 成立；若 $x\notin G$，则 $d(x,G^c)=0$，故 $f_k(x)=0$。于是 $f_k\uparrow 1_G$。由 (a) 与 $f_k\le 1_G$，

$$\liminf_{n\to\infty}\mu_n(G)\ge\lim_{n\to\infty}\int f_k\,d\mu_n=\int f_k\,d\mu .$$

令 $k\to\infty$，由单调收敛定理 $\int f_k\,d\mu\uparrow\mu(G)$，故 $\liminf_n\mu_n(G)\ge\mu(G)$。

**(b) $\Leftrightarrow$ (c)。** 取补集：$F$ 闭等价于 $G=F^c$ 开，且 $\mu_n(F)=1-\mu_n(G)$、$\mu(F)=1-\mu(G)$。于是 $\limsup\mu_n(F)=1-\liminf\mu_n(G)\le1-\mu(G)=\mu(F)$，反向同理。

**(b), (c) $\Rightarrow$ (d)。** 设 $\mu(\partial A)=0$。由 (b) 用于开集 $\mathring A$ 与 (c) 用于闭集 $\overline A$，

$$\mu(\mathring A)\le\liminf_n\mu_n(\mathring A)\le\liminf_n\mu_n(A)\le\limsup_n\mu_n(A)\le\limsup_n\mu_n(\overline A)\le\mu(\overline A).$$

因 $\mathring A\subseteq A\subseteq\overline A$ 且 $\mu(\overline A\setminus\mathring A)=\mu(\partial A)=0$，有 $\mu(\mathring A)=\mu(A)=\mu(\overline A)$，故上式两端相等，得 $\lim_n\mu_n(A)=\mu(A)$。

**(d) $\Rightarrow$ (a)。** 设 $f\in C_b(S)$。通过 $f\mapsto f-\inf f$ 与 $f\mapsto\lambda f$（并把 $\mu_n(S)=\mu(S)=1$ 用于常数部分），不妨设 $0\le f\le M$。

令 $\eta:=\mu\circ f^{-1}$ 为 $\mathbb R$ 上的有限 Borel 测度。$\eta$ 的原子至多可数，故可取分割 $0=t_0<t_1<\dots<t_m=M$，使每个 $t_i$ 都是 $\eta$ 的连续点（即 $\eta(\{t_i\})=0$，等价于 $\mu\big(f^{-1}\{t_i\}\big)=0$），且 $\max_i(t_i-t_{i-1})<\epsilon$。

令 $A_i:=f^{-1}\big((t_{i-1},t_i]\big)$（$1\le i\le m$）。先验证 $A_i$ 是 $\mu$-连续集。设 $x\notin f^{-1}\{t_{i-1}\}\cup f^{-1}\{t_i\}$。若 $t_{i-1}<f(x)<t_i$，由连续性取邻域使其中 $f$ 仍落在 $(t_{i-1},t_i)$ 内，故 $x\in\mathring A_i$；若 $f(x)\le t_{i-1}$，则 $f(x)<t_{i-1}$，取邻域使 $f<t_{i-1}$，故 $x\notin\overline{A_i}$；若 $f(x)>t_i$ 同理 $x\notin\overline{A_i}$。因此在三种情形下都有 $x\notin\partial A_i$，即

$$\partial A_i\subseteq f^{-1}\{t_{i-1}\}\cup f^{-1}\{t_i\},\qquad \mu(\partial A_i)=0 .$$

于是由 (d)，$\mu_n(A_i)\to\mu(A_i)$ 对每个 $i$ 成立。注意 $\{A_i\}_{i=1}^m$ 是 $S$ 的一个分割（因 $0\le f\le M$）。

定义阶梯函数

$$g:=\sum_{i=1}^m t_{i-1}1_{A_i},\qquad h:=\sum_{i=1}^m t_i1_{A_i} .$$

则 $g\le f\le h$ 处处成立，且 $h-g=\sum_i(t_i-t_{i-1})1_{A_i}<\epsilon$ 处处成立，故

$$\int h\,d\mu-\int g\,d\mu=\int(h-g)\,d\mu<\epsilon .$$

于是

$$\liminf_{n}\int f\,d\mu_n\ge\liminf_n\int g\,d\mu_n=\lim_n\sum_i t_{i-1}\mu_n(A_i)=\sum_i t_{i-1}\mu(A_i)=\int g\,d\mu\ge\int f\,d\mu-\epsilon,$$

$$\limsup_{n}\int f\,d\mu_n\le\limsup_n\int h\,d\mu_n=\lim_n\sum_i t_i\mu_n(A_i)=\sum_i t_i\mu(A_i)=\int h\,d\mu\le\int f\,d\mu+\epsilon .$$

由 $\epsilon>0$ 任意，得 $\lim_n\int f\,d\mu_n=\int f\,d\mu$，即 (a)。

**(a) $\Rightarrow$ (e) $\Rightarrow$ (f)。** 显然：有界 Lipschitz 函数有界一致连续，有界一致连续函数有界连续。

**(f) $\Rightarrow$ (a)（同理 (e) $\Rightarrow$ (a)）。** 设 (f) 成立，记 $\mathcal{A}:=\mathrm{Lip}_b(S)$（$S$ 上有界 Lipschitz 函数全体）。$\mathcal{A}$ 是含常数 $1$ 的实向量空间，且对逐点乘积封闭（有界 Lipschitz 函数之积仍有界 Lipschitz），又 $\sigma(\mathcal{A})=\mathcal{B}(S)$：事实上每个 $x_0\in S$ 对应的 $x\mapsto d(x,x_0)$ 属于 $\mathcal{A}$，而每个开球 $\{d(x,x_0)<r\}$ 属于 $\sigma(\mathcal{A})$，可分性不是必需的（度量空间中任一开集是若干开球之并），故一切开集属于 $\sigma(\mathcal{A})$，反之 $\mathcal{A}$ 中函数连续故 Borel 可测。

令

$$\mathcal{C}:=\Big\{f\in B_b(S):\ \int f\,d\mu_n\xrightarrow[n\to\infty]{}\int f\,d\mu\Big\},$$

其中 $B_b(S)$ 是 $S$ 上有界 Borel 函数全体（赋上确界范数）。

**$\mathcal{C}$ 是向量空间**，包含常数（因 $\mu_n(S)=\mu(S)=1$），且由 (f) 有 $\mathcal{A}\subseteq\mathcal{C}$。

**$\mathcal{C}$ 对逐点有界单调极限封闭**：设 $f_k\in\mathcal{C}$，$|f_k|\le K$，$f_k\uparrow f$ 逐点。对每个 $\epsilon>0$，由有界收敛定理（对有限测度）$\int|f-f_k|\,d\mu_m\to0\ (k\to\infty)$，且因 $|f-f_k|\le 2K$ 与 $\mu_m(S)=1$，收敛对 $m$ 是**一致**的：存在 $k_0$ 使 $k\ge k_0$ 时对一切 $m$

$$\Big|\int f\,d\mu_m-\int f_k\,d\mu_m\Big|<\frac{\epsilon}{2} .$$

取这样的 $k\ge k_0$（且 $f_k\in\mathcal{C}$），再取 $n$ 充分大使 $\big|\int f_k\,d\mu_n-\int f_k\,d\mu\big|<\epsilon/2$，则对这样的 $n$

$$\Big|\int f\,d\mu_n-\int f\,d\mu\Big|\le\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon .$$

故 $\lim_n\int f\,d\mu_n=\int f\,d\mu$，即 $f\in\mathcal{C}$。

现由函数型单调类定理（$\mathcal{A}$ 为含 $1$、对乘积封闭的有界函数代数，$\sigma(\mathcal{A})=\mathcal{B}(S)$），$\mathcal{C}$ 包含一切有界 $\mathcal{B}(S)$-可测函数；特别地 $C_b(S)\subseteq B_b(S)\subseteq\mathcal{C}$，这正是 (a)。

**紧集的补充结论。** 若 $K$ 紧则 $K$ 闭，由 (c) 直接得 $\limsup_n\mu_n(K)\le\mu(K)$。

综上，六条条件等价。$\square$

**推论 1**：$\mu_n\Rightarrow\mu$ 当且仅当对一切 $\mu$-连续集有 $\mu_n(A)\to\mu(A)$；这给出检验弱收敛最方便的方式。

**推论 2**：$\nu\mapsto\nu(G)$（$G$ 开）在弱拓扑下下半连续，$\nu\mapsto\nu(F)$（$F$ 闭）上半连续。这是 Prokhorov 定理证明中构造开覆盖的基础。

**推论 3**：若 $\mu_n\Rightarrow\mu$ 且 $\mu$ 由某个子族决定（例如 $\mu$ 在一切 $\mu$-连续集上取值确定），则极限唯一。

## 相关条目

- [紧性准则](./紧性准则.md)：Prokhorov 定理的证明反复使用本定理的开集下半连续性。
- [单调类定理](./单调类定理.md)：本定理中 (e) 与 (a) 的等价性依赖函数型单调类定理。
- [Ulam胎紧定理](./Ulam胎紧定理.md)：为弱收敛理论提供紧集的来源与测度的正则性。
