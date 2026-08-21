# Arnold 猜想

> **一句话大白话**：一个能动而守恒的变换（辛同胚，"像液滴不破地流动"）引发的稳定点，至少要和曲面本身"洞的数目"一样多——把力学里的稳定点个数问题压到拓扑下界，是辛几何硬核问题（多数靠Floer同调已证）。
>
> **小例子**：对紧致辛流形 $(M^{2n},\omega)$，一阶哈密顿量在"好的"限制下其周期轨道数 ≥ $M$ 的亏格性下界（如 ≥ $\min\#\mathrm{crit}$ of a Morse 函数）；至少"洞"数那么多个稳定圈哪种都逃不掉 — 这被证明在主要辛环境下成立。

## 一、定理介绍

> **前置依赖**：辛流形、Hamilton 方程与作用泛函、Morse 理论、Floer 同调、Poincaré-Birkhoff 定理。

Arnold 猜想由 Vladimir Arnold 于 20 世纪 60 年代提出，是辛拓扑与 Hamilton 动力学的标志性猜想，被誉为现代辛拓扑的起点。它将 Morse 理论中临界点数与同调维数的关系类比推广到 Hamilton 同胚的不动点问题。

经典形式断言：紧辛流形 $(M, \omega)$ 上非退化 Hamilton 同胚 $\varphi$ 的不动点数不低于 $M$ 上的 Betti 数之和。这一猜想的深刻性在于：它将动力学问题（Hamilton 流的不动点）与纯拓扑量（流形的同调）联系起来，表明辛结构与 Hamilton 动力学之间存在刚性约束。

Arnold 猜想由 Andreas Floer 在 1988 年左右通过他创立的 Floer 同调理论证明（在 $\pi_2(M) = 0$ 或 $\omega|_{\pi_2} = 0$ 等假设下），这是 Floer 同调的诞生地。后续由 Fukaya-Ono、Liu-Tian、Hofer-Salamon 等推广至一般闭辛流形。

## 二、原理思路

Arnold 猜想的原理思路如下：

1. **Poincaré-Birkhoff 定理的推广**：Poincaré 在 1912 年的最后猜想（由 Birkhoff 证明）断言平环的保定向扭转同胚至少有两个不动点。Arnold 将其推广到高维辛流形上的 Hamilton 同胚。

2. **Morse 理论的类比**：在有限维 Morse 理论中，Morse 函数 $f: M \to \mathbb{R}$ 的非退化临界点数 $\#\mathrm{Crit}(f) \geq \sum_k \dim H_k(M)$。Arnold 猜想把 $f$ 换成 Hamilton 函数 $H$，把临界点换成 Hamilton 同胚的不动点。

3. **Hamilton 同胚的不动点 = 作用泛函的临界点**：Hamilton 同胚 $\varphi_H$ 的不动点对应于作用泛函 $\mathcal{A}_H$ 的临界点，即 Hamilton 方程的 1-周期解。

4. **Floer 同调的桥梁**：Floer 同调将 $\mathcal{A}_H$ 的"临界点数"转化为同调群的维数，得到
$$
\#\mathrm{Fix}(\varphi_H) \geq \sum_k \dim HF_k(M, H) = \sum_k \dim H_k(M; \mathbb{Z}_2).
$$

5. **辛刚性的体现**：Arnold 猜想表明 Hamilton 同胚的不动点数有下界，这是辛几何的刚性现象——一般微分同胚没有这种下界。

## 三、定理的严格表述

**设定**：设 $(M, \omega)$ 是 $2n$ 维闭辛流形，$H: S^1 \times M \to \mathbb{R}$ 是时间周期 Hamilton 函数，$\varphi_H: M \to M$ 是由 Hamilton 方程 $\dot{x} = X_H(t, x)$ 给定的 1-周期 Hamilton 同胚。

**定义（非退化）**：$\varphi_H$ 称为**非退化**的，若其所有不动点 $x$ 处的线性化映射 $d\varphi_H(x): T_xM \to T_xM$ 都没有特征值 1。等价地，对应 1-周期轨道的线性化 Poincaré 映射非退化。

**定理（Arnold 猜想——非退化情形）**：设 $(M, \omega)$ 是闭辛流形，$\varphi_H$ 是非退化 Hamilton 同胚。则
$$
\#\mathrm{Fix}(\varphi_H) \geq \sum_{k=0}^{2n} \dim H_k(M; \mathbb{Z}_2) =: \mathrm{SB}(M; \mathbb{Z}_2),
$$
其中 $\mathrm{SB}$ 表示 Betti 数之和。

**定理（Arnold 猜想——一般情形）**：设 $\varphi_H$ 是任意 Hamilton 同胚。则
$$
\#\mathrm{Fix}(\varphi_H) \geq \mathrm{CL}(M; \mathbb{Z}_2),
$$
其中 $\mathrm{CL}$ 是 $M$ 上 Hamilton 同痕的不动点 cup-length，至少为 $n + 1$（在合适的系数下为 $2n + 1$ 的情形需更精细分析）。简化的版本为
$$
\#\mathrm{Fix}(\varphi_H) \geq n + 1.
$$

**完整结果（Fukaya-Ono, Liu-Tian, Hofer-Salamon）**：对任意闭辛流形 $(M, \omega)$ 和任意 Hamilton 同胚 $\varphi_H$，按 $\mathbb{Z}_2$ 系数计数，有
$$
\#\mathrm{Fix}(\varphi_H) \geq \sum_k \dim H_k(M; \mathbb{Z}_2),
$$
其中非孤立不动点按其局部同调贡献计权（使用同调计数）。

## 四、证明过程

**非退化情形的证明（Floer 1988，在 $\omega|_{\pi_2(M)} = 0$ 假设下）**：

