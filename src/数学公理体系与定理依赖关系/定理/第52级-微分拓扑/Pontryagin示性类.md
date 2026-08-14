# Pontryagin 示性类

## 一、定理介绍

Pontryagin 示性类是微分拓扑和代数拓扑中的重要不变量，由苏联数学家 Lev Pontryagin 在 1940 年代引入。这些示性类是实向量丛的特征类，取值于流形的上同调群，提供了向量丛和流形的重要拓扑信息。

Pontryagin 示性类在配边理论、指标理论、微分拓扑的许多基本定理中扮演核心角色。

## 二、原理思路

Pontryagin 示性类的核心思想包括：

1. **特征类的一般概念**：特征类是将向量丛映射到基空间上同调群的不变量，满足自然性（对拉回交换）。

2. **复化丛**：Pontryagin 类通过实向量丛的复化来定义。给定实向量丛 $E$，其复化 $E \otimes \mathbb{C}$ 是复向量丛。

3. **Chern 类的关系**：Pontryagin 类定义为复化丛的 Chern 类：$p_i(E) = (-1)^i c_{2i}(E \otimes \mathbb{C})$。

4. **万有性质**：Pontryagin 类是 $BO(n)$ 的分类空间的上同调环的生成元。

5. **示性数**：通过在流形的基本类上计算 Pontryagin 类的乘积，得到 Pontryagin 数，这是配边不变量。

## 三、定理的严格表述

**Pontryagin 类定义**：设 $E \to M$ 是实向量丛。定义 $E$ 的**第 $i$ 个 Pontryagin 类**为：
$$p_i(E) = (-1)^i c_{2i}(E \otimes \mathbb{C}) \in H^{4i}(M; \mathbb{Z})$$

其中 $c_{2i}(E \otimes \mathbb{C})$ 是复化丛 $E \otimes \mathbb{C}$ 的第 $2i$ 个 Chern 类。

**总 Pontryagin 类**：
$$p(E) = 1 + p_1(E) + p_2(E) + \cdots \in H^*(M; \mathbb{Z})$$

**基本性质**：
1. **自然性**：如果 $f: N \to M$ 是连续映射，则 $p_i(f^*E) = f^*p_i(E)$。

2. **Whitney 和公式**：
$$p(E \oplus F) = p(E) \cdot p(F) \mod \text{2-扭元}$$

即 $p(E \oplus F) - p(E) \cdot p(F)$ 的元素都是 2 的幂次扭元。

3. **归一化**：如果 $E$ 是平凡丛，则 $p(E) = 1$。

4. **维数**：$p_i(E) \in H^{4i}(M; \mathbb{Z})$，因此当 $4i > \dim M$ 时 $p_i(E) = 0$。

**切丛的 Pontryagin 类**：对于光滑流形 $M$，定义 $M$ 的 Pontryagin 类为切丛 $TM$ 的 Pontryagin 类：
$$p_i(M) = p_i(TM) \in H^{4i}(M; \mathbb{Z})$$

**Pontryagin 数**：设 $M$ 是紧定向 $n$ 维流形（$n = 4k$）。给定非负整数 $i_1, \ldots, i_r$ 满足 $i_1 + \cdots + i_r = k$，定义**Pontryagin 数**为：
$$p_{i_1} \cdots p_{i_r}[M] = \langle p_{i_1}(M) \cdots p_{i_r}(M), [M] \rangle$$

其中 $[M]$ 是 $M$ 的基本类。

**Pontryagin 数的性质**：
1. **配边不变量**：如果 $M$ 和 $N$ 是定向配边的，则它们的所有 Pontryagin 数相等。

2. **定向同胚不变量**：Pontryagin 数在定向同胚下不变（Novikov 定理）。

3. **有理同伦不变量**：Pontryagin 类在有理同伦意义下是不变的。

**Thom-Pontryagin 定理**：两个紧定向流形 $M$ 和 $N$ 是定向配边的，当且仅当它们的所有 Stiefel-Whitney 数和 Pontryagin 数相等。

**Hirzebruch 符号差定理**：设 $M$ 是紧定向 $4k$ 维流形。则 $M$ 的符号差 $\sigma(M)$ 可以表示为 Pontryagin 类的多项式：
$$\sigma(M) = \langle L_k(p_1, \ldots, p_k), [M] \rangle$$

其中 $L_k$ 是 Hirzebruch $L$-多项式。

**前几个 $L$-多项式**：
- $L_1 = \frac{1}{3} p_1$
- $L_2 = \frac{1}{45}(7p_2 - p_1^2)$
- $L_3 = \frac{1}{945}(62p_3 - 13p_1 p_2 + 2p_1^3)$

**Pontryagin 类的万有性质**：
$$H^*(BO; \mathbb{Z}) \otimes \mathbb{Z}[1/2] \cong \mathbb{Z}[1/2][p_1, p_2, \ldots]$$

其中 $|p_i| = 4i$。

## 四、证明过程

**步骤 1：复化丛的构造**

设 $E \to M$ 是实向量丛，转移函数为 $g_{\alpha\beta}: U_\alpha \cap U_\beta \to GL(n, \mathbb{R})$。

定义复化丛 $E \otimes \mathbb{C}$，其转移函数为 $g_{\alpha\beta} \otimes 1: U_\alpha \cap U_\beta \to GL(n, \mathbb{C})$。

$E \otimes \mathbb{C}$ 是复向量丛，可以定义 Chern 类 $c_i(E \otimes \mathbb{C})$。

**步骤 2：Pontryagin 类的定义**

