# Jacobian 行列式

> **一句话大白话**：换元积分时坐标系一换，微元会被拉伸或压扁；$|\det J|$ 就是"局部体积被放大了几倍"的倍数因子，乘上它，积分才不丢不重。

> **小例子**：极坐标换元 $x=r\cos\theta,\ y=r\sin\theta$ 的 Jacobian 行列式绝对值为 $r$，于是 $\iint f(x,y)\,dx\,dy=\iint f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$；多元统计里把 $\boldsymbol{X}$ 换成 $\boldsymbol{W}=\boldsymbol{X}\boldsymbol{X}^\top$ 时，同样靠一个 Jacobian 因子把密度"搬运"过去。

## 一、定理介绍

> **前置依赖**：多元微分与方向导数、线性映射的伸缩与平行体体积、行列式与体积、Cholesky 分解、对称矩阵的谱分解与正交群、Gamma 函数。

Jacobian 行列式（Jacobian determinant）是多元换元积分公式的倍数因子。设 $\phi:U\to\mathbb R^p$ 是光滑坐标变换，其在点 $\boldsymbol{t}$ 处的微分 $J_\phi(\boldsymbol{t})$ 把切空间的单位立方体映为一个平行体，而 $|\det J_\phi(\boldsymbol{t})|$ 正是该平行体与单位立方体的体积之比。因此面积/体积微元满足 $\mathrm{d}\boldsymbol{x}=|\det J|\,\mathrm{d}\boldsymbol{y}$，换元公式据此成立。

这一工具在多元统计分析中无处不在。当随机向量 $\boldsymbol{X}$ 是 $\boldsymbol{Y}$ 的可微变换时，两个密度之间相差一个 Jacobian 因子；Wishart 分布的密度、Hotelling $T^2$ 的分布、多元正态的最大似然估计，都通过矩阵变量换元（线性变换、Cholesky 分解、谱分解）推出。矩阵情形的 Jacobian 往往带幂次因子，例如 Cholesky 换元 $\boldsymbol{A}=\boldsymbol{T}\boldsymbol{T}'$ 的 Jacobian 含 $\prod_i t_{ii}^{p+1-i}$，它在 Wishart 密度中留下 $|\boldsymbol{T}|^{p-m-1}$ 型（等价地 $|\boldsymbol{W}|^{(m-p-1)/2}$ 型）幂次。

## 二、原理思路

1. **局部线性化**：$\phi$ 在小邻域内近似为其微分 $J_\phi$，而线性映射把单位立方体（体积 $1$）映为体积 $|\det J_\phi|$ 的平行体。

2. **体积伸缩因子**：$|\det J_\phi|$ 就是局部体积的放大倍数；$\det J_\phi=0$ 处映射退化，故要求 Jacobian 处处非零以保证不丢失体积信息。

3. **拼接**：用单位分解把区域分块，逐块用局部线性化，主项相加即得全局换元公式。

4. **密度变换**：若 $\boldsymbol{X}=\phi(\boldsymbol{Y})$，则 $\boldsymbol{X}$ 的密度为 $\boldsymbol{Y}$ 的密度乘上逆变换的 Jacobian 绝对值，这就是概率论中"变量代换法"的全部内容。

5. **矩阵换元**：对矩阵变量，按独立元素计数可验证维数匹配，再用分块递推（Cholesky）或一阶扰动（谱分解）算出幂次型 Jacobian。

## 三、定理的严格表述

**定理（多元换元公式）**：设 $U\subset\mathbb R^p$ 为开集，$\phi:U\to\mathbb R^p$ 是 $C^1$ 单射，且 $\det J_\phi(\boldsymbol{y})\neq0$ 对一切 $\boldsymbol{y}\in U$ 成立（此处 $J_\phi$ 为 $\phi$ 的 Jacobi 矩阵）。若 $f$ 在 $\phi(U)$ 上可积，则
$$
\int_{\phi(U)} f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}=\int_{U} f\bigl(\phi(\boldsymbol{y})\bigr)\,\lvert\det J_\phi(\boldsymbol{y})\rvert\,\mathrm{d}\boldsymbol{y}.
$$

**推论（密度变换）**：设 $\boldsymbol{Y}$ 有密度 $g$，$\boldsymbol{X}=\phi(\boldsymbol{Y})$，$\phi$ 满足上述条件，则 $\boldsymbol{X}$ 有密度
$$
f_{\boldsymbol{X}}(\boldsymbol{x})=g\bigl(\phi^{-1}(\boldsymbol{x})\bigr)\,\bigl\lvert\det J_{\phi^{-1}}(\boldsymbol{x})\bigr\rvert .
$$

**命题（Cholesky 换元的 Jacobian）**：设 $\boldsymbol{A}=\boldsymbol{T}\boldsymbol{T}'$，其中 $\boldsymbol{T}=(t_{ij})$ 为 $p\times p$ 下三角矩阵且对角元 $t_{ii}>0$。则
$$
\mathrm{d}\boldsymbol{A}=2^p\prod_{i=1}^{p} t_{ii}^{\,p+1-i}\,\mathrm{d}\boldsymbol{T}.
$$
（若写成 $\boldsymbol{A}=\boldsymbol{T}'\boldsymbol{T}$ 且 $\boldsymbol{T}$ 上三角，同样得到 $\prod_i t_{ii}^{p+1-i}$。）

