# Morrey-Kohn-Hörmander 恒等式

> **一句话大白话**：把 $\bar\partial u$ 与 $\bar\partial^*u$ 的 $L^2$ 范数平方加起来，可以通过分部积分被"拆开"成一个全导数项（可控制）、一个权重（度规）曲率项和一个边界 Levi 形式项——只要这两项非负，就得到 $\bar\partial$-Neumann 问题的基本估计。
>
> **小例子**：取 $\Omega=\{z\in\mathbb C:|z|<1\}$（$n=1$）、$\phi=0$、$u=f\,d\bar z$ 且满足边界条件。恒等式退化为 $\|\bar\partial u\|^2+\|\bar\partial^*u\|^2=\sum_k\|\partial u/\partial\bar z_k\|^2+\oint_{\partial\Omega}|f|^2\,ds$，右端非负直接给出估计。

## 一、定理介绍

> **前置依赖**：$\bar\partial$ 算子与 $(0,q)$-形式、加权 $L^2$ 内积 $\langle u,v\rangle_\phi=\int u\bar v\,e^{-\phi}$、$\bar\partial^{*}_{\phi}$ 的显式表达式与 $\bar\partial$-Neumann 边界条件、定义函数 $\rho$ 与 Levi 形式、分部积分（Stokes 定理）、多次调和函数（plurisubharmonic）与拟凸域

Morrey–Kohn–Hörmander 恒等式（Kohn–Morrey–Hörmander formula，20 世纪 60 年代由 Kohn、Morrey、Hörmander 分别独立获得）是 $\bar\partial$-Neumann 问题的核心恒等式。它把 $(0,1)$-形式的 $\bar\partial$ 与其加权伴随 $\bar\partial^{*}_{\phi}$ 的 $L^2$ 范数平方之和，精确地分解为三项：
$$\int_\Omega|\bar\partial u|^{2}e^{-\phi}+\int_\Omega|\bar\partial^{*}_{\phi}u|^{2}e^{-\phi}
=\underbrace{\sum_{j,k}\int_\Omega\frac{\partial^{2}\phi}{\partial z_j\partial\bar z_k}\,u_j\bar u_k\,e^{-\phi}}_{\text{权重曲率项}}
+\underbrace{\sum_{j,k}\int_\Omega\left|\frac{\partial u_j}{\partial\bar z_k}\right|^{2}e^{-\phi}}_{\text{全导数项}}
+\underbrace{\sum_{j,k}\int_{\partial\Omega}\frac{\partial^{2}\rho}{\partial z_j\partial\bar z_k}\,u_j\bar u_k\,\frac{e^{-\phi}\,dS}{|\nabla\rho|}}_{\text{边界 Levi 形式项}}.$$

其中 $\rho$ 是 $\Omega=\{\rho<0\}$ 的定义函数，$u$ 须满足 $\bar\partial$-Neumann 边界条件 $\sum_j u_j\,\partial\rho/\partial\bar z_j\big|_{\partial\Omega}=0$。

该恒等式的威力在于：若 $\phi$ 多次调和（权重曲率项 $\ge0$）且 $\Omega$ 拟凸（边界 Levi 形式项 $\ge0$），则右端第一、三项自动非负，只剩全导数项，于是
$$\|\bar\partial u\|^{2}_{\phi}+\|\bar\partial^{*}_{\phi}u\|^{2}_{\phi}\ \ge\ \sum_{j,k}\left\|\frac{\partial u_j}{\partial\bar z_k}\right\|^{2}_{\phi},$$
这就是 $\bar\partial$-Neumann 问题的**基本估计**，由此可证明 Neumann 算子 $N$ 的有界性与 $\bar\partial$ 的 $L^2$ 可解性（Hörmander $L^2$ 存在定理），也是 Kohn 亚椭圆估计、Ohsawa–Takegoshi 延拓定理、乘子理想层理论的出发点。

## 二、原理思路

