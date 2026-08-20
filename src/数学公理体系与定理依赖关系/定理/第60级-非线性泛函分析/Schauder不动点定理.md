# Schauder不动点定理

> **一句话大白话**：把一个紧凸集合映到自身的连续变换，无论怎样都会有至少一个点被"稳稳钉住"不动——这是压缩映射思想在无穷维空间的推广。
>
> **小例子**：Banach 空间中闭凸紧集 $K$ 上连续映射 $f:K\to K$ 必存在 $x^*\in K$ 使 $f(x^*)=x^*$，常用于证明非线性积分方程有解。

## 一、定理介绍

Schauder 不动点定理（Schauder Fixed Point Theorem）由 Juliusz Schauder 于 1930 年提出，是非线性泛函分析中最基本的不动点定理之一。它将 Brouwer 不动点定理从有限维推广到无穷维 Banach 空间，断言：**Banach 空间中紧凸集到自身的连续映射必有不动点**。

该定理是研究非线性偏微分方程、积分方程、动力系统等存在性问题最常用的工具之一，相较于 Banach 不动点定理，它不要求映射是压缩的，仅要求连续性与紧性，因此适用范围远为广泛。

## 二、原理思路

Schauder 不动点定理的核心思想可以归纳为以下几点：

1. **从有限维到无穷维的过渡**：Brouwer 不动点定理在有限维空间 $\mathbb{R}^n$ 中保证紧凸集上自映射的不动点存在。Schauder 定理通过"有限维逼近"将结论推广到无穷维。

2. **紧性的核心作用**：在无穷维空间中，单位球不再紧致，因此直接套用 Brouwer 定理行不通。Schauder 定理通过要求映射是**紧映射**（将闭有界集映为相对紧集）来恢复紧性。

3. **有限维逼近（Schauder 投影技巧）**：将紧映射用有限维映射逼近，每个逼近映射由 Brouwer 定理给出不动点 $x_n$；再利用紧性使 $\{x_n\}$ 收敛到原映射的不动点。

4. **凸性的必要性**：凸性保证了有限维逼近时像点仍落在集合内部，是有限维投影构造的关键。

## 三、定理的严格表述

**Schauder 不动点定理（一般形式）**：设 $X$ 是 Banach 空间，$C \subset X$ 是非空闭凸子集（不必有界），$T: C \to C$ 是连续映射。若 $T$ 是**紧映射**，即 $T$ 将 $C$ 的有界子集映为相对紧集，且 $T(C)$ 有界，则 $T$ 在 $C$ 中存在不动点，即存在 $x^* \in C$ 使
$$T(x^*) = x^*.$$

**Schauder 不动点定理（紧凸集形式）**：设 $X$ 是 Banach 空间，$K \subset X$ 是非空紧凸子集，$T: K \to K$ 是连续映射，则 $T$ 在 $K$ 中存在不动点。

**紧算子形式（最常用）**：设 $X$ 是 Banach 空间，$C \subset X$ 是非空有界闭凸子集，$T: C \to C$ 是**全连续算子**（连续且将弱收敛序列映为强收敛序列，等价于连续紧映射），则 $T$ 存在不动点。

## 四、证明过程

下面证明紧凸集形式（其一般形式可通过考虑 $\overline{T(C)}$ 这个紧凸子集化为此形式）。

设 $K \subset X$ 是非空紧凸集，$T: K \to K$ 连续。

**步骤 1：有限维逼近——构造 Schauder 投影**

由于 $K$ 紧，对任意 $n \geq 1$，存在有限 $\frac{1}{n}$-网 $\{x_1^{(n)}, \ldots, x_{N(n)}^{(n)}\} \subset K$，即对任意 $x \in K$，存在 $i$ 使 $\|x - x_i^{(n)}\| < 1/n$。

定义 Schauder 投影 $P_n: K \to \operatorname{conv}\{x_1^{(n)}, \ldots, x_{N(n)}^{(n)}\}$ 为
$$P_n(x) = \sum_{i=1}^{N(n)} \mu_i(x) x_i^{(n)},$$
其中
$$\mu_i(x) = \frac{\max(0, \frac{1}{n} - \|x - x_i^{(n)}\|)}{\sum_{j=1}^{N(n)} \max(0, \frac{1}{n} - \|x - x_j^{(n)}\|)}.$$