**步骤 1：不动点与周期轨道的对应**

$\varphi_H$ 的不动点 $x_0 \in M$ 对应于初值 $x(0) = x_0$ 的 Hamilton 方程 $\dot{x} = X_H(t, x)$ 的 1-周期解 $x(t)$（即 $x(1) = x(0) = x_0$）。

**步骤 2：作用泛函**

在环路空间 $\mathcal{L}M = C^\infty(S^1, M)$ 上定义作用泛函
$$
\mathcal{A}_H(x) = -\int_{D^2} \tilde{x}^*\omega + \int_0^1 H(t, x(t))\,dt,
$$
其中 $\tilde{x}: D^2 \to M$ 是 $x$ 的任意光滑延拓。当 $\omega|_{\pi_2} = 0$ 时，第一项良定义（与延拓无关）。

计算一阶变分：
$$
d\mathcal{A}_H(x)[\xi] = \int_0^1 \omega(\xi, \dot{x} - X_H(t, x))\,dt.
$$
故 $d\mathcal{A}_H(x) = 0$ 当且仅当 $\dot{x} = X_H(t, x)$，即 $x$ 是 1-周期解。因此不动点 = $\mathcal{A}_H$ 的临界点。

**步骤 3：Floer 链复形**

对每个非退化周期解 $x$，赋予 Conley-Zehnder 指标 $\mu_{CZ}(x) \in \mathbb{Z}$。定义
$$
CF_k(H) = \bigoplus_{\mu_{CZ}(x) = k} \mathbb{Z}_2 \langle x \rangle.
$$

**步骤 4：边界算子与 $\partial^2 = 0$**

定义 $\partial_k: CF_k \to CF_{k-1}$ 由 Floer 方程
$$
\partial_s u + J_t(u)(\partial_t u - X_H(t, u)) = 0, \quad u(-\infty) = x^-, \quad u(+\infty) = x^+
$$
的模空间（模 $\mathbb{R}$-平移）的模 2 计数给出。由 Gromov 紧性定理（在 $\omega|_{\pi_2} = 0$ 假设下无球气泡）和模空间紧化的边界分析，证明 $\partial^2 = 0$。详细论证见 Floer 同调条目。

**步骤 5：Floer 同调与奇异同调同构**

通过 continuation map 与退化 Hamilton 函数的极限（取 $H = \varepsilon f$，$\varepsilon \to 0$，$f$ 为 Morse 函数），Floer 同调退化为 Morse 同调，故
$$
HF_*(M, H) \cong MH_{*+n}(M, f) \cong H_{*+n}(M; \mathbb{Z}_2).
$$

**步骤 6：临界点数下界**

由链复形代数，链群的维数不低于同调的维数：
$$
\#\mathrm{Fix}(\varphi_H) = \sum_k \dim CF_k(H) \geq \sum_k \dim HF_k(M, H) = \sum_k \dim H_k(M; \mathbb{Z}_2).
$$
$\square$

**一般情形的证明概要（Fukaya-Ono, Liu-Tian）**：

**步骤 A：处理退化情形**

通过扰动 $H$ 为非退化 $H_\varepsilon$，将退化不动点附近的局部同调作为贡献。使用虚拟模空间（virtual moduli cycle）技术处理所有同伦类的问题，定义局部 Floer 同调。

**步骤 B：消除 $\omega|_{\pi_2} = 0$ 假设**

一般情形下需处理球气泡（sphere bubbling）。Fukaya-Ono 与 Liu-Tian 独立构造虚拟模空间，通过多级 glued 模空间的分析得到 $\partial^2 = 0$。关键步骤是球气泡的消去（通过虚拟技术的边界同调）。

**步骤 C：同调计数**

定义虚拟链（virtual chain）替代简单模 2 计数，得到 Hamilton 同胚的不动点按 $\mathbb{Z}_2$ 同调计数后大于等于 Betti 数之和。$\square$

## 五、应用与意义

**理论意义**：
1. **辛拓扑的起点**：Arnold 猜想激发了 Floer 同调的创立，是现代辛拓扑的奠基性结果。

2. **辛刚性的标志**：定理表明 Hamilton 同胚的不动点数有拓扑下界，这是辛几何独有的现象——一般同胚（即使是体积保持）没有这种下界。

3. **Morse 理论的无穷维推广**：Floer 同调将 Morse 理论成功推广到无穷维作用泛函，奠定了 Floer-type 理论的范式。

**应用领域**：
1. **Hamilton 动力学**：Arnold 猜想给出 Hamilton 同胚不动点存在性的拓扑保证，是研究 Hamilton 系统周期轨道的基础。

2. **Weinstein 猜想**：在某些情形下，Arnold 猜想的方法（特别是 Floer 同调）被推广用于证明 Weinstein 猜想——紧切触流形上 Reeb 向量场的周期轨道存在性。

3. **辛同胚群的结构**：Arnold 猜想的下界反映了辛同胚群与同伦群的深层联系，是辛同伦论的研究主题。

4. **镜像对称**：Floer 同调作为 Arnold 猜想的工具，是 Homological Mirror Symmetry 的核心代数对象。

**重要推广与变体**：
- **量子 Arnold 猜想**：考虑量子同调的不变量给出更精细的下界；
- **Lagrangian Arnold 猜想**：Lagrangian 子流形在 Hamilton 同胚下的相交数下界；
- **等变 Arnold 猜想**：带有群作用的辛流形上的等变不动点定理；
- **相对 Arnold 猜想**：带边辛流形或带 Lagrangian 边界的情形。

Arnold 猜想的证明及其后续发展深刻改变了辛拓扑、Hamilton 动力学与几何分析的面貌，是 20 世纪末数学的重大成就之一。