恒等式是一个**分部积分（integration by parts）的结果**，其推导可以概括为：

1. **展开**：把 $|\bar\partial u|^{2}$ 展开为 $\sum_{j,k}|\bar\partial_k u_j|^{2}-\sum_{j,k}\bar\partial_k u_j\overline{\bar\partial_j u_k}$（这里 $\bar\partial_k=\partial/\partial\bar z_k$），把 $|\bar\partial^{*}_{\phi}u|^{2}$ 用 $\bar\partial^{*}_{\phi}$ 的显式式
$$\bar\partial^{*}_{\phi}u=-\sum_{j}\left(\frac{\partial u_j}{\partial z_j}-\frac{\partial\phi}{\partial z_j}u_j\right)$$
展开。

2. **把 $\partial/\partial z_k$ 分部积分掉**：交叉项中含 $\partial/\partial z_k$ 的部分通过 Stokes 定理转移为对 $e^{-\phi}$ 的导数（$\partial_k e^{-\phi}=-\phi_k e^{-\phi}$，其中 $\phi_k=\partial\phi/\partial z_k$），产生 $\phi$ 的一阶、二阶导数项与边界项。

3. **合并得到三项**：$\phi$ 的二阶导项合并为权重曲率项 $\sum\phi_{j\bar k}u_j\bar u_k$；剩余的主部（对 $\bar z_k$ 的全导数）成为全导数项 $\sum|\bar\partial_k u_j|^{2}$；边界项在 $\bar\partial$-Neumann 条件 $\sum_j u_j\bar\partial_j\rho=0$ 下化为 Levi 形式的边界积分。

4. **取估计**：在拟凸 + 多次调和假设下丢弃非负项。

## 三、定理的严格表述

**（Morrey–Kohn–Hörmander 恒等式）** 设 $\Omega=\{\rho<0\}\Subset\mathbb C^{n}$ 是有 $C^{2}$ 边界的有界区域，$\rho$ 为定义函数，$\phi\in C^{2}(\overline\Omega)$ 为实值权重。设 $u=\sum_{j=1}^{n}u_j\,d\bar z_j$ 是 $(0,1)$-形式，在 $\overline\Omega$ 上 $C^{1}$ 且满足 $\bar\partial$-Neumann 边界条件
$$\sum_{j=1}^{n}u_j\,\frac{\partial\rho}{\partial\bar z_j}\bigg|_{\partial\Omega}=0.$$
以 $\bar\partial^{*}_{\phi}$ 记 $\bar\partial$ 关于加权 $L^{2}$ 内积 $\langle u,v\rangle_{\phi}=\int_\Omega u\bar v\,e^{-\phi}$ 的伴随。则
$$\int_\Omega|\bar\partial u|^{2}e^{-\phi}+\int_\Omega|\bar\partial^{*}_{\phi}u|^{2}e^{-\phi}
=\sum_{j,k}\int_\Omega\frac{\partial^{2}\phi}{\partial z_j\partial\bar z_k}u_j\bar u_k\,e^{-\phi}
+\sum_{j,k}\int_\Omega\left|\frac{\partial u_j}{\partial\bar z_k}\right|^{2}e^{-\phi}
+\sum_{j,k}\int_{\partial\Omega}\frac{\partial^{2}\rho}{\partial z_j\partial\bar z_k}u_j\bar u_k\,\frac{e^{-\phi}\,dS}{|\nabla\rho|}.$$

**（基本估计）** 若 $\phi$ 多次调和（即在 $\Omega$ 上 $\bigl(\partial^{2}\phi/\partial z_j\partial\bar z_k\bigr)\ge0$）且 $\Omega$ 拟凸（即边界 Levi 形式 $\bigl(\partial^{2}\rho/\partial z_j\partial\bar z_k\bigr)\big|_{\partial\Omega}$ 在复切空间上 $\ge0$），则对一切满足 Neumann 边界条件的 $u$ 有
$$\int_\Omega|\bar\partial u|^{2}e^{-\phi}+\int_\Omega|\bar\partial^{*}_{\phi}u|^{2}e^{-\phi}\ \ge\ \sum_{j,k}\int_\Omega\left|\frac{\partial u_j}{\partial\bar z_k}\right|^{2}e^{-\phi}.$$

