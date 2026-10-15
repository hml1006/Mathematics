# 几何Langlands的范畴化

> **一句话大白话**：符号层面的几何 Langlands 对应可以被"升级"成一个关于范畴的范畴事实——把等式的两端再往上一层看成两个大范畴，并给出它们之间的函子与相容性。
>
> **小例子**：$\mathrm{D\text{-}mod}_{\mathrm{Bun}_G}$ 的结构（复合、对偶、无穷速度运算）被整体打包进一个 $(\infty,2)$-范畴表述，使对应可逐阶组合。

## 一、定理介绍

> **前置依赖**：∞-范畴与higher范畴论、D-模的∞-范畴化、IndCoh-拟凝聚层、Fourier-Mukai变换、Hecke算子堆

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

## 课堂问答

**老师**：范畴化到底把几何 Langlands"升"到了什么层次？请说明它"恢复"的是什么。

**学生**：先给结论：范畴化把两端的层范畴换成更大的高阶范畴之间的（伪）自然等价 $\mathrm{D\text{-}mod}_{\mathrm{Bun}_G}^{\mathrm{categ}}\simeq \mathrm{QCoh}_{\mathrm{LocSys}_{{}^LG}}^{\mathrm{categ}}$，使得 Hecke 本征层、Fourier–Mukai 核、组合与平移都被映射到对应的高阶对象；原来的 Beilinson–Drinfeld 等价是这个高阶等价"退化到零阶"的恢复。

**老师（追问）**：为什么要范畴化？零阶的等价已经不够用了吗？

**学生**：零阶只记录了"哪些层对应哪些层"，丢掉了 Hecke 算子的复合结构、平移函子与 Koszul 对偶等派生数据。范畴化把这些也一并编码，使"符号等价"被理解为两个高阶世界之间的函子性等价，从而能研究 Hecke 算子堆（$\infty$ 维结构）与主要算法的范畴。常见误区：以为范畴化只是"把东西换成 $\infty$-范畴"的语言游戏——它实际给出的是可在每一步组合、可做逆归约的严格结构。

**老师（拓展）**：证明范畴化用到哪些现代工具？它与 Fargues–Scholze 有什么关系？

**学生**：需要 $\mathrm{D\text{-}mod}$ 与 $\mathrm{QCoh}$ 的 $\infty$-范畴化模型（如 $\mathrm{DK}$/$\mathrm{IndCoh}$）、Hecke 堆与平移函子、Hecke 本征条件的 $\infty$-版本，并逐步验证各阶兼容性；Gaitsgory 路线把问题归约到 $\infty$-范畴化的核。它也是 Fargues–Scholze 框架的先声：在那里算术（$p$-adic）对应本身就以范畴/层的等价形式陈述，范畴化是必然的表述层级。
