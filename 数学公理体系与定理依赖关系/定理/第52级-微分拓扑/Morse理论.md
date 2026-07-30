# Morse 理论

## 一、定理介绍

Morse 理论是微分拓扑和几何分析的重要分支，由美国数学家 Marston Morse 在 1920-1930 年代创立。该理论研究光滑流形上的函数（Morse 函数）的临界点与流形拓扑之间的关系。

Morse 理论的核心思想是：流形的拓扑结构可以通过其上的 Morse 函数的临界点来理解。每个临界点对应于流形"添加"一个胞腔，从而改变拓扑结构。

## 二、原理思路

Morse 理论的核心思想包括：

1. **Morse 函数**：光滑函数 $f: M \to \mathbb{R}$ 是 Morse 函数，如果它的所有临界点都是非退化的（Hessian 矩阵非退化）。

2. **临界点指标**：非退化临界点 $p$ 的指标 $\lambda(p)$ 定义为 Hessian 矩阵 $H_f(p)$ 的负特征值的个数。

3. **Morse 引理**：在非退化临界点附近，函数可以写成标准二次型形式：$f(x) = f(p) - x_1^2 - \cdots - x_\lambda^2 + x_{\lambda+1}^2 + \cdots + x_n^2$。

4. **拓扑变化**：当水平集 $f^{-1}(-\infty, a]$ 经过临界点时，拓扑发生变化：添加一个 $\lambda$ 维胞腔。

5. **Morse 不等式**：临界点的个数给定了 Betti 数的下界。

## 三、定理的严格表述

**Morse 函数定义**：设 $M$ 是光滑流形，$f: M \to \mathbb{R}$ 是光滑函数。点 $p \in M$ 是 $f$ 的**临界点**，如果 $df_p = 0$。临界点 $p$ 是**非退化的**，如果 Hessian 矩阵：
$$H_f(p) = \left(\frac{\partial^2 f}{\partial x_i \partial x_j}(p)\right)$$

非退化（即行列式非零）。$f$ 是 **Morse 函数**，如果它的所有临界点都是非退化的。

**临界点指标**：非退化临界点 $p$ 的**指标** $\lambda(p)$ 定义为 $H_f(p)$ 的负特征值的个数（或等价地，负定子空间的最大维数）。

**Morse 引理**：设 $p$ 是 $f$ 的非退化临界点，指标为 $\lambda$。则存在 $p$ 附近的局部坐标 $(x_1, \ldots, x_n)$，使得：
$$f(x) = f(p) - x_1^2 - \cdots - x_\lambda^2 + x_{\lambda+1}^2 + \cdots + x_n^2$$

**Morse 不等式**：设 $f: M \to \mathbb{R}$ 是紧流形 $M$ 上的 Morse 函数。记 $c_k$ 为指标为 $k$ 的临界点个数，$b_k = \dim H_k(M; \mathbb{Z}_2)$ 为第 $k$ 个 Betti 数。则：

**弱 Morse 不等式**：
$$c_k \geq b_k \quad \text{对所有 } k$$

**强 Morse 不等式**：存在非负整数 $R_k$，使得：
$$c_k = b_k + R_k + R_{k-1} \quad \text{对所有 } k$$

（约定 $R_{-1} = R_n = 0$）

**Morse 不等式的等价形式**：
$$c_k - c_{k-1} + c_{k-2} - \cdots \geq b_k - b_{k-1} + b_{k-2} - \cdots$$

**Euler 示性数**：
$$\chi(M) = \sum_{k=0}^n (-1)^k c_k = \sum_{k=0}^n (-1)^k b_k$$

**Morse 函数的存在性**：任何光滑流形上都存在 Morse 函数。事实上，Morse 函数在 $C^\infty(M, \mathbb{R})$ 中是稠密的。

**Handlebody 分解定理**：设 $f: M \to \mathbb{R}$ 是紧流形 $M$ 上的 Morse 函数。则 $M$ 具有 handlebody 分解，其中每个指标为 $\lambda$ 的临界点对应于添加一个 $\lambda$-handle。

## 四、证明过程

**步骤 1：Morse 引理的证明**

设 $p$ 是 $f$ 的非退化临界点，指标为 $\lambda$。不妨设 $f(p) = 0$。

由于 $df_p = 0$，Taylor 展开给出：
$$f(x) = \frac{1}{2} \sum_{i,j} \frac{\partial^2 f}{\partial x_i \partial x_j}(p) x_i x_j + O(|x|^3)$$

由非退化条件，Hessian 矩阵 $H = \left(\frac{\partial^2 f}{\partial x_i \partial x_j}(p)\right)$ 可逆。

由线性代数，存在可逆矩阵 $P$ 使得 $P^T H P$ 是对角矩阵，对角元为 $\pm 1$。

