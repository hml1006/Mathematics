# Sauer-Shelah引理

> **一句话大白话**：一个 VC 维为 $d$ 的假设空间，即使它能对任意 $n$ 个点产生很多种分类方式，分类方式的总数也不会超过把 $n$ 个点中最多 $d$ 个点挑出来的所有组合数之和。

> **小例子**：取 $n=10$、VC 维 $d=2$，则生长函数至多 $\binom{10}{0}+\binom{10}{1}+\binom{10}{2}=1+10+45=56$；而全部可能的二分类方式有 $2^{10}=1024$ 种，说明低 VC 维把表达力压低了近二十倍。

## 一、定理介绍

> **前置依赖**：VC维与生长函数、二项式系数、数学归纳法原理、组合恒等式。

Sauer-Shelah 引理是组合学与统计学习理论交叉处的一个基本计数结果，由 Norbert Sauer 与 Saharon Shelah 于 1972 年、以及 Vapnik 与 Chervonenkis 于 1971 年前后独立得到，因此有时也称 Sauer 引理或 Vapnik-Chervonenkis-Sauer 引理。它的历史动机来自一个纯粹的集合论问题：给定一个集合系（族）$\mathcal{H}$，若它不"打散"（shatter）任何 $d+1$ 元子集，那么它对 $n$ 元集合的限制最多能产生多少个不同的子集？这等价于问：VC 维这个"局部复杂度指标"能否反过来给出全局计数上界？

这个问题的意义在于，学习理论中控制泛化误差需要对假设空间做一致化的联合界（union bound），而联合界要求枚举所有可能的分类方式。若分类方式的数量可以被 VC 维以多项式（而非指数）方式上界，则联合界就能给出有意义的一致收敛速度。Sauer-Shelah 引理正是这一环节的关键：它证明生长函数 $\Pi_\mathcal{H}(n)$ 被 $\sum_{i=0}^{d}\binom{n}{i}$ 控制，从而至多按 $n^{d}$ 增长，为 VC 维泛化界、PAC 学习基本定理提供了组合基础。它与 Vapnik-Chervonenkis 维的"有限即学习可能"这一哲学结论紧密相连，也在组合几何、模型论（Shelah 的 NIP 理论）中有深远应用。

## 二、原理思路

1. 设 $S$ 是 $n$ 个点的集合，把假设空间限制在 $S$ 上，统计不同分类方式（即限制映射）的个数 $|\mathcal{H}_S|$。对 $n$ 做归纳，目标是把 $|\mathcal{H}_S|$ 分解为"去掉一个点后的限制数"加"被重复实现的那部分"。

2. 关键观察：每个限制在 $S'=S\setminus\{x_n\}$ 上的分类方式，在 $S$ 上要么只对应一种标签（唯一延拓），要么同时对应 $x_n$ 的两种标签（双重延拓）。双重延拓的集合 $D$ 是"子类"，它的 VC 维至多 $d-1$，因为若 $D$ 打散 $T$ 则原空间 $\mathcal{H}$ 会打散 $T\cup\{x_n\}$。

3. 于是得到递推 $|\mathcal{H}_S|\le\Phi(n-1,d)+\Phi(n-1,d-1)$，用 Pascal 恒等式合并成 $\Phi(n,d)=\sum_{i=0}^{d}\binom{n}{i}$，再用二项式系数的初等估计得到 $\left(\frac{en}{d}\right)^{d}$。

## 三、定理的严格表述

### 生长函数

设 $\mathcal{H}\subseteq\{0,1\}^{\mathcal{X}}$ 为二分类假设空间（或集合系）。它在 $n$ 个点上的生长函数定义为

$$
\Pi_{\mathcal{H}}(n)=\max_{x_1,\dots,x_n\in\mathcal{X}}\left|\left\{\left(h(x_1),\dots,h(x_n)\right):h\in\mathcal{H}\right\}\right| .
$$

若 $\mathcal{H}$ 能实现 $\{x_1,\dots,x_n\}$ 的全部 $2^{n}$ 种标签，则称 $\mathcal{H}$ 打散该集合；VC 维 $\mathrm{VCdim}(\mathcal{H})$ 为能被 $\mathcal{H}$ 打散的最大集合的基数。

### Sauer-Shelah 引理

