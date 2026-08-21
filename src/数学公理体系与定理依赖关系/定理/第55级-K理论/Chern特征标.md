# Chern 特征标

> **一句话大白话**：给每个向量丛"贴一张特征价签"（有理上同调类），且把 K 类的加法与乘法翻译成上同调的加乘——是连接两种"洞的账本"之间的忠实翻译官。
>
> **小例子**：对线丛 $L$，$\mathrm{ch}(L)=e^{c_1(L)}=1+c_1+\tfrac12c_1^2+\cdots$；此映射满足 $\mathrm{ch}(E\oplus F)=\mathrm{ch}\,E+\mathrm{ch}\,F$、$\mathrm{ch}(E\otimes F)=\mathrm{ch}\,E\cdot\mathrm{ch}\,F$。

## 一、定理介绍

> **前置依赖**：Chern 类与分裂原理、对称函数基本定理、Atiyah-Hirzebruch 谱序列、Chern-Weil 理论与 de Rham 上同调、拓扑 K 理论

Chern 特征标是 K 理论与上同调之间的桥梁，由 Shiing-Shen Chern 和陈省身的工作发展而来。它是一个环同态 $\text{ch}: K(X) \to H^*(X; \mathbb{Q})$，将向量丛的 K 类映射到有理上同调类。

Chern 特征标在指标定理中扮演核心角色，因为它将 K 理论中的代数信息转化为上同调中的可计算量。通过 Chern-Weil 理论，Chern 特征标可以用曲率形式显式表达。

## 二、原理思路

### 基本构造思想

Chern 特征标的构造基于以下观察：

1. **分裂原理**：对于任何向量丛 $E$，存在空间 $F(E)$（旗流形）使得 $p^*E$ 分裂为线丛的直和，且 $p^*: H^*(X) \to H^*(F(E))$ 是单射。

2. **线丛的 Chern 类**：对于线丛 $L$，第一 Chern 类 $c_1(L) \in H^2(X; \mathbb{Z})$ 是良定义的。

3. **特征标的定义**：对于线丛 $L$，定义 $\text{ch}(L) = e^{c_1(L)}$。对于一般向量丛，通过分裂原理定义。

### 关键性质

Chern 特征标的关键性质是它是环同态：
$$\text{ch}(E \oplus F) = \text{ch}(E) + \text{ch}(F)$$
$$\text{ch}(E \otimes F) = \text{ch}(E) \cdot \text{ch}(F)$$

这使得 K 理论的乘法结构可以转移到上同调中。

## 三、定理的严格表述

**定义 1（Chern 特征标）** 设 $X$ 为紧光滑流形。Chern 特征标是映射：
$$\text{ch}: K(X) \to H^{\text{even}}(X; \mathbb{Q}) = \bigoplus_{k=0}^\infty H^{2k}(X; \mathbb{Q})$$
定义为：

对于线丛 $L$：
$$\text{ch}(L) = e^{c_1(L)} = 1 + c_1(L) + \frac{c_1(L)^2}{2!} + \frac{c_1(L)^3}{3!} + \cdots$$

对于向量丛 $E$，假设 $E$ 分裂为线丛 $L_1, \ldots, L_n$（由分裂原理）：
$$\text{ch}(E) = \sum_{i=1}^n e^{c_1(L_i)} = \sum_{i=1}^n \left(1 + c_1(L_i) + \frac{c_1(L_i)^2}{2!} + \cdots\right)$$

**定理 1（Chern 特征标的基本性质）**
1. **良定义性**：$\text{ch}(E)$ 不依赖于线丛的分裂方式
2. **加法性**：$\text{ch}(E \oplus F) = \text{ch}(E) + \text{ch}(F)$
3. **乘法性**：$\text{ch}(E \otimes F) = \text{ch}(E) \cdot \text{ch}(F)$
4. **函子性**：若 $f: X \to Y$ 连续，则 $\text{ch}(f^*E) = f^*\text{ch}(E)$
5. **归一化**：对于平凡丛 $\mathbb{C}^n$，$\text{ch}(\mathbb{C}^n) = n$

**定理 2（Chern 特征标的显式公式）** 设 $E$ 为秩 $r$ 的向量丛，$c_k(E)$ 为 Chern 类。则：
$$\text{ch}(E) = r + c_1(E) + \frac{1}{2}(c_1(E)^2 - 2c_2(E)) + \frac{1}{6}(c_1(E)^3 - 3c_1(E)c_2(E) + 3c_3(E)) + \cdots$$

