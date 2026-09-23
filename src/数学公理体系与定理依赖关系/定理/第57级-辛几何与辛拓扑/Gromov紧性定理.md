# Gromov 紧性定理

> **一句话大白话**：一列总能量有界的伪全纯曲线，在不损失能量的地方总能"收敛"；能量集中的地方会炸出新的曲线（气泡），把气泡和极限一起记下来，就得到紧致性——模空间的紧化就是把结点曲线添进来。
>
> **小例子**：$(\mathbb{CP}^{1},\omega_{FS})$ 中一列次数为 $1$ 的伪全纯球面在某点附近"塌缩"时，极限是一条退化曲线：一个常数曲面加上附着在其上的一个球（气泡），它仍代表原来的同调类。

## 一、定理介绍

> **前置依赖**：辛流形 $(M,\omega)$ 与相容近复结构 $J$、伪全纯曲线 $u:(\Sigma,j)\to(M,J)$（$\bar\partial_Ju=0$）、能量 $E(u)=\int u^{*}\omega$、单值化与 Deligne–Mumford 稳定曲线、Gromov 单调性引理与能量量子化、Gromov 可去奇点定理、Arzelà–Ascoli 与椭圆正则性（气泡分析）

Gromov 紧性定理（Gromov compactness theorem，1985 年由 Mikhael Gromov 在《Pseudo holomorphic curves in symplectic manifolds》中提出）是伪全纯曲线理论的基本定理。它断言：给定闭辛流形 $(M,\omega)$，一列**亏格固定、能量一致有界**的 $J$-全纯曲线（$J$ 在紧集上 $C^{\infty}$ 收敛），总可以抽取子列，在**重参数化**之后收敛到一条**稳定 $J$-全纯曲线**（允许出现结点与气泡，即 Gromov 极限）；收敛是"Gromov 意义"下的 $C^{\infty}_{\mathrm{loc}}$ 收敛，且保持同调类与能量（多余能量只可能以气泡形式出现）。

该定理是 Gromov–Witten 不变量、Floer 同调、辛拓扑（非挤压定理、辛容量）、以及辛场论（SFT）的基石。它使"曲线模空间"具有紧化 $\overline{\mathcal M}_{g,k}(M,J,A)$（稳定映射空间），从而可以对模空间计数与积分，定义 Gromov–Witten 不变量。

## 二、原理思路

紧性是三个独立机制的综合：

1. **能量量子化（没有无限多气泡）**：由 Gromov 单调性引理，任何经过定点的非平凡 $J$-全纯曲线在固定小球内的能量有统一正下界 $\hbar>0$；故总能量 $E\le C$ 的曲线至多含有 $\lfloor C/\hbar\rfloor$ 个"气泡"。这排除了无限多个集中点。

2. **梯度界（紧性在正规点成立）**：对伪全纯曲线有**平均值不等式（mean value inequality）**：若 $u$ 在圆盘上的能量有界，则 $|du|$ 在半径减半的圆盘上有一致界
$$\sup_{B_{r/2}}|du|\le\frac{C}{r}\left(\int_{B_r}u^{*}\omega\right)^{1/2}.$$
结合椭圆正则性（$\bar\partial_Ju=0$ 是椭圆方程），在有界能量下可对每个局部圆盘得到 $C^{\infty}$-界。

3. **气泡分析 + 可去奇点**：在能量集中点处，把区域按能量尺度重标定（rescaling），得到新的 $J$-全纯曲线（气泡），它们本身能满足同样的能量界，故可递归分解；在极限中被"丢掉"的点上，曲线在除去有限点后是 $C^{\infty}_{\mathrm{loc}}$-收敛的，而**Gromov 可去奇点定理**保证：有界的 $J$-全纯映射从穿孔圆盘可连续（甚至光滑）延拓，因此极限可补成一条定义在稳定曲线（带结点、带气泡）上的 $J$-全纯映射。

4. **定义域稳定化**：亏格固定、带 $k$ 个标记点的 Riemann 面序列在 Deligne–Mumford 空间 $\overline{\mathcal M}_{g,k}$ 中有紧化；必要时把"细脖子"收缩为结点，得到稳定曲线。

## 三、定理的严格表述

**（Gromov 紧性定理）** 设 $(M,\omega)$ 是闭辛流形，$J_k$ 是 $\omega$-相容的近复结构序列，在 $C^{\infty}$ 下收敛到相容近复结构 $J$。设 $u_k:(\Sigma_k,j_k)\to(M,J_k)$ 是一列 $J_k$-全纯曲线，满足：
- $\Sigma_k$ 是亏格为 $g$、带 $k$ 个标记点 $p_1^{(k)},\dots,p_k^{(k)}$ 的闭连通 Riemann 面（光滑情形）；
- **能量一致有界**：$\displaystyle E(u_k)=\int_{\Sigma_k}u_k^{*}\omega\le C<\infty$；
- 曲线在 $M$ 中不"整体塌缩"（例如固定一条可通过点 $x_0\in M$ 的要求，或固定同调类 $A\in H_2(M;\mathbb Z)$ 使 $\omega(A)\le C$）。

