# Gelfand-Naimark 定理（交换情形）

## 一、定理介绍

Gelfand-Naimark 定理（交换情形）是 C*-代数理论中的基础性定理，它建立了交换 C*-代数与局部紧 Hausdorff 空间上连续函数代数之间的对偶关系。这个定理最早由 I.M. Gelfand 和 M.A. Naimark 在 1943 年提出，标志着算子代数理论的诞生。

该定理的核心思想是：任何交换 C*-代数都可以通过 Gelfand 变换表示为某个局部紧 Hausdorff 空间上的连续函数代数。这为研究抽象的交换 C*-代数提供了具体的几何模型，建立了代数与分析、拓扑之间的深刻联系。

## 二、原理思路

Gelfand-Naimark 定理的证明基于以下几个关键概念：

1. **特征标空间**：交换 C*-代数 $A$ 的特征标是指非零的乘法线性泛函 $\chi : A \to \mathbb{C}$。所有特征标组成的集合称为特征标空间（或 Gelfand 谱），记为 $\hat{A}$ 或 $\Delta(A)$。

2. **Gelfand 变换**：对每个 $a \in A$，定义其 Gelfand 变换 $\hat{a} : \hat{A} \to \mathbb{C}$ 为 $\hat{a}(\chi) = \chi(a)$。Gelfand 变换将 $A$ 中的元素映射为 $\hat{A}$ 上的函数。

3. **Gelfand 拓扑**：在 $\hat{A}$ 上赋予弱*拓扑（即作为 $A^*$ 的子集继承的拓扑），使其成为局部紧 Hausdorff 空间。

4. **核心等式**：对交换 C*-代数，Gelfand 变换是等距同构，即 $\|\hat{a}\|_\infty = \|a\|$。

证明的关键步骤是：
- 证明特征标空间非空（使用极大理想的存在性）
- 证明 Gelfand 变换是代数同态
- 利用 C*-恒等式证明等距性
- 应用 Stone-Weierstrass 定理证明满射性

## 三、定理的严格表述

**定义 1（特征标）**：设 $A$ 是交换 C*-代数，$A$ 的特征标是指满足以下条件的映射 $\chi : A \to \mathbb{C}$：
1. $\chi \neq 0$（非零）
2. $\chi(ab) = \chi(a)\chi(b)$（乘法性）
3. $\chi(\lambda a + \mu b) = \lambda\chi(a) + \mu\chi(b)$（线性）

$A$ 的所有特征标组成的集合记为 $\hat{A}$ 或 $\Delta(A)$，称为 $A$ 的 Gelfand 谱或特征标空间。

**定义 2（Gelfand 变换）**：设 $A$ 是交换 C*-代数，Gelfand 变换是指映射 $\Gamma : A \to C_0(\hat{A})$，定义为
$$\Gamma(a) = \hat{a}, \quad \text{其中 } \hat{a}(\chi) = \chi(a)$$
这里 $C_0(\hat{A})$ 表示 $\hat{A}$ 上在无穷远处消失的连续函数空间。

**定理 1（交换 C*-代数的 Gelfand-Naimark 定理）**：设 $A$ 是交换 C*-代数，则：

1. **特征标空间的性质**：$\hat{A}$ 在弱*拓扑下是局部紧 Hausdorff 空间。若 $A$ 有单位元，则 $\hat{A}$ 是紧致的。

2. **Gelfand 变换的性质**：Gelfand 变换 $\Gamma : A \to C_0(\hat{A})$ 是等距 *-同构，即：
   - $\Gamma$ 是双射
   - $\|\hat{a}\|_\infty = \|a\|$（等距）
   - $\widehat{a^*} = \overline{\hat{a}}$（保持对合）
   - $\widehat{ab} = \hat{a}\hat{b}$（保持乘法）

3. **谱的刻画**：对任意 $a \in A$，$\sigma(a) = \hat{a}(\hat{A}) \cup \{0\}$（若 $A$ 无单位元）或 $\sigma(a) = \hat{a}(\hat{A})$（若 $A$ 有单位元）。

**定理 2（交换 C*-代数的分类）**：映射 $X \mapsto C_0(X)$ 建立了局部紧 Hausdorff 空间（在同胚意义下）与交换 C*-代数（在等距 *-同构意义下）之间的一一对应。

## 四、证明过程

**定理 1 的证明**：

**步骤 1：特征标与极大理想的关系**

设 $\chi$ 是 $A$ 的特征标，则 $\ker\chi$ 是 $A$ 的极大理想。

首先，$\ker\chi$ 是理想：若 $a \in \ker\chi$，$b \in A$，则 $\chi(ab) = \chi(a)\chi(b) = 0$，故 $ab \in \ker\chi$。

其次，$\ker\chi$ 是极大的：由于 $\chi \neq 0$，存在 $e \in A$ 使得 $\chi(e) = 1$。对任意 $a \in A$，$a - \chi(a)e \in \ker\chi$，故 $A = \ker\chi + \mathbb{C}e$，因此 $\ker\chi$ 是余维为 1 的理想，必为极大理想。

反之，若 $M$ 是 $A$ 的极大理想，则 $A/M$ 是域。由于 $A$ 是 Banach 代数，$M$ 是闭的，$A/M$ 也是 Banach 代数。由 Gelfand-Mazur 定理，$A/M \cong \mathbb{C}$，故存在特征标 $\chi$ 使得 $M = \ker\chi$。

**步骤 2：特征标的连续性与范数**

