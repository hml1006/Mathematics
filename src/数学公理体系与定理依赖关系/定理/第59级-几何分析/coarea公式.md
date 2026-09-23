# coarea 公式

> **一句话大白话**：把"体积"按函数值切成一层层水平集再累加起来就还原体积，只不过每一层要按梯度模长"付费"：$\int g\,|\nabla f|=\int_{\mathbb R}\bigl(\int_{f^{-1}(t)}g\bigr)dt$。

> **小例子**：取 $f(x)=|x|$ 于 $\mathbb R^n$，除原点外 $|\nabla f|=1$，水平集 $f^{-1}(t)=tS^{n-1}$。coarea 公式化为 $\int_{\mathbb R^n}g\,dx=\int_0^\infty\bigl(\int_{|x|=t}g\,d\sigma\bigr)dt$，这正是球坐标（极坐标）积分公式。

## 一、定理介绍

> **前置依赖**：Lipschitz 函数与 Rademacher 定理、梯度与 Jacobian、Hausdorff 测度与面积公式（area formula）、Sard 定理、Fubini 定理、隐函数定理。

coarea 公式（coarea formula，又称余面积公式、水平集公式）是几何测度论中的基本积分公式，其系统形式由 Federer 在 1944 年的曲率测度研究与 1959 年的《Geometric Measure Theory》中确立。它的特殊情形早已为人熟知：Cauchy 用它计算曲面的"倾斜度"积分，而极坐标积分公式（球坐标）正是它最简单的例子。

公式把区域上的积分分解为沿函数水平集的积分：给定 Lipschitz 函数 $f$ 与非负可测函数 $g$，

$$\int_M g\,|\nabla f|\,d\mu=\int_{\mathbb R}\Bigl(\int_{f^{-1}(t)}g\,d\mathcal H^{n-1}\Bigr)dt.$$

它可看作 Fubini 定理在"曲面水平集"情形（而非坐标超平面）的推广——关键差别在于要引入因子 $|\nabla f|$ 来补偿水平集间距随位置的变化。

coarea 公式是几何分析中被使用最频繁的工具之一。在几何测度论中，它给出 BV 函数的总变差、有限周长集的定义与 De Giorgi 的结构定理，也是证明可求长性与 rectifiability 的手段；在极小曲面与平均曲率流中，它用于把体积单调性、密度估计与水平集的几何量联系起来；在分析中，它是"层饼表示"（layer cake）与 Sobolev、等周不等式证明的标准工具。与它并列的 area formula $\int_M g\,J_f\,d\mu=\int_{\mathbb R^n}\bigl(\int_{f^{-1}(y)}g\,d\mathcal H^{m-n}\bigr)dy$ 是把积分推到像空间；两者互为"对偶"。

## 二、原理思路

1. **光滑且无临界点时的标架分解**：若 $\nabla f\ne0$，取正交标架使 $e_1=\nabla f/|\nabla f|$，其余 $e_2,\dots,e_n$ 切于水平集。对偶余标架中 $\theta^1(e_1)=1$、$\theta^1(e_j)=0\,(j\ge2)$，故 $\theta^1=df/|\nabla f|$；而 $\theta^2\wedge\cdots\wedge\theta^n$ 正是水平集的 $(n-1)$ 维面积元。

2. **体积元按"层"分解**：由上一步，$d\mu=\theta^1\wedge\cdots\wedge\theta^n=\frac{df}{|\nabla f|}\wedge d\sigma$，其中 $d\sigma$ 是水平集面积元。等价地 $g|\nabla f|\,d\mu=g\,df\wedge d\sigma$。

3. **对 $t$ 用 Fubini**：把 $g\,df\wedge d\sigma$ 沿 $f$ 的值 $t$ 积分，即得 $\int_{\mathbb R}\bigl(\int_{f^{-1}(t)}g\,d\sigma\bigr)dt$。一般的 Lipschitz 情形用 Rademacher 定理（几乎处处可微）与光滑逼近，并说明临界值集与奇异集测度为零。

## 三、定理的严格表述

**定理（coarea 公式，一维目标）**：设 $(M^n,g)$ 是黎曼流形，$f:M\to\mathbb R$ 是 Lipschitz 函数，$g\ge0$ 是 Borel 可测函数。则

$$\int_M g\,|\nabla f|\,d\mu=\int_{-\infty}^{+\infty}\Bigl(\int_{f^{-1}(t)}g\,d\mathcal H^{n-1}\Bigr)dt,$$

其中 $\nabla f$ 是 $f$ 的近似梯度（几乎处处存在），$f^{-1}(t)$ 配以 $(n-1)$ 维 Hausdorff 测度 $\mathcal H^{n-1}$（对几乎所有 $t$，$f^{-1}(t)$ 是可求长的，该等式对一般 $f$ 仍然成立）。

**定理（一般形式）**：设 $f:M^m\to\mathbb R^n$ 是 Lipschitz 映射，$J_f$ 为其 Jacobian（$J_f=\sqrt{\det(df\,df^{\mathsf T})}$）。则

$$\int_M g\,J_f\,d\mu=\int_{\mathbb R^n}\Bigl(\int_{f^{-1}(y)}g\,d\mathcal H^{m-n}\Bigr)\,dy.$$

**推论（层饼表示）**：取 $g$ 为指示函数，得 $\int_M|\nabla f|\,d\mu=\int_{\mathbb R}\mathcal H^{n-1}(f^{-1}(t))\,dt$；对 $f\ge0$ 的 Lipschitz 函数还有 $\int_M f\,|\nabla u|\,d\mu=\int_0^\infty\bigl(\int_{\{f>t\}}|\nabla u|\,d\mu\bigr)dt$ 一类层饼公式。

