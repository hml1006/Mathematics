# 第 73 级：Hopf 代数与量子群 (Hopf Algebras and Quantum Groups)

> Hopf 代数与量子群是 20 世纪 80 年代以来数学物理中最深刻的发展之一。Hopf 代数以德国数学家 Heinz Hopf 命名，是同时具有代数结构和余代数结构的代数系统，满足相容性条件。量子群作为 Drinfeld 和 Jimbo 在解决量子 Yang-Baxter 方程过程中引入的 Hopf 代数变形，是李群表示论的非交换非余交换推广。量子群为三维流形的拓扑不变量（如 Jones 多项式、Witten 不变量）提供了统一的代数框架，并深刻影响了低维拓扑、表示论、数学物理和范畴论。本课程从 Hopf 代数的基本定义出发，系统介绍量子群 $U_q(\mathfrak{sl}_2)$ 的表示理论、$R$-矩阵与 Yang-Baxter 方程、辫子张量范畴以及量子不变量等核心内容。

---

## 1. 学习目标

1. 理解 Hopf 代数的定义与基本性质（代数、余代数、对极映射）。
2. 掌握对偶配对与卷积代数的概念。
3. 理解余模及其与模的关系。
4. 掌握 Drinfeld 量子双与量子群 $U_q(\mathfrak{sl}_2)$ 的构造。
5. 理解 $R$-矩阵与 Yang-Baxter 方程的关系。
6. 掌握量子群 $U_q(\mathfrak{sl}_2)$ 的表示分类。
7. 理解辫子张量范畴与拟三角 Hopf 代数的概念。
8. 掌握量子迹与 Jones 多项式的关系。
9. 了解 Tannaka-Krein 对偶定理的基本思想。

---

## 2. 核心概念

### 2.1 Hopf 代数定义

**定义 2.1**（代数）域 $\mathbb{k}$ 上的 **代数** $(A, m, \eta)$ 是一个 $\mathbb{k}$-向量空间 $A$，配备：
- 乘法 $m: A \otimes A \to A$，是线性映射；
- 单位 $\eta: \mathbb{k} \to A$，是线性映射；
满足结合律和单位律。

**定义 2.2**（余代数）域 $\mathbb{k}$ 上的 **余代数** $(C, \Delta, \varepsilon)$ 是一个 $\mathbb{k}$-向量空间 $C$，配备：
- 余乘法 $\Delta: C \to C \otimes C$，是线性映射；
- 余单位 $\varepsilon: C \to \mathbb{k}$，是线性映射；
满足余结合律和余单位律。

**定义 2.3**（双代数）**双代数** $(H, m, \eta, \Delta, \varepsilon)$ 同时是代数和余代数，且 $\Delta$ 和 $\varepsilon$ 是代数同态（或等价地，$m$ 和 $\eta$ 是余代数同态）。

**定义 2.4**（Hopf 代数）**Hopf 代数** $(H, m, \eta, \Delta, \varepsilon, S)$ 是一个双代数，配备 **对极映射** $S: H \to H$，满足：

$$
m \circ (S \otimes \operatorname{id}) \circ \Delta = \eta \circ \varepsilon = m \circ (\operatorname{id} \otimes S) \circ \Delta.
$$

用 Sweedler 记号 $\Delta(h) = \sum_{(h)} h_{(1)} \otimes h_{(2)}$，对极条件为：

$$
\sum_{(h)} S(h_{(1)}) h_{(2)} = \varepsilon(h) \cdot 1 = \sum_{(h)} h_{(1)} S(h_{(2)}).
$$

**例 2.1**（群代数）有限群 $G$ 的群代数 $\mathbb{k}[G]$ 是 Hopf 代数，其中：
- $\Delta(g) = g \otimes g$，$\varepsilon(g) = 1$，$S(g) = g^{-1}$ 对 $g \in G$。

**例 2.2**（李代数的包络代数）李代数 $\mathfrak{g}$ 的泛包络代数 $U(\mathfrak{g})$ 是 Hopf 代数，其中：
- $\Delta(X) = X \otimes 1 + 1 \otimes X$，$\varepsilon(X) = 0$，$S(X) = -X$ 对 $X \in \mathfrak{g}$。

### 2.2 对偶配对

**定义 2.5**（对偶配对）两个 Hopf 代数 $H$ 和 $K$ 之间的 **对偶配对** 是一个非退化双线性形式 $\langle \cdot, \cdot \rangle: K \otimes H \to \mathbb{k}$，满足：

$$
\langle xy, h \rangle = \langle x \otimes y, \Delta_H(h) \rangle, \quad \langle x, gh \rangle = \langle \Delta_K(x), g \otimes h \rangle,
$$
$$
\langle 1_K, h \rangle = \varepsilon_H(h), \quad \langle x, 1_H \rangle = \varepsilon_K(x),
$$
$$
\langle S_K(x), h \rangle = \langle x, S_H(h) \rangle.
$$

### 2.3 卷积代数

**定义 2.6**（卷积代数）设 $(C, \Delta, \varepsilon)$ 是余代数，$(A, m, \eta)$ 是代数。则 $\operatorname{Hom}(C, A)$ 上的 **卷积** 定义为：

