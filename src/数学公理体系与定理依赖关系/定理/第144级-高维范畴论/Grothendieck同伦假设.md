# Grothendieck同伦假设

> **一句话大白话**：每个拓扑空间（或一般可缩的单形 SSet）的"形状"都可以被一个 $\infty$-群胚完全记住——这强有力地联系了拓扑与高阶范畴论。
>
> **小例子**：拟范畴中"同构"的对象组成可逆态射；Grothendieck假设把这种结构推广成：适当范畴（含 $\infty$-群胚）与同伦类型一一对应。

## 一、定理介绍

> **前置依赖**：$\infty$-群胚与同伦类型、基本无限群胚、Kan复形与单纯集合理论、CW复形范畴、Lurie的∞-范畴论框架

Grothendieck同伦假设（有时称 Grothendieck 的"$\infty$-群胚=同伦型"纲领）断言：**善良**的高阶范畴（满足某些有限同伦-可逆条件的 $(\infty,1)$-范畴，即 $\infty$-群胚）的幺半结构范畴等价于同伦类型的范畴——即每个 $\infty$-群胚实现为一个 $\infty$ 维被 homotopy 体型范畴，且这种实现为一对应。这巩固了"同伦类型"与"范畴对象"的等值。

## 二、原理思路

想法是把一个空间 $X$ 的"形状"完整编码进范畴：以 $X$ 的割为对象、以同伦映射为态射，得到 $\infty$-群胚 $\Pi_\infty X$；反过来给出每个 $\infty$-群胚一个纲领即其同伦实现。假设说明这两个方向的组合给出范畴等价。现代实现把 $\infty$-群胚等同于恰好（相当于切）homotopy 类型的 $\infty$-范畴，并研究其伴随与完整性。

## 三、定理的严格表述（主断）

对着适当的 $\infty$-群胚（即对象间态射均可逆、具 homotopy 提升条件的 $(\infty,1)$-范畴）定义其同伦实现 $\vert\ \cdot\ \vert: \infty\text{-Gpoid}\to\text{HTy}$ 与基本无限群胚 $\Pi_\infty:\text{HTy}\to\infty\text{-Gpoid}$，则它们给出范畴等价
$$
\infty\text{-Gpoids}\;\;\simeq\;\;\text{Homotopy Types},
$$
其中 homotopy 类型为"善良"的具体（如 CW 型）。

## 四、证明过程

在最为接受的框架（Lurie 等的 $\infty$-范畴论）中，论证分两部分：先建立 $\infty$-群胚与 homotopy 类型的伴随：$\Pi_\infty$ 与"同伦实现 $\vert\cdot\vert$"形成 adjunction；再证明对 CW 型空间该伴随限制为等价，即 $\vert\Pi_\infty X\vert\simeq X$ 且 $\Pi_\infty\vert C\vert\simeq C$。随后把一般情形逐步退化到合理模型。

## 五、应用与意义

同伦假设统一了拓扑、代数拓扑和高阶范畴论对"形态"的多种刻画，是 $\infty$-范畴论的基本愿景之一。它支撑了导出几何、稳定同伦与 Langlands 中"无穷形状"的形式化，其严格的现代形式（Lurie、Batanin 等）仍是活跃的研究前沿。