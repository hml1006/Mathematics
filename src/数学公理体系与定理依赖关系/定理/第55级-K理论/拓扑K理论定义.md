# 拓扑 K 理论定义

> **一句话大白话**：给空间上的"向量丛"排座次——把同构的、可稳定加加减减的丛归成一个群（K群），用组合数字刻画"空间能抖出多少种不同纬度方向的纤维层"，是"二维上的抽象算术"。
>
> **小例子**：对紧致 X，$K(X)$ 由复向量丛的稳定等价类构成、取直和为加法；$K(\{*\})=\mathbb{Z}$，而 $K(S^2)$ 有一个额外的 $\mathbb{Z}$（对应 Hopf 丛），如同给空间发一张"纤维系数的户口卡"。

## 一、定理介绍

> **前置依赖**：向量丛与直和运算、Grothendieck 群构造、约化悬化空间、向量丛的同伦不变性、广义上同调公理

拓扑 K 理论是代数拓扑的一个重要分支，由 Friedrich Hirzebruch 于 1950 年代中期引入，后经 Michael Atiyah 等人发展完善。它通过研究拓扑空间上的向量丛来定义新的拓扑不变量，为代数拓扑提供了强大的工具。

K 理论的核心思想是将向量丛的分类问题转化为代数结构的研究。与同调群和上同调群不同，K 理论是一个广义上同调理论，具有乘法结构，并且在指标定理等深刻结果中扮演关键角色。

## 二、原理思路

### 基本构造思想

拓扑 K 理论的构造基于以下观察：

1. **向量丛的稳定性**：对于紧空间 $X$ 上的向量丛，直接和运算 $\oplus$ 满足交换律和结合律，但不满足消去律。通过 Grothendieck 群构造，我们可以得到一个群结构。

2. **约化 K 理论**：对于基点空间 $(X, x_0)$，定义约化 K 群 $\tilde{K}(X)$ 为 $K(X)$ 模去平凡丛的部分。

3. **悬化同构**：关键洞察是 $\tilde{K}(X)$ 与 $\tilde{K}(\Sigma^2 X)$ 之间存在周期性同构关系，这引出了 Bott 周期性定理。

### 公理化方法

K 理论满足 Eilenberg-Steenrod 公理的推广版本：
- 同伦不变性
- 精确序列
- 切除性质
- 维度公理（在广义意义下）

## 三、定理的严格表述

**定义 1（K 群）** 设 $X$ 为紧 Hausdorff 空间。定义 $\text{Vect}(X)$ 为 $X$ 上复向量丛的同构类的集合。在直接和运算 $\oplus$ 下，$\text{Vect}(X)$ 构成一个交换半群。

**K 群** $K(X)$ 定义为 $\text{Vect}(X)$ 的 Grothendieck 群，即：
$$K(X) = \{[E] - [F] : E, F \in \text{Vect}(X)\}$$
其中等价关系为 $[E_1] - [F_1] = [E_2] - [F_2]$ 当且仅当存在 $G \in \text{Vect}(X)$ 使得
$$E_1 \oplus F_2 \oplus G \cong E_2 \oplus F_1 \oplus G$$

**定理 1（K 群的基本性质）** 
1. $K(X)$ 是交换群，群运算为 $[E] - [F] + [E'] - [F'] = [E \oplus E'] - [F \oplus F']$
2. 若 $f: X \to Y$ 连续，则诱导同态 $f^*: K(Y) \to K(X)$
3. 同伦映射诱导相同的同态：若 $f \simeq g$，则 $f^* = g^*$
4. 对于直积空间，存在自然同构 $K(X \times Y) \cong K(X) \otimes K(Y)$（在某些条件下）

**定义 2（约化 K 群）** 设 $(X, x_0)$ 为基点空间。定义约化 K 群为：
$$\tilde{K}(X) = \ker(i^*: K(X) \to K(\{x_0\}))$$
其中 $i: \{x_0\} \hookrightarrow X$ 为包含映射。

**定理 2** 对于基点空间 $(X, x_0)$，有直和分解：
$$K(X) \cong \tilde{K}(X) \oplus \mathbb{Z}$$
其中 $\mathbb{Z}$ 由平凡线丛的类生成。

**定义 3（高阶 K 群）** 对于 $n \geq 0$，定义：
$$K^{-n}(X) = \tilde{K}(\Sigma^n X)$$
其中 $\Sigma^n X$ 表示 $X$ 的 $n$ 重约化悬化。

## 四、证明过程

### K 群的良定义性证明

**步骤 1：Grothendieck 群构造**

设 $S = \text{Vect}(X)$ 为交换半群。定义 $S \times S$ 上的等价关系：
$$(E_1, F_1) \sim (E_2, F_2) \iff \exists G \in S, E_1 \oplus F_2 \oplus G \cong E_2 \oplus F_1 \oplus G$$

**验证等价关系：**
- **自反性**：$(E, F) \sim (E, F)$，取 $G = \emptyset$（零丛）
- **对称性**：显然
- **传递性**：若 $(E_1, F_1) \sim (E_2, F_2)$ 且 $(E_2, F_2) \sim (E_3, F_3)$，则存在 $G_1, G_2$ 使得
  $$E_1 \oplus F_2 \oplus G_1 \cong E_2 \oplus F_1 \oplus G_1$$
  $$E_2 \oplus F_3 \oplus G_2 \cong E_3 \oplus F_2 \oplus G_2$$
  将第一式与 $F_3 \oplus G_2$ 直和，第二式与 $F_1 \oplus G_1$ 直和，利用同构的组合可得 $(E_1, F_1) \sim (E_3, F_3)$

