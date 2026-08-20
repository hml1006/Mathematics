# KMS 态与热力学形式

> **一句话大白话**：KMS 条件用"时间演化与配分函数之间的一条交换律"来严格定义什么叫温度稳定的热平衡态，是量子统计力学中"热平衡"的正规数学画像。
>
> **小例子**：经典 Gibbs 平衡态由 $\rho=\mathrm e^{-\beta H}/Z$（$Z$ 为配分函数，$\beta=1/(kT)$ 为逆温度）描述；KMS 态正是这套规律的算子代数版本。

## 一、定理介绍

KMS（Kubo-Martin-Schwinger）态是量子统计力学中描述热平衡态的数学概念，由 R. Kubo、P.C. Martin 和 J. Schwinger 在 1957 年至 1964 年间独立提出。KMS 条件为量子统计力学中的平衡态提供了严格的数学刻画，是算子代数方法在统计力学中应用的核心工具。

KMS 态的基本思想是：在热平衡态下，系统的关联函数满足特定的解析性和周期性条件。这一条件等价于经典统计力学中的 Gibbs 态条件，但适用于无穷多自由度的量子系统。KMS 理论与 Tomita-Takesaki 模理论密切相关，模自同构群自然地给出了系统的时间演化。

## 二、原理思路

KMS 态的理论基于以下关键概念：

1. **C*-动力学系统**：一个 C*-动力学系统是指三元组 $(A, \mathbb{R}, \alpha)$，其中 $A$ 是 C*-代数，$\alpha : \mathbb{R} \to \text{Aut}(A)$ 是强连续的单参数自同构群，描述系统的时间演化。

2. **KMS 条件**：给定逆温度 $\beta > 0$，态 $\omega$ 是 $(\beta, \alpha)$-KMS 态，如果对任意 $a, b \in A$，存在函数 $F_{a,b}(z)$，在带状区域 $0 \le \text{Im}(z) \le \beta$ 上解析，在边界上连续，且满足
$$F_{a,b}(t) = \omega(a\alpha_t(b)), \quad F_{a,b}(t + i\beta) = \omega(\alpha_t(b)a), \quad \forall t \in \mathbb{R}$$

3. **物理意义**：KMS 条件可以理解为量子版本的细致平衡条件。在有限温度下，系统的关联函数在虚时间方向上具有周期性，周期为 $\beta$（逆温度）。

4. **与 Gibbs 态的关系**：对有限系统（矩阵代数），KMS 态等价于 Gibbs 态 $\omega(a) = \text{tr}(e^{-\beta H}a) / \text{tr}(e^{-\beta H})$，其中 $H$ 是 Hamilton 量，$\alpha_t(a) = e^{itH}ae^{-itH}$。

## 三、定理的严格表述

**定义 1（C*-动力学系统）**：C*-动力学系统是指三元组 $(A, \mathbb{R}, \alpha)$，其中：
- $A$ 是 C*-代数
- $\alpha : \mathbb{R} \to \text{Aut}(A)$ 是单参数自同构群，即 $\alpha_{t+s} = \alpha_t \circ \alpha_s$，$\alpha_0 = \text{id}$
- 强连续性：对任意 $a \in A$，映射 $t \mapsto \alpha_t(a)$ 是连续的

**定义 2（KMS 态）**：设 $(A, \mathbb{R}, \alpha)$ 是 C*-动力学系统，$\beta > 0$ 是逆温度。态 $\omega$ 是 $(\beta, \alpha)$-KMS 态，如果对任意 $a, b \in A$，存在复值函数 $F_{a,b}(z)$，满足：
1. $F_{a,b}(z)$ 在带状区域 $D_\beta = \{z \in \mathbb{C} : 0 < \text{Im}(z) < \beta\}$ 上解析
2. $F_{a,b}(z)$ 在闭带状区域 $\overline{D_\beta} = \{z \in \mathbb{C} : 0 \le \text{Im}(z) \le \beta\}$ 上连续
3. 边界条件：
$$F_{a,b}(t) = \omega(a\alpha_t(b)), \quad \forall t \in \mathbb{R}$$
$$F_{a,b}(t + i\beta) = \omega(\alpha_t(b)a), \quad \forall t \in \mathbb{R}$$

**定理 1（KMS 态的等价刻画）**：设 $(A, \mathbb{R}, \alpha)$ 是 C*-动力学系统，$\omega$ 是 $A$ 上的态。以下等价：
1. $\omega$ 是 $(\beta, \alpha)$-KMS 态
2. 对任意 $a, b \in A$，$\omega(a\alpha_t(b))$ 的 Fourier 变换 $\hat{f}_{a,b}(\lambda)$ 满足
$$\hat{f}_{a,b}(-\lambda) = e^{-\beta\lambda}\hat{f}_{a,b}(\lambda), \quad \forall \lambda \in \mathbb{R}$$
3. 对任意 $a, b \in A$，存在函数 $G_{a,b}(t)$ 使得
$$\omega(a\alpha_t(b)) = \int_{-\infty}^\infty e^{i\lambda t}G_{a,b}(\lambda)d\lambda$$
且 $G_{a,b}(\lambda) \ge 0$，$G_{a,b}(-\lambda) = e^{-\beta\lambda}G_{a,b}(\lambda)$

