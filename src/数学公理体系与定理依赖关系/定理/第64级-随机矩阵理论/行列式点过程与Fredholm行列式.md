# 行列式点过程与 Fredholm 行列式

> **一句话大白话**：有一类随机点过程，它的"两点、三点、任意多点同时出现的概率"都能写成一串整齐的行列式；于是"某个区域里一个点都没有"的概率就等于一个无穷维行列式 $\det(I-K)$，可积性由此而来。
>
> **小例子**：GUE 的大特征值不超过 $t$ 的概率为 $\mathbb P(\lambda_{\max}\le t)=\det(I-K_{\mathrm{Ai}})_{L^2(t,\infty)}$，其中 $K_{\mathrm{Ai}}$ 是 Airy 核——这正是 Tracy-Widom 分布的出发点。

## 一、定理介绍

> **前置依赖**：Fredholm二择一定理、正交多项式理论、行列式展开定理、矩阵的迹、控制收敛定理。

行列式点过程（determinantal point process, DPP）是一类由核函数 $K(x,y)$ 完全刻画的点过程：它的各阶相关函数都是 $K$ 的 Grenander 型行列式。Fredholm 行列式则是无穷维算子 $I-K$ 的行列式，其幂级数展开把 $\det(I-K)$ 与算子各阶外幂的迹联系起来。两者的结合给出随机矩阵与可积概率中最有力的公式之一：**点过程避开某个区域 $D$ 的概率等于 $\det(I-K\mathbf 1_D)$**。这条公式把"概率问题"翻译成"算子行列式问题"，使 GUE 最大特征值的分布、随机排列最长递增子序列等问题都能化为对 Fredholm 行列式的渐近分析；Tracy-Widom 分布正是把 Airy 核代入该公式后得到的。

## 二、原理思路

1. 行列式点过程由"相关函数是行列式"来定义，因而其一切概率信息都被核 $K$ 承载。
2. 计算"没有点落进 $D$"的概率，等价于计算生成函数 $\mathbb E\bigl[\prod_i(1-g(x_i))\bigr]$ 在 $g=\mathbf 1_D$ 处的值。
3. 把该期望按点数 $k$ 分组展开，每一项含积分 $\int\det[K(x_i,x_j)]\,dx_1\cdots dx_k$。
4. 用 Gram 行列式与行列式展开定理（Cauchy–Binet 型展开）算出上述积分为 $k!$ 倍的外幂迹 $\operatorname{tr}(\wedge^kK)$。
5. 于是总和恰是 Fredholm 行列式的展开式 $\det(I-K)=\sum_k(-1)^k\operatorname{tr}(\wedge^kK)$，取 $g=\mathbf 1_D$ 即得结论；一般核由有限秩核逼近并用控制收敛定理过渡。

## 三、定理的严格表述

设 $\Lambda\subseteq\mathbb R^d$ 带参考测度 $dx$，$\mathbb P$ 为 $\Lambda$ 上局部有限的点过程，记 $\#(D)$ 为落在 $D$ 中的点数。称 $\mathbb P$ 为核 $K$ 的**行列式点过程**，若对每个 $k\ge1$ 与任意有界可测 $g$，第 $k$ 阶相关函数存在且

$$
\rho_k(x_1,\dots,x_k)=\det\bigl[K(x_i,x_j)\bigr]_{i,j=1}^{k},
$$

其中 $K$ 为 Hermitian 正定核，$\operatorname{tr}K=\int K(x,x)\,dx<\infty$（迹类条件）。

**定理 1（生成函数）**：对任意有界可测 $g$，

$$
\mathbb E\Bigl[\prod_{i:\,x_i\in\Lambda}\bigl(1-g(x_i)\bigr)\Bigr]=\det\bigl(I-gK\bigr),
$$

右端为 $L^2(\Lambda)$ 上的 Fredholm 行列式，其展开为 $\det(I-K)=\sum_{k\ge0}(-1)^k\operatorname{tr}(\wedge^kK)$。

**定理 2（空区概率）**：取 $g=\mathbf 1_D$，得

