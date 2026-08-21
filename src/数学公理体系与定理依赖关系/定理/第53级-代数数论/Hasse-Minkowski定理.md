# 局部整体原理（Hasse-Minkowski 定理）

> **一句话大白话**：一个方程在"所有局部地盘"（实数处和每个 $p$-进处）都有解，就等于在整个数域有解——局部的零散信号拼在一起就是全局真相，把难题拆成一堆小检查。
>
> **小例子**：判断二次型 $ax^2+by^2+cz^2=0$ 有无非平凡解，只需在 $\mathbb{R}$ 和所有 $\mathbb{Q}_p$ 上一一检查；任一局部无解则全局无解，处处有解则全局必能解。

## 一、定理介绍

> **前置依赖**：$p$-进数域 $\mathbb{Q}_p$ 与 Hensel 引理、Hilbert 符号与 Hilbert 互反律、二次型的对角化与判别式、四元数代数与 Brauer 群、Chevalley-Warning 定理

Hasse-Minkowski 定理是代数数论中**局部整体原理**（Local-Global Principle）或称 **Hasse 原理**的最重要实例。该定理由 Hasse 于 1920 年代对二次型证明，Minkowski  earlier 的工作为其奠定了基础。

定理的核心思想极为优美：一个有理系数二次型是否有非平凡有理零点，可以完全由它在所有**局部域**（实数域 $\mathbb{R}$ 和所有 $p$-进数域 $\mathbb{Q}_p$）上是否有非平凡零点来判定。换言之，整体问题可以分解为局部问题的集合。

这一原理的哲学是："全局"的数学对象（如有理数上的二次型）的性质，可以由它在所有"局部"完备化（如 $\mathbb{R}$ 和 $\mathbb{Q}_p$）上的性质完全确定。虽然 Hasse 原理对二次型成立，但对更高次的齐次方程一般不成立（反例由 Selmer 和 others 给出），因此理解 Hasse 原理何时成立、何时失败是现代数论的核心课题。

## 二、原理思路

### 从整体到局部

设 $f(x_1, \ldots, x_n)$ 是有理系数二次型。我们关心 $f = 0$ 是否有非平凡的有理数解（即 $(x_1, \ldots, x_n) \in \mathbb{Q}^n \setminus \{0\}$）。

显然，如果 $f = 0$ 有有理数解，则它对每个素数 $p$ 在 $\mathbb{Q}_p$ 中有解（$p$-进解），且在 $\mathbb{R}$ 中有解（实解）。这些是**必要条件**。

Hasse-Minkowski 定理断言这同时也是**充分条件**：如果在所有局部域上都有非平凡解，则在 $\mathbb{Q}$ 上也有非平凡解。

### 二次型的分类

证明的核心是对二次型进行** Witt 分解**和** Hasse 不变量**的计算。

每个有理数域上的二次型都可以对角化为 $f \cong \langle a_1, a_2, \ldots, a_n \rangle$，即 $f(x) = a_1 x_1^2 + a_2 x_2^2 + \cdots + a_n x_n^2$。

对每个局部域 $F$（$\mathbb{R}$ 或 $\mathbb{Q}_p$），二次型有完整的不变量系统：
- **维数** $n$
- **判别式** $d(f) = \prod a_i \in F^\times / (F^\times)^2$
- **Hasse-Witt 不变量** $\epsilon_p(f) = \prod_{i < j} (a_i, a_j)_p \in \{\pm 1\}$

其中 $(a, b)_p$ 是 **Hilbert 符号**。

两个局部二次型等价当且仅当它们有相同的维数、判别式和 Hasse 不变量。

### 关键工具：Hilbert 互反律

Hilbert 符号满足**乘积公式**（Hilbert 互反律）：对任意 $a, b \in \mathbb{Q}^\times$，
$$\prod_v (a, b)_v = 1,$$
其中积取遍 $\mathbb{Q}$ 的所有位置（places）$v$（包括 $\infty$ 对应 $\mathbb{R}$，和所有素数 $p$ 对应 $\mathbb{Q}_p$）。

这一互反律是证明 Hasse-Minkowski 定理的关键——它保证了局部不变量之间的相容性，从而使得局部-整体的对应成为可能。

## 三、定理的严格表述

**定理（Hasse-Minkowski）：**

设 $f(x_1, \ldots, x_n)$ 是 $\mathbb{Q}$ 上的二次型。则以下等价：