**步骤 2：群结构**

定义 $K(X) = (S \times S) / \sim$，记 $[E, F]$ 为等价类。定义加法：
$$[E_1, F_1] + [E_2, F_2] = [E_1 \oplus E_2, F_1 \oplus F_2]$$

**验证良定义性**：若 $(E_1, F_1) \sim (E_1', F_1')$ 且 $(E_2, F_2) \sim (E_2', F_2')$，则存在 $G_1, G_2$ 使得
$$E_1 \oplus F_1' \oplus G_1 \cong E_1' \oplus F_1 \oplus G_1$$
$$E_2 \oplus F_2' \oplus G_2 \cong E_2' \oplus F_2 \oplus G_2$$
直和这两个同构式，得
$$(E_1 \oplus E_2) \oplus (F_1' \oplus F_2') \oplus (G_1 \oplus G_2) \cong (E_1' \oplus E_2') \oplus (F_1 \oplus F_2) \oplus (G_1 \oplus G_2)$$
因此 $(E_1 \oplus E_2, F_1 \oplus F_2) \sim (E_1' \oplus E_2', F_1' \oplus F_2')$

**步骤 3：单位元和逆元**

- **零元**：$[0, 0]$，其中 $0$ 表示零丛
- **逆元**：$-[E, F] = [F, E]$

验证：$[E, F] + [F, E] = [E \oplus F, F \oplus E] = [0, 0]$（因为 $E \oplus F \oplus 0 \cong F \oplus E \oplus 0$）

### 同伦不变性证明

**定理**：若 $f, g: X \to Y$ 同伦，则 $f^* = g^*: K(Y) \to K(X)$

**证明思路**：

设 $H: X \times [0, 1] \to Y$ 为同伦，$H(x, 0) = f(x)$，$H(x, 1) = g(x)$。

对于 $Y$ 上的向量丛 $E$，考虑 $X \times [0, 1]$ 上的拉回丛 $H^*E$。

**关键引理**：对于紧空间 $X$，若 $p: X \times [0, 1] \to X$ 为投影，则 $p^*: \text{Vect}(X) \to \text{Vect}(X \times [0, 1])$ 是双射。

**引理证明**：
- **单射**：显然 $p^*E \cong p^*F \implies E \cong F$
- **满射**：利用 $[0, 1]$ 的紧致性和向量丛的局部平凡性，可以证明 $X \times [0, 1]$ 上的任何向量丛都同构于某个 $X$ 上向量丛的拉回

由此，$i_0^* H^* E \cong i_1^* H^* E$，其中 $i_t: X \to X \times [0, 1]$ 为 $i_t(x) = (x, t)$。

因此 $f^*E = i_0^* H^* E \cong i_1^* H^* E = g^*E$，即 $f^*[E] = g^*[E]$。

### 约化 K 群的直和分解

**证明**：定义映射
$$\phi: K(X) \to \tilde{K}(X) \oplus \mathbb{Z}$$
$$\phi([E] - [F]) = ([E] - [F] - (\text{rank}(E) - \text{rank}(F))[\mathbb{C}]), (\text{rank}(E) - \text{rank}(F)))$$

其中 $[\mathbb{C}]$ 表示平凡线丛的类。

**验证同构**：
- **同态**：直接验证保持加法
- **单射**：若 $\phi([E] - [F]) = (0, 0)$，则 $\text{rank}(E) = \text{rank}(F)$ 且 $[E] - [F] = (\text{rank}(E) - \text{rank}(F))[\mathbb{C}] = 0$
- **满射**：对任意 $([E] - [F], n) \in \tilde{K}(X) \oplus \mathbb{Z}$，取 $[E \oplus n\mathbb{C}] - [F] \in K(X)$（当 $n \geq 0$）

## 五、应用与意义

### 1. 向量丛分类

K 理论为向量丛的分类提供了强大的代数工具。通过计算空间的 K 群，可以确定该空间上向量丛的结构。

**例子**：计算 $K(S^2)$
- 利用 clutching 构造，$S^2$ 上的向量丛由 $\pi_1(U(n))$ 的元素分类
- 由于 $\pi_1(U(n)) \cong \mathbb{Z}$，得到 $\tilde{K}(S^2) \cong \mathbb{Z}$
- 生成元为 Hopf 线丛 $H - 1$，其中 $H$ 为 Hopf 丛

### 2. J-函子与 Adams 运算

K 理论中的 Adams 运算 $\psi^k$ 在研究球面同伦群和 J-函子中发挥关键作用。Adams 利用 K 理论证明了向量场问题的完整解答。

### 3. 指标定理

Atiyah-Singer 指标定理的 K 理论表述是最优雅的形式之一：
$$\text{ind}(D) = \int_{T^*M} \text{ch}([\sigma(D)]) \cdot \text{td}(T^*M \otimes \mathbb{C})$$
其中 $\text{ch}$ 为 Chern 特征标，$\text{td}$ 为 Todd 类。

### 4. 广义上同调理论

K 理论是一个广义上同调理论，满足：
- 同伦公理
- 精确序列公理
- 切除公理
- 加法公理

这为研究拓扑空间提供了新的视角和工具。

### 5. 算子代数中的应用

K 理论在 C*-代数的分类中扮演核心角色。AF 代数、纯无限单 C*-代数等的分类都依赖于 K 理论不变量。

### 6. 物理学应用

在弦理论和凝聚态物理中，K 理论用于分类 D-膜电荷和拓扑绝缘体。例如，Type II 弦理论中的 D-膜电荷由 K 理论群 $K(X)$ 或 $KO(X)$ 分类。
