# 三角形全等判定 ASA

> **一句话大白话**：两个三角形"两角夹同一条边"都一样，那它们就一模一样（全等）——因为角的形状一定，夹边一定，整个三角形就被钉死了。
>
> **小例子**：$\triangle ABC$ 与 $\triangle DEF$ 中若 $\angle A=\angle D$、$AB=DE$、$\angle B=\angle E$，则 $\triangle ABC\cong\triangle DEF$。

## 介绍

ASA（Angle-Side-Angle，角边角）全等判定定理是三角形全等的基本判定定理之一：如果两个三角形的两角及其夹边分别对应相等，则这两个三角形全等。ASA 判定定理可以由 SAS 公理和三角形内角和定理推导出来，它是全等三角形判定中常用的方法之一。

## 分析

**前置依赖**：合同公理、三角形内角和定理。

**定理内容**：在 $\triangle ABC$ 和 $\triangle DEF$ 中，若 $\angle A = \angle D$，$AB = DE$，$\angle B = \angle E$，则 $\triangle ABC \cong \triangle DEF$。

**数学内涵**：
- ASA 判定等价于：给定一条边和两个相邻角，三角形唯一确定。
- 由三角形内角和定理，AAS（两角及其中一角的对边对应相等）也是全等的充分条件，因为两角相等意味着第三角也相等，从而转化为 ASA。
- ASA 判定是测量学中的重要工具——通过测量一条基线（已知边）和两个角度，可以确定一个三角形的形状。

**证明策略**：
- 由三角形内角和定理，两角相等推出第三角相等，从而转化为 SAS 或直接用叠合法证明。

## 思考过程

ASA 判定的证明可以从 SAS 公理出发。如果两个三角形有两角相等，由三角形内角和为 $180^\circ$，第三角也必然相等。因此我们实际上有"两角及其夹边"对应相等，结合"第三角相等"的信息，我们可以用 SAS 来证明全等。

具体来说，在 $\triangle ABC$ 和 $\triangle DEF$ 中，已知 $\angle A = \angle D$，$AB = DE$，$\angle B = \angle E$。由三角形内角和定理，$\angle C = 180^\circ - \angle A - \angle B = 180^\circ - \angle D - \angle E = \angle F$。因此我们有 $\angle A = \angle D$，$AB = DE$，$\angle C = \angle F$，这实际上是 ASA 的一个变体，可以直接用叠合法证明。

## 证明过程

**定理**（ASA 全等判定）：若两个三角形的两角及其夹边分别对应相等，则这两个三角形全等。

**证明**：

设 $\triangle ABC$ 和 $\triangle DEF$ 满足 $\angle A = \angle D$，$AB = DE$，$\angle B = \angle E$。

由三角形内角和定理：

$$
\angle C = 180^\circ - \angle A - \angle B = 180^\circ - \angle D - \angle E = \angle F
$$

因此 $\angle C = \angle F$。

现在，将 $\triangle ABC$ 平移旋转，使 $A$ 与 $D$ 重合，$B$ 与 $E$ 重合（由于 $AB = DE$）。

由于 $\angle A = \angle D$，射线 $AC$ 与射线 $DF$ 重合。由于 $\angle B = \angle E$，射线 $BC$ 与射线 $EF$ 重合。因此 $AC$ 与 $DF$ 的交点 $C$ 与 $F$ 重合。

故 $\triangle ABC \cong \triangle DEF$。$\square$

---

**推论**（AAS 判定）：若两个三角形的两角及其中一角的对边分别对应相等，则这两个三角形全等。这是因为两角相等推出第三角相等，从而转化为 ASA 情形。

**证明**：设 $\angle A = \angle D$，$\angle B = \angle E$，$BC = EF$。由内角和定理得 $\angle C = \angle F$。于是 $\angle B = \angle E$，$BC = EF$，$\angle C = \angle F$，由 ASA 得 $\triangle ABC \cong \triangle DEF$。$\square$

## 课堂问答

**老师**：ASA 判定说的是什么？它是公理还是定理？

**学生**：结论：若 $\angle A=\angle D$、$AB=DE$、$\angle B=\angle E$，则 $\triangle ABC\cong\triangle DEF$。它是定理而非公理，可由 SAS 合同公理结合三角形内角和定理推出。

**老师（追问）**：怎么把"两角夹边"转成能用 SAS 或叠合法的形式？

**学生**：由内角和 $\angle C=180^\circ-\angle A-\angle B=180^\circ-\angle D-\angle E=\angle F$，于是三对角全部相等。再用叠合法：平移旋转使 $A$ 与 $D$、$B$ 与 $E$ 重合，$\angle A=\angle D$ 迫使射线 $AC$ 与 $DF$ 重合，$\angle B=\angle E$ 迫使射线 $BC$ 与 $EF$ 重合，交点 $C$ 与 $F$ 必重合。别把 AAS 当成新公理，它靠"两角相等推出第三角相等"化归为 ASA。

**老师（拓展）**：测量中怎么用这条判定？

**学生**：给定一条基线（已知边）与它两端的视角，三角形被唯一确定，这正是三角测量中确定远处目标距离的原理。
