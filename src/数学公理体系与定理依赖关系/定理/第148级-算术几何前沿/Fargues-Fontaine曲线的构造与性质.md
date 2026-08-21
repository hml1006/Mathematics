# Fargues-Fontaine曲线的构造与性质
>
> **一句话大白话**：p-adic 世界里也有一条"射影直线"（Fargues–Fontaine 曲线），它用一个周期环把特征 0 与特征 p 连接，并为 p-adic Langlands 提供了几何舞台。
>
> **小例子**：定义在 $B_{\mathrm{cris}}$ 的 $\varphi$ 不动部分上：
$$
X=\mathrm{Proj}\Big(\bigoplus_{n\ge0}B_{\mathrm{cris}}^{\varphi=p^n}\Big),
$$
它是局部谱-射影曲线，闭点对应 p-adic 域上的完美化特征 p 域。

## 一、定理介绍

> **前置依赖**：perfectoid空间、Fontaine周期环$B_\mathrm{cris}$与$B_\mathrm{dR}$、Frobenius与$\varphi$-模块、射影$\mathrm{Proj}$构造、向量丛与分级模

Fargues–Fontaine曲线（Fargues–Fontaine 2018；2015）是 p-adic 几何中一条**过完备、分离、正则的一维曲线**，其坐标环由周期环 $B_\mathrm{cris}$ 的 $\varphi=p^n$ 部分构成：
$$
X=\mathrm{Proj}\Big(\bigoplus_{n\ge0} B_{\mathrm{cris}}^{\varphi=p^n}\Big).
$$
其闭点参数化（分级的）p-adic 局部域的完美化特征 p 域；其结构承载混合特征 p/0，被用作 p-adic Langlands 与 Hodge 理论的"基础曲线"。

## 二、原理思路

构造基于 $B_\mathrm{dR}$ 与 $B_\mathrm{cris}$ 的结构：对维度/完美化等 J. 置的加法集的不可约子概，用 $\varphi$-结构（同理 $p^n$ 特征）定义分次环。它同时（i）从根上连接了特征 p（完美空间）与特征 0（p-adic 域）——经 $k\to B_\mathrm{cris}^{\varphi=p^n}$ 的映射——且（ii）其几何（拟凝聚层、向量丛）由分级模刻画，故自然产生线丛$\mathcal O(1)$，模合 p-adic 平移。

## 三、定理的严格表述

设 $B_{\mathrm{cris}}$ 为 Fontaine 的晶体环（来自称原始 perfectoid），$\varphi$ 为其 Frobenius。定义
$$
X=\mathrm{Proj}\Big(\bigoplus_{n\ge0}B_{\mathrm{cris}}^{\varphi=p^n}\Big)
$$
（$A:=B_{\mathrm{cris}}^{\varphi=1}$ 可微的谱）。则：(1) $X$ 为过完备、正则、一维（全∥）曲线；(2) 闭点 $\leftrightarrow$ p-adic 域 $E$ 的优秀完美化 $E^\flat$ 的分级对应；(3) 其有无 $G_{K}$ 作用且 $\mathrm{Hom}(X,\mathbb A^1)$ 小；(4) 向量丛理论有"内核对偶"（π-L 分裂）。

## 四、证明过程

主步骤：建立 $B_{\mathrm{cris}}^{\varphi=p^n}$ 的分级代数并验证其 Noether/正则（用 perfectoid 周期方法）；证明 $\mathrm{Proj}$ 在局部特征下的浸入证之；用分级模/向量丛的对偶与线丛即可通过 $\mathrm{Proj}$ 实现整个分类，从而得到曲线的基本不变量（Picard、谱）。轨迹对闭点的分类则依赖 Fargues 的 $\varphi$-模块分类。

## 五、应用与意义

Fargues–Fontaine 曲线是 p-adic Langlands（Fargues–Scholze 的对应）、向量丛与 $\widehat T$-倩华和 Hodge 理论统一的舞台，也用于构造 $\mathbb B_\mathrm{dR}$ 的几何化、膨胀 Hodge 滤级与 Sh[tem] 对应，是现代 p-adic 几何命名标志。