**（推论：$\bar\partial$-Neumann 算子的存在性与可解性）** 在基本估计下，$\bar\partial\oplus\bar\partial^{*}_{\phi}$ 的像闭、$\Box_{\phi}=\bar\partial\bar\partial^{*}_{\phi}+\bar\partial^{*}_{\phi}\bar\partial$ 有有界逆 $N_{\phi}$（Neumann 算子）；从而对任意 $\bar\partial$-闭的 $f\in L^{2}_{(0,1)}(\Omega,\phi)$，方程
$$\bar\partial v=f$$
有解 $v\in L^{2}_{(0,0)}(\Omega,\phi)$，且 $\|v\|^{2}_{\phi}\le C\|\bar\partial^{*}_{\phi}N_{\phi}f\|^{2}_{\phi}$ 型估计成立（Hörmander $L^{2}$ 存在定理）。

**（严格拟凸情形）** 若 Levi 形式在边界上一致正定（严格拟凸），把边界项与全导数项结合还可得到亚椭圆估计 $\|u\|^{2}_{s+\frac12}\lesssim\|\bar\partial u\|_{s}^{2}+\|\bar\partial^{*}u\|^{2}_{s}$（Kohn）。

## 四、证明过程

**步骤 1：$\bar\partial$ 与 $\bar\partial^{*}_{\phi}$ 的显式表达式。**

记 $\partial_j=\partial/\partial z_j$，$\bar\partial_j=\partial/\partial\bar z_j=\partial_{\bar j}$，$\phi_j=\partial_j\phi$。对 $u=\sum_j u_j\,d\bar z_j$，
$$\bar\partial u=\sum_{j<k}\bigl(\bar\partial_k u_j-\bar\partial_j u_k\bigr)\,d\bar z_j\wedge d\bar z_k.$$
关于 $\bar\partial^{*}_{\phi}$：由 $\langle\bar\partial v,u\rangle_{\phi}=\langle v,\bar\partial^{*}_{\phi}u\rangle_{\phi}$ 与分部积分（对 $(0,0)$-形式 $v$），可算得
$$\bar\partial^{*}_{\phi}u=-\sum_{j=1}^{n}\bigl(\partial_j u_j-\phi_j u_j\bigr)=-\sum_{j=1}^{n}e^{\phi}\,\partial_j\bigl(e^{-\phi}u_j\bigr).$$
其定义域由分部积分产生的边界项为零确定，即 $\bar\partial$-Neumann 边界条件 $\sum_j u_j\,\bar\partial_j\rho\big|_{\partial\Omega}=0$。

**步骤 2：展开两项的模长。**

由 $\bar\partial u=\sum_{j<k}(\bar\partial_k u_j-\bar\partial_j u_k)\,d\bar z_j\wedge d\bar z_k$，
$$|\bar\partial u|^{2}=\sum_{j,k}\bigl|\bar\partial_k u_j\bigr|^{2}-\sum_{j,k}\bar\partial_k u_j\,\overline{\bar\partial_j u_k}.$$
（展开 $\sum_{j<k}|a_k-a_j|^{2}$ 并合并同类项。）另一方面
$$|\bar\partial^{*}_{\phi}u|^{2}=\sum_{j,k}\bigl(\partial_j u_j-\phi_j u_j\bigr)\overline{\bigl(\partial_k u_k-\phi_k u_k\bigr)}.$$

**步骤 3：分部积分——把 $\partial_j$ 转移掉。**

