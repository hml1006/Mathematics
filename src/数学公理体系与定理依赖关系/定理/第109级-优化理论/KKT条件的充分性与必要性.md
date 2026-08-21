# KKT条件的充分性与必要性

> **一句话大白话**：在"允许的最优解点"上，目标函数的"下山方向"和所有活跃约束的"法线方向"必须能相互抵销成 0（拉格朗日驻点条件），而且"松的约束"对应的乘子必须是 0（互补松弛）。这些条件就是判断某点是不是最优解的"金标准"，凸问题上它充分又必要。
>
> **小例子**：最小化 $f(x,y)=(x-1)^2+(y-2)^2$ 在 $x+y\le2$ 下。最优解 $x=0.5,\ y=1.5$ 处梯度 $(-1,-1)$ 与约束法线 $(1,1)$ 平行反号，且约束活跃（$=2$），乘子 $\lambda=1>0$，KKT 全部满足——检测通过即最优。

## 一、定理介绍

**KKT（Karush–Kuhn–Tucker）条件**给出带不等式与等式约束优化问题的**一阶必要/充分条件**。在凸性（$f,g_i$ 凸、$h_j$ 仿射）下它既是局部最优的**必要性**（需适当的约束规范），也是**全局最优的充分性**。是凸优化、机器学习、运筹学求解与验证的核心判据。

## 二、原理思路

必要性的直观：若 $x^*$ 是局部最优，则不存在"同时改善目标函数又保持可行"的方向。把"可行方向"限制为由活跃不等式与等式约约束的切锥 $\mathcal F(x^*)$ 描述；若存在使 $\nabla f^\top d<0$ 的 $d\in\mathcal F$，则沿 $d$ 微移会改进目标——矛盾。再用 Farkas 引理把"这个线性系统无解"转化成"存在非负组合使梯度平衡"，即 KKT 的驻点方程；活跃约束取得非零乘子、非活跃约束取 0，得互补松弛。

## 三、定理的严格表述

考虑 $\min_x f(x)$ s.t. $g_i(x)\le0\ (i=1,\dots,m)$，$h_j(x)=0\ (j=1,\dots,p)$。
- **必要性**：若 $x^*$ 为局部最优且满足约束规范（如 LICQ 或 Slater），则存在 $\lambda_i^*\ge0,\ \mu_j^*$ 使（i）驻点 $\nabla f(x^*)+\sum_i\lambda_i^*\nabla g_i(x^*)=-\sum_j\mu_j^*\nabla h_j(x^*)$（合并写 $\nabla f+\sum\lambda_i\nabla g_i+\sum\mu_j\nabla h_j=0$）；（ii）互补松弛 $\lambda_i^*g_i(x^*)=0$。
- **充分性**：若 $f,g_i$ 凸、$h_j$ 仿射，且 $(x^*,\lambda^*,\mu^*)$ 满足 KKT，则 $x^*$ 是全局最优。

## 四、证明要点

**必要性**：
1. **可行方向锥**.$\mathcal F=\{d:\nabla g_i(x^*)^\top d\le0\ \forall i\in\mathcal A,\ \nabla h_j(x^*)^\top d=0\ \forall j\}$。局部最优时对任意 $d\in\mathcal F$ 有 $\nabla f(x^*)^\top d\ge0$，故系统 $\nabla f^\top d<0,\ \nabla g_i^\top d\le0\ (i\in\mathcal A),\ \pm\nabla h_j^\top d\le0$ 无解。
2. **Farkas 应用**.由 Farkas/Motzkin 择一，存在 $\lambda_i\ge0\ (i\in\mathcal A)$ 与 $\mu_j$ 使 $-\nabla f=\sum_{i\in\mathcal A}\lambda_i\nabla g_i+\sum_j\mu_j\nabla h_j$；补 $\lambda_i=0\ (i\notin\mathcal A)$ 即得驻点与互补松弛。

**充分性**：
3. 由 $f$ 凸：$f(x)\ge f(x^*)+{\nabla f(x^*)}^\top(x-x^*)$；用驻点消去 $\nabla f(x^*)$。
4. 由 $g_i$ 凸与 $\lambda_i^*\ge0$：$-\lambda_i^*{\nabla g_i(x^*)}^\top(x-x^*)\ge \lambda_i^*(g_i(x^*)-g_i(x))=-\lambda_i^*g_i(x)\ge0$（互补松弛与可行性）；仿射约束项为 0。
5. 合并得 $f(x)\ge f(x^*)$，$x^*$ 全局最优。$\blacksquare$

## 五、应用与意义

- **最优性检测/SVM**.支撑向量机通过 KKT 判据确定支持向量与求解对偶。
- **惩罚与约束方法**.内点法、SQP 均围绕 KKT 方程构造迭代。
- **算法终止判据**.多数优化求解器以"KKT 残差小"作为收敛退出标准。
- **理论地位**.从 Lagrange 条件推广到含不等式，是优化理论承上启下的枢纽。