# Floer 同调

> **一句话大白话**：像普通同调用"几何形状"计数，Floer同调用"哈密顿环路的解"（拟别线）来定义一种新的不变性质——它把那类高阶（无穷维）问题离散化成一个可算的同调群，为辛流形与三类/高维几何给出"能算的数字投票"。
>
> **小例子**：对辛流形取哈密顿量族，其周期轨道的"莫尔斯型"纠缠拼出 Floer 群 $HF_*$；配合"链复形-边界算子"两端同一，Arnold 猜想的证明正依赖此——无穷维"最速线"整理成可数模的空间。

## 一、定理介绍

> **前置依赖**：辛流形、Morse 同调、Cauchy-Riemann 型方程与相容近复结构、Gromov 紧性定理、Conley-Zehnder 指标。

Floer 同调由 Andreas Floer 于 1988 年左右提出，是辛拓扑与 Hamilton 动力系统的核心工具。Floer 同调将 Morse 瑞论的无穷维类比应用于 Hamilton 方程的周期解空间，将辛流形上的 1-周期轨道空间与连接它们的 Floer 轨道（即连接周期解的瞬子方程解）的模空间组织成一个同调群，称为 Floer 同调群。

Floer 同调是 Arnold 猜想证明的关键工具，也是辛拓扑从几何走向代数拓扑化的桥梁。它将 Hamilton 同胚的不动点数下界转化为同调群的秩下界，并将 Morse 理论、辛几何、规范理论的工具统一起来。Floer 同调后来发展为多种变体（辛 Floer 同调、切触同调、嵌入切触同调、Wrapped Floer 同调等），成为现代辛拓扑与切触拓扑的主干。

## 二、原理思路

Floer 同调的核心思路是将 Morse 理论推广到无穷维作用泛函的情形：

1. **作用泛函**：在闭辛流形 $(M, \omega)$ 上，对 Hamilton 函数 $H: S^1 \times M \to \mathbb{R}$，定义环路空间 $\mathcal{L}M = C^\infty(S^1, M)$ 上的作用泛函
$$
\mathcal{A}_H(x) = -\int_{D^2} \tilde{x}^*\omega + \int_{S^1} H(t, x(t))\,dt,
$$
其中 $\tilde{x}: D^2 \to M$ 是 $x: S^1 \to M$ 的延拓。

2. **临界点对应周期解**：$\mathcal{A}_H$ 的临界点恰是 Hamilton 方程 $\dot{x} = X_H(t, x)$ 的 1-周期解。

3. **Morse 理论无穷维化**：$\mathcal{A}_H$ 的 Hessian 在临界点处有无限多个正负特征值，故经典 Morse 理论失效，但 Floer 通过考虑负梯度流的轨道（连接轨道）来构造同调群。

4. **瞬子方程**：负梯度流方程在相容近复结构 $J$ 下变为 Cauchy-Riemann 型方程（Floer 方程）：
$$
\partial_s u + J(u)\big(\partial_t u - X_H(t, u)\big) = 0,
$$
其中 $u: \mathbb{R} \times S^1 \to M$。

5. **模空间与边界算子**：连接轨道的模空间经紧性定理与可数性分析，其 1 维子模空间的边界对应于断裂轨道，由此定义边界算子 $\partial$ 并证明 $\partial^2 = 0$。

6. **连续性**：不同 Hamilton 函数的 Floer 同调同构，从而 Floer 同调是辛流形本身的拓扑不变量。

## 三、定理的严格表述

**设定**：设 $(M, \omega)$ 是闭辛流形，$\omega$ 上的相容近复结构 $J$ 给出 $M$ 的度量。$H: S^1 \times M \to \mathbb{R}$ 是非退化 Hamilton 函数（所有 1-周期轨道的线性化 Poincaré 映射均无非 1 特征值）。

**临界点**：Hamilton 方程
$$
\dot{x}(t) = X_H(t, x(t)), \quad x(t) \in M, \quad t \in S^1 = \mathbb{R}/\mathbb{Z}
$$
的 1-周期解 $x(t)$（即 $x(t+1) = x(t)$）恰为 $\mathcal{A}_H$ 的临界点，记其集合为 $\mathcal{P}(H)$。

