# Lyapunov稳定性定理

> **一句话大白话**：找个“越降越小的能量函数”来盯着系统，只要这个能量沿轨道只减不增，系统就稳定；减到零更是渐近稳定。
>
> **小例子**：看小球滚向碗底，能量（高度＋动能）不断减小、最后到零，小球就停在碗底——Lyapunov 就是这种“能量法”的一般化。

## 一、定理介绍

Lyapunov 稳定性定理给出自治系统 $\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$（$\boldsymbol f(\boldsymbol 0)=\boldsymbol 0$）稳定性的充分条件：若存在正定函数 $V$ 使 $\dot V\le0$，则原点 Lyapunov 稳定；若 $\dot V<0$ 则渐近稳定；并结合 LaSalle 不变原理处理 $\dot V$ 仅半负定的情形。

## 二、原理思路

用“能量水平”刻画：$V$ 正定、在球面有正下界，且沿轨道递减，故轨道无法逃离等值线所围区域。渐近稳定性需证明 $V\to0$，反设下界 $c>0$ 并利用紧集上的负定导出矛盾；LaSalle 原理用 $\omega$-极限集处理半负定。

## 三、定理的严格表述

对 $\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$，$\boldsymbol f(\boldsymbol 0)=\boldsymbol 0$。若存在连续可微函数 $V(\boldsymbol x)$ 满足
1. $V$ 正定：$V(\boldsymbol 0)=0$，$\boldsymbol x\ne\boldsymbol 0$ 时 $V(\boldsymbol x)>0$；
2. $\dot V=\nabla V\cdot\boldsymbol f\le0$（半负定），

则原点 Lyapunov 稳定；若 $\dot V<0$（$\boldsymbol x\ne\boldsymbol 0$）则渐近稳定；若 $\dot V\le0$ 且集合 $\{\dot V=0\}$ 不含除原点的完整轨道，由 LaSalle 原理亦渐近稳定。

## 四、证明过程

1. **稳定**。对 $\epsilon$，令 $\alpha=\min_{\|x\|=\epsilon}V>0$，由连续性取 $\delta$ 使 $\|x_0\|<\delta\Rightarrow V(x_0)<\alpha$。因 $\dot V\le0$，$V(x(t))\le V(x_0)<\alpha$，故 $\|x(t)\|<\epsilon$。
2. **渐近稳定**。设 $\lim V=c>0$，则轨道落在紧集 $\Omega=\{c\le V\le V(x_0)\}$ 上，其上 $\dot V\le-\gamma<0$，得 $V$ 线性递减至负值矛盾，故 $c=0$。
3. **LaSalle**。$\omega$-极限集为紧不变集，其上 $V$ 恒为常数故 $\dot V=0$，$\omega(x_0)\subseteq M$（$\dot V=0$ 之最大不变集）。若 $M=\{\boldsymbol 0\}$ 则收敛到原点。

## 五、应用与意义

Lyapunov 方法是非线性系统与最优控制稳定性的核心工具，广泛用于航天、机器人、电力与自适应控制。它无需显式解轨迹即可判定稳定，也是 LQR 闭环稳定性证明与神经网络控制设计的理论基础。