**命题（谱分解换元的 Jacobian）**：设 $\boldsymbol{A}=\boldsymbol{O}\boldsymbol{\Lambda}\boldsymbol{O}'$，$\boldsymbol{O}$ 正交、$\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_p)$。则（在某归一化常数 $c_p$ 意义下）
$$
\mathrm{d}\boldsymbol{A}=c_p\prod_{i<j}\lvert\lambda_i-\lambda_j\rvert\,\mathrm{d}\boldsymbol{\Lambda}\,\mathrm{d}\boldsymbol{O},
$$
其中 $\mathrm{d}\boldsymbol{O}$ 为 $\mathrm{O}(p)$ 上的 Haar 测度。

**应用（Wishart 密度中的因子）**：设 $\boldsymbol{W}=\boldsymbol{T}'\boldsymbol{T}$，$\boldsymbol{T}$ 为 $p\times p$ 上三角、对角元为正，则 $\lvert\boldsymbol{W}\rvert^{1/2}=\det\boldsymbol{T}=\lvert\boldsymbol{T}\rvert$，故密度里的 $\lvert\boldsymbol{W}\rvert^{(n-p-1)/2}$ 恰等于 $\lvert\boldsymbol{T}\rvert^{n-p-1}$；记矩阵维数为 $p$、样本数为 $m=n$，该幂次即文献中的 $p-m-1$ 型因子。

## 四、证明过程

**步骤 1（一维原型与局部线性化）。** 一维情形即链式法则：$\int_{\phi(a)}^{\phi(b)} f(x)\,dx=\int_a^b f(\phi(t))\lvert\phi'(t)\rvert\,dt$，其 Jacobian 为 $\lvert\phi'\rvert$。高维时，取 $\boldsymbol{t}_0\in U$，由可微性 $\phi(\boldsymbol{t})=\phi(\boldsymbol{t}_0)+J_\phi(\boldsymbol{t}_0)(\boldsymbol{t}-\boldsymbol{t}_0)+o(\lVert\boldsymbol{t}-\boldsymbol{t}_0\rVert)$。对以 $\boldsymbol{t}_0$ 为中心、边长 $h$ 的小立方体 $Q$，$\phi(Q)$ 与平行体 $J_\phi(\boldsymbol{t}_0)(Q)+\phi(\boldsymbol{t}_0)$ 的体积之比随 $h\to0$ 趋于 $1$。而 $\operatorname{Vol}\bigl(J_\phi(\boldsymbol{t}_0)(Q)\bigr)=\lvert\det J_\phi(\boldsymbol{t}_0)\rvert\,h^p$，故小体元被放大的倍数趋于 $\lvert\det J_\phi\rvert$。

**步骤 2（拼接得全局公式）。** 用单位分解或把 $U$ 分成充分小的小块，使 $\phi$ 在每块上接近线性；在每个小块上用步骤 1 的近似，误差为 $o(\text{块体积})$。令分割的网眼趋于 $0$，近似式的 Riemann 和收敛，误差项趋于 $0$，即得换元公式。$\square$

**步骤 3（线性换元）。** 若 $\phi(\boldsymbol{y})=\boldsymbol{B}\boldsymbol{y}$，则 $J_\phi=\boldsymbol{B}$ 为常矩阵，$\lvert\det J_\phi\rvert=\lvert\det\boldsymbol{B}\rvert$。作为特例，$\boldsymbol{W}=\boldsymbol{B}\boldsymbol{X}$ 的密度变换给出 $\lvert\det\boldsymbol{B}\rvert$ 因子；Wishart 中一般协方差 $\boldsymbol{\Sigma}$ 的情形即由此得到 $|\boldsymbol{\Sigma}|^{n/2}$ 因子。

**步骤 4（Cholesky Jacobian 的归纳）。** $\boldsymbol{T}$ 与对称矩阵 $\boldsymbol{A}$ 的独立元素个数同为 $p(p+1)/2$，故可作坐标换元。按分块递推：写
$$
\boldsymbol{T}=\begin{pmatrix}\boldsymbol{T}_{p-1} & \boldsymbol{0}\\ \boldsymbol{t}^\top & t_{pp}\end{pmatrix},\qquad
\boldsymbol{A}=\boldsymbol{T}\boldsymbol{T}'=\begin{pmatrix}\boldsymbol{A}_{p-1} & \boldsymbol{a}\\ \boldsymbol{a}^\top & a_{pp}\end{pmatrix},
$$
其中 $\boldsymbol{A}_{p-1}=\boldsymbol{T}_{p-1}\boldsymbol{T}_{p-1}'$ 只依赖 $\boldsymbol{T}_{p-1}$，故其 Jacobian 由归纳假设给出；末列给出 $\boldsymbol{a}=\boldsymbol{T}_{p-1}\boldsymbol{t}$、$a_{pp}=\boldsymbol{t}^\top\boldsymbol{t}+t_{pp}^2$，映射 $\boldsymbol{t}\mapsto\boldsymbol{a}$ 的 Jacobian 为 $\det\boldsymbol{T}_{p-1}=\prod_{i=1}^{p-1}t_{ii}$，而 $t_{pp}\mapsto a_{pp}$ 还贡献因子 $2t_{pp}$。故从 $p-1$ 到 $p$，Jacobian 乘以 $2t_{pp}\prod_{i=1}^{p-1}t_{ii}$，于是每个 $t_{ii}$ 的幂次加 $1$。以 $p=1$（$\mathrm{d}a_{11}=2t_{11}\mathrm{d}t_{11}$）为基，递推得 $\mathrm{d}\boldsymbol{A}=2^p\prod_{i=1}^p t_{ii}^{p+1-i}\,\mathrm{d}\boldsymbol{T}$。$\square$

