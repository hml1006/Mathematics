# 代数 K 理论（$K_0$ 与 $K_1$）

> **一句话大白话**：拓扑 K 理论研究"向量丛怎么分"，代数 K 理论改成研究"投射模与自同构"这些代数对象的分类，用环上的 $K_0,K_1,\ldots$ 来记账。
>
> **小例子**：对主理想整环 $R$（如 $\mathbb{Z}$ 或域 $k$），$K_0(R)=\mathbb{Z}$、$K_1(R)=R^\times$；在代数几何与数论里，这组不变量被用来刻画各种环的算术结构。

## 一、定理介绍

> **前置依赖**：投射模与 Grothendieck 群构造、一般线性群与初等矩阵、Dedekind 整环与理想类群、Quillen +构造、Swan 定理

代数 K 理论是 K 理论在代数领域的推广，研究环、代数和其他代数结构的不变量。与拓扑 K 理论研究向量丛不同，代数 K 理论研究投射模、自同构群和其他代数对象。

代数 K 理论由 Alexander Grothendieck 在证明 Grothendieck-Riemann-Roch 定理时引入 $K_0$，随后 Hyman Bass 和 John Milnor 定义了 $K_1$。更高阶的 K 群 $K_n$ 由 Daniel Quillen 于 1972 年给出严格定义，这一突破性工作获得了 1978 年 Fields 奖。

代数 K 理论在数论、代数几何、代数拓扑和算子代数中都有深刻应用，是现代数学的核心领域之一。

## 二、原理思路

### 基本构造思想

代数 K 理论的构造基于以下动机：

1. **$K_0$ 的动机**：对于交换环 $R$，投射模是自由模的推广。$K_0(R)$ 捕捉了投射模的"稳定等价类"，类似于拓扑 K 理论中向量丛的构造。

2. **$K_1$ 的动机**：$K_1(R)$ 与一般线性群 $GL(R)$ 相关，捕捉了环的自同构信息。它类似于拓扑 K 理论中的 $K^{-1}$。

3. **高阶 K 群**：Quillen 的 +构造和 Q构造提供了定义 $K_n(R)$（$n \geq 2$）的方法，这些群包含了环的深层代数信息。

### 关键洞察

代数 K 理论与拓扑 K 理论的联系：
- 对于紧空间 $X$，$K(X) \cong K_0(C(X))$，其中 $C(X)$ 是连续函数环
- Swan 定理：向量丛对应于投射模
- 代数 K 理论可以看作是拓扑 K 理论的"代数版本"

## 三、定理的严格表述

### $K_0$ 群的定义与性质

**定义 1（$K_0$ 群）** 设 $R$ 为含幺环。定义 $\mathcal{P}(R)$ 为 $R$ 上有限生成投射模的同构类集合。在直和运算 $\oplus$ 下，$\mathcal{P}(R)$ 构成交换半群。

**$K_0$ 群** 定义为 $\mathcal{P}(R)$ 的 Grothendieck 群：
$$K_0(R) = \{[P] - [Q] : P, Q \in \mathcal{P}(R)\}$$
其中等价关系为 $[P_1] - [Q_1] = [P_2] - [Q_2]$ 当且仅当存在 $S \in \mathcal{P}(R)$ 使得
$$P_1 \oplus Q_2 \oplus S \cong P_2 \oplus Q_1 \oplus S$$

**定理 1（$K_0$ 的基本性质）**
1. **函子性**：环同态 $f: R \to S$ 诱导同态 $f_*: K_0(R) \to K_0(S)$，$f_*([P]) = [P \otimes_R S]$
2. **Morita 不变性**：若 $R$ 和 $S$ 是 Morita 等价的，则 $K_0(R) \cong K_0(S)$
3. **交换环的秩映射**：对于交换环 $R$，存在秩同态 $\text{rank}: K_0(R) \to C(\text{Spec}(R), \mathbb{Z})$，其中 $C(\text{Spec}(R), \mathbb{Z})$ 是 $\text{Spec}(R)$ 上连续整数函数
4. **局部环**：若 $R$ 为局部环，则 $K_0(R) \cong \mathbb{Z}$，由 $[R]$ 生成

**定理 2（交换环的 $K_0$）** 设 $R$ 为交换环。定义约化 K 群 $\tilde{K}_0(R) = \ker(\text{rank}: K_0(R) \to \mathbb{Z})$。

则 $\tilde{K}_0(R)$ 可以识别为投射模的稳定等价类模去自由模：
$$\tilde{K}_0(R) = \mathcal{P}(R) / \{[P] \sim [Q] \iff \exists \text{ 自由模 } F, P \oplus F \cong Q \oplus F\}$$