**定理 2（有限系统的 KMS 态）**：设 $A = M_n(\mathbb{C})$ 是 $n \times n$ 矩阵代数，$H = H^* \in A$ 是 Hamilton 量，$\alpha_t(a) = e^{itH}ae^{-itH}$。则 $\omega$ 是 $(\beta, \alpha)$-KMS 态当且仅当
$$\omega(a) = \frac{\text{tr}(e^{-\beta H}a)}{\text{tr}(e^{-\beta H})}, \quad \forall a \in A$$
即 $\omega$ 是 Gibbs 态。

**定理 3（KMS 态的存在性与唯一性）**：设 $(A, \mathbb{R}, \alpha)$ 是 C*-动力学系统，则：
1. **存在性**：对任意 $\beta > 0$，存在 $(\beta, \alpha)$-KMS 态
2. **唯一性**：若 $A$ 是 UHF 代数（均匀超有限代数）且 $\alpha$ 满足某些条件，则 KMS 态唯一
3. **相变**：一般地，KMS 态不唯一，不同 KMS 态对应于系统的不同热力学相

**定理 4（KMS 态与模理论）**：设 $M$ 是 von Neumann 代数，$\omega$ 是 $M$ 上的忠实正规正规化态，$\{\sigma_t^\omega\}$ 是模自同构群。则 $\omega$ 是 $(1, \sigma^\omega)$-KMS 态，即
$$\omega(a\sigma_t^\omega(b)) = F_{a,b}(t), \quad \omega(\sigma_t^\omega(b)a) = F_{a,b}(t + i)$$
其中 $F_{a,b}(z)$ 在 $0 \le \text{Im}(z) \le 1$ 上解析。

**定理 5（Araki-Woods 定理）**：设 $(A, \mathbb{R}, \alpha)$ 是 C*-动力学系统，$\omega$ 是 $(\beta, \alpha)$-KMS 态。则 $\omega$ 的 GNS 表示 $(H_\omega, \pi_\omega, \xi_\omega)$ 具有以下性质：
1. 存在强连续的单参数酉群 $U(t)$，使得 $\pi_\omega(\alpha_t(a)) = U(t)\pi_\omega(a)U(t)^*$
2. $U(t)\xi_\omega = \xi_\omega$（$\xi_\omega$ 是 $U(t)$ 的不变向量）
3. 存在反酉算子 $J$，使得 $JU(t)J = U(-t)$，$J\pi_\omega(a)J \in \pi_\omega(A)'$
4. 模算子 $\Delta$ 满足 $\Delta^{it} = U(t/\beta)$

## 四、证明过程

**定理 2 的证明（有限系统的 KMS 态）**：

**步骤 1：Gibbs 态满足 KMS 条件**

设 $\omega(a) = \text{tr}(e^{-\beta H}a) / Z$，其中 $Z = \text{tr}(e^{-\beta H})$。

定义 $F_{a,b}(z) = \text{tr}(e^{-\beta H}a e^{izH}be^{-izH}) / Z$。

验证 $F_{a,b}(z)$ 的性质：
- 解析性：$e^{izH}$ 关于 $z$ 是整函数，故 $F_{a,b}(z)$ 是整函数
- 边界条件：
  $$F_{a,b}(t) = \text{tr}(e^{-\beta H}a e^{itH}be^{-itH}) / Z = \omega(a\alpha_t(b))$$
  $$F_{a,b}(t + i\beta) = \text{tr}(e^{-\beta H}a e^{i(t+i\beta)H}be^{-i(t+i\beta)H}) / Z$$
  $$= \text{tr}(e^{-\beta H}a e^{itH}e^{-\beta H}be^{-itH}e^{\beta H}) / Z$$
  $$= \text{tr}(e^{-\beta H}e^{itH}be^{-itH}a) / Z = \omega(\alpha_t(b)a)$$

这里使用了迹的循环性质 $\text{tr}(XY) = \text{tr}(YX)$。

**步骤 2：KMS 态必为 Gibbs 态**

设 $\omega$ 是 $(\beta, \alpha)$-KMS 态。定义密度矩阵 $\rho = e^{-\beta H} / Z$。

对任意矩阵元 $|i\rangle, |j\rangle$，设 $H|i\rangle = E_i|i\rangle$。

取 $a = |i\rangle\langle j|$，$b = |k\rangle\langle l|$，则 $\alpha_t(a) = e^{it(E_i - E_j)}|i\rangle\langle j|$。

