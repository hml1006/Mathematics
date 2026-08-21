# Calabi-Yau 定理

> **一句话大白话**：若一个复流形拓扑上"可当作无质量暗洞"（第一陈类=0 且 Kähler），那么它就真能配出一套"处处无曲率绕着各向同性方向刚好搭平"的特别度量（Ricci平坦、Chern对偶上自对偶）——Calabi 猜想的证明，是"拓扑上像空 → 真能找到空度量"的漂亮落地。
>
> **小例子**：K3 曲面或复环 $T^{2}$ 上可取处处 Ricci 平坦的 Kähler 度量，全靠 Calabi-Yau 定理把"共形类里的平坦体积"实现出来；这给了弦论里"没有引力源的内空间"（Calabi-Yau 流形）的构造基石。

## 一、定理介绍

> **前置依赖**：Kähler 流形与 Ricci 形式、第一 Chern 类、复 Monge-Ampère 方程、连续性方法、先验估计（$C^0$、$C^2$ 估计与 Schauder 理论）。

Calabi-Yau 定理是 Kähler 几何中里程碑式的结果，由丘成桐（Shing-Tung Yau）于 1978 年证明，确立了 Calabi 于 1954 年提出的著名猜想。定理断言：在任意紧 Kähler 流形 $(X, \omega)$ 上，给定代表 $c_1(X)$ 的任意闭 $(1,1)$-形式 $\alpha$，存在唯一的 Kähler 度量 $\tilde\omega$，使其 Kähler 形式与 $\omega$ 同调且 Ricci 形式恰为 $\alpha$。

特别地，若 $X$ 具有平凡典则线丛（即第一 Chern 类 $c_1(X) = 0$），则存在 Ricci 平坦的 Kähler 度量——这是 Calabi-Yau 流形（在弦理论中至关重要）的几何基础。

这一定理将 Kähler 几何中的非线性偏微分方程问题（复 Monge-Ampère 方程）转化为整体几何问题，是 20 世纪几何分析最重要的成果之一。

## 二、原理思路

### 基本思想

问题归结为求解复 Monge-Ampère 方程。设 $\omega$ 为初始 Kähler 形式，要找 Kähler 形式

$$\tilde\omega = \omega + \sqrt{-1}\partial\bar\partial \varphi$$

（$\varphi$ 为光滑实值函数）使得 $\text{Ric}(\tilde\omega)$ 是预给的形式。由局部公式，Ricci 形式为

$$\text{Ric}(\omega) = -\sqrt{-1}\partial\bar\partial \log \det(g_{i\bar j})$$

故 Ricci 形式的改变由度量的行列式的比值刻画。

### Monge-Ampère 方程的导出

设 $\omega^n / n!$ 为体积形式。要使 $\text{Ric}(\tilde\omega) = \alpha$，等价于（由 Chern-Weil 理论与 Bianchi 恒等式）

$$\frac{\tilde\omega^n}{\omega^n} = e^{F - \varphi}$$

其中 $F$ 是由 $\alpha$ 决定的函数。由此得到完全非线性 PDE：

$$(\omega + \sqrt{-1}\partial\bar\partial\varphi)^n = e^{F - \varphi}\,\omega^n$$

加上 Kähler 条件 $\omega + \sqrt{-1}\partial\bar\partial\varphi > 0$ 与归一化条件 $\sup_X \varphi = 0$。

### Yau 的方法

证明包含两个核心步骤：

1. **先验估计**：利用 Yau 的 Moser 迭代与 Calabi 的思路，对解的二阶导数与三阶导数给出一致先验界（$C^{2,\alpha}$ 估计）。

2. **连续性方法**：将方程嵌入单参数族，证明解集既开又闭，由先验估计与 Aubin-Yau 的存在定理得到整体解。

## 三、定理的严格表述

**定理（Calabi-Yau）** 设 $(X, \omega)$ 为 $n$ 维紧 Kähler 流形。设 $[\alpha] \in 2\pi c_1(X)$ 为 $c_1(X)$ 的代表闭 $(1,1)$-形式（即 $[\alpha]/(2\pi) = c_1(X) \in H^{1,1}(X, \mathbb{R})$）。则存在唯一的 Kähler 形式 $\tilde\omega$，使得：

1. $[\tilde\omega] = [\omega] \in H^2_{\text{dR}}(X, \mathbb{R})$（同调类不变）；
2. $\text{Ric}(\tilde\omega) = \alpha$。

**推论（Ricci-平坦度量存在）** 若 $c_1(X) = 0$（即 $X$ 的典则丛 $K_X$ 是拓扑平凡的全纯线丛），则存在唯一的 Ricci 平坦 Kähler 度量 $\tilde\omega \in [\omega]$，即 $\text{Ric}(\tilde\omega) = 0$。

