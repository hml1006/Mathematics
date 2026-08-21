# 全局Langlands对应（Drinfeld的shtuka构造）

> **一句话大白话**：对函数域，全局Langlands对应可以完全被构造出来——尖点自守形式对应的 Galois 表示来自一种特殊的几何对象"pants（shtuka）"，这使抽象猜想变成一个可计算的几何定理。
>
> **小例子**：对 $\mathbb{F}_q(T)$ 上的 $GL_2$ 文档模形式，Drinfeld 从某种意义上构造了一个对应的二维 Galois 表示，其 L-函数与自守形式 L-函数相等。

## 一、定理介绍

> **前置依赖**：shtuka理论、向量丛与Frobenius结构、ℓ-adic层与Galois表示、函数域上的L函数、局部-全局相容性

全局Langlands对应（Drinfeld）针对**函数域** $K=\mathbb{F}_q(T)$ 等（有限特征、整体域）建立了自守表示与全局Galois表示的完整对应。与数域的经典情形不同，在函数域上可以通过几何对象——shtuka——真正构造出使得 L-函数匹配的 Galois 表示，从而构成全局对应在"pants 语言学"下的具体实现。

## 二、原理思路

其核心思想是把函数域上的算术对象"几何化"：考虑曲线 $X$ 及其解空间，可构造一种带 Frobenius 结构的向量丛（shtuka），它把一个点（其坐标由自守信息给出）的某种"形变数据"与 Galois 表示编码在一起。Drinfeld 正是利用这种 shtuka 从自守表示读出 Frobenius 特征值，从而整体地确定 Galois 表示。

## 三、定理的严格表述

设 $K$ 为特征 $p$ 的全局函数域，丝 $F$ 为某光滑曲线。则对 $K$ 上的 $GL_2$ 尖点自守表示 $\pi$，存在唯一二（误差有界）维 $\ell$-adic Galois 表示 $\rho_\pi:\operatorname{Gal}(\bar{K}/K)\to GL_2(\bar{\mathbb{Q}}_\ell)$，满足对任意处于（未约化、分歧点之外的）位置 $v$，有
$$
L_v(s,\rho_\pi)=L_v(s,\pi).
$$
更一般地，该构造对幂等自守表示给出相应阶数的Galois表示，且局部-全局相容。

## 四、证明过程

总路线：先在函数域上用 Drinfeld 的 shukta 理论构造表示。给定自守表示，构造其对应的 shtuka（它给出 Frobenius 与"啜变"的交换图）。对每处分歧位取局部条件确定局部表示；最后对比所得的 Frobenius 特征值给出 L-函数等式。证明中用到 $\ell$-adic 层的定值与多项式恒等比较，并以 Bôch…Dawis 保持局部-全局相容固定表示。

## 五、应用与意义

这是 Langlands 对应中第一个"完全构造"的非平凡成果（n=2），确立了函数域上抽象的对应可以被具体几何对象实现。它开创了用几何（层、shtuka、moduli栈）驱动算术对应的先例，并直接影响了几何Langlands和后来在 $p$-adic 算术几何中的对应构造。