一般地，$\text{ch}(E)$ 的 $2k$ 次分量可以表示为 Chern 类的多项式：
$$\text{ch}_k(E) = \frac{1}{k!} s_k(c_1, \ldots, c_k)$$
其中 $s_k$ 是 Newton 多项式，由 $c_1, \ldots, c_k$ 表示。

**定理 3（Chern 特征标与 Chern 类的关系）** 设 $x_1, \ldots, x_r$ 为 $E$ 的形式根（即 $c(E) = \prod_{i=1}^r (1 + x_i)$），则：
$$\text{ch}(E) = \sum_{i=1}^r e^{x_i}$$
$$c_k(E) = \sigma_k(x_1, \ldots, x_r) \quad \text{（初等对称多项式）}$$
$$\text{ch}_k(E) = \frac{1}{k!} p_k(x_1, \ldots, x_r) \quad \text{（幂和）}$$

其中 $p_k = \sum_{i=1}^r x_i^k$。

**定理 4（有理同构）** 对于有限 CW 复形 $X$，映射：
$$\text{ch}: K(X) \otimes \mathbb{Q} \to H^{\text{even}}(X; \mathbb{Q})$$
是环同构。

**定理 5（Chern 特征标的微分形式表示）** 设 $E$ 为复向量丛，$\nabla$ 为 $E$ 上的联络，$\Omega = \nabla^2$ 为曲率形式。则：
$$\text{ch}(E) = \left[\text{tr}\left(\exp\left(\frac{i}{2\pi}\Omega\right)\right)\right] \in H^{\text{even}}_{\text{dR}}(X; \mathbb{C})$$
其中 $[\cdot]$ 表示 de Rham 上同调类。

## 四、证明过程

### 良定义性的证明

**步骤 1：分裂原理**

**引理（分裂原理）**：对于任何向量丛 $E \to X$，存在空间 $p: F(E) \to X$ 使得：
1. $p^*E \cong L_1 \oplus \cdots \oplus L_r$，其中 $L_i$ 为线丛
2. $p^*: H^*(X; \mathbb{Z}) \to H^*(F(E); \mathbb{Z})$ 是单射

**构造**：$F(E)$ 是 $E$ 的旗流形，其纤维为 $GL(r)/B$，其中 $B$ 为上三角矩阵群。

**步骤 2：对称性**

由于 $\text{ch}(E) = \sum e^{x_i}$ 是对称多项式，由对称函数基本定理，它可以表示为初等对称多项式 $\sigma_k$ 的多项式。

因此 $\text{ch}(E)$ 可以表示为 Chern 类 $c_k(E)$ 的多项式，不依赖于分裂方式。

### 加法性的证明

设 $E = L_1 \oplus \cdots \oplus L_r$，$F = M_1 \oplus \cdots \oplus M_s$（在旗流形上）。

则 $E \oplus F = L_1 \oplus \cdots \oplus L_r \oplus M_1 \oplus \cdots \oplus M_s$

因此：
$$\text{ch}(E \oplus F) = \sum_{i=1}^r e^{c_1(L_i)} + \sum_{j=1}^s e^{c_1(M_j)} = \text{ch}(E) + \text{ch}(F)$$

### 乘法性的证明

$E \otimes F$ 的形式根为 $\{x_i + y_j\}_{i,j}$，其中 $x_i$ 为 $E$ 的形式根，$y_j$ 为 $F$ 的形式根。

因此：
$$\text{ch}(E \otimes F) = \sum_{i,j} e^{x_i + y_j} = \sum_{i,j} e^{x_i} e^{y_j} = \left(\sum_i e^{x_i}\right)\left(\sum_j e^{y_j}\right) = \text{ch}(E) \cdot \text{ch}(F)$$

### 有理同构的证明

**步骤 1：单射**

若 $\text{ch}(x) = 0$，则 $x \otimes 1 = 0 \in K(X) \otimes \mathbb{Q}$。

**证明**：使用 Atiyah-Hirzebruch 谱序列。该谱序列从 $E_2^{p,q} = H^p(X; K^q(pt))$ 收敛到 $K^{p+q}(X)$。

由于 $K^q(pt) = \mathbb{Z}$（$q$ 偶）或 $0$（$q$ 奇），$E_2$ 项为：
$$E_2^{p,q} = \begin{cases} H^p(X; \mathbb{Z}) & q \text{ 偶} \\ 0 & q \text{ 奇} \end{cases}$$

