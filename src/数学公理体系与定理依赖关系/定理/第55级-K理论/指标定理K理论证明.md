# 指标定理的 K 理论证明

> **一句话大白话**：一个椭圆算子的"缺口"（核减余核的维数=指标）是个拓扑不变量，能翻译成 K 理论里的"特征标组合"去算——用拓扑唯一签名就把分析量算干净，这是 Atiyah-Singer 指标定理用 K 理论的漂亮处理。
>
> **小例子**：指标定理说 $\mathrm{ind}(D)=(-1)^n\langle\mathrm{ch}[\sigma_D]\cdot\mathrm{Td}(TX),[X]\rangle$，其中符号在 K 理论里取守恒类；如 $\mathbb{S}^2$ 上 Dirac 算子的指标恰为 ±1，恰好对应第一 Chern 数。

## 一、定理介绍

Atiyah-Singer 指标定理是 20 世纪数学最伟大的成就之一，由 Michael Atiyah 和 Isadore Singer 于 1963 年证明。该定理建立了椭圆微分算子的解析指标与其拓扑指标之间的深刻联系，揭示了解析学、拓扑学和几何学之间的内在统一性。

K 理论证明是指标定理最优雅的证明方式之一，由 Atiyah 和 Singer 在 1968 年左右发展完善。这一证明将指标问题转化为 K 理论中的代数问题，利用 K 理论的函子性和 Bott 周期性，给出了指标定理的简洁而深刻的证明。

## 二、原理思路

### 核心思想

K 理论证明的核心洞察是：

1. **指标的同伦不变性**：椭圆算子的指标在连续变形下保持不变，这意味着指标只依赖于算子的象征类。

2. **K 理论的函子性**：指标可以看作是从 K 理论群到整数的同态，利用 K 理论的自然变换可以简化计算。

3. **约化到基本情形**：通过 K 理论的函子性和 Thom 同构，可以将一般流形上的指标问题约化到欧氏空间上的基本情形。

4. **Bott 周期性的应用**：Bott 周期性提供了关键的 Thom 同构，使得可以在切丛的余切丛上定义推前映射。

### 证明策略

K 理论证明的主要步骤：

1. **定义象征映射**：从微分算子到 K 理论的切丛。
2. **构造 Thom 同构**：利用 K 理论的 Thom 同构将问题转移到余切丛。
3. **定义拓扑指标**：通过推前映射到点，定义拓扑指标。
4. **证明相等性**：通过局部化原理和指标的同伦不变性，证明解析指标等于拓扑指标。

## 三、定理的严格表述

**定义 1（椭圆算子）** 设 $M$ 为紧光滑流形，$E, F$ 为 $M$ 上的向量丛。微分算子 $D: \Gamma(E) \to \Gamma(F)$ 的**象征** $\sigma(D)$ 是余切丛 $T^*M$ 上的丛同态：
$$\sigma(D): \pi^*E \to \pi^*F$$
其中 $\pi: T^*M \to M$ 为投影。

$D$ 称为**椭圆**的，若 $\sigma(D)$ 在 $T^*M \setminus \{0\}$ 上处处可逆。

**定义 2（解析指标）** 椭圆算子 $D$ 的**解析指标**定义为：
$$\text{ind}(D) = \dim \ker D - \dim \text{coker} D$$
其中 $\ker D$ 和 $\text{coker} D$ 分别为 $D$ 的核和余核。

**定理 1（象征类的良定义性）** 椭圆算子 $D$ 的象征 $\sigma(D)$ 定义了 K 理论群中的一个元素：
$$[\sigma(D)] \in K(T^*M)$$
且若 $D_t$ 为椭圆算子的连续族，则 $[\sigma(D_t)]$ 在 $K(T^*M)$ 中恒定。

**定义 3（拓扑指标）** 设 $M$ 为紧流形，$i: M \to \mathbb{R}^N$ 为嵌入。定义**拓扑指标**同态：
$$\text{t-ind}: K(T^*M) \to \mathbb{Z}$$
为复合映射：
$$K(T^*M) \xrightarrow{i_!} K(T^*\mathbb{R}^N) \xrightarrow{\text{Thom}^{-1}} K(\mathbb{R}^{2N}) \xrightarrow{\text{excision}} K(T^*\text{pt}) \cong \mathbb{Z}$$
其中 $i_!$ 为 Thom 同构的逆（推前映射）。

**定理 2（Atiyah-Singer 指标定理）** 设 $D$ 为紧流形 $M$ 上的椭圆算子。则：
$$\text{ind}(D) = \text{t-ind}([\sigma(D)])$$

**定理 3（指标定理的显式公式）** 在 de Rham 上同调中，指标定理可以写为：
$$\text{ind}(D) = (-1)^n \int_{T^*M} \text{ch}([\sigma(D)]) \cdot \text{td}(T^*M \otimes \mathbb{C})$$
其中 $n = \dim M$，$\text{ch}$ 为 Chern 特征标，$\text{td}$ 为 Todd 类。

