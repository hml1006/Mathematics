# Atiyah-Hirzebruch 谱序列

> **一句话大白话**：把一个空间的"普通洞"（上同调）当底料，一层层取极限"熬"，最终逼近高级洞（如 K 群）——谱序列是用普通上同调递推计算 K 理论的系统性方法。
>
> **小例子**：对 CW 复形 $X$，$E_2^{p,q}=H^p(X;\mathbb{Z}^q)$ 收敛到 K$^*(X)$；对球面 $S^1$ 这类小空间，该项只有 $p=0,1$ 非零，直接榨出 $K^*(S^1)$。

## 一、定理介绍

Atiyah-Hirzebruch 谱序列是连接普通上同调与广义上同调（如 K 理论）的强大工具，由 Michael Atiyah 和 Friedrich Hirzebruch 于 1960 年代初期建立。该谱序列从空间的普通上同调群出发，逐步逼近其 K 群，为 K 理论的计算提供了系统的方法。

谱序列的核心思想是：任何广义上同调理论都可以通过"扭曲"普通上同调来理解。Atiyah-Hirzebruch 谱序列量化了这种扭曲，并通过微分 $d_r$ 捕捉了 K 理论与普通上同调之间的差异。

## 二、原理思路

### 基本构造思想

Atiyah-Hirzebruch 谱序列的构造基于以下观察：

1. **骨架过滤**：对于 CW 复形 $X$，其骨架过滤 $X^0 \subset X^1 \subset X^2 \subset \cdots$ 诱导了 K 理论的过滤。

2. **相对 K 理论**：相对 K 群 $K(X^n, X^{n-1})$ 可以通过 Thom 同构与胞腔的上同调联系起来。

3. **精确偶**：通过长精确序列构造精确偶，进而得到谱序列。

### 关键洞察

谱序列的 $E_2$ 项是普通上同调：
$$E_2^{p,q} = H^p(X; K^q(pt))$$
其中 $K^q(pt)$ 是点的 K 群（由 Bott 周期性给出）。

微分 $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ 捕捉了从普通上同调到 K 理论的"修正"。

## 三、定理的严格表述

**定理 1（Atiyah-Hirzebruch 谱序列的存在性）** 设 $X$ 为有限 CW 复形。存在收敛到 $K^*(X)$ 的谱序列 $\{E_r^{*,*}, d_r\}$，满足：

1. **$E_2$ 项**：
$$E_2^{p,q} = H^p(X; K^q(pt))$$
其中 $K^q(pt) = \begin{cases} \mathbb{Z} & q \text{ 偶} \\ 0 & q \text{ 奇} \end{cases}$

因此：
$$E_2^{p,q} = \begin{cases} H^p(X; \mathbb{Z}) & q \text{ 偶} \\ 0 & q \text{ 奇} \end{cases}$$

2. **微分**：$d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$，满足 $d_r \circ d_r = 0$

3. **收敛性**：谱序列强收敛到 $K^{p+q}(X)$，即存在过滤
$$0 = F^{n+1} \subset F^n \subset \cdots \subset F^0 = K^n(X)$$
使得 $E_\infty^{p,q} \cong F^p K^{p+q}(X) / F^{p+1} K^{p+q}(X)$

**定理 2（低阶微分的识别）**

1. **$d_2$ 微分**：$d_2: E_2^{p,q} \to E_2^{p+2, q-1}$
   - 当 $q$ 为偶数时，$d_2: H^p(X; \mathbb{Z}) \to H^{p+2}(X; 0) = 0$
   - 因此 $d_2 = 0$，$E_3 = E_2$

2. **$d_3$ 微分**：$d_3: E_3^{p,q} \to E_3^{p+3, q-2}$
   - 当 $q$ 为偶数时，$d_3: H^p(X; \mathbb{Z}) \to H^{p+3}(X; \mathbb{Z})$
   - $d_3$ 与 Steenrod 运算 $Sq^3$ 相关：$d_3 = \rho \circ Sq^3$，其中 $\rho$ 为约化模 2

更一般地，$d_3$ 可以由 Bockstein 同态和 Steenrod 运算表示。

