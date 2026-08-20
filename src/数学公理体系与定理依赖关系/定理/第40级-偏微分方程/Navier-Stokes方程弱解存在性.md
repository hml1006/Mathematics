# Navier-Stokes 方程弱解存在性

> **一句话大白话**：给不可压黏性流体的运动方程找一个"广义解"，即使真实解可能太粗糙、处处光滑性说不清，也能在弱意义下证明解存在且有界的能量——流体问题可以在温和框架下先有解再说光滑。
>
> **小例子**：Leray 在 1934 年证明，三维不可压 Navier-Stokes 方程对平方可积初速存在全局弱解，满足能量不等式 $\|u(t)\|_{L^2}^2+\nu\int_0^t\|\nabla u\|^2\le\|u_0\|_{L^2}^2$，但解的光滑唯一性至今未决。

## 一、定理介绍

Navier-Stokes 方程是描述粘性不可压缩流体运动的基本方程组。弱解存在性定理由 Jean Leray 于 1934 年首次证明，是偏微分方程理论中的里程碑结果。该定理证明了在三维空间中，Navier-Stokes 方程存在全局弱解（尽管强解的存在唯一性仍是千禧年难题之一）。

Leray 的弱解理论为流体力学提供了数学基础，开创了现代 PDE 弱解方法的研究，对后来的非线性偏微分方程理论产生了深远影响。

## 二、原理思路

**核心思想**：通过正则化、先验估计和紧性论证构造弱解。

**关键观察**：
1. Navier-Stokes 方程的非线性项 $(u \cdot \nabla)u$ 使得直接求解困难
2. 通过 Galerkin 逼近或正则化（如添加高阶耗散项）构造近似解
3. 能量估计提供一致有界性：$\frac{1}{2}\frac{d}{dt}\|u\|_{L^2}^2 + \nu\|\nabla u\|_{L^2}^2 = 0$
4. 利用紧性定理（如 Aubin-Lions 引理）从近似解中提取收敛子列
5. 弱极限满足弱形式的 Navier-Stokes 方程

**证明策略**：
- Galerkin 方法：在有限维子空间中求解
- 建立一致先验估计（能量不等式）
- 利用紧性论证取极限
- 验证极限满足弱形式

## 三、定理的严格表述

**Navier-Stokes 方程**：不可压缩粘性流体的运动方程为
$$\frac{\partial u}{\partial t} + (u \cdot \nabla)u - \nu \Delta u + \nabla p = f, \quad \nabla \cdot u = 0$$
其中 $u = u(x, t)$ 是速度场，$p = p(x, t)$ 是压力，$\nu > 0$ 是运动粘性系数，$f$ 是外力。

**定义（弱解）**：设 $\Omega \subset \mathbb{R}^3$ 是有界光滑区域，$T > 0$。向量场 $u \in L^\infty(0, T; L^2(\Omega)) \cap L^2(0, T; H^1_0(\Omega))$ 称为 Navier-Stokes 方程的**弱解**，如果：

1. **不可压缩条件**：$\nabla \cdot u = 0$（在分布意义下）

2. **弱形式**：对任意测试函数 $\varphi \in C^\infty_c([0, T) \times \Omega)$ 满足 $\nabla \cdot \varphi = 0$，
$$\int_0^T \int_\Omega \left[-u \cdot \frac{\partial \varphi}{\partial t} + (u \cdot \nabla)u \cdot \varphi + \nu \nabla u : \nabla \varphi\right] dx \, dt = \int_0^T \int_\Omega f \cdot \varphi \, dx \, dt + \int_\Omega u_0(x) \cdot \varphi(x, 0) \, dx$$

**定理（Leray-Hopf 弱解存在性）**：设 $\Omega \subset \mathbb{R}^3$ 是有界光滑区域（或 $\mathbb{R}^3$ 本身），$u_0 \in L^2(\Omega)$ 满足 $\nabla \cdot u_0 = 0$，$f \in L^2(0, T; H^{-1}(\Omega))$。则存在 Navier-Stokes 方程的弱解 $u$，满足：

1. **能量不等式**：对任意 $t \in [0, T]$，
$$\frac{1}{2}\|u(t)\|_{L^2}^2 + \nu \int_0^t \|\nabla u(s)\|_{L^2}^2 \, ds \leq \frac{1}{2}\|u_0\|_{L^2}^2 + \int_0^t \langle f(s), u(s) \rangle \, ds$$

2. **正则性**：$u \in L^\infty(0, T; L^2(\Omega)) \cap L^2(0, T; H^1(\Omega))$

3. **时间连续性**：$u \in C_w([0, T]; L^2(\Omega))$（弱连续）

**注**：弱解的唯一性和正则性在三维情形仍是开放问题（千禧年难题之一）。

## 四、证明过程

**证明**（Galerkin 方法）：

**步骤 1**：Galerkin 逼近。设 $\{w_k\}_{k=1}^\infty$ 是 Stokes 算子 $A = -P\Delta$（$P$ 是 Leray 投影到无散度场）的特征函数，构成 $L^2(\Omega)$ 的正交基和 $H^1_0(\Omega)$ 的基。