**定理 4（K 理论版本的指标定理）** 指标定理等价于以下交换图：
$$\begin{array}{ccc}
K(T^*M) & \xrightarrow{\text{ind}} & \mathbb{Z} \\
\downarrow{\text{ch}} & & \| \\
H^{\text{even}}(T^*M; \mathbb{Q}) & \xrightarrow{\int \cdot \text{td}} & \mathbb{Z}
\end{array}$$
其中左边的垂直映射为 Chern 特征标，右边的垂直映射为恒等映射。

## 四、证明过程

### 步骤 1：象征类的良定义性

**引理 1**：椭圆算子 $D$ 的象征 $\sigma(D)$ 在 $T^*M \setminus \{0\}$ 上可逆，因此定义了 $K(B(T^*M), S(T^*M))$ 中的元素，其中 $B(T^*M)$ 和 $S(T^*M)$ 分别为单位球丛和单位球面丛。

**证明**：
- 由椭圆性，$\sigma(D)(x, \xi)$ 对 $\xi \neq 0$ 可逆
- 通过齐次性假设，可以假设 $\sigma(D)$ 在 $S(T^*M)$ 上为恒等映射
- 因此 $\sigma(D)$ 定义了相对 K 群 $K(B(T^*M), S(T^*M))$ 中的元素
- 由 Thom 同构，$K(B(T^*M), S(T^*M)) \cong K(T^*M)$

**引理 2**：若 $D_t$ 为椭圆算子的连续族，则 $[\sigma(D_t)]$ 在 $K(T^*M)$ 中恒定。

**证明**：
- 椭圆算子的空间是开的，因此 $D_t$ 定义了从 $[0, 1]$ 到椭圆算子空间的连续映射
- 象征映射 $\sigma: \text{Ell}(M) \to K(T^*M)$ 是连续的
- 由于 $[0, 1]$ 连通，$[\sigma(D_t)]$ 在 $K(T^*M)$ 中恒定

### 步骤 2：Thom 同构与推前映射

**定义 Thom 同构**：对于向量丛 $E \to M$，Thom 同构是：
$$\phi: K(M) \xrightarrow{\cong} K(E, E \setminus M)$$
其中 $M$ 作为零截面嵌入 $E$。

**构造**：
- 对于线丛 $L$，$\phi(x) = \pi^*x \cdot \lambda$，其中 $\lambda$ 为 Thom 类
- 对于一般向量丛，通过分裂原理定义

**推前映射**：对于嵌入 $i: M \to N$，法丛为 $\nu$。定义推前映射：
$$i_!: K(T^*M) \to K(T^*N)$$
为复合：
$$K(T^*M) \xrightarrow{\pi_!} K(\nu, \nu \setminus M) \xrightarrow{\text{Thom}^{-1}} K(T^*N)$$
其中 $\pi_!$ 为沿法丛的推前。

### 步骤 3：约化到欧氏空间

**关键约化**：通过嵌入 $i: M \to \mathbb{R}^N$，可以将指标问题约化到 $\mathbb{R}^N$。

**引理 3**：对于 $\mathbb{R}^N$ 上的椭圆算子，指标定理可以直接验证。

**证明**：
- $\mathbb{R}^N$ 上的椭圆算子可以通过紧化转化为 $S^N$ 上的算子
- 对于 $S^N$，K 理论和上同调都是已知的
- 通过显式计算，可以验证指标定理

### 步骤 4：指标的同伦不变性

**定理**：解析指标 $\text{ind}(D)$ 只依赖于象征类 $[\sigma(D)] \in K(T^*M)$。

**证明**：
- 设 $D_0, D_1$ 为两个椭圆算子，$[\sigma(D_0)] = [\sigma(D_1)]$
- 由象征类的定义，存在椭圆算子的连续族 $D_t$ 连接 $D_0$ 和 $D_1$
- 由引理 2，$[\sigma(D_t)]$ 在 $K(T^*M)$ 中恒定
- 由于指标是整数值的连续函数，$\text{ind}(D_t)$ 必须恒定
- 因此 $\text{ind}(D_0) = \text{ind}(D_1)$

### 步骤 5：乘性性质

**引理 4**：指标映射 $\text{ind}: K(T^*M) \to \mathbb{Z}$ 是群同态。

**证明**：
- 设 $D_1, D_2$ 为椭圆算子，象征类为 $[\sigma(D_1)], [\sigma(D_2)]$
- 定义张量积算子 $D_1 \otimes D_2$，其象征为 $[\sigma(D_1)] \cdot [\sigma(D_2)]$
- 由指标的可加性，$\text{ind}(D_1 \oplus D_2) = \text{ind}(D_1) + \text{ind}(D_2)$
- 因此指标是群同态

### 步骤 6：证明指标定理

**主要步骤**：

**步骤 6.1：定义拓扑指标**

对于嵌入 $i: M \to \mathbb{R}^N$，定义拓扑指标为：
$$\text{t-ind}([\sigma(D)]) = i_!([\sigma(D)]) \in K(T^*\mathbb{R}^N) \cong K(\mathbb{R}^{2N}) \cong \mathbb{Z}$$

**步骤 6.2：证明解析指标等于拓扑指标**

