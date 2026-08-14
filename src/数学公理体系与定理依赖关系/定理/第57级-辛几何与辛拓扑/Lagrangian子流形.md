# Lagrangian 子流形

## 一、定理介绍

Lagrangian 子流形理论是辛几何的核心分支，由 Jean-Louis Koszul 和 André Lichnerowicz 在 20 世纪 50 年代引入，并由 Vladimir Arnold 在 60-80 年代发展为辛拓扑与经典力学的中心研究对象。

Lagrangian 子流形是辛流形中维数为辛流形一半、且辛形式在其上恒为零的子流形，是辛几何中"最大迷向"的子流形。Arnold 早就指出，Lagrangian 子流形是经典力学中相空间的自然几何对象（如位形空间的余切丛的零截面、生成函数给出的图等），它们的不变量与相交性质是辛拓扑研究的关键。

Lagrangian 子流形的理论包括 Weinstein 邻域定理、Lagrangian 相交的 Hamilton 不变性、Floer 同调的 Lagrangian 版本、Lagrangian 配边理论、displaceability 与 Lagrangian 容量等。它们在镜像对称的 Homological Mirror Symmetry 中作为镜像对象一侧的核心代数结构。

## 二、原理思路

Lagrangian 子流形理论的核心原理如下：

1. **极大迷向性**：辛流形 $(M^{2n}, \omega)$ 中，子流形 $L \subset M$ 是 Lagrangian 的条件为 $\dim L = n$ 且 $\omega|_L \equiv 0$。这等价于 $L$ 是极大迷向子流形：$T_xL = (T_xL)^{\omega}$（$\omega$-正交补）。

2. **余切丛的模型**：$T^*N$ 上的标准辛形式 $\omega = -d\lambda$（$\lambda$ 为 Liouville 形式）中，零截面 $N \subset T^*N$ 是 Lagrangian。Weinstein 邻域定理断言：每个 Lagrangian 子流形都局部辛同胚于余切丛的零截面，因此 Lagrangian 子流形在局部是平凡的。

3. **Hamilton 不变性与位移能量**：Lagrangian 子流形在 Hamilton 同胚下的相交数有下界（Arnold 猜想的 Lagrangian 版本），这是 Lagrangian Floer 同调的基础。Lagrangian 子流形的 displaceability（能否被 Hamilton 同胚移开自身）是辛拓扑中重要的问题。

4. **生成函数与微局部层论**：每个闭 Lagrangian 子流形局部可由生成函数表示，这是微局部分析与辛几何的接口。

5. **镜像对称的对象**：在 Homological Mirror Symmetry 中，辛流形的 Fukaya 范畴（以 Lagrangian 子流形为对象，Floer 同态为态射）与镜像代数流形的凝聚层导出范畴等价。

## 三、定理的严格表述

**定义（Lagrangian 子流形）**：设 $(M^{2n}, \omega)$ 是辛流形。嵌入子流形 $i: L \hookrightarrow M$ 称为 **Lagrangian 子流形**，若：
- $\dim L = n$；
- $i^*\omega = 0$（即 $\omega$ 在 $L$ 上恒为零）。

等价地，对任意 $x \in L$，$T_xL = (T_xL)^\omega$（$L$ 是极大 $\omega$-迷向的）。

**定理（Weinstein 邻域定理）**：设 $(M, \omega)$ 是辛流形，$L \subset M$ 是紧 Lagrangian 子流形。则存在 $L$ 在 $M$ 中的开邻域 $U$ 和余切丛 $T^*L$ 中零截面的开邻域 $V$，以及辛微分同胚
$$
\Phi: (U, \omega|_U) \to (V, \omega_{T^*L}),
$$
满足 $\Phi|_L = \mathrm{id}_L$（其中 $L$ 与 $T^*L$ 的零截面等同）。这里 $\omega_{T^*L} = -d\lambda$ 是 $T^*L$ 上的标准辛形式，$\lambda = \sum_i p_i \, dq^i$ 是 Liouville 形式。

