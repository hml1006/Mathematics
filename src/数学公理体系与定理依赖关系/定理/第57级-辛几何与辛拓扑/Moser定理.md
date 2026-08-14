# Moser 定理

## 一、定理介绍

Moser 定理是辛几何的基础结果，由 Jürgen Moser 于 1965 年证明。它断言：在紧流形上，若一族辛形式 $\omega_t$ 在 de Rham 上同调中保持同调类不变（即 $\frac{d}{dt}\omega_t = d\sigma_t$），则存在依赖于 $t$ 的微分同胚族 $\varphi_t$ 使得 $\varphi_t^*\omega_t = \omega_0$。换言之，**同调于常数的辛形式是辛同胚等价的**。

Moser 定理的深刻意义在于：在辛几何中，辛形式的局部几何完全由其上同调类决定。这与 Riemann 几何形成鲜明对比——Riemann 度量的局部不变量（曲率）连续变化，而辛形式在固定上同调类中是"刚性"的，没有局部模空间。

Moser 定理是 Darboux 定理、辛同痕定理、相对 Darboux 定理等众多结果的基础工具，被广泛称为"Moser 路径方法"（Moser's path method），是微分几何中的基本技巧。

## 二、原理思路

Moser 定理的核心思路如下：

1. **路径方法**：将辛形式 $\omega_0$ 与 $\omega_1$ 用光滑路径 $\omega_t$ 连接。若路径在上同调层面是平凡的（$[\omega_t] = [\omega_0]$ 对所有 $t$），那么 $\frac{d\omega_t}{dt}$ 是恰当的，即 $\frac{d\omega_t}{dt} = d\sigma_t$。

2. **构造向量场**：希望找到 $X_t$ 使其流 $\varphi_t$ 满足 $\varphi_t^*\omega_t = \omega_0$。微分此式得
$$
0 = \frac{d}{dt}\varphi_t^*\omega_t = \varphi_t^*(\mathcal{L}_{X_t}\omega_t + d\omega_t/dt),
$$
即需 $\mathcal{L}_{X_t}\omega_t + d\sigma_t = 0$。

3. **Cartan 公式与非退化**：由 Cartan 公式 $\mathcal{L}_{X_t}\omega_t = d(\iota_{X_t}\omega_t) + \iota_{X_t}d\omega_t = d(\iota_{X_t}\omega_t)$（由 $d\omega_t = 0$），故只需
$$
d(\iota_{X_t}\omega_t + \sigma_t) = 0.
$$
更严格地，若能取 $\iota_{X_t}\omega_t = -\sigma_t$，则方程满足。

4. **辛形式的非退化**：$\omega_t$ 非退化保证 $\omega_t: T_xM \to T_x^*M$ 是同构，因此 $X_t = -\omega_t^{-1}\sigma_t$ 唯一存在。

5. **整体存在性**：紧流形上向量场 $X_t$ 整体存在，其流 $\varphi_t$ 在 $t \in [0, 1]$ 上整体定义，给出 $\varphi_1^*\omega_1 = \omega_0$。

## 三、定理的严格表述

**定理（Moser 定理——辛形式稳定性）**：设 $M$ 是闭光滑流形，$\{\omega_t\}_{t \in [0, 1]}$ 是 $M$ 上一族光滑依赖 $t$ 的辛形式。假设其上同调类不依赖于 $t$：
$$
[\omega_t] \in H^2(M; \mathbb{R}) \text{ 与 } t \text{ 无关},
$$
等价地 $\frac{d\omega_t}{dt} = d\sigma_t$ 对某族 1-形式 $\sigma_t$ 成立。则存在光滑依赖 $t$ 的微分同胚族 $\varphi_t: M \to M$，满足 $\varphi_0 = \mathrm{id}_M$ 且
$$
\varphi_t^*\omega_t = \omega_0, \quad \forall t \in [0, 1].
$$

**推论 1（同调于常数的辛形式等价）**：若 $\omega_0$ 与 $\omega_1$ 是 $M$ 上辛形式且 $[\omega_0] = [\omega_1] \in H^2(M; \mathbb{R})$，且存在连接它们的辛形式路径 $\omega_t$，则存在微分同胚 $\varphi: M \to M$ 使 $\varphi^*\omega_1 = \omega_0$。

**推论 2（Moser 相对定理）**：设在闭子流形 $N \subset M$（如一点、Lagrangian 子流形）上 $\omega_0|_N = \omega_1|_N$ 且在 $N$ 的邻域内同伦相等，则可选取 $\varphi$ 使 $\varphi|_N = \mathrm{id}_N$。

**定理（Moser 定理——非紧情形）**：若 $M$ 非紧但 $X_t$ 有紧支集（$\sigma_t$ 在 $M$ 的紧子集外为零），则结论同样成立。

## 四、证明过程

**步骤 1：路径的上同调条件**

由假设 $[\omega_t] = [\omega_0]$ 对所有 $t$，故 $\frac{d\omega_t}{dt}$ 闭且上同调为零。因此存在 1-形式族 $\sigma_t$ 使得
$$
\frac{d\omega_t}{dt} = d\sigma_t, \quad t \in [0, 1].
$$
（在闭流形上由 de Rham 定理直接给出。）

**步骤 2：构造向量场 $X_t$**

由 $\omega_t$ 非退化，映射 $\omega_t^\flat: T_xM \to T_x^*M$，$X \mapsto \iota_X\omega_t$ 是同构。定义 $X_t \in \mathfrak{X}(M)$ 为
$$
\iota_{X_t}\omega_t = -\sigma_t.
$$
即 $X_t = -\omega_t^{-1}\sigma_t$（用 $\omega_t$ 把 1-形式 $\sigma_t$ 转化为向量场）。$X_t$ 光滑依赖 $t$。

