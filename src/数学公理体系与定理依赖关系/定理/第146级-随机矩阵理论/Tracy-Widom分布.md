# Tracy-Widom分布

> **一句话大白话**：随机矩阵最大特征值的随机起伏，在缩放后收敛到一个普适分布（Tracy–Widom），它描述"边缘统计"并普适了谱的极值行为。
>
> **小例子**：GUE 的最大特征值 $\lambda_{\max}=(2\sqrt n+\text{尺度}n^{-1/6})\chi$，其中 $\chi$ 服从 $\beta=2$ Tracy–Widom 分布，其尾部与 Airy 核有关。

## 一、定理介绍

Tracy–Widom分布（TW，Tracy–Widom 1994）描述的是随机矩阵谱的最大特征值（更一般地，谱边缘）经 $n^{-1/6}$ 缩放后的普适极限分布族 $\mathrm{TW}_\beta$（$\beta=1,2,4$ 对应 GOE/GUE/GSE）。它以 Airy 函数/行列式点过程（Fredholm 行列式）表达，是随机矩阵、KPZ 普适类与最值过程的核心对象。

## 二、原理思路

对于 $\beta=2$（GUE 复 Hermite），Gaudin/Mehta 的软边缘公式给出点过程行列式核：Airy 核 $K_{\mathrm{Ai}}(x,y)=\frac{\mathrm{Ai}(x)\mathrm{Ai}'(y)-\mathrm{Ai}'\!\mathrm{Ai}(y)…}{x-y}$。最大特征值的分布即该核的 Fredholm 行列式 $\det(I-\lambda K_{\mathrm{Ai}})$。缩放尺度 $\cdot n^{-1/6}$ 来自边缘的宽度（与 Airy 波形散度 $x\sim n^{1/3}$ 相匹配）。

## 三、定理的严格表述

设 $W$ 为 $n\times n$ 单位方差 GUE（或 GOE）。存在常数 $c_\beta$ 使，对 $\lambda_{\max}$ 归一：
$$
\lim_{n\to\infty}\mathbb P\!\Big(\frac{\lambda_{\max}-2\sqrt n}{c_\beta n^{-1/6}}\le s\Big)=F_\beta(s),
$$
其中
$$
F_2(s)=\det(I-K_{\mathrm{Ai}})\big|_{L^2(s,\infty)}=\exp\Big(-\int_s^\infty (x-s)\,u(x)^2\,dx\Big),
$$
$u$ 满足 Painlevé II $u''=2u^3+x u$、$u\sim\mathrm{Ai}(x)$ 且 $u(+\infty)\to0$。GOE（$\beta=1$）与 GSE（$\beta=4$）用类似核与 $F_1,F_4$ 表出。

## 四、证明过程

对 $\beta=2$：由 GUE 特征值的联合密度及 Mehta 型行列式公式给出边缘点过程核 $K_{\mathrm{Ai}}$；证明最大点分布等于 $\det(I-\mathbf 1_{(s,\infty)}K_{\mathrm{Ai}})$；借 Grassmann 变量或直接行列式论证得到 Painlevé II 表示（Tracy–Widom 用 Fredholm + integrable 核 + 双正交多项式的 $u$ 方程）。$\beta=1,4$ 以 Pfaffian/双核推进。再以 Edge universality 定理把结果推广到一般 Wigner 矩阵。

## 五、应用与意义

Tracy–Widom 分布是随机矩阵最大特征值/谱边缘的普适极限，同时作为 KPZ 普适类、扩散（首选数学物理）与数论（L-函数峰值）的模型量纲，广泛出现在统计（PCA）、格模型与演化方程（Airy 过程）的研究里。