$$
(f * g)(c) = m(f \otimes g)(\Delta(c)) = \sum_{(c)} f(c_{(1)}) g(c_{(2)}).
$$

$(\operatorname{Hom}(C, A), *, \eta \circ \varepsilon)$ 构成一个代数，称为 **卷积代数**。

### 2.4 余模

**定义 2.7**（余模）设 $H$ 是 Hopf 代数。一个 **右 $H$-余模** 是一个向量空间 $M$ 配备 **余作用** $\rho: M \to M \otimes H$，满足：
1. $(\rho \otimes \operatorname{id}) \circ \rho = (\operatorname{id} \otimes \Delta) \circ \rho$（余结合律）；
2. $(\operatorname{id} \otimes \varepsilon) \circ \rho = \operatorname{id}$（余单位律）。

用 Sweedler 记号 $\rho(m) = \sum_{(m)} m_{(0)} \otimes m_{(1)}$。

### 2.5 Drinfeld 量子双

**定义 2.8**（Drinfeld 量子双）设 $H$ 是有限维 Hopf 代数。**Drinfeld 量子双** $D(H)$ 是 $H$ 和 $H^{*\text{op}}$ 在某种意义下的双积，其作为向量空间为 $H \otimes H^*$，具有特定的代数、余代数结构和 $R$-矩阵。

### 2.6 量子群 $U_q(\mathfrak{sl}_2)$

**定义 2.9**（量子群 $U_q(\mathfrak{sl}_2)$）设 $q \in \mathbb{k}^\times$ 且 $q^2 \neq 1$。**量子群** $U_q(\mathfrak{sl}_2)$ 是由生成元 $E, F, K, K^{-1}$ 满足以下关系的 $\mathbb{k}$-代数：

$$
KK^{-1} = K^{-1}K = 1,
$$
$$
KEK^{-1} = q^2 E, \quad KFK^{-1} = q^{-2} F,
$$
$$
[E, F] = \frac{K - K^{-1}}{q - q^{-1}}.
$$

余代数结构和对极映射为：

$$
\Delta(K) = K \otimes K, \quad \varepsilon(K) = 1, \quad S(K) = K^{-1},
$$
$$
\Delta(E) = E \otimes K + 1 \otimes E, \quad \varepsilon(E) = 0, \quad S(E) = -EK^{-1},
$$
$$
\Delta(F) = F \otimes 1 + K^{-1} \otimes F, \quad \varepsilon(F) = 0, \quad S(F) = -KF.
$$

### 2.7 $R$-矩阵

**定义 2.10**（$R$-矩阵）设 $H$ 是 Hopf 代数。**$R$-矩阵** 是一个可逆元 $R \in H \otimes H$，满足：

$$
\Delta^{\text{op}}(x) = R \Delta(x) R^{-1}, \quad \forall x \in H,
$$
$$
(\Delta \otimes \operatorname{id})(R) = R_{13} R_{23}, \quad (\operatorname{id} \otimes \Delta)(R) = R_{13} R_{12},
$$

其中 $R_{12} = R \otimes 1$，$R_{23} = 1 \otimes R$，$R_{13} = (\tau \otimes \operatorname{id})(1 \otimes R)$（$\tau$ 是交换因子）。

具有 $R$-矩阵的 Hopf 代数称为 **拟三角 Hopf 代数**。

### 2.8 Yang-Baxter 方程

**定义 2.11**（Yang-Baxter 方程）设 $V$ 是向量空间，$R \in \operatorname{End}(V \otimes V)$。**Yang-Baxter 方程** 为：

$$
R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12} \quad \text{在} \quad V \otimes V \otimes V \text{上},
$$

其中 $R_{12} = R \otimes \operatorname{id}_V$，$R_{23} = \operatorname{id}_V \otimes R$，$R_{13} = (\tau \otimes \operatorname{id})(\operatorname{id}_V \otimes R)$。

### 2.9 辫子张量范畴

**定义 2.12**（辫子张量范畴）**辫子张量范畴** $(\mathcal{C}, \otimes, \mathbf{1}, \alpha, \lambda, \rho, c)$ 是一个张量范畴，配备 **辫子同构** $c_{X,Y}: X \otimes Y \to Y \otimes X$，满足六边形公理（即对任意 $X, Y, Z \in \mathcal{C}$，以下图表交换）：

$$
\begin{CD}
X \otimes (Y \otimes Z) @>{c_{X, Y \otimes Z}}>> (Y \otimes Z) \otimes X \\
@V{\alpha_{X,Y,Z}}VV @VV{\alpha^{-1}_{Y,Z,X}}V \\
(X \otimes Y) \otimes Z @>>{c_{X,Y} \otimes \operatorname{id}_Z}> (Y \otimes X) \otimes Z @>{\operatorname{id}_Y \otimes c_{X,Z}}>> Y \otimes (Z \otimes X)
\end{CD}
$$

拟三角 Hopf 代数的表示范畴构成辫子张量范畴。

### 2.10 拟三角 Hopf 代数

**定义 2.13**（拟三角 Hopf 代数）一个 **拟三角 Hopf 代数** $(H, R)$ 是一个 Hopf 代数 $H$ 配备一个 $R$-矩阵。

若 $R$ 还满足 $R_{21} = R^{-1}$，则称 $H$ 是 **三角 Hopf 代数**。