$$
\mathbb P\bigl(\#(D)=0\bigr)=\det\bigl(I-K\mathbf 1_D\bigr)_{L^2(D)} .
$$

## 四、证明过程

**步骤 1（按点数展开期望）。** 由相关函数的定义，对任意有界可测 $g$ 有基本展开

$$
\mathbb E\Bigl[\prod_i\bigl(1-g(x_i)\bigr)\Bigr]
=\sum_{k\ge0}\frac{(-1)^k}{k!}\int_{\Lambda^k}\det\bigl[K(x_i,x_j)\bigr]\prod_{i=1}^k g(x_i)\,dx_1\cdots dx_k ,
$$

其中 $k=0$ 项为 $1$。这是"相关函数决定点过程"的标准形式：第 $k$ 项度量恰好有 $k$ 个点被 $g$ 计入的概率密度。

**步骤 2（有限秩核的积分公式）。** 先设 $K(x,y)=\sum_{m=1}^{M}\varphi_m(x)\overline{\varphi_m(y)}$，$\{\varphi_m\}_{m=1}^M$ 在 $L^2$ 中标准正交。令 $u(x)=\bigl(\varphi_1(x),\dots,\varphi_M(x)\bigr)$，则 $K(x_i,x_j)=\langle u(x_i),u(x_j)\rangle$ 是 Gram 矩阵元素。记 $U$ 为以 $u(x_1),\dots,u(x_k)$ 为行的 $k\times M$ 矩阵，则 $\det[K(x_i,x_j)]=\det(UU^{*})$。由行列式展开定理按全部 $k$ 阶子式展开（Cauchy–Binet 公式），

$$
\det(UU^{*})=\sum_{|S|=k}\bigl|\det\bigl[\,\varphi_{s}(x_i)\,\bigr]_{i,s\in S}\bigr|^2 .
$$

对 $x_1,\dots,x_k$ 逐变量积分。由 $\{\varphi_m\}$ 的正交性，乘积积分 $\int\varphi_{s}(x_i)\overline{\varphi_{s'}(x_i)}\,dx_i=\delta_{ss'}$，展开两个 $k$ 阶行列式后只有 $S=S'$ 的项存活，于是

$$
\int_{\Lambda^k}\det\bigl[K(x_i,x_j)\bigr]\,dx_1\cdots dx_k
=\sum_{|S|=k}k!
=k!\,\binom{M}{k}
=k!\,\operatorname{tr}\bigl(\wedge^kK\bigr).
$$

最后一步用到 $\wedge^kK$ 在正交基 $\{\varphi_{s_1}\wedge\cdots\wedge\varphi_{s_k}\}$ 下是对角元为 $1$ 的算子（有限秩投影），其迹等于 $\binom{M}{k}$；这也印证了 [矩阵的迹](../第14级-线性代数/矩阵的迹.md) 在此处的用法。

**步骤 3（组装成 Fredholm 行列式）。** 把步骤 2 的公式代入步骤 1 的展开，逐项把 $g$ 吸收进算子（$g$ 有界可测，$g^{1/2}$ 良定义，且 $\operatorname{tr}(g^{1/2}Kg^{1/2})=\int gK(x,x)dx<\infty$，故仍是迹类），得

$$
\mathbb E\Bigl[\prod_i\bigl(1-g(x_i)\bigr)\Bigr]
=\sum_{k\ge0}(-1)^k\operatorname{tr}\bigl(\wedge^k(g^{1/2}Kg^{1/2})\bigr)
=\det\bigl(I-g^{1/2}Kg^{1/2}\bigr)
=\det\bigl(I-gK\bigr).
$$

这里用到了 Fredholm 行列式的幂级数定义，即 $\det(I-A)=\sum_{k\ge0}(-1)^k\operatorname{tr}(\wedge^kA)$；当 $A$ 迹类时该级数绝对收敛，故可逐项与步骤 1 的有限截断比较。

**步骤 4（从有限秩过渡到一般核；空区概率）。** 对一般迹类核 $K$，取一列有限秩核 $K_n\to K$（在迹范数意义下），由 Fredholm二择一定理，$I-K$ 的 Fredholm 行列式存在且 $\det(I-K_n)\to\det(I-K)$；又由控制收敛定理，步骤 1 左端的期望也相应收敛，故定理 1 对一般 $K$ 成立。最后在定理 1 中取 $g=\mathbf 1_D$：此时 $1-g(x_i)$ 对落在 $D$ 内的点取 $0$、对 $D$ 外的点取 $1$，故乘积非零当且仅当 $D$ 中没有点，于是

$$
\mathbb P\bigl(\#(D)=0\bigr)=\det\bigl(I-K\mathbf 1_D\bigr)_{L^2(D)},
$$

这正是所要证明的空区概率公式。

## 五、应用与意义

- **随机矩阵极值**：GUE/GOE/GSE 的特征值构成以 Hermite 多项式核为核的行列式点过程，$\mathbb P(\lambda_{\max}\le t)=\det(I-K)_{L^2(t,\infty)}$，是 Tracy-Widom 分布与谱边缘普适性的出发点。
- **Airy 核与 Painlevé 方程**：把核在谱边缘作 Plancherel–Rotach 渐近得到 Airy 核 $K_{\mathrm{Ai}}$，再对其 Fredholm 行列式作对数导数运算即导出 Painlevé II 方程。
- **可积模型**：随机排列的最长递增子序列、离散随机生长模型、无交缠随机游走等问题的分布都可写成 Fredholm 行列式，进而作渐近分析。
- **统计与机器学习**：行列式点过程被广泛用作"多样性采样"的概率模型，核的选择直接决定点之间的排斥强度。

## 课堂问答

**老师**：说某区域里一个点都没有的概率等于 $\det(I-K)$，这句话为什么成立？

**学生**：因为行列式点过程的第 $k$ 阶相关函数是 $\rho_k(x_1,\dots,x_k)=\det[K(x_i,x_j)]$。取生成函数 $\mathbb E[\prod_i(1-g(x_i))]$ 按点数展开，第 $k$ 项含积分 $\int\det[K(x_i,x_j)]\prod_i g(x_i)\,dx$。用 Gram 行列式与 Cauchy–Binet 展开，该积分恰为 $k!\operatorname{tr}(\wedge^k g K)$，求和即为 Fredholm 展开 $\det(I-gK)=\sum_k(-1)^k\operatorname{tr}(\wedge^k g K)$。取 $g=\mathbf 1_D$ 即得空区概率。

**老师（追问）**：为什么积分 $\int\det[K(x_i,x_j)]\,dx$ 会冒出一个 $k!$ 和外幂的迹？

**学生**：先把核写成有限秩 $K=\sum_m\varphi_m\otimes\overline{\varphi_m}$，则 $[K(x_i,x_j)]$ 是 Gram 矩阵 $UU^*$。按列子式展开（Cauchy–Binet）得 $\det(UU^*)=\sum_{|S|=k}|\det[\varphi_s(x_i)]|^2$。逐变量积分时用正交性 $\int\varphi_s\overline{\varphi_{s'}}=\delta_{ss'}$，两个行列式展开后只剩 $S=S'$ 存活，共 $k!\binom{M}{k}=k!\operatorname{tr}(\wedge^kK)$ 项。一般核用有限秩逼近加控制收敛过渡。

**老师（拓展）**：这个公式直接把什么难题变简单了？

**学生**：把求极值分布的概率变成算算子行列式。例如 GUE 有 $\mathbb P(\lambda_{\max}\le t)=\det(I-K_{\mathrm{Ai}})$ 在 $L^2(t,\infty)$ 上，这正是 Tracy–Widom 分布的出发点；把核作 Plancherel–Rotach 渐近得到 Airy 核后，对其行列式求对数导数即导出 Painlevé II。常见误区是以为必须知道全部相关函数，其实核 $K$ 已承载全部信息。

## 相关条目

- [Tracy-Widom分布](./Tracy-Widom分布.md)：把 Airy 核代入空区概率公式所得到的谱边缘极限分布。
- [正交多项式理论](../第67级-逼近论与样条理论/正交多项式理论.md)：Hermite 核等正交多项式核的一般框架。
- [Fredholm二择一定理](../第31级-泛函分析/Fredholm二择一定理.md)：Fredholm 行列式存在性与逼近性质的算子论基础。
