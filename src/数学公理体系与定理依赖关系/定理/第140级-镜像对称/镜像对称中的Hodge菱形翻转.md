# 镜像对称中的Hodge菱形翻转

> **一句话大白话**：镜像对称最直观的"指纹"：镜像流形的 Hodge 数把另一边的 Hodge 菱形"上下翻转"——$M$ 的 $h^{p,q}$ 等于 $W$ 的 $h^{n-p,q}$。数数 Hodge 数就能认出谁是"镜像对"。
>
> **小例子**：三次 Calabi-Yau 3-重有 $h^{1,1}=1$、$h^{2,1}=101$，镜像则 $h^{1,1}=101$、$h^{2,1}=1$——正是 $h^{p,q}(M)=h^{n-p,q}(W)$（$n=3$）。

## 一、定理介绍

> **前置依赖**：Hodge分解与Serre对偶、变化Hodge结构（VHS）、Kodaira-Spencer理论、同调镜像对称

Hodge 菱形翻转定理断言：若 $M,W$ 为镜像对称的 $n$ 维 Calabi-Yau 流形，则
$$
h^{p,q}(M)=h^{n-p,q}(W).
$$
它是镜像对称最直接可验证的数值证据——识别镜像对的标准"指纹"。

## 二、原理思路

镜像映射在复结构模空间 $\mathcal M_{cs}(M)$ 与 Kähler 模空间 $\mathcal M_{\mathrm{K\"ah}}(W)$ 之间建立局部同构。切空间理论给出关键配对：Kodaira-Spencer 表明 $T\mathcal M_{cs}(M)\cong H^{n-1,1}(M)$，而 $T\mathcal M_{\mathrm{K\"ah}}(W)\cong H^{1,1}(W)$，故镜像映射诱导 $H^{n-1,1}(M)\cong H^{1,1}(W)$。高阶 Hodge 数由变化 Hodge 结构（周期映射）推广并由同调镜像对称的 Hochschild 同调一致性最终验证。

## 三、定理的严格表述

设 $M,W$ 为镜像 $n$-Calabi-Yau，存在镜像映射 $\Phi:\mathcal M_{cs}(M)\to\mathcal M_{\mathrm{K\"ah}}(W)$，其切映射诱导
$$
H^{n-1,1}(M)\cong H^{1,1}(W),
$$
并贯穿 Hodge 菱形：$h^{p,q}(M)=h^{n-p,q}(W)$（$0\le p,q\le n$）。

## 四、证明过程

**步骤1：Hodge 数的变形性质。** 复结构变形下 Hodge 滤过变化但一般点 Hodge 数稳定；Hodge 分解 $H^k=\bigoplus_{p+q=k}H^{p,q}$，$H^{p,q}\cong H^q(M,\Omega^p)$。

**步骤2：Calabi-Yau 的 Hodge 约束。** $h^{0,0}=h^{n,n}=1$，$h^{n,0}=h^{0,n}=1$，Serre 对偶 $h^{p,q}=h^{n-p,n-q}$ 限制菱形外围。

**步骤3：构造镜像映射的切向。** 切空间同构 $T\mathcal M_{cs}(M)\cong H^{n-1,1}(M)$、$T\mathcal M_{\mathrm{K\"ah}}(W)\cong H^{1,1}(W)$，故 $d\Phi$ 给出 $H^{n-1,1}(M)\cong H^{1,1}(W)$（即 $h^{n-1,1}=h^{1,1}$）。

**步骤4：推广到高阶 Hodge。** 变化 Hodge 结构（VHS）与周期映射 $\mathcal P:\mathcal M_{cs}\to\mathcal D/\Gamma$ 保持 Hodge 滤过结构；镜像映射在周期域之间诱导同构并翻折 Hodge 菱形。

**步骤5：构造性验证。** 五次 Calabi-Yau 3-重 $h^{1,1}=1$、$h^{2,1}=101$、镜像 $h^{1,1}=101$、$h^{2,1}=1$，满足 $h^{p,q}(M)=h^{3-p,q}(W)$，其余 Hodge 块由 Serre 对偶与翻转规则相符，验证菱形确实翻转。

**步骤6：同调代数验证。** 由同调镜像对称，$\mathcal F(M)$ 与 $D^b\mathrm{Coh}(W)$ 的 Hochschild 同调分别给出 $h^{p,q}$；范畴等价使 Hochschild 同调同构，故 Hodge 菱形翻转成立。

**结论（$\square$）**：镜像对满足 $h^{p,q}(M)=h^{n-p,q}(W)$。

## 五、应用与意义

Hodge 菱形翻转是镜像效应的第一个数值例证与识别工具，广泛用于构造与检验镜像对、寻找 Calabi-Yau 反射（如光学模空间）。它把"是否互为镜像"简化为可计算的 Hodge 数核对，是镜像对称从猜想走向实用鉴别的可靠抓手。