对含 $\partial_j u_j$ 的项，用
$$\int_\Omega \partial_j u_j\;\overline{\,\cdot\,}\;e^{-\phi}=-\int_\Omega u_j\,\partial_j\bigl(\overline{\,\cdot\,}\,e^{-\phi}\bigr)+\text{(边界项)}$$
（由 $\int_\Omega\partial_j\bigl(u_j\overline{\,\cdot\,}e^{-\phi}\bigr)=0$ 的实部与 Stokes 定理）。具体地，把 $|\bar\partial u|^{2}+|\bar\partial^{*}_{\phi}u|^{2}$ 乘 $e^{-\phi}$ 并对 $\Omega$ 积分，逐步把所有对 $z_j$ 的导数从 $u_j$ 上"移走"，得到：

- 来自 $\phi_j\overline{\phi_k}$ 与交叉项的贡献：在 $\bar\partial$ 与 $\bar\partial^{*}_{\phi}$ 的交换子中产生
$$[\bar\partial^{*}_{\phi},\bar\partial_k]\ \text{型（曲率）项}\ \Longrightarrow\ \sum_{j,k}\phi_{j\bar k}\,u_j\bar u_k,\qquad \phi_{j\bar k}=\frac{\partial^{2}\phi}{\partial z_j\partial\bar z_k}.$$
这一步的关键是 $\partial_j$ 与 $\bar\partial_k$ 可交换（$[\partial_j,\bar\partial_k]=0$），故 $\phi$ 的一阶导项相消，只剩二阶导（曲率）项。

- 来自 $\sum_{j,k}\bar\partial_k u_j\,\overline{\bar\partial_k u_j}=\sum_{j,k}|\bar\partial_k u_j|^{2}$：这是未被转移的部分，即全导数项。
- 来自 $|\bar\partial u|^{2}$ 的交叉项 $\sum_{j,k}\bar\partial_k u_j\overline{\bar\partial_j u_k}$：与 $\bar\partial^{*}_{\phi}$ 展开中的相应项相消（同型项合并时系数抵消，这是主项能留下 $\sum_{j,k}|\bar\partial_k u_j|^{2}$ 而不再是 $|\bar\partial u|^{2}$ 的原因）。

**步骤 4：边界项的化简。**

步骤 3 的分部积分在 $\partial\Omega$ 上留下边界积分。用 $\rho$ 的梯度作面积元 $\dfrac{dS}{|\nabla\rho|}$，并以 $\bar\partial_j\rho$ 表示法向对偶，可得边界项为
$$\sum_{j,k}\int_{\partial\Omega}\frac{\partial^{2}\rho}{\partial z_j\partial\bar z_k}u_j\bar u_k\,\frac{e^{-\phi}\,dS}{|\nabla\rho|}+\text{（与}\ \bar\partial\text{-Neumann 条件成正比的项）}.$$
由 $u$ 满足 $\sum_j u_j\,\bar\partial_j\rho\big|_{\partial\Omega}=0$，法向分量为零，剩余的边界项恰为 Levi 形式的积分（上式第一项）。这一步用到 $\rho$ 与 $\bar\partial$ 在对 $\partial\Omega$ 的切方向上的一致性：将 $u$ 分解为法向（已消失）与切向分量，Levi 形式作用在切向复切空间上。

**步骤 5：合并得恒等式。**

把步骤 2–4 的结果相加，即得
$$\int_\Omega|\bar\partial u|^{2}e^{-\phi}+\int_\Omega|\bar\partial^{*}_{\phi}u|^{2}e^{-\phi}
=\sum_{j,k}\int_\Omega\phi_{j\bar k}u_j\bar u_k\,e^{-\phi}
+\sum_{j,k}\int_\Omega|\bar\partial_k u_j|^{2}e^{-\phi}
+\sum_{j,k}\int_{\partial\Omega}\frac{\partial^{2}\rho}{\partial z_j\partial\bar z_k}u_j\bar u_k\frac{e^{-\phi}dS}{|\nabla\rho|}. \square$$