**(1)** $f$ 在 $\mathbb{Q}$ 上表示零，即存在 $(x_1, \ldots, x_n) \in \mathbb{Q}^n \setminus \{0\}$ 使得 $f(x_1, \ldots, x_n) = 0$。

**(2)** $f$ 在 $\mathbb{R}$ 上表示零，且对每个素数 $p$，$f$ 在 $\mathbb{Q}_p$ 上表示零。

等价地，用二次型的等价语言：

**定理（二次型的局部整体等价）：**

两个 $\mathbb{Q}$ 上的二次型 $f$ 和 $g$ 在 $\mathbb{Q}$ 上等价，当且仅当它们在所有局部域（$\mathbb{R}$ 和所有 $\mathbb{Q}_p$）上等价。

**推论（二元二次型）：** 二元二次型 $ax^2 + by^2 = c$（$a, b, c \in \mathbb{Q}^\times$）有有理数解当且仅当：
- 在 $\mathbb{R}$ 上有解（即不是 $a, b$ 同号而 $c$ 异号的矛盾情形）；
- 对每个素数 $p$，在 $\mathbb{Q}_p$ 上有解。

## 四、证明过程

### 第一步：约化到维数 3 和 4

首先注意：$f$ 在 $\mathbb{Q}$ 上表示零 $\iff$ $f$ 在 $\mathbb{Q}$ 上等价于 $\langle 0 \rangle \perp f'$（即 $f$ 包含一个零作为直和项）。

通过 Witt 消去定理，可以将问题约化。对 $n \geq 3$，若 $f$ 在所有局部域上表示零，则需要证明 $f$ 在 $\mathbb{Q}$ 上表示零。

**关键引理：** 若 $\dim f \geq 5$，则 $f$ 在 $\mathbb{Q}$ 上一定表示零（不需要局部条件）。这是因为 5 维以上的有理二次型总是迷向的（isotropic），这可以由 Chevalley-Warning 定理和 Hensel 引理得出。

因此只需处理 $n = 3$ 和 $n = 4$ 的情形。

### 第二步：三元二次型的情形

设 $f = \langle a, b, c \rangle$，即 $f(x,y,z) = ax^2 + by^2 + cz^2$。

$f$ 在 $\mathbb{Q}_v$ 上表示零 $\iff$ $(a, b)_v = (a, -c)_v$（通过 Hilbert 符号刻画）。

假设 $f$ 在所有 $\mathbb{Q}_v$ 上表示零。由 Hilbert 互反律：
$$\prod_v (a, b)_v = 1, \quad \prod_v (a, -c)_v = 1.$$

由于在每个 $v$ 处 $(a, b)_v = (a, -c)_v$，这些乘积公式自动相容。

需要证明 $f$ 在 $\mathbb{Q}$ 上表示零。这等价于证明 $c$ 被 $\langle a, b \rangle$ 在 $\mathbb{Q}$ 上表示。

利用**强逼近定理**（Strong Approximation）或有理数的 Hasse 原理对四元数代数：考虑 $\mathbb{Q}$ 上的四元数代数 $A = \left(\frac{a, b}{\mathbb{Q}}\right)$。$f$ 在 $\mathbb{Q}_v$ 上表示零 $\iff$ $A \otimes \mathbb{Q}_v$ 不是除代数（即分裂）。

由四元数代数的 Hasse 原理：$A$ 是除代数当且仅当存在某个 $v$ 使得 $A \otimes \mathbb{Q}_v$ 是除代数。因此若 $A$ 在所有 $v$ 处分裂，则 $A$ 本身分裂，即 $A \cong M_2(\mathbb{Q})$，从而 $f$ 在 $\mathbb{Q}$ 上表示零。

### 第三步：四元数代数的 Hasse 原理

设 $A = \left(\frac{a, b}{\mathbb{Q}}\right)$ 是 $\mathbb{Q}$ 上的四元数代数。$A$ 的中心为 $\mathbb{Q}$，$\dim_{\mathbb{Q}} A = 4$。

$A$ 的**Hasse 不变量**定义为：对每个位置 $v$，
$$\text{inv}_v(A) = (a, b)_v \in \{\pm 1\} \cong \frac{1}{2}\mathbb{Z}/\mathbb{Z}.$$

