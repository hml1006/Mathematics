# Minkowski 嵌入与数域判别式

> **一句话大白话**：把数域的每个元素"同时扔进所有实数与复数坐标系"，就得到一个 $n$ 维欧氏空间里的格子；这个格子的体积（的平方，去掉 $2$ 的因子）就是判别式，它衡量数域"有多扭曲"，也决定哪些素数会分歧。
>
> **小例子**：$K=\mathbb Q(\sqrt2)$ 有两个实嵌入 $\sqrt2\mapsto\pm\sqrt2$，Minkowski 嵌入把整数环 $\mathbb Z[\sqrt2]$ 送成 $\mathbb R^2$ 中的正菱形格子，余体积为 $\tfrac12\sqrt{|d_K|}$，而 $d_K=8$。

## 一、定理介绍

> **前置依赖**：本原元素定理、Minkowski凸体定理、共轭嵌入与迹形式、代数整数与整闭性

在代数数论中，数域 $K$ 是 $\mathbb Q$ 的 $n$ 次有限扩张，其元素是抽象的代数数。**Minkowski 嵌入**（Minkowski embedding）把 $K$ 线性地嵌入到 $n$ 维欧氏空间 $\mathbb R^{r_1}\times\mathbb C^{r_2}$ 中，从而使"抽象的数域"变成"具体的格（lattice）"：$K$ 中每个元素对应一个实向量，整数环 $\mathcal O_K$ 对应一个离散的、余体积有限的格。

这一转换（Hermann Minkowski，19 世纪末）是代数数论的几何化开端。一旦有了格，就可以使用 Minkowski 凸体定理这类"几何数论"工具，得出纯代数很难得到的结论：判别式是非零整数、$|d_K|>1$（$K\ne\mathbb Q$）、理想类群有限、单位群由 Dirichlet 单位定理描述。

**判别式**（discriminant）$d_K$ 是数域最基本的数值不变量之一。它与 Minkowski 嵌入的格余体积直接相关，并精确刻画分歧：有理素数 $p$ 在 $\mathcal O_K$ 中分歧（即 $p\mathcal O_K$ 的某个指数 $e_i>1$）当且仅当 $p\mid d_K$。本条目把嵌入、迹形式、判别式与格余体积这四条线索统一起来。

**迹形式**（trace form）$T(x,y)=\mathrm{Tr}_{K/\mathbb Q}(xy)$ 是 $K$ 上 $\mathbb Q$-双线性型，其行列式（在 $\mathbb Z$-基下）正是判别式。这一等价刻画使判别式可以用线性代数计算，也是判别式乘性行为与"基变换公式"的来源。

## 二、原理思路

设 $K$ 是 $n$ 次数域，$\alpha$ 为本原元素（即 $K=\mathbb Q(\alpha)$，由本原元素定理存在）。

**1. 共轭嵌入。** $\alpha$ 的极小多项式有 $n$ 个复根，实根给出 $r_1$ 个实嵌入 $\sigma_1,\dots,\sigma_{r_1}:K\hookrightarrow\mathbb R$，非实根成共轭对，给出 $r_2$ 个复嵌入对 $\sigma_{r_1+1},\overline{\sigma_{r_1+1}},\dots$。于是

$$
n=r_1+2r_2 .
$$

**2. Minkowski 嵌入。** 定义

$$
\iota:K\longrightarrow \mathbb R^{r_1}\times\mathbb C^{r_2}\cong\mathbb R^n,\qquad
\iota(x)=\bigl(\sigma_1(x),\dots,\sigma_{r_1}(x),\sigma_{r_1+1}(x),\dots,\sigma_{r_1+r_2}(x)\bigr).
$$

它是 $\mathbb Q$-线性单射（若所有 $\sigma_i(x)=0$ 则 $x$ 的所有共轭为 $0$，故 $x=0$）。

