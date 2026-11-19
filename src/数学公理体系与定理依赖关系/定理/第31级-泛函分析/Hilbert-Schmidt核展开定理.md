# Hilbert–Schmidt 核展开定理

> **一句话大白话**：对称且平方可积的积分核，可以按积分算子的实特征值与正交特征函数展开；但这个展开首先只是 $L^2$ 平均意义下的展开，不会自动升级成逐点一致收敛。
>
> **小例子**：若 $\|\varphi\|_2=1$ 且 $K(x,y)=\varphi(x)\overline{\varphi(y)}$，则相应算子是秩一投影 $Tf=\langle f,\varphi\rangle\varphi$。唯一非零特征值为 $1$，核展开只有一项 $1\cdot\varphi(x)\overline{\varphi(y)}$。

## 介绍

Hilbert–Schmidt 核展开定理是紧自伴算子谱定理在积分算子上的核形式。它同时给出算子的谱分解、核的 $L^2$ 展开以及特征值平方和公式。它常被与 Mercer 定理混为一谈：后者额外要求连续半正核，并得到连续特征函数及绝对一致收敛；一般 Hilbert–Schmidt 核没有这些结论。

## 分析

**前置依赖**：可分的 $L^2$ 空间、Hilbert–Schmidt 算子、紧算子、自伴性、紧自伴算子谱定理。

**定理内容**：设 $(X,\mu)$ 为 $\sigma$-有限测度空间且 $L^2(X,\mu)$ 可分，核 $K\in L^2(X\times X,\mu\otimes\mu)$ 满足 Hermite 对称性

$$
K(x,y)=\overline{K(y,x)}
\qquad\text{几乎处处}.
$$

定义

$$
(T_Kf)(x)=\int_XK(x,y)f(y)\,\mathrm d\mu(y).
$$

则 $T_K$ 是紧自伴的 Hilbert–Schmidt 算子。其非零特征值记为 $\lambda_j$，按重数重复，均为实数；对应特征函数 $\varphi_j$ 可取为标准正交系。若特征值有无穷多个，则 $\lambda_j\to0$，并且

$$
T_Kf=\sum_j\lambda_j\langle f,\varphi_j\rangle\varphi_j
\qquad\text{在 }L^2(X)\text{ 中收敛},
$$

$$
\boxed{K(x,y)=\sum_j\lambda_j\varphi_j(x)\overline{\varphi_j(y)}
\qquad\text{在 }L^2(X\times X)\text{ 中收敛}.}
$$

同时

$$
\sum_j|\lambda_j|^2
=\iint_{X\times X}|K(x,y)|^2\,\mathrm d\mu(x)\mathrm d\mu(y)
=\|T_K\|_{\mathrm{HS}}^2.
$$

非零特征函数构成 $(\ker T_K)^\perp=\overline{\operatorname{ran}T_K}$ 的完备正交基；要得到整个 $L^2(X)$ 的基，通常还必须加入 $\ker T_K$ 的正交基。

## 思考过程

平方可积核使 $T_K$ 成为 Hilbert–Schmidt 算子，而 Hermite 对称性使它自伴。紧自伴谱定理先把算子对角化。再把有限秩算子 $T_Nf=\sum_{j\le N}\lambda_j\langle f,\varphi_j\rangle\varphi_j$ 对应到核 $K_N=\sum_{j\le N}\lambda_j\varphi_j\otimes\overline{\varphi_j}$，它们的 Hilbert–Schmidt 误差恰是尾部特征值平方和，所以核展开在 $L^2$ 中收敛。整个论证没有逐点估计，因此不能推出一致收敛。

## 证明过程

**证明纲要**：

