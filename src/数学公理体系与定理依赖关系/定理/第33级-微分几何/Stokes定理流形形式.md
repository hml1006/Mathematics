# Stokes 定理（流形形式）

> **一句话大白话**：流形上的微积分居然可以"换皮不换髓"——在一块区域的微分形式外派导数的积分，等于其边界上的直接积分，把体积分的账安全转移到边界上去算。
>
> **小例子**：在 $\mathbb R^2$ 上它退化为格林定理、在 $\mathbb R^3$ 退化为高斯和旋度定理；用纯集合语言：$\int_\Omega d\omega=\int_{\partial\Omega}\omega$，边界"消化"内部的所有变化。

## 一、定理介绍

> **前置依赖**：微分形式与外微分、单位分解、流形与边界的定向、Fubini 定理与微积分基本定理

Stokes 定理是微积分基本定理、Green 定理、Gauss 散度定理和经典 Stokes 定理在光滑流形上的统一推广。它建立了流形上微分形式的积分与其边界上积分之间的关系，是微分几何和几何测度论的核心结果。

Stokes 定理将局部微分运算（外微分）与全局拓扑性质（边界）联系起来，是 de Rham 上同调理论、Hodge 理论和指标定理的基础。它在物理学（如电磁学、流体力学）和工程学中有直接应用。

## 二、原理思路

**核心思想**：流形上微分形式的外微分的积分等于该形式在边界上的积分。

**关键观察**：
1. 微积分基本定理：$\int_a^b f'(x) dx = f(b) - f(a)$ 是 Stokes 定理在 1 维的特例
2. 外微分 $d$ 是局部运算，积分是全局运算，Stokes 定理连接了二者
3. 定理的证明可以通过单位分解归结为 $\mathbb{R}^n$ 中上半空间的情形
4. 定向和边界的一致性是定理成立的关键

**证明策略**：
- 利用单位分解将全局问题局部化
- 在坐标卡中归结为 $\mathbb{R}^n_+$ 上的 Fubini 定理和微积分基本定理
- 处理边界项时注意定向的相容性

## 三、定理的严格表述

**定理（Stokes 定理）**：设 $M$ 是 $n$ 维紧致定向光滑流形（带边界），$\omega$ 是 $M$ 上的 $(n-1)$-次光滑微分形式。则
$$\int_M d\omega = \int_{\partial M} \omega$$
其中 $\partial M$ 赋予诱导定向。

**诱导定向**：若 $M$ 的定向由体积形式 $\Omega$ 给出，则 $\partial M$ 的定向由以下方式确定：在边界点 $p$，取外向法向量 $\nu$，则 $\partial M$ 的定向由 $\iota_\nu \Omega$ 给出（即"先法向量，后切空间"的约定）。

**经典特例**：

1. **微积分基本定理**（$M = [a, b]$，$\omega = f$）：
$$\int_{[a,b]} df = \int_a^b f'(x) dx = f(b) - f(a) = \int_{\partial [a,b]} f$$

2. **Green 定理**（$M \subset \mathbb{R}^2$，$\omega = P dx + Q dy$）：
$$\int_M d\omega = \int_M \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx \wedge dy = \int_{\partial M} P dx + Q dy$$

3. **Gauss 散度定理**（$M \subset \mathbb{R}^3$，$\omega = F_1 dy \wedge dz + F_2 dz \wedge dx + F_3 dx \wedge dy$）：
$$\int_M d\omega = \int_M \nabla \cdot F \, dV = \int_{\partial M} F \cdot dS$$

4. **经典 Stokes 定理**（$M \subset \mathbb{R}^3$ 曲面，$\omega = F_1 dx + F_2 dy + F_3 dz$）：
$$\int_M d\omega = \int_M (\nabla \times F) \cdot dS = \int_{\partial M} F \cdot dr$$

## 四、证明过程

**证明**：

**步骤 1**：单位分解。设 $\{U_\alpha, \phi_\alpha\}$ 是 $M$ 的定向坐标卡覆盖，$\{\rho_\alpha\}$ 是从属的单位分解。则 $\omega = \sum \rho_\alpha \omega$，且 $d\omega = \sum d(\rho_\alpha \omega)$。

由于积分的线性性，只需对每个 $\rho_\alpha \omega$ 证明定理。因此可以假设 $\omega$ 的支撑包含在单个坐标卡 $U$ 中。

**步骤 2**：内部坐标卡。若 $U \cap \partial M = \emptyset$（$U$ 在 $M$ 内部），则 $\partial U = \emptyset$。在坐标 $(x^1, \ldots, x^n)$ 下，
$$\omega = \sum_{i=1}^n (-1)^{i-1} f_i \, dx^1 \wedge \cdots \wedge \widehat{dx^i} \wedge \cdots \wedge dx^n$$
$$d\omega = \sum_{i=1}^n \frac{\partial f_i}{\partial x^i} dx^1 \wedge \cdots \wedge dx^n$$

