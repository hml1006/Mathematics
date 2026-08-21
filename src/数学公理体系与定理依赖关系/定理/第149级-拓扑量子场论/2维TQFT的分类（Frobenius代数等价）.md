# 2维TQFT的分类（Frobenius代数等价）
>
> **一句话大白话**：二维定向 TQFT 与交换 Frobenius 代数一一对应——"把流形当拼图，其赋值就是代数结构"。
>
> **小例子**：对 TQFT $Z:\mathrm{Cob}_2^{\mathrm{or}}\to\mathrm{Vect}$，$A=Z(S^1)$ 是交换 Frobenius 代数：乘法来自"裤子"曲面，迹来自"帽子"。

## 一、定理介绍

> **前置依赖**：cobordism范畴、对称幺半函子、Frobenius代数、二维曲面Morse分解、拓扑粘贴不变性

二维定向 TQFT 的分类定理（Atiyah；Dijkgraaf；Lazarov 等完备化）断言：存在范畴等价
$$
\operatorname{2TQFT}^{\mathrm{or}}\;\cong\;\operatorname{CommFrobAlg},
$$
即每个二维定向 TQFT $Z:\mathrm{Cob}_2^{\mathrm{or}}\to\mathrm{Vect}_{\mathbb C}$ 确定一个交换 Frobenius 代数 $A=Z(S^1)$（同 $Z(D)$ 的 $-{e}$ 迹），反之每个交换 Frobenius 代数给出唯一 TQFT。这是 TQFT 最经典且完整的分类结果。

## 二、原理思路

识别的关键是二维曲面的"手术/分解引理"：任何二维定向闭曲面可由圆盘、裤子（pair of pants）与圆柱（帽）粘合而成，而 TQFT 把"S与帽"赋予代数结构。于是定义 $A=Z(S^1)$，乘法 $m=Z(\text{裤子}):A\otimes A\to A$、单位 $u=Z(\text{圆盘}):\mathbb C\to A$、迹 $\varepsilon=Z(\text{帽}):A\to\mathbb C$，Frobenius 关系由曲面上的拓扑恒等（割/拼）保证。

## 三、定理的严格表述

存在二维定向 cobordism 范畴等价：
$$
\operatorname{2TQFT}^{\mathrm{or}}:=\operatorname{SymMonFun}(\mathrm{Cob}_2^{\mathrm{or}},\operatorname{Vect}_{\mathbb C})\;\cong\;\operatorname{CommFrobAlg}_{\mathbb C}.
$$
方向（→）：$Z\mapsto A=Z(S^1)$ 配乘法 $m=Z(P)$（$P$ 裤子）、单位 $Z(D)$、迹 $\varepsilon=Z(\bar D)$，满足交换/结合/Frobenius 关系。逆方向：从交换 Frobenius 代数按穿衣的 $Z$ 拼装。两者互逆。

## 四、证明过程

先证"TQFT⇒Frobenius"：用曲片分解将图形映成道路算子并汇集四元组结构（乘法、单位、余积、迹），Frobenius 关系由曲面图上合法的割/并恒等导出（如帽子+裤子可重组）。再证"Frobenius⇒TQFT"：利用二维曲面的 Morse 分解—每个闭曲面可化为多种基本片段的组合—并按 Frobenius 代数求值；验证井井有条（粘贴不变），得唯一 TQFT。

## 五、应用与意义

该分类给出了最朴素 TQFT 的完整代数模型，是超对称、《复数》编辑、弦论（视觉 Schyori）与模张量范畴（更高维/扩展情形）的范式；它揭示范畴与流形赋值的即时联系，是沿 Atiyah 公理深入 TQFT 第一站。