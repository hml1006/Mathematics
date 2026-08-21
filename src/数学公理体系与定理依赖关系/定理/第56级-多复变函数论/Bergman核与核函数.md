# Bergman 核与核函数

> **一句话大白话**：一个区域里所有"平方可积的解析函数"能构成一个内积空间，而把这种函数的取值"抽取"出来用的是一把特别的核（Bergman核）——它像一个水龙头，把全空间的解析函数逐点拧出数值，还能直接给出最佳逼近与度量的"度量张量"。
>
> **小例子**：单位圆盘的 Bergman 核是 $K(z,w)=1/(1-z\bar w)^2$；给定 $f$ 在该空间，其逐点值 $f(z)=\int f(w)K(w,z)\,dw$——核把整个函数按点"抽"回来，连通复分析、几何与函数论。

## 一、定理介绍

> **前置依赖**：Hilbert 空间、Riesz 表示定理、Cauchy 估计、双全纯映射、Kähler 度量。

Bergman 核函数是复分析中的核心工具之一，由 Stefan Bergman 在 1922 年引入。它通过 $L^2$ 全纯函数空间的再生核构造，给出了区域 $\Omega \subset \mathbb{C}^n$ 上一个规范、自然、且携带丰富几何信息的全纯函数 $K(z, w)$。

Bergman 核 $K_\Omega(z, w)$ 是 $\Omega \times \Omega$ 上的全纯函数（关于 $z$，反全纯关于 $w$），具有"再生性质"：对任意 $L^2$ 全纯函数 $f$，
$$f(z) = \int_\Omega K_\Omega(z, w) f(w) \, dV(w).$$
它在 $z = w$ 处的值 $K_\Omega(z) := K_\Omega(z, z)$ 为正函数，其 $\log K_\Omega(z)$ 给出 **Bergman 度量**
$$g^B_{j\bar{k}}(z) = \frac{\partial^2 \log K_\Omega(z)}{\partial z_j \partial \bar{z}_k}.$$
这一度量是 Kähler 度量，是区域 $\Omega$ 的双全纯不变量，承载了 $\Omega$ 的丰富几何信息。

在单复变中，Bergman 度量在单连通严格凸域上与 Poincaré 度量重合；在多复变中，Bergman 度量是研究双全纯刚性、等价问题的核心工具。Lu Qi-Keng 猜测、Bergman 度量的齐性空间分类等是当代多复变研究热点。

## 二、原理思路

Bergman 核理论的根本思想是利用 $L^2$ 全纯函数空间的 Hilbert 空间结构再生点赋值。

**关键观察**：
1. 对有界域 $\Omega \subset \mathbb{C}^n$，空间 $A^2(\Omega) = L^2(\Omega) \cap \mathcal{O}(\Omega)$ 是 $L^2(\Omega)$ 的闭子空间，故为 Hilbert 空间。
2. 点赋值泛函 $L_z: f \mapsto f(z)$ 在 $A^2(\Omega)$ 上有界（由 Cauchy 估计）。
3. 由 Riesz 表示定理，存在唯一 $K_z \in A^2(\Omega)$ 使得 $f(z) = \langle f, K_z \rangle$。设 $K(z, w) = \overline{K_z(w)}$，即得 Bergman 核。

**主要工具**：
- 正交投影（Bergman 投影）$P: L^2(\Omega) \to A^2(\Omega)$，$Pf(z) = \int K(z, w) f(w) dV(w)$。
- Bergman 度量 $g^B$ 的 Kähler 几何研究。
- Bergman 核的渐近行为（对角线 $K(z, z)$ 在边界附近的发散）给出与 Levi 形式的联系。

## 三、定理的严格表述

### Bergman 核的存在与再生性质

**定理（Bergman 核存在性）**：设 $\Omega \subset \mathbb{C}^n$ 为有界域。则存在唯一函数 $K_\Omega: \Omega \times \Omega \to \mathbb{C}$，满足：

1. **全纯性**：$K_\Omega(z, w)$ 关于 $z \in \Omega$ 全纯，关于 $w$ 反全纯。
2. **再生性**：对任意 $f \in A^2(\Omega) = L^2(\Omega) \cap \mathcal{O}(\Omega)$，
   $$f(z) = \int_\Omega K_\Omega(z, w) f(w) \, dV(w), \quad \forall z \in \Omega.$$
