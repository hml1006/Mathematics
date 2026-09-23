# Jacobi-Trudi 行列式与 Vandermonde 行列式

> **一句话大白话**：Schur 函数虽然定义成"半标准表的权重和"，其实可以整个塞进一个行列式——把完全齐次对称函数 $h_k$ 按划分 $\lambda$ 的形状错位摆放、取行列式，得到的正是 $s_\lambda$；而分母上那个著名的 Vandermonde 行列式 $\prod_{i<j}(x_i-x_j)$，其实就是"置换符号"的化身，为行列式比表达式提供反对称性。

> **小例子**：对 $\lambda=(2,1)$，Jacobi–Trudi 给出 $s_{(2,1)}=\det\begin{smallmatrix}h_2&h_3\\h_0&h_1\end{smallmatrix}=h_2h_1-h_3$，在三个变量下展开正是 $x_1^2x_2+x_1x_2^2+x_1^2x_3+x_1x_3^2+x_2^2x_3+x_2x_3^2+2x_1x_2x_3$；Vandermonde 行列式 $\det(x_i^{\,3-j})_{i,j=1}^3$ 则等于 $(x_1-x_2)(x_1-x_3)(x_2-x_3)$。

## 一、定理介绍

> **前置依赖**：完全齐次对称函数与初等对称函数、Schur 函数与半标准 Young 表、Young 图与共轭划分、行列式与 Leibniz 展开、行列式展开定理、对称函数基本定理。

Jacobi–Trudi 恒等式（Jacobi 1841、Trudi 1864）是 Schur 函数最古典的两个行列式表达式，它把"半标准表计数"这一组合定义转化为完全齐次对称函数 $h_k$（或对偶地，初等对称函数 $e_k$）的行列式。设 $\lambda=(\lambda_1\ge\cdots\ge\lambda_r\ge0)$ 为划分，$\lambda'$ 为其共轭划分，并约定 $h_0=e_0=1$、$k<0$ 时 $h_k=e_k=0$，则

$$ s_\lambda=\det\big(h_{\lambda_i-i+j}\big)_{1\le i,j\le r}=\det\big(e_{\lambda'_i-i+j}\big)_{1\le i,j\le r}. $$

Vandermonde 行列式（Vandermonde 1772）是另一个古典结果：对 $n$ 个变量 $x_1,\dots,x_n$，

$$ \det\big(x_i^{\,n-j}\big)_{1\le i,j\le n}=\prod_{1\le i<j\le n}(x_i-x_j). $$

两者结合给出 Schur 函数的"行列式比"（Weyl 分母公式），它是 Schur 函数对称性、正交性与 Weyl 特征标公式在 $GL(n)$ 情形的组合出发点：

$$ s_\lambda(x_1,\dots,x_n)=\frac{\det\big(x_i^{\lambda_j+n-j}\big)_{i,j=1}^{n}}{\det\big(x_i^{\,n-j}\big)_{i,j=1}^{n}}. $$

## 二、原理思路

1. **Vandermonde：用零因子定位符号。** 行列式 $V(x)=\det(x_i^{\,n-j})$ 是交错多项式（交换两个变量变号）。令 $x_i=x_j$ 则两行相同、$V=0$，故每个 $x_j-x_i$ 都整除 $V$；诸因子两两互素，故其乘积整除 $V$。比较次数与首项系数即得公式。

2. **Jacobi–Trudi：把行列式展开读成符号消去。** $h_k$ 展开为长度 $k$ 的弱增序列的单项式之和，于是 Leibniz 展开给出"按行排布的弱增序列组"的有符号求和。一个对合操作（交换某列中出现相等条目的相邻两行）把符号相反的项成对抵消；幸存者恰好是"行弱增、列严格增"的填充，即半标准 Young 表（SSYT），且每张表符号为 $+1$，故行列式等于 $s_\lambda$。

3. **对偶形式。** 把 $h$ 换成 $e$、把"行弱增"的初始约束换成"列严格增"（$e_k$ 展开为严格增序列）后重复同一消去论证，幸存者是"行严格增、列弱增"的填充；经转置（Bender–Knuth 型权保持对合）即得 $\lambda'$ 的 SSYT，于是 $\det(e_{\lambda'_i-i+j})=s_\lambda$。这解释了为什么"$h\leftrightarrow e$ 与 $\lambda\leftrightarrow\lambda'$ 同时替换"保持公式不变。

4. **行列式比。** 在 $r=n$、$\mu_j=\lambda_j+n-j$ 的情形下把第一形式与生成函数 $\sum_kh_kt^k=\prod_i(1-x_it)^{-1}$ 结合，用 Cauchy–Binet 分离变量，即得 $\det(h_{\mu_j-i+j})=\det(x_i^{\mu_j})/\prod_{i<j}(x_i-x_j)$，这正是行列式比。