Chern 特征标对应于谱序列的边缘同态。若 $\text{ch}(x) = 0$，则 $x$ 在谱序列的所有阶都为零，因此 $x$ 是挠元。

**步骤 2：满射**

对于任何 $\alpha \in H^{2k}(X; \mathbb{Q})$，需要找到 $x \in K(X)$ 使得 $\text{ch}(x) = \alpha$。

**构造**：使用 Thom 类和 pushforward。

对于 $\alpha \in H^{2k}(X; \mathbb{Q})$，可以表示为 $c_k(E)$ 的有理线性组合（由 Thom 同构和 Pontryagin Thom 构造）。

由于 $\text{ch}_k(E) = \frac{1}{k!} s_k + \text{低阶项}$，可以通过归纳法构造原像。

### 微分形式表示的证明

**步骤 1：Chern-Weil 理论**

对于向量丛 $E$ 上的联络 $\nabla$，曲率 $\Omega = \nabla^2$ 是 $\text{End}(E)$-值的 2-形式。

Chern 形式的定义为：
$$c_k(E, \nabla) = \left[\det\left(I + \frac{i}{2\pi}\Omega\right)\right]_{2k}$$

**步骤 2：指数映射**

定义 Chern 特征形式：
$$\text{ch}(E, \nabla) = \text{tr}\left(\exp\left(\frac{i}{2\pi}\Omega\right)\right)$$

展开指数：
$$\text{ch}(E, \nabla) = \text{tr}\left(I + \frac{i}{2\pi}\Omega + \frac{1}{2!}\left(\frac{i}{2\pi}\right)^2\Omega^2 + \cdots\right)$$

**步骤 3：闭形式和上同调类**

由 Bianchi 恒等式 $d\Omega = [\Omega, \nabla]$，可以证明 $\text{ch}(E, \nabla)$ 是闭形式。

不同联络给出的 Chern 特征形式相差恰当形式，因此定义了 de Rham 上同调类。

**步骤 4：与拓扑定义的比较**

通过比较奇异上同调和 de Rham 上同调，可以证明微分形式定义与拓扑定义一致。

这可以通过计算线丛的情况来验证：对于线丛 $L$，$\Omega = 2\pi i \omega$，其中 $\omega$ 为第一 Chern 类的代表元。

因此 $\text{ch}(L, \nabla) = e^{2\pi i \omega / 2\pi i} = e^\omega$，与拓扑定义一致。

## 五、应用与意义

### 1. 指标定理

Chern 特征标在 Atiyah-Singer 指标定理中扮演核心角色。指标定理的 K 理论表述为：
$$\text{ind}(D) = \int_M \text{ch}([\sigma(D)]) \cdot \text{td}(TM \otimes \mathbb{C})$$
其中 $[\sigma(D)] \in K(T^*M)$ 为象征类，$\text{td}$ 为 Todd 类。

### 2. Riemann-Roch 定理

在代数几何中，Hirzebruch-Riemann-Roch 定理使用 Chern 特征标：
$$\chi(X, E) = \int_X \text{ch}(E) \cdot \text{td}(TX)$$
其中 $\chi(X, E)$ 为相干上同调的 Euler 示性数。

### 3. 有理同伦论

Chern 特征标提供了 K 理论的有理化，使得可以使用上同调的工具研究 K 理论。

### 4. 特征类的计算

Chern 特征标与 Chern 类的关系使得可以在两者之间转换：
$$c_1 = \text{ch}_1$$
$$c_2 = \frac{1}{2}(\text{ch}_1^2 - 2\text{ch}_2)$$
$$c_3 = \frac{1}{6}(2\text{ch}_1^3 - 6\text{ch}_1\text{ch}_2 + 6\text{ch}_3)$$

### 5. 物理学应用

在弦理论中，Chern 特征标用于计算 D-膜的电荷：
$$Q_{\text{D-brane}} = \text{ch}(E) \cdot \sqrt{\text{td}(TX)}$$

在反常消除中，Chern 特征标用于计算反常多项式。

### 6. 不动点定理

Atiyah-Bott 不动点定理使用 Chern 特征标：
$$\text{Lefschetz number} = \sum_{p \in \text{Fix}(f)} \frac{\text{tr}(f^*|_E)}{|\det(I - df_p)|}$$
这可以表示为 Chern 特征标的积分。

### 7. 代数 K 理论

Chern 特征标可以推广到代数 K 理论，提供从 $K_n(X)$ 到循环上同调的映射，这在算术几何中有重要应用。