3. **对称性**：$K_\Omega(z, w) = \overline{K_\Omega(w, z)}$。
4. **正性**：$K_\Omega(z) := K_\Omega(z, z) > 0$ 对所有 $z \in \Omega$。

### Bergman 投影

定义 **Bergman 投影**
$$P_\Omega f(z) = \int_\Omega K_\Omega(z, w) f(w) \, dV(w).$$
则 $P_\Omega: L^2(\Omega) \to A^2(\Omega)$ 为正交投影。

### Bergman 度量

设 $\Omega$ 为有界域，$K_\Omega(z) = K_\Omega(z, z) > 0$。定义 **Bergman 度量**
$$g^B_{j\bar{k}}(z) = \frac{\partial^2 \log K_\Omega(z)}{\partial z_j \partial \bar{z}_k}, \quad j, k = 1, \dots, n.$$
则 $g^B$ 是 $\Omega$ 上的 Kähler 度量，且在双全纯映射下不变：若 $\Phi: \Omega_1 \to \Omega_2$ 为双全纯映射，则
$$\Phi^* g^B_{\Omega_2} = g^B_{\Omega_1}.$$

### 重要定理

**定理（Bergman 核在双全纯映射下的变换公式）**：设 $\Phi: \Omega_1 \to \Omega_2$ 为双全纯映射，则
$$K_{\Omega_2}(\Phi(z), \Phi(w)) \det \Phi'(z) \overline{\det \Phi'(w)} = K_{\Omega_1}(z, w).$$

**定理（Lu Qi-Keng 性质）**：若 $\Omega$ 满足 $K_\Omega(z, w) \neq 0$ 对所有 $z, w \in \Omega$ 成立，则称 $\Omega$ 为 Lu Qi-Keng 域。所有对称齐性有界域为 Lu Qi-Keng 域。

**定理（Bergman 核的边界渐近性，Fefferman）**：设 $\Omega \subset \mathbb{C}^n$ 为 $C^\infty$ 严格伪凸域。则在边界附近，
$$K_\Omega(z, z) = \frac{\varphi(z)}{\text{dist}(z, \partial \Omega)^{n+1}} + \psi(z) \log \text{dist}(z, \partial \Omega) + \text{光滑项},$$
其中 $\varphi, \psi$ 为 $\partial \Omega$ 附近的 $C^\infty$ 函数，$\varphi|_{\partial \Omega} \neq 0$，$\psi$ 在 $n \geq 2$ 时消失。

## 四、证明过程

### Bergman 核存在性证明

**步骤 1：Hilbert 空间结构**。设 $\Omega$ 为有界域。由 Cauchy 估计，对任意 $z \in \Omega$ 与紧子集 $K \subset \Omega$，
$$|f(z)| \leq C(z) \|f\|_{L^2}, \quad \forall f \in A^2(\Omega).$$
（由 $f(z) = \frac{1}{\text{Vol}(B(z,r))} \int_{B(z,r)} f dV$ 与 Cauchy–Schwarz 得。）

因此点赋值 $L_z: A^2(\Omega) \to \mathbb{C}$, $f \mapsto f(z)$ 为有界线性泛函。

**步骤 2：Riesz 表示**。由 Riesz 表示定理，存在唯一 $K_z \in A^2(\Omega)$ 使得
$$f(z) = \langle f, K_z \rangle = \int_\Omega f(w) \overline{K_z(w)} \, dV(w).$$
定义 $K_\Omega(z, w) := \overline{K_z(w)}$。

**步骤 3：对称性**。由 Riesz 表示的唯一性：$K_z(w) = \overline{K_w(z)}$，从而 $K_\Omega(z, w) = \overline{K_\Omega(w, z)}$。

**步骤 4：全纯性**。$K_\Omega(z, w) = \overline{K_w(z)}$ 关于 $z$ 全纯（因 $K_w \in A^2$）；由对称性，关于 $w$ 反全纯。

**步骤 5：正性**。$K_\Omega(z, z) = \|K_z\|^2 > 0$（因 $K_z \neq 0$）。$\square$

### 双全纯变换公式

设 $\Phi: \Omega_1 \to \Omega_2$ 双全纯。定义 $L^2$ 同构
$$T: A^2(\Omega_2) \to A^2(\Omega_1), \quad (Tf)(z) = f(\Phi(z)) \det \Phi'(z).$$
（变量替换 $\Phi(z) = w$ 给出 $T$ 等距。）

