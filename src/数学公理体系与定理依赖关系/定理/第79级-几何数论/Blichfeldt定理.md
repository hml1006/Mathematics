# Blichfeldt 定理

> **一句话大白话**：一个可测集合只要体积超过格子基本区域的体积（$\det\Lambda$），里面就必然缝进了格子上平移出来的"平移到格点"两点——即集合里有两点之差落在格上。
>
> **小例子**：把 $[0,1)^2$ 当作基本区域（面积 1），若平面上画一个有面积大于 1 的区域 $S$，则 $S$ 中必有两点的坐标差为整数对。例如区域 $[0,1.5)\times[0,1.5)$ 中有两点相差 $(1,1)$。

## 一、定理介绍

> **前置依赖**：格与基本区域、Lebesgue 测度与体积的可加性、鸽巢原理（面积重叠论证）。

Blichfeldt 定理是几何数论最基本的"鸽巢"引理，也是 Minkowski 凸体定理的核心构件。它断言体积超过 $\det\Lambda$ 的可测集必含两个不同点其差在格 $\Lambda$ 中。用平方式划定在基本区域上计数，"塞物即撞"是它最本质的表述。

## 二、原理思路

把 $\mathbb{R}^n$ 按格平移 $\mathcal{F}+\lambda$（$\mathcal{F}$ 为基本区域）铺开，把 $S$ 的每一片 $S\cap(\mathcal{F}+\lambda)$ 平移回 $\mathcal{F}$（$\lambda$ 处减去 $\lambda$）。总体积超过 $\mathcal{F}$ 的体积，而它们都被装进 $\mathcal{F}$，故必有重叠：两块叠点之差为某两个格点之差 $\lambda_1-\lambda_2\in\Lambda$。

## 三、定理的严格表述

设 $\Lambda\subset\mathbb{R}^n$ 是格，$S\subseteq\mathbb{R}^n$ 可测且 $\operatorname{vol}(S)>\det(\Lambda)$。则存在不同点 $x,y\in S$，使 $x-y\in\Lambda$。

## 四、证明过程

**证明：**

**步骤 1：铺展。** 取基本区域 $\mathcal{F}$，$\mathbb{R}^n=\bigcup_{\lambda\in\Lambda}(\mathcal{F}+\lambda)$。

**步骤 2：平移回装。** 对每个 $\lambda$，令 $S_\lambda=S\cap(\mathcal{F}+\lambda)$，$S_\lambda'=S_\lambda-\lambda\subseteq\mathcal{F}$。平移保体积，故
$$\sum_{\lambda}\operatorname{vol}(S_\lambda)=\operatorname{vol}(S)>\det(\Lambda)=\operatorname{vol}(\mathcal{F}).$$

**步骤 3：重叠矛盾。** 若所有 $S_\lambda'$ 互不相交，则 $\bigcup_\lambda S_\lambda'\subseteq\mathcal{F}$，从而
$$\sum_\lambda\operatorname{vol}(S_\lambda)=\operatorname{vol}\Big(\bigcup_\lambda S_\lambda'\Big)\le\operatorname{vol}(\mathcal{F})=\det(\Lambda),$$
与 $\operatorname{vol}(S)>\det(\Lambda)$ 矛盾。$\blacksquare$

**步骤 4：结论。** 故存在 $\lambda_1\neq\lambda_2$ 使 $S_{\lambda_1}'\cap S_{\lambda_2}'\neq\varnothing$：存在 $x\in S_{\lambda_1},y\in S_{\lambda_2}$ 使 $x-\lambda_1=y-\lambda_2$，即 $x-y=\lambda_1-\lambda_2\in\Lambda$，且 $x\neq y$。$\square$

## 五、应用与意义

Blichfeldt 定理是几何数论的"体积-格点"基本桥梁，直接导出 Minkowski 凸体定理与线性型定理。在数论中它用于证明丢番图逼近、代数数论中理想格点的存在（从而推证类数有限、Dirichlet 单位定理等）。在几何与编码（格码）、数值分析苑地也有应用，是把连续体积信息转化为分立格点信息的典型工具。