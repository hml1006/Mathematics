# 预解恒等式（Resolvent 恒等式）

> **一句话大白话**：同一个算子在两个不同参数处的两个"逆"相减，等于它们相乘再乘上参数之差——于是"逆的差"这条非线性信息被化成了"逆的乘积"，可以逐项展开、求导、做估计。

> **小例子**：取 $T=0$，则 $R(\lambda)=\lambda^{-1}I$，直接算出 $R(\lambda)-R(\mu)=\big(\tfrac1\lambda-\tfrac1\mu\big)I=\tfrac{\mu-\lambda}{\lambda\mu}I=(\mu-\lambda)R(\lambda)R(\mu)$，与恒等式完全吻合。

## 一、定理介绍

> **前置依赖**：C星代数定义与基本性质、谱半径公式、谱映射定理、vonNeumann代数基础、Hilbert 空间上有界算子与算子范数、Neumann 级数。

预解恒等式（resolvent identity，又称第一预解恒等式）是谱理论中最朴素的代数恒等式，历史几乎与预解式概念同龄：Hilbert 在 1900 年代研究积分方程时引入预解核 $(\lambda I-T)^{-1}$ 并发现它满足这一恒等式，Gelfand 学派随后把它提升为 Banach 代数的结构性工具。

它重要，是因为"可逆"是非线性条件，谱 $\sigma(T)$ 由它定义而难以直接操作；预解恒等式把两个逆算子之差写成逆算子之积这一纯代数表达式，使预解映射 $\lambda\mapsto R(\lambda)$ 的连续性、解析性、各阶导数，以及"谱是闭集""谱半径公式"等结论都能由它推出。它还是扰动理论（第二预解恒等式）、散射理论、Kato–Rellich 定理、谱投影与 Riesz 演算的计算起点，在算子代数中用于构造解析演算与 KMS 态相关的解析延拓。

## 二、原理思路

1. **纯代数来源**：对两个可逆元 $A=\lambda I-T$、$B=\mu I-T$，注意 $A-B=(\lambda-\mu)I$ 是纯量，于是 $A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}=(\mu-\lambda)R(\lambda)R(\mu)$。整个推导不含分析工具，只需"可逆元之积可逆"。

2. **交换性**：由于 $A$ 与 $B$ 都是 $T$ 的一次多项式，$AB=BA$，故 $R(\lambda)R(\mu)=R(\mu)R(\lambda)$，两种因子次序的写法等价。

3. **由恒等式到解析性**：把 $\lambda$ 移到 $\mu$ 附近，恒等式给出 $R(\lambda)=R(\mu)-(\lambda-\mu)R(\lambda)R(\mu)$，解出 $R(\lambda)=\big(I+(\lambda-\mu)R(\mu)\big)^{-1}R(\mu)$，展开成 Neumann 级数即得局部幂级数展开，从而解析并有导数 $R'(\lambda)=-R(\lambda)^2$。

## 三、定理的严格表述

设 $A$ 是含单位元 $I$ 的复 Banach 代数（例如 Hilbert 空间 $\mathcal H$ 上的有界算子代数 $B(\mathcal H)$），$T\in A$。称
$$
\rho(T)=\{\lambda\in\mathbb C:\lambda I-T\ \text{可逆}\}
$$
为 $T$ 的**预解集**，$\sigma(T)=\mathbb C\setminus\rho(T)$ 为**谱**，并对 $\lambda\in\rho(T)$ 记
$$
R(\lambda)=(\lambda I-T)^{-1}\in A
$$
为**预解算子**。则对任意 $\lambda,\mu\in\rho(T)$ 成立：

（1）第一预解恒等式：
$$
R(\lambda)-R(\mu)=(\mu-\lambda)R(\lambda)R(\mu)=(\mu-\lambda)R(\mu)R(\lambda);
$$

（2）等价形式（$\lambda\ne\mu$）：
$$
R(\lambda)R(\mu)=\frac{R(\mu)-R(\lambda)}{\mu-\lambda};
$$

（3）预解算子彼此交换：$R(\lambda)R(\mu)=R(\mu)R(\lambda)$；

（4）局部展开与导数：当 $|\lambda-\mu|<\|R(\mu)\|^{-1}$ 时
$$
R(\lambda)=\sum_{k=0}^{\infty}(-1)^k(\lambda-\mu)^k R(\mu)^{k+1},\qquad R'(\lambda)=-R(\lambda)^2 .
$$

**推论**：$\rho(T)$ 是开集、$\sigma(T)$ 是紧集，且 $\lambda\mapsto R(\lambda)$ 在 $\rho(T)$ 上解析。

## 四、证明过程

**步骤 1（代数推导第一预解恒等式）。** 令 $A=\lambda I-T$，$B=\mu I-T$，二者在对应参数属于 $\rho(T)$ 时可逆。注意
$$
A-B=(\lambda I-T)-(\mu I-T)=(\lambda-\mu)I .
$$
对可逆元使用恒等式 $A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}$（右端 $=A^{-1}BB^{-1}-A^{-1}AB^{-1}=A^{-1}-B^{-1}$，直接验证成立），代入 $B-A=(\mu-\lambda)I$，得
$$
R(\lambda)-R(\mu)=A^{-1}-B^{-1}=A^{-1}(\mu-\lambda)B^{-1}=(\mu-\lambda)R(\lambda)R(\mu).
$$