**定理 3（Dedekind 整环的 $K_0$）** 设 $R$ 为 Dedekind 整环（如代数整数环）。则：
$$K_0(R) \cong \mathbb{Z} \oplus \text{Cl}(R)$$
其中 $\text{Cl}(R)$ 为理想类群。

特别地，$\tilde{K}_0(R) \cong \text{Cl}(R)$。

### $K_1$ 群的定义与性质

**定义 2（$K_1$ 群）** 设 $R$ 为含幺环。定义一般线性群：
$$GL(R) = \varinjlim GL_n(R)$$
其中 $GL_n(R)$ 为 $R$ 上可逆 $n \times n$ 矩阵群，包含映射为 $A \mapsto \begin{pmatrix} A & 0 \\ 0 & 1 \end{pmatrix}$。

**交换子子群** $[GL(R), GL(R)]$ 为由交换子 $[A, B] = ABA^{-1}B^{-1}$ 生成的子群。

**$K_1$ 群** 定义为：
$$K_1(R) = GL(R) / [GL(R), GL(R)] = GL(R)_{\text{ab}}$$
即 $GL(R)$ 的交换化。

**定理 4（Whitehead 引理）** 对于 $A \in GL_n(R)$，定义稳定化映射 $i: GL_n(R) \to GL(R)$。则：
1. $i(A) \in [GL(R), GL(R)]$ 当且仅当 $A$ 可以表示为初等矩阵的乘积
2. $K_1(R) \cong GL(R) / E(R)$，其中 $E(R)$ 为由初等矩阵生成的子群

**定理 5（交换环的行列式映射）** 设 $R$ 为交换环。行列式映射 $\det: GL(R) \to R^*$ 诱导同态：
$$\det: K_1(R) \to R^*$$
且有直和分解：
$$K_1(R) \cong R^* \oplus SK_1(R)$$
其中 $SK_1(R) = \ker(\det) = SL(R) / [GL(R), GL(R)]$。

**定理 6（域的 $K_1$）** 对于域 $F$，有：
$$K_1(F) \cong F^*$$
因为 $SL(F) = [GL(F), GL(F)]$（对于大多数域）。

### 高阶 K 群

**定义 3（Quillen 的 +构造）** 设 $R$ 为环，$BGL(R)^+$ 为 $BGL(R)$ 的 Quillen +构造（关于完美子群 $[GL(R), GL(R)]$）。

定义高阶 K 群：
$$K_n(R) = \pi_n(BGL(R)^+), \quad n \geq 1$$
且 $K_0(R)$ 由前述定义。

**定理 7（Quillen 的等价性）** +构造给出的 $K_1$ 和 $K_2$ 与前述定义一致。

**定理 8（Q构造）** Quillen 还给出了等价的 Q构造：定义范畴 $Q(R)$，其对象为有限生成投射模，态射为特殊 diagram。则：
$$K_n(R) = \pi_n(\Omega B Q(R))$$

### 拓扑 K 理论与代数 K 理论的关系

**定理 9（Swan 定理）** 设 $X$ 为紧 Hausdorff 空间，$C(X)$ 为连续复值函数环。则：
$$K(X) \cong K_0(C(X))$$
即拓扑 K 理论同构于连续函数环的代数 K 理论。

**定理 10（Karoubi 定理）** 对于 C*-代数 $A$，拓扑 K 理论 $K^{\text{top}}(A)$ 与代数 K 理论 $K^{\text{alg}}(A)$ 在有理系数下同构：
$$K^{\text{top}}_n(A) \otimes \mathbb{Q} \cong K^{\text{alg}}_n(A) \otimes \mathbb{Q}$$

## 四、证明过程

### $K_0$ 的良定义性

**步骤 1：Grothendieck 群构造**

设 $S = \mathcal{P}(R)$ 为交换半群。定义 $S \times S$ 上的等价关系：
$$(P_1, Q_1) \sim (P_2, Q_2) \iff \exists S \in \mathcal{P}(R), P_1 \oplus Q_2 \oplus S \cong P_2 \oplus Q_1 \oplus S$$