**3. 判别式作为"格拉姆行列式"。** 对 $K$ 的一组 $\mathbb Q$-基 $\alpha_1,\dots,\alpha_n$，定义

$$
\mathrm{disc}(\alpha_1,\dots,\alpha_n)=\det\bigl(\mathrm{Tr}_{K/\mathbb Q}(\alpha_i\alpha_j)\bigr)_{i,j}
=\det\bigl(\sigma_i(\alpha_j)\bigr)_{i,j}^{2}.
$$

判别式与基无关，只差一个平方因子；对整基 $\omega_1,\dots,\omega_n$（$\mathcal O_K=\mathbb Z\omega_1\oplus\cdots\oplus\mathbb Z\omega_n$，其存在性是数域与整数环理论的结果）记

$$
d_K=\mathrm{disc}(\omega_1,\dots,\omega_n)\in\mathbb Z\setminus\{0\}.
$$

**4. 格余体积。** $\iota(\mathcal O_K)$ 是 $\mathbb R^n$ 中的格。用共轭对把 $\mathbb C$ 换成 $\mathbb R^2$ 时体积元引入 $2^{-r_2}$ 的因子，最终

$$
\operatorname{covol}\bigl(\iota(\mathcal O_K)\bigr)=2^{-r_2}\sqrt{|d_K|}.
$$

**5. 用凸体定理得到判别式界限。** 取对称凸体（如"球"或"方体"）的体积足够大，由 Minkowski 凸体定理可得其中存在非零格点，从而得到

$$
|d_K|\ \ge\ \Bigl(\frac{n^n}{n!}\Bigr)^{2}\Bigl(\frac{\pi}{4}\Bigr)^{2r_2},
$$

特别地 $|d_K|>1$（$n\ge2$）。由于 $d_K$ 是非零整数，这就给出了判别式的"下界"。

## 三、定理的严格表述

**（Minkowski 嵌入定理）** 设 $K$ 为 $n$ 次数域，具有 $r_1$ 个实嵌入与 $r_2$ 对复嵌入，$n=r_1+2r_2$。则

$$
\iota:K\to\mathbb R^{r_1}\times\mathbb C^{r_2}\cong\mathbb R^n,\qquad
x\mapsto(\sigma_1(x),\dots,\sigma_{r_1}(x),\sigma_{r_1+1}(x),\dots,\sigma_{r_1+r_2}(x))
$$

是 $\mathbb Q$-线性的单射，且 $\iota(K)$ 在 $\mathbb R^n$ 中稠密当且仅当 $n=1$；而 $\iota(\mathcal O_K)$ 是 $\mathbb R^n$ 中的满秩格，其余体积为

$$
\operatorname{covol}\bigl(\iota(\mathcal O_K)\bigr)=2^{-r_2}\sqrt{|d_K|}.
$$

**（判别式的等价刻画）** 设 $\alpha_1,\dots,\alpha_n$ 是 $K$ 的一组 $\mathbb Q$-基，则

$$
\mathrm{disc}(\alpha_1,\dots,\alpha_n)=\det\bigl(\mathrm{Tr}_{K/\mathbb Q}(\alpha_i\alpha_j)\bigr)_{i,j}=\det\bigl(\sigma_i(\alpha_j)\bigr)_{i,j}^{2}\neq0 .
$$

特别地，$\alpha_1,\dots,\alpha_n$ 线性无关当且仅当该行列式非零。

**（基变换公式）** 若 $\beta_i=\sum_j a_{ij}\alpha_j$（$A=(a_{ij})$），则

$$
\mathrm{disc}(\beta_1,\dots,\beta_n)=\det(A)^{2}\,\mathrm{disc}(\alpha_1,\dots,\alpha_n).
$$

因此对任意 $\mathbb Z$-基 $\beta_1,\dots,\beta_n$ 生成的子格 $\Lambda=\mathbb Z\beta_1\oplus\cdots\oplus\mathbb Z\beta_n\subseteq\mathcal O_K$ 有

