# Gromov多项式增长定理

> **一句话大白话**：一个有限生成群"球内元素随半径多项式增长"时，它不会长得太野，必定"接近"一个幂零群——只差一个有限指数子群。
>
> **小例子**：$\mathbb{Z}^n$ 是幂零的，增长阶恰为 $n$；自由群 $F_2$ 指数增长，故不可能是多项式增长的幂零群。

## 一、定理介绍

Gromov 多项式增长定理刻画了增长性质的代数来源：多项式增长有限生成群 $\Longleftrightarrow$ virtually 幂零群。它一举解决了关于增长型的核心分类问题，是几何群论与李理论交汇的经典成果。

## 二、原理思路

多项式增长 $\Rightarrow$ virtually 幂零的方向最难：把单位球按半径缩放，得到一族度量空间，靠 Gromov–Hausdorff 收敛得极限空间（渐近锥）$X$。多项式增长保证 $X$ 完备、齐次、连通、测地；Montgomery–Zippin 与 Gleason–Yamabe 定理说明其对等距的连通 Lie 群；再借 Lipschitz 同态 $\varphi:G\to\operatorname{Iso}(X)$ 证 $\ker\varphi$ 有限而商幂零。反方向：幂零群的下中心列给出 $\beta(n)\le Cn^c$。

## 三、定理的严格表述

（Gromov 多项式增长定理）有限生成群 $G$ 具有多项式增长当且仅当 $G$ 是 virtually 幂零群（即包含有限指数的幂零子群）。

## 四、证明过程

**第一步：** 设 $G$ 多项式增长：$\beta_{G,S}(n)\le Cn^d$。

**第二步（渐近锥）：** 考虑缩放 Cayley 图 $(G,\frac1n d_S)$。由多项式增长，这些空间 Gromov–Hausdorff 收敛到极限空间 $X$（渐近锥）。

**第三步（性质）：** $X$ 完备、齐次、测地且连通（由多项式增长保证）。Montgomery–Zippin 与 Gleason–Yamabe 定理推出连通齐次空间是 Lie 群，故 $X$ 是幂零 Lie 群。

**第四步（构造同态）：** 存在 Lipschitz 同态 $\varphi:G\to\operatorname{Iso}(X)$，其像生成 $\operatorname{Iso}(X)$ 中幂零子群；且 $\ker(\varphi)$ 有限，$G/\ker(\varphi)$ 幂零。故 $G$ virtually 幂零。

**第五步（逆命题）：** 若 $G$ 是幂零群，设下中心列 $G=G_1\supset G_2\supset\cdots\supset G_{c+1}=\{1\}$，可证存在 $C$ 使 $\beta_{G,S}(n)\le Cn^c$，即多项式增长。$\square$

**推论 1：** $\mathbb{Z}^n$ 多项式增长，增长次数 $n$。
**推论 2：** $F_n$（$n\ge2$）指数增长。
**推论 3：** Grigorchuk 群中间增长（既非多项式也非指数），是第一个中间增长群的例子。

## 五、应用与意义

本定理完整解决了"多项式增长"这一几何性质与"幂零性"这一纯代数性质的等价，是 Lie 理论在离散群上的胜利。它催生了 Grigorchuk 关于中间增长的著名例子，并深刻影响微分几何、离散群在流形上的作用以及随机游走的逃逸速率研究。