设 $\chi$ 是特征标，则 $\|\chi\| = 1$（若 $A$ 有单位元）或 $\|\chi\| \le 1$（若 $A$ 无单位元）。

对任意 $a \in A$，$\chi(a) \in \sigma(a)$，故 $|\chi(a)| \le r(a) \le \|a\|$，因此 $\|\chi\| \le 1$。

若 $A$ 有单位元 $1$，则 $\chi(1) = 1$，故 $\|\chi\| = 1$。

**步骤 3：特征标空间的拓扑性质**

$\hat{A}$ 是 $A^*$ 的子集，赋予弱*拓扑。由 Banach-Alaoglu 定理，$A^*$ 中的单位球在弱*拓扑下是紧致的。

$\hat{A}$ 是闭集：设 $\chi_\alpha$ 是 $\hat{A}$ 中的网，弱*收敛到 $\chi \in A^*$。则对任意 $a, b \in A$，
$$\chi(ab) = \lim_\alpha \chi_\alpha(ab) = \lim_\alpha \chi_\alpha(a)\chi_\alpha(b) = \chi(a)\chi(b)$$
故 $\chi$ 也是乘法线性泛函。若 $\chi \neq 0$，则 $\chi \in \hat{A}$。

因此 $\hat{A}$ 是局部紧 Hausdorff 空间。若 $A$ 有单位元，$\hat{A}$ 包含在单位球中，故是紧致的。

**步骤 4：Gelfand 变换的等距性**

对任意 $a \in A$，要证 $\|\hat{a}\|_\infty = \|a\|$。

首先，$\|\hat{a}\|_\infty = \sup_{\chi \in \hat{A}} |\chi(a)| \le \sup_{\chi \in \hat{A}} \|a\| = \|a\|$。

另一方面，考虑 $A$ 中由 $a$ 生成的闭子代数 $B$。$B$ 是交换 C*-子代数，且 $\sigma_B(a) = \sigma_A(a)$（C*-子代数的谱不变性）。

由谱半径公式，$r(a) = \lim_{n\to\infty} \|a^n\|^{1/n}$。

由于 $\chi(a) \in \sigma(a)$，$|\chi(a)| \le r(a)$，故 $\|\hat{a}\|_\infty \le r(a)$。

对自伴元素 $a = a^*$，由 C*-代数性质，$r(a) = \|a\|$，故 $\|\hat{a}\|_\infty = \|a\|$。

对一般元素 $a$，$a^*a$ 是自伴的，$\|\hat{a}\|_\infty^2 = \|\widehat{a^*a}\|_\infty = \|a^*a\| = \|a\|^2$，故 $\|\hat{a}\|_\infty = \|a\|$。

**步骤 5：Gelfand 变换的满射性**

$\Gamma(A)$ 是 $C_0(\hat{A})$ 的 *-子代数：
- $\Gamma$ 是线性的显然
- $\widehat{ab} = \hat{a}\hat{b}$：$\widehat{ab}(\chi) = \chi(ab) = \chi(a)\chi(b) = \hat{a}(\chi)\hat{b}(\chi)$
- $\widehat{a^*} = \overline{\hat{a}}$：$\widehat{a^*}(\chi) = \chi(a^*) = \overline{\chi(a)} = \overline{\hat{a}(\chi)}$

$\Gamma(A)$ 分离点：若 $\chi_1 \neq \chi_2$，则存在 $a \in A$ 使得 $\chi_1(a) \neq \chi_2(a)$，即 $\hat{a}(\chi_1) \neq \hat{a}(\chi_2)$。

$\Gamma(A)$ 在每点非零：对任意 $\chi \in \hat{A}$，$\chi \neq 0$，故存在 $a \in A$ 使得 $\chi(a) \neq 0$，即 $\hat{a}(\chi) \neq 0$。

由 Stone-Weierstrass 定理，$\Gamma(A)$ 在 $C_0(\hat{A})$ 中稠密。

由于 $\Gamma$ 是等距映射，$\Gamma(A)$ 是闭的，故 $\Gamma(A) = C_0(\hat{A})$。$\square$

## 五、应用与意义

Gelfand-Naimark 定理（交换情形）在数学的多个领域有深远影响：

1. **交换调和分析**：局部紧 Abel 群 $G$ 的群代数 $L^1(G)$ 的 C*-包络同构于 $C_0(\hat{G})$，其中 $\hat{G}$ 是 $G$ 的 Pontryagin 对偶群。这为 Fourier 分析提供了抽象框架。

2. **谱理论的严格化**：定理为正规算子的谱分解提供了严格基础。正规算子生成的 C*-代数是交换的，可以表示为连续函数代数，从而可以用谱定理进行函数演算。

3. **代数几何的启发**：Gelfand 谱的概念启发了代数几何中仿射概形的定义。交换环的素谱与 C*-代数的特征标空间有深刻的类比关系。

4. **非交换几何的起点**：定理表明交换 C*-代数等价于局部紧 Hausdorff 空间的连续函数代数。这促使数学家研究非交换 C*-代数，将其视为"非交换空间"的函数代数，从而发展出非交换几何。

5. **量子力学的数学基础**：在量子力学中，可交换的可观测量对应于交换 C*-代数，可以用经典概率论处理。Gelfand-Naimark 定理为理解量子-经典对应提供了数学工具。

6. **指标定理**：Atiyah-Singer 指标定理的拓扑 K-理论证明中，交换 C*-代数的分类是基础工具。

这个定理展示了数学中代数、分析、拓扑和几何的深刻统一，是现代数学的典范成果之一。
