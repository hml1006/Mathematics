# Fredholm二择一定理

## 介绍

Fredholm二择一定理（Fredholm Alternative）是积分方程理论和泛函分析中的经典定理，由瑞典数学家 Erik Ivar Fredholm 在 1903 年研究积分方程时提出。它断言：对于紧扰动恒等算子的算子 $I - T$（其中 $T$ 是紧算子），要么方程 $(I - T)x = y$ 对任意右端 $y$ 有唯一解，要么齐次方程 $(I - T)x = 0$ 有非平凡解。这个"二择一"性质是线性积分方程理论的核心，也是偏微分方程中许多存在性结果的基础。

## 分析

**定理的精确表述**：设 $X$ 是 Banach 空间，$T: X \to X$ 是紧线性算子。则：

1. $\dim \ker(I - T) < \infty$；
2. $\operatorname{Range}(I - T)$ 是闭的；
3. $\operatorname{codim} \operatorname{Range}(I - T) = \dim \ker(I - T) < \infty$；
4. $\ker(I - T) = \{0\}$ 当且仅当 $\operatorname{Range}(I - T) = X$（Fredholm 二择一）。

**等价形式**：对于方程 $x - T x = y$，以下两种情形必居其一且仅居其一：
- **第一择一**：对任意 $y \in X$，方程有唯一解 $x \in X$；
- **第二择一**：齐次方程 $x - T x = 0$ 有非平凡解，此时方程 $x - T x = y$ 可解的充要条件是 $y$ 与 $\ker(I - T^*)$ 正交（即 $f(y) = 0$ 对所有 $f \in \ker(I - T^*)$ 成立）。

**关键要点**：

- 定理的核心是：$I - T$ 是 Fredholm 算子——它的核与余核都是有限维的。
- 对偶版本：$I - T^*$ 也有相同的性质，且 $\dim \ker(I - T) = \dim \ker(I - T^*)$。
- 这个定理是线性积分方程理论的基石——对于 Fredholm 积分方程 $x(s) - \int_a^b K(s, t) x(t) dt = y(s)$，若核 $K$ 是连续的（或平方可积的），则对应的积分算子 $T$ 是紧算子。

## 思考过程

Fredholm 二择一定理的证明分为几个层面：

1. **核的有限维性**：利用紧算子的性质——若 $I - T$ 的核是无穷维的，则存在单位向量列 $\{x_n\} \subset \ker(I - T)$，则 $T x_n = x_n$，但 $\{T x_n\}$ 有收敛子列（因为 $T$ 紧），矛盾。

2. **值域的闭性**：使用标准技巧——若 $y_n = (I - T)x_n \to y$，需要证明 $y \in \operatorname{Range}(I - T)$。将 $\{x_n\}$ 分解为核方向的分量和正交补方向的分量，利用紧性提取收敛子列。

3. **指标为零**（$\dim \ker = \operatorname{codim} \operatorname{Range}$）：利用对偶理论和紧算子的性质，或者通过构造有限秩逼近来证明。

## 证明过程

**证明**：设 $X$ 是 Banach 空间，$T: X \to X$ 是紧线性算子。

**引理 1**：$\ker(I - T)$ 是有限维的。

**证明**：设 $B = \{x \in \ker(I - T) \mid \|x\| \le 1\}$ 是 $\ker(I - T)$ 中的闭单位球。对任意 $x \in B$，$x = T x$，故 $B = T(B)$。由于 $T$ 是紧算子，$T(B)$ 是相对紧集，故 $B$ 是紧集。由 Riesz 引理，$\ker(I - T)$ 是有限维的。$\square$

**引理 2**：$\operatorname{Range}(I - T)$ 是闭的。

**证明**：设 $y_n = (I - T)x_n \to y$。记 $N = \ker(I - T)$，$d(x_n, N) = \inf_{z \in N} \|x_n - z\|$。选取 $z_n \in N$ 使得 $\|x_n - z_n\| \le d(x_n, N) + 1/n$。令 $u_n = x_n - z_n$，则 $(I - T)u_n = (I - T)x_n = y_n$（因为 $z_n \in N$），且 $d(u_n, N) = d(x_n, N)$。

若 $\{u_n\}$ 有界，则由 $T$ 的紧性，$\{T u_n\}$ 有收敛子列，$\{u_n\}$ 也有收敛子列（因为 $u_n = T u_n + y_n$），设 $u_{n_k} \to u$，则 $y = \lim y_{n_k} = \lim (I - T)u_{n_k} = (I - T)u$，故 $y \in \operatorname{Range}(I - T)$。

若 $\{u_n\}$ 无界，考虑归一化 $v_n = u_n / \|u_n\|$，则 $(I - T)v_n = y_n / \|u_n\| \to 0$。由 $T$ 的紧性，$\{T v_n\}$ 有收敛子列，$\{v_n\}$ 也有收敛子列，设 $v_{n_k} \to v$，则 $(I - T)v = 0$，即 $v \in N$。但 $d(v_n, N) = d(u_n, N)/\|u_n\| \to 0$，故 $v \in N$ 且 $\|v\| = 1$，矛盾于 $v_n$ 的构造。因此 $\{u_n\}$ 必须有界。$\square$

**引理 3**：$\operatorname{codim} \operatorname{Range}(I - T) = \dim \ker(I - T)$。

**证明**：考虑 $T$ 的共轭算子 $T^*: X^* \to X^*$，$T^*$ 也是紧算子。由引理 1，$\ker(I - T^*)$ 是有限维的。可以证明 $\operatorname{Range}(I - T)^\perp = \ker(I - T^*)$。由 Hahn-Banach 定理，$\operatorname{codim} \operatorname{Range}(I - T) = \dim \operatorname{Range}(I - T)^\perp = \dim \ker(I - T^*)$。

类似地，对 $T^*$ 应用相同论证，$\dim \ker(I - T^*) = \operatorname{codim} \operatorname{Range}(I - T^*) = \dim \ker(I - T)$（因为 $\ker(I - T)^\perp = \operatorname{Range}(I - T^*)$ 且 $\dim \ker(I - T) = \operatorname{codim} \operatorname{Range}(I - T^*)$）。故 $\dim \ker(I - T) = \operatorname{codim} \operatorname{Range}(I - T)$。$\square$

**Fredholm 二择一**：由引理 3，$\dim \ker(I - T) = 0$ 当且仅当 $\operatorname{codim} \operatorname{Range}(I - T) = 0$，即 $\ker(I - T) = \{0\}$ 当且仅当 $\operatorname{Range}(I - T) = X$。$\square$

**应用——积分方程**：考虑 Fredholm 积分方程

$$
x(s) - \int_a^b K(s, t) x(t) dt = y(s), \quad s \in [a, b],
$$

其中 $K$ 是连续核。定义算子 $T: C[a,b] \to C[a,b]$ 为 $(T x)(s) = \int_a^b K(s, t) x(t) dt$，则 $T$ 是紧算子。Fredholm 二择一定理保证了上述积分方程的解的存在唯一性完全由齐次方程的非平凡解决定。