### 2.11 量子维数

**定义 2.14**（量子维数）设 $H$ 是拟三角 Hopf 代数，$V$ 是有限维 $H$-模。**量子维数**（或量子迹）定义为：

$$
\operatorname{qdim}(V) = \operatorname{tr}_V(R_{21} R_{12} \cdot K^{-1}),
$$

其中 $K$ 是某些量子群中存在的"量子行列式"元素。

### 2.12 量子不变量与 Jones 多项式

**定义 2.15**（量子不变量）三维流形的 **量子不变量**（Reshetikhin-Turaev 不变量）通过将流形用手术法分解为基本构件，再用量子群 $U_q(\mathfrak{sl}_2)$ 的表示论数据（如 $6j$-符号）赋值得到。

**Jones 多项式** $V_L(t)$ 是纽结 $L$ 的 Laurent 多项式不变量，可以通过量子群 $U_q(\mathfrak{sl}_2)$ 在 $q = t^{1/4}$ 时的表示论构造得到。

### 2.13 Monoidal 范畴

**定义 2.16**（Monoidal 范畴）**Monoidal 范畴**（张量范畴）$(\mathcal{C}, \otimes, \mathbf{1}, \alpha, \lambda, \rho)$ 是一个范畴 $\mathcal{C}$ 配备：
- 张量积函子 $\otimes: \mathcal{C} \times \mathcal{C} \to \mathcal{C}$；
- 单位对象 $\mathbf{1} \in \mathcal{C}$；
- 结合约束 $\alpha_{X,Y,Z}: (X \otimes Y) \otimes Z \to X \otimes (Y \otimes Z)$ 满足五边形公理；
- 左右单位约束 $\lambda_X: \mathbf{1} \otimes X \to X$，$\rho_X: X \otimes \mathbf{1} \to X$ 满足三角公理。

---

## 3. 定理与证明

### 3.1 量子群 $U_q(\mathfrak{sl}_2)$ 的表示分类

**定理 3.1**（$U_q(\mathfrak{sl}_2)$ 的有限维不可约表示分类）设 $q$ 不是单位根（即 $q^n \neq 1$ 对任意 $n \in \mathbb{N}$）。则 $U_q(\mathfrak{sl}_2)$ 的有限维不可约表示由最高权分类。对每个非负整数 $n$，存在唯一的 $(n+1)$ 维不可约表示 $V_n$，基为 $\{v_0, v_1, \ldots, v_n\}$，作用如下：

$$
K \cdot v_k = q^{n-2k} v_k,
$$
$$
E \cdot v_k = \begin{cases}
\frac{q^{n-k+1} - q^{-(n-k+1)}}{q - q^{-1}} v_{k-1}, & k > 0, \\
0, & k = 0,
\end{cases}
$$
$$
F \cdot v_k = \begin{cases}
\frac{q^{k+1} - q^{-(k+1)}}{q - q^{-1}} v_{k+1}, & k < n, \\
0, & k = n.
\end{cases}
$$

**证明**：

**步骤 1：最高权向量**

设 $V$ 是有限维不可约 $U_q(\mathfrak{sl}_2)$-模。由于 $K$ 的作用可对角化（因为 $K$ 在 $U_q(\mathfrak{sl}_2)$ 中是群元），$V$ 可以分解为 $K$ 的特征空间的直和：

$$
V = \bigoplus_{\lambda} V_\lambda,
$$

其中 $V_\lambda = \{v \in V : K \cdot v = \lambda v\}$，$\lambda \in \mathbb{k}^\times$。

**步骤 2：$E$ 和 $F$ 的作用**

由关系 $KEK^{-1} = q^2 E$，若 $v \in V_\lambda$，则：

$$
K \cdot (E \cdot v) = KEK^{-1} \cdot (K \cdot v) = q^2 E \cdot (K \cdot v) = q^2 \lambda (E \cdot v).
$$

因此 $E \cdot V_\lambda \subseteq V_{q^2 \lambda}$。类似地，$F \cdot V_\lambda \subseteq V_{q^{-2} \lambda}$。

**步骤 3：存在最高权向量**

由于 $V$ 有限维，$K$ 的特征值有限。取 $\lambda$ 使得 $|\lambda|$ 最大（在某种意义下），则 $E \cdot V_\lambda = 0$（否则 $E \cdot v$ 将给出特征值 $q^2 \lambda$，模长更大）。设 $v_0 \in V_\lambda$ 是非零最高权向量，则 $E \cdot v_0 = 0$。

**步骤 4：生成权链**

定义 $v_k = \frac{1}{[k]!} F^k \cdot v_0$，其中 $[k]! = [1][2]\cdots[k]$，$[k] = \frac{q^k - q^{-k}}{q - q^{-1}}$ 是 $q$-整数。

由 $F$ 的作用，$K \cdot v_k = q^{-2k} \lambda v_k$。由于 $V$ 有限维，存在 $n$ 使得 $v_{n+1} = 0$ 但 $v_n \neq 0$。

**步骤 5：确定参数**

计算 $E \cdot v_k$。利用 $[E, F] = \frac{K - K^{-1}}{q - q^{-1}}$，通过归纳法可得：