则存在子列（仍记为 $u_k$）与一条**稳定的 $J$-全纯曲线**（Gromov 极限）
$$\bigl((\Sigma_\infty,j_\infty,\{p_i\}),\ u_\infty:\Sigma_\infty\to M\bigr),$$
其中 $\Sigma_\infty$ 是稳定（带结点）曲线，$u_\infty$ 是 $J$-全纯的、与 $u_k$ 同调类相同，使得：
1. **Gromov 收敛**：在 $\Sigma_\infty$ 的非结点正则部分上（除去有限个点），$u_k$ 在 $C^{\infty}_{\mathrm{loc}}$ 意义下收敛到 $u_\infty$；
2. **能量守恒**：$\displaystyle E(u_k)\to E(u_\infty)$（多余能量在气泡中损失，而气泡被计入 $u_\infty$ 的像）；
3. **无能量丢失**：$\displaystyle E(u_\infty)=\int_{\Sigma_\infty}u_\infty^{*}\omega=\lim_k E(u_k)$。

**（同调表述）** 若 $A\in H_2(M;\mathbb Z)$ 使 $\omega(A)\le C$，则曲线模空间 $\overline{\mathcal M}_{g,k}(M,J,A)$（稳定映射的模空间）是紧的（在 Gromov 拓扑下）。

**（关键辅助定理）**
- **Gromov 单调性引理**：存在 $\hbar=\hbar(M,\omega,J,r)>0$，使任何经过 $p$ 的、具多重数 $m$ 的 $J$-全纯曲线满足 $\int_{u^{-1}(B_r(p))}u^{*}\omega\ge m\hbar$；
- **可去奇点定理**：若 $u:D\setminus\{0\}\to M$ 是 $J$-全纯且有界（像含于紧集），则 $u$ 可光滑延拓到 $D$；
- **平均值不等式**：如上，控制 $|du|$。

## 四、证明过程

**步骤 1：能量量子化——气泡数目有限。**

设曲线经过定点 $p$（或某固定区域的能量有下界）。由单调性引理，若 $u$ 在球 $B_{r}(p)$ 内的能量 $\int_{u^{-1}(B_r(p))}u^{*}\omega$ 非零，则它 $\ge\hbar>0$。把 $u$ 的能量按覆盖 $M$ 的有限个球分解，注意每个球的能量要么为 $0$ 要么 $\ge\hbar$，故总能量 $E(u)\le C$ 意味着**能量非零的球的数量**一致有界。特别地，任何能量集中点集的势一致有界；经过子列，集中点集收敛到有限个点。$\square$

**步骤 2：正规点处的 $C^{\infty}$-界（平均值不等式 + 椭圆正则性）。**

**引理（平均值不等式）**：存在常数 $C=C(M,\omega,J)$，使对任意 $J$-全纯 $u:B_r\to M$ 有
$$\sup_{B_{r/2}}|du|^{2}\le\frac{C}{r^{2}}\int_{B_r}u^{*}\omega.$$
*证明要点*：对 $J$-全纯映射，$u^{*}\omega=|du|^{2}_{\text{由}\ \omega\ \text{诱导的度量}}\,dx\wedge dy$（在局部实坐标 $z=x+iy$ 下，$\omega(\partial_xu,\partial_yu)$ 给出 $\tfrac12|du|^2$ 的度量因子，是逐点不等式，来自 $J$-相容性）；因此能量 $\int_{B_r}u^*\omega$ 控制 $|du|^{2}$ 的 $L^{1}$ 范数。再对 $|du|^{2}$ 的次调和性（$\Delta|du|^{2}\ge-C|du|^{2}$ 型 Bochner 型不等式）应用标准的次调和函数平均值不等式，得上述估计。$\square$

由步骤 2，在能量有界的区域上 $|du_k|$ 一致有界（取 $r$ 为上一步中保证能量下界之外的球）。再由 $\bar\partial_{J_k}u_k=0$ 是椭圆方程、$J_k\to J$ 于 $C^\infty$，标准的椭圆正则性（Schauder 估计）给出更高阶导数的一致界，从而由 Arzelà–Ascoli 得到 $C^{\infty}_{\mathrm{loc}}$-收敛的子列（在非集中点附近）。