**验证等价关系**：
- **自反性**：$(P, Q) \sim (P, Q)$，取 $S = 0$
- **对称性**：显然
- **传递性**：若 $(P_1, Q_1) \sim (P_2, Q_2)$ 且 $(P_2, Q_2) \sim (P_3, Q_3)$，则存在 $S_1, S_2$ 使得
  $$P_1 \oplus Q_2 \oplus S_1 \cong P_2 \oplus Q_1 \oplus S_1$$
  $$P_2 \oplus Q_3 \oplus S_2 \cong P_3 \oplus Q_2 \oplus S_2$$
  直和这两个同构式并重新排列，得 $(P_1, Q_1) \sim (P_3, Q_3)$

**步骤 2：群结构**

定义 $K_0(R) = (S \times S) / \sim$，加法为：
$$[P_1, Q_1] + [P_2, Q_2] = [P_1 \oplus P_2, Q_1 \oplus Q_2]$$

良定义性的验证与拓扑 K 理论类似。

### Dedekind 整环的 $K_0$ 计算

**定理**：对于 Dedekind 整环 $R$，$K_0(R) \cong \mathbb{Z} \oplus \text{Cl}(R)$

**证明**：

**步骤 1：结构定理**

Dedekind 整环上的有限生成投射模具有标准形式：
$$P \cong R^{r-1} \oplus I$$
其中 $r = \text{rank}(P)$，$I$ 为分式理想。

**步骤 2：稳定等价**

两个投射模 $P_1 \cong R^{r_1-1} \oplus I_1$ 和 $P_2 \cong R^{r_2-1} \oplus I_2$ 稳定等价当且仅当：
- $r_1 = r_2$（秩相同）
- $[I_1] = [I_2] \in \text{Cl}(R)$（理想类相同）

**步骤 3：同构构造**

定义映射 $\phi: K_0(R) \to \mathbb{Z} \oplus \text{Cl}(R)$：
$$\phi([P] - [Q]) = (\text{rank}(P) - \text{rank}(Q), [I_P] - [I_Q])$$

验证这是群同构：
- **同态**：直接验证
- **单射**：若 $\phi([P] - [Q]) = (0, 0)$，则 $P$ 和 $Q$ 稳定等价
- **满射**：对任意 $(r, [I])$，取 $P = R^{r-1} \oplus I$

### $K_1$ 的 Whitehead 引理

**定理**：$K_1(R) \cong GL(R) / E(R)$

**证明**：

**步骤 1：初等矩阵**

初等矩阵 $E_{ij}(a)$ 为第 $(i,j)$ 位置为 $a$，对角线为 1，其余为 0 的矩阵。

**步骤 2：Whitehead 引理**

**引理**：对于 $A \in GL_n(R)$，$A \in E_n(R)$ 当且仅当 $A$ 可以表示为初等矩阵的乘积。

**证明**：使用行变换将 $A$ 化为单位矩阵。

**步骤 3：交换子计算**

**关键观察**：对于 $A \in GL_n(R)$ 和 $B \in GL_m(R)$，在 $GL_{n+m}(R)$ 中：
$$\begin{pmatrix} AB & 0 \\ 0 & I \end{pmatrix} \sim \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \begin{pmatrix} B & 0 \\ 0 & A \end{pmatrix}^{-1} \pmod{E}$$

这表明在 $K_1$ 中，直和对应于矩阵乘法。

**步骤 4：同构构造**

定义 $\phi: GL(R) \to K_1(R)$ 为自然投影。

由定义，$\ker(\phi) = [GL(R), GL(R)]$。

需要证明 $[GL(R), GL(R)] = E(R)$：
- $E(R) \subset [GL(R), GL(R)]$：初等矩阵是交换子
- $[GL(R), GL(R)] \subset E(R)$：商群 $GL(R)/E(R)$ 是交换的

### Quillen +构造的合理性

**步骤 1：+构造的定义**

对于空间 $X$ 和完美子群 $H \subset \pi_1(X)$，Quillen +构造产生空间 $X^+$，满足：
- $\pi_1(X^+) \cong \pi_1(X) / H$
- $H_*(X^+; \mathbb{Z}[H]) \cong H_*(X; \mathbb{Z}[H])$

**步骤 2：应用到 $BGL(R)$**

取 $X = BGL(R)$，$H = [GL(R), GL(R)]$（由 Whitehead 引理，这是完美的）。

则 $BGL(R)^+$ 满足：
- $\pi_1(BGL(R)^+) = GL(R) / [GL(R), GL(R)] = K_1(R)$
- $H_n(BGL(R)^+; \mathbb{Z}) \cong H_n(BGL(R); \mathbb{Z})$

**步骤 3：高阶同伦群**

定义 $K_n(R) = \pi_n(BGL(R)^+)$。

对于 $n = 1$，$K_1(R) = \pi_1(BGL(R)^+)$，与前述定义一致。

