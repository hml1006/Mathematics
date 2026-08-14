# Riemann-Roch定理曲线

## 介绍

Riemann-Roch 定理是代数曲线理论中最核心的定理之一，由 Bernhard Riemann 在 1857 年提出雏形，后由 Gustav Roch 在 1865 年完善。该定理建立了代数曲线上除子的维数与曲线的亏格之间的精确关系，是连接代数几何、复分析和数论的重要桥梁。其现代形式通过层上同调表述，可以推广到高维代数簇（Hirzebruch-Riemann-Roch 定理和 Grothendieck-Riemann-Roch 定理）。

## 分析

**前置依赖**：代数曲线、除子、层、层上同调、Serre 对偶性。

**定理内容**：设 $C$ 是域 $k$ 上的光滑射影曲线，$K_C$ 是典范除子，$D$ 是 $C$ 上的任意除子，则
$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$
其中 $\ell(D) = \dim_k H^0(C, \mathcal{O}_C(D))$ 是除子 $D$ 的线性系的维数，$g = \dim_k H^1(C, \mathcal{O}_C)$ 是 $C$ 的亏格。

**数学内涵**：
- $\ell(D)$ 是 $D$ 的线性系的大小，即 $D$ 上有理函数空间的维数。
- $\ell(K_C - D)$ 是余维数修正项，可以视为 Serre 对偶性中的 $H^1$ 维数。
- 亏格 $g$ 是曲线的不变量，直观上表示曲线"洞"的个数。
- 若 $\deg D > 2g - 2$，则 $\ell(K_C - D) = 0$，从而 $\ell(D) = \deg D + 1 - g$。

**证明策略**：
1. 将除子 $D$ 对应到可逆层 $\mathcal{O}_C(D)$。
2. 利用层上同调将 $\ell(D)$ 和 $\ell(K_C - D)$ 表示为上同调维数。
3. 应用 Serre 对偶性 $H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \mathcal{O}_C(K_C - D))^\vee$。
4. 计算 Euler 示性数 $\chi(C, \mathcal{O}_C(D)) = \deg D + 1 - g$。

## 思考过程

Riemann-Roch 定理的深刻之处在于它统一了曲线的三个基本不变量：线性系维数、除子次数和亏格。从函数论的角度看，$\ell(D)$ 衡量了曲线上具有指定极点的有理函数空间的维数，而 $g$ 是曲线本身的内在拓扑不变量。

该定理的现代证明通过层上同调的语言实现，展示了代数几何中"几何-代数-同调"三位一体的思维方式。它是代数曲线分类理论的基础，也是通向高维代数几何的重要入口。

## 证明过程

**定理**（Riemann-Roch）：设 $C$ 是光滑射影曲线，$K_C$ 是典范除子，则对任意除子 $D$，
$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

**证明**：

### 1. 转化为层上同调

对除子 $D$，考虑可逆层 $\mathcal{O}_C(D)$。由定义：
$$\ell(D) = \dim_k H^0(C, \mathcal{O}_C(D))$$

由 Serre 对偶性：
$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \mathcal{O}_C(K_C - D))^\vee$$
故 $\dim_k H^1(C, \mathcal{O}_C(D)) = \ell(K_C - D)$。

### 2. Euler 示性数

定义 Euler 示性数：
$$\chi(C, \mathcal{O}_C(D)) = \dim_k H^0(C, \mathcal{O}_C(D)) - \dim_k H^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$$

### 3. 计算 $\chi(C, \mathcal{O}_C(D))$

对 $D = 0$（即 $\mathcal{O}_C$），有
$$\chi(C, \mathcal{O}_C) = 1 - g$$

对一般除子 $D$，考虑短正合序列：
$$0 \to \mathcal{O}_C \to \mathcal{O}_C(D) \to \mathcal{O}_D \to 0$$
其中 $\mathcal{O}_D$ 是 $D$ 上的结构层（支撑在 $D$ 的支点上）。取 Euler 示性数：
$$\chi(C, \mathcal{O}_C(D)) = \chi(C, \mathcal{O}_C) + \chi(C, \mathcal{O}_D)$$

而 $\chi(C, \mathcal{O}_D) = \dim_k H^0(C, \mathcal{O}_D) = \deg D$（因为 $\mathcal{O}_D$ 是 $D$ 上有限个点的结构层的直和，每个点贡献 1 维）。

因此：
$$\chi(C, \mathcal{O}_C(D)) = (1 - g) + \deg D = \deg D + 1 - g$$

### 4. 结论

由 $\chi(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$ 和 $\chi(C, \mathcal{O}_C(D)) = \deg D + 1 - g$，得证。$\square$

**推论**：若 $\deg D > 2g - 2$，则 $\ell(D) = \deg D + 1 - g$。

**证明**：当 $\deg D > 2g - 2$ 时，$\deg(K_C - D) = 2g - 2 - \deg D < 0$，故 $H^0(C, \mathcal{O}_C(K_C - D)) = 0$，即 $\ell(K_C - D) = 0$。$\square$