**定理 3（Chern 特征标与谱序列的关系）** Chern 特征标诱导了谱序列的映射：
$$\text{ch}: E_r^{p,q}(X) \to H^p(X; \mathbb{Q})$$
在 $E_\infty$ 项，$\text{ch}$ 给出同构：
$$\text{ch}: E_\infty^{p,q} \otimes \mathbb{Q} \to \begin{cases} H^p(X; \mathbb{Q}) & q \text{ 偶} \\ 0 & q \text{ 奇} \end{cases}$$

**定理 4（乘性结构）** Atiyah-Hirzebruch 谱序列具有乘性结构：
$$E_r^{p,q} \otimes E_r^{p',q'} \to E_r^{p+p', q+q'}$$
与 K 理论的杯积相容，即：
$$d_r(x \cdot y) = d_r(x) \cdot y + (-1)^{|x|} x \cdot d_r(y)$$

**定理 5（函子性）** 对于 CW 复形的映射 $f: X \to Y$，诱导谱序列的映射：
$$f^*: E_r^{p,q}(Y) \to E_r^{p,q}(X)$$
与 $f^*: K^*(Y) \to K^*(X)$ 相容。

## 四、证明过程

### 谱序列的构造

**步骤 1：骨架过滤**

设 $X$ 为 CW 复形，$X^n$ 为 $n$-骨架。定义 K 理论的过滤：
$$F^p K^n(X) = \ker(K^n(X) \to K^n(X^{p-1}))$$

这等价于 $F^p K^n(X) = \text{im}(K^n(X, X^{p-1}) \to K^n(X))$。

**步骤 2：相对 K 群**

由 Thom 同构定理和悬化同构：
$$K^n(X^p, X^{p-1}) \cong \bigoplus_{\alpha} K^n(D^p, S^{p-1}) \cong \bigoplus_{\alpha} K^{n-p}(pt)$$
其中 $\alpha$ 遍历 $p$-胞腔。

因此：
$$K^n(X^p, X^{p-1}) \cong C^p(X; K^*(pt))$$
即胞腔上链群，系数在 $K^*(pt)$ 中。

**步骤 3：精确偶**

定义：
$$D_1^{p,q} = K^{p+q}(X^p)$$
$$E_1^{p,q} = K^{p+q}(X^p, X^{p-1})$$

由长精确序列：
$$\cdots \to K^{p+q}(X^p, X^{p-1}) \xrightarrow{j} K^{p+q}(X^p) \xrightarrow{i} K^{p+q}(X^{p-1}) \xrightarrow{\delta} K^{p+q+1}(X^p, X^{p-1}) \to \cdots$$

这构成精确偶 $(D_1, E_1, i, j, \delta)$，其中：
- $i: D_1^{p-1,q+1} \to D_1^{p,q}$（限制映射）
- $j: E_1^{p,q} \to D_1^{p,q}$（从相对到绝对的映射）
- $\delta: D_1^{p,q} \to E_1^{p+1,q-1}$（连接同态）

**步骤 4：导出偶**

由精确偶的标准构造，定义 $d_1 = j \circ \delta: E_1^{p,q} \to E_1^{p+1,q}$。

计算 $d_1$：
$$d_1: K^{p+q}(X^p, X^{p-1}) \to K^{p+q+1}(X^{p+1}, X^p)$$

这正是胞腔上链复形的微分，因此：
$$E_2^{p,q} = H(E_1^{*,q}, d_1) \cong H^p(X; K^q(pt))$$

**步骤 5：高阶微分**

定义 $D_2 = \text{im}(D_1) \subset D_1$，$E_2 = H(E_1, d_1)$。

继续构造导出偶 $(D_r, E_r, i_r, j_r, \delta_r)$，定义 $d_r = j_r \circ \delta_r$。

微分的次数为 $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$。

### 收敛性的证明

**步骤 1：过滤的有界性**

对于有限 CW 复形，存在 $N$ 使得 $X^N = X$。因此：
$$F^{N+1} K^n(X) = 0$$
$$F^0 K^n(X) = K^n(X)$$

**步骤 2：强收敛**

需要证明对于每个 $(p,q)$，存在 $R$ 使得 $d_r: E_r^{p-r, q+r-1} \to E_r^{p,q}$ 和 $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ 在 $r \geq R$ 时为零。

由于 $X$ 有限，$E_2^{p,q}$ 在 $p < 0$ 或 $p > \dim X$ 时为零。因此对于固定的 $(p,q)$，当 $r$ 足够大时，$d_r$ 的源或目标为零。

