# Nash 嵌入定理

## 一、定理介绍

Nash 嵌入定理是微分几何中的里程碑结果，由 John Nash 于 1956 年证明。该定理断言：每个 Riemann 流形都可以等距嵌入到足够高维的欧几里得空间中。这一结果出乎意料，因为它表明抽象的 Riemann 流形总可以具体实现为欧氏空间的子流形，同时保持度量结构。

Nash 的证明使用了高度非线性的偏微分方程理论和 Nash-Moser 隐函数定理，开创了非线性 PDE 在几何中的应用。

## 二、原理思路

**核心思想**：通过逐步修正短嵌入（short embedding），使其逐渐逼近等距嵌入。

**关键观察**：
1. Whitney 嵌入定理保证光滑流形可以嵌入到 $\mathbb{R}^N$（$N$ 足够大），但不保持度量
2. 等距嵌入条件 $g_{ij} = \frac{\partial F}{\partial x^i} \cdot \frac{\partial F}{\partial x^j}$ 是欠定非线性 PDE 系统
3. Nash 的策略：先构造"短嵌入"（pullback 度量 $\leq$ 目标度量），然后逐步添加微扰使度量精确匹配
4. 微扰需要解决"损失导数"问题，Nash 发明了 Nash-Moser 隐函数定理

**证明策略**：
- 将等距嵌入问题转化为非线性 PDE
- 使用 Nash 微扰技术逐步修正度量误差
- Nash-Moser 隐函数定理处理导数损失
- 通过精细的估计保证收敛性

## 三、定理的严格表述

**定理（Nash 嵌入定理，光滑情形）**：设 $(M^n, g)$ 是 $n$ 维紧致光滑 Riemann 流形。则存在等距光滑嵌入 $F: M \to \mathbb{R}^N$，即 $F$ 是光滑嵌入且 $F^* g_{\text{Eucl}} = g$，其中 $N$ 仅依赖 $n$。

**维数估计**：

- **光滑紧致情形**：$N \leq \frac{n(3n+11)}{2}$（Nash 原始估计），后经改进为 $N \leq \frac{n(n+1)}{2} + n$（Gromov, Günther）
- **光滑非紧致情形**：$N \leq \frac{n(n+1)}{2} + \frac{n(n-1)}{2} + 1$（Günther）
- **$C^1$ 等距嵌入**：$N \geq n+1$ 即可（Nash-Kuiper 定理）

**Nash-Kuiper 定理（$C^1$ 等距嵌入）**：设 $(M^n, g)$ 是 $n$ 维 Riemann 流形，$F_0: M \to \mathbb{R}^N$（$N \geq n+1$）是短嵌入（即 $F_0^* g_{\text{Eucl}} < g$ 作为二次型）。则对任意 $\varepsilon > 0$，存在 $C^1$ 等距嵌入 $F: M \to \mathbb{R}^N$ 使得 $\|F - F_0\|_{C^0} < \varepsilon$。

**注**：$C^1$ 等距嵌入可以任意接近短嵌入，这与直觉相悖（如可以将球面 $C^1$ 等距嵌入到任意小的球中）。

## 四、证明过程

**定理（Nash 嵌入定理，简化版）**：紧致 Riemann 流形可以等距嵌入到 $\mathbb{R}^N$（$N$ 足够大）。

**证明思路**：

**步骤 1**：自由嵌入。称嵌入 $F: M \to \mathbb{R}^N$ 是**自由的**，如果对每个 $p \in M$，向量 $\{\frac{\partial F}{\partial x^i}(p)\}_{i=1}^n$ 和 $\{\frac{\partial^2 F}{\partial x^i \partial x^j}(p)\}_{1 \leq i \leq j \leq n}$ 线性无关。自由嵌入需要 $N \geq n + \frac{n(n+1)}{2} = \frac{n(n+3)}{2}$。

由 Whitney 嵌入定理的加强形式，自由嵌入存在（$N$ 足够大）。

**步骤 2**：度量误差。设 $F: M \to \mathbb{R}^N$ 是自由嵌入，$h = F^* g_{\text{Eucl}}$ 是 pullback 度量。度量误差为 $f = g - h$，是对称 $(0,2)$-张量。

**步骤 3**：Nash 微扰。对小的对称矩阵 $\delta$，寻找向量场 $v: M \to \mathbb{R}^N$ 使得 $(F + v)^* g_{\text{Eucl}} = h + f$。

展开到一阶：
$$(F + v)^* g_{\text{Eucl}} \approx h + 2 \langle dF, dv \rangle + \langle dv, dv \rangle$$

忽略二阶项，需要解
$$\langle dF, dv \rangle = \frac{1}{2} f$$

这是关于 $v$ 的线性 PDE。由于 $F$ 是自由嵌入，算子 $v \mapsto \langle dF, dv \rangle$ 的线性化是可逆的（在适当的函数空间中）。

**步骤 4**：Nash-Moser 隐函数定理。由于线性化算子损失导数（$v$ 需要比 $f$ 多一阶导数），标准隐函数定理不适用。Nash 发明了带光滑化子的迭代方法：

$$F_{k+1} = F_k + \eta_k S_{\theta_k}(v_k)$$
其中 $S_\theta$ 是光滑化算子（如 Fourier 截断），$\theta_k \to \infty$，$\eta_k$ 是步长。

**步骤 5**：收敛性估计。通过精细的 Sobolev 估计，证明迭代序列 $\{F_k\}$ 在 $C^\infty$ 拓扑下收敛到等距嵌入 $F_\infty$。

关键估计：
- 光滑化子保证每步的导数损失被控制
- 步长 $\eta_k$ 的快速衰减保证级数收敛
- 自由嵌入条件保证线性化算子的逆存在

**步骤 6**：从短嵌入到等距嵌入。若初始嵌入 $F_0$ 不是短的，先通过缩放使其成为短的，然后应用上述迭代。$\square$

**Nash-Kuiper 定理的证明思路**：

$C^1$ 情形不需要 Nash-Moser 定理。通过凸积分（convex integration）或周期性微扰，可以在 $C^0$ 接近的条件下修正度量。关键是利用 $C^1$ 拓扑下的高频振荡来"吸收"度量误差。

## 五、应用与意义

Nash 嵌入定理在数学中有深远影响：

1. **微分几何**：证明了抽象 Riemann 流形可以具体实现为欧氏空间子流形。

2. **PDE 理论**：Nash-Moser 隐函数定理成为处理导数损失问题的标准工具。

3. **几何分析**：启发了后来的几何流和正则性理论。

4. **刚性问题**：等距嵌入的唯一性和刚性是活跃的研究方向。

5. **$C^1$ 几何**：Nash-Kuiper 定理导致了 $h$-原理（h-principle）的发展（Gromov）。

6. **广义相对论**：等距嵌入用于研究时空的嵌入和初始值问题。

7. **材料科学**：$C^1$ 等距嵌入的"反直觉"性质与薄膜起皱现象相关。

Nash 嵌入定理的推广包括：伪 Riemann 流形的等距嵌入、带边流形的等距嵌入、以及局部等距嵌入问题。