$$
E \cdot v_k = \frac{\lambda q^{-(k-1)} - \lambda^{-1} q^{(k-1)}}{q - q^{-1}} v_{k-1}.
$$

由于 $v_{n+1} = 0$，即 $F \cdot v_n = 0$，计算 $E \cdot v_{n+1}$（必须为 $0$）可得：

$$
0 = E \cdot v_{n+1} \propto \frac{\lambda q^{-n} - \lambda^{-1} q^{n}}{q - q^{-1}} v_n.
$$

因此 $\lambda q^{-n} = \lambda^{-1} q^n$，即 $\lambda = \pm q^n$。由于 $q$ 不是单位根，适当选取可设 $\lambda = q^n$。

**步骤 6：构造完成**

此时 $\lambda = q^n$，$K$ 的特征值为 $q^{n-2k}$（$k = 0, \ldots, n$），且 $E$ 和 $F$ 的作用如定理所述。可以验证这些算子满足 $U_q(\mathfrak{sl}_2)$ 的关系，从而 $V_n$ 是 $(n+1)$ 维不可约表示。

**步骤 7：唯一性**

由上述构造，任何有限维不可约表示的最高权决定了整个表示的结构，且最高权必须为 $q^n$（$n \in \mathbb{N}$）。因此所有有限维不可约表示都是 $V_n$（$n \geq 0$）。$\square$

### 3.2 $R$-矩阵的存在唯一性

**定理 3.2**（$U_q(\mathfrak{sl}_2)$ 的 $R$-矩阵）量子群 $U_q(\mathfrak{sl}_2)$ 是拟三角 Hopf 代数，其 $R$-矩阵为：

$$
R = q^{\frac{1}{2} H \otimes H} \sum_{n=0}^{\infty} \frac{(1 - q^{-2})^n}{[n]!} q^{\frac{n(n-1)}{2}} (E^n \otimes F^n),
$$

其中 $H$ 是形式生成元满足 $K = q^H$。$R$ 满足 Yang-Baxter 方程。

**证明**：

**步骤 1：$R$-矩阵的构造**

定义 $R$ 为 $U_q(\mathfrak{sl}_2) \hat{\otimes} U_q(\mathfrak{sl}_2)$ 中的元素（完备化张量积）：

$$
R = q^{\frac{1}{2} H \otimes H} \sum_{n=0}^{\infty} \frac{(1 - q^{-2})^n}{[n]!} q^{\frac{n(n-1)}{2}} (E^n \otimes F^n).
$$

**步骤 2：验证拟三角条件**

需要验证：
1. $\Delta^{\text{op}}(x) R = R \Delta(x)$ 对所有 $x \in U_q(\mathfrak{sl}_2)$；
2. $(\Delta \otimes \operatorname{id})(R) = R_{13} R_{23}$；
3. $(\operatorname{id} \otimes \Delta)(R) = R_{13} R_{12}$。

**验证条件 1**：只需验证对生成元 $E, F, K$ 成立。

对 $K$：$\Delta(K) = K \otimes K$，$\Delta^{\text{op}}(K) = K \otimes K$，因此 $R \Delta(K) = \Delta^{\text{op}}(K) R$ 自动成立。

对 $E$：$\Delta(E) = E \otimes K + 1 \otimes E$，$\Delta^{\text{op}}(E) = K \otimes E + E \otimes 1$。

需要验证 $(K \otimes E + E \otimes 1) R = R (E \otimes K + 1 \otimes E)$。

利用 $q^{\frac{1}{2} H \otimes H}$ 与 $E \otimes 1$ 和 $1 \otimes E$ 的交换关系：
- $q^{\frac{1}{2} H \otimes H} (E \otimes 1) = q^{1 \otimes H} (E \otimes 1) q^{\frac{1}{2} H \otimes H}$；
- $q^{\frac{1}{2} H \otimes H} (1 \otimes E) = q^{H \otimes 1} (1 \otimes E) q^{\frac{1}{2} H \otimes H}$。

结合级数项的验证，可得条件 1 成立。

**验证条件 2**：$(\Delta \otimes \operatorname{id})(R) = R_{13} R_{23}$。

计算 $(\Delta \otimes \operatorname{id})(q^{\frac{1}{2} H \otimes H}) = q^{\frac{1}{2} (\Delta(H) \otimes H)} = q^{\frac{1}{2} (H \otimes 1 + 1 \otimes H) \otimes H} = q^{\frac{1}{2} H \otimes 1 \otimes H} q^{\frac{1}{2} 1 \otimes H \otimes H} = (q^{\frac{1}{2} H \otimes H})_{13} (q^{\frac{1}{2} H \otimes H})_{23}$。

类似地，$(\Delta \otimes \operatorname{id})(E^n \otimes F^n) = (\Delta(E)^n \otimes F^n)$。利用 $\Delta(E) = E \otimes K + 1 \otimes E$ 的二项式展开，可得 $(\Delta \otimes \operatorname{id})(R) = R_{13} R_{23}$。

**步骤 3：唯一性**

在 $U_q(\mathfrak{sl}_2)$ 的完备化中，满足拟三角条件的 $R$-矩阵在上述构造下是唯一的，由 Drinfeld 量子双的泛性质保证。$\square$