**Conley-Zehnder 指标**：对每个非退化周期轨道 $x \in \mathcal{P}(H)$，赋予整数 $\mu_{CZ}(x) \in \mathbb{Z}$，由线性化方程的迷群路径的 Maslov 指标定义。

**Floer 链复形**：定义分次 $\mathbb{Z}_2$-向量空间
$$
CF_k(H) = \bigoplus_{\substack{x \in \mathcal{P}(H) \\ \mu_{CZ}(x) = k}} \mathbb{Z}_2 \cdot \langle x \rangle.
$$
（在系数取 $\mathbb{Z}$ 的情形需引入配置空间与定向。）

**Floer 方程**：设 $J = \{J_t\}_{t \in S^1}$ 是相容近复结构的族。对 $x^\pm \in \mathcal{P}(H)$，考虑方程
$$
\begin{cases}
\partial_s u + J_t(u)\big(\partial_t u - X_H(t, u)\big) = 0, \\
\lim_{s \to -\infty} u(s, t) = x^-(t), \quad \lim_{s \to +\infty} u(s, t) = x^+(t).
\end{cases}
$$
其解的模空间记为 $\mathcal{M}(x^-, x^+; H, J)$，模去 $\mathbb{R}$-平移后记为 $\widehat{\mathcal{M}}$。

**边界算子**：当 $\mu_{CZ}(x^-) - \mu_{CZ}(x^+) = 1$ 时，$\widehat{\mathcal{M}}(x^-, x^+)$ 是 0 维紧致流形。定义
$$
\partial_k: CF_k(H) \to CF_{k-1}(H), \quad \partial_k \langle x^- \rangle = \sum_{\mu_{CZ}(x^+) = k-1} \#_2 \widehat{\mathcal{M}}(x^-, x^+) \langle x^+ \rangle,
$$
其中 $\#_2$ 表示模 2 计数。

**定理（Floer 同调）**：在上述设定下，$\partial \circ \partial = 0$。Floer 链复形 $(CF_*(H), \partial)$ 的同调
$$
HF_*(M, \omega; H, J) = H_*(CF_*(H), \partial)
$$
不依赖于 $H$ 与 $J$ 的选择（在合适的单调性条件下），因此是辛流形 $(M, \omega)$ 的不变量，记为 $HF_*(M, \omega)$。

**与奇异同调的关系**：若 $\pi_2(M) = 0$（或 $\omega$ 在 $\pi_2$ 上为零），则
$$
HF_*(M, \omega) \cong H_{* + n}(M; \mathbb{Z}_2),
$$
其中 $n = \frac{1}{2}\dim M$，$H_*$ 是奇异同调。

## 四、证明过程

**步骤 1：能量恒等式**

对 Floer 方程的解 $u$，定义能量
$$
E(u) = \int_{\mathbb{R} \times S^1} |\partial_s u|^2 \, ds\,dt = \mathcal{A}_H(x^-) - \mathcal{A}_H(x^+).
$$
由此，连接轨道只在 $\mathcal{A}_H(x^-) > \mathcal{A}_H(x^+)$ 时存在，能量有正下界。

**步骤 2：模空间的维数**

由指数定理，$\dim \mathcal{M}(x^-, x^+) = \mu_{CZ}(x^-) - \mu_{CZ}(x^+)$。故 $\mu_{CZ}(x^-) - \mu_{CZ}(x^+) = 1$ 时模空间（模去 $\mathbb{R}$-平移）是 0 维。

**步骤 3：Gromov 紧性**

**定理（Gromov-Floer 紧性）**：模空间 $\mathcal{M}(x^-, x^+)$ 在能量有界时的紧化（在 $\omega|_{\pi_2} = 0$ 假设下无球气泡）由"断裂轨道"构成：序列 $u_k$ 收敛（至多重极限）于若干连接轨道的复合，中间穿过其他周期轨道 $y_1, \ldots, y_k$。

