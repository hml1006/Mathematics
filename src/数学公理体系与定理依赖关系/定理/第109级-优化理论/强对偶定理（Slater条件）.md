# 强对偶定理（Slater条件）

> **一句话大白话**：对凸问题，只要存在一个"守住可行域内部、让所有不等式都严格放松"的点（Slater 点），那么"最优原值"和"最优对偶值"就严格相等——对偶间隙为零。可以放心地转成对偶去解。
>
> **小例子**：$\min e^{-x}$ s.t. $x\le0$。$x=-1$ 严格满足 $x\le0$，Slater 成立，故 $\min e^{-x}=1$ 等于对偶最大值；而若不满足 Slater（可行集只剩一个点），强对偶可能破缺。

## 一、定理介绍

> **前置依赖**：弱对偶、凸优化的理论与 Lagrange 对偶函数、凸集分离定理、支持超平面、相对内点与 Slater 条件。

**强对偶定理**：对凸优化问题，在 **Slater 条件**（存在严格内点使所有非仿射不等式约束严格成立）成立时，原值 $p^*$ 等于对偶值 $d^*$。该定理建立"原–对偶等价"，是支撑对偶分解、仅据对偶恢复原解的理论基础。

## 二、原理思路

弱对偶 $d^*\le p^*$ 恒真，关键要证 $d^*\ge p^*$。做法是通过"可行性干扰的**摄动集**"：在 $m$ 维方向把约束放松 $u_i$，收集所有可能的（干扰，目标）对构成凸集 $\mathcal A\subseteq\mathbb{R}^{m+1}$（由凸性保证凸）。点 $(0,p^*)$ 在该集的边界。用凸集分离定理在 $(0,p^*)$ 处取支撑超平面，得到非负系数 $(\tilde\lambda,\tilde\mu)$；Slater 条件精确保证 $\tilde\mu>0$（否则矛盾），归一化后再代回对偶函数即得 $d^*\ge p^*$。

## 三、定理的严格表述

凸问题 $\min f_0(x)$ s.t. $f_i(x)\le0\ (i=1,\dots,m)$，$Ax=b$。若存在 $x\in\operatorname{relint}\mathcal D$（$\mathcal D=\bigcap\operatorname{dom}f_i$）使所有非仿射 $f_i(x)<0$ 且 $Ax=b$（Slater），且 $p^*>-\infty$，则存在对偶解使 $p^*=d^*$（强对偶）。

## 四、证明要点

1. **摄动集构造**.$\mathcal A=\{(u,t):\exists x,\ f_i(x)\le u_i\ \forall i,\ f_0(x)\le t\}$ 为凸集；$(0,p^*)\in\partial\mathcal A$ 且 $(0,p^*-\epsilon)\notin\mathcal A\ (\epsilon>0)$。
2. **支撑超平面**.由分离定理得非零 $(\tilde\lambda,\tilde\mu)\ge0$（因 $u_i,t$ 可取任意大）使
   $$
   \tilde\lambda^\top u+\tilde\mu t\ge\tilde\mu p^*,\quad\forall(u,t)\in\mathcal A.
   $$
3. **Slater 保证 $\tilde\mu>0$**.取 Slater 点 $x_0$：$f_i(x_0)<0$。若 $\tilde\mu=0$，则 $\sum_i\tilde\lambda_i f_i(x_0)\ge0$ 且 $\le0$，故 $=0$；因 $f_i(x_0)<0$ 得 $\tilde\lambda_i=0$，与 $(\tilde\lambda,\tilde\mu)\neq0$ 矛盾。故 $\tilde\mu>0$。
4. **归一化**.令 $\lambda_i=\tilde\lambda_i/\tilde\mu$，得 $\sum_i\lambda_i f_i(x)+f_0(x)\ge p^*$（对任意 $x$）。取 $x$ 使 $g(\lambda,0)=\inf_x L(x,\lambda,0)\ge p^*$，从而 $d^*=\sup g\ge p^*$；联合 $d^*\le p^*$ 得 $p^*=d^*$。$\blacksquare$

## 五、应用与意义

- **对偶求解**.模型在有 Slater 内点时，可转化为对偶问题（常更易优化）。
- **灵敏度/影子价格**.最优对偶变量给出约束松弛的边际价值，用于经济学与资源分配。
- **内点与分解**.Slater 保证原–对偶内点法收敛到同一最优值，支撑大规模分解算法。
- **理论地位**.把"原–对偶等价"严格化，是凸优化的核心结论之一。