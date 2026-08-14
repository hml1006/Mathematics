# Grothendieck谱序列

## 介绍

Grothendieck谱序列（Grothendieck Spectral Sequence）是同调代数中导出函子复合的基本工具，由亚历山大·格罗滕迪克在其里程碑性的论文"同调代数中的一些论题"（Tôhoku 论文）中系统建立。该谱序列将两个函子的复合的导出函子与各函子导出函子的复合联系起来。具体地，对于左正合函子 $F: \mathcal{A} \to \mathcal{B}$ 和 $G: \mathcal{B} \to \mathcal{C}$，在一定条件下存在谱序列：
$$
E^{p,q}_2 = (R^p G)(R^q F)(A) \Rightarrow R^{p+q}(G \circ F)(A)
$$
Grothendieck谱序列在代数几何（如 Leray 谱序列）、层上同调和群上同调中具有核心地位。

## 分析

**前置依赖**：导出函子、谱序列、阿贝尔范畴、内射分解、正合函子。

**数学内涵**：

**定理条件**：设 $\mathcal{A}, \mathcal{B}, \mathcal{C}$ 是阿贝尔范畴，$F: \mathcal{A} \to \mathcal{B}$ 和 $G: \mathcal{B} \to \mathcal{C}$ 是左正合函子。若 $F$ 将内射对象映为 $G$-零调对象（即 $R^p G(F(I)) = 0$ 对 $p \ge 1$ 和所有内射 $I \in \mathcal{A}$），则对任意 $A \in \mathcal{A}$ 存在第一象限上同调谱序列：
$$
E^{p,q}_2 = (R^p G)(R^q F)(A) \Rightarrow R^{p+q}(G \circ F)(A)
$$

**数学内涵**：Grothendieck谱序列是导出函子"复合"的莱布尼茨法则，它揭示了函子复合的导出与导出函子复合之间的深层联系。

**证明策略**：取 $A$ 的内射分解 $A \to I^\bullet$，应用 $F$ 得到 $\mathcal{B}$ 中的复形，再取 $G$-零调分解构造双复形，应用双复形谱序列。

## 思考过程

Grothendieck谱序列的核心思想是：要计算 $G \circ F$ 的导出函子，一种方式是对 $A$ 取内射分解后直接应用 $G \circ F$；另一种方式是先应用 $F$，再取 $F(I^\bullet)$ 的 $G$-零调分解，然后应用 $G$。后者给出了一个双复形，其两种不同的计算方式分别给出 $E_2$ 页和收敛目标。

条件"$F$ 将内射映为 $G$-零调对象"保证了第一个方向的谱序列的 $E_2$ 页具有简洁形式。

常见的特例是：
- 若 $F$ 是正合函子，则 $R^q F = 0$ 对 $q \ge 1$，谱序列退化到 $R^p(G \circ F) \cong R^p G \circ F$。
- 若 $G$ 是正合函子，则 $R^p G = 0$ 对 $p \ge 1$，谱序列退化到 $R^q(G \circ F) \cong G \circ R^q F$。

## 证明过程

### 定理陈述

**定理**（Grothendieck谱序列）：设 $\mathcal{A}, \mathcal{B}, \mathcal{C}$ 是阿贝尔范畴，$F: \mathcal{A} \to \mathcal{B}$ 和 $G: \mathcal{B} \to \mathcal{C}$ 是左正合函子。假设 $F$ 将内射对象映为 $G$-零调对象（即对任意内射 $I \in \mathcal{A}$，$R^p G(F(I)) = 0$ 对所有 $p \ge 1$ 成立）。则对任意 $A \in \mathcal{A}$，存在第一象限上同调谱序列：
$$
E^{p,q}_2 = (R^p G)(R^q F)(A) \Rightarrow R^{p+q}(G \circ F)(A)
$$

### 证明

**步骤 1**：取内射分解。取 $A$ 的内射分解 $A \to I^\bullet$：
$$
0 \to A \to I^0 \to I^1 \to I^2 \to \cdots
$$
其中每个 $I^q$ 是 $\mathcal{A}$ 中的内射对象。