$$\int_M d\omega = \sum_i \int_{\mathbb{R}^n} \frac{\partial f_i}{\partial x^i} dx^1 \cdots dx^n$$

由 Fubini 定理和 $f_i$ 的紧支集，对每个 $i$，
$$\int_{\mathbb{R}} \frac{\partial f_i}{\partial x^i} dx^i = 0$$
（因为 $f_i$ 在无穷远处为零）。因此 $\int_M d\omega = 0 = \int_{\partial M} \omega$。

**步骤 3**：边界坐标卡。若 $U \cap \partial M \neq \emptyset$，选取坐标使得 $U$ 对应于上半空间 $\mathbb{R}^n_+ = \{x^n \geq 0\}$，边界对应于 $x^n = 0$。

$$\int_M d\omega = \sum_i \int_{\mathbb{R}^n_+} \frac{\partial f_i}{\partial x^i} dx^1 \cdots dx^n$$

对 $i < n$，由 Fubini 定理和 $f_i$ 的紧支集，$\int_{\mathbb{R}} \frac{\partial f_i}{\partial x^i} dx^i = 0$。

对 $i = n$，
$$\int_{\mathbb{R}^n_+} \frac{\partial f_n}{\partial x^n} dx^1 \cdots dx^n = \int_{\mathbb{R}^{n-1}} \left(\int_0^\infty \frac{\partial f_n}{\partial x^n} dx^n\right) dx^1 \cdots dx^{n-1}$$
$$= \int_{\mathbb{R}^{n-1}} [f_n(x^1, \ldots, x^{n-1}, \infty) - f_n(x^1, \ldots, x^{n-1}, 0)] dx^1 \cdots dx^{n-1}$$
$$= -\int_{\mathbb{R}^{n-1}} f_n(x^1, \ldots, x^{n-1}, 0) dx^1 \cdots dx^{n-1}$$

**步骤 4**：边界积分。在 $\partial M$ 上（$x^n = 0$），
$$\omega|_{\partial M} = (-1)^{n-1} f_n(x^1, \ldots, x^{n-1}, 0) dx^1 \wedge \cdots \wedge dx^{n-1}$$

由诱导定向的约定，$\partial M$ 的定向形式为 $(-1)^{n-1} dx^1 \wedge \cdots \wedge dx^{n-1}$（外向法向量是 $-\frac{\partial}{\partial x^n}$，需要调整符号）。

因此
$$\int_{\partial M} \omega = (-1)^{n-1} \int_{\mathbb{R}^{n-1}} f_n(x^1, \ldots, x^{n-1}, 0) dx^1 \cdots dx^{n-1}$$

与步骤 3 比较，$\int_M d\omega = \int_{\partial M} \omega$。$\square$

**推论**：若 $M$ 是紧致无边界流形，则对任意 $(n-1)$-形式 $\omega$，$\int_M d\omega = 0$。

**推论**：若 $M$ 是紧致定向 $n$ 维流形，$\omega$ 是闭 $n$-形式（自动成立，因为 $\Omega^{n+1}(M) = 0$），则 $\int_M \omega$ 仅依赖于 $\omega$ 的上同调类。

## 五、应用与意义

Stokes 定理在数学和物理中有广泛应用：

1. **de Rham 上同调**：Stokes 定理是证明 de Rham 上同调是拓扑不变量的关键工具。它建立了积分映射 $H^k_{\text{dR}}(M) \to \mathbb{R}$ 的良定性。

2. **Hodge 理论**：Stokes 定理用于证明 Laplace 算子的自伴性和 Hodge 分解定理。

3. **守恒律**：在物理学中，Stokes 定理将局部守恒律（微分形式）与全局守恒量（边界积分）联系起来。

4. **电磁学**：Maxwell 方程的积分形式和微分形式通过 Stokes 定理等价。

5. **流体力学**：Kelvin 环流定理和涡量守恒通过 Stokes 定理表述。

6. **广义相对论**：Einstein-Hilbert 作用量的变分和边界项通过 Stokes 定理处理。

7. **几何测度论**：Stokes 定理推广到 rectifiable 流形和 currents 理论。

8. **指标定理**：Atiyah-Singer 指标定理的证明中，Stokes 定理用于处理流形边界上的贡献。

Stokes 定理的推广包括：带奇异性流形上的 Stokes 定理、currents 理论中的 Stokes 定理、以及非交换几何中的推广。
