# von Neumann平均遍历定理

## 介绍

von Neumann平均遍历定理（von Neumann Mean Ergodic Theorem）由John von Neumann于1932年证明，是遍历理论中第一个严格的数学结果。该定理从Hilbert空间的角度研究保测变换的时间平均收敛性，断言：在保测变换下，$L^2$ 函数的时间平均在 $L^2$ 范数意义下收敛到其空间平均的投影。与Birkhoff逐点遍历定理不同，von Neumann定理关注的是平均收敛（而非几乎处处收敛），且仅适用于 $L^2$ 函数。该定理为泛函分析方法在遍历理论中的应用开创了先河。

## 分析

**前置依赖**：测度论、Hilbert空间、正交投影、酉算子、保测变换、Hilbert空间中的平均收敛。

**定理内容**：设 $(X, \mathcal{F}, \mu)$ 是概率空间，$T: X \to X$ 是保测变换。定义Koopman算子 $U_T: L^2(X, \mu) \to L^2(X, \mu)$ 为 $U_T f = f \circ T$。则 $U_T$ 是酉算子。对任意 $f \in L^2(X, \mu)$，部分和序列
$$\frac{1}{n} \sum_{k=0}^{n-1} U_T^k f$$
在 $L^2$ 范数意义下收敛到 $P f$，其中 $P: L^2 \to L^2$ 是到 $T$-不变子空间 $\{g \in L^2 \mid U_T g = g\}$ 上的正交投影。

**数学内涵**：
- Koopman算子 $U_T$ 将保测变换 $T$ 提升为Hilbert空间上的酉算子，从而可用泛函分析的工具研究。
- 时间平均 $\frac{1}{n}\sum_{k=0}^{n-1} f(T^k(x))$ 在 $L^2$ 意义下收敛到不变函数 $f^*$。
- 当 $T$ 遍历时，$P f = \int_X f \, d\mu$（常数函数），即时间平均在 $L^2$ 范数下收敛到空间平均。
- 该定理适用于所有 $L^2$ 函数，但不提供逐点收敛信息。

**证明策略**：
1. 将Koopman算子 $U_T$ 视为酉算子，利用谱定理或Hilbert空间的正交分解。
2. 将 $L^2$ 分解为不变子空间和其正交补：$L^2 = \ker(I - U_T) \oplus \overline{\operatorname{ran}(I - U_T)}$。
3. 证明在 $\overline{\operatorname{ran}(I - U_T)}$ 上时间平均收敛到 $0$，在 $\ker(I - U_T)$ 上时间平均是常数。

## 思考过程

von Neumann平均遍历定理的核心思想是：时间平均算子 $A_n = \frac{1}{n} \sum_{k=0}^{n-1} U_T^k$ 在Hilbert空间上强收敛到正交投影 $P$。这一收敛性可以通过将 $U_T$ 进行谱分解来直观理解——在 $U_T$ 的特征值 $1$ 对应的特征空间上，$A_n$ 恒为恒等映射；在其余部分，$A_n$ 的范数以 $O(1/n)$ 趋于零。

该定理与Birkhoff定理形成互补：von Neumann定理给出 $L^2$ 收敛，Birkhoff定理给出几乎处处收敛。一般而言，$L^2$ 收敛比几乎处处收敛更容易证明，但提供的信息更弱——两者不可相互替代。

## 证明过程

**定理**（von Neumann平均遍历定理）：设 $(X, \mathcal{F}, \mu)$ 是概率空间，$T: X \to X$ 保测，$U_T$ 是Koopman算子。则对任意 $f \in L^2(X, \mu)$，
$$\lim_{n \to \infty} \left\| \frac{1}{n} \sum_{k=0}^{n-1} U_T^k f - P f \right\|_{L^2} = 0$$
其中 $P$ 是到 $U_T$-不变子空间 $\{g \in L^2 \mid U_T g = g\}$ 上的正交投影。

**证明**：

### 1. Koopman算子的酉性

对任意 $f, g \in L^2$，
$$\langle U_T f, U_T g \rangle = \int_X f(T(x)) \overline{g(T(x))} \, d\mu(x) = \int_X f(x) \overline{g(x)} \, d\mu(x) = \langle f, g \rangle$$
其中第二个等式由 $T$ 的保测性保证。因此 $U_T$ 是酉算子，$U_T^{-1} = U_T^*$。

### 2. 正交分解

令 $I$ 为恒等算子。考虑子空间
$$F = \ker(I - U_T) = \{g \in L^2 \mid U_T g = g\}$$
和
$$G = \overline{\operatorname{ran}(I - U_T)} = \overline{\{h \in L^2 \mid h = g - U_T g, \; g \in L^2\}}$$
由于 $U_T$ 是酉算子，$F$ 和 $G$ 互为正交补：$L^2 = F \oplus G$。事实上，$g \in F^\perp$ 当且仅当 $\langle g, h - U_T h \rangle = 0$ 对所有 $h$ 成立，等价于 $U_T^* g = g$，即 $U_T^{-1} g = g$，亦即 $U_T g = g$，故 $F^\perp = F$。

### 3. 在 $F$ 上的收敛性

若 $f \in F$，则 $U_T f = f$，从而 $\frac{1}{n} \sum_{k=0}^{n-1} U_T^k f = f$，极限就是 $f$ 本身，且 $P f = f$。

### 4. 在 $G$ 上的收敛性

首先考虑 $G$ 的稠密子集 $\operatorname{ran}(I - U_T)$。若 $f = g - U_T g$，则
$$\frac{1}{n} \sum_{k=0}^{n-1} U_T^k f = \frac{1}{n} \sum_{k=0}^{n-1} (U_T^k g - U_T^{k+1} g) = \frac{1}{n} (g - U_T^n g)$$
因此
$$\left\| \frac{1}{n} \sum_{k=0}^{n-1} U_T^k f \right\|_{L^2} \leq \frac{2\|g\|_{L^2}}{n} \to 0 \quad (n \to \infty)$$

对任意 $f \in G$，取 $\{f_m\} \subseteq \operatorname{ran}(I - U_T)$ 使得 $f_m \to f$。则
$$\left\| \frac{1}{n} \sum_{k=0}^{n-1} U_T^k f \right\| \leq \left\| \frac{1}{n} \sum_{k=0}^{n-1} U_T^k (f - f_m) \right\| + \left\| \frac{1}{n} \sum_{k=0}^{n-1} U_T^k f_m \right\|$$
第一项不超过 $\|f - f_m\|$（因为 $\|U_T\| = 1$），第二项可任意小。令 $n \to \infty$ 再令 $m \to \infty$ 即得收敛到 $0$。

### 5. 一般情况

对任意 $f \in L^2$，由正交分解 $f = f_F + f_G$，其中 $f_F = P f \in F$，$f_G \in G$。则
$$\frac{1}{n} \sum_{k=0}^{n-1} U_T^k f = f_F + \frac{1}{n} \sum_{k=0}^{n-1} U_T^k f_G \to f_F = P f \quad (\text{在 } L^2 \text{ 中})$$
$\square$

**推论**（遍历情形）：若 $T$ 是遍历的，则不变函数几乎处处为常数，因此 $P f = \int_X f \, d\mu \cdot \mathbf{1}_X$，从而
$$\lim_{n \to \infty} \left\| \frac{1}{n} \sum_{k=0}^{n-1} f \circ T^k - \int_X f \, d\mu \right\|_{L^2} = 0$$
$\square$