**定理（Lagrangian 不等式 / Maslov 类约束）**：设 $L \subset (M, \omega)$ 是闭 Lagrangian 子流形，且 $\omega|_{\pi_2(M, L)} = 0$。则对任意光滑圆盘 $u: (D^2, \partial D^2) \to (M, L)$，其 Maslov 指标 $\mu(u) \in \mathbb{Z}$ 给出 Lagrangian 的 Maslov 类 $\mu_L \in H^1(L; \mathbb{Z})$。若 $L$ 是单调的（monotone），即存在 $\lambda > 0$ 使
$$
\int u^*\omega = \lambda \cdot \mu(u), \quad \forall u \in \pi_2(M, L),
$$
则 $L$ 的代数拓扑受到强烈约束。

**定理（Gromov 的 Lagrangian 不嵌入定理）**：在标准辛 $\mathbb{R}^{2n}$ 中，不存在闭（紧致无边界）Lagrangian 子流形的辛嵌入。即不存在紧 Lagrangian $L^n \subset (\mathbb{R}^{2n}, \omega_0)$。

**定理（Arnold-Lagrangian 相交猜想）**：设 $(M, \omega)$ 是紧辛流形，$L_0, L_1 \subset M$ 是两个闭 Lagrangian 子流形，且 $L_1 = \varphi(L_0)$ 是 $L_0$ 在某 Hamilton 同胚 $\varphi$ 下的像，$L_0 \pitchfork L_1$。则
$$
\#(L_0 \cap L_1) \geq \dim H_*(L_0; \mathbb{Z}_2).
$$
此即 Arnold 猜想的 Lagrangian 版本，由 Floer 在 $\pi_2(M, L) = 0$ 等假设下证明。

## 四、证明过程

**Weinstein 邻域定理的证明**：

**步骤 1：构造余切丛局部同构**

由于 $L$ 是 Lagrangian，$\omega$ 在 $L$ 处为零，且 $T_xL = (T_xL)^\omega$。考虑法丛 $NL = TM|_L / TL$。由 Lagrangian 条件，纤维 $N_xL \cong T_xL$（通过 $\omega$ 给出的 $TM/T_xL \to T_xL$ 的同构）。事实上 $NL \cong T^*L$（通过 $\omega$）。

**步骤 2：定义辛微分同胚**

在 $L$ 附近取坐标系，使 $L$ 对应零截面。利用 $\omega$ 在 $L$ 处为零与 $\omega$ 非退化，可定义 $U \subset T^*L$ 的开邻域与 $M$ 中 $L$ 的邻域之间的微分同胚 $\Phi$，使 $\Phi^*\omega_M = \omega_{T^*L}$。

**步骤 3：Moser 路径方法**

设 $\omega_t = (1-t)\omega_{T^*L} + t \Phi^*\omega_M$ 为 $L$ 零截面附近的辛形式路径。由于 $\omega_0 - \omega_1$ 在零截面处为零（辛形式在 Lagrangian 零截面处的限制一致），由 Poincaré 引理存在 1-形式 $\alpha$ 使 $d\alpha = \Phi^*\omega_M - \omega_{T^*L}$，且 $\alpha$ 在零截面上为零。

由 Moser 方程 $\iota_{X_t}\omega_t = -\alpha$ 解出 $X_t$，其流 $\varphi_t$ 满足 $\varphi_t^*\omega_t = \omega_0$。最终 $\varphi_1 \circ \Phi$ 即为所求辛微分同胚，且在 $L$ 上为恒等。$\square$

**Gromov Lagrangian 不嵌入定理的证明概要**：

设存在紧 Lagrangian $L \subset (\mathbb{R}^{2n}, \omega_0)$。由 Weinstein 邻域定理，$L$ 在 $\mathbb{R}^{2n}$ 中的邻域辛同胚于 $T^*L$ 中零截面的邻域。

**步骤 1：构造全纯圆盘**

在 $\mathbb{R}^{2n} = \mathbb{C}^n$ 上取标准复结构 $J_0$。对 $L$ 配以相容 $J$（在 $L$ 邻域与 $J_0$ 一致）。考虑从 $L$ 出发的 $J_0$-全纯圆盘 $u: (D^2, \partial D^2) \to (\mathbb{C}^n, L)$。

**步骤 2：模空间维数与存在性**

由 Gromov 紧性与指数定理，模空间 $\mathcal{M}(L)$ 的维数足够大，存在非平凡全纯圆盘 $u$。其能量
$$
E(u) = \int_{D^2} u^*\omega_0 > 0.
$$

