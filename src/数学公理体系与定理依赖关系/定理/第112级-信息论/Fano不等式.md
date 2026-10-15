# Fano不等式

> **一句话大白话**：如果要从观测 $Y$ 去猜 $X$，那么"猜错那点余地"本身就要花钱——放射性熵：条件熵 $H(X|Y)$ 越大，可容许的误差概率下限越高；误差概率若很小，条件熵也必然很小。两者被上如下地拴在一起。
>
> **小例子**：$X$ 有 4 个等可能取值且必须凭很差的观测猜，条件熵 $H(X|Y)$ 若接近 2 比特，则错误概率下界 $\ge\frac{H(X|Y)-1}{\log4}\ge\frac{2-1}{2}=0.5$——即至少一半时候猜错，这正是 Fano 排队。

## 一、定理介绍

> **前置依赖**：熵与条件熵、互信息、链式法则多变量、二元熵函数、对数的上界性质。

**Fano 不等式**：设 $X,\hat X$ 取值于同一字母表 $\mathcal X$，$P_e=P(X\neq\hat X)$。则
$$
H(X|\hat X)\le H(P_e)+P_e\log(|\mathcal X|-1)\le1+P_e\log|\mathcal X|.
$$
它把"估计误差概率"与"剩余不确定性（条件熵）"绑定，是信息论中估计/决策误差下界的核心工具。

## 二、原理思路

引入误差指示变量 $E=\mathbf1_{\{X\neq\hat X\}}$。用链式法则拆分条件熵 $H(X|\hat X)=H(E|\hat X)+H(X|E,\hat X)$：$H(E|\hat X)\le H(E)=H(P_e)$；而给定 $E=1$（出错）时 $X$ 至多有 $|\mathcal X|-1$ 个取值，故该项 $\le P_e\log(|\mathcal X|-1)$。相加即得上界。再由 $H(P_e)\le1$ 得简化形式。

## 三、定理的严格表述

如上，$H(P_e)=-P_e\log P_e-(1-P_e)\log(1-P_e)$。则
$$
H(X|\hat X)\le H(P_e)+P_e\log(|\mathcal X|-1)\le1+P_e\log|\mathcal X|.
$$

## 四、证明要点

1. **链式法则**. $H(X|\hat X)=H(E|\hat X)+H(X|E,\hat X)$（$E$ 由 $X,\hat X$ 决定故 $H(E|X,\hat X)=0$）。
2. **第一个因子**.$H(E|\hat X)\le H(E)=H(P_e)$。
3. **第二个因子**. $H(X|E,\hat X)=P_e\cdot H(X|\hat X,E=1)+0\cdot(\dots)$；出错时 $X$ 可取 $\le|\mathcal X|-1$ 个值，故 $H\le P_e\log(|\mathcal X|-1)$。
4. **合并**.两端相加即（i）；由于 $H(P_e)\le1$、$\log(|\mathcal X|-1)\le\log|\mathcal X|$ 得（ii）。$\blacksquare$

## 五、应用与意义

- **信道逆向定理**.配合数据处理不等式证明 $R>C$ 时 $P_e$ 有正下界。
- **估计/假设检验中间**.量化"最小可达成误差"的下确界。
- **与率失真/EED 联系**.刻画估计器的能力边界。
- **理论地位**.是"条件熵→误差下界"这一方向的标杆不等式，与数据处理不等式相辅相成。

## 课堂问答

**老师**：用观测 $\hat X$ 去猜 $X$，误差概率 $P_e$ 与条件熵 $H(X|\hat X)$ 之间谁约束谁？

**学生**：结论 $H(X|\hat X)\le H(P_e)+P_e\log(|\mathcal X|-1)\le1+P_e\log|\mathcal X|$。理由是引入误差指示 $E=\mathbf1_{\{X\ne\hat X\}}$，用链式法则 $H(X|\hat X)=H(E|\hat X)+H(X|E,\hat X)$，第一项 $\le H(P_e)$，出错时 $X$ 至多 $|\mathcal X|-1$ 个取值故第二项 $\le P_e\log(|\mathcal X|-1)$。常见误区是误以为第二个"$\le$"是等式。

**老师（追问）**：哪个方向才是真正有用的？

**学生**：逆向使用，即误差下界 $P_e\ge\frac{H(X|\hat X)-1}{\log|\mathcal X|}$：条件熵越大，任何估计器都不可能太准。比如 $|\mathcal X|=4$ 且 $H(X|\hat X)\approx2$ 时必有 $P_e\ge\tfrac12$，配合数据处理不等式即可证明 $R>C$ 时错误概率有正下界。

**老师（拓展）**：有没有更精确的形式？

**学生**：$H(P_e)+P_e\log(|\mathcal X|-1)$ 是精确式，$H(P_e)\le1$ 与 $\log(|\mathcal X|-1)\le\log|\mathcal X|$ 才给出简化式；这一族不等式是率失真、假设检验与估计误差下界的共同基础。