### 3.3 Yang-Baxter 方程的解与量子群的关系

**定理 3.3**（Yang-Baxter 方程与量子群）设 $H$ 是拟三角 Hopf 代数，$R \in H \otimes H$ 是其 $R$-矩阵。则对任意 $H$-模 $V$，$R$ 在 $V \otimes V$ 上的作用 $R_{V,V} = \rho_V \otimes \rho_V(R)$ 给出 Yang-Baxter 方程的解：

$$
(R_{V,V})_{12} (R_{V,V})_{13} (R_{V,V})_{23} = (R_{V,V})_{23} (R_{V,V})_{13} (R_{V,V})_{12} \quad \text{在} \quad V \otimes V \otimes V \text{上}.
$$

**证明**：

**步骤 1：将问题转化为 Hopf 代数中的关系**

设 $R = \sum_i a_i \otimes b_i \in H \otimes H$。在 $V \otimes V \otimes V$ 上，$R_{12}$ 的作用为 $\sum_i a_i \otimes b_i \otimes 1$，$R_{13}$ 的作用为 $\sum_i a_i \otimes 1 \otimes b_i$，$R_{23}$ 的作用为 $\sum_i 1 \otimes a_i \otimes b_i$。

**步骤 2：利用 $R$-矩阵的拟三角条件**

由拟三角条件的 $(\Delta \otimes \operatorname{id})(R) = R_{13} R_{23}$ 和 $(\operatorname{id} \otimes \Delta)(R) = R_{13} R_{12}$，以及余结合律。

**步骤 3：计算 Yang-Baxter 复合**

考虑 $R_{12} R_{13} R_{23}$：

$$
R_{12} R_{13} R_{23} = \sum_{i,j,k} (a_i \otimes b_i \otimes 1)(a_j \otimes 1 \otimes b_j)(1 \otimes a_k \otimes b_k)
$$

$$
= \sum_{i,j,k} a_i a_j \otimes b_i a_k \otimes b_j b_k.
$$

另一方面，$R_{23} R_{13} R_{12} = \sum_{i,j,k} (1 \otimes a_i \otimes b_i)(a_j \otimes 1 \otimes b_j)(a_k \otimes b_k \otimes 1)$

$$
= \sum_{i,j,k} a_j a_k \otimes a_i b_k \otimes b_i b_j.
$$

**步骤 4：利用拟三角条件化简**

由 $(\Delta \otimes \operatorname{id})(R) = R_{13} R_{23}$，得：

$$
\sum_j \Delta(a_j) \otimes b_j = \sum_{j,k} a_j \otimes a_k \otimes b_j b_k.
$$

由 $(\operatorname{id} \otimes \Delta)(R) = R_{13} R_{12}$，得：

$$
\sum_i a_i \otimes \Delta(b_i) = \sum_{i,k} a_i a_k \otimes b_k \otimes b_i.
$$

**步骤 5：验证等式**

利用上述关系，经过计算可得：

$$
R_{12} R_{13} R_{23} = \sum_{i,j} a_i \Delta(b_i) \otimes b_j = \sum_{i,j} \Delta^{\text{op}}(a_j) b_i \otimes b_j = R_{23} R_{13} R_{12}.
$$

其中第二步使用了 $\Delta^{\text{op}}(x) R = R \Delta(x)$。

**步骤 6：在 $V \otimes V \otimes V$ 上的作用**

将 $R$ 通过表示 $\rho_V$ 作用到 $V$ 上，得到 $R_{V,V} = (\rho_V \otimes \rho_V)(R)$。由于 $\rho_V$ 是代数同态，上述在 $H$ 中成立的关系在 $\operatorname{End}(V \otimes V \otimes V)$ 中仍然成立。因此 $R_{V,V}$ 满足 Yang-Baxter 方程。$\square$

### 3.4 量子迹与 Jones 多项式的关系

**定理 3.4**（量子迹与 Jones 多项式）设 $L$ 是纽结或链环，$V_L(t)$ 是 Jones 多项式。则存在量子群 $U_q(\mathfrak{sl}_2)$ 的表示 $V_1$（二维不可约表示），使得 Jones 多项式可以表示为量子迹：

$$
V_L(t) = \operatorname{qtr}_{V_1^{\otimes |L|}} (\text{缠绕算子}),
$$

其中 $|L|$ 是 $L$ 的分支数，$t = q^4$，缠绕算子由 $R$-矩阵和辫子作用给出。

**证明**：我们给出证明的框架。

**步骤 1：Kauffman 括号与 Jones 多项式**

Jones 多项式可以通过 Kauffman 括号 $\langle L \rangle$ 构造：

$$
V_L(t) = (-t^{-3/4})^{w(L)} \langle L \rangle,
$$

其中 $w(L)$ 是 $L$ 的拧数（writhe），Kauffman 括号由以下 skein 关系定义：

$$
\langle \bigcirc \rangle = 1, \quad \langle L \cup \bigcirc \rangle = (-t^{1/2} - t^{-1/2}) \langle L \rangle,
$$
$$
\langle \times \rangle = t^{1/4} \langle \text{ } \rangle + t^{-1/4} \langle \text{ } \rangle.
$$

**步骤 2：量子群表示与辫子表示**

