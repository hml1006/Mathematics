# Leray-Schauder度理论

> **一句话大白话**：把"一个方程有几个解、解稳不稳"编码成一个整数（称为度），它连续变形不变，从而不用真解出来就能判断解一定存在。
>
> **小例子**：对方程 $x-T(x)=0$，若紧算子 $T$ 满足先验界 $|x-Tx|\in[0,1)$ 时可定义度 $\deg(I-T,\Omega,0)$；度非零即保证 $\Omega$ 内存在解。

## 一、定理介绍

> **前置依赖**：Brouwer 度及其同伦不变性、紧算子与有限维逼近（Schauder 投影）、先验估计方法、线性紧算子的谱理论。

Leray-Schauder 度理论由 Jean Leray 与 Juliusz Schauder 于 1934 年提出，是非线性泛函分析中研究非线性方程解的存在性、多解性与解的稳定性的核心工具。它将 Brouwer 度从有限维空间推广到无穷维 Banach 空间中的紧扰动恒等算子，即形如 $I - T$ 的算子（其中 $T$ 是紧算子）。

Leray-Schauder 度的精髓在于：它为方程 $F(x) = 0$ 解的"代数个数"赋予一个整数——拓扑度，使得度非零时方程必有解。度理论提供了非线性分析中最为系统的拓扑方法，被广泛应用于椭圆型偏微分方程、积分方程、微分方程边值问题的研究。

## 二、原理思路

Leray-Schauder 度理论的核心思想可归纳如下：

1. **度的本质**：拓扑度是一个整数值 $\operatorname{deg}(F, \Omega, p)$，反映方程 $F(x) = p$ 在区域 $\Omega$ 中解的"代数计数"，同伦下不变，在边界上为零时表明区域内无解。

2. **有限维到无穷维的过渡**：Brouwer 度定义在 $\mathbb{R}^n$ 上。Leray-Schauder 通过紧算子的有限维逼近——将紧算子 $T$ 用有限维算子 $T_n$ 逼近——使 $\operatorname{deg}(I - T_n, \cdot, \cdot)$ 收敛到一个稳定极限，定义为 $\operatorname{deg}(I - T, \cdot, \cdot)$。

3. **同伦不变性**：连续形变下度不变，是度理论最重要的性质，使得我们可以将复杂算子简化为已知度的简单算子（如恒等算子或线性算子）。

4. **存在性原理**：若 $\operatorname{deg}(F, \Omega, p) \neq 0$，则方程 $F(x) = p$ 在 $\Omega$ 内必有解。这是度理论应用的核心。

5. **Leray-Schauder 延拓定理**：通过"先验估计"——若所有解满足一致界——可利用同伦将未知问题与已知问题相连，从而推出解的存在性。

## 三、定理的严格表述

设 $X$ 是 Banach 空间，$\Omega \subset X$ 是有界开集，$T: \overline\Omega \to X$ 是紧算子（连续且将 $\overline\Omega$ 映为相对紧集），$f = I - T$，且 $p \notin f(\partial \Omega)$。

**Leray-Schauder 度的存在与唯一性**：存在唯一整数值函数
$$\operatorname{deg}(I - T, \Omega, p) \in \mathbb{Z},$$
满足以下公理：

1. **规范性**：$\operatorname{deg}(I, \Omega, p) = 1$ 若 $p \in \Omega$，$= 0$ 若 $p \notin \overline\Omega$。

2. **区域可加性**：若 $\Omega_1, \Omega_2 \subset \Omega$ 是不相交的开集，且 $p \notin f(\overline{\Omega \setminus (\Omega_1 \cup \Omega_2)})$，则
$$\operatorname{deg}(f, \Omega, p) = \operatorname{deg}(f, \Omega_1, p) + \operatorname{deg}(f, \Omega_2, p).$$

3. **同伦不变性**：设 $h: [0,1] \times \overline\Omega \to X$ 使得 $h_t(x) = h(t, x)$ 是紧算子族（关于 $t$ 一致连续紧），且 $p \notin (I - h_t)(\partial \Omega)$ 对所有 $t$ 成立，则 $\operatorname{deg}(I - h_t, \Omega, p)$ 与 $t$ 无关。

4. **边界依赖（连续依赖）**：度只依赖 $f$ 在 $\partial \Omega$ 上的值。

**存在性定理**：若 $\operatorname{deg}(f, \Omega, p) \neq 0$，则存在 $x \in \Omega$ 使 $f(x) = p$，即 $x - T(x) = p$。

**Leray-Schauder 延拓原理（先验界原理）**：设 $T: X \to X$ 紧。假设存在常数 $M > 0$，使得方程
$$x = \lambda T(x) \quad (\lambda \in [0,1])$$
的所有解满足 $\|x\| \leq M$。则 $T$ 在 $X$ 的闭球 $\overline{B_M}$ 中存在不动点。

## 四、证明过程

**步骤 1：有限维逼近构造度**

由于 $T(\overline\Omega)$ 相对紧，对任意 $n \geq 1$，存在有限 $\frac{1}{n}$-网 $\{y_1, \ldots, y_{N(n)}\} \subset T(\overline\Omega)$。设 $X_n = \operatorname{span}\{y_1, \ldots, y_{N(n)}\}$，定义 Schauder 投影 $P_n: X \to X_n$（同 Schauder 不动点定理证明中的构造），$\|P_n y - y\| \leq 1/n$ 对 $y \in T(\overline\Omega)$。

