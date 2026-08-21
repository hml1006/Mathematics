# Gelfand-Naimark 定理（一般情形）

> **一句话大白话**：任何抽象的 C*-代数，都长得和"某个希尔伯特空间上真正算子的子代数"一模一样——抽象公理一定能落成具体算子，绝不是纸上谈兵。
>
> **小例子**：抽象的有限维 C*-代数 $\mathbb{C}^n$（按坐标相乘）能看成对角阵代数，即 $B(\mathbb{C}^n)$ 的交换闭子代数；这就是等距 *-同构的一个实例。

## 一、定理介绍

> **前置依赖**：GNS 构造、交换 C*-代数的 Gelfand-Naimark 定理、Hahn-Banach 定理（状态的延拓）、谱半径公式与谱映射定理、Hilbert 空间直和与有界算子代数

Gelfand-Naimark 定理（一般情形）是 C*-代数理论的巅峰成果之一，它表明：任何 C*-代数都等距 *-同构于某个 Hilbert 空间上有界线性算子代数的闭 *-子代数。这个定理最早由 Gelfand 和 Naimark 在 1943 年证明，标志着算子代数作为一个独立数学分支的诞生。

该定理的深刻意义在于：它将抽象的 C*-代数（纯代数和分析的定义）与具体的算子代数（Hilbert 空间上的算子）完全等价起来。这意味着研究抽象 C*-代数与研究 Hilbert 空间上的算子代数是同一件事，为算子代数理论提供了坚实的基础。

## 二、原理思路

Gelfand-Naimark 定理（一般情形）的证明策略是：

1. **利用 GNS 构造**：对 C*-代数 $A$ 上的每个状态 $\omega$，GNS 构造给出一个表示 $\pi_\omega : A \to B(H_\omega)$。

2. **直和表示**：将所有状态的 GNS 表示取直和，得到 universal 表示 $\pi_u = \bigoplus_{\omega \in S(A)} \pi_\omega : A \to B(H_u)$，其中 $H_u = \bigoplus_{\omega \in S(A)} H_\omega$。

3. **证明忠实性**：关键步骤是证明 universal 表示是忠实的（即单射），这等价于证明：对任意非零元素 $a \in A$，存在状态 $\omega$ 使得 $\omega(a^*a) > 0$。

4. **等距性**：由 C*-代数的基本性质，忠实 *-同态自动是等距的。

5. **闭像**：忠实 *-同态的像是闭的，因此 $A$ 等距 *-同构于 $B(H_u)$ 的闭 *-子代数。

证明的核心在于状态空间足够"丰富"，能够分离 C*-代数中的元素。这体现了 C*-代数中代数结构与分析结构的完美和谐。

## 三、定理的严格表述

**定理 1（Gelfand-Naimark 定理，一般情形）**：设 $A$ 是 C*-代数，则存在 Hilbert 空间 $H$ 和等距 *-同态 $\pi : A \to B(H)$，使得 $\pi(A)$ 是 $B(H)$ 的闭 *-子代数。

换言之，任何 C*-代数都等距 *-同构于某个 Hilbert 空间上有界线性算子代数的闭 *-子代数。

**定理 2（universal 表示）**：设 $A$ 是 C*-代数，$S(A)$ 是 $A$ 的状态空间。定义 universal 表示为
$$\pi_u = \bigoplus_{\omega \in S(A)} \pi_\omega : A \to B\left(\bigoplus_{\omega \in S(A)} H_\omega\right)$$
其中 $(\pi_\omega, H_\omega)$ 是状态 $\omega$ 的 GNS 表示。则 $\pi_u$ 是忠实表示。

**定理 3（C*-代数的抽象刻画）**：Banach 代数 $A$ 具有对合运算 $*$，以下等价：
1. $A$ 是 C*-代数（即满足 C*-恒等式 $\|a^*a\| = \|a\|^2$）
2. $A$ 等距 *-同构于某个 Hilbert 空间上有界线性算子代数的闭 *-子代数

**推论 1**：设 $A$ 是 C*-代数，$a \in A$，则
$$\|a\| = \sup\{\|\pi(a)\| : \pi \text{ 是 } A \text{ 的非退化 *-表示}\}$$

**推论 2**：C*-代数上的 *-同态 $\phi : A \to B$ 自动连续，且 $\|\phi\| \le 1$。

## 四、证明过程

**定理 1 的证明**：

**步骤 1：状态分离正元素**

首先证明关键引理：对任意非零正元素 $a \in A$（即 $a = b^*b$ 对某个 $b$），存在状态 $\omega$ 使得 $\omega(a) > 0$。

设 $a \ge 0$ 且 $a \neq 0$。考虑由 $a$ 生成的交换 C*-子代数 $C^*(a)$。

由交换情形的 Gelfand-Naimark 定理，$C^*(a) \cong C_0(\hat{a})$，其中 $\hat{a}$ 是 $C^*(a)$ 的 Gelfand 谱。

在 $C_0(\hat{a})$ 中，$a$ 对应于某个非负非零函数 $\hat{a}$。存在 $\chi \in \hat{a}$ 使得 $\hat{a}(\chi) > 0$。

特征标 $\chi$ 是 $C^*(a)$ 上的状态，且 $\chi(a) > 0$。

由 Hahn-Banach 定理，$\chi$ 可以延拓为 $A$ 上的状态 $\omega$，且 $\omega(a) = \chi(a) > 0$。

**步骤 2：universal 表示的忠实性**

