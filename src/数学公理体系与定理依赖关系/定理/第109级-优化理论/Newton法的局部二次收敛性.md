# Newton法的局部二次收敛性

> **一句话大白话**：如果目标函数在最优解附近足够光滑（Hessian 连续且正定），Newton 法会"越靠越紧"——误差从 $\epsilon$ 变成 $\approx C\epsilon^2$，即每步误差大致平方化，几个量级地狂飙逼近最优点。代价是每步要解线性方程组。
>
> **小例子**：求 $f(x)=\tfrac12 x^2-\cos x$ 的极小。初值 $x_0=1$，Newton 步 $x_{k+1}=x_k-f'/f''$ 在两步内就把误差压到 $10^{-10}$ 量级——远比梯度下降几十步都快，典型二次收敛。

## 一、定理介绍

> **前置依赖**：多变量 Taylor 展开与积分型余项、Hessian 矩阵与 Lipschitz 连续性、正定矩阵与范数、不动点与收敛阶分析。

**Newton 法局部二次收敛**：设 $f:\mathbb R^n\to\mathbb R$ 二次连续可微，$\nabla^2 f$ 在 $x^*$ 邻域 Lipschitz 连续且 $\nabla^2f(x^*)\succ0$。则 Newton 迭代 $x_{k+1}=x_k-[\nabla^2 f(x_k)]^{-1}\nabla f(x_k)$ 在充分靠近 $x^*$ 处**局部二次收敛**：存在 $\delta,C>0$ 使 $\|x_0-x^*\|<\delta$ 时 $\|x_{k+1}-x^*\|\le C\|x_k-x^*\|^2$。

## 二、原理思路

Newton 步本质是"用二阶 Taylor 模型求驻点"：$x_{k+1}$ 满足近似驻点方程。误差递推由此而来：把 $\nabla f(x^*)=0$ 在 $x_k$ 展开，用积分型 Taylor 余项 $\nabla f(x^*)=\nabla f(x_k)+\int_0^1\nabla^2 f(x^*+t(x_k-x^*))(x_k-x^*)dt$；两端代入 Newton 迭代，利用 $\nabla^2$ 的 Lipschitz/正定把"模型误差项"量级定为 $\|x_k-x^*\|^2$，即得二次收敛。

## 三、定理的严格表述

设 $\nabla^2 f$ 在 $B(x^* ,r)$ 内 Lipschitz：$\|\nabla^2f(x)-\nabla^2 f(y)\|\le L\|x-y\|$，且 $\nabla^2f(x^*)\succ0$（从而存在 $\lambda>0$ 使 $\|\nabla^2f(x)^{-1}\|\le\lambda$ 于邻域内）。则存在 $\delta>0$ 与常数 $C>0$，$\|x_0-x^*\|\le\delta\Rightarrow\|x_{k+1}-x^*\|\le C\|x_k-x^*\|^2$。

## 四、证明要点

1. **积分余项**.由多变量 Taylor：
   $$
   \nabla f(x^*)=\nabla f(x_k)+\int_0^1 \nabla^2 f(x^*+t(x_k-x^*))(x_k-x^*)dt.
   $$
2. **误差代换**.由迭代，两边减 $x^*$：
   $$
   x_{k+1}-x^*=[\nabla^2 f(x_k)]^{-1}\big[\nabla^2 f(x_k)(x_k-x^*)-\nabla f(x_k)\big].
   $$
3. **括号内估计**.利用积分余项，括号内等于
   $$
   \int_0^1[\nabla^2f(x_k)-\nabla^2 f(x^*+t(x_k-x^*))](x_k-x^*)dt,
   $$
   其范数 $\le\tfrac12 L\|x_k-x^*\|^2$（Lipschitz）。
4. **合成**.故 $\|x_{k+1}-x^*\|\le\|\nabla^2f(x_k)^{-1}\|\cdot\tfrac12 L\|x_k-x^*\|^2\le \frac{\lambda L}{2}\|x_k-x^*\|^2$。$\blacksquare$

## 五、应用与意义

- **快速局部求解**.在线性规划内点法、非线性最小二乘（Gauss–Newton）末段都靠二次收敛收尾。
- **全局化**.配以线搜索/置信域（近 Newton）保证无全局收敛之忧后，进入二次收敛阶段。
- **代价与回报**.每步需解 Hessian 方程组，但步数极少，适合中小规模高精度问题。
- **理论价值**.二次收敛是局部方法精度的"天花板"，也是准 Newton 方法（拟 Newton）对标的目标。