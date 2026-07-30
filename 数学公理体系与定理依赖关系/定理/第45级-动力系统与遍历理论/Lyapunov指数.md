# Lyapunov指数

## 介绍

Lyapunov指数（Lyapunov Exponent）是动力系统理论中刻画轨道稳定性和混沌程度的核心量，由俄罗斯数学家 Aleksandr Lyapunov 在19世纪末研究稳定性问题时引入。Lyapunov指数衡量相空间中相邻轨道的平均指数发散（或收敛）速率。正Lyapunov指数标志着系统对初始条件的敏感依赖性——混沌的典型特征。Lyapunov指数现已成为动力系统、遍历理论、混沌理论和时间序列分析中最基本也是最重要的概念之一。

## 分析

**前置依赖**：动力系统、常微分方程、线性化、矩阵的特征值、微分流形、遍历理论。

**定理内容**：设 $M$ 是光滑流形，$f: M \to M$ 是 $C^1$ 映射，$\mu$ 是 $f$-不变遍历概率测度。对 $\mu$-几乎处处 $x \in M$ 和所有 $v \in T_xM \setminus \{0\}$，定义Lyapunov指数
$$\lambda(x, v) = \limsup_{n \to \infty} \frac{1}{n} \log \|Df^n(x) \cdot v\|$$
则存在实数 $\lambda_1(x) > \lambda_2(x) > \cdots > \lambda_k(x)$ 和对应的子空间链
$$\{0\} = V_0(x) \subsetneq V_1(x) \subsetneq \cdots \subsetneq V_k(x) = T_xM$$
使得对 $v \in V_i(x) \setminus V_{i-1}(x)$，有 $\lambda(x, v) = \lambda_i(x)$。对连续动力系统 $\varphi_t$，定义
$$\lambda(x, v) = \limsup_{t \to \infty} \frac{1}{t} \log \|D\varphi_t(x) \cdot v\|$$

**数学内涵**：
- Lyapunov指数刻画了相空间各方向上的平均指数增长率。
- 最大Lyapunov指数 $\lambda_{\max} > 0$ 是混沌的判据。
- 所有Lyapunov指数之和等于 $\lim_{n\to\infty} \frac{1}{n} \log |\det Df^n(x)|$，对保守系统为零。
- 对遍历系统，Lyapunov指数在 $\mu$-几乎处处是常数（不依赖于 $x$）。

**证明策略**：
1. 考虑线性化系统 $v_{n+1} = Df(x_n) \cdot v_n$。
2. 利用Oseledets乘法遍历定理（Multiplicative Ergodic Theorem）证明几乎处处存在极限。
3. 通过极分解或Gram-Schmidt正交化构造出各指数对应的子空间。

## 思考过程

Lyapunov指数是动力系统理论中连接局部线性化行为与全局混沌性质的桥梁。其核心思想源于线性代数中矩阵乘积的增长率：一个线性映射 $A$ 的迭代 $A^n$ 的增长率由其特征值的模决定。对于非线性系统，切映射 $Df^n(x)$ 的增长率由Lyapunov指数刻画，它是"非线性特征值"的推广。

Oseledets乘法遍历定理是Lyapunov指数理论的基础，它断言在遍历假设下，乘积 $Df^n(x)$ 的奇异性状几乎处处有良好定义的极限。这一定理是遍历理论在动力系统中最深刻的应用之一。

## 证明过程

**定理**（Lyapunov指数与Oseledets乘法遍历定理）：设 $f: M \to M$ 是紧致流形 $M$ 上的 $C^1$ 映射，$\mu$ 是 $f$-不变概率测度。则对 $\mu$-几乎处处 $x \in M$，存在整数 $k(x)$ 和实数 $\lambda_1(x) > \cdots > \lambda_{k(x)}(x)$，以及 $T_xM$ 的滤子
$$\{0\} = V_0(x) \subsetneq V_1(x) \subsetneq \cdots \subsetneq V_{k(x)}(x) = T_xM$$
满足 $Df(x)(V_i(x)) = V_i(f(x))$，且对任意 $v \in V_i(x) \setminus V_{i-1}(x)$，
$$\lim_{n \to \infty} \frac{1}{n} \log \|Df^n(x) \cdot v\| = \lambda_i(x)$$

**证明**：

### 1. 线性化系统与逐点行为

对给定轨道 $\{x_n = f^n(x)\}$，考虑线性化映射序列 $A_n = Df(x_n): T_{x_n}M \to T_{x_{n+1}}M$。定义乘积
$$P_n = A_{n-1} \circ \cdots \circ A_0: T_xM \to T_{x_n}M$$
则 $P_n = Df^n(x)$。

### 2. 奇异值分解

对每个 $n$，对 $P_n$ 进行奇异值分解。设 $s_1^{(n)}(x) \geq s_2^{(n)}(x) \geq \cdots \geq s_d^{(n)}(x) > 0$ 是 $P_n$ 的奇异值（即 $\sqrt{(P_n^* P_n)}$ 的特征值）。定义
$$\lambda_i(x) = \lim_{n \to \infty} \frac{1}{n} \log s_i^{(n)}(x)$$
若极限存在。

### 3. Oseledets正则性

称 $x$ 是Oseledets正则点，若以下极限存在：
$$\lim_{n \to \infty} (P_n^* P_n)^{1/2n} = \Lambda_x$$
其中 $\Lambda_x$ 是 $T_xM$ 上的正定对称算子。记其特征值为 $e^{\lambda_1(x)} > \cdots > e^{\lambda_{k(x)}(x)}$，对应的特征子空间为 $E_1(x), \ldots, E_{k(x)}(x)$。

### 4. 滤子构造

定义 $V_i(x) = E_1(x) \oplus \cdots \oplus E_i(x)$。则对任意 $v \in V_i(x) \setminus V_{i-1}(x)$，有
$$\lim_{n \to \infty} \frac{1}{n} \log \|P_n v\| = \lambda_i(x)$$

### 5. Oseledets定理的断言

Oseledets乘法遍历定理断言：$\mu$-几乎处处点都是Oseledets正则点。证明的关键步骤是：
1. 利用Kingman次可加遍历定理处理 $\log \|P_n v\|$ 的次可加性。
2. 通过极分解 $P_n = O_n \cdot S_n$（$O_n$正交，$S_n$对称正定）将问题转化为对称矩阵乘积的极限问题。
3. 应用Furstenberg-Kesten定理证明 $\frac{1}{n} \log \|P_n\|$ 几乎处处收敛。

### 6. 连续动力系统情形

对连续系统 $\varphi_t$，定义
$$\lambda(x, v) = \limsup_{t \to \infty} \frac{1}{t} \log \|D\varphi_t(x) \cdot v\|$$
Oseledets定理同样适用于线性化系统 $v(t) = D\varphi_t(x) \cdot v_0$，只需将离散乘积替换为连续时间的发展算子。$\square$

**推论**：若 $\mu$ 是遍历测度，则Lyapunov指数 $\lambda_i(x)$ 和维数 $k(x)$ 在 $\mu$-几乎处处为常数，记为 $\lambda_i$ 和 $k$。$\square$