$$
\mathrm{disc}(\beta_1,\dots,\beta_n)=[\mathcal O_K:\Lambda]^{2}\,d_K .
$$

**（Minkowski 判别式界限）** 设 $n\ge2$，则

$$
|d_K|\ \ge\ \Bigl(\frac{n^n}{n!}\Bigr)^{2}\Bigl(\frac{\pi}{4}\Bigr)^{2r_2}>1 .
$$

特别地 $d_K\ne\pm1$ 对 $n\ge2$ 成立。

## 四、证明过程

**步骤 1：$\iota$ 是 $\mathbb Q$-线性单射。**

每个 $\sigma_i$ 是域嵌入，故是 $\mathbb Q$-线性的，因此 $\iota$ 是 $\mathbb Q$-线性的。若 $\iota(x)=0$，则 $x$ 的每个共轭 $\sigma_i(x)=0$。由本原元素定理写 $K=\mathbb Q(\alpha)$，$x=g(\alpha)$（$g\in\mathbb Q[x]$，$\deg g<n$），则 $\sigma_i(x)=g(\sigma_i(\alpha))$。$x$ 的共轭（含重数）$g(\sigma_i(\alpha))$ 全为 $0$，即多项式 $g$ 在 $\alpha$ 的全部共轭处取零，共 $n$ 个根；而 $\deg g<n$，故 $g\equiv0$，于是 $x=0$。$\square$

**步骤 2：判别式 = 迹形式行列式 = $\det(\sigma_i(\alpha_j))^2$。**

设 $M=(\sigma_i(\alpha_j))_{i,j}$（$n\times n$ 复矩阵）。计算

$$
(M M^{\mathsf T})_{ij}=\sum_{k}\sigma_k(\alpha_i)\sigma_k(\alpha_j).
$$

由于 $\sigma_{r_1+t}$ 与 $\sigma_{r_1+r_2+t}$ 成共轭对（分别记作 $\sigma,\bar\sigma$），当 $t$ 取遍 $1,\dots,r_2$ 时

$$
\sigma(\alpha_i)\sigma(\alpha_j)+\bar\sigma(\alpha_i)\bar\sigma(\alpha_j)=2\operatorname{Re}\bigl(\sigma(\alpha_i)\sigma(\alpha_j)\bigr)
$$

而 $\mathrm{Tr}_{K/\mathbb Q}(\alpha_i\alpha_j)=\sum_{t=1}^{n}\sigma_t(\alpha_i\alpha_j)=\sum_t\sigma_t(\alpha_i)\sigma_t(\alpha_j)$；实嵌入项与共轭对项相加后恰等于上式右端的实部之和，即 $\sum_k\sigma_k(\alpha_i)\sigma_k(\alpha_j)$。故

$$
MM^{\mathsf T}=\bigl(\mathrm{Tr}_{K/\mathbb Q}(\alpha_i\alpha_j)\bigr)_{i,j},
$$

取行列式得 $\det(M)^2=\det(\mathrm{Tr}(\alpha_i\alpha_j))$，即所证。（$\det M$ 的平方消去符号歧义。）

**步骤 3：非零性与基变换公式。**

由步骤 1，$\{\alpha_j\}$ 是 $K$ 的 $\mathbb Q$-基，故矩阵 $M=(\sigma_i(\alpha_j))$ 可逆：若 $Mv=0$，则 $\sum_j v_j\alpha_j$ 的所有共轭为零，由步骤 1 得 $\sum_j v_j\alpha_j=0$，因 $\{\alpha_j\}$ 线性无关得 $v=0$。于是 $\det M\ne0$，判别式非零。

基变换公式来自行列式的乘性：把 $\beta_i=\sum_j a_{ij}\alpha_j$ 代入 $\det(\sigma_i(\beta_j))=\det(M A^{\mathsf T})=\det M\det A$，平方即得。取 $\Lambda$ 由整基子集生成、并注意 $\det A=[\mathcal O_K:\Lambda]$，得 $\mathrm{disc}(\beta)=[\mathcal O_K:\Lambda]^2 d_K$。

