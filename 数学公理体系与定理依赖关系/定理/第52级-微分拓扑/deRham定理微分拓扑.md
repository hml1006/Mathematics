# de Rham 定理（微分拓扑）

## 一、定理介绍

de Rham 定理是微分拓扑和代数拓扑中的基本定理，由法国数学家 Georges de Rham 于 1931 年证明。该定理建立了微分形式的外导数上同调（de Rham 上同调）与奇异上同调之间的同构关系，揭示了微分几何与代数拓扑之间的深刻联系。

de Rham 定理表明，流形的拓扑信息可以通过微分形式来捕捉，这为使用分析工具研究拓扑问题提供了基础。

## 二、原理思路

de Rham 定理的核心思想包括：

1. **de Rham 上同调**：在光滑流形 $M$ 上，可以定义微分形式的外代数 $\Omega^*(M)$ 和外导数 $d$。由于 $d^2 = 0$，可以定义上同调群 $H^k_{dR}(M) = \ker(d: \Omega^k \to \Omega^{k+1}) / \text{im}(d: \Omega^{k-1} \to \Omega^k)$。

2. **奇异上同调**：从代数拓扑的角度，流形 $M$ 有奇异上同调群 $H^k(M; \mathbb{R})$，定义为奇异链复形的上同调。

3. **积分映射**：通过积分，可以定义从 de Rham 上同调到奇异上同调的映射：$[\omega] \mapsto (\sigma \mapsto \int_\sigma \omega)$。

4. **Mayer-Vietoris 序列**：证明的关键是使用 Mayer-Vietoris 序列和五引理，通过归纳论证建立同构。

5. **Poincaré 引理**：局部上，闭形式都是恰当形式，这是证明的基础。

## 三、定理的严格表述

**de Rham 定理**：设 $M$ 是光滑流形。则积分映射：
$$I: H^k_{dR}(M) \to H^k(M; \mathbb{R})$$
$$[\omega] \mapsto \left([\sigma] \mapsto \int_\sigma \omega\right)$$

是良定义的同构。

**等价表述**：
- de Rham 上同调群 $H^k_{dR}(M)$ 同构于奇异上同调群 $H^k(M; \mathbb{R})$
- 流形的微分形式上同调完全决定了它的实系数上同调

**de Rham 上同调的定义**：
- $\Omega^k(M)$：$M$ 上的光滑 $k$-形式空间
- $d: \Omega^k(M) \to \Omega^{k+1}(M)$：外导数
- $Z^k(M) = \ker(d: \Omega^k \to \Omega^{k+1})$：闭 $k$-形式空间
- $B^k(M) = \text{im}(d: \Omega^{k-1} \to \Omega^k)$：恰当 $k$-形式空间
- $H^k_{dR}(M) = Z^k(M) / B^k(M)$：第 $k$ 个 de Rham 上同调群

**奇异上同调的定义**：
- $S_k(M)$：$M$ 的奇异 $k$-链群（奇异单形的形式线性组合）
- $\partial: S_k(M) \to S_{k-1}(M)$：边界算子
- $S^k(M; \mathbb{R}) = \text{Hom}(S_k(M), \mathbb{R})$：奇异 $k$-上链群
- $\delta: S^k \to S^{k+1}$：上边缘算子
- $H^k(M; \mathbb{R}) = \ker(\delta) / \text{im}(\delta)$：第 $k$ 个奇异上同调群

**de Rham 定理的推论**：
- **Poincaré 对偶**：如果 $M$ 是紧定向 $n$ 维流形，则 $H^k_{dR}(M) \cong H^{n-k}_{dR}(M)^*$
- **Künneth 公式**：$H^*_{dR}(M \times N) \cong H^*_{dR}(M) \otimes H^*_{dR}(N)$
- **Mayer-Vietoris 序列**：de Rham 上同调满足 Mayer-Vietoris 长正合序列

## 四、证明过程

**步骤 1：良定义性**

首先证明积分映射 $I$ 是良定义的。

- **与代表元无关**：如果 $\omega' = \omega + d\eta$，则由 Stokes 定理：
$$\int_\sigma \omega' = \int_\sigma \omega + \int_\sigma d\eta = \int_\sigma \omega + \int_{\partial \sigma} \eta$$

如果 $\sigma$ 是闭链（$\partial \sigma = 0$），则 $\int_\sigma d\eta = 0$。因此 $I([\omega])$ 与闭形式的代表元选择无关。