$U_q(\mathfrak{sl}_2)$ 的二维表示 $V_1$ 上的 $R$-矩阵作用给出辫子群 $B_n$ 的表示。具体地，对 $n$ 股辫子，生成元 $\sigma_i$ 作用在 $V_1^{\otimes n}$ 上为：

$$
\sigma_i \mapsto \operatorname{id}^{\otimes (i-1)} \otimes \check{R} \otimes \operatorname{id}^{\otimes (n-i-1)},
$$

其中 $\check{R} = \tau \circ R$，$\tau$ 是交换因子。

**步骤 3：计算 $R$-矩阵在 $V_1 \otimes V_1$ 上的作用**

在 $V_1$ 的基 $\{v_0, v_1\}$ 上，$R$-矩阵的作用为：

$$
R(v_0 \otimes v_0) = q^{1/2} v_0 \otimes v_0,
$$
$$
R(v_0 \otimes v_1) = q^{-1/2} v_1 \otimes v_0 + (q^{-1/2} - q^{3/2}) v_0 \otimes v_1,
$$
$$
R(v_1 \otimes v_0) = q^{-1/2} v_0 \otimes v_1,
$$
$$
R(v_1 \otimes v_1) = q^{1/2} v_1 \otimes v_1.
$$

**步骤 4：量子迹的定义**

在 $U_q(\mathfrak{sl}_2)$ 中，元素 $K$ 定义了量子迹。对任意算子 $f \in \operatorname{End}(V_1^{\otimes n})$，量子迹定义为：

$$
\operatorname{qtr}(f) = \operatorname{tr}(f \circ K^{\otimes n}).
$$

**步骤 5：验证 skein 关系**

通过直接计算，可以验证量子迹 $\operatorname{qtr}$ 作用于辫子表示上满足 Kauffman 括号的 skein 关系。令 $t = q^4$，则：

$$
\operatorname{qtr}(\operatorname{id}) = q + q^{-1} = t^{1/2} + t^{-1/2},
$$
$$
\operatorname{qtr}(\sigma_i) = \operatorname{qtr}(\sigma_i^{-1}) = \cdots,
$$

且以下关系成立：

$$
\operatorname{qtr}(\sigma_i) - \operatorname{qtr}(\sigma_i^{-1}) = (t^{1/4} - t^{-1/4}) \operatorname{qtr}(\operatorname{id}).
$$

**步骤 6：构造 Jones 多项式**

给定纽结 $L$ 的辫子表示（由 Alexander 定理，任何纽结可以表示为闭辫子），取对应的辫子群元素 $\beta \in B_n$，定义：

$$
V_L(t) = \frac{(-t^{-3/4})^{w(\beta)}}{d^{n-1}} \operatorname{qtr}(\beta),
$$

其中 $d = q + q^{-1} = t^{1/2} + t^{-1/2}$。可以验证该表达式在 Markov 移动下不变，且满足 Jones 多项式的公理，因此与 Jones 多项式一致。$\square$

### 3.5 Tannaka-Krein 对偶定理

**定理 3.5**（Tannaka-Krein 对偶定理）设 $G$ 是紧李群，$\operatorname{Rep}(G)$ 是 $G$ 的有限维连续表示的张量范畴，配备遗忘函子 $F: \operatorname{Rep}(G) \to \operatorname{Vect}_\mathbb{C}$。则：

$$
G \cong \operatorname{Aut}^{\otimes}(F),
$$

其中 $\operatorname{Aut}^{\otimes}(F)$ 是 $F$ 的张量自同构群。换言之，$G$ 可以从其表示范畴 $\operatorname{Rep}(G)$ 中完全恢复。

更一般地，对任何 Hopf 代数 $H$，$H$ 可以从其表示范畴 $\operatorname{Rep}(H)$ 中恢复，只要该范畴配备了遗忘函子。

**证明思路**：

**步骤 1：定义张量自同构群**

考虑遗忘函子 $F: \operatorname{Rep}(G) \to \operatorname{Vect}_\mathbb{C}$，它将每个表示映射到其底向量空间，忽略 $G$ 的作用。

$F$ 的 **张量自同构** 是一个自然变换 $\eta: F \Rightarrow F$，使得：
1. $\eta$ 与张量积相容：$\eta_{V \otimes W} = \eta_V \otimes \eta_W$；
2. $\eta$ 与单位表示相容：$\eta_{\mathbf{1}} = \operatorname{id}_\mathbb{C}$。

所有这样的张量自同构构成群 $\operatorname{Aut}^{\otimes}(F)$。

**步骤 2：构造同态 $G \to \operatorname{Aut}^{\otimes}(F)$**

对每个 $g \in G$，定义 $\eta^{(g)}_V = \rho_V(g): V \to V$，其中 $\rho_V$ 是表示 $V$ 的群作用。由于 $\rho_{V \otimes W}(g) = \rho_V(g) \otimes \rho_W(g)$，$\eta^{(g)}$ 是张量自同构。这给出了群同态 $\phi: G \to \operatorname{Aut}^{\otimes}(F)$。

**步骤 3：证明 $\phi$ 是单射（$G$ 紧致）**

若 $\phi(g) = \phi(h)$，则对所有表示 $V$，$\rho_V(g) = \rho_V(h)$。由 Peter-Weyl 定理，$G$ 的不可约表示分离 $G$ 中的点，因此 $g = h$。故 $\phi$ 是单射。

