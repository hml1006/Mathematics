# Hopf分歧定理

> **一句话大白话**：当一对共轭复特征值横穿着穿越虚轴，且第一 Lyapunov 系数非零时，平衡点会"抖出"一族小振幅周期轨道（极限环），振幅随 $\sqrt{|\mu-\mu_0|}$ 走出。
>
> **小例子**：超临界 Hopf 分歧：$\mu<0$ 原点稳定，$\mu>0$ 原点失稳并出现稳定极限环 $r=\sqrt{\mu}$（$\dot r=\mu r-r^3$）。

## 一、定理介绍

> **前置依赖**：中心流形约化、Poincaré 规范形理论、特征值与稳定性分析、第一 Lyapunov 系数、极坐标变换、叉形分歧的规范形

Hopf 分歧定理是分支理论最著名的结果之一：当参数增大、共轭复特征值 $\alpha(\mu)\pm i\omega(\mu)$ 在 $\mu_0$ 处横截穿越虚轴（$\alpha'(\mu_0)\neq0$），则从该平衡点分支出周期轨道族，振幅 $O(\sqrt{|\mu-\mu_0|})$、频率 $O(\omega(\mu_0))$，子临界/超临界由第一 Lyapunov 系数的符号判定。

## 二、原理思路

依赖中心流形约化与规范形：在 $\mu_0$ 处纯虚特征值给出二维中心流形，把系统约化，再展开为 $\dot z=(\alpha+i\omega)z+az|z|^2+\cdots$，经规范形化为极坐标 $\dot r=\alpha(\mu)r+a_r r^3$。径向方程是叉形分歧，其非零平衡 $r=\sqrt{-\alpha'\epsilon/a_r}$ 即极限环。

## 三、定理的严格表述

（Hopf 分歧定理）设 $\dot x=f(x,\mu)$，$x\in\mathbb{R}^2$，$\mu\in\mathbb{R}$，满足：$f(0,\mu)=0$；$A(\mu)=Df(0,\mu)$ 有共轭复特征值 $\alpha(\mu)\pm i\omega(\mu)$，$\omega(\mu_0)>0$；横截条件 $\alpha'(\mu_0)\neq0$；非退化条件：第一 Lyapunov 系数 $l_1\neq0$。则在 $\mu_0$ 处分支出周期轨道，振幅 $O(\sqrt{|\mu-\mu_0|})$、频率 $O(\omega(\mu_0))$。若 $l_1<0$ 分歧超临界（稳定极限环），$l_1>0$ 亚临界（不稳定极限环）。

## 四、证明过程

**第一步（中心流形约化）：** 在 $\mu=\mu_0$，$A=Df(0,\mu_0)$ 有一对纯虚特征值 $\pm i\omega_0$、其余实部非零，故二维中心流形存在，约化后
$$
\dot z=F(z,\mu),\quad z\in\mathbb{C},\ F(0,\mu)=0,\ D_zF(0,\mu_0)=i\omega_0
$$

**第二步（展开）：** 在 $(0,\mu_0)$ 附近
$$
F(z,\mu)=\alpha(\mu)z+i\omega(\mu)z+a(\mu)z|z|^2+O(|z|^5)
$$
$\alpha(\mu_0)=0$，$\omega(\mu_0)=\omega_0$。

**第三步（规范形）：** 经近恒等变换，极坐标化为
$$
\begin{cases}\dot r=\alpha(\mu)r+a_r(\mu)r^3+O(r^5)\\\dot\theta=\omega(\mu)+a_i(\mu)r^2+O(r^4)\end{cases}
$$
其中 $a_r=\operatorname{Re}(a)$ 即第一 Lyapunov 系数。

**第四步（分歧分析）：** $\alpha(\mu)=\alpha'(\mu_0)(\mu-\mu_0)+O((\mu-\mu_0)^2)$，记 $\epsilon=\mu-\mu_0$：
$$
\dot r=\alpha'(\mu_0)\epsilon\,r+a_r(\mu_0)r^3
$$
非零平衡 $r=\sqrt{-\alpha'(\mu_0)\epsilon/a_r(\mu_0)}$ 存在当且仅当符号相符，且解出 $\mu$ 的局部唯一分支结构。

**第五步（周期解）：** 对应原系统有周期解 $x(t)=r\cos(\omega t+\theta_0)+O(r^2)$，其稳定性由 $l_1=a_r$ 符号决定。$\square$

## 五、应用与意义

Hopf 分歧刻画了从静态平衡跳到周期振荡的根本机制，是电气回路、化学振荡、生物节律（如心跳）与流体失稳（如涡街）的普适模型。其稳定判据（第一 Lyapunov 系数）在数值分支计算中被广泛采用。