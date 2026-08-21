# IFS吸引子的存在唯一性

> **一句话大白话**：给定一组压缩映射（迭代函数系统 IFS），在全体紧集组成、配有 Hausdorff 距离的空间里，"把这些压缩映射一起作用"这个操作本身也是压缩的，于是由 Banach 不动点定理必有一个唯一的吸引子。
>
> **小例子**：取 $f_1(x)=x/3$、$f_2(x)=x/3+2/3$，它的唯一吸引子就是经典 Cantor 集——从任意初始集合开始反复迭代都收敛到它。

## 一、定理介绍

> **前置依赖**：迭代函数系统（IFS）的定义、压缩映射、Hausdorff 距离、完备度量空间、Banach 不动点定理

本定理（Hutchinson 定理）奠定了迭代函数系统（IFS）的理论基础：一族压缩映射 $\{f_1,\dots,f_m\}$ 唯一地确定一个自相似"吸引子" $A$，满足 $A=\bigcup_i f_i(A)$。它是连接离散递归构造与连续极限集合的桥梁。

## 二、原理思路

把每个紧集 $K$ 对应到并集 $F(K)=\bigcup_i f_i(K)$。在由全体非空紧集构成的完备度量空间 $(\mathcal{K}(\mathbb{R}^n),d_H)$ 上，$F$ 的压缩比恰为 $\max_i r_i<1$。于是 Banach 不动点定理直接给出不动点 $A$（吸引子）及其存在唯一性，同时保证从任意初始紧集出发的迭代 $K_{k+1}=F(K_k)$ 以几何速率收敛。

## 三、定理的严格表述

（IFS 吸引子的存在唯一性）设 $\{f_1,\dots,f_m\}$ 是 $\mathbb{R}^n$ 上的 IFS，$f_i$ 的压缩比为 $r_i$，定义 $F:\mathcal{K}(\mathbb{R}^n)\to\mathcal{K}(\mathbb{R}^n)$ 为 $F(K)=\bigcup_{i=1}^m f_i(K)$，则 $F$ 是 $(\mathcal{K}(\mathbb{R}^n),d_H)$ 上的压缩映射（压缩比 $r=\max\{r_1,\dots,r_m\}$），存在唯一的不动点 $A$，即唯一吸引子，满足 $A=\bigcup_{i=1}^m f_i(A)$；且对任意初始紧集 $K_0$，迭代收敛到 $A$。

## 四、证明过程

**证：**

**第一步：$F$ 是压缩映射。** 任取 $K,L\in\mathcal{K}(\mathbb{R}^n)$，设 $x\in F(K)=\bigcup_i f_i(K)$，则存在 $i$ 与 $y\in K$ 使 $x=f_i(y)$。因 $L$ 紧，存在 $z\in L$ 使 $|y-z|=\inf_{w\in L}|y-w|$，于是
$$
d(x,f_i(L))\le|f_i(y)-f_i(z)|\le r_i|y-z|\le r_i\,d_H(K,L)
$$
故 $\sup_{x\in F(K)}d(x,F(L))\le r\,d_H(K,L)$，其中 $r=\max_i r_i$。对称地也有 $\sup_{x\in F(L)}d(x,F(K))\le r\,d_H(K,L)$，从而
$$
d_H(F(K),F(L))\le r\,d_H(K,L)
$$
因 $0\le r<1$，$F$ 是压缩映射。

**第二步：应用 Banach 不动点定理。** $(\mathcal{K}(\mathbb{R}^n),d_H)$ 完备且 $F$ 压缩，故 $F$ 存在唯一不动点 $A$，满足 $A=\bigcup_{i=1}^m f_i(A)$。

**第三步：收敛性。** Banach 不动点定理还给出迭代 $K_{k+1}=F(K_k)$ 收敛到 $A$，且
$$
d_H(K_k,A)\le\frac{r^k}{1-r}d_H(K_0,K_1)
$$
$\square$

## 五、应用与意义

本定理是分形构造的"通用机器"：Cantor 集、Sierpinski 三角形、Koch 曲线等都可通过指定有限个压缩相似映射而唯一确定，避免了逐级"手动递归"的繁琐。它还保证了随机与确定性迭代算法的收敛性，是图像压缩（分形编码）、自然景物建模的数学根基。