令 $T_n = P_n \circ T$，则 $T_n: \overline\Omega \cap X_n \to X_n$ 是有限维连续映射。设 $\Omega_n = \Omega \cap X_n$，当 $n$ 充分大时 $p \notin (I - T_n)(\partial \Omega_n)$（由 $p \notin (I-T)(\partial\Omega)$ 与紧性）。定义
$$\operatorname{deg}(I - T, \Omega, p) = \operatorname{deg}(I - T_n, \Omega_n, p),$$
其中右端为有限维 Brouwer 度。

**步骤 2：度的良定义性**

需证明上式右端对充分大 $n$ 与逼近的选取无关，且稳定。这通过同伦不变性证明：对两个不同的逼近 $T_n, T_m$，构造线性同伦
$$h_t = (1 - t) T_n + t T_m, \quad t \in [0,1].$$
需验证 $p \notin (I - h_t)(\partial \Omega_n)$ 对所有 $t$ 成立。利用 $T_n \to T$ 一致逼近与 $p \notin (I-T)(\partial\Omega)$，可保证这一点。由 Brouwer 度的同伦不变性，
$$\operatorname{deg}(I - T_n, \Omega_n, p) = \operatorname{deg}(I - T_m, \Omega_m, p).$$

**步骤 3：公理的验证**

规范性、可加性、同伦不变性、边界依赖均可由 Brouwer 度对应性质通过逼近取极限得到。具体而言：

- **规范性**：$T = 0$，$I - T = I$，有限维逼近平凡，由 Brouwer 度规范性可得。
- **可加性**：将 $\Omega_1, \Omega_2$ 与有限维逼近相交，应用 Brouwer 度可加性。
- **同伦不变性**：紧同伦 $h_t$ 通过有限维逼近 $h_{n,t} = P_n \circ h_t$ 逼近，Brouwer 度的同伦不变性给出 $\operatorname{deg}(I - h_{n,t}, \Omega_n, p)$ 与 $t$ 无关，取极限即得。

**步骤 4：唯一性**

满足上述公理的整数值函数唯一，可通过比较给定的两度函数，借助同伦不变性将一般算子简化为线性算子情形证明。

**步骤 5：存在性定理的证明**

若 $f(x) = p$ 在 $\Omega$ 中无解，则 $p \notin f(\overline\Omega)$，由可加性取 $\Omega_1 = \Omega$，$\Omega_2 = \emptyset$，$\operatorname{deg}(f, \Omega, p) = 0$，矛盾。

**步骤 6：Leray-Schauder 延拓原理的证明**

定义同伦 $h_t(x) = t T(x)$，$t \in [0,1]$，考察方程 $x - t T(x) = 0$。由先验估计，所有解满足 $\|x\| \leq M$，故 $0 \notin (I - h_t)(\partial B_M)$ 对所有 $t \in [0,1]$ 成立。

由同伦不变性，
$$\operatorname{deg}(I - T, B_M, 0) = \operatorname{deg}(I - h_1, B_M, 0) = \operatorname{deg}(I - h_0, B_M, 0) = \operatorname{deg}(I, B_M, 0) = 1 \neq 0.$$
由存在性定理，$T$ 在 $B_M$ 中存在不动点。$\square$

**步骤 7：线性算子的度（Leray-Schauder 公式）**

若 $T$ 是线性紧算子，$I - T$ 在 $0$ 处可逆（即 $1$ 不是 $T$ 的特征值），则
$$\operatorname{deg}(I - T, B_1, 0) = (-1)^\beta,$$
其中 $\beta$ 是 $T$ 在 $(1, \infty)$ 上的特征值代数重数之和（按重数计算）。这给出度的具体计算公式，是应用中的重要工具。

## 五、应用与意义

**理论意义**：

1. **拓扑方法的奠基**：Leray-Schauder 度是非线性泛函分析中最系统的拓扑工具，将方程解的存在性转化为度的计算。

2. **多解性研究**：度的变化反映了解的拓扑性质，可用于证明多解的存在（通过 Borsuk 定理、奇映射的度等）。

3. **不依赖变分结构**：相比变分方法，度理论不要求泛函结构，适用于非变分形式的非线性问题。

**应用领域**：

1. **椭圆方程 Dirichlet 问题**：
$$-\Delta u = f(x, u), \quad u|_{\partial \Omega} = 0,$$
将问题改写为 $u = K(f(\cdot, u(\cdot)))$（其中 $K$ 是逆 Laplace 算子的紧算子），通过 Leray-Schauder 延拓原理证明解的存在性。关键是建立解的先验估计。

2. **Neumann 边值问题与 Robin 问题**：类似方法适用于其他边值条件。

3. **积分方程**：Fredholm 与 Hammerstein 积分方程
$$u(x) = \int_\Omega K(x, y) f(y, u(y))\, dy$$
直接转化为紧算子不动点问题，应用 Leray-Schauder 理论。

4. **周期解与边值问题**：常微分方程周期解、二阶边值问题的存在性。

5. **分歧理论**：结合隐函数定理与度的同伦不变性，研究解的分歧现象（如 Crandall-Rabinowitz 分歧定理）。

6. **常微分方程共振问题**：处理非线性项在谱点附近时的解的存在性。

**重要变体与推广**：
- **Borsuk 定理（奇映射度）**：$\operatorname{deg}(f, \Omega, 0) = (-1)^{\dim}$ 的奇形式，给出奇映射的度为奇数。
- **对偶度（Nussbaum）**：用于非紧算子的扩展。
- **Conley 指标理论**：动力系统版本的度理论。
- **A-proper 映射的度**：更一般的逼近理论框架下的度。