定义 universal 表示 $\pi_u = \bigoplus_{\omega \in S(A)} \pi_\omega$，作用在 $H_u = \bigoplus_{\omega \in S(A)} H_\omega$ 上。

要证 $\pi_u$ 是忠实的，即 $\ker\pi_u = \{0\}$。

设 $a \in \ker\pi_u$，则对所有 $\omega \in S(A)$，$\pi_\omega(a) = 0$。

特别地，$\pi_\omega(a)\xi_\omega = 0$，故 $\|\pi_\omega(a)\xi_\omega\|^2 = 0$。

但 $\|\pi_\omega(a)\xi_\omega\|^2 = \langle \xi_\omega, \pi_\omega(a^*a)\xi_\omega \rangle = \omega(a^*a)$。

因此对所有 $\omega \in S(A)$，$\omega(a^*a) = 0$。

由步骤 1 的引理，$a^*a = 0$，故 $a = 0$。

因此 $\pi_u$ 是忠实的。

**步骤 3：等距性**

设 $\pi : A \to B(H)$ 是忠实 *-同态。要证 $\pi$ 是等距的。

对任意 $a \in A$，$\|\pi(a)\|^2 = \|\pi(a)^*\pi(a)\| = \|\pi(a^*a)\|$。

由于 $\pi$ 是 *-同态，$\pi(a^*a)$ 是正算子，其谱半径等于范数。

由谱映射定理，$\sigma(\pi(a^*a)) \subset \sigma(a^*a) \cup \{0\}$。

由于 $\pi$ 忠实，可以证明 $\sigma(\pi(a^*a)) = \sigma(a^*a)$（C*-子代数的谱不变性）。

因此 $\|\pi(a^*a)\| = r(\pi(a^*a)) = r(a^*a) = \|a^*a\| = \|a\|^2$。

故 $\|\pi(a)\| = \|a\|$，$\pi$ 是等距的。

**步骤 4：闭像**

由于 $\pi_u$ 是等距的，$\pi_u(A)$ 是 $B(H_u)$ 的闭子集（等距映射将 Cauchy 列映为 Cauchy 列，完备空间的闭子集是完备的）。

$\pi_u(A)$ 是 *-子代数：$\pi_u(ab) = \pi_u(a)\pi_u(b)$，$\pi_u(a^*) = \pi_u(a)^*$。

因此 $\pi_u(A)$ 是 $B(H_u)$ 的闭 *-子代数，即 C*-子代数。

故 $A \cong \pi_u(A)$ 是 $B(H_u)$ 的 C*-子代数。$\square$

**推论 2 的证明**：

设 $\phi : A \to B$ 是 C*-代数 *-同态。

对任意 $a \in A$，$a^*a$ 是正元素，故 $\sigma(a^*a) \subset [0, \infty)$。

$\phi(a^*a) = \phi(a)^*\phi(a)$ 也是正元素，$\sigma(\phi(a^*a)) \subset [0, \infty)$。

由谱映射定理，$\sigma(\phi(a^*a)) \subset \sigma(a^*a) \cup \{0\}$。

故 $r(\phi(a^*a)) \le r(a^*a)$，即 $\|\phi(a^*a)\| \le \|a^*a\|$。

因此 $\|\phi(a)\|^2 = \|\phi(a)^*\phi(a)\| = \|\phi(a^*a)\| \le \|a^*a\| = \|a\|^2$。

故 $\|\phi(a)\| \le \|a\|$，$\|\phi\| \le 1$。$\square$

## 五、应用与意义

Gelfand-Naimark 定理（一般情形）在数学和物理学中有深远影响：

1. **算子代数的公理化**：定理表明 C*-代数的抽象定义与算子代数的具体定义完全等价。这为算子代数理论提供了严格的公理化基础，使得数学家可以在抽象框架下工作，而不必依赖具体的 Hilbert 空间实现。

2. **表示理论的起点**：定理表明研究 C*-代数等价于研究其在 Hilbert 空间上的表示。这催生了丰富的表示理论，包括不可约表示、因子表示、类型分类等。

3. **von Neumann 代数的基础**：von Neumann 代数是 $B(H)$ 的弱闭 *-子代数，是 C*-代数的特殊情况。Gelfand-Naimark 定理为 von Neumann 代数理论奠定了基础。

4. **量子力学的数学基础**：在量子力学中，可观测量形成 C*-代数，态是 C*-代数上的正线性泛函。Gelfand-Naimark 定理保证了任何量子系统都可以在 Hilbert 空间框架下描述。

5. **K-理论**：C*-代数的投影算子（满足 $p = p^* = p^2$ 的元素）的等价类定义了 K-群，这是拓扑 K-理论的核心。Gelfand-Naimark 定理保证了 K-理论的几何意义。

6. **指标定理**：Atiyah-Singer 指标定理的 C*-代数证明依赖于算子代数的表示理论，Gelfand-Naimark 定理是基础工具。

7. **非交换几何**：Connes 的非交换几何将 C*-代数视为"非交换空间"的函数代数。Gelfand-Naimark 定理为这一观点提供了严格基础：交换 C*-代数对应经典空间，非交换 C*-代数对应量子空间。

8. **分类问题**：C*-代数的分类（特别是单纯核 C*-代数）是当代研究的核心问题。Gelfand-Naimark 定理为分类提供了框架：分类 C*-代数等价于分类 Hilbert 空间上的算子代数。

Gelfand-Naimark 定理是 20 世纪数学的重大成就之一，它展示了代数、分析、拓扑和几何的深刻统一，继续推动着现代数学和理论物理的发展。