1. **紧性与自伴性**：由 $K\in L^2(X\times X)$，$T_K$ 是 Hilbert–Schmidt 算子，故为紧算子且
   $$
   \|T_K\|_{\mathrm{HS}}^2=\iint|K(x,y)|^2\,\mathrm d\mu(x)\mathrm d\mu(y).
   $$
   Fubini 定理与 Hermite 对称性给出 $\langle T_Kf,g\rangle=\langle f,T_Kg\rangle$，所以 $T_K$ 自伴。
2. **应用谱定理**：紧自伴算子的非零谱由实特征值组成，每个非零特征空间有限维，特征值只可能聚集于 $0$。选取标准正交特征函数 $\varphi_j$，即得 $L^2$ 中的算子谱展开。
3. **识别有限秩核**：算子 $T_N=\sum_{j\le N}\lambda_j\langle\cdot,\varphi_j\rangle\varphi_j$ 的积分核正是
   $$
   K_N(x,y)=\sum_{j\le N}\lambda_j\varphi_j(x)\overline{\varphi_j(y)}.
   $$
   由正交性，$\|T_K-T_N\|_{\mathrm{HS}}^2=\sum_{j>N}|\lambda_j|^2$，而 Hilbert–Schmidt 算子与其核的 $L^2$ 范数一致，故 $K_N\to K$ 于 $L^2(X\times X)$。
4. **平方和公式**：对规范正交核基计算 $\|K\|_2^2$，或直接令 $N\to\infty$，即得 $\sum_j|\lambda_j|^2=\|K\|_2^2$。这也说明只有有限多个非零特征值或它们趋于零，并且级数具有所需的尾部控制。$\square$

**与 Mercer 定理的界线**：Mercer 定理通常设 $X$ 为紧拓扑空间，配以支撑为 $X$ 的有限 Borel 测度，且 $K$ 连续 Hermite、半正定。此时非零 $\lambda_j>0$，特征函数可取连续，并有
$$K(x,y)=\sum_j\lambda_j\varphi_j(x)\overline{\varphi_j(y)}$$
在 $X\times X$ 上绝对一致收敛；若测度支撑只是 $X$ 的真子集，逐点展开应限制在支撑上陈述。仅凭 $K\in L^2$ 与对称性，既不能保证逐点公式，也不能保证所有非零特征值为正。

## 课堂问答

**老师**：为什么核展开中的系数是 $\lambda_j$，而不是 $1/\lambda_j$？

**学生**：因为这里 $\lambda_j$ 定义为本条目中算子的特征值，即 $T_K\varphi_j=\lambda_j\varphi_j$。直接展开算子便得到 $T_K=\sum_j\lambda_j\langle\cdot,\varphi_j\rangle\varphi_j$。有些积分方程教材把特征参数定义为 $T_K\varphi=\mu^{-1}\varphi$，那时核系数自然写成 $\mu^{-1}$，只是记号约定不同。

**老师（追问）**：非零特征函数是否总构成整个 $L^2$ 的完备正交基？

**学生**：不一定。它们只在 $\overline{\operatorname{ran}T_K}=(\ker T_K)^\perp$ 中完备。若 $T_K$ 有非平凡零空间，例如秩一算子，就必须补上零空间的正交基，才能张成整个 $L^2$。

**老师（拓展）**：加上连续、对称条件后，是否就能使用 Mercer 的一致收敛结论？

**学生**：还不够，还需要半正定性以及通常的紧空间、有限且支撑为整个空间的测度设定；若测度支撑较小，只能直接在支撑上写出一致展开。连续对称核可能有负特征值；一般 Hilbert–Schmidt 展开本来就允许正负实特征值。Mercer 定理的这些附加条件正是把 $L^2$ 展开升级为绝对一致展开的关键输入。

## 相关条目

- [谱定理（紧自伴算子）](./谱定理紧自伴算子.md)
- [Riesz–Schauder 定理](./Riesz-Schauder定理.md)
- [Volterra 积分方程的预解核](./Volterra积分方程的预解核.md)
- [主教程第60级：积分方程](../../../05-高阶专题I-分析几何统计/第60级-积分方程.md)