由类域论（或初等方法），$A$ 由其在所有局部域的不变量完全决定：
- $A$ 是除代数 $\iff$ 存在 $v$ 使得 $\text{inv}_v(A) \neq 0$。
- $\sum_v \text{inv}_v(A) = 0$（在 $\mathbb{Q}/\mathbb{Z}$ 中），这是 Hilbert 互反律。

因此，若对所有 $v$，$A \otimes \mathbb{Q}_v \cong M_2(\mathbb{Q}_v)$（即 $\text{inv}_v(A) = 0$），则 $A \cong M_2(\mathbb{Q})$，从而 $f$ 在 $\mathbb{Q}$ 上表示零。

### 第四步：一般维数

对 $n \geq 5$：由 Chevalley-Warning 定理，$f \bmod p$ 对几乎所有 $p$ 有非平凡零点。由 Hensel 引理，$f$ 在几乎所有 $\mathbb{Q}_p$ 上自动表示零。再结合 $n \geq 5$ 时局部条件的自动满足性，可以证明 $f$ 在 $\mathbb{Q}$ 上表示零。

对 $n = 4$：若 $f$ 在所有局部域上表示零，则 $f$ 的 Hasse 不变量在所有 $v$ 处为 0。由四元数代数的 Hasse 原理，$f$ 在 $\mathbb{Q}$ 上表示零。

对 $n = 3$：$f$ 在所有局部域上表示零意味着 $f$ 的 Clifford 代数（四元数代数）在所有局部域上分裂，从而在 $\mathbb{Q}$ 上分裂，因此 $f$ 在 $\mathbb{Q}$ 上表示零。

对 $n \leq 2$：定理仍然成立，但证明更简单（$n=1$ 是平凡的；$n=2$ 归结为 Hilbert 符号的计算）。$\blacksquare$

## 五、应用与意义

### 1. 二次型的完整分类

Hasse-Minkowski 定理使得有理数域上的二次型可以通过局部不变量完全分类。两个有理二次型等价当且仅当它们在所有局部域上等价，而局部二次型的分类是完全已知的（由维数、判别式和 Hasse 不变量确定）。

### 2. 局部整体原理的范式

Hasse-Minkowski 定理是局部整体原理最成功的实例。它启发了数论中一系列重要的猜想和研究方向：
- **Hasse 原理对高次曲面：** 对三次曲面（如椭圆曲线），Hasse 原理一般不成立。反例由 Selmer（三次型 $3x^3 + 4y^3 + 5z^3 = 0$）给出。
- **Brauer-Manin 障碍：** Manin 提出了用 Brauer 群解释 Hasse 原理失败的系统方法。对许多代数簇，Brauer-Manin 障碍是 Hasse 原理失败的唯一原因。

### 3. 四元数代数与 Brauer 群

Hasse-Minkowski 定理的证明引入了四元数代数和 Brauer 群的概念。$\mathbb{Q}$ 的 Brauer 群 $\text{Br}(\mathbb{Q})$ 通过 Hasse 不变量映射嵌入 $\bigoplus_v \text{Br}(\mathbb{Q}_v)$，且像恰好是满足"不变量之和为零"的元素。这是类域论的雏形。

### 4. 二次 Diophantine 方程

Hasse-Minkowski 定理给出了判定二次 Diophantine 方程是否有有理数解的**有效算法**：只需检查有限多个局部条件（有限多个 $p$ 和 $\mathbb{R}$）。这与高次方程形成鲜明对比——高次方程的有理可解性一般是不可判定的（Matiyasevich 定理）。

### 5. 向 adele 语言的推广

Hasse-Minkowski 定理在 adele 语言中有更优雅的表述。设 $V$ 是 $\mathbb{Q}$ 上的二次空间，$V_{\mathbb{A}} = V \otimes \mathbb{A}$ 是其 adele 化。则 $V$ 在 $\mathbb{Q}$ 上表示零 $\iff$ $V_{\mathbb{A}}$ 在 adele 上表示零。这一观点自然地将局部整体原理推广到代数群的上同调。

### 6. 与其他 Hasse 原理的联系

- **数论中的 Hasse 原理：** 对线性代数群 $G$，$H^1(\mathbb{Q}, G) \to \prod_v H^1(\mathbb{Q}_v, G)$ 的核的研究。
- **代数几何中的 Hasse 原理：** 对代数簇 $X/\mathbb{Q}$，$X(\mathbb{Q}) \neq \emptyset$ 与 $X(\mathbb{Q}_v) \neq \emptyset$（所有 $v$）之间的关系。