**步骤 4：格余体积公式。**

把 $\mathbb C$ 用实坐标 $(u,v)\mapsto u+iv$ 识别为 $\mathbb R^2$。映射 $\mathbb C\to\mathbb R^2$ 在实意义下是 $\mathbb R$-线性的；由

$$
(u+iv)(x+iy)=(ux-vy)+i(uy+vx)
$$

得乘法的实矩阵行列式为 $u^2+v^2=|z|^2$。因此由 $\mathbb C^{r_2}\to\mathbb R^{2r_2}$ 的变换使体积元放大 $|\det|=1$，但共轭对的两行互相确定，实际使用的 $r_2$ 个复嵌入所张成的实二维块体积元相对于"每对贡献的两个实坐标"相差因子 $2^{r_2}$；逐步计算得基本域体积

$$
\operatorname{covol}\bigl(\iota(\mathcal O_K)\bigr)=\bigl|\det(\sigma_i(\omega_j))\bigr|\cdot 2^{-r_2}=2^{-r_2}\sqrt{|d_K|}.
$$

（等价说法：$\iota(K)$ 在 $\mathbb R^{r_1}\times\mathbb C^{r_2}$ 的映射下，$\mathcal O_K$ 的基本域体积恰为 $\sqrt{|d_K|}$，除以共轭方向重复计数 $2^{r_2}$。）$\square$

**步骤 5：判别式界限（调用 Minkowski 凸体定理）。**

在 $\mathbb R^{r_1}\times\mathbb C^{r_2}$ 中取对称凸体

$$
B_t=\Bigl\{(x_1,\dots,x_{r_1},z_1,\dots,z_{r_2}):\ \sum_{i=1}^{r_1}|x_i|+2\sum_{j=1}^{r_2}|z_j|<t\Bigr\}.
$$

其体积为 $\operatorname{vol}(B_t)=2^{r_1}\bigl(\tfrac{\pi}{2}\bigr)^{r_2}\dfrac{t^n}{n!}$。取 $t$ 使 $\operatorname{vol}(B_t)>2^n\operatorname{covol}(\iota(\mathcal O_K))$，由 Minkowski 凸体定理存在非零格点 $\iota(x)\in B_t$（$x\in\mathcal O_K\setminus\{0\}$）。对这样的 $x$，由 $N(x)=\prod_i\sigma_i(x)$ 的绝对值满足 $|N(x)|\ge1$（$x$ 是非零代数整数）与算术–几何平均不等式

$$
\Bigl(\sum_{i=1}^{r_1}|x_i|+2\sum_{j=1}^{r_2}|z_j|\Bigr)^n\ \ge\ n^n\Bigl(\frac{\pi}{4}\Bigr)^{r_2}\prod_{i=1}^{n}|\sigma_i(x)|\ \ge\ n^n\Bigl(\frac{\pi}{4}\Bigr)^{r_2},
$$

结合 $\iota(x)\in B_t$ 给出 $t$ 的一个上界，代入体积不等式整理即得 $|d_K|\ge\bigl(\tfrac{n^n}{n!}\bigr)^2\bigl(\tfrac{\pi}{4}\bigr)^{2r_2}$。右端当 $n\ge2$ 时严格大于 $1$（由 $n^n/n!$ 的增长与 $(\pi/4)^{2r_2}=\mathrm e^{O(n)}$ 的下降相比慢，需 $2r_2=2n-2r_1\le n-1$ 时逐项验证，$n=2$ 直接得 $|d_K|\ge\pi^2/4>1$，$n\ge3$ 时 $\bigl(n^n/n!\bigr)^2\ge 2^{2n}/n!$ 已充分大）。$\square$

## 五、应用与意义