KMS 条件给出：
$$\omega(a\alpha_t(b)) = e^{it(E_k - E_l)}\omega(|i\rangle\langle j|k\rangle\langle l|) = e^{it(E_k - E_l)}\delta_{jk}\omega_{il}$$
$$\omega(\alpha_t(b)a) = e^{it(E_k - E_l)}\omega(|k\rangle\langle l|i\rangle\langle j|) = e^{it(E_k - E_l)}\delta_{li}\omega_{kj}$$

KMS 边界条件 $F_{a,b}(t + i\beta) = \omega(\alpha_t(b)a)$ 给出：
$$e^{-\beta(E_k - E_l)}\delta_{jk}\omega_{il} = \delta_{li}\omega_{kj}$$

取 $j = k$，$l = i$：$e^{-\beta(E_i - E_j)}\omega_{ij} = \omega_{ji}$。

这说明 $\omega_{ij} = c_i\delta_{ij}$，即 $\omega$ 是对角矩阵。

进一步，$e^{-\beta(E_i - E_j)}\omega_{ii} = \omega_{jj}$，故 $\omega_{ii} = Ce^{-\beta E_i}$。

由归一化 $\sum_i \omega_{ii} = 1$，$C = 1/Z$。

因此 $\omega(a) = \text{tr}(e^{-\beta H}a) / Z$。$\square$

**定理 4 的证明（KMS 态与模理论）**：

**步骤 1：模自同构群的定义**

设 $M$ 是 von Neumann 代数，$\omega$ 是忠实正规正规化态。由 Tomita-Takesaki 理论，存在模算子 $\Delta$ 和模共轭 $J$，模自同构群 $\sigma_t^\omega(x) = \Delta^{it}x\Delta^{-it}$。

**步骤 2：构造解析函数**

对 $a, b \in M$，定义 $F_{a,b}(z) = \langle \xi_\omega, a\Delta^{iz}b\xi_\omega \rangle$，其中 $\xi_\omega$ 是 GNS 循环向量。

由于 $\Delta^{iz}$ 在 $0 \le \text{Im}(z) \le 1$ 上有定义且解析，$F_{a,b}(z)$ 在该区域上解析。

**步骤 3：验证边界条件**

在实轴上（$z = t$）：
$$F_{a,b}(t) = \langle \xi_\omega, a\Delta^{it}b\xi_\omega \rangle = \langle \xi_\omega, a\sigma_t^\omega(b)\xi_\omega \rangle = \omega(a\sigma_t^\omega(b))$$

在直线 $\text{Im}(z) = 1$ 上（$z = t + i$）：
$$F_{a,b}(t + i) = \langle \xi_\omega, a\Delta^{i(t+i)}b\xi_\omega \rangle = \langle \xi_\omega, a\Delta^{it}\Delta^{-1}b\xi_\omega \rangle$$

由 Tomita 算子的性质，$S = J\Delta^{1/2}$，$S\xi_\omega = \xi_\omega$（因为 $S(1\xi_\omega) = 1^*\xi_\omega = \xi_\omega$）。

故 $\Delta^{-1/2}\xi_\omega = J\xi_\omega = \xi_\omega$，$\Delta^{-1}\xi_\omega = \xi_\omega$。

利用 $Jb^*J \in M'$ 和 $J\Delta^{it}J = \Delta^{-it}$，经过计算可得：
$$F_{a,b}(t + i) = \langle \xi_\omega, \sigma_t^\omega(b)a\xi_\omega \rangle = \omega(\sigma_t^\omega(b)a)$$

因此 $\omega$ 满足 $(1, \sigma^\omega)$-KMS 条件。$\square$

## 五、应用与意义

KMS 态理论在数学和物理学中有广泛应用：

1. **量子统计力学**：KMS 态为无穷多自由度量子系统的热平衡态提供了严格数学定义。不同 KMS 态对应于系统的不同热力学相，相变对应于 KMS 态的非唯一性。

2. **相变理论**：通过研究 KMS 态随温度 $\beta$ 的变化，可以严格定义和分析相变现象。例如，Ising 模型的量子版本在临界温度以下有多个 KMS 态。

3. **算子代数分类**：KMS 态的存在性和唯一性与 von Neumann 代数的类型密切相关。III 型因子的模自同构群非平凡，反映了系统的热力学性质。

4. **非交换几何**：Connes 的非交换几何中，KMS 态用于定义"非交换空间"上的测度和积分。

5. **量子场论**：在代数量子场论中，KMS 态描述了热场论中的平衡态。Unruh 效应和 Hawking 辐射可以用 KMS 条件来理解。

6. **遍历理论**：KMS 态与遍历理论中的平衡态测度密切相关，为研究动力系统的统计性质提供了工具。

7. **量子信息**：KMS 态在量子信息理论中用于研究热态的纠缠性质和量子信道。

8. **数学物理**：KMS 理论为数学物理中的平衡态统计力学提供了严格的公理化基础，连接了微观动力学和宏观热力学。

KMS 态理论展示了算子代数方法在统计力学中的强大威力，是数学物理中最重要的成果之一。它不仅为热力学提供了严格的数学基础，而且揭示了量子系统深层的代数结构。