**步骤 3：$E_\infty$ 项的识别**

定义 $E_\infty^{p,q} = \bigcap_r \text{im}(E_r^{p,q} \to E_r^{p,q})$。

由谱序列理论，$E_\infty^{p,q} \cong F^p K^{p+q}(X) / F^{p+1} K^{p+q}(X)$。

### $d_3$ 微分的识别

**定理**：$d_3: H^p(X; \mathbb{Z}) \to H^{p+3}(X; \mathbb{Z})$ 由 $d_3 = \beta \circ Sq^2 \circ \rho$ 给出，其中 $\rho: H^p(X; \mathbb{Z}) \to H^p(X; \mathbb{Z}_2)$ 为约化模 2，$\beta$ 为 Bockstein 同态。

**证明思路**：

1. 计算 $S^3$ 的 K 理论：$\tilde{K}(S^3) = 0$，但 $H^3(S^3; \mathbb{Z}) = \mathbb{Z}$

2. 在谱序列中，$E_2^{3,0} = \mathbb{Z}$ 必须被某个微分消灭

3. 唯一的可能是 $d_3: E_3^{0,2} \to E_3^{3,0}$，即 $d_3: \mathbb{Z} \to \mathbb{Z}$

4. 通过显式计算，$d_3$ 是乘以 2 的映射（对应于 $\eta$ 的 Hopf 不变量）

5. 推广到一般空间，$d_3$ 由 Steenrod 运算给出

## 五、应用与意义

### 1. K 群的计算

Atiyah-Hirzebruch 谱序列是计算 K 群的主要工具。

**例子**：计算 $K^*(\mathbb{CP}^n)$
- $H^*(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z}[x]/(x^{n+1})$，$|x| = 2$
- $E_2^{p,q} = H^p(\mathbb{CP}^n; K^q(pt))$
- 由于所有非零 $E_2$ 项都在 $p$ 偶数，$d_r$ 必须为零（次数原因）
- 因此 $E_\infty = E_2$，$K^0(\mathbb{CP}^n) = \mathbb{Z}^{n+1}$，$K^1(\mathbb{CP}^n) = 0$

**例子**：计算 $K^*(\mathbb{RP}^n)$
- $H^*(\mathbb{RP}^n; \mathbb{Z})$ 有 2-挠
- $d_3$ 微分非平凡，消灭部分 2-挠
- 结果：$K^0(\mathbb{RP}^n) = \mathbb{Z} \oplus \mathbb{Z}_{2^{\lfloor n/2 \rfloor}}$

### 2. 挠子群的研究

谱序列揭示了 K 理论的挠子群与上同调的挠子群之间的关系。

**定理**：若 $H^*(X; \mathbb{Z})$ 无挠，则 $K^*(X)$ 也无挠，且 $K^*(X) \cong H^{\text{even}}(X; \mathbb{Z})$（作为群）。

### 3. 特征类的构造

通过谱序列，可以构造从 K 理论到上同调的自然变换。

**应用**：Chern 特征标、Todd 类等都可以用谱序列的语言理解。

### 4. 广义上同调理论

Atiyah-Hirzebruch 谱序列可以推广到任何广义上同调理论 $E^*$：
$$E_2^{p,q} = H^p(X; E^q(pt)) \Rightarrow E^{p+q}(X)$$

这为研究广义上同调提供了统一框架。

### 5. 不动点定理

在 Atiyah-Bott 不动点定理中，谱序列用于计算等变 K 理论。

### 6. 指标定理

在 Atiyah-Singer 指标定理的证明中，谱序列用于将解析指标与拓扑指标联系起来。

### 7. 代数几何

在代数几何中，类似的谱序列连接了 motivic 上同调与代数 K 理论：
$$E_2^{p,q} = H^{p-q}_{\text{mot}}(X; \mathbb{Z}(-q)) \Rightarrow K_{-p-q}(X)$$
这是 Bloch-Lichtenbaum 谱序列。

### 8. 稳定同伦论

在稳定同伦论中，Atiyah-Hirzebruch 谱序列的特殊情况给出了从普通上同调到稳定同伦群的映射，这与 Adams 谱序列密切相关。

### 9. 物理学应用

在弦理论中，谱序列用于计算 D-膜电荷的 K 理论群，特别是在有挠上同调的情况下。