**1. 判别式与分歧。** $p$ 在 $K$ 中分歧 $\iff p\mid d_K$。由于 $|d_K|$ 有限（步骤 5 给出界），每个数域只有有限多个分歧素数——这是"几乎处处不分歧"这一数论基本原则的根源。

**2. 格论工具的全部威力。** 有了 $\iota(\mathcal O_K)$ 是余体积有限的满秩格，Minkowski 凸体定理、格的约化理论、Hermite 常数等几何数论工具都可以直接使用。理想类群有限性（见[理想类群与有限性](./理想类群与有限性.md)）就是用 Minkowski 凸体定理在每个理想类中"挑出"范数有界的整理想而得到的。

**3. 判别式与二次型、二次域。** 二次域 $K=\mathbb Q(\sqrt d)$ 的判别式为 $d_K=d$（$d\equiv1\bmod4$）或 $d_K=4d$（$d\equiv2,3\bmod4$），直接对应二次数域的整基与二次型的判别式理论。

**4. 类数与 $\zeta$ 函数。** $d_K$ 出现在 Dedekind $\zeta$ 函数的函数方程与类数公式（Dirichlet 类数公式）中；解析类数公式把 $h_K$ 与 $\sqrt{|d_K|}$、$L(1,\chi)$ 联系起来。

**5. 迹形式与代数数论。** 迹形式 $T(x,y)=\mathrm{Tr}(xy)$ 给出 $\mathcal O_K$ 的对偶格与**不同理想**（different）$\mathfrak D_{K/\mathbb Q}$ 的刻画，进而给出判别式的理想论描述 $d_K=N(\mathfrak D)$ 与 Riemann–Roch 型定理（不同理想–判别式定理）。

**6. 计算与算法。** Minkowski 嵌入与判别式界限是计算数域表、判别式分类与类群计算（如经 LLL 约化求整基与短向量）的核心工具。

## 课堂问答

**老师**：判别式到底是哪一个矩阵的行列式？它和格体积是什么关系？

**学生**：$d_K=\det(\operatorname{Tr}_{K/\mathbb Q}(\omega_i\omega_j))=\det(\sigma_i(\omega_j))^2$，即迹形式在整基下的行列式。Minkowski 嵌入 $\iota(x)=(\sigma_1(x),\dots,\sigma_{r_1}(x),\sigma_{r_1+1}(x),\dots)$ 把 $\mathcal O_K$ 送成 $\mathbb R^{r_1}\times\mathbb C^{r_2}\cong\mathbb R^n$ 中的满秩格，其余体积为 $\operatorname{covol}(\iota(\mathcal O_K))=2^{-r_2}\sqrt{|d_K|}$。

**老师（追问）**：判别式怎么控制"哪些素数分歧"？

**学生**：有理素数 $p$ 在 $K$ 中分歧 $\iff p\mid d_K$。配合 Minkowski 判别式界限 $|d_K|\ge(\frac{n^n}{n!})^2(\frac\pi4)^{2r_2}>1$（$n\ge2$），立刻得到：每个数域只有有限多个分歧素数，且 $n\ge2$ 时不存在无分歧扩张（因为那会要求 $|d_K|=1$）。

**老师（拓展）**：基变换公式和常见误区？

**学生**：换 $\mathbb Q$-基时 $(\beta_i)=(\alpha_j)A$ 给出 $\operatorname{disc}(\beta_1,\dots,\beta_n)=\det(A)^2\operatorname{disc}(\alpha_1,\dots,\alpha_n)$，故整基实现最小判别式；对子格 $\Lambda=\mathbb Z\beta_1\oplus\cdots\oplus\mathbb Z\beta_n\subseteq\mathcal O_K$ 更有 $\operatorname{disc}(\beta)=[\mathcal O_K:\Lambda]^2 d_K$。误区是以为判别式会随基改变——它只差一个平方因子，作为数域的不变量（在选定整基后）完全确定。