**步骤 6：取基本估计与推出可解性。**

若 $\phi$ 多次调和，则矩阵 $(\phi_{j\bar k})\ge0$，故 $\sum_{j,k}\phi_{j\bar k}u_j\bar u_k\ge0$。若 $\Omega$ 拟凸，则边界 Levi 形式在复切空间上 $\ge0$，故边界项（与法向已消失后剩余的切向部分）$\ge0$。于是恒等式右端 $\ge\sum_{j,k}\int|\bar\partial_k u_j|^{2}e^{-\phi}$，即基本估计。

由基本估计：对正交分解 $u=u_{1}+u_{2}$（$u_1\in\ker\bar\partial$，$u_2\in(\ker\bar\partial)^{\perp}\subset\ker\bar\partial^{*}_{\phi}$），可证 $\|\bar\partial u_2\|^{2}$ 控制 $\|u_2\|^{2}$（Poincaré 型不等式），从而 $\bar\partial$ 在 $(\ker\bar\partial)^{\perp}$ 上有有界逆，得到 $\Box_{\phi}$ 的有界逆 $N_{\phi}$ 及 $\bar\partial v=f$ 的 $L^{2}$ 解。特别地，取 $\phi=|z|^{2}$ 或更一般的多次调和权即得 Hörmander $L^{2}$ 存在定理。$\square$

## 五、应用与意义

**理论意义**：
1. **$\bar\partial$-Neumann 问题的基础恒等式**：它把算子 $\Box=\bar\partial\bar\partial^{*}+\bar\partial^{*}\bar\partial$ 的分析性质（基本估计、亚椭圆性）与区域的凸性、权重的多次调和性定量联系起来。
2. **正性与几何**：恒等式把"$\bar\partial$ 的 $L^{2}$ 几何"归结为两个曲率量的正性——权重 $\phi$ 的复 Hessian 与边界的 Levi 形式，这是复几何中"正性 ⇒ 消没"的典型机制。
3. **$L^{2}$ 方法与层论的互补**：给出 Dolbeault 上同调消没的非层论证明，且对无光滑边界的拟凸域也有效。

**应用领域**：
1. **Hörmander $L^{2}$ 存在定理**：以 $\phi$ 为权重的 $L^{2}$ 可解性，是乘子理想层、$L^{2}$ 延拓与 $L^{2}$ 上同调消没（Andreotti–Vesentini 定理的 $L^{2}$ 版本）的技术核心。
2. **Ohsawa–Takegoshi $L^{2}$ 延拓定理**：其证明使用**扭化**（twisted）版本的恒等式（把 $\phi$ 换成 $\phi-\log\eta$），是复几何与代数几何（乘子理想、Birkar–Cascini–Hacon–McKernan、Siu 的方法）中的关键工具。
3. **Kohn 亚椭圆估计**：严格拟凸域上的 $\bar\partial$-Neumann 算子亚椭圆性、正则性理论（Kohn–Nirenberg、Catlin、D'Angelo 型）都建立在恒等式之上。
4. **CR 几何与 $\bar\partial_b$**：在边界上的对应恒等式（Kohn–Morrey–Hörmander on the boundary）给出 Szegő 投影与复 Green 算子的估计。

**推广**：
- **$(0,q)$-形式的恒等式**：对 $q>1$ 有相应的恒等式，曲率项中出现 $q$ 个 Levi 特征值的和，正是"$q$-凸性"与弱 $q$-凸性的来源。
- **向量丛取值与度量联络**：把 $u$ 换成取值于 Hermite 向量丛的 $(0,q)$-形式，权重曲率项换成联络的曲率（Chern 曲率）作用在取值空间上，得到 Bochner–Kodaira–Nakano 型恒等式。
- **流形与完备情形**：在完备 Kähler 流形与紧复流形上有相应的 $L^{2}$ 恒等式（Demailly 的 $L^{2}$ 估计框架），是现代复几何的标准工具。