**步骤 4：证明 $\partial^2 = 0$**

考虑 $\mu_{CZ}(x^-) - \mu_{CZ}(x^+) = 2$ 的模空间 $\widehat{\mathcal{M}}(x^-, x^+)$，其为 1 维紧致带边流形。其边界恰为
$$
\partial \widehat{\mathcal{M}}(x^-, x^+) = \bigsqcup_{y \in \mathcal{P}(H)} \widehat{\mathcal{M}}(x^-, y) \times \widehat{\mathcal{M}}(y, x^+),
$$
其中并取遍 $\mu_{CZ}(y) = \mu_{CZ}(x^-) - 1$ 的 $y$。

由 1 维紧致流形的边界计数的模 2 数为零：
$$
0 = \#_2 \partial \widehat{\mathcal{M}}(x^-, x^+) = \sum_y \#_2 \widehat{\mathcal{M}}(x^-, y) \cdot \#_2 \widehat{\mathcal{M}}(y, x^+).
$$
此即 $\langle \partial^2 x^-, x^+ \rangle = 0$，故 $\partial^2 = 0$。$\square$

**步骤 5：与奇异同调的同构**

选取 $H_\varepsilon = \varepsilon \cdot H_0$，$\varepsilon \to 0$。当 $H$ 充分小时，$\mathcal{A}_H$ 逼近 Morse 函数 $-H_0$（在 $M$ 上），Floer 方程退化为 $M$ 上 $-H_0$ 的负梯度流方程。由 Morse 同调与奇异同调的同构
$$
MH_*(M; f) \cong H_*(M; \mathbb{Z}_2),
$$
结合 Floer 同调关于 $H$ 的连续性（通过 continuation map），得到
$$
HF_*(M, \omega) \cong MH_{*+n}(M) \cong H_{*+n}(M; \mathbb{Z}_2).
$$
位移 $n$ 来自 Conley-Zehnder 指标的规范选取。$\square$

**步骤 6：连续性与不变量性**

对不同 $H_-, H_+$，通过选择连接它们的路径 $H_s$，构造依赖 $s$ 的 Floer 方程，定义 continuation map
$$
\Phi_{H_- H_+}: CF_*(H_-) \to CF_*(H_+),
$$
其诱导同调层级同构且与复合相容。故 $HF_*$ 仅依赖于 $(M, \omega)$。$\square$

## 五、应用与意义

**理论意义**：
1. **Arnold 猜想的证明**：Floer 同调给出 Arnold 猜想的关键证明：非退化 Hamilton 同胚的不动点数 $\#\mathrm{Fix}(\varphi_H) \geq \sum_k \dim H_k(M; \mathbb{Z}_2)$，因为不动点即 $\mathcal{A}_H$ 的临界点，其个数不低于链复形的秩。

2. **Morse 理论的无穷维推广**：Floer 同调是 Morse 理论在无穷维情形的成功推广，为瞬子方程、Yang-Mills 方程、Seiberg-Witten 方程的类似理论提供了范例。

3. **辛拓扑的代数化**：Floer 同调将辛拓扑问题转化为代数拓扑计算，是辛拓扑从几何向代数拓扑方法转变的标志。

**应用领域**：
1. **Hamilton 动力学**：Floer 同调用于证明 Weinstein 猜想（标准接触球面上的周期 Reeb 轨道存在性）、Hofer-Zehnder 猜想等动力学问题。

2. **辛配边与 Lagrangian 子流形**：Floer 同调推广为 Lagrangian Floer 同调，用于研究 Lagrangian 子流形的相交不变量与 Hamilton 拉直的不变性。

3. **镜像对称**：Lagrangian Floer 同调是 Homological Mirror Symmetry 的核心代数对象，将几何问题转化为 $A_\infty$-范畴的计算。

4. **规范理论**：Floer 同调启发了 Instanton Floer 同调、Heegaard Floer 同调、Monopole Floer 同调等，深刻影响低维拓扑的研究。
