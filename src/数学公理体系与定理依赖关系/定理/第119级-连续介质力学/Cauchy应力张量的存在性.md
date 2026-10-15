# Cauchy应力张量的存在性

> **一句话大白话**：物体内部任意一个小面上的力，都可以用一个“统一矩阵”（应力张量）乘以这个面的法向算出来，不用为每个方向各存一套力。
>
> **小例子**：压一块豆腐，不管从哪个角度切开去看内部，那个切面上的力都能由同一个应力张量 $\boldsymbol\sigma$ 按 $\boldsymbol t=\boldsymbol\sigma\cdot\boldsymbol n$ 算出。

## 一、定理介绍

> **前置依赖**：牛顿第二定律（动量平衡）、力与面元的几何投影关系、张量代数、角动量守恒（力矩平衡）、无穷小体元极限论证。

Cauchy 定理（Cauchy 应力张量的存在性）断言：当体力密度 $\boldsymbol b$ 与面力密度 $\boldsymbol t(\boldsymbol n)$ 满足动量平衡时，存在对称二阶张量 $\boldsymbol\sigma$ 使得 $\boldsymbol t(\boldsymbol n)=\boldsymbol\sigma\cdot\boldsymbol n$。它保证了连续介质内部应力的统一描述与对称性。

## 二、原理思路

用无穷小四面体的力平衡证明。斜面与三坐标面的面积投影关系 $S_i=n_iS$ 结合牛顿第二定律，令四面体收缩到一点使体力项（$O(h^3)$）低于面力项（$O(h^2)$），从而得到线性关系；对称性则由角动量守恒（力矩平衡）给出。

## 三、定理的严格表述

在连续介质中，若面力满足动量平衡，则存在对称张量场 $\boldsymbol\sigma$ 使对任意法向 $\boldsymbol n$
$$
\boldsymbol t(\boldsymbol n)=\boldsymbol\sigma\cdot\boldsymbol n,
$$
且 $\boldsymbol\sigma=\boldsymbol\sigma^{\top}$。

## 四、证明过程

1. **四面体平衡**。对斜法与坐标面法向，列力平衡
   $$
   \boldsymbol t(\boldsymbol n)S-\sum_{i=1}^{3}\boldsymbol t(\boldsymbol e_i)n_iS+\rho\boldsymbol b\,\Delta V=\rho\boldsymbol a\,\Delta V.
   $$
2. **取极限**。$h\to0$ 时 $\Delta V=O(h^3)$，$\Delta S=O(h^2)$，体积项消失，得 $\boldsymbol t(\boldsymbol n)=\sum_i\boldsymbol t(\boldsymbol e_i)n_i$。
3. **定义张量**。令 $\boldsymbol t(\boldsymbol e_i)=\sigma_{ij}\boldsymbol e_j$，则 $\boldsymbol t(\boldsymbol n)=\boldsymbol\sigma\cdot\boldsymbol n$。
4. **对称性**。由角动量守恒（Cauchy 第二运动定律）对无穷小体元的力矩平衡推出 $\sigma_{ij}=\sigma_{ji}$。

## 五、应用与意义

Cauchy 应力张量是连续介质力学的核心概念，是弹性、塑性、流体等本构理论的标尺。Cauchy 定理的存在性证明（四面体论证）保证了应力描述的普适性，也为后续守恒律与有限元方法提供了基础。

## 课堂问答

**老师**：为什么"任意小面上的力"都能用一个矩阵统一表示？

**学生**：因为动量平衡迫使面力关于法向是线性的：对法向三个坐标分量分解，且关于法向是奇函数。于是存在二阶张量 $\boldsymbol\sigma$ 使 $\boldsymbol t(\boldsymbol n)=\boldsymbol\sigma\cdot\boldsymbol n$，并且由角动量守恒得对称性 $\boldsymbol\sigma=\boldsymbol\sigma^\top$。

**老师（追问）**：无穷小四面体论证里，体积项为什么可以丢？

**学生**：因为四面体收缩时面力 $\sim O(h^2)$、体力 $\sim O(h^3)$，故
$$
\boldsymbol t(\boldsymbol n)S-\sum_{i=1}^{3}\boldsymbol t(\boldsymbol e_i)n_iS+\rho\boldsymbol b\,\Delta V=\rho\boldsymbol a\,\Delta V,
$$
当 $h\to0$ 体积项相对面力项是高阶小量而被消去，剩下的正是线性关系 $\boldsymbol t(\boldsymbol n)=\sum_i n_i\boldsymbol t(\boldsymbol e_i)$。

**老师（拓展）**：对称性是从哪条守恒律来的？

**学生**：从角动量守恒（Cauchy 第二运动定律）。对无穷小体元写力矩平衡，无力偶应力时必须 $\sigma_{ij}=\sigma_{ji}$。注意对称性并非来自动量平衡，而是额外用了一次角动量守恒；在 Cosserat 等含力偶的极性介质中，$\boldsymbol\sigma$ 一般不对称。
