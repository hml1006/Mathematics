# Lyapunov稳定性定理

> **一句话大白话**：找个“越降越小的能量函数”来盯着系统，只要这个能量沿轨道只减不增，系统就稳定；减到零更是渐近稳定。
>
> **小例子**：看小球滚向碗底，能量（高度＋动能）不断减小、最后到零，小球就停在碗底——Lyapunov 就是这种“能量法”的一般化。

## 一、定理介绍

> **前置依赖**：Picard-Lindelöf定理、正定函数与水平集、紧集与连续函数最值、LaSalle不变集原理、反证法。

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

## 课堂问答

**老师**：判断 $\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$ 的原点稳定，为什么找一个正定函数 $V$ 且 $\dot V\le0$ 就够了？背后的几何图像是什么？

**学生**：结论：正定 $V$ 的水平集 $\{V=c\}$ 是一圈圈包围原点的闭曲线，$\dot V\le0$ 说明轨道只能由外向内穿过或沿其走，永远逃不出去。严格地，对 $\epsilon$ 取 $\alpha=\min_{\|\boldsymbol x\|=\epsilon}V>0$，由连续性选 $\delta$ 使 $\|\boldsymbol x_0\|<\delta$ 时 $V(\boldsymbol x_0)<\alpha$；因 $V$ 沿轨道不增，$\|\boldsymbol x(t)\|<\epsilon$，即稳定。

**老师（追问）**：那凭什么从 $\dot V<0$ 升级到渐近稳定，$V\to0$ 这一步怎么写？

**学生**：反设 $V$ 递减到 $c>0$，轨道就落在紧集 $\{c\le V\le V(\boldsymbol x_0)\}$ 上，其上 $\dot V\le-\gamma<0$，于是 $V$ 以正速率线性下降，终将跌到 $c$ 以下，矛盾，故 $c=0$，$\boldsymbol x(t)\to\boldsymbol 0$。若只有 $\dot V\le0$，就用 LaSalle：$\omega$-极限集是不变集、其上 $V$ 恒为常数故 $\dot V=0$，轨道收敛到 $\{\dot V=0\}$ 的最大不变集。

**老师（拓展）**：若一时找不到现成的 $V$，线性系统 $\dot{\boldsymbol x}=\boldsymbol A\boldsymbol x$ 能反过来由稳定性造出 $V$ 吗？

**学生**：能。任取 $\boldsymbol Q>\boldsymbol 0$，解 Lyapunov 方程 $\boldsymbol A^{\top}\boldsymbol P+\boldsymbol P\boldsymbol A=-\boldsymbol Q$，取 $V=\boldsymbol x^{\top}\boldsymbol P\boldsymbol x$，则 $\dot V=-\boldsymbol x^{\top}\boldsymbol Q\boldsymbol x<0$，且当且仅当 $\boldsymbol A$ 的谱在左半平面时 $\boldsymbol P>\boldsymbol 0$。这与代数Riccati方程唯一性证明里"两个 Hurwitz 矩阵的 Sylvester 方程只有零解"同源。

## 相关条目

- [Lyapunov 稳定性定理（第69级-控制理论）](../第69级-控制理论/Lyapunov稳定性定理.md)：与本条目为同一定理，另收录于第69级-控制理论，可交叉参考。
