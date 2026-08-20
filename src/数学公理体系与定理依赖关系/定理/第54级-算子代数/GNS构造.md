# Gelfand-Naimark-Segal (GNS) 构造

> **一句话大白话**：给定一个"取平均/期望"的法则（状态），就能凭空造出一个希尔伯特空间，把每个代数元素变成实实在在的算子——状态先生成空间，抽象代数由此落地。
>
> **小例子**：对矩阵代数 $M_n(\mathbb{C})$ 取"规范化迹"态 $\omega(T)=\tfrac1n\operatorname{tr}T$，GNS 表示自然落在 $\mathbb{C}^n$ 上，且 $\omega$ 由单位向量 $\frac1{\sqrt n}(1,\ldots,1)$ 实现。

## 一、定理介绍

Gelfand-Naimark-Segal (GNS) 构造是 C*-代数表示理论中最基本和最重要的工具之一。它表明：给定 C*-代数上的任意状态（正线性泛函），都可以构造出一个 Hilbert 空间表示，使得该状态由 Hilbert 空间中的某个向量实现。

GNS 构造的核心意义在于：它将抽象的 C*-代数元素具体实现为 Hilbert 空间上的有界线性算子，从而可以运用 Hilbert 空间理论的强大工具来研究 C*-代数。这一构造在量子统计力学、算子代数分类、以及非交换几何等领域有广泛应用。

## 二、原理思路

GNS 构造的基本思想类似于从内积构造 Hilbert 空间的过程：

1. **从状态出发**：给定 C*-代数 $A$ 上的状态 $\omega$（即满足 $\omega(a^*a) \ge 0$ 且 $\|\omega\| = 1$ 的正线性泛函）。

2. **构造半内积**：利用 $\omega$ 在 $A$ 上定义半内积 $\langle a, b \rangle_\omega = \omega(b^*a)$。

3. **商空间**：令 $N_\omega = \{a \in A : \omega(a^*a) = 0\}$，这是左理想。商空间 $A/N_\omega$ 上定义了真正的内积。

4. **完备化**：将 $A/N_\omega$ 关于内积完备化，得到 Hilbert 空间 $H_\omega$。

5. **表示**：$A$ 通过左乘法作用在 $H_\omega$ 上，即 $\pi_\omega(a)[b] = [ab]$。

6. **循环向量**：存在循环向量 $\xi_\omega = [1]$（若 $A$ 有单位元），使得 $\omega(a) = \langle \xi_\omega, \pi_\omega(a)\xi_\omega \rangle$。

关键要点是：GNS 构造将抽象的状态与具体的 Hilbert 空间表示联系起来，且循环向量的存在保证了表示的不可约性条件。

## 三、定理的严格表述

**定义 1（状态）**：设 $A$ 是 C*-代数，$A$ 上的状态是指满足以下条件的线性泛函 $\omega : A \to \mathbb{C}$：
1. **正性**：$\omega(a^*a) \ge 0$，对所有 $a \in A$
2. **归一化**：$\|\omega\| = 1$（若 $A$ 有单位元 $1$，则 $\omega(1) = 1$）

$A$ 上所有状态组成的集合记为 $S(A)$，称为 $A$ 的状态空间。

**定义 2（GNS 三元组）**：设 $A$ 是 C*-代数，$\omega$ 是 $A$ 上的状态。GNS 三元组是指三元组 $(H_\omega, \pi_\omega, \xi_\omega)$，其中：
- $H_\omega$ 是 Hilbert 空间
- $\pi_\omega : A \to B(H_\omega)$ 是 *-表示（即保持代数运算和对合的 *-同态）
- $\xi_\omega \in H_\omega$ 是循环向量，即 $\overline{\pi_\omega(A)\xi_\omega} = H_\omega$
- 满足 $\omega(a) = \langle \xi_\omega, \pi_\omega(a)\xi_\omega \rangle$，对所有 $a \in A$

**定理 1（GNS 构造定理）**：设 $A$ 是 C*-代数，$\omega$ 是 $A$ 上的状态。则存在 GNS 三元组 $(H_\omega, \pi_\omega, \xi_\omega)$，且在以下意义下唯一：