性质：
- $\mu_i(x) \geq 0$，$\sum_i \mu_i(x) = 1$；
- $\mu_i$ 连续；
- $P_n$ 连续；
- $\|P_n(x) - x\| \leq 1/n$ 对所有 $x \in K$（因为仅距离小于 $1/n$ 的 $x_i$ 贡献非零）；
- $P_n(K) \subset K$（由 $K$ 凸性）。

**步骤 2：构造有限维映射并应用 Brouwer 定理**

令 $K_n = \operatorname{conv}\{x_1^{(n)}, \ldots, x_{N(n)}^{(n)}\} \subset K$，$K_n$ 是有限维（维数 $\leq N(n) - 1$）紧凸集。

定义 $T_n: K_n \to K_n$ 为
$$T_n(x) = P_n(T(x)).$$
由于 $T(K) \subset K$ 且 $P_n(K) \subset K_n$，故 $T_n(K_n) \subset K_n$，且 $T_n$ 连续。

由 Brouwer 不动点定理，存在 $x_n \in K_n$ 使
$$T_n(x_n) = x_n, \quad \text{即 } P_n(T(x_n)) = x_n.$$

**步骤 3：利用紧性取极限**

由于 $K$ 紧，$\{x_n\}$ 存在子列（仍记为 $\{x_n\}$）收敛到某点 $x^* \in K$。

**步骤 4：验证 $x^*$ 是不动点**

由 $P_n(T(x_n)) = x_n$ 与 $\|P_n(y) - y\| \leq 1/n$（对任意 $y$），
$$\|T(x_n) - x_n\| = \|T(x_n) - P_n(T(x_n))\| \leq \frac{1}{n} \to 0.$$

由 $T$ 连续与 $x_n \to x^*$，
$$T(x^*) = \lim_{n \to \infty} T(x_n) = \lim_{n \to \infty} x_n = x^*.$$

故 $x^*$ 是 $T$ 的不动点。$\square$

**一般形式的归约**：设 $C$ 非空闭凸，$T: C \to C$ 紧连续且 $T(C)$ 有界。令 $\widetilde K = \overline{\operatorname{conv}(T(C))}$，则 $\widetilde K \subset C$（由 $C$ 闭凸），$\widetilde K$ 紧（因为 $T(C)$ 相对紧，其闭凸包仍紧——Mazur 定理），且 $T(\widetilde K) \subset T(C) \subset \widetilde K$。对 $T|_{\widetilde K}: \widetilde K \to \widetilde K$ 应用紧凸集形式即得不动点。

## 五、应用与意义

**理论意义**：

1. **Brouwer 定理的无穷维推广**：Schauder 定理是有限维 Brouwer 不动点定理在 Banach 空间的自然推广，是非线性泛函分析的奠基性结果。

2. **紧性代替凸性-压缩性**：相比 Banach 不动点定理的压缩性要求，Schauder 仅需连续与紧性，能够处理非压缩的强非线性问题。

3. **拓扑方法在分析中的桥梁**：将代数拓扑（Brouwer 度）与泛函分析（紧算子理论）相结合。

**应用领域**：

1. **常微分方程初值问题**：考虑
$$\dot x = f(t, x), \quad x(0) = x_0,$$
通过将解转化为积分算子 $T(x)(t) = x_0 + \int_0^t f(s, x(s)) ds$ 的不动点，应用 Schauder 定理证明解的存在性（Picard-Lindelöf 定理的另一种证明，不要求 Lipschitz 条件，仅需连续性）。

2. **椭圆方程 Dirichlet 问题**：
$$-\Delta u = f(x, u), \quad u|_{\partial \Omega} = 0,$$
通过将其转化为紧算子（Schauder 不动点定理或 Leray-Schauder 方法）的不动点，证明弱解或经典解的存在性。

3. **积分方程**：Fredholm 积分方程与 Volterra 积分方程
$$u(x) = \int_\Omega K(x, y) f(y, u(y))\, dy$$
利用 Schauder 定理证明解的存在性。

4. **动力系统不变集**：证明流的不变集存在性。

5. **博弈论与经济学**：在一般均衡存在性证明中（Arrow-Debreu 模型），Schauder 定理或其推广（如 Kakutani 不动点定理）是核心工具。

**推广**：
- **Leray-Schauder 定理**：结合拓扑度理论给出更精细的不动点存在性条件。
- **Krasnoselskii 定理**：压缩算子与紧算子之和的不动点定理。
- **Tychonoff 不动点定理**：局部凸拓扑向量空间上的推广。
- **Fan-Glicksberg 定理**：自反 Banach 空间中弱紧凸集上的推广，应用于博弈论。