## 三、定理的严格表述

固定变量个数 $n$。对 $k\ge0$ 定义

$$ h_k=\sum_{1\le i_1\le\cdots\le i_k\le n}x_{i_1}\cdots x_{i_k},\qquad e_k=\sum_{1\le i_1<\cdots<i_k\le n}x_{i_1}\cdots x_{i_k},\qquad h_0=e_0=1, $$

约定 $k<0$ 时 $h_k=e_k=0$。设 $\lambda$ 为划分，$\ell(\lambda)$ 为其部分数，$\lambda'$ 为共轭划分。

**定理（Jacobi–Trudi，第一形式）**：对任意 $r\ge\ell(\lambda)$，

$$ s_\lambda=\det\big(h_{\lambda_i-i+j}\big)_{1\le i,j\le r}, $$

其中 $\lambda$ 补零至长度 $r$（$i>r$ 时不出现）。$r$ 增大时行列式不变。

**定理（Jacobi–Trudi，第二形式）**：对任意 $r'\ge\ell(\lambda')$，

$$ s_\lambda=\det\big(e_{\lambda'_i-i+j}\big)_{1\le i,j\le r'}. $$

**定理（Vandermonde 行列式）**：$\det\big(x_i^{\,n-j}\big)_{1\le i,j\le n}=\prod_{1\le i<j\le n}(x_i-x_j)$；等价地

$$ \det\big(x_i^{\,j-1}\big)_{1\le i,j\le n}=\prod_{1\le i<j\le n}(x_j-x_i)=(-1)^{\binom n2}\prod_{1\le i<j\le n}(x_i-x_j). $$

**推论 1（Weyl 分母公式 / 行列式比）**：$s_\lambda=\dfrac{\det\big(x_i^{\lambda_j+n-j}\big)}{\det\big(x_i^{\,n-j}\big)}$。特别地 $s_{(k)}=h_k$、$s_{(1^k)}=e_k$，且

$$ s_{(n-1,n-2,\dots,1,0)}(x_1,\dots,x_n)=\prod_{1\le i<j\le n}(x_i-x_j). $$

**推论 2（Schur 函数的对称性）**：由推论 1，分子分母同为交错多项式，交换 $x_i,x_j$ 时同时变号，比值不变，故 $s_\lambda$ 是对称函数。

## 四、证明过程

**证明（Vandermonde 行列式）：**

$V(x)=\det(x_i^{\,n-j})$ 是 $x_1,\dots,x_n$ 的 $\binom n2$ 次齐次多项式，且为交错多项式：交换 $x_i$ 与 $x_j$ 等于交换该行列式的第 $i,j$ 两行，故 $V$ 变号。若 $x_i=x_j$，两行完全相同故 $V=0$；由因子定理，$x_j-x_i$ 整除 $V$。因不同因子 $x_j-x_i$ 两两互素，乘积 $P=\prod_{i<j}(x_j-x_i)$ 也整除 $V$。$P$ 与 $V$ 同为 $\binom n2$ 次齐次多项式，故 $V=cP$；比较主对角线项 $\prod_{i}x_i^{\,n-i}$ 的系数（$V$ 中该项系数为 $1$，$P$ 中亦为 $1$），得 $c=1$。$\blacksquare$

**证明（Jacobi–Trudi，第一形式）：**

**第一步（Leibniz 展开读成行填充）。** 由行列式的 Leibniz 公式，

$$ \det\big(h_{\lambda_i-i+j}\big)=\sum_{\sigma\in S_r}\mathrm{sgn}(\sigma)\prod_{i=1}^rh_{\lambda_i-i+\sigma(i)}. $$

把每个 $h_k$ 展开为长度 $k$ 的弱增序列 $1\le a_1\le\cdots\le a_k\le n$ 的 $x_{a_1}\cdots x_{a_k}$ 之和。固定 $\sigma$ 后，$\prod_ih_{\lambda_i-i+\sigma(i)}$ 的每一项对应于"第 $i$ 行填入一个长度 $\lambda_i$ 的弱增序列"，其中序列被安置的位置由行内偏移决定；因此每一项对应于把 $\lambda$ 的格子按行填入数字、使每行弱增的一个填充 $T$，并附带符号 $\mathrm{sgn}(\sigma)$，权重为 $x^T=\prod_{\text{格}}x_{T(\text{格})}$。

**第二步（符号消去）。** 定义映射 $\varphi$：若存在相邻两行 $i,i+1$ 在某列 $c$ 上条目相等，取最靠上的这样一对，交换第 $i$、$i+1$ 两行的整段数据（等价地把 $\sigma$ 右乘换位 $(i\,i+1)$ 并相应交换两行序列）。因 $\lambda_{i+1}\le\lambda_i$、行间恰错位一格，交换后仍是合法的弱增行填充，而 $\mathrm{sgn}$ 因换位（奇置换）变号，故两项符号相反、权重相同，成对抵消。$\varphi$ 是对合，故所有"某列存在相等相邻条目"的项总和为零。

**第三步（幸存者即 SSYT）。** 消去后剩下的填充满足：每行弱增，且每列严格增。这正是形状 $\lambda$、取值于 $\{1,\dots,n\}$ 的半标准 Young 表。反之，SSYT 不存在可消去的相邻相等对，故不被 $\varphi$ 移动；且此时错位方式与行弱增相容，$\sigma$ 的贡献只为恒等元（其余 $\sigma$ 给出的填充必然在某列出现相等的相邻条目），符号为 $+1$。于是

$$ \det\big(h_{\lambda_i-i+j}\big)=\sum_{T\in\mathrm{SSYT}(\lambda)}x^{T}=s_\lambda. \qquad\blacksquare $$

**证明（第二形式）：** 把上述论证中的 $h_k$ 换成 $e_k$：$e_k$ 展开为严格增序列，故初始约束变成"每列严格增"，符号消去（对合改在"某行出现相等相邻条目"处进行）后的幸存者满足"每行严格增、每列弱增"。转置这样的填充得形状 $\lambda'$ 的弱增行、严格增列表，即 $\mathrm{SSYT}(\lambda')$ 在权保持对合下的像，权重和仍为 $s_\lambda$（转置不改变各列/各行乘积的权），故 $\det(e_{\lambda'_i-i+j})=s_\lambda$。$\blacksquare$

**证明（推论 1，行列式比）：** 取 $r=n$，令 $\mu_j=\lambda_j+n-j$（则 $\mu_1>\mu_2>\cdots>\mu_n\ge0$，且 $\lambda_j=\mu_j-(n-j)$），第一形式给出

$$ s_\lambda=\det\big(h_{\mu_j-i+j}\big)_{1\le i,j\le n}. $$

由生成函数 $\sum_{k\ge0}h_kt^k=\prod_{m=1}^{n}(1-x_mt)^{-1}$，把每列 $j$ 的序列看作 $t^{\mu_j-i+j}$ 的系数，用 Cauchy–Binet 展开 $\det(h_{\mu_j-i+j})$ 为"变量分配"的求和，得

$$ \det\big(h_{\mu_j-i+j}\big)=\frac{\det\big(x_i^{\mu_j}\big)_{i,j=1}^{n}}{\prod_{i<j}(x_i-x_j)}. $$

分母由 Vandermonde 公式给出（$\det(x_i^{\,n-j})=\prod_{i<j}(x_i-x_j)$，与 $\det(x_i^{\,j-1})$ 相差 $(-1)^{\binom n2}$，分子分母同乘该符号后相消），代入 $\mu_j=\lambda_j+n-j$ 即得行列式比。再由分子分母在交换 $x_i,x_j$ 时同乘 $-1$，比值不变，即得推论 2。$\square$

## 五、应用与意义

Jacobi–Trudi 恒等式是 Schur 函数理论的枢纽：它把 Schur 函数的组合定义（半标准表）与分析定义（行列式比 / bialternant）以及代数定义（$GL(n)$ 不可约特征标）三者连成一体，并使"对称性"（推论 2）与"正交性"（Hall 内积下 $\langle s_\lambda,s_\mu\rangle=\delta_{\lambda\mu}$）的证明只需一次符号计算。Vandermonde 行列式则是对称多项式、判别式 $\Delta=\prod_{i<j}(x_i-x_j)^2$、Weyl 分母公式、Gelfand–Tsetlin 模式与随机矩阵（$\beta$-系综的联合密度含 Vandermonde 因子）中的基本构件。

具体用途包括：由 $s_{(k)}=h_k$、$s_{(1^k)}=e_k$ 得到 $h,e$ 的 Schur 展开；导出 Giambelli 公式与 Pieri 公式；在表示论中给出 Weyl 特征标公式的组合证明；在可积系统与 Schubert 演算中提供行列式（旗 Schur、双 Schur 函数）的统一表达；在代数组合中与钩长公式、RSK 对应共同完成 $n!=\sum_{\lambda\vdash n}(f^\lambda)^2$ 的两侧计算。