若 $(H', \pi', \xi')$ 是另一个满足上述条件的三元组，则存在唯一的酉算子 $U : H_\omega \to H'$，使得
$$U\pi_\omega(a) = \pi'(a)U, \quad \forall a \in A$$
$$U\xi_\omega = \xi'$$

**定理 2（表示的分解）**：设 $\pi : A \to B(H)$ 是 C*-代数 $A$ 的非退化 *-表示，$\xi \in H$ 是循环向量。定义状态 $\omega(a) = \langle \xi, \pi(a)\xi \rangle$，则 $(H, \pi, \xi)$ 酉等价于 $(H_\omega, \pi_\omega, \xi_\omega)$。

**定理 3（纯态与不可约表示）**：设 $\omega$ 是 C*-代数 $A$ 上的状态，则以下等价：
1. $\omega$ 是纯态（即 $S(A)$ 的极点）
2. $\pi_\omega$ 是不可约表示（即 $\pi_\omega(A)' = \mathbb{C}I$）

## 四、证明过程

**定理 1 的证明**：

**步骤 1：构造左理想 $N_\omega$**

定义 $N_\omega = \{a \in A : \omega(a^*a) = 0\}$。

首先证明 $N_\omega$ 是左理想：
- 若 $a \in N_\omega$，$b \in A$，由 Cauchy-Schwarz 不等式（对正泛函成立）：
$$|\omega(b^*a)|^2 \le \omega(b^*b)\omega(a^*a) = 0$$
故 $\omega(a^*b) = 0$。
- 考虑 $\omega((ba)^*(ba)) = \omega(a^*b^*ba)$。由于 $b^*b \le \|b\|^2 I$（若 $A$ 有单位元），
$$\omega(a^*b^*ba) \le \|b\|^2 \omega(a^*a) = 0$$
故 $ba \in N_\omega$。

因此 $N_\omega$ 是左理想。

**步骤 2：定义半内积与商空间**

在 $A$ 上定义半内积：
$$\langle a, b \rangle_\omega = \omega(b^*a)$$

验证半内积性质：
- 共轭对称性：$\langle b, a \rangle_\omega = \omega(a^*b) = \overline{\omega(b^*a)} = \overline{\langle a, b \rangle_\omega}$
- 线性：$\langle \lambda a + b, c \rangle_\omega = \omega(c^*(\lambda a + b)) = \lambda\omega(c^*a) + \omega(c^*b) = \lambda\langle a, c \rangle_\omega + \langle b, c \rangle_\omega$
- 半正定性：$\langle a, a \rangle_\omega = \omega(a^*a) \ge 0$

由于 $N_\omega = \{a : \langle a, a \rangle_\omega = 0\}$，商空间 $A/N_\omega$ 上定义了真正的内积。

记 $[a]$ 为 $a$ 在 $A/N_\omega$ 中的等价类，则 $\langle [a], [b] \rangle_\omega = \omega(b^*a)$ 定义良好。

**步骤 3：完备化得到 Hilbert 空间**

$A/N_\omega$ 关于内积 $\langle \cdot, \cdot \rangle_\omega$ 是内积空间，但不一定完备。令 $H_\omega$ 为 $A/N_\omega$ 的完备化，即 $H_\omega = \overline{A/N_\omega}$。

**步骤 4：构造表示 $\pi_\omega$**

对 $a \in A$，定义左乘法算子 $L_a : A/N_\omega \to A/N_\omega$ 为 $L_a[b] = [ab]$。

首先验证 $L_a$ 定义良好：若 $[b] = [c]$，则 $b - c \in N_\omega$，即 $\omega((b-c)^*(b-c)) = 0$。
$$\omega((ab-ac)^*(ab-ac)) = \omega((b-c)^*a^*a(b-c)) \le \|a^*a\|\omega((b-c)^*(b-c)) = 0$$
故 $[ab] = [ac]$，$L_a$ 定义良好。

$L_a$ 是有界的：$\|L_a[b]\|^2 = \omega((ab)^*(ab)) = \omega(b^*a^*ab) \le \|a^*a\|\omega(b^*b) = \|a\|^2\|[b]\|^2$。
故 $\|L_a\| \le \|a\|$。

定义 $\pi_\omega(a) = L_a$，则 $\pi_\omega$ 是 *-表示：
- $\pi_\omega(ab)[c] = [abc] = L_a L_b [c] = \pi_\omega(a)\pi_\omega(b)[c]$
- $\langle \pi_\omega(a)[b], [c] \rangle = \omega(c^*ab) = \langle [b], \pi_\omega(a^*)[c] \rangle$，故 $\pi_\omega(a^*) = \pi_\omega(a)^*$

**步骤 5：循环向量**

若 $A$ 有单位元 $1$，令 $\xi_\omega = [1]$。则对任意 $[a] \in A/N_\omega$，$\pi_\omega(a)\xi_\omega = [a \cdot 1] = [a]$。
故 $\pi_\omega(A)\xi_\omega = A/N_\omega$，在 $H_\omega$ 中稠密，$\xi_\omega$ 是循环向量。

验证状态实现：$\langle \xi_\omega, \pi_\omega(a)\xi_\omega \rangle = \langle [1], [a] \rangle = \omega(1^*a) = \omega(a)$。

**步骤 6：唯一性**

设 $(H', \pi', \xi')$ 是另一个 GNS 三元组。定义映射 $U_0 : \pi_\omega(A)\xi_\omega \to H'$ 为
$$U_0(\pi_\omega(a)\xi_\omega) = \pi'(a)\xi'$$

验证 $U_0$ 是等距的：
$$\|U_0(\pi_\omega(a)\xi_\omega)\|^2 = \|\pi'(a)\xi'\|^2 = \langle \xi', \pi'(a^*a)\xi' \rangle = \omega(a^*a)$$
$$= \langle \xi_\omega, \pi_\omega(a^*a)\xi_\omega \rangle = \|\pi_\omega(a)\xi_\omega\|^2$$

故 $U_0$ 是等距映射，可以唯一地延拓为 $H_\omega$ 到 $\overline{\pi'(A)\xi'} = H'$ 的酉算子 $U$。

由构造，$U\pi_\omega(a)\xi_\omega = \pi'(a)\xi'$，且 $U\xi_\omega = \xi'$。

对任意 $b \in A$，$U\pi_\omega(a)\pi_\omega(b)\xi_\omega = U\pi_\omega(ab)\xi_\omega = \pi'(ab)\xi' = \pi'(a)\pi'(b)\xi' = \pi'(a)U\pi_\omega(b)\xi_\omega$。

由于 $\pi_\omega(A)\xi_\omega$ 在 $H_\omega$ 中稠密，$U\pi_\omega(a) = \pi'(a)U$。$\square$

## 五、应用与意义

GNS 构造在算子代数和相关领域有广泛应用：

1. **C*-代数的忠实表示**：对 C*-代数 $A$ 上所有状态的 GNS 表示的直和 $\bigoplus_{\omega \in S(A)} \pi_\omega$ 是忠实表示，这证明了 Gelfand-Naimark 定理（一般情形）的关键步骤。

2. **von Neumann 代数的构造**：给定 von Neumann 代数上的正规状态，GNS 构造产生标准形式，这是 Tomita-Takesaki 模理论的基础。

3. **量子统计力学**：在量子统计力学中，KMS 态（描述热平衡态）的 GNS 构造产生了模自同构群，描述了系统的时间演化。

4. **纯态与不可约表示**：GNS 构造建立了纯态与不可约表示之间的一一对应，这是 C*-代数表示理论的核心结果。

5. **因子的分类**：通过研究 GNS 表示中交换子的结构，可以对 von Neumann 代数进行分类（I 型、II 型、III 型）。

6. **量子场论**：在代数量子场论中，不同真空态的 GNS 表示给出了不同的超选择扇区，描述了物理系统的不同相位。

7. **非交换概率论**：GNS 构造是非交换概率论中从"分布"构造"随机变量"的基本工具，类似于经典概率论中从分布函数构造随机变量的过程。

GNS 构造是连接抽象代数结构与具体算子实现的桥梁，是现代算子代数理论不可或缺的工具。