对 $f \in A^2(\Omega_2)$ 与 $z \in \Omega_1$：
$$f(\Phi(z)) = \int_{\Omega_2} K_{\Omega_2}(\Phi(z), w) f(w) dV(w).$$
另一方面，
$$(Tf)(z) = f(\Phi(z)) \det \Phi'(z) = \int_{\Omega_1} K_{\Omega_1}(z, \zeta) (Tf)(\zeta) dV(\zeta) = \int_{\Omega_1} K_{\Omega_1}(z, \zeta) f(\Phi(\zeta)) \det \Phi'(\zeta) dV(\zeta).$$
令 $w = \Phi(\zeta)$, $dV(w) = |\det \Phi'(\zeta)|^2 dV(\zeta)$：
$$(Tf)(z) = \int_{\Omega_2} K_{\Omega_1}(z, \Phi^{-1}(w)) f(w) \det \Phi'(\Phi^{-1}(w)) \frac{1}{|\det \Phi'(\Phi^{-1}(w))|^2} dV(w).$$
比较两式，由 $f$ 任意性与 Riesz 唯一性：
$$K_{\Omega_2}(\Phi(z), w) \det \Phi'(z) = \frac{K_{\Omega_1}(z, \Phi^{-1}(w))}{\overline{\det \Phi'(\Phi^{-1}(w))}}.$$
即
$$K_{\Omega_1}(z, \zeta) = K_{\Omega_2}(\Phi(z), \Phi(\zeta)) \det \Phi'(z) \overline{\det \Phi'(\zeta)}. \quad \square$$

### Bergman 度量的不变性

由变换公式，
$$\log K_{\Omega_1}(z) = \log K_{\Omega_2}(\Phi(z)) + \log |\det \Phi'(z)|^2.$$
后一项 $\log |\det \Phi'(z)|^2 = \log \det \Phi'(z) + \overline{\log \det \Phi'(z)}$ 关于 $z_j, \bar{z}_k$ 的混合导数为零（分别为全纯与反全纯）。因此
$$g^B_{\Omega_1, j\bar{k}}(z) = \sum_{a, b} g^B_{\Omega_2, a\bar{b}}(\Phi(z)) \frac{\partial \Phi_a}{\partial z_j} \overline{\frac{\partial \Phi_b}{\partial z_k}},$$
即 $\Phi^* g^B_{\Omega_2} = g^B_{\Omega_1}$。$\square$

### Fefferman 渐近公式概要

利用参数微积分（$\bar{\partial}$-Neumann 理论的边界行为）与奇性分析，Fefferman（1974）证明在严格伪凸边界附近，$K_\Omega(z, z)$ 主奇异项为 $\varphi(z) / \text{dist}(z, \partial \Omega)^{n+1}$。这一定理是高维双全纯刚性的基础。$\square$

## 五、应用与意义

Bergman 核与核函数理论在多复变与复几何中具有核心地位：

1. **双全纯不变量与刚性**：Bergman 度量是双全纯不变量。在严格伪凸域上，Bergman 度量的全测地子流形与边界刚性给出深远的刚性结果（如 Fefferman 的"双全纯映射光滑延拓到边界"定理）。

2. **齐性域分类**：单位球 $\mathbb{B}^n$ 的 Bergman 核为
   $$K_{\mathbb{B}^n}(z, w) = \frac{n!}{\pi^n} \frac{1}{(1 - \langle z, w \rangle)^{n+1}}.$$
   齐性有界域的 Bergman 核显式表达是分类的核心工具。Lu Qi-Keng 等利用 Bergman 核研究齐性域。

3. **边界全纯延拓**：Fefferman 的 Bergman 核渐近公式是证明严格伪凸域间双全纯映射光滑延拓到边界的关键工具，这一结果是多复变函数论的里程碑。

4. **复几何中的 Einstein 度量**：在球与多圆盘上，Bergman 度量分别为复双曲度量与乘积 Poincaré 度量。Bergman 度量是否为 Kähler–Einstein 度量与域的几何密切相关，是 Cheng 谱猜想等的研究对象。

5. **物理学应用**：Bergman 核在量子相空间几何、弦理论（Calabi–Yau 度量的 Bergman 逼近）、量子信息（Bergman 度量作为 Fisher 信息几何）有应用。

6. **数值与计算复几何**：Bergman 核的数值计算与逼近在多复变函数论计算中至关重要。Bergman 核的快速计算方法在现代科学计算中有广泛应用。