设 $\mathrm{VCdim}(\mathcal{H})=d<\infty$。则对任意 $n\ge d$，

$$
\Pi_{\mathcal{H}}(n)\le\sum_{i=0}^{d}\binom{n}{i},
$$

并且进一步地有

$$
\Pi_{\mathcal{H}}(n)\le\left(\frac{en}{d}\right)^{d}.
$$

## 四、证明过程

**步骤 1（归结为有限集合上的计数）。** 固定 $S=\{x_1,\dots,x_n\}$，记 $\mathcal{H}_S=\left\{h|_{S}:h\in\mathcal{H}\right\}$ 为限制族。由于生长函数取遍所有 $n$ 点集的最大值，只需对任意固定的 $S$ 证明 $|\mathcal{H}_S|\le\Phi(n,d)$，其中

$$
\Phi(n,d)=\sum_{i=0}^{d}\binom{n}{i}.
$$

**步骤 2（归纳假设）。** 对 $n$ 归纳。基础情形 $n=0$：$\mathcal{H}$ 在空集上只有一种限制，$\Phi(0,d)=1$，成立。归纳假设：对一切至多 $n-1$ 个点、且 VC 维不超过 $d$ 或 $d-1$ 的族，结论成立。

**步骤 3（按延拓方式分类）。** 令 $S'=S\setminus\{x_n\}$，考虑限制映射 $\rho\colon\mathcal{H}_S\to\mathcal{H}_{S'}$，$\rho(h|_S)=h|_{S'}$。对每个 $h'\in\mathcal{H}_{S'}$，它在 $\rho$ 下的原像只能是 $1$ 或 $2$ 个元素（因为 $x_n$ 的标签只有 $0,1$ 两种）。记

$$
D=\left\{h'\in\mathcal{H}_{S'}:\ |\rho^{-1}(h')|=2\right\}
$$

为"双重延拓"的限制集合。于是

$$
\left|\mathcal{H}_S\right|=\left|\mathcal{H}_{S'}\right|+\left|D\right| .
$$

**步骤 4（第一项的界）。** $\mathcal{H}_{S'}$ 作为 $S'$ 上的集合系，其 VC 维不超过 $\mathrm{VCdim}(\mathcal{H})=d$（在更少的点上更不可能打散），故由归纳假设

$$
\left|\mathcal{H}_{S'}\right|\le\Phi(n-1,d).
$$

**步骤 5（$D$ 的 VC 维下降）。** 断言 $\mathrm{VCdim}(D)\le d-1$。反设 $D$ 打散某个 $T\subseteq S'$ 且 $|T|=d$。任取 $R\subseteq T\cup\{x_n\}$：若 $x_n\notin R$，由 $D$ 打散 $T$ 存在 $h'\in D$ 使 $h'$ 在 $T$ 上与 $R$ 一致，又 $h'\in D$ 有延拓 $h\in\mathcal{H}$，于是 $h|_{T}=R|_{T}$；若 $x_n\in R$，同样取 $h'\in D$ 在 $T$ 上与 $R\cap T$ 一致，并取 $h'$ 的那个使 $h(x_n)=1$ 的延拓（双重延拓保证存在）。两种情形说明 $\mathcal{H}$ 能实现 $T\cup\{x_n\}$ 的任一二分标签，即 $\mathcal{H}$ 打散 $T\cup\{x_n\}$，共 $d+1$ 个点，与 $\mathrm{VCdim}(\mathcal{H})=d$ 矛盾。故 $\mathrm{VCdim}(D)\le d-1$。

**步骤 6（合并递推）。** 对 $D$ 用归纳假设，

$$
\left|D\right|\le\Phi(n-1,d-1)=\sum_{i=0}^{d-1}\binom{n-1}{i}.
$$

代入步骤 3 并用 Pascal 恒等式 $\binom{n-1}{i}+\binom{n-1}{i-1}=\binom{n}{i}$，得

$$
\left|\mathcal{H}_S\right|\le\sum_{i=0}^{d}\binom{n-1}{i}+\sum_{i=0}^{d-1}\binom{n-1}{i}=\sum_{i=0}^{d}\binom{n}{i}=\Phi(n,d).
$$

**步骤 7（多项式形式上界）。** 由 $\binom{n}{i}=\binom{n}{d}\cdot\frac{d!\,(n-d)!}{i!\,(n-i)!}$ 对 $i\le d$ 有 $\binom{n}{i}\le\binom{n}{d}\left(\frac{n}{d}\right)^{d-i}$，故

$$
\sum_{i=0}^{d}\binom{n}{i}\le\binom{n}{d}\sum_{i=0}^{d}\left(\frac{d}{n}\right)^{d-i}\le\binom{n}{d}\sum_{j\ge0}\left(\frac{d}{n}\right)^{j}\le\left(\frac{en}{d}\right)^{d}\cdot\frac{1}{1-d/n}.
$$

当 $n\ge2d$ 时 $\frac{1}{1-d/n}\le2$，吸收常数后得到所断言的 $\left(\frac{en}{d}\right)^{d}$ 型上界（常数可从指数中吸收）。$\square$

## 五、应用与意义

- 学习理论：它是 VC 维泛化界与 PAC 学习基本定理的组合支柱，把"有限 VC 维"翻译为"生长函数多项式增长"，使一致联合界成为可能。
- 组合几何：刻画集合系在有限点集上的投影数上限，用于 $\varepsilon$-网、范围查询等问题的复杂度分析。
- 模型论：Shelah 的 NIP（不具独立性质）理论中，Sauer-Shelah 引理是"VC 维有限等价于 NIP"的核心工具。
- 计算学习：给出学习所需样本量随 VC 维线性、随精度多项式增长的定量保证，支持结构风险最小化的模型选择。

## 课堂问答

**老师**：一个 VC 维为 $d$ 的族，最多能对 $n$ 个点产生多少种分类？

**学生**：结论：$\Pi_{\mathcal{H}}(n)\le\sum_{i=0}^{d}\binom{n}{i}$，进一步不超过 $\big(\frac{en}{d}\big)^d$。例如 $n=10,d=2$ 时上界是 $1+10+45=56$，远小于 $2^{10}=1024$，说明低 VC 维把表达力压成多项式级而非指数级。

**老师（追问）**：归纳证明里，最关键的是哪一步？

**学生**：是"双重延拓集合"的 VC 维下降。记 $D=\{h'\in\mathcal{H}_{S'}:\ |\rho^{-1}(h')|=2\}$，断言 $\operatorname{VCdim}(D)\le d-1$。反设 $D$ 打散某个 $|T|=d$ 的子集，则 $T$ 上任一标签再配上 $x_n$ 的两种选择都能实现，于是 $\mathcal{H}$ 打散 $T\cup\{x_n\}$ 这 $d+1$ 个点，与 $\operatorname{VCdim}(\mathcal{H})=d$ 矛盾。由此得 $|\mathcal{H}_S|\le\Phi(n-1,d)+\Phi(n-1,d-1)$，用 Pascal 恒等式合并即得。

**老师（拓展）**：为什么这个计数结果在整个学习理论里这么重要？

**学生**：因为它把"VC 维有限"翻译成"生长函数按 $n^d$ 多项式增长"，使一致化所需的联合界从"枚举指数多个事件"变成"只需管多项式多个"，VC 维泛化界与 PAC 基本定理才得以成立。常见误区是以为"能实现 $2^d$ 种标签"就等于 VC 维为 $d$——VC 维要求的是打散某个具体的 $d$ 点集，即对该集全部 $2^d$ 种标签都能实现，二者不是一回事。

## 相关条目

- [VC维的泛化界](./VC维的泛化界.md)：直接以本引理把生长函数用 VC 维控制，得到一致泛化界。
- [PAC学习的基本定理](./PAC学习的基本定理.md)：有限假设空间的样本复杂度结论与本引理同源。
- [Rademacher复杂度的泛化界](./Rademacher复杂度的泛化界.md)：另一条刻画假设空间复杂度的路径。
- [SVM的泛化界](./SVM的泛化界.md)：以间隔与 VC 维结合的泛化分析。
- [组合恒等式](../第28级-组合数学/组合恒等式.md)：Pascal 恒等式等计数工具。
- [数学归纳法原理](../第07级-数列与数学归纳法/数学归纳法原理.md)：本证明采用的归纳框架。
- [鸽巢原理一般形式](../第28级-组合数学/鸽巢原理一般形式.md)：计数型存在性论证的同类工具。