**步骤 3：流的局部存在性**

由常微分方程理论，对每个 $x \in M$，方程
$$
\frac{d}{dt}\varphi_t(x) = X_t(\varphi_t(x)), \quad \varphi_0(x) = x
$$
在某个区间 $(-\varepsilon, \varepsilon)$ 上有唯一解。

**步骤 4：整体存在性**

由于 $M$ 紧致，$X_t$ 整体有界，流 $\varphi_t$ 在 $t \in [0, 1]$ 上整体存在，定义微分同胚 $\varphi_t: M \to M$。

**步骤 5：验证 $\varphi_t^*\omega_t = \omega_0$**

计算 $\frac{d}{dt}\varphi_t^*\omega_t$：
$$
\frac{d}{dt}\varphi_t^*\omega_t = \varphi_t^*\left(\mathcal{L}_{X_t}\omega_t + \frac{d\omega_t}{dt}\right).
$$

由 Cartan 魔法公式 $\mathcal{L}_{X_t}\omega_t = d(\iota_{X_t}\omega_t) + \iota_{X_t}(d\omega_t)$，结合 $d\omega_t = 0$（$\omega_t$ 是辛形式，闭）：
$$
\mathcal{L}_{X_t}\omega_t = d(\iota_{X_t}\omega_t) = d(-\sigma_t) = -d\sigma_t.
$$

由假设 $\frac{d\omega_t}{dt} = d\sigma_t$，故
$$
\mathcal{L}_{X_t}\omega_t + \frac{d\omega_t}{dt} = -d\sigma_t + d\sigma_t = 0.
$$

因此 $\frac{d}{dt}\varphi_t^*\omega_t = 0$，从而 $\varphi_t^*\omega_t$ 与 $t$ 无关。代入 $t = 0$：
$$
\varphi_t^*\omega_t = \varphi_0^*\omega_0 = \omega_0, \quad \forall t \in [0, 1].
$$

特别地 $\varphi_1^*\omega_1 = \omega_0$。$\square$

**步骤 6：相对版本（Moser 相对定理）**

设在子流形 $N \subset M$ 上 $\omega_0|_N = \omega_1|_N$，且在 $N$ 邻域内存在辛形式路径 $\omega_t$ 与 $\sigma_t$ 使 $\sigma_t|_N = 0$。则由 $X_t = -\omega_t^{-1}\sigma_t$ 与 $\sigma_t|_N = 0$，得 $X_t|_N = 0$，故 $\varphi_t|_N = \mathrm{id}_N$。

**步骤 7：非紧情形**

若 $M$ 非紧，且 $\sigma_t$ 在 $M$ 的某紧子集外为零，则 $X_t$ 也有紧支集，其流整体存在（紧支集向量场的流在 $\mathbb{R}$ 上整体定义）。结论同样成立。$\square$

**注**：若不假设紧支集，非紧情形可能由于向量场在无限远处"逃逸"而失效。

## 五、应用与意义

**理论意义**：
1. **辛形式的同调刚性**：Moser 定理表明辛形式在固定上同调类中是辛同胚等价的，辛几何的"模空间"在闭流形上是离散的——这就是辛流形的同调类（凸锥 $\subset H^2(M; \mathbb{R})$）。这与 Riemann 度量有无限维模空间形成鲜明对比。

2. **Darboux 定理的基础**：Darboux 定理的 Moser 证明正是 Moser 路径方法的局部应用，将局部辛形式同化为标准形。

3. **辛同痕定理**：Moser 定理给出辛形式的等价判定——两个辛形式辛同胚等价的必要条件是上同调类相同。在低维（$\dim \leq 4$）这常也是充分条件，对其他情形则受 Gromov 非挤压等约束。

4. **基本工具**：Moser 路径方法已推广到许多其他几何结构（Kähler 结构、Poisson 结构、接触结构等）的稳定性问题。

**应用领域**：
1. **辛流形分类**：Moser 定理是闭辛流形按辛形式分类的起点，结合 Gromov 非挤压等辛刚性现象，给出辛流形的精细分类。

2. **Lagrangian 邻域定理**：Weinstein 邻域定理的证明基于 Moser 路径方法，将 Lagrangian 子流形附近的辛结构同化为余切丛的标准辛形式。

3. **Kähler 流形的稳定性**：Moser 定理用于证明 Kähler 度量在固定 Kähler 类中的稳定性，并推广到 Kähler-Ricci 流的分析。

4. **接触几何的稳定性**：Gray 定理（接触结构的同伦稳定性）是 Moser 路径方法在接触几何的类比，表明同伦的接触结构是同痕等价的。

5. **Hamilton 同胚的生成**：Moser 方程 $\iota_{X_t}\omega = dH$ 给出 Hamilton 向量场的定义，是 Hamilton 力学的几何基础。

**重要变体**：
- **相对 Moser 定理**：保持子流形不动的辛同胚，用于 Darboux 定理与 Weinstein 邻域定理；
- **局部 Moser 定理**：在一点的邻域上将辛形式同化，给出 Darboux 坐标；
- **Moser 同痕定理**：辛形式的连续族给出辛同胚的连续族，用于参数化辛结构的研究；
- ** Thurston 的辛结构构造**：基于 Moser 的同调刚性，构造具有给定上同调类的辛结构。

Moser 定理以其简洁而深刻的内容，成为现代辛几何、Kähler 几何与微分拓扑的基本工具，是 20 世纪微分几何的代表性成果之一。