**等价的 PDE 形式** 设 $\omega$ 为 Kähler 形式，$f \in C^\infty(X)$ 由 $\alpha = -\sqrt{-1}\partial\bar\partial \log f$ 与归一化 $\int_X f\,\omega^n = \int_X \omega^n$ 唯一决定。则求解 $\varphi \in C^\infty(X, \mathbb{R})$，满足：

$$
\begin{cases}
(\omega + \sqrt{-1}\partial\bar\partial\varphi)^n = e^F \omega^n, & \text{（其中 } e^F \text{ 由 } f \text{ 确定）}\\
\omega + \sqrt{-1}\partial\bar\partial\varphi > 0, & \\
\sup_X \varphi = 0. &
\end{cases}
$$

具体地，当 $\alpha = 0$ 时，方程化为 $(\omega + \sqrt{-1}\partial\bar\partial\varphi)^n = C\,\omega^n$，其中 $C$ 为常数。

## 四、证明过程

以下以 $\text{Ric}(\tilde\omega) = 0$ 情形（即 $c_1(X) = 0$）为例说明证明思路。

### 步骤 1：化归为复 Monge-Ampère 方程

设 $\omega$ 为给定 Kähler 形式，$\tilde\omega = \omega + \sqrt{-1}\partial\bar\partial\varphi$。要使 $\text{Ric}(\tilde\omega) = 0$，等价于 $\tilde\omega^n$ 是常值体积形式。

由 Ricci 形式公式：
$$\text{Ric}(\tilde\omega) = -\sqrt{-1}\partial\bar\partial\log\det(\tilde g_{i\bar j})$$

要 $\text{Ric}(\tilde\omega) = 0$，需 $\det(\tilde g_{i\bar j})$ 为常数（局部），即

$$\frac{\det(\tilde g_{i\bar j})}{\det(g_{i\bar j})} = \text{const.}$$

而 $\det(\tilde g_{i\bar j})/\det(g_{i\bar j}) = (\omega + \sqrt{-1}\partial\bar\partial\varphi)^n/\omega^n$，故化为方程

$$(\omega + \sqrt{-1}\partial\bar\partial\varphi)^n = C\,\omega^n$$

其中 $C$ 由体积归一化确定：$C = \int_X \omega^n / \int_X \omega^n = 1$（若 $[\tilde\omega] = [\omega]$）。实际上 $C = 1$（因 $\int \tilde\omega^n = \int \omega^n$）。

### 步骤 2：连续性方法

引入单参数族方程：对 $t \in [0, 1]$，求 $\varphi_t$ 使

$$(\omega + \sqrt{-1}\partial\bar\partial\varphi_t)^n = (1 - t + t\,e^F)\,\omega^n$$

$t = 0$：平凡解 $\varphi_0 = 0$；$t = 1$：目标方程。

设 $S = \{t \in [0, 1] : \exists\,\varphi_t \text{ 解}\}$。证明：

1. **$S$ 为开集**：由隐函数定理，复 Monge-Ampère 算子的线性化是线性椭圆算子 $\Delta_{\tilde\omega}$，故解局部存在唯一。

2. **$S$ 为闭集**：需对 $t \in S$ 一致地得到 $\varphi_t$ 的先验估计。

### 步骤 3：先验估计

Yau 的核心贡献是建立一致先验估计。

**(i) $C^0$ 估计**：由 Chern-Lu 不等式与比较定理，得 $\sup_X |\varphi| \leq C$。

具体地，对 $\tilde\omega$-Laplacian $\Delta_{\tilde\omega}\varphi$，经计算 $\Delta_{\tilde\omega}\log(n + \Delta_\omega\varphi)$ 与 $\Delta_{\tilde\omega}\varphi$ 之间满足不等式，结合 Yau 的截断技巧得到 $\varphi$ 的 $L^\infty$ 界。

**(ii) $C^2$ 估计（梯量估计）**：这是 Yau 证明的关键突破。考虑辅助函数

$$S = \log\left(\text{tr}_\omega \tilde\omega\right) - \lambda \varphi$$

其中 $\text{tr}_\omega \tilde\omega = g^{i\bar j}\tilde g_{i\bar j}$。Yau 用了 Chern-Lu 不等式的复版本，结合 Moser 迭代与极大值原理，得到 $\text{tr}_\omega \tilde\omega \leq C$，从而 $\Delta_\omega \varphi$ 一致有界。

