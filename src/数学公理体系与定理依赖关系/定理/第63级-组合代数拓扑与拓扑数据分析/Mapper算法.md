# Mapper 算法：拓扑数据可视化方法

> **一句话大白话**：把一堆密密麻麻的高维数据点先用少数几个"标尺"投影拉长，再按分格逐段聚会成一小团一小团，连成一幅拓扑图——让你一眼看到数据的"空腔"和"骨架"。
>
> **小例子**：对一个圆环形的点云取一个单调坐标作 filter，分若干格子每格聚类得到若干节点，环状相邻节点连边后生成的 Mapper 图本身就是一圈，重现环形拓扑。

## 一、定理介绍

> **前置依赖**：覆盖的 nerve 构造、filter 函数与 pullback 覆盖、连通分支与聚类算法、Reeb 图及其稳定性、Gromov–Hausdorff 距离。

Mapper 是由 Singh、Mémoli 与 Carlsson 提出的拓扑数据可视化算法。它通过一组 filter 函数把高维点云投影到低维空间，再用覆盖（cover）和聚类把原数据分割成局部块，最后以这些局部块为顶点、块间交集为边构建一个图（或单纯复形）。Mapper 能在保持全局拓扑轮廓的同时压缩数据规模，是拓扑数据分析中最具影响力的可视化工具之一。

## 二、原理思路

1. **Filter 函数**：选取 $f:X\to \mathbb{R}^d$（如密度、PCA 坐标、偏心度等），把高维数据映射到低维空间。
2. **覆盖 pullback**：在像空间 $f(X)$ 上取有限开覆盖 $\mathcal{U}=\{U_\alpha\}$，拉回得到 $X$ 的覆盖 $f^{-1}\mathcal{U}=\{f^{-1}(U_\alpha)\}$。
3. **局部聚类**：对每个 $f^{-1}(U_\alpha)$ 用聚类算法（单连锁、DBSCAN 等）分成若干连通分支/簇 $V_{\alpha,1},\dots,V_{\alpha,k_\alpha}$。
4. **构建 nerve**：以所有簇为顶点，若两个簇来自相邻覆盖元且有非空交集，则在图中连边；也可推广到高维单纯形。

## 三、定理的严格表述

设 $(X,d)$ 为有限度量空间，$f:X\to \mathbb{R}^d$ 为 filter 函数，$\mathcal{U}=\{U_\alpha\}_{\alpha\in A}$ 为 $f(X)$ 的有限开覆盖。对每个 $\alpha$，设
$$
f^{-1}(U_\alpha) = V_{\alpha,1} \sqcup V_{\alpha,2} \sqcup \cdots \sqcup V_{\alpha,k_\alpha}
$$
是聚类算法给出的划分（例如每个 $V_{\alpha,i}$ 是 $f^{-1}(U_\alpha)$ 的一个连通分支或一个簇）。

**Mapper 图** $M(X,f,\mathcal{U})$ 定义如下：
- 顶点集：$\{(\alpha,i): \alpha\in A,\; 1\le i\le k_\alpha\}$，每个顶点对应一个簇 $V_{\alpha,i}$；
- 边集：两个顶点 $(\alpha,i)$ 与 $(\beta,j)$ 之间有边当且仅当 $\alpha\neq\beta$、$U_\alpha\cap U_\beta\neq\varnothing$ 且 $V_{\alpha,i}\cap V_{\beta,j}\neq\varnothing$。

更一般地，Mapper 复形是 refined pullback cover $\{V_{\alpha,i}\}$ 的 nerve：
$$
M(X,f,\mathcal{U}) = \mathcal{N}\left(\{V_{\alpha,i}\}_{\alpha,i}\right).
$$

**收敛性结果（Reeb 图逼近）**：设 $X$ 为紧致路径连通度量空间，$f:X\to\mathbb{R}$ 为 Morse 型函数。若覆盖 $\mathcal{U}$ 充分细且聚类能准确识别每个 $f^{-1}(U_\alpha)$ 的连通分支，则 Mapper 图在 Gromov–Hausdorff 距离下逼近 $f$ 的 Reeb 图；更精确地，存在与覆盖粒度相关的上界
$$
d_{GH}\bigl(M(X,f,\mathcal{U}), \operatorname{Reeb}(X,f)\bigr) \le \varepsilon(\mathcal{U}),
$$
其中 $\varepsilon(\mathcal{U})$ 随覆盖最大直径趋于 $0$ 而趋于 $0$。

## 四、证明过程

**步骤 1：Mapper 是 nerve 的特例。**
簇族 $\{V_{\alpha,i}\}$ 构成 $X$ 的一个覆盖。Mapper 图/复形正是该覆盖的 nerve，只不过原覆盖元来自低维像空间的 pullback 与聚类精化。

**步骤 2：与 Reeb 图的联系。**
Reeb 图 $\operatorname{Reeb}(X,f)$ 是把 $f$ 的水平集 $f^{-1}(t)$ 的每个连通分支收缩为一个点得到的商空间。当像空间覆盖的每个元 $U_\alpha$ 只跨过一个临界值区间时，$f^{-1}(U_\alpha)$ 的分支与 Reeb 图中对应区间上的弧一一对应；相邻覆盖元 pullback 的交集分支对应 Reeb 图中弧的连接点。

**步骤 3：收敛性估计。**
利用 Reeb 图的稳定性：对两个 Morse 型函数 $f,g$，其 Reeb 图在函子距离/ Gromov–Hausdorff 距离下被 $\|f-g\|_\infty$ 控制。把 Mapper 构造视为对 $f$ 的分段常数近似 $f_\mathcal{U}$（在每个簇上取常数值），当覆盖变细时 $\|f-f_\mathcal{U}\|_\infty\to 0$，故 Mapper 收敛到 Reeb 图。

**步骤 4：计算实现。**
实际中先计算所有 $f^{-1}(U_\alpha)$ 的聚类，再用集合交运算建立边；时间复杂度主要取决于聚类次数与覆盖元数量，通常远低于直接构造 Vietoris–Rips 复形。

## 五、应用与意义

- **高维数据可视化**：Mapper 把复杂数据集压缩成可解释的图，广泛用于生物信息学（疾病亚型）、材料科学、运动分析与社会网络。
- **特征发现**：图中分支、环、枢纽对应数据中的亚群、反馈回路与过渡态，帮助生成假设。
- **与持久同调互补**：Mapper 提供定性全局草图，持久同调提供定量洞特征，两者结合可构建完整 TDA 分析流程。