**步骤 2（交换性）。** 由 $A$ 与 $B$ 都是 $T$ 的一次多项式，$AB=BA$。对等式两端取逆：$(AB)^{-1}=(BA)^{-1}$，而 $(AB)^{-1}=B^{-1}A^{-1}$、$(BA)^{-1}=A^{-1}B^{-1}$，故 $B^{-1}A^{-1}=A^{-1}B^{-1}$，即 $R(\mu)R(\lambda)=R(\lambda)R(\mu)$。于是步骤 1 中两种因子次序都成立，并给出（2）式。

**步骤 3（局部幂级数展开与连续性）。** 固定 $\mu\in\rho(T)$，记 $\delta=\lambda-\mu$。由 $\lambda I-T=(\mu I-T)+\delta I=(\mu I-T)\big(I+\delta R(\mu)\big)$ 及乘积的可逆性，
$$
R(\lambda)=\big(I+\delta R(\mu)\big)^{-1}R(\mu).
$$
当 $|\delta|\,\|R(\mu)\|<1$ 时 $\|\delta R(\mu)\|<1$，Neumann 级数 $\sum_{k\ge0}\big(-\delta R(\mu)\big)^{k}$ 在范数下收敛到 $\big(I+\delta R(\mu)\big)^{-1}$，故
$$
R(\lambda)=\sum_{k=0}^{\infty}(-\delta)^k R(\mu)^{k+1}=\sum_{k=0}^{\infty}(-1)^k(\lambda-\mu)^k R(\mu)^{k+1}.
$$
该级数在圆盘 $|\lambda-\mu|<\|R(\mu)\|^{-1}$ 内收敛，故 $R$ 在 $\mu$ 附近可展为幂级数，特别在 $\mu$ 连续。$\rho(T)$ 中每点都有这样的邻域，故 $\rho(T)$ 是开集、$\sigma(T)$ 是闭集，且 $R$ 在 $\rho(T)$ 上解析。

**步骤 4（导数公式）。** 由步骤 1，
$$
\frac{R(\lambda)-R(\mu)}{\lambda-\mu}=\frac{(\mu-\lambda)R(\lambda)R(\mu)}{\lambda-\mu}=-R(\lambda)R(\mu).
$$
令 $\lambda\to\mu$，由步骤 3 的连续性 $R(\lambda)\to R(\mu)$，得 $R'(\mu)=-R(\mu)^2$，即 $R'(\lambda)=-R(\lambda)^2$。

**步骤 5（紧性）。** 由 Neumann 级数知 $|\lambda|>\|T\|$ 时 $\lambda\in\rho(T)$ 且 $\|R(\lambda)\|\le(|\lambda|-\|T\|)^{-1}\to0$，故 $\sigma(T)\subseteq\{|\lambda|\le\|T\|\}$ 有界；又 $\sigma(T)$ 闭，故紧。$\square$

## 五、应用与意义

- **解析演算的骨架**：预解映射的解析性是谱投影、Riesz 演算与 Gelfand 变换的定义基础，由此可把全纯函数演算写成围道积分 $f(T)=\frac{1}{2\pi i}\oint f(\lambda)R(\lambda)\,d\lambda$。
- **谱半径公式的输入**：由无穷远 Laurent 展开 $R(\lambda)=\sum_{n\ge0}T^n\lambda^{-n-1}$ 可直接推出 $\limsup_n\|T^n\|^{1/n}\le r(T)$，这是谱半径公式证明中估计上界的关键一步。
- **扰动理论**：第二预解恒等式 $R_1(\lambda)-R_2(\lambda)=R_1(\lambda)(T_2-T_1)R_2(\lambda)$ 由此恒等式变形而来，是 Kato–Rellich 定理、解析扰动与散射理论中波算子构造的出发点。
- **算子代数与量子理论**：在 von Neumann 代数与 $C^*$-代数中用于证明谱的非空性、正规元的范数等于谱半径（$\|T\|=r(T)$），以及 Tomita–Takesaki 模理论中解析延拓的估计。
- **数值线性代数**：迭代法收敛性与 Krylov 方法（Arnoldi/GMRES）的残差递推，本质上是预解式在离散参数处的版本。

## 相关条目

- [谱半径公式](./谱半径公式.md)：其证明中预解算子的无穷远展开与解析性正是本恒等式的直接推论。
- [谱映射定理](./谱映射定理.md)：与本恒等式同为谱论支柱，一个给出谱的代数变换，一个给出预解映射的解析结构。
- [Gelfand-Mazur定理](./Gelfand-Mazur定理.md)：其证明用预解恒等式建立 $R(\lambda)$ 的解析性与有界性。
- [Fekete引理](./Fekete引理.md)：与预解恒等式配合，在谱半径公式中分别负责极限存在与上界估计。
- [C星代数定义与基本性质](./C星代数定义与基本性质.md)：预解恒等式在一般 $C^*$-代数范数下的成立性是谱论推广的起点。