**步骤 3：气泡分解与递归。**

设 $p_0\in\Sigma_\infty$ 是能量集中点（步骤 2 的估计在该点附近失效，即任意小球内能量都 $\ge\hbar$）。取重标定参数 $\epsilon_k\to0$（能量集中的尺度），定义
$$\tilde u_k(z)=u_k(p_0(\text{局部坐标})+\epsilon_k z)\quad\text{或}\quad \tilde u_k=\exp_{u_k(p_0)}^{-1}\circ u_k\ \text{重标定},$$
经适当的平移/缩放（在局部"近复结构"，把 $M$ 局部模型化为 $\mathbb C^n$），$\tilde u_k$ 的能量仍有界且收敛到一个非平凡的 $J$-全纯映射 $\tilde u_\infty:\mathbb C\to M$
（或 $\mathbb{CP}^{1}\to M$，由能量量子化与可去奇点把它紧化为球面）。这就是一个**气泡**。在原点处对原曲线作修改（把气泡"贴上"），重复步骤 1–2，得到有限层的气泡/结点结构。因能量每次至少减少 $\hbar$，气泡分解必在有限步终止。$\square$

**步骤 4：可去奇点——把极限补全。**

极限 $u_\infty$ 定义在穿孔的区域上。由构造，$u_\infty$ 有界（像含于紧集 $M$）；由 Gromov 可去奇点定理，有界的 $J$-全纯穿孔映射可光滑延拓，故 $u_\infty$ 实际上定义在整个紧化曲面（含结点）上。于是得到定义在稳定曲线上的 $J$-全纯映射 $u_\infty:\Sigma_\infty\to M$。$\square$

**步骤 5：定义域的稳定化与同调类。**

每个 $\Sigma_k$ 亏格 $g$、带 $k$ 个标记点，故其 $j_k$ 属于 Deligne–Mumford 空间 $\mathcal M_{g,k}$；由 $\overline{\mathcal M}_{g,k}$ 的紧性，可取子列使 $j_k$ 收敛到稳定曲线 $j_\infty$（必要时把退化环柄/细脖子缩为结点）。由步骤 3–4 的气泡分解与结点结构，$u_k$ 的像与同调类 $[u_k]\in H_2(M;\mathbb Z)$ 在极限中保持（气泡与结点都不改变总同调类）；由 $\omega(A)=\int u_k^{*}\omega=E(u_k)$ 与步骤 3 的能量守恒，得 $\int u_\infty^{*}\omega=\lim E(u_k)$，且 $[u_\infty]=[u_k]$（在子列意义下）。$\square$

**步骤 6：结论。**

综合步骤 1–5，存在子列在 Gromov 意义下收敛到稳定 $J$-全纯曲线，能量与同调类守恒，即 $\overline{\mathcal M}_{g,k}(M,J,A)$ 紧。$\square$

## 五、应用与意义

**理论意义**：
1. **曲线模空间紧化**：$\overline{\mathcal M}_{g,k}(M,J,A)$ 的紧性是 Gromov–Witten 不变量定义的前提（通过对模空间求虚拟基本类积分）。
2. **从局部到整体**：把"局部能量界 ⇒ 局部梯度界 ⇒ 全局紧性"的分析机制带入辛几何，是几何分析在辛拓扑中最有力的工具。
3. **刚性结果**：由紧性 + 不可约性/不可约存在性可推出辛嵌入的障碍（Gromov 非挤压定理）。

**应用领域**：
1. **Gromov–Witten 理论与计数几何**：枚举几何、镜像对称（Givental、Kontsevich 的 Witten 猜想证明）都以模空间紧性为基础。
2. **Floer 同调与 Arnold 猜测**：Floer 同调的不变性与 $\partial^2=0$ 依赖伪全纯条带的紧性/气泡分析。
3. **辛拓扑与辛容量**：Gromov 非挤压定理、辛容量、Lagrangian 嵌入障碍。
4. **辛场论与接触几何**：SFT 的紧性与全纯建筑的收敛（Hofer、Wysocki、Zehnder 的高维 SFT 紧性定理）推广了本定理。

**推广**：
- **带边界的紧性**：带 Lagrange 边界的伪全纯曲线、Floer 同调的紧性需要额外的边界分析（边界气泡）。
- **高亏格与相对 Gromov–Witten**：相对情形、orbifold 与对数辛几何中的紧性定理（Abramovich–Chen、Gross–Siebert 的对数 GW）。
- **SFT 的高维紧性**：把"能量有界 ⇒ 紧"推广到带柱端的辛流形（Hofer 能量取代 $\omega$-能量），是全纯建筑理论的核心。