**步骤 2**：应用 $F$。对 $I^\bullet$ 逐项应用 $F$，得到 $\mathcal{B}$ 中的复形 $F(I^\bullet)$：
$$
0 \to F(I^0) \to F(I^1) \to F(I^2) \to \cdots
$$
由 $F$ 的左正合性，$H^0(F(I^\bullet)) \cong F(A)$，且 $H^q(F(I^\bullet)) \cong (R^q F)(A)$。

**步骤 3**：构造双复形。对每个 $F(I^q)$，取 $G$-零调分解 $F(I^q) \to J^{q,\bullet}$（即每个 $J^{q,p}$ 是 $G$-零调的）。这给出了双复形 $J^{\bullet,\bullet}$ 使得：
- 对每个固定的 $q$，$F(I^q) \to J^{q,\bullet}$ 是 $G$-零调分解
- 边映射 $J^{q,\bullet} \to J^{q+1,\bullet}$ 由 $F(I^q) \to F(I^{q+1})$ 诱导

**步骤 4**：应用谱序列。考虑总复形 $\operatorname{Tot}(J^{\bullet,\bullet})$ 的两种谱序列。

**第一谱序列**（先取列上同调）：
- $^I E^{p,q}_1 = H^p_q(J^{\bullet,\bullet})$ = $G$ 作用在 $J^{q,\bullet}$ 第 $q$ 行的第 $p$ 个上同调
- 由于 $J^{q,\bullet}$ 是 $F(I^q)$ 的 $G$-零调分解，$^I E^{p,q}_1 = 0$ 对 $p \ge 1$，且 $^I E^{0,q}_1 = G(F(I^q))$
- 因此 $^I E^{p,q}_2 = H^p(G(F(I^\bullet))) = H^p((G \circ F)(I^\bullet)) = (R^p(G \circ F))(A)$
- 该谱序列退化，给出 $H^n(\operatorname{Tot}(J^{\bullet,\bullet})) \cong (R^n(G \circ F))(A)$

**第二谱序列**（先取行上同调）：
- $^{II} E^{p,q}_1 = H^q_p(J^{\bullet,\bullet})$ = $J^{\bullet,p}$ 的第 $q$ 个上同调
- 由 $F(I^\bullet)$ 的构造，$^{II} E^{p,q}_1 \cong (R^q F)(A)$ 的 $G$-零调分解的第 $p$ 项
- 因此 $^{II} E^{p,q}_2 = (R^p G)((R^q F)(A))$

**步骤 5**：收敛性。两个谱序列收敛到同一个极限 $H^n(\operatorname{Tot}(J^{\bullet,\bullet}))$，故：
$$
E^{p,q}_2 = (R^p G)(R^q F)(A) \Rightarrow R^{p+q}(G \circ F)(A)
$$

$\square$

### 重要特例

**推论 1**（Leray 谱序列）：设 $f: X \to Y$ 是拓扑空间的连续映射，$\mathcal{F}$ 是 $X$ 上的阿贝尔群层，则存在谱序列：
$$
E^{p,q}_2 = H^p(Y; R^q f_* \mathcal{F}) \Rightarrow H^{p+q}(X; \mathcal{F})
$$

**推论 2**（群上同调的 Hochschild-Serre 谱序列）：设 $H \trianglelefteq G$ 是群的正规子群，$M$ 是 $G$-模，则存在谱序列：
$$
E^{p,q}_2 = H^p(G/H; H^q(H; M)) \Rightarrow H^{p+q}(G; M)
$$

**推论 3**（复合函子的谱序列推广）：Grothendieck谱序列是 Leray 谱序列、Hochschild-Serre 谱序列等众多谱序列的统一框架。

**应用**：Grothendieck谱序列是代数几何中层上同调理论的核心工具，也是群上同调和同调代数中导出函子复合的基本方法。$\square$