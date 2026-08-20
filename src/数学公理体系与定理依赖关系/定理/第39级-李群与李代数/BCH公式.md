# BCH 公式

> **一句话大白话**：两个矩阵取指数相乘 $\exp(X)\exp(Y)$，多数时候不等于把 $X,Y$ 加起来再取指数；BCH 公式把这个"偏差"精确拼出来——用 $X,Y$ 的李括号写成一个无穷级数，告诉你群乘法到底是怎么"扭"的。
>
> **小例子**：若 $X,Y$ 交换（$[X,Y]=0$），则 $\exp(X)\exp(Y)=\exp(X+Y)$；而当 $[X,Y]$ 是中心元时，有 $\exp(X)\exp(Y)=\exp(X+Y+\tfrac12[X,Y])$。

## 介绍

Baker–Campbell–Hausdorff 公式（简称 BCH 公式）是李群与李代数理论中的一个基本公式，它给出了两个李代数元素 $X,Y$ 的指数乘积 $\exp(X)\exp(Y)$ 的指数表达式，即 $\exp(X)\exp(Y) = \exp(Z)$，其中 $Z$ 由 $X$ 和 $Y$ 通过李括号的无穷级数表示。该公式精确地揭示了李括号如何编码群乘法的非交换性，是李群–李代数对应的核心计算工具。

## 分析

**前置依赖**：指数映射、李代数、李括号、多重线性代数、幂级数展开。

**定理内容**：设 $G$ 是李群，$\mathfrak{g}$ 是其李代数。存在 $0 \in \mathfrak{g}$ 的邻域 $U$，使得对任意 $X,Y \in U$，$\exp(X)\exp(Y) \in \exp(U)$，且存在 $\mathfrak{g}$ 值形式幂级数
$$Z = X + Y + \frac{1}{2}[X,Y] + \frac{1}{12}[X,[X,Y]] - \frac{1}{12}[Y,[X,Y]] + \cdots$$
使得 $\exp(X)\exp(Y) = \exp(Z)$。

更精确地，在 $\mathfrak{g}$ 是矩阵李代数的情况下，BCH 公式可写作
$$\log(\exp(X)\exp(Y)) = X + Y + \frac{1}{2}[X,Y] + \frac{1}{12}[X,[X,Y]] - \frac{1}{12}[Y,[X,Y]] + \cdots$$
其中 $\log$ 是矩阵对数。

**数学内涵**：BCH 公式表明，李代数 $\mathfrak{g}$ 上的李括号运算完全决定了李群 $G$ 在单位元附近的乘法结构。具体地，群乘法的所有信息都编码在李括号中——这是李群–李代数对应能够成立的根本原因。公式中的每一项都是 $X,Y$ 的嵌套李括号的线性组合，系数是特定的有理数。

**证明策略**：证明通常有两种途径。一种是通过在 $\mathfrak{g}$ 上构造一个微分方程并求解，利用 $\frac{d}{dt}\log(\exp(tX)\exp(Y))$ 的表达式，得到关于 $Z(t)$ 的微分方程，然后用幂级数展开求解。另一种是直接利用 Dynkin 的显式公式，将 $Z$ 表达为所有可能嵌套李括号的和。

## 思考过程

BCH 公式的核心思想是：对于矩阵李群，$\exp(X)\exp(Y)$ 的幂级数展开会产生 $X$ 和 $Y$ 的所有可能乘积，但乘积的"非交换性"使得结果不是简单的 $X+Y$ 的指数。通过整理这些乘积项，发现它们可以全部用李括号来表示。

指数映射的局部微分同胚性质保证了存在 $Z$ 使得 $\exp(X)\exp(Y) = \exp(Z)$。BCH 公式给出了 $Z$ 的显式表达式。

一个重要特例是：若 $[X,Y] = 0$（即 $X$ 和 $Y$ 交换），则 $Z = X+Y$，回到交换群的情形。若 $[X,Y]$ 与 $X,Y$ 都交换（即 $[X,[X,Y]] = [Y,[X,Y]] = 0$），则 $Z = X+Y + \frac{1}{2}[X,Y]$，这是 Heisenberg 李代数的情形。

## 证明过程

**定理**（BCH 公式）：设 $\mathfrak{g}$ 是李代数，存在 $0$ 的邻域 $U \subseteq \mathfrak{g}$，使得对任意 $X,Y \in U$，
$$\exp(X)\exp(Y) = \exp(Z)$$
其中
$$Z = X + Y + \sum_{n=2}^\infty \frac{1}{n} \sum_{\substack{1 \le i \le n \\ 0 < m_1 < p_1, \dots, m_i, p_i}} \frac{(-1)^{i-1}}{i} \frac{[\text{ad}_{X}^{m_1}\text{ad}_{Y}^{p_1} \cdots \text{ad}_{X}^{m_i}\text{ad}_{Y}^{p_i-1}Y]}{m_1!p_1!\cdots m_i!p_i!}$$

**证明**（微分方程方法）：

**步骤 1**：对固定的 $Y$，考虑 $Z(t) = \log(\exp(tX)\exp(Y))$，其中 $t$ 是实参数。目标是求 $Z(1)$。

**步骤 2**：求导 $\frac{d}{dt}Z(t)$。对矩阵李群，有公式
$$\frac{d}{dt}Z(t) = \frac{\text{ad}_{Z(t)}}{1 - e^{-\text{ad}_{Z(t)}}}(X)$$
其中 $\frac{\text{ad}_{Z}}{1 - e^{-\text{ad}_{Z}}} = \sum_{k=0}^\infty \frac{B_k}{k!}\text{ad}_{Z}^k$，$B_k$ 是 Bernoulli 数。

**步骤 3**：注意 $Z(0) = Y$，且 $Z(t)$ 满足微分方程
$$\frac{d}{dt}Z(t) = \sum_{k=0}^\infty \frac{B_k}{k!}\text{ad}_{Z(t)}^k(X)$$

**步骤 4**：通过迭代求解该微分方程。将 $Z(t)$ 展开为 $t$ 的幂级数 $Z(t) = \sum_{n=0}^\infty Z_n t^n$，其中 $Z_0 = Y$。

**步骤 5**：代入微分方程，逐项比较系数：
- $Z_1 = X$
- $Z_2 = \frac{1}{2}[X,Y]$
- $Z_3 = \frac{1}{12}[X,[X,Y]] - \frac{1}{12}[Y,[X,Y]]$
- 更高阶项以此类推。

**步骤 6**：取 $t=1$ 得 $Z = Z(1)$，即 BCH 公式。

**Dynkin 显式公式**：BCH 公式的通项可以写为
$$Z = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} \sum_{\substack{r_i + s_i > 0 \\ 1 \le i \le n}} \frac{[X^{r_1}Y^{s_1}\cdots X^{r_n}Y^{s_n}]}{\left(\sum_{i=1}^n (r_i + s_i)\right) \prod_{i=1}^n r_i! s_i!}$$
其中 $[X^{r_1}Y^{s_1}\cdots X^{r_n}Y^{s_n}]$ 表示嵌套李括号
$$\underbrace{[X,[X,\cdots[X}_{r_1}, \underbrace{[Y,[Y,\cdots[Y}_{s_1}, \cdots \underbrace{[X,[X,\cdots[X}_{r_n}, \underbrace{[Y,[Y,\cdots[Y}_{s_n-1} Y]\cdots]$$

**推论**：由 BCH 公式可知，李代数 $\mathfrak{g}$ 上的李括号完全决定了李群 $G$ 在单位元附近的乘法结构。具体地，若两个李群有同构的李代数，则它们在单位元附近是局部同构的。$\square$