通过坐标变换 $y = Px$，得到：
$$f(y) = \frac{1}{2}(-y_1^2 - \cdots - y_\lambda^2 + y_{\lambda+1}^2 + \cdots + y_n^2) + O(|y|^3)$$

使用 Moser 技巧或逐步规范化，可以消除高阶项，得到标准形式。

**步骤 2：水平集的拓扑变化**

设 $a < b$，$f^{-1}[a, b]$ 不包含临界点。则 $f^{-1}(-\infty, a]$ 微分同胚于 $f^{-1}(-\infty, b]$。

证明：由于在 $f^{-1}[a, b]$ 上 $df \neq 0$，可以定义向量场 $X = \nabla f / |\nabla f|^2$。$X$ 的流 $\phi_t$ 满足 $f(\phi_t(x)) = f(x) + t$。

通过流的适当截断，可以构造从 $f^{-1}(-\infty, a]$ 到 $f^{-1}(-\infty, b]$ 的微分同胚。

**步骤 3：经过临界点时的变化**

设 $p$ 是 $f$ 的唯一临界点，$f(p) = c$，指标为 $\lambda$。设 $a < c < b$，$f^{-1}[a, b]$ 中只有 $p$ 一个临界点。

由 Morse 引理，在 $p$ 附近有坐标使得 $f(x) = c - x_1^2 - \cdots - x_\lambda^2 + x_{\lambda+1}^2 + \cdots + x_n^2$。

定义 $e_\epsilon = \{x : f(x) \leq c + \epsilon, |x| \leq \delta\}$。可以证明 $f^{-1}(-\infty, c + \epsilon]$ 同伦等价于 $f^{-1}(-\infty, c - \epsilon] \cup_\phi D^\lambda$，其中 $D^\lambda$ 是 $\lambda$ 维盘，$\phi: \partial D^\lambda \to f^{-1}(-\infty, c - \epsilon]$ 是附着映射。

**步骤 4：弱 Morse 不等式的证明**

由步骤 3，$M$ 具有 CW 复形结构，其中每个指标为 $k$ 的临界点对应一个 $k$ 维胞腔。

因此 $M$ 的同调群满足：
$$\dim H_k(M) \leq \text{（$k$ 维胞腔的个数）} = c_k$$

即 $b_k \leq c_k$。

**步骤 5：强 Morse 不等式的证明**

定义 Morse 多项式和 Poincaré 多项式：
$$M(t) = \sum_{k=0}^n c_k t^k, \quad P(t) = \sum_{k=0}^n b_k t^k$$

强 Morse 不等式等价于：存在多项式 $R(t) = \sum R_k t^k$（系数非负），使得：
$$M(t) - P(t) = (1 + t) R(t)$$

这可以通过分析胞腔复形的边界算子来证明。

**步骤 6：Morse 函数的存在性**

由 Whitney 嵌入定理，$M$ 可以嵌入到 $\mathbb{R}^N$ 中。对于几乎处处的方向 $v \in \mathbb{R}^N$，高度函数 $f_v(x) = \langle x, v \rangle$ 是 Morse 函数。

这由 Sard 定理保证：考虑映射 $F: M \to \mathbb{R}^N$，$F(x) = x$。对几乎处处的 $v$，$f_v$ 的临界点都是非退化的。

## 五、应用与意义

**理论意义**：
1. **流形拓扑的刻画**：Morse 理论通过函数的临界点来刻画流形的拓扑结构，建立了分析与拓扑的深刻联系。

2. **Handlebody 理论**：Morse 函数给出了流形的 handlebody 分解，这是高维流形分类的基础。

3. **最优性**：Morse 不等式给出了临界点个数的下界，这个下界在某些情况下是最佳的。

**应用领域**：
1. **几何分析**：在极小曲面、调和映射等研究中，Morse 理论用于分析解空间的结构。

2. **辛几何**：Arnold 猜想使用 Floer 同调（Morse 理论的无穷维推广）研究辛流形的不动点。

3. **最优控制**：Morse 理论在最优控制和变分法中有应用。

4. **计算机图形学**：Morse-Smale 复形用于曲面分析和可视化。

**具体应用实例**：
- **球面的临界点**：$S^2$ 上的 Morse 函数至少有 2 个临界点（极大值和极小值）
- **环面的临界点**：$T^2$ 上的 Morse 函数至少有 4 个临界点（$b_0 = 1, b_1 = 2, b_2 = 1$）
- **Poincaré 猜想**：Smale 使用 h-配边定理（基于 Morse 理论）证明了高维 Poincaré 猜想

**推广与发展**：
- **Floer 同调**：Morse 理论在无穷维的推广，用于辛几何和低维拓扑
- **Morse-Bott 理论**：允许临界点形成子流形的情形
- **离散 Morse 理论**：在组合拓扑中的离散版本
- **持久同调**：在拓扑数据分析中，Morse 理论的思想被用于分析数据的拓扑结构