**步骤 4：证明 $\phi$ 是满射**

设 $\eta \in \operatorname{Aut}^{\otimes}(F)$。对任意表示 $V$，$\eta_V$ 是 $V$ 上的线性自同构，且与所有表示间的 $G$-等变映射交换（由自然性）。特别地，对正则表示 $L^2(G)$，$\eta_{L^2(G)}$ 是 $G \times G$-等变的（因为 $L^2(G) \cong \bigoplus_V V \otimes V^*$）。

由 Schur 引理，$\eta_{L^2(G)}$ 必须是某个 $g \in G$ 的左乘作用。因此 $\eta = \phi(g)$，$\phi$ 是满射。

**步骤 5：Hopf 代数情形**

对 Hopf 代数 $H$，考虑表示范畴 $\operatorname{Rep}(H)$ 和遗忘函子 $F: \operatorname{Rep}(H) \to \operatorname{Vect}_\mathbb{k}$。则 $H$ 同构于 $F$ 的余代数的张量自同构端代数：

$$
H \cong \operatorname{End}^{\otimes}(F).
$$

这是 Tannaka-Krein 对偶定理的代数版本，它表明任何 Hopf 代数可以从其表示范畴中恢复。

**证明概述**：设 $A = \operatorname{End}^{\otimes}(F)$ 是 $F$ 的张量自同构的端代数。构造 $H \to A$ 的映射：每个 $h \in H$ 定义自然变换 $\eta^{(h)}_V(v) = h \cdot v$。可以证明这是 Hopf 代数同构。$\square$

---

## 4. 示例

### 示例 4.1：$U_q(\mathfrak{sl}_2)$ 的表示构造

**二维表示 $V_1$**

取 $n = 1$，则 $V_1$ 是二维表示，基为 $\{v_0, v_1\}$。

作用为：

$$
K \cdot v_0 = q v_0, \quad K \cdot v_1 = q^{-1} v_1,
$$
$$
E \cdot v_0 = 0, \quad E \cdot v_1 = v_0,
$$
$$
F \cdot v_0 = v_1, \quad F \cdot v_1 = 0.
$$

**验证 $[E, F]$ 关系**：

$$
[E, F] \cdot v_0 = E F \cdot v_0 - F E \cdot v_0 = E \cdot v_1 - 0 = v_0,
$$
$$
\frac{K - K^{-1}}{q - q^{-1}} \cdot v_0 = \frac{q - q^{-1}}{q - q^{-1}} v_0 = v_0.
$$

类似地对 $v_1$ 验证，关系成立。

**三维表示 $V_2$**

取 $n = 2$，基为 $\{v_0, v_1, v_2\}$。

作用为：

$$
K \cdot v_0 = q^2 v_0, \quad K \cdot v_1 = v_1, \quad K \cdot v_2 = q^{-2} v_2,
$$
$$
E \cdot v_0 = 0, \quad E \cdot v_1 = \frac{q - q^{-1}}{q - q^{-1}} v_0 = v_0, \quad E \cdot v_2 = \frac{q^2 - q^{-2}}{q - q^{-1}} v_1 = (q + q^{-1}) v_1,
$$
$$
F \cdot v_0 = \frac{q - q^{-1}}{q - q^{-1}} v_1 = v_1, \quad F \cdot v_1 = \frac{q^2 - q^{-2}}{q - q^{-1}} v_2 = (q + q^{-1}) v_2, \quad F \cdot v_2 = 0.
$$

### 示例 4.2：量子群的 $R$-矩阵计算

对于 $U_q(\mathfrak{sl}_2)$ 的二维表示 $V_1$，$R$-矩阵在 $V_1 \otimes V_1$ 上的作用为：

$$
R = q^{1/2} \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & q^{-2} & 1 - q^{-2} & 0 \\
0 & 0 & q^{-2} & 0 \\
0 & 0 & 0 & 1
\end{pmatrix},
$$

在基 $\{v_0 \otimes v_0, v_0 \otimes v_1, v_1 \otimes v_0, v_1 \otimes v_1\}$ 下。

**验证 Yang-Baxter 方程**：

在 $V_1 \otimes V_1 \otimes V_1$ 上，$R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}$ 可以通过直接矩阵乘法验证（$8 \times 8$ 矩阵）。

**计算 $\check{R} = \tau \circ R$**：

$$
\check{R}(v_0 \otimes v_0) = q^{1/2} v_0 \otimes v_0,
$$
$$
\check{R}(v_0 \otimes v_1) = q^{-1/2} v_1 \otimes v_0,
$$
$$
\check{R}(v_1 \otimes v_0) = q^{-1/2} v_0 \otimes v_1 + (q^{-1/2} - q^{3/2}) v_1 \otimes v_0,
$$
$$
\check{R}(v_1 \otimes v_1) = q^{1/2} v_1 \otimes v_1.
$$

$\check{R}$ 满足辫子关系：$\check{R}_{12} \check{R}_{23} \check{R}_{12} = \check{R}_{23} \check{R}_{12} \check{R}_{23}$。

---

## 5. 习题

### 习题 5.1