需要证明 $\text{ind}(D) = \text{t-ind}([\sigma(D)])$。

**方法 1：局部化原理**

- 对于 $\mathbb{R}^N$ 上的算子，可以直接计算
- 通过嵌入，将 $M$ 上的算子局部化为 $\mathbb{R}^N$ 上的算子
- 利用指标的同伦不变性，证明两者相等

**方法 2：K 理论的函子性**

- 定义自然变换 $\alpha: K(T^*M) \to \mathbb{Z}$ 为解析指标
- 定义自然变换 $\beta: K(T^*M) \to \mathbb{Z}$ 为拓扑指标
- 证明 $\alpha$ 和 $\beta$ 都满足相同的函子性性质
- 由 K 理论的万有性质，$\alpha = \beta$

**方法 3：指标公式的推导**

使用 Chern 特征标和 Todd 类：
$$\text{ind}(D) = (-1)^n \int_{T^*M} \text{ch}([\sigma(D)]) \cdot \text{td}(T^*M \otimes \mathbb{C})$$

**推导**：
- 由 Thom 同构，$\text{ch} \circ i_! = i_* \circ (\text{ch} \cdot \text{td}^{-1})$
- 对于 $\mathbb{R}^{2N}$，$\text{td}(T^*\mathbb{R}^{2N} \otimes \mathbb{C}) = 1$
- 因此 $\text{t-ind}([\sigma(D)]) = (-1)^n \int_{T^*M} \text{ch}([\sigma(D)]) \cdot \text{td}(T^*M \otimes \mathbb{C})$

### 步骤 7：特殊情况验证

**例子 1：de Rham 算子**

对于 de Rham 复形，$D = d + d^*$，指标为 Euler 示性数：
$$\text{ind}(D) = \chi(M) = \sum_{k=0}^n (-1)^k b_k$$

由指标定理：
$$\chi(M) = \int_M \text{td}(TM \otimes \mathbb{C}) \cdot \text{ch}([\sigma(D)])$$

计算可得 $\chi(M) = \int_M e(TM)$，其中 $e(TM)$ 为 Euler 类，这正是 Gauss-Bonnet 定理。

**例子 2：Dirac 算子**

对于 Spin 流形上的 Dirac 算子 $D$，指标为 $\hat{A}$-亏格：
$$\text{ind}(D) = \hat{A}(M) = \int_M \hat{A}(TM)$$

这与 Lichnerowicz 定理一致：若 $\hat{A}(M) \neq 0$，则 $M$ 不允许正数量曲率度量。

**例子 3：Signature 算子**

对于 signature 算子，指标为 signature：
$$\text{ind}(D) = \text{sign}(M) = \int_M L(TM)$$
其中 $L$ 为 Hirzebruch L-类。

## 五、应用与意义

### 1. 微分几何

指标定理在微分几何中有广泛应用：

**正数量曲率**：若 $M$ 允许正数量曲率度量，则 $\hat{A}(M) = 0$。

**复流形**：对于 Kähler 流形，指标定理给出 Hirzebruch-Riemann-Roch 定理。

### 2. 代数几何

在代数几何中，指标定理用于证明：

**Riemann-Roch 定理**：对于代数簇上的向量丛，Euler 示性数可以用 Chern 类表示。

**Lefschetz 不动点定理**：通过指标定理可以证明 Lefschetz 不动点定理。

### 3. 表示论

指标定理在表示论中的应用：

**字符公式**：通过指标定理可以推导 Lie 群的字符公式。

**分支律**：指标定理用于研究表示的分支律。

### 4. 数学物理

在量子场论和弦理论中：

**反常**：指标定理用于计算量子场论中的反常。

**指数定理与超对称**：Dirac 算子的指标与超对称量子力学相关。

**D-膜电荷**：在弦理论中，D-膜电荷由 K 理论分类，指标定理用于计算电荷。

### 5. 拓扑

指标定理在拓扑中的应用：

**流形的分类**：通过指标定理可以区分不同微分结构的流形。

**不变量**：$\hat{A}$-亏格、signature 等是重要的微分拓扑不变量。

### 6. K 理论的发展

指标定理的 K 理论证明推动了 K 理论的发展：

**等变 K 理论**：Atiyah-Segal 发展了等变 K 理论，用于研究群作用下的指标定理。

** families 指标定理**：将指标定理推广到参数族的情形。

**高阶指标定理**：研究更高阶 K 群中的指标。

### 7. 非交换几何

在 Connes 的非交换几何中：

**叶状空间**：指标定理用于研究叶状空间的"非交换几何"。

**C*-代数扩张**：指标定理用于研究 C*-代数的扩张理论。

### 8. 数论

在数论中的应用：

**算术指标定理**：将指标定理推广到算术簇。

**L-函数**：指标定理与 L-函数的特殊值相关。

### 9. 现代发展

指标定理的现代发展包括：

**索引定理的范畴化**：研究指标定理的高阶版本。

**导出代数几何**：在导出代数几何框架下重新理解指标定理。

**同伦论方法**：使用稳定同伦论的工具研究指标定理。