- **与同调类无关**：如果 $\sigma' = \sigma + \partial \tau$，则：
$$\int_{\sigma'} \omega = \int_\sigma \omega + \int_{\partial \tau} \omega = \int_\sigma \omega + \int_\tau d\omega$$

如果 $\omega$ 是闭形式（$d\omega = 0$），则 $\int_{\partial \tau} \omega = 0$。因此 $I([\omega])$ 与同调类的代表元选择无关。

**步骤 2：Mayer-Vietoris 序列**

设 $M = U \cup V$，其中 $U, V$ 是开子集。定义：
- $i_U: U \hookrightarrow M$，$i_V: V \hookrightarrow M$：包含映射
- $j_U: U \cap V \hookrightarrow U$，$j_V: U \cap V \hookrightarrow V$：包含映射

de Rham 上同调的 Mayer-Vietoris 序列：
$$\cdots \to H^k_{dR}(M) \xrightarrow{(i_U^*, i_V^*)} H^k_{dR}(U) \oplus H^k_{dR}(V) \xrightarrow{j_U^* - j_V^*} H^k_{dR}(U \cap V) \xrightarrow{\delta} H^{k+1}_{dR}(M) \to \cdots$$

其中连接同态 $\delta$ 定义为：给定 $[\omega] \in H^k_{dR}(U \cap V)$，取单位分解 $\{\rho_U, \rho_V\}$ 从属于 $\{U, V\}$。则：
$$\delta([\omega]) = [d\rho_U \wedge \omega]$$

（在 $U$ 上 $d\rho_U \wedge \omega$ 可以延拓为零，在 $V$ 上类似）

奇异上同调也有类似的 Mayer-Vietoris 序列。

**步骤 3：积分映射与 Mayer-Vietoris 序列交换**

证明积分映射 $I$ 与 Mayer-Vietoris 序列中的映射交换：
$$\begin{array}{ccc}
H^k_{dR}(M) & \xrightarrow{\delta} & H^{k+1}_{dR}(U \cap V) \\
\downarrow I & & \downarrow I \\
H^k(M; \mathbb{R}) & \xrightarrow{\delta} & H^{k+1}(U \cap V; \mathbb{R})
\end{array}$$

这可以通过直接计算验证。

**步骤 4：五引理**

由交换图表和五引理，如果 $I$ 在 $U, V, U \cap V$ 上是同构，则在 $M$ 上也是同构。

**步骤 5：基础情形**

- **可收缩空间**：如果 $M$ 可收缩到一点（如 $\mathbb{R}^n$），则由 Poincaré 引理，$H^k_{dR}(M) = 0$（$k > 0$），$H^0_{dR}(M) = \mathbb{R}$。奇异上同调也有相同结果。因此 $I$ 是同构。

- **开集**：如果 $M$ 是 $\mathbb{R}^n$ 的开子集且可收缩，结论成立。

**步骤 6：归纳论证**

对于一般流形 $M$，取局部有限开覆盖 $\{U_i\}$，使得每个有限交 $U_{i_1} \cap \cdots \cap U_{i_k}$ 可收缩。

对覆盖的个数进行归纳。设 $M = U \cup V$，其中 $U$ 和 $V$ 是有限个可收缩开集的并，且 $U \cap V$ 也是。

由归纳假设，$I$ 在 $U, V, U \cap V$ 上是同构。由 Mayer-Vietoris 序列和五引理，$I$ 在 $M$ 上也是同构。

**步骤 7：非紧流形**

对于非紧流形，使用紧支集上同调或适当的极限论证。

**步骤 8：Poincaré 引理的证明**

Poincaré 引理：如果 $M$ 可收缩到一点，则 $H^k_{dR}(M) = 0$（$k > 0$）。

证明思路：设 $H: M \times [0, 1] \to M$ 是收缩同伦，$H(x, 0) = x$，$H(x, 1) = p$。

定义链同伦算子 $K: \Omega^k(M) \to \Omega^{k-1}(M)$：
$$K\omega = \int_0^1 H^*(\omega) dt$$

可以证明 $dK + Kd = \text{id} - H_1^*$，其中 $H_1(x) = H(x, 1) = p$。

如果 $\omega$ 是闭形式，则 $\omega = dK\omega + H_1^*\omega$。由于 $H_1^*\omega = 0$（$k > 0$），$\omega = dK\omega$ 是恰当的。

## 五、应用与意义

**理论意义**：
1. **微分几何与拓扑的桥梁**：de Rham 定理建立了微分几何（微分形式）与代数拓扑（上同调）之间的基本联系。

2. **计算工具**：de Rham 定理提供了计算上同调群的实用方法，因为微分形式比奇异链更容易操作。

3. **Hodge 理论的基础**：de Rham 定理是 Hodge 理论的基础，后者进一步将上同调类与调和形式联系起来。

**应用领域**：
1. **物理学**：在规范场论和广义相对论中，de Rham 上同调用于描述拓扑不变量。

2. **指标理论**：Atiyah-Singer 指标定理的证明依赖于 de Rham 定理。

3. **特征类理论**：Chern 类、Pontryagin 类等特征类可以通过微分形式（曲率形式）来表示。

4. **辛几何**：在辛几何中，de Rham 上同调用于研究辛流形的拓扑性质。

**具体应用实例**：
- **计算球面的上同调**：$H^k_{dR}(S^n) = \mathbb{R}$（$k = 0, n$），其他为零
- **计算环面的上同调**：$H^k_{dR}(T^n) = \mathbb{R}^{\binom{n}{k}}$
- **证明 Brouwer 不动点定理**：使用 de Rham 上同调

**推广与发展**：
- **de Rham 定理的层论版本**：使用层上同调可以推广到更一般的空间
- **等变 de Rham 定理**：考虑群作用下的 de Rham 上同调
- **非交换 de Rham 上同调**：在非交换几何中的推广
- **Hodge 分解定理**：在紧 Kähler 流形上，de Rham 上同调可以分解为调和形式
