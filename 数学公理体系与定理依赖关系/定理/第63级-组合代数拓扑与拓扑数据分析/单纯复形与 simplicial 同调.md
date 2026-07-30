# 单纯复形与 simplicial 同调

## 一、定理介绍

单纯复形（simplicial complex）是拓扑空间的一种组合描述方式：它把空间拆成点、线段、三角形、四面体等“单纯形”，并规定这些单纯形如何沿公共面粘贴。simplicial 同调则是赋予每个单纯复形一系列交换群 $H_n(K)$ 的代数工具，用来刻画空间的“洞”——$H_0$ 描述连通分支数，$H_1$ 描述一维洞（环），$H_2$ 描述二维空腔，依此类推。该理论架起了组合结构与连续拓扑之间的桥梁，是代数拓扑与拓扑数据分析的基石。

## 二、原理思路

1. **链群**：对单纯复形 $K$，记 $C_n(K)$ 为由所有 $n$ 维单纯形生成的自由交换群（系数通常取 $\mathbb{Z}$ 或域 $\mathbb{F}$）。
2. **边缘算子**：定义 $\partial_n: C_n(K) \to C_{n-1}(K)$，把每个 $n$ 维单纯形映为其诸 $(n-1)$ 维面的交替和。
3. **闭链与边缘**：满足 $\partial_n c = 0$ 的 $c$ 称为 $n$ 维闭链；若存在 $b$ 使得 $c = \partial_{n+1}b$，则称 $c$ 为边缘。
4. **同调群**：核心观察是“边缘的边缘为零”，即 $\partial_{n-1}\circ\partial_n = 0$。于是可定义商群
   $$
   H_n(K) = \ker \partial_n \big/ \operatorname{im} \partial_{n+1},
   $$
   它度量“$n$ 维洞”的个数。

## 三、定理的严格表述

设 $K$ 为抽象单纯复形（有限或局部有限），$\mathbb{F}$ 为域（或取 $\mathbb{Z}$）。对每个 $n\ge 0$，令 $C_n(K;\mathbb{F})$ 为以 $K$ 的 $n$ 维单纯形为基的自由 $\mathbb{F}$ 向量空间。对每个 $n$ 维单纯形 $\sigma = [v_0,\dots,v_n]$，定义边缘算子
$$
\partial_n(\sigma) = \sum_{i=0}^{n} (-1)^i [v_0,\dots,\widehat{v_i},\dots,v_n],
$$
并线性延拓到整个 $C_n(K;\mathbb{F})$。则
$$
\partial_{n-1}\circ \partial_n = 0 \quad (n\ge 1).
$$
从而第 $n$ 个 simplicial 同调群
$$
H_n(K;\mathbb{F}) = \frac{\ker(\partial_n: C_n \to C_{n-1})}{\operatorname{im}(\partial_{n+1}: C_{n+1} \to C_n)}
$$
是良定义的拓扑不变量：若两个单纯复形 $K,L$ 的几何实现同胚（或同伦等价），则 $H_n(K;\mathbb{F}) \cong H_n(L;\mathbb{F})$ 对所有 $n$ 成立。

## 四、证明过程

**步骤 1：验证 $\partial^2 = 0$。**
任取 $\sigma = [v_0,\dots,v_n]$。计算
$$
\partial_{n-1}\partial_n(\sigma)
= \sum_{i=0}^{n} (-1)^i \partial_{n-1}[v_0,\dots,\widehat{v_i},\dots,v_n].
$$
再删去一个顶点 $v_j$ 后，每个项出现两次：一次是先删 $v_i$ 再删 $v_j$（符号 $(-1)^{i+j-1}$，因 $j>i$ 时指标左移），另一次是先删 $v_j$ 再删 $v_i$（符号 $(-1)^{i+j}$）。两者恰好抵消，故和为 $0$。

**步骤 2：同调群是链复形的导出对象。**
由 $\partial^2=0$ 知 $\operatorname{im}\partial_{n+1} \subseteq \ker\partial_n$，商群良定义。

**步骤 3：拓扑不变性。**
对两个单纯复形 $K,L$，若其几何实现 $|K|,|L|$ 同伦等价，则可用 simplicial approximation theorem 把连续映射 $f:|K|\to|L|$ 近似为单纯映射，并构造链映射 $f_\sharp: C_*(K)\to C_*(L)$。进一步可证明 $f_\sharp$ 与 $g_\sharp$ 互为链同伦逆，从而诱导同构 $f_*: H_n(K)\to H_n(L)$。

## 五、应用与意义

- **Betti 数**：$\beta_n = \dim H_n(K;\mathbb{F})$ 直接给出不同维数洞的数量，是拓扑数据分析中的核心特征。
- **网络空腔**：在复杂网络中，高维单纯形可建模群体交互，simplicial 同调能检测传统图论无法发现的高维洞与协同结构。
- **计算可行性**：由于只需处理组合数据，simplicial 同调可通过线性代数高效实现，是持久同调、离散 Morse 理论等后续工具的起点。
