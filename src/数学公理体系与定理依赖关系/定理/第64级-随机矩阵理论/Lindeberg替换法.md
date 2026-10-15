# Lindeberg 替换法

> **一句话大白话**：要证明随机变量之和趋于正态，可以一次只把一个变量换成同方差的高斯变量，逐项估计误差；误差由三阶矩控制，全部替换完毕后和就变成了正态。
>
> **小例子**：独立同分布、均值 $0$、方差 $1$、三阶矩有限时，取 $Y_i\sim N(0,1)$ 且相互独立，则对三次可导的 $h$，两和的期望之差被 $\frac{\lvert h'''\rvert_\infty}{2}\,n^{-1/2}\,\mathbb E\lvert X\rvert^3$ 控制，这正是 Berry–Esseen 型收敛速度 $O(n^{-1/2})$ 的定量来源。

## 一、定理介绍

> **前置依赖**：四矩匹配定理、中心极限定理、特征函数唯一性定理、Taylor 展开与矩方法、截断与尾部估计（概念）、鞅差中心极限定理。

Lindeberg 替换法（Lindeberg's replacement method，又称 swapping / replacement trick）由 Jarl Waldemar Lindeberg 在 1922 年提出，用于给出中心极限定理的一个初等而可定量的证明。其核心动作是：把目标随机变量和与一个同方差的高斯和作比较，并且一次只替换一个变量，把两和之差写成 $n$ 个"单变量差异"之和，每个差异用三次 Taylor 展开估计，二次项因同均值同方差而精确抵消，余项被三阶矩控制。

1960 年代 Trotter 把这一技巧整理为一般工具（用于讨论测度在拓扑下的光滑逼近）；2010 年前后，Tao–Vu 与 Erdős–Schlein–Yau 等人把替换法发展为证明随机矩阵普适性的主力技术：对 Wigner 矩阵的每个元素作替换，把一般系综与高斯系综作比较，配合四矩匹配定理即得半圆律与局部半圆律的普适性。

定理的意义有三层。其一，它给出定量 CLT（Berry–Esseen 型界）与局部 CLT 的可推广技术。其二，它把 CLT 从独立情形推广到局部依赖、鞅差与图上随机变量的情形，因为"逐点替换 + 局部估计"不要求特征函数的解析工具。其三，它是随机矩阵理论中"从高斯到一般"的普适性桥梁，是四矩匹配定理得以发挥作用的引擎。

## 二、原理思路

1. **逐项替换的构造**：设 $X_{n,1},\dots,X_{n,n}$ 独立、均值 $0$、方差和 $\sum_k\sigma_{n,k}^2=1$；取同方差独立高斯 $Y_{n,k}\sim N(0,\sigma_{n,k}^2)$。定义中间和 $S^{(k)}$：前 $k$ 项用高斯、后 $n-k$ 项用原变量。

2. **望远镜求和**：$\mathbb Eh(S_n)-\mathbb Eh(N(0,1))=\sum_{k=1}^n\big(\mathbb Eh(S^{(k-1)})-\mathbb Eh(S^{(k)})\big)$，误差分摊到每一步"只换一个变量"上。

3. **三次 Taylor 展开**：把一个 $X$ 换成 $Y$ 时，其余变量 $Z$ 固定，展开三项；一阶项因同均值、二阶项因同方差而抵消，三阶项由高斯对称性（$\mathbb EY^3=0$）与 $X$ 的三阶矩控制。

4. **截断与尾部**：三阶矩可能发散，故先把变量截断到 $\lvert X\rvert\leq\varepsilon$；截断误差用 Lindeberg 条件（截断二阶矩）与 Chebyshev 不等式控制，最后令 $\varepsilon\to0$。

5. **推广到随机矩阵**：把每个矩阵元素作替换，误差由元素的矩与 resolvent 的局部化估计控制；四矩匹配保证高斯与一般系综的差异在高阶消失，从而把高斯系综的普适性传给一般系综。

## 三、定理的严格表述

**定理（Lindeberg 中心极限定理）**：对每个 $n$，设 $X_{n,1},\dots,X_{n,n}$ 相互独立，$\mathbb EX_{n,k}=0$，$\sigma_{n,k}^2=\operatorname{Var}X_{n,k}$，且
$$\sum_{k=1}^n\sigma_{n,k}^2=1 .$$
若 Lindeberg 条件成立，即对一切 $\varepsilon>0$
$$\lim_{n\to\infty}\sum_{k=1}^n\mathbb E\big[X_{n,k}^2\,\mathbf 1_{\{\lvert X_{n,k}\rvert>\varepsilon\}}\big]=0,$$
则
$$S_n:=\sum_{k=1}^nX_{n,k}\ \Longrightarrow\ N(0,1).$$

**替换引理（定量形式）**：设 $X,Y$ 独立、$\mathbb EX=\mathbb EY$、$\operatorname{Var}X=\operatorname{Var}Y$，$Z$ 独立于 $X,Y$，$h\in C^3(\mathbb R)$ 且 $\lVert h'''\rVert_\infty<\infty$。则
$$\big\lvert\mathbb Eh(Z+X)-\mathbb Eh(Z+Y)\big\rvert\leq\frac{\lVert h'''\rVert_\infty}{6}\big(\mathbb E\lvert X\rvert^3+\mathbb E\lvert Y\rvert^3\big).$$
特别地，若 $Y\sim N(0,\sigma^2)$、$\sigma^2=\operatorname{Var}X$，则
$$\big\lvert\mathbb Eh(Z+X)-\mathbb Eh(Z+Y)\big\rvert\leq\frac{\lVert h'''\rVert_\infty}{2}\,\mathbb E\lvert X\rvert^3 .$$
**求和形式（定量 CLT）**：在定理的条件下，
$$\big\lvert\mathbb Eh(S_n)-\mathbb Eh(N(0,1))\big\rvert\leq\frac{\lVert h'''\rVert_\infty}{2}\sum_{k=1}^n\mathbb E\lvert X_{n,k}\rvert^3 .$$
（若 $\sum_k\mathbb E\lvert X_{n,k}\rvert^3\leq\beta_n$，即得 Berry–Esseen 型的 $O(\beta_n)$ 界。）

**随机矩阵版本**：设 $W_n=n^{-1/2}(x_{ij})$ 为实对称 Wigner 矩阵，$G_n=n^{-1/2}(g_{ij})$ 为同方差高斯 Wigner 矩阵，且前四阶矩匹配（$\mathbb Ex_{ij}=\mathbb Eg_{ij}$、$\mathbb Ex_{ij}^2=\mathbb Eg_{ij}^2$、$\mathbb Ex_{ij}^4=\mathbb Eg_{ij}^4$）。则在适当的矩与局部化假设下，对每个 $k$ 存在 $c_k>0$ 使光滑检验函数 $h$ 满足
$$\big\lvert\mathbb Eh(W_n)-\mathbb Eh(G_n)\big\rvert\leq C_k\,n^{-c_k}\,\lVert h\rVert_{C^k},$$
从而由高斯情形的 Wigner 半圆律推出一般系综的半圆律（普适性）。

## 四、证明过程

**步骤 1（逐项替换的构造与望远镜求和）。** 设 $X_{n,k}$ 独立、$\mathbb EX_{n,k}=0$、$\operatorname{Var}X_{n,k}=\sigma_{n,k}^2$、$\sum_k\sigma_{n,k}^2=1$。取独立高斯 $Y_{n,k}\sim N(0,\sigma_{n,k}^2)$，且所有 $Y_{n,k}$ 与所有 $X_{n,j}$ 相互独立。定义
$$S^{(k)}=\sum_{i=1}^{k}Y_{n,i}+\sum_{i=k+1}^{n}X_{n,i},\qquad k=0,1,\dots,n .$$
则 $S^{(0)}=S_n$、$S^{(n)}=\sum_kY_{n,k}\sim N(0,1)$。对任意有界可测 $h$，
$$\mathbb Eh(S_n)-\mathbb Eh(N(0,1))=\sum_{k=1}^{n}\Big(\mathbb Eh\big(S^{(k-1)}\big)-\mathbb Eh\big(S^{(k)}\big)\Big).$$

**步骤 2（替换引理：三次 Taylor 展开）。** 固定 $k$，令
$$Z=S^{(k-1)}-X_{n,k}=S^{(k)}-Y_{n,k},$$
即除去第 $k$ 项之外的和；$Z$ 与 $X_{n,k}$、$Y_{n,k}$ 独立。于是
$$\mathbb Eh\big(S^{(k-1)}\big)-\mathbb Eh\big(S^{(k)}\big)=\mathbb E\Big[h\big(Z+X_{n,k}\big)-h\big(Z+Y_{n,k}\big)\Big].$$
对 $h$ 在 $Z$ 处作三次 Taylor 展开（带 Lagrange 余项）：
$$h(Z+T)=h(Z)+h'(Z)T+\tfrac12h''(Z)T^2+\tfrac16h'''(\xi_T)T^3 .$$
分别取 $T=X_{n,k}$ 与 $T=Y_{n,k}$ 的期望再相减。利用 $X_{n,k},Y_{n,k}$ 独立于 $Z$ 及矩条件
$$\mathbb EX_{n,k}=\mathbb EY_{n,k}=0,\qquad \mathbb EX_{n,k}^2=\mathbb EY_{n,k}^2=\sigma_{n,k}^2,\qquad \mathbb EY_{n,k}^3=0\ (\text{高斯对称}),$$
一阶项与二阶项在相减时精确抵消，故只剩
$$\big\lvert\mathbb Eh(S^{(k-1)})-\mathbb Eh(S^{(k)})\big\rvert\leq\frac{\lVert h'''\rVert_\infty}{6}\Big(\mathbb E\lvert X_{n,k}\rvert^3+\mathbb E\lvert Y_{n,k}\rvert^3\Big).$$
又由 Lyapunov 不等式 $\sigma_{n,k}^3=(\mathbb EX_{n,k}^2)^{3/2}\leq\mathbb E\lvert X_{n,k}\rvert^3$ 与高斯矩公式 $\mathbb E\lvert Y\rvert^3=2\sqrt{2/\pi}\,\sigma^3\leq2\sigma^3$，得 $\mathbb E\lvert Y_{n,k}\rvert^3\leq2\mathbb E\lvert X_{n,k}\rvert^3$，于是
$$\big\lvert\mathbb Eh(S^{(k-1)})-\mathbb Eh(S^{(k)})\big\rvert\leq\frac{\lVert h'''\rVert_\infty}{2}\,\mathbb E\lvert X_{n,k}\rvert^3 .$$
对 $k=1,\dots,n$ 求和即得替换引理与定量 CLT 的界。

**步骤 3（截断与尾部控制）。** Lindeberg 条件下 $\sum_k\mathbb E\lvert X_{n,k}\rvert^3$ 未必趋于 $0$，故先截断。取 $\varepsilon>0$，令
$$\hat X_{n,k}=X_{n,k}\mathbf 1_{\{\lvert X_{n,k}\rvert\leq\varepsilon\}}-\mathbb E\big[X_{n,k}\mathbf 1_{\{\lvert X_{n,k}\rvert\leq\varepsilon\}}\big],$$
则 $\mathbb E\hat X_{n,k}=0$ 且 $\lvert\hat X_{n,k}\rvert\leq2\varepsilon$ 几乎必然。逐项估计截断误差：
$$\mathbb E\big\lvert X_{n,k}-\hat X_{n,k}\big\rvert\leq2\,\mathbb E\big[\lvert X_{n,k}\rvert\mathbf 1_{\{\lvert X_{n,k}\rvert>\varepsilon\}}\big]\leq\frac{2}{\varepsilon}\,\mathbb E\big[X_{n,k}^2\mathbf 1_{\{\lvert X_{n,k}\rvert>\varepsilon\}}\big],$$
后一步用事件上 $\lvert X_{n,k}\rvert\leq\varepsilon^{-1}X_{n,k}^2$。求和并由 Lindeberg 条件得
$$\sum_{k=1}^n\mathbb E\big\lvert X_{n,k}-\hat X_{n,k}\big\rvert\ \longrightarrow\ 0 .$$
于是对任意 $\delta>0$，由 Chebyshev 不等式（一阶矩形式）
$$\mathbb P\Big(\Big\lvert\sum_{k}\big(X_{n,k}-\hat X_{n,k}\big)\Big\rvert>\delta\Big)\leq\frac{1}{\delta}\sum_{k}\mathbb E\big\lvert X_{n,k}-\hat X_{n,k}\big\rvert\ \longrightarrow\ 0 ,$$
故 $\sum_k\hat X_{n,k}$ 与 $S_n$ 在概率意义下渐近相同。又
$$\Big\lvert\sum_k\operatorname{Var}\hat X_{n,k}-1\Big\rvert\leq\sum_k\mathbb E\big[X_{n,k}^2\mathbf 1_{\{\lvert X_{n,k}\rvert>\varepsilon\}}\big]+\sum_k\Big(\mathbb E\big[X_{n,k}\mathbf 1_{\{\lvert X_{n,k}\rvert>\varepsilon\}}\big]\Big)^2\ \longrightarrow\ 0 ,$$
故标准化因子 $\lambda_n:=\big(\sum_k\operatorname{Var}\hat X_{n,k}\big)^{-1/2}$ 满足 $\lambda_n\to1$，且把 $\hat X_{n,k}$ 乘以 $\lambda_n$ 后方差和恰为 $1$；该缩放的附加误差由 $\lVert h'\rVert_\infty\lvert\lambda_n-1\rvert\sum_k\mathbb E\lvert\hat X_{n,k}\rvert$ 控制并趋于 $0$。

**步骤 4（截断变量上的替换估计）。** 记 $\tilde X_{n,k}=\lambda_n\hat X_{n,k}$。则 $\tilde X_{n,k}$ 独立、均值 $0$、$\sum_k\operatorname{Var}\tilde X_{n,k}=1$、$\lvert\tilde X_{n,k}\rvert\leq2\lambda_n\varepsilon=:M_n$。由步骤 2 的替换引理，
$$\big\lvert\mathbb Eh\big(\textstyle\sum_k\tilde X_{n,k}\big)-\mathbb Eh(N(0,1))\big\rvert\leq\frac{\lVert h'''\rVert_\infty}{2}\sum_k\mathbb E\lvert\tilde X_{n,k}\rvert^3 .$$
而由 $\lvert\tilde X_{n,k}\rvert\leq M_n$ 得 $\lvert\tilde X_{n,k}\rvert^3\leq M_n\lvert\tilde X_{n,k}\rvert^2$，故
$$\sum_k\mathbb E\lvert\tilde X_{n,k}\rvert^3\leq M_n\sum_k\mathbb E\big\lvert\tilde X_{n,k}\big\rvert^2=M_n\cdot 1=2\lambda_n\varepsilon .$$
于是由替换引理，步骤 4 的误差不超过 $\lVert h'''\rVert_\infty\,\lambda_n\varepsilon$。
**步骤 5（合并得 CLT）。** 对任意 $h\in C_b^3$（三阶导有界），合并步骤 3 的尾部控制与步骤 4 的替换估计：先令 $n\to\infty$（此时 $\lambda_n\to1$、截断误差在概率意义下消失），再令 $\varepsilon\to0$，得
$$\big\lvert\mathbb Eh(S_n)-\mathbb Eh(N(0,1))\big\rvert\leq\lVert h'''\rVert_\infty\varepsilon+2\lVert h\rVert_\infty\cdot\limsup_{n}\mathbb P\Big(\Big\lvert\sum_k(X_{n,k}-\hat X_{n,k})\Big\rvert>\delta\Big)\ \xrightarrow[\varepsilon\to0]{}\ 0 .$$
由于 $\{h\in C_b^3\}$ 是弱收敛的决定类（其收敛蕴含一切有界连续函数的收敛，从而可用特征函数唯一性定理与连续性定理判别），得
$$\sum_{k=1}^nX_{n,k}\ \Longrightarrow\ N(0,1),$$
Lindeberg 中心极限定理得证。

**步骤 6（随机矩阵版本：四矩匹配 + 替换）。** 设 $W_n=n^{-1/2}(x_{ij})$、$G_n=n^{-1/2}(g_{ij})$ 为同方差 Wigner 矩阵且前四阶矩匹配。对光滑检验函数 $h$，逐元素把 $x_{ij}$ 替换为 $g_{ij}$：由矩阵版本的替换引理（用 resolvent 展开或 Stein 方法），单个元素的替换误差被元素的低阶矩与 resolvent 的局部化界（$\lVert(W_n-z)^{-1}\rVert\sim n^{-1/2}$ 型估计）控制；四阶矩匹配使低阶项精确抵消，剩下 $O(n^{-c})$ 的余项，累加得
$$\big\lvert\mathbb Eh(W_n)-\mathbb Eh(G_n)\big\rvert\leq C_kn^{-c_k}\lVert h\rVert_{C^k} .$$
高斯情形的 Wigner 半圆律（其矩满足 $\mathbb Em_{2k}=C_k$ 即 Catalan 数）由四矩匹配定理验证，于是由上式得一般系综的半圆律（普适性）。$\square$

**注**：替换法的关键在于"同均值同方差使二阶项抵消"，因此矩匹配的阶数决定能证明的普适性强度：CLT 只需二阶矩匹配，随机矩阵的半圆律需四阶匹配，而更精细的统计量（如局部特征值统计）需要更高阶匹配与更强的局部化估计。

## 五、应用与意义

- **定量中心极限定理**：Berry–Esseen 型界、局部 CLT、三角形阵列的 Lindeberg–Feller 定理，均可用替换法直接得到。
- **随机矩阵普适性**：Lindeberg 替换与四矩匹配是 Wigner 半圆律、局部半圆律以及稀疏、带状 Wigner 矩阵普适性的标准证明路线。
- **相依变量**：对局部依赖、鞅差与图上随机变量逐一替换，可把 CLT 归约到高斯情形，是鞅差中心极限定理与网络统计量极限理论的基础。
- **非线性泛函的普适性**：对谱多项式、线性统计量、特征值间距等泛函，替换法把普适性从高斯系综传递到一般系综。
- **误差控制与计算**：替换法的误差界给出显式的收敛速度，可用于选择高斯近似与样本量。

## 课堂问答

**老师**：证明 CLT 时一次只把一个变量换成正态变量，凭什么误差可控？

**学生**：因为把两和之差写成望远镜求和 $\mathbb Eh(S_n)-\mathbb Eh(N)=\sum_{k=1}^n\bigl(\mathbb Eh(S^{(k-1)})-\mathbb Eh(S^{(k)})\bigr)$，每步只换一个变量。对 $h$ 作三次 Taylor 展开，一次项因同均值、二次项因同方差而精确抵消，高斯又有 $\mathbb EY^3=0$，余项只剩三阶矩：$\bigl|\mathbb Eh(Z+X)-\mathbb Eh(Z+Y)\bigr|\le\frac{\|h^{\prime\prime\prime}\|_\infty}{2}\mathbb E|X|^3$。求和即得 Berry–Esseen 型 $O(\sum_k\mathbb E|X_{n,k}|^3)$。

**老师（追问）**：三阶矩可能发散，这一步怎么补？

**学生**：先截断 $\hat X_{n,k}=X_{n,k}\mathbf 1_{\{|X_{n,k}|\le\varepsilon\}}-\mathbb E[X_{n,k}\mathbf 1_{\{|X_{n,k}|\le\varepsilon\}}]$，用 Lindeberg 条件控制 $\sum_k\mathbb E|X_{n,k}-\hat X_{n,k}|\to0$，使截断和与原和在概率意义下渐近相同；再对截断变量用替换引理，其误差 $\le\|h^{\prime\prime\prime}\|_\infty\lambda_n\varepsilon$，先令 $n\to\infty$ 再令 $\varepsilon\to0$ 即得 CLT。

**老师（拓展）**：它怎么推广到随机矩阵的普适性？

**学生**：把每个矩阵元素 $x_{ij}$ 逐个替换为同方差高斯 $g_{ij}$，单步误差用 resolvent 展开与局部化界控制；只要前四阶矩匹配，低阶项精确抵消，累积误差为 $O(n^{-c})$，于是把高斯系综的半圆律传给一般系综。要点是 CLT 只需二阶矩匹配，半圆律需四阶匹配，阶数决定能证到的普适性强度。

## 相关条目

- [四矩匹配定理](./四矩匹配定理.md)：与本方法配合，把高斯系综的普适性传给一般系综。
- [Wigner半圆律](./Wigner半圆律.md)：随机矩阵替换法的目标极限律。
- [普适性猜想](./普适性猜想.md)：替换法所证明的普适性的猜想性表述。
- [Marchenko-Pastur定律](./Marchenko-Pastur定律.md)：样本协方差矩阵中的对应极限律，同一替换框架可处理。
- [Stieltjes变换的反演公式](./Stieltjes变换的反演公式.md)：把矩收敛转为谱测度收敛的工具，与替换法的矩计算衔接。
- [中心极限定理](../第24级-概率论基础/中心极限定理.md)：本方法所证明的定量版本的基础定理。
- [特征函数唯一性定理](../第24级-概率论基础/特征函数唯一性定理.md)：步骤 5 中判断弱收敛的工具。
- [鞅差中心极限定理](../第41级-随机过程/鞅差中心极限定理.md)：把替换法推广到相依（鞅差）情形。
