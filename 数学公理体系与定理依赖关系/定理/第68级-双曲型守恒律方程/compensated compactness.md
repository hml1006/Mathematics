# compensated compactness

## 一、定理介绍

补偿紧性（compensated compactness）是处理非线性守恒律弱收敛解的一类重要工具，由 L. Tartar 与 F. Murat 在 1970 年代发展起来。其核心思想是：即使函数列本身仅弱收敛、乘积不保持极限，但若函数列满足某些相容的微分约束（如一个序列的散度紧、另一个序列的旋度紧），则它们的双线性型仍可弱收敛到极限的乘积。该理论在证明双曲守恒律弱解存在性、研究振荡与集中现象中具有不可替代的作用。

## 二、原理思路

经典紧性理论中，强收敛保证乘积收敛：若 $u_\varepsilon\to u$ 强，$v_\varepsilon\to v$ 强，则 $u_\varepsilon v_\varepsilon\to uv$。弱收敛则不一定。补偿紧性指出，若额外已知

- $\operatorname{div} U_\varepsilon$ 在 $H^{-1}$ 中紧，
- $\operatorname{curl} V_\varepsilon$ 在 $H^{-1}$ 中紧，

则内积 $U_\varepsilon\cdot V_\varepsilon$ 的弱极限等于 $U\cdot V$。对守恒律，状态变量与通量之间恰好满足散度–旋度结构，从而可利用 compensated compactness 把 Young 测度的支撑缩小，最终证明解的存在性。

## 三、定理的严格表述

### 3.1 Tartar–Murat div-curl 引理

设 $\Omega\subset\mathbb{R}^N$ 为有界开集，$U_\varepsilon,V_\varepsilon$ 为 $\mathbb{R}^N$ 值函数列，满足

$$
U_\varepsilon \rightharpoonup U,\qquad V_\varepsilon \rightharpoonup V
\quad \text{在 } L^2(\Omega;\mathbb{R}^N) \text{ 中弱收敛}.
$$

假设

$$
\operatorname{div} U_\varepsilon \text{ 在 } H^{-1}(\Omega) \text{ 中强收敛（或紧）},
$$

$$
\operatorname{curl} V_\varepsilon \text{ 在 } H^{-1}(\Omega) \text{ 中强收敛（或紧）},
$$

则

$$
U_\varepsilon\cdot V_\varepsilon \rightharpoonup U\cdot V
\quad \text{在分布意义下}.
$$

更一般地，若 $U_\varepsilon\cdot V_\varepsilon$ 在 $L^1$ 中有界，则该收敛在 $\mathcal{D}'(\Omega)$ 中成立。

### 3.2 Murat 引理

设 $u_\varepsilon$ 可分解为 $u_\varepsilon=v_\varepsilon^1-v_\varepsilon^2$，其中 $v_\varepsilon^1$ 在 $W^{-1,r}(\Omega)$ 中有界，$r>2$，$v_\varepsilon^2$ 在 $\mathcal{M}(\Omega)$（Radon 测度空间）中有界，并且 $u_\varepsilon$ 在 $W^{-1,p}(\Omega)$ 中有界，$p>2$，则 $u_\varepsilon$ 在 $H^{-1}_{\mathrm{loc}}(\Omega)$ 中紧。该引理常用于验证 div-curl 引理的前提条件。

### 3.3 Young 测度与 Tartar  commuting relations

设 $\nu_\varepsilon$ 满足守恒律 $\partial_t \nu_\varepsilon + \partial_x f(\nu_\varepsilon)=0$，并设 $\nu_\varepsilon$ 生成 Young 测度 $\{\nu_{(x,t)}\}_{(x,t)}$。若系统存在足够多的熵对 $(\eta_i,q_i)$，则可对 div-curl 引理应用于向量场

$$
U_\varepsilon^i = \bigl(q_i(\nu_\varepsilon),\,-\eta_i(\nu_\varepsilon)\bigr),
$$

得到关于 Young 测度的**交换关系**（commuting relations）：

$$
\big\langle \nu,\, q_i\eta_j - q_j\eta_i \big\rangle
= \big\langle \nu,\, q_i \big\rangle \big\langle \nu,\, \eta_j \big\rangle
- \big\langle \nu,\, q_j \big\rangle \big\langle \nu,\, \eta_i \big\rangle.
$$

在某些情况下，这些关系足以迫使 Young 测度为 Dirac 测度，从而 $\nu_\varepsilon$ 几乎处处收敛。

## 四、证明过程

### 4.1 div-curl 引理的证明思路

记 $U_\varepsilon=U+w_\varepsilon$，$V_\varepsilon=V+z_\varepsilon$，其中 $w_\varepsilon,z_\varepsilon\rightharpoonup 0$。只需证明 $w_\varepsilon\cdot z_\varepsilon\rightharpoonup 0$。利用 Hodge 分解，将 $w_\varepsilon$ 分解为梯度部分与散度自由部分：

$$
w_\varepsilon = \nabla p_\varepsilon + \operatorname{curl} A_\varepsilon.
$$

梯度部分与 $z_\varepsilon$ 的乘积可写成

$$
\nabla p_\varepsilon\cdot z_\varepsilon = \operatorname{div}(p_\varepsilon z_\varepsilon) - p_\varepsilon\,\operatorname{div} z_\varepsilon.
$$

由于 $\operatorname{div} z_\varepsilon$ 紧，$p_\varepsilon$ 弱收敛到 0，第二项趋于 0；第一项为散度形式，对试验函数分部积分后也趋于 0。旋度部分类似处理，利用 $\operatorname{curl} V_\varepsilon$ 紧的条件。

### 4.2 应用到守恒律

考虑标量守恒律或其 $2\times 2$ 系统。由方程可知 $(\nu_\varepsilon,f(\nu_\varepsilon))$ 的散度紧；若同时有某个熵对 $(\eta,q)$，则 $(q(\nu_\varepsilon),-\eta(\nu_\varepsilon))$ 的散度也紧。将这两个向量场分别取为 div-curl 引理中的 $U_\varepsilon$ 与 $V_\varepsilon$，便可得到熵等式在极限下成立。结合足够多的熵对，可推导 Young 测度的交换关系，最终证明其支集退化为单点。

## 五、应用与意义

补偿紧性为处理守恒律近似解的弱极限提供了系统方法，避免了直接获得强收敛的困难。它成功地应用于：

- 标量守恒律解的存在性与稳定性；
- 某些 $2\times 2$ 双曲系统（如等熵 Euler 方程）弱解的存在性；
- 弹性力学、相变模型中的 Young 测度刻画；
- 均匀化问题中振荡极限的精确描述。

补偿紧性理论深刻揭示了守恒律方程解的结构性信息，即使在不具备 BV 估计的情况下，也能通过微分约束恢复部分非线性紧性。