对于 $n = 2$，$K_2(R) = \pi_2(BGL(R)^+)$，可以证明与 Milnor 的 $K_2$ 定义一致。

## 五、应用与意义

### 1. 数论

代数 K 理论在数论中有深刻应用：

**例子**：对于数域 $F$ 的整数环 $\mathcal{O}_F$：
- $K_0(\mathcal{O}_F) \cong \mathbb{Z} \oplus \text{Cl}(\mathcal{O}_F)$
- $K_1(\mathcal{O}_F) \cong \mathcal{O}_F^* \oplus \text{（有限群）}$
- $K_2(\mathcal{O}_F)$ 与 Hilbert 符号和二次互反律相关

**Borel 定理**：对于数域 $F$，$K_n(\mathcal{O}_F) \otimes \mathbb{Q}$ 与 Dedekind zeta 函数 $\zeta_F(s)$ 在特殊点的值相关。

### 2. 代数几何

在代数几何中，代数 K 理论用于研究相干层和导出范畴：

**Grothendieck-Riemann-Roch 定理**：对于真态射 $f: X \to Y$ 和相干层 $\mathcal{F}$：
$$\text{ch}(f_! \mathcal{F}) \cdot \text{td}(T_Y) = f_*(\text{ch}(\mathcal{F}) \cdot \text{td}(T_X))$$

**Higher Riemann-Roch**：使用高阶 K 群和 Chern 特征标，可以推广到更一般的情形。

### 3. 拓扑

代数 K 理论与拓扑 K 理论的联系：

**Atiyah-Hirzebruch 谱序列**：对于空间 $X$，存在谱序列：
$$E_2^{p,q} = H^p(X; K_q(\mathbb{C})) \Rightarrow K^{p+q}(X)$$

**代数 K 理论的同伦论**：$K_n(\mathbb{C})$ 的计算涉及稳定同伦论。

### 4. 算子代数

在 C*-代数中，代数 K 理论与拓扑 K 理论的关系：

**C*-代数的 K 理论**：对于 C*-代数 $A$，定义 $K_0(A)$ 和 $K_1(A)$ 为投影和酉群的稳定等价类。

**周期性与 Bott 周期性**：$K_i(A) \cong K_{i+2}(A)$，这与拓扑 K 理论的 Bott 周期性一致。

### 5. 几何拓扑

在流形拓扑中，代数 K 理论用于研究 h-配边和伪同痕：

**Whitehead 群**：$Wh(\pi_1(M)) = K_1(\mathbb{Z}[\pi_1(M)]) / \{\pm g : g \in \pi_1(M)\}$

**s-配边定理**：单连通流形的 h-配边分类由 Whitehead 群控制。

### 6. 代数 K 理论的计算

**有限域的 K 群**：Quillen 计算了有限域 $\mathbb{F}_q$ 的 K 群：
$$K_n(\mathbb{F}_q) = \begin{cases} \mathbb{Z} & n = 0 \\ \mathbb{Z}/(q^k - 1) & n = 2k-1 \\ 0 & n = 2k > 0 \end{cases}$$

**整数环的 K 群**：
$$K_0(\mathbb{Z}) = \mathbb{Z}$$
$$K_1(\mathbb{Z}) = \mathbb{Z}/2$$
$$K_2(\mathbb{Z}) = \mathbb{Z}/2$$
$$K_3(\mathbb{Z}) = \mathbb{Z}/48$$

### 7.  motivic 上同调

Voevodsky 的 motivic 上同调理论与代数 K 理论密切相关：

**Bloch-Kato 猜想**（现为定理）：motivic 上同调与 Galois 上同调之间的关系，由 Rost 和 Voevodsky 证明。

**Milnor 猜想**：Milnor K 理论与 Galois 上同调的关系，由 Voevodsky 证明。

### 8. 非交换几何

在 Connes 的非交换几何中，代数 K 理论用于定义非交换空间的"上同调"：

**Chern-Connes 特征标**：从 K 理论到循环上同调的映射：
$$\text{ch}: K_n(A) \to HC_n(A)$$
其中 $HC_*$ 为循环上同调。

### 9. 物理学应用

在弦理论和凝聚态物理中，代数 K 理论用于分类 D-膜和拓扑相：

**拓扑绝缘体**：某些拓扑绝缘体的分类由 $K_0$ 或 $K_1$ 给出。

**弦理论中的 K 理论**：D-膜电荷由 K 理论群分类，代数 K 理论提供了更精细的不变量。