**步骤 5（谱分解 Jacobian 的扰动计算）。** 对 $\boldsymbol{A}(t)=\boldsymbol{A}+t\boldsymbol{E}$ 作一阶扰动。由 $\boldsymbol{A}=\boldsymbol{O}\boldsymbol{\Lambda}\boldsymbol{O}'$ 得 $\delta\boldsymbol{A}=\boldsymbol{O}\,\delta\boldsymbol{\Lambda}\,\boldsymbol{O}'+\boldsymbol{O}\,[\boldsymbol{\Omega},\boldsymbol{\Lambda}]\,\boldsymbol{O}'$，其中 $\boldsymbol{\Omega}=\boldsymbol{O}'\delta\boldsymbol{O}$ 为反对称（$\boldsymbol{O}$ 的 Lie 代数元素）。把 $\boldsymbol{A}$ 的元素按对称性取独立分量考察：沿对称方向 $\delta\boldsymbol{\Lambda}$ 的贡献是对角放缩，而反对称方向 $[\boldsymbol{\Omega},\boldsymbol{\Lambda}]$ 的对角为零、$(i,j)$ 分量为 $(\lambda_j-\lambda_i)\Omega_{ij}$。于是把 $\mathrm{d}\boldsymbol{A}$ 写成 $(\mathrm{d}\boldsymbol{\Lambda},\boldsymbol{\Omega})$ 的线性组合时，其系数矩阵按 $\Lambda$ 的对角化基下呈块结构，行列式的模为 $\prod_{i<j}\lvert\lambda_i-\lambda_j\rvert$（再乘上 $\boldsymbol{O}$ 上的 Haar 归一化常数）。当特征值互异时该 Jacobian 非零，换元公式适用。$\square$

**步骤 6（Wishart 密度中的应用）。** 从 $\boldsymbol{X}$ 的密度（$n\times p$ 数据阵，标准情形）出发，作换元 $\boldsymbol{X}=\boldsymbol{U}\boldsymbol{T}$（$\boldsymbol{U}\in V_{n,p}$ 取自 Stiefel 流形，$\boldsymbol{T}$ 上三角），其 Jacobian 为 $\prod_{i=1}^p t_{ii}^{n-i}$；再把 $\boldsymbol{W}=\boldsymbol{T}'\boldsymbol{T}$ 代入。由于 $\lvert\boldsymbol{W}\rvert^{1/2}=\det\boldsymbol{T}$，指数部分 $\exp(-\tfrac12\operatorname{tr}\boldsymbol{W})$ 不变，而幂次部分由 $\prod_i t_{ii}^{n-i}$ 与换元的幂次合并为 $\lvert\boldsymbol{T}\rvert^{n-p-1}=\lvert\boldsymbol{W}\rvert^{(n-p-1)/2}$，这正是 Wishart 密度的幂次指数。至此 Jacobian 因子完成了从 $\boldsymbol{X}$ 到 $\boldsymbol{W}$ 的密度搬运。$\square$

## 五、应用与意义

- **概率密度的变换**：一切"随机变量函数的分布"公式（包括和、积、商的密度）都是 Jacobian 公式的直接应用。
- **多元统计分析**：Wishart 密度、Hotelling $T^2$ 检验、Wilks $\Lambda$ 分布的推导都依赖矩阵换元的 Jacobian，尤其是 Cholesky 与谱分解两种标准化换元。
- **最大似然与信息几何**：Fisher 信息矩阵、参数的坐标变换、先验分布的 Jeffreys 先验 $(\det I)^{1/2}$ 都与 Jacobian 的变换律密切相关。
- **主成分与降维**：谱分解换元的 Jacobian $\prod_{i<j}(\lambda_i-\lambda_j)$ 解释了为什么特征值会"相互排斥"，是随机矩阵与主成分分析的理论基础。
- **数值积分与采样**：蒙特卡洛中的变量代换、球坐标与极坐标采样、超球面上的均匀采样，都需以 Jacobian 因子修正权重。
- **流形上的积分**：把一个流形的积分通过坐标卡拉到 $\mathbb R^p$ 时，Jacobian 是转移积分与体积元的通用机制，是微分几何中体积形式的技术核心。
