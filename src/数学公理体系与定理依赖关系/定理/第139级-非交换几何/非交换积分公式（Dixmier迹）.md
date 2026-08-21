# 非交换积分公式（Dixmier迹）

> **一句话大白话**：当常轨迹（普通迹）对某些算子+∞罢工时，Dixmier 迹用"奇异值的对数级平均再取极限"这个精巧办法，让很多"迹应为有限"的算子也能称出维数——它是非交换几何里"积分"的替身。
>
> **小例子**：$\mathrm{Tr}_\omega(T)=\lim_\omega\frac1{\log N}\sum_{n\le N}\lambda_n(T)$（$\lambda_n$ 为奇异值）；当极限存在且与 $\omega$ 无关即为 Dixmier 迹，可用于 $\int a=\mathrm{Tr}_\omega(a|D|^{-d})$ 定义非交换积分。

## 一、定理介绍

> **前置依赖**：紧算子与奇异值谱、自由超滤子极限、迹性质、Wodzicki留数与谱三元组

非交换积分公式（Dixmier 迹）给出在非交换几何中定义"积分"的方法。对可测算子 $T$（满足相关奇异值对数平均有界），定义
$$
\mathrm{Tr}_\omega(T)=\lim_{\omega}\frac{1}{\log N}\sum_{n=1}^{N}\lambda_n(T),
$$
其中 $\lim_\omega$ 沿自由超滤子 $\omega$ 的广义一致极限。Dixmier 迹是迹（满足 $\mathrm{Tr}_\omega(TS)=\mathrm{Tr}_\omega(ST)$、$\mathrm{Tr}_\omega(T^+)\ge0$、$\mathrm{Tr}_\omega(I)=+\infty$），与普通有限迹两者互相补充。借助它，非交换积分写作 $\int a=\mathrm{Tr}_\omega(a|D|^{-d})$。

## 二、原理思路

普通迹对紧算子的对角和收敛，但对 $I$（单位）与许多非紧算子发散。观测到奇异值之和对 $\log$ 的规范：若 $\lambda_n(T)\approx C(\log n)^{-1}$，则 $\frac1{\log N}\sum_1^N\lambda_n$ 有界地逼近 $C$。把有限和沿自由超滤子取极限，"聪明地求平均"砍掉振荡，得到与"求和顺序无关"的数值。这给非交换留数 $=$ 迹公式 $(\mathrm{Res}_{s=0})$ 提供基础，也用于度量 $d$ 维谱三元组中算子的维度信息。

## 三、定理的严格表述

设 $T$ 为 $\mathcal H$ 上紧算子，奇异值 $\lambda_n(T)$ 满足
$$
\sup_{N\ge1}\frac1{\log N}\sum_{n=1}^{N}\lambda_n(T)<\infty.
$$
则沿自由超滤子 $\omega$ 的广义一致极限
$$
\mathrm{Tr}_\omega(T)=\lim_\omega\frac{1}{\log N}\sum_{n=1}^{N}\lambda_n(T)
$$
存在，定义了一个迹（Dixmier 迹）。非交换积分由
$$
\int a=\mathrm{Tr}_\omega(a|D|^{-d})
$$
给出，且与谱三元组维度 $d$ 相关。

## 四、证明过程

**步骤1：动机。** 对 $T$ 若普通迹发散（$\sum\lambda_n=+\infty$），考察对数规范化：令 $\sigma_N(T)=\frac1{\log N}\sum_{n\le N}\lambda_n(T)$。

**步骤2：有界性假设。** 定理条件 $\sup_N\sigma_N(T)<\infty$ 保证序列有界。

**步骤3：自由超滤子极限。** 沿 $N\to\infty$ 的适当（自由）超滤子 $\omega$ 取广义一致极限，得
$$
\mathrm{Tr}_\omega(T)=\lim_\omega\sigma_N(T),
$$
其与求和顺序无关，良定。

**步骤4：迹性质。** 奇异值函数 $s\mapsto s_N(T)$ 满足有关性质的"对数可加"近似，可验证循环性 $\mathrm{Tr}_\omega(TS)=\mathrm{Tr}_\omega(ST)$、正性 $\mathrm{Tr}_\omega(T^+)\ge0$、以及 $\mathrm{Tr}_\omega(T)=0$ 当 $T$ 本质谱为零（一致到对数阶衰减）。

**步骤5：非交换积分。** 对谱三元组，定义 $\int a=\mathrm{Tr}_\omega(a|D|^{-d})$；它满足迹性质并给出 $d$-维的"体积"式标量。Dixmier 迹与非交换留数 $\mathrm{Res}_{s=0}\mathrm{Tr}(a|D|^{-s})$ 在网络（可测算子代数的"对数维"）一致。

**结论（$\square$）**：Dixmier 迹良定地给出非交换积分公式。

## 五、应用与意义

Dixmier 迹是非交换几何中构建积分"而非求和"的基石，用于定义谱维度、非交换留数、Connes 度量与迹公式，并支撑局部指标公式中的 $\int a$。它在叶状结构、超交换几何的 Wodzicki 留数联系以及"关于退化数算子的积分几何"中必不可少，是"无点空间上的积分学"核心工具。