定义 $V_m = \text{span}\{w_1, \ldots, w_m\}$。寻找 $u_m(t) = \sum_{k=1}^m c_{mk}(t) w_k$ 满足
$$\left(\frac{du_m}{dt}, w_k\right) + \nu(\nabla u_m, \nabla w_k) + ((u_m \cdot \nabla)u_m, w_k) = (f, w_k), \quad k = 1, \ldots, m$$
初始条件 $u_m(0) = P_m u_0$（$P_m$ 是到 $V_m$ 的投影）。

这是一个常微分方程组，由 Cauchy-Lipschitz 定理，局部解存在。

**步骤 2**：先验估计。取 $w_k$ 的线性组合，测试函数为 $u_m$ 本身：
$$\frac{1}{2}\frac{d}{dt}\|u_m\|_{L^2}^2 + \nu\|\nabla u_m\|_{L^2}^2 = (f, u_m)$$
（注意 $((u_m \cdot \nabla)u_m, u_m) = 0$，因为 $\nabla \cdot u_m = 0$）

由 Poincaré 不等式和 Young 不等式，
$$(f, u_m) \leq \|f\|_{H^{-1}} \|u_m\|_{H^1} \leq \frac{1}{2\nu}\|f\|_{H^{-1}}^2 + \frac{\nu}{2}\|\nabla u_m\|_{L^2}^2$$

因此
$$\frac{d}{dt}\|u_m\|_{L^2}^2 + \nu\|\nabla u_m\|_{L^2}^2 \leq \frac{1}{\nu}\|f\|_{H^{-1}}^2$$

积分得
$$\|u_m(t)\|_{L^2}^2 + \nu\int_0^t \|\nabla u_m(s)\|_{L^2}^2 \, ds \leq \|u_m(0)\|_{L^2}^2 + \frac{1}{\nu}\int_0^t \|f(s)\|_{H^{-1}}^2 \, ds$$

由于 $\|u_m(0)\|_{L^2} \leq \|u_0\|_{L^2}$，这给出一致估计：
$$\{u_m\} \text{ 在 } L^\infty(0, T; L^2) \cap L^2(0, T; H^1) \text{ 中有界}$$

**步骤 3**：时间导数的估计。对任意 $v \in H^1_0(\Omega)$，$\|v\|_{H^1} \leq 1$，
$$\left|\left(\frac{du_m}{dt}, v\right)\right| \leq \nu\|\nabla u_m\|_{L^2} \|\nabla P_m v\|_{L^2} + |(u_m \cdot \nabla u_m, P_m v)| + \|f\|_{H^{-1}} \|P_m v\|_{H^1}$$

通过仔细估计（使用 Sobolev 嵌入和 Hölder 不等式），可以证明
$$\left\|\frac{du_m}{dt}\right\|_{L^{4/3}(0, T; H^{-1})} \leq C$$

**步骤 4**：紧性论证。由 Aubin-Lions 引理，$\{u_m\}$ 在 $L^2(0, T; L^2(\Omega))$ 中相对紧。因此存在子列（仍记为 $u_m$）和 $u \in L^2(0, T; L^2)$ 使得
$$u_m \to u \quad \text{强收敛于 } L^2(0, T; L^2)$$
$$u_m \rightharpoonup u \quad \text{弱收敛于 } L^2(0, T; H^1)$$
$$u_m \overset{*}{\rightharpoonup} u \quad \text{弱*收敛于 } L^\infty(0, T; L^2)$$

**步骤 5**：非线性项的收敛。由于 $u_m \to u$ 强收敛于 $L^2(0, T; L^2)$，且 $\{u_m\}$ 在 $L^2(0, T; H^1)$ 中有界，可以证明
$$(u_m \cdot \nabla)u_m \to (u \cdot \nabla)u \quad \text{在分布意义下}$$

**步骤 6**：取极限。在 Galerkin 方程中令 $m \to \infty$，得到 $u$ 满足弱形式的 Navier-Stokes 方程。

**步骤 7**：能量不等式。由弱下半连续性，
$$\|u(t)\|_{L^2}^2 \leq \liminf_{m \to \infty} \|u_m(t)\|_{L^2}^2$$
因此能量不等式成立。$\square$

## 五、应用与意义

Navier-Stokes 方程弱解理论在多个领域有重要应用：

1. **流体力学**：为不可压缩流体的数学理论奠定基础。

2. **数值分析**：有限元方法和谱方法的收敛性分析依赖弱解理论。

3. **湍流研究**：弱解的 non-uniqueness 可能与湍流的数学描述有关。

4. **最优控制**：流体控制问题的存在性分析使用弱解框架。

5. **几何流**：Ricci 流等几何演化方程的弱解理论受 Navier-Stokes 理论启发。

6. **正则性理论**：Leray 弱解的正则性研究推动了偏微分方程正则性理论的发展。

**开放问题**：

- **三维强解**：三维 Navier-Stokes 方程强解的全局存在性仍是千禧年难题（Clay 数学研究所百万美元悬赏问题）。
- **弱解唯一性**：三维弱解是否唯一未知。
- **部分正则性**：Caffarelli-Kohn-Nirenberg 定理证明了一维 Hausdorff 测度为零的奇点集。

相关理论包括：Leray-Hopf 弱解、非常数密度 Navier-Stokes 方程、可压缩 Navier-Stokes 方程（Lions 弱解）。
