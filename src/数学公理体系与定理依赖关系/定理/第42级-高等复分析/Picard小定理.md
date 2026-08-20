# Picard 小定理

> **一句话大白话**：一个"几乎处处能展开"的整函数，如果不是单纯地取到一个常数，那么它的值域整个复平面至多漏掉一个点——想永远躲开两个不同的逃跑路线是不可能的。
>
> **小例子**：$e^z$ 是整函数，它取不到 0，但其它每个非零复数都能取到——只漏这一个点；任何非常数整函数最多只能像这样"跳过"一个值。

## 介绍

Picard 小定理（Picard's little theorem）是复分析中最深刻的定理之一，由 Charles Émile Picard 在 1879 年证明。该定理断言：非常数整函数的值域要么是整个复平面 $\mathbb{C}$，要么是 $\mathbb{C}$ 去掉一个点（即最多有一个例外值）。这是 Liouville 定理（有界整函数为常数）的巨大推广，深刻地揭示了整函数的本质。

## 分析

**前置依赖**：整函数、Liouville 定理、Casorati–Weierstrass 定理、模函数、单值化定理。

**定理内容**：设 $f$ 是非常数整函数，则 $f(\mathbb{C})$ 在 $\mathbb{C}$ 中稠密，且最多遗漏一个值。即存在至多一个复数 $a$ 使得 $f(z) \neq a$ 对所有 $z \in \mathbb{C}$ 成立。

**等价形式**：若整函数 $f$ 不取两个不同的值 $a$ 和 $b$，则 $f$ 为常数。

**数学内涵**：Picard 小定理是 Liouville 定理的实质性加强。Liouville 定理说"有界整函数为常数"，而 Picard 定理说"不取两个值的整函数为常数"。例如，$e^z$ 不取 $0$，但取所有其他值（所以可以有一个例外值）。

**证明策略**：Picard 定理的经典证明需要用到模函数（modular function）$\lambda(\tau)$ 或椭圆模函数。基本思路是：假设 $f$ 不取 $0$ 和 $1$，则构造一个从复平面到单位圆盘的解析映射，从而 $f$ 有界，由 Liouville 定理得 $f$ 为常数。

## 思考过程

Picard 小定理的证明利用了"覆盖空间"的思想。考虑模函数 $\lambda: \mathbb{H} \to \mathbb{C} \setminus \{0,1\}$，它是上半平面到 $\mathbb{C}$ 去掉 $0,1$ 的万有覆盖映射。如果 $f: \mathbb{C} \to \mathbb{C} \setminus \{0,1\}$ 是整函数，由覆盖空间理论，存在提升 $\tilde{f}: \mathbb{C} \to \mathbb{H}$ 使得 $f = \lambda \circ \tilde{f}$。由于 $\mathbb{C}$ 是单连通的，提升存在。而 $\tilde{f}$ 将 $\mathbb{C}$ 映射到上半平面，其值域有界（因为 $\mathbb{H}$ 共形等价于单位圆盘 $D$），故 $\tilde{f}$ 有界，由 Liouville 定理，$\tilde{f}$ 为常数，从而 $f$ 为常数。

## 证明过程

**定理**（Picard 小定理）：非常数整函数不能遗漏两个不同的值。

**证明**：

**步骤 1**：假设整函数 $f$ 不取 $0$ 和 $1$。考虑模函数 $\lambda: \mathbb{H} \to \mathbb{C} \setminus \{0,1\}$，它是上半平面到 $\mathbb{C}\setminus\{0,1\}$ 的万有覆盖映射，且 $\lambda$ 是局部共形映射。

**步骤 2**：由于 $\mathbb{C}$ 是单连通的，由覆盖空间理论，存在提升 $\tilde{f}: \mathbb{C} \to \mathbb{H}$ 使得下图交换：
$$\begin{CD}
\mathbb{C} @>{\tilde{f}}>> \mathbb{H} \\
@| @VV{\lambda}V \\
\mathbb{C} @>{f}>> \mathbb{C} \setminus \{0,1\}
\end{CD}$$
即 $f(z) = \lambda(\tilde{f}(z))$ 对所有 $z \in \mathbb{C}$ 成立。

**步骤 3**：上半平面 $\mathbb{H}$ 共形等价于单位圆盘 $D = \{w \in \mathbb{C} \mid |w| < 1\}$，通过 Cayley 变换 $\varphi(z) = (z-i)/(z+i)$。因此 $\varphi \circ \tilde{f}: \mathbb{C} \to D$ 是整函数，且值域有界（在单位圆盘内）。

**步骤 4**：由 Liouville 定理，有界整函数为常数，故 $\varphi \circ \tilde{f}$ 为常数，从而 $\tilde{f}$ 为常数，进而 $f = \lambda \circ \tilde{f}$ 为常数。

**步骤 5**：因此，若 $f$ 遗漏两个不同的值 $a$ 和 $b$，则 $(f-a)/(b-a)$ 是遗漏 $0$ 和 $1$ 的整函数，由上述论证为常数，故 $f$ 为常数。$\square$

**推论**：非常数整函数的值域要么是 $\mathbb{C}$，要么是 $\mathbb{C} \setminus \{a\}$ 对某个 $a$。例如：
- $f(z) = z$ 的值域为 $\mathbb{C}$。
- $f(z) = e^z$ 的值域为 $\mathbb{C} \setminus \{0\}$。
- $f(z) = \sin z$ 的值域为 $\mathbb{C}$。