**步骤 3：精确性矛盾**

由 $L \subset \mathbb{R}^{2n}$ 中 $\omega_0 = d\lambda_0$（$\lambda_0 = \sum_i x_i dy_i - y_i dx_i$ 之半，即 $d\lambda_0 = \omega_0$）。由 Stokes 定理
$$
E(u) = \int_{D^2} u^*\omega_0 = \int_{\partial D^2} u^*\lambda_0.
$$
由 $u(\partial D^2) \subset L$ 且 $L$ 是 Lagrangian，$\lambda_0|_L$ 闭。在 $\pi_1(L)$ 有限生成的情形下，能量受限于 $L$ 的拓扑。但模空间中能量趋于零的圆盘对应于常值映射，与 $u$ 非平凡矛盾。具体论证利用 $\omega_0$ 精确、$L$ 紧致得到 $\omega_0|_L = 0$ 使 $\lambda_0|_L$ 闭，且由 Stokes 公式得到圆盘面积由边界决定；通过 Gromov 紧性给出能量零极限序列，与拓扑约束矛盾。$\square$

**Arnold-Lagrangian 相交定理的证明概要（Floer）**：

设 $\pi_2(M, L) = 0$，$L_0$ 与 $L_1 = \varphi(L_0)$ 横截。定义 Lagrangian Floer 链复形：
$$
CF_k(L_0, L_1) = \bigoplus_{\substack{x \in L_0 \cap L_1 \\ \mu(x) = k}} \mathbb{Z}_2 \langle x \rangle,
$$
其中 $\mu(x)$ 由穿过 $L_0$ 与 $L_1$ 的路径的 Maslov 指标定义。边界算子由 Cauchy-Riemann 方程（带 Hamilton 项）的连接轨道模空间定义。由 Gromov 紧性与 $\partial^2 = 0$，得到 Lagrangian Floer 同调 $HF_*(L_0, L_1)$。

由 Hamilton 同痕下的不变性，$HF_*(L_0, L_1) \cong HF_*(L_0, L_0) \cong H_*(L_0; \mathbb{Z}_2)$。后一同构由 $L_0$ 与自身微小形变的极限（PSS 同构或 Morse 退化）得到。

由链复形秩不等式：
$$
\#(L_0 \cap L_1) = \dim CF_*(L_0, L_1) \geq \dim HF_*(L_0, L_1) = \dim H_*(L_0; \mathbb{Z}_2).
$$
$\square$

## 五、应用与意义

**理论意义**：
1. **辛拓扑的核心对象**：Lagrangian 子流形是辛流形中最自然的子流形，其分类与相交性质是辛拓扑的基本问题。

2. **镜像对称的几何侧**：Fukaya 范畴以 Lagrangian 子流形为对象，是 Homological Mirror Symmetry 的核心。Lagrangian 子流形的代数结构反映了辛流形的几何信息。

3. **经典力学的几何化**：Lagrangian 子流形是经典力学中不变环面、作用量-角变量、Hamilton-Jacobi 理论的几何载体。

**应用领域**：
1. **Hamilton 动力学**：Lagrangian 不变环面（KAM 理论）保证近可积系统的拟周期运动；Arnold-Lagrangian 相交定理给出 Hamilton 同胚下不动点的下界。

2. **镜像对称**：Fukaya 范畴的 Lagrangian 子流形是镜像对称的核心研究对象，Lagrangian Floer 同调计算是验证镜像对称的工具。

3. **辛配边与切触几何**：Lagrangian 子流形的配边与 Legendrian 子流形紧密相关，是切触拓扑的研究对象。

4. **辛嵌入与容量**：Lagrangian 子流形的 displaceability 与 displacement energy 给出辛流形的容量信息。

**重要结果与开问题**：
- **Arnold 猜想（Lagrangian 版）**：在合适假设下已由 Floer 证明；
- **Gromov 不嵌入定理**：$\mathbb{R}^{2n}$ 中不存在闭 Lagrangian；
- **Audin 猜想**：每个 Lagrangian 嵌入到 $\mathbb{C}^n$ 的 Maslov 类非零；
- **Lagrangian 设想（Arnold 4-问题）**：辛拓扑中 Lagrangian 子流形的拓扑限制问题，至今仍是活跃研究主题。