核心局部计算：在 $\tilde g$ 的正规坐标下，$S$ 的 $\tilde\omega$-Laplacian 满足

$$\Delta_{\tilde\omega} S \geq -C_1 \text{tr}_\omega\tilde\omega + C_2 \,\text{Ric}(\tilde\omega) - C_3$$

在极大值点处用 $\text{Ric}(\tilde\omega)$ 的方程约束，得界。

**(iii) 高阶估计**：由 Monge-Ampère 方程的一致椭圆性（$\tilde\omega \geq c\omega$，由 $C^2$ 估计得到）+ Evans-Krylov-Safonov 正则性 + Schauder 理论：$\|\varphi\|_{C^{k,\alpha}} \leq C_k$。

### 步骤 4：闭集的证明

由一致先验估计 $\|\varphi_t\|_{C^{2,\alpha}} \leq C$（一致于 $t \in [0,1]$），可在 $t \to t_0$ 时取极限，得 $\varphi_{t_0}$。故 $S$ 闭。

由 $S$ 非空、开、闭，$S = [0, 1]$，$t = 1$ 给出解。

### 步骤 5：唯一性

设 $\varphi_1, \varphi_2$ 均为解。由 $\tilde\omega_1^n = \tilde\omega_2^n$，设 $\psi = \varphi_1 - \varphi_2$，使用复 Monge-Ampère 的凹性（$\det^{1/n}$ 凹性）：

$$0 \geq n\,(\det \tilde g_1)^{1/n} - n\,(\det \tilde g_2)^{1/n} \geq \tilde g_2^{i\bar j}\,\partial_i\bar\partial_j\psi$$

结合极大值原理（$\sup \psi = 0$、$\inf \psi = 0$），得 $\psi = 0$。

### 步骤 6：一般情形 $\text{Ric}(\tilde\omega) = \alpha$

将方程改为

$$(\omega + \sqrt{-1}\partial\bar\partial\varphi)^n = e^{F - \varphi}\,\omega^n$$

（其中 $F$ 由 $\alpha$ 决定）。连续性方法中方程为 $(\omega + \sqrt{-1}\partial\bar\partial\varphi_t)^n = e^{tF - \varphi_t + (1-t)\varphi_0 + \cdots}\omega^n$，先验估计多一项 $e^{-\varphi}$（与 $\varphi$ 同方向），由相同的极值原理方法处理。证明的关键差异在于：$\varphi$ 的下界可由方程直接得到（指数项控制）。

## 五、应用与意义

### 1. Calabi-Yau 流形的定义

Ricci-平坦 Kähler 度量的存在性使"Calabi-Yau 流形"有了坚实的几何意义，是弦理论中紧化的几何基础。

### 2. 弦理论中的镜像对称

Calabi-Yau 三维流形上 Ricci 平坦度量的存在性，是弦理论 $N=1$ 超对称性保持的几何基础。镜面对称猜想的基础依赖于 Calabi-Yau 度量的特殊结构。

### 3. Yau 的 millennium 问题

Calabi-Yau 定理的方法（复 Monge-Ampère 方程的先验估计）是 Hamilton 的 Ricci 流方法与 Perelman 证明 Poincaré 猜想的先导。是几何分析的奠基性范例。

### 4. Chern 数不等式

由 Yau 的证明方法可推出 Miyaoka-Yau 不等式：对于 Kähler 曲面（或一般型高维流形），有

$$c_2(X) \geq \frac{n+1}{2n}\,c_1(X)^2$$

是分类理论与复曲面几何的基础。

### 5. Donaldson-Thomas 理论

Calabi-Yau 度量作为"标准度量"，是 Donaldson-Thomas 不变量、特殊拉格朗日子流形研究、稳定向量丛与 Hermitian-Einstein 度量对应的几何基础。

### 6. 几何稳定性

Yau 对 Calabi 猜想的证明启发了 Donaldson 关于 Kähler 度量稳定性（$K$-稳定性）与 Fano 流形上 Kähler-Einstein 度量存在性（Yau-Tian-Donaldson 猜想）的研究。

### 7. 代数几何中的整体截面

Calabi-Yau 定理保证典则丛平凡流形上的 Ricci 平坦度量，使 Hodge 理论可使用 $h^{n,0} = 1$ 的结构，是研究 Calabi-Yau 流形代数结构（如 $N^K = 1$）的关键工具。

### 8. 与 Yau 的 Miyaoka-Yau 不等式

通过 Ricci 平坦度量上的 Gauss-Bonnet-Chern 公式，可得到 $c_2 \geq 0$ 与高阶 Chern 类的精密不等式，是高维代数几何与微分几何交汇的核心结果。