定义 $p_i(E) = (-1)^i c_{2i}(E \otimes \mathbb{C}) \in H^{4i}(M; \mathbb{Z})$。

符号 $(-1)^i$ 的选取是为了使某些公式更简洁。

**步骤 3：证明 $p_i$ 是实的**

需要证明 $c_{2i+1}(E \otimes \mathbb{C})$ 是 2-扭元。

考虑复共轭映射 $\sigma: E \otimes \mathbb{C} \to E \otimes \mathbb{C}$，$\sigma(v \otimes z) = v \otimes \bar{z}$。

由于 $\sigma$ 是反线性同构，$\sigma^*(E \otimes \mathbb{C}) \cong \overline{E \otimes \mathbb{C}}$。

由 Chern 类的性质，$c_i(\bar{E}) = (-1)^i c_i(E)$。

因此 $c_i(E \otimes \mathbb{C}) = c_i(\overline{E \otimes \mathbb{C}}) = (-1)^i c_i(E \otimes \mathbb{C})$。

当 $i$ 为奇数时，$c_i(E \otimes \mathbb{C}) = -c_i(E \otimes \mathbb{C})$，即 $2c_i(E \otimes \mathbb{C}) = 0$。

**步骤 4：Whitney 和公式**

由 Chern 类的 Whitney 和公式：
$$c(E \otimes \mathbb{C} \oplus F \otimes \mathbb{C}) = c(E \otimes \mathbb{C}) \cdot c(F \otimes \mathbb{C})$$

由于 $(E \oplus F) \otimes \mathbb{C} \cong (E \otimes \mathbb{C}) \oplus (F \otimes \mathbb{C})$，得到：
$$p(E \oplus F) = p(E) \cdot p(F) \mod \text{2-扭元}$$

**步骤 5：万有性质的证明**

考虑分类空间 $BO(n)$ 和 $BU(n)$。复化给出映射 $c: BO(n) \to BU(n)$。

诱导的上同调映射 $c^*: H^*(BU(n); \mathbb{Z}) \to H^*(BO(n); \mathbb{Z})$ 将 Chern 类映射到 Pontryagin 类。

通过分析 $H^*(BO; \mathbb{Z})$ 的结构，可以证明 Pontryagin 类生成 $H^*(BO; \mathbb{Z}) \otimes \mathbb{Z}[1/2]$。

**步骤 6：Hirzebruch 符号差定理的证明**

设 $M$ 是紧定向 $4k$ 维流形。交形式 $Q: H^{2k}(M; \mathbb{R}) \times H^{2k}(M; \mathbb{R}) \to \mathbb{R}$ 定义为：
$$Q(\alpha, \beta) = \langle \alpha \cup \beta, [M] \rangle$$

符号差 $\sigma(M)$ 是 $Q$ 的正特征值个数减负特征值个数。

Hirzebruch 使用指标定理和 Atiyah-Singer 指标定理的特殊情形，证明：
$$\sigma(M) = \langle L_k(p_1, \ldots, p_k), [M] \rangle$$

**步骤 7：Novikov 定理的证明**

Novikov 证明了 Pontryagin 类在有理同伦意义下是不变的。

证明使用手术理论和配边理论的深刻结果。基本思想是通过手术将同胚分解为基本手术的组合，然后证明每个手术不改变有理 Pontryagin 类。

**步骤 8：配边不变量的证明**

如果 $M = \partial W$，则切丛满足 $TW|_M \cong TM \oplus \nu$，其中 $\nu$ 是法丛（平凡丛）。

因此 $p(M) = p(W)|_M$。

由 Stokes 定理，对于 $4k$ 维闭形式 $\omega$，$\int_M \omega = \int_W d\omega$。

由于 $p_{i_1} \cdots p_{i_r}$ 是闭形式，且 $d(p_{i_1} \cdots p_{i_r}) = 0$，得到 $p_{i_1} \cdots p_{i_r}[M] = 0$。

## 五、应用与意义

**理论意义**：
1. **流形分类**：Pontryagin 类和 Pontryagin 数是流形分类的重要不变量。

2. **配边理论**：Pontryagin 数是定向配边群的基本不变量，Thom-Pontryagin 定理使用它们刻画配边关系。

3. **指标理论**：Pontryagin 类在 Atiyah-Singer 指标定理中扮演核心角色。

**应用领域**：
1. **微分拓扑**：用于研究流形的微分结构，如 exotic sphere 的分类。

2. **代数几何**：Pontryagin 类的概念被推广到代数簇。

3. **数学物理**：在规范场论和弦理论中，Pontryagin 类描述拓扑效应。

4. **几何分析**：在研究 Einstein 流形和特殊和乐流形时，Pontryagin 类提供拓扑约束。

**具体应用实例**：
- **Exotic spheres**：Milnor 使用 Pontryagin 类构造了 exotic 7 维球面
- **Hirzebruch 符号差定理**：$\sigma(\mathbb{CP}^2) = 1$，$p_1(\mathbb{CP}^2) = 3$，验证 $L_1 = \frac{1}{3}p_1$
- **Rokhlin 定理**：如果 $M$ 是 spin 4 维流形，则 $\sigma(M) \equiv 0 \pmod{16}$

**推广与发展**：
- **Chern 类**：复向量丛的特征类
- **Euler 类**：定向实向量丛的 Euler 类
- **Stiefel-Whitney 类**：实向量丛的 $\mathbb{Z}_2$ 值特征类
- **K-理论特征类**：在 K-理论中的推广
- **二次型特征类**：更一般的特征类理论