**依赖的概念**：近似梯度、Jacobian、Hausdorff 测度、面积公式、Fubini 定理。

## 四、证明过程

**步骤 1（无临界点处的余标架）。** 设 $f$ 光滑且 $\nabla f(x_0)\ne0$。在 $x_0$ 的邻域内取单位向量场

$$e_1=\frac{\nabla f}{|\nabla f|},\qquad e_2,\dots,e_n\ \text{切于水平集}\ f=\mathrm{const},$$

使 $\{e_1,\dots,e_n\}$ 是 $M$ 的局部正交标架（先取水平集的局部正交标架，再补上 $e_1$）。设对偶余标架为 $\theta^1,\dots,\theta^n$，即 $\theta^i(e_j)=\delta^i_j$。于是对任意 $j$，

$$\theta^1(e_1)=1,\qquad \theta^1(e_j)=0\ (j\ge2),$$

而 $df(e_1)=\langle\nabla f,e_1\rangle=|\nabla f|$、$df(e_j)=\langle\nabla f,e_j\rangle=0$。因此

$$\theta^1=\frac{df}{|\nabla f|}.$$

**步骤 2（体积元的分解）。** $M$ 的体积元为 $d\mu=\theta^1\wedge\cdots\wedge\theta^n$。记水平集的 $(n-1)$ 维面积元

$$d\sigma=\theta^2\wedge\cdots\wedge\theta^n\big|_{\{f=\mathrm{const}\}},$$

它在每层 $f^{-1}(t)$ 上恰是 $\mathcal H^{n-1}$ 的面积元。把 $\theta^1=df/|\nabla f|$ 代入：

$$d\mu=\frac{1}{|\nabla f|}\,df\wedge d\sigma,\qquad\text{即}\qquad |\nabla f|\,d\mu=df\wedge d\sigma.$$

**步骤 3（沿层积分）。** 两边乘以 $g$ 并在 $M$ 上积分：

$$\int_M g\,|\nabla f|\,d\mu=\int_M g\,df\wedge d\sigma.$$

右端是"先沿每层 $f^{-1}(t)$ 积分、再把结果按 $t$ 积分"的表述，把它写成累次积分（每一步都在局部标架下成立，沿 $M$ 用单位分解拼起来），即

$$\int_M g\,df\wedge d\sigma=\int_{-\infty}^{+\infty}\Bigl(\int_{f^{-1}(t)}g(x)\,d\sigma_t(x)\Bigr)dt=\int_{-\infty}^{+\infty}\Bigl(\int_{f^{-1}(t)}g\,d\mathcal H^{n-1}\Bigr)dt.$$

这就是光滑无临界点情形的 coarea 公式。

**步骤 3'（处理临界点与奇异点）。** 令 $C=\{x:\nabla f(x)=0\}$ 为临界点集。由 Sard 定理，$f(C)$ 在 $\mathbb R$ 中测度为零；又对 $t\notin f(C)$，$f^{-1}(t)$ 是 $C^\infty$ 超曲面且各点满足 $\nabla f\ne0$，步骤 1 至 3 适用。于是公式右端在被积函数（关于 $t$）几乎处处有定义，且两条不等式方向都可由逼近得到。详细地说，把 $f$ 用一列光滑函数 $f_k$ 逼近（在 $W^{1,p}$ 意义下 $f_k\to f$、$\nabla f_k\to\nabla f$ 于 $L^1_{\mathrm{loc}}$），对每个 $f_k$ 用步骤 3，令 $k\to\infty$，并用 $\mathcal H^{n-1}$ 的下半连续性与控制收敛（$g\,|\nabla f|$ 可积）即可把等式传递到极限。

**步骤 4（一般形式的来源）。** 若 $f:M^m\to\mathbb R^n$ Lipschitz，则对几乎所有的值 $y$，$f^{-1}(y)$ 是 $(m-n)$ 维可求长集，且可用同样的余标架论证（把 $\mathbb R^n$ 方向的 $n$ 个正交法向作为 $\theta^1,\dots,\theta^n$，其余切于纤维）得

$$\int_M g\,J_f\,d\mu=\int_{\mathbb R^n}\Bigl(\int_{f^{-1}(y)}g\,d\mathcal H^{m-n}\Bigr)dy.$$

一维目标即 $n=1$、$J_f=|\nabla f|$ 的特例。$\square$

## 五、应用与意义

- **极坐标与球面平均**：$f(x)=|x|$ 给出球坐标积分公式，是调和分析与偏微分方程中球面平均法的来源。
- **BV 函数与有限周长**：coarea 公式给出 $\mathrm{Var}(u;U)=\int_{\mathbb R}\mathrm{Per}(\{u>t\};U)\,dt$，是有限周长集理论的定义性工具。
- **层饼表示**：$L^p$ 范数与分布函数的层饼分解、Sobolev 不等式与等周不等式的标准证明步骤。
- **极小曲面与平均曲率流**：将体积积分的单调性、密度估计化为水平集几何量的估计。
- **可求长性**：结合面积公式用于证明集合可求长（rectifiable）与 De Giorgi 结构定理。

## 相关条目

- [第一变分公式](./第一变分公式.md)：把几何量沿曲面变分分解，与本公式"沿水平集分解"互补。
- [几何测度论紧性定理](./几何测度论紧性定理.md)：coarea 公式是流的切片（slicing）理论与紧性定理的基础工具。
- [Huisken单调公式](./Huisken单调公式.md)：其证明要把积分沿曲面与时间分解，常与 coarea 型分解配合。
- [极小曲面理论](./极小曲面理论.md)：水平集方法与面积估计依赖 coarea 公式。
- [平均曲率流](./平均曲率流.md)：水平集表述与体积单调性用 coarea 公式建立。