验证 $U_q(\mathfrak{sl}_2)$ 的对极映射 $S$ 满足 Hopf 代数的对极条件。

**提示**：分别对生成元 $K, E, F$ 验证 $m \circ (S \otimes \operatorname{id}) \circ \Delta = \eta \circ \varepsilon$。

### 习题 5.2

证明 $U_q(\mathfrak{sl}_2)$ 中以下关系成立：

$$
[E, F^n] = [n] \frac{q^{-(n-1)} K - q^{n-1} K^{-1}}{q - q^{-1}} F^{n-1},
$$

其中 $[n] = \frac{q^n - q^{-n}}{q - q^{-1}}$。

**提示**：利用归纳法，使用 $[E, F] = \frac{K - K^{-1}}{q - q^{-1}}$ 和 $KF = q^{-2}FK$。

### 习题 5.3

验证 $U_q(\mathfrak{sl}_2)$ 的二维表示 $V_1$ 中 $R$-矩阵的显式形式。

**提示**：在基 $\{v_0, v_1\}$ 上写出 $E, F, K$ 的矩阵表示，然后代入 $R = q^{\frac{1}{2} H \otimes H} \sum_{n=0}^{\infty} \frac{(1 - q^{-2})^n}{[n]!} q^{\frac{n(n-1)}{2}} (E^n \otimes F^n)$，并计算级数。

### 习题 5.4

证明 $U_q(\mathfrak{sl}_2)$ 中 $R$-矩阵的逆为 $R^{-1} = \sum_{n=0}^{\infty} \frac{(q^{-2} - 1)^n}{[n]!} q^{-\frac{n(n-1)}{2}} (F^n \otimes E^n) q^{-\frac{1}{2} H \otimes H}$。

**提示**：直接在 $V_1 \otimes V_1$ 上验证 $R R^{-1} = R^{-1} R = 1$。

### 习题 5.5

证明 $U_q(\mathfrak{sl}_2)$ 的表示 $V_n$ 的量子维数为 $\operatorname{qdim}(V_n) = \frac{q^{n+1} - q^{-(n+1)}}{q - q^{-1}} = [n+1]$。

**提示**：量子维数定义为 $\operatorname{tr}_{V_n}(K)$，利用 $K$ 在 $V_n$ 上的特征值求和。

### 习题 5.6

利用 $U_q(\mathfrak{sl}_2)$ 的表示论构造三叶结（trefoil knot）的 Jones 多项式。

**提示**：三叶结可以表示为 $(3, 2)$-torus 纽结，其辫子表示为 $\sigma_1^3 \in B_2$。利用二维表示 $V_1$ 计算 $\operatorname{qtr}(\sigma_1^3)$。

### 习题 5.7

证明辫子张量范畴的六边形公理等价于 Yang-Baxter 方程。

**提示**：将六边形公理应用到 $X \otimes Y \otimes Z$ 上，写出 $c_{X,Y \otimes Z}$ 和 $c_{X \otimes Y, Z}$ 的分解。

### 习题 5.8

设 $H$ 是有限维 Hopf 代数，$D(H)$ 是其 Drinfeld 量子双。证明 $D(H)$ 是拟三角的，并给出其 $R$-矩阵。

**提示**：$D(H) = H \otimes H^{*\text{op}}$ 作为向量空间，$R$-矩阵为 $R = \sum_i (1 \otimes e_i) \otimes (e^i \otimes 1)$，其中 $\{e_i\}$ 是 $H$ 的基，$\{e^i\}$ 是对偶基。

---

## 6. 总结

本课程系统介绍了 Hopf 代数与量子群的核心理论。

**核心收获**：

1. **Hopf 代数的结构**：Hopf 代数同时具有代数结构和余代数结构，通过对极映射联系两者。群代数和泛包络代数是最基本的例子。对偶配对、卷积代数、余模等概念构成了 Hopf 代数理论的基本语言。

2. **量子群 $U_q(\mathfrak{sl}_2)$**：作为泛包络代数 $U(\mathfrak{sl}_2)$ 的 $q$-变形，$U_q(\mathfrak{sl}_2)$ 保持了 Hopf 代数结构但失去了余交换性。其有限维不可约表示由最高权 $q^n$（$n \in \mathbb{N}$）分类，维数为 $n+1$。

3. **$R$-矩阵与 Yang-Baxter 方程**：拟三角 Hopf 代数的 $R$-矩阵是 Yang-Baxter 方程的解族，为辫子群提供表示。$R$-矩阵的存在唯一性是量子群理论的核心结果。

4. **量子不变量**：量子群 $U_q(\mathfrak{sl}_2)$ 的表示论为三维流形和纽结提供了丰富的拓扑不变量。Jones 多项式是量子迹在纽结上的具体实现，标志着量子拓扑的开端。

5. **Tannaka-Krein 对偶**：Tannaka-Krein 对偶定理表明 Hopf 代数可以从其表示范畴中完全恢复，建立了代数结构和范畴结构之间的深刻联系。

**衔接**：Hopf 代数与量子群是当前数学物理研究的前沿领域，与低维拓扑、共形场论、顶点算子代数、非交换几何等方向密切相关。本课程为后续学习量子拓扑、模块化张量范畴、以及更高维的量子不变量理论奠定了基础。