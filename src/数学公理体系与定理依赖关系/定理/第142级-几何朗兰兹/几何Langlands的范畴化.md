# 几何Langlands的范畴化

> **一句话大白话**：符号层面的几何 Langlands 对应可以被"升级"成一个关于范畴的范畴事实——把等式的两端再往上一层看成两个大范畴，并给出它们之间的函子与相容性。
>
> **小例子**：$\mathrm{D\text{-}mod}_{\mathrm{Bun}_G}$ 的结构（复合、对偶、无穷速度运算）被整体打包进一个 $(\infty,2)$-范畴表述，使对应可逐阶组合。

## 一、定理介绍

几何Langlands的范畴化（categorification）把经典几何 Langlands 对应提升到更高范畴层次：原对应中的层范畴被视为某个大范畴（如 $(\infty,2)$-范畴或 $\mathcal{D}$-模的范畴化族）的对象，而等价被解释为这些大范畴之间的"函子性等价"，从而能捕捉更精细的结构（Hecke 算子堆、无穷速度函子、平移）。

## 二、原理思路

思路是"沿着箭头升级数学结构"：若符号等价 $A\cong B$ 说明两层范畴同构，则范畴化要求把 $A,B$ 分别放进更大的宇宙，使得原层的范畴成为它们的结构片段，等价被整合进一个更高阶的等价（$(\infty,k)$-函子）。这允许系统性研究 Hecke 算子组成的 $\infty$ 维结构与主要算法的范畴。

## 三、定理的严格表述（要点）

范畴化主张存在一个（伪）自然等价
$$
\mathrm{D\text{-}mod}_{\mathrm{Bun}_G}^{\mathrm{categ}}\;\simeq\;\mathrm{QCoh}_{\mathrm{LocSys}_{{}^LG}}^{\mathrm{categ}},
$$
使得各阶对象（Hecke 本征层、其 Fourier–Mukai 核、组合）被映射到对应高阶对象，并且原 Beilinson–Drinfeld 等价构成该高阶等价"退化到零阶"的恢复。其各阶一致性由适当的纤维范畴与模型范畴条件（如 $\mathrm{IndCoh}$、$\infty$-局部化）所描述。

## 四、证明过程

典型路线是：先建立 $\mathrm{D\text{-}mod}$ 与 $\mathrm{QCoh}$ 的 $\infty$-范畴化模型（如 $\mathrm{DK}$/$\mathrm{IndCoh}$），构造 Hecke 算子的高阶版本（Hecke 堆、平移函子），证明 Hecke 本征条件的 $\infty$-版本，并逐步验证各阶等价的兼容性。Gaitsgory 计划用归约到 $\infty$-范畴化核、结合 $p$-adic 对应与逆归约给出完整证明。

## 五、应用与意义

范畴化把几何 Langlands 从"两个空间的层等价"提升为"两个高阶世界的等价"，为研究 Hecke 特征、Koszul 对偶与派生结构提供统一语言。它也是 $p$-adic、算术几何与 Fargues–Scholze 框架（其中对应本身就是范畴化）的理论先声。