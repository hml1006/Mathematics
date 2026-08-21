# Roth 定理

> **一句话大白话**：$\{1,\dots,N\}$ 中任何"正密度"子集（$|A|\ge\delta N$）都藏着一个非平凡的三项算术级数 $x,x+d,x+2d$（$d\ne0$）。密度够高，等差三连"藏不住"。
>
> **小例子**：$N=100$、$\delta=0.3$，任意 30 个数里必有三项等差。Roth 定理保证了这一点，且 $\delta$ 只需为任意固定的正数。

## 一、定理介绍

Roth 定理（1953）是加法组合的经典结果：对任意 $\delta>0$ 存在 $N_0(\delta)$，使 $N>N_0(\delta)$ 时正密度集 $A\subseteq\{1,\dots,N\}$（$|A|\ge\delta N$）必含非平凡三项算术级数。它是密度算术级数理论的开端，Szemerédi 定理（任意长度）的原型。

## 二、原理思路

用傅里叶分析（密度增量策略）。把数嵌入 $\mathbb{Z}_N$，考虑特征函数 $f$。三项级数计数 $\sum_x f(x)f(x+d)f(x+2d)$ 用傅里叶系数表示 $\frac1N\sum_\xi\hat f(\xi)^2\hat f(-2\xi)$。主导项来自 $\xi=0$ 为 $\delta^3N^2$。若无三项级数，则总和 $O(N)$，迫使非零频率系数 $|\hat f(\xi)|\ge c\delta^2N$ 大；按该频率方向分划得一个子算术级数上密度增量 $\delta\to\delta+c\delta^2$。迭代 $O(1/\delta)$ 次（密度不能超 1）得到 $N_0(\delta)\le\exp(\exp(O(1/\delta)))$。

## 三、定理的严格表述

对任意 $\delta>0$，存在 $N_0(\delta)$，使 $N>N_0(\delta)$ 时，集合 $A\subseteq\{1,2,\dots,N\}$ 若 $|A|\ge\delta N$，则 $A$ 含非平凡三项算术级数 $x,x+d,x+2d$（$d\ne0$）。

## 四、证明过程

**证明（傅里叶分析/密度增量）：**

**步骤 1：嵌入与傅里叶。** 将 $A$ 视为 $\mathbb{Z}_N$ 子集（$N$ 素数），特征函数 $f$。三项级数等价于 $\sum_{x,d}f(x)f(x+d)f(x+2d)>0$（$d\ne0$）。$\blacksquare$

**步骤 2：级数计数公式。** 
$$\sum_{x,d}f(x)f(x+d)f(x+2d)=\frac1N\sum_{\xi}\hat f(\xi)^2\hat f(-2\xi),\qquad \hat f(\xi)=\sum_x f(x)e^{-2\pi i\xi x/N}.$$
主项：$\xi=0$ 贡献 $\frac1N\hat f(0)^3=\delta^3N^2$。$\blacksquare$

**步骤 3：无三项级数情形。** 若 $A$ 无三项级数，总和为 $O(N)$（仅 $d=0$ 平凡解），故
$$\Big|\frac1N\sum_{\xi\ne0}\hat f(\xi)^2\hat f(-2\xi)\Big|\ge c\delta^3N^2.$$
由 Cauchy-Schwarz/Hölder 得存在 $\xi\ne0$ 使 $|\hat f(\xi)|\ge c\delta^2N$。$\blacksquare$

**步骤 4：构造密度增量。** 频率 $\xi\ne0$ 显著时，把 $\mathbb{Z}_N$ 按 $\xi$ 方向分成约 $\delta^{-2}$ 长的算术级数；由三角不等式存在某子级数 $P$（$|P|\approx N^{1/2}$）使 $A$ 在 $P$ 上密度 $\ge\delta+c\delta^2$。$\blacksquare$

**步骤 5：迭代。** 令 $\delta_0=\delta$，$\delta_{i+1}=\delta_i+c\delta_i^2$；因 $\delta_i\le1$，迭代 $O(1/\delta)$ 次内密度达 1（含满级数即有三项级数）或原 $N$ 缩小到 $N^{1/2}$ 后己找到。故 $N_0(\delta)\le\exp(\exp(O(1/\delta)))$（Bloom-Sisask 后来改进）。$\square$

## 五、应用与意义

Roth 定理是现代 additive combinatorics 的标杆，它把"密度型"问题与调和分析结合，激发 Szemerédi 定理（一般长度）、Gowers 范数（高维）、密度增技术与筛法深度结合。在三元甚至多元的算术组合（稀疏 Ramsey 数、弱 Ruzsa-Szemerédi）、以及"结构 vs 随机"二分、Bourgain 的独立傅里叶与格积技术中均属奠基并可推广。它的量级谱系尚在积极改进（Bloom-Sisask、2024 上限~$\exp(-c(\log N)^{1/12})$）。