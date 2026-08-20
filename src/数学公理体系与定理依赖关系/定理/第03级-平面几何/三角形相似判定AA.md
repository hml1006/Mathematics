# 三角形相似判定 AA

> **一句话大白话**：两个三角形只要两个角对应相等，第三个角自动也相等，它们就"形状相同"（相似），哪怕一大一小。
>
> **小例子**：三个角都是 $40^\circ,70^\circ,70^\circ$ 的两个三角形，看起来就是个它的小放大版，对应边成比例、面积成倍。

## 介绍

AA（Angle-Angle，角角）相似判定定理是三角形相似的基本判定定理：如果两个三角形的两个角分别对应相等，则这两个三角形相似。该定理是相似理论的核心，是证明比例线段、平行线性质、三角函数定义以及勾股定理等众多几何结论的基础。

## 分析

**前置依赖**：三角形内角和定理。

**定理内容**：在 $\triangle ABC$ 和 $\triangle DEF$ 中，若 $\angle A = \angle D$ 且 $\angle B = \angle E$，则 $\triangle ABC \sim \triangle DEF$。

**数学内涵**：
- 由三角形内角和定理，若两个角相等，则第三个角也必然相等，因此 AA 实际上等价于 AAA。
- 相似三角形的对应边成比例：$\frac{AB}{DE} = \frac{BC}{EF} = \frac{CA}{FD}$。
- 相似三角形在欧几里得几何中保持了"形状"不变，而大小可以不同——这是放缩变换（位似变换）的几何基础。

**证明策略**：
- 将 $\triangle ABC$ 通过放缩和旋转使 $\angle A$ 与 $\angle D$ 重合，然后利用平行线分线段成比例定理证明对应边成比例。
- 或利用三角函数定义（若角度相等，则对应三角函数值相等，从而边长成比例）。

## 思考过程

AA 相似判定的直观理解是：三角形的形状完全由它的角度决定。如果两个三角形的两个角相等，那么第三个角也必然相等，因此它们具有相同的"形状"（即角度相同），只是大小可能不同。这意味着一个三角形是另一个三角形的放大或缩小版本。

证明的思路是：将 $\triangle ABC$ 叠放到 $\triangle DEF$ 上，使 $\angle A$ 与 $\angle D$ 重合。由于 $\angle B = \angle E$，$BC$ 与 $EF$ 平行，从而由平行线分线段成比例定理可得对应边成比例。

## 证明过程

**定理**（AA 相似判定）：若两个三角形的两个角分别对应相等，则这两个三角形相似。

**证明**：

设 $\triangle ABC$ 和 $\triangle DEF$ 满足 $\angle A = \angle D$，$\angle B = \angle E$。

由三角形内角和定理，$\angle C = 180^\circ - \angle A - \angle B = 180^\circ - \angle D - \angle E = \angle F$，故三个角分别对应相等。

将 $\triangle ABC$ 平移旋转，使 $A$ 与 $D$ 重合，且 $AB$ 与 $DE$ 在同一条射线上。设 $B'$ 为 $AB$ 上的一点使得 $AB' = DE$，$C'$ 为 $AC$ 上的一点使得 $AC' = DF$。

由于 $\angle A = \angle D$，射线 $AC$ 与射线 $DF$ 重合，故 $C'$ 与 $F$ 重合（$AC' = DF$）。

现在，$\angle AB'C' = \angle ABC$（因为 $\angle ABC = \angle DEF$），且 $\angle AB'C'$ 与 $\angle ABC$ 是同位角，故 $B'C' \parallel BC$。

由平行线分线段成比例定理：

$$
\frac{AB'}{AB} = \frac{AC'}{AC} = \frac{B'C'}{BC}
$$

代入 $AB' = DE$，$AC' = DF$，$B'C' = EF$ 得：

$$
\frac{DE}{AB} = \frac{DF}{AC} = \frac{EF}{BC}
$$

即 $\frac{AB}{DE} = \frac{AC}{DF} = \frac{BC}{EF}$，故 $\triangle ABC \sim \triangle DEF$。$\square$

---

**推论**：若两个三角形相似，则对应边成比例，对应角相等，且面积比等于相似比的平方。