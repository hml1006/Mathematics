# 局部Langlands对应

> **一句话大白话**：局部域上游的 $GL_n$ 不可约光滑表示，正好和 $(n$ 维 Weil 表示 $+$ 一个 $SL_2(\mathbb{C})$ 参数$)$ 一一对应，而且这种对应唯一。
>
> **小例子**：对 $n=2$、$F=\mathbb{Q}_p$，主序列表示 $\mathrm{Ind}(\chi_1\otimes\chi_2)$ 对应由分量的 Weil 表示与 $SL_2$ 权重拼成的二维 Langlands 参数。

## 一、定理介绍

> **前置依赖**：Weil表示与L-群参数、超cuspidal表示与抛物诱导、局部Galois上同调、ε-因子理论、类体论（n=1情形）

局部Langlands对应（Harris–Taylor / Henniart）把局部域 $F$（$\mathbb{R}$、$\mathbb{C}$ 或 $\mathbb{Q}_p$ 的有限扩张）上 $GL_n(F)$ 的不可约（光滑、生成）表示与所谓 $(n$ 维) Langlands 参数——即 $W_F\times SL_2(\mathbb{C})$ 的（半单、在 $SL_2$ 上代数）表示——建立起唯一双射。它是全局对应在单点"纤维化"后的局部版本。

## 二、原理思路

其基本想法是：每个光滑不可约表示对应一个 $L$-群元，即 $\ell$-adic 参数 $W_F\to{}^L G$。在 $G=GL_n$、$^LG=GL_n$ 时，参数简化为 $W_F\times SL_2(\mathbb{C})$ 的 $n$ 维表示。对应要求保持"秩"— 利用超cuspidal 表示与 Weil 表示之间的先验对应（经 Local Langlands 若尔当分解），并藉由局部 Galois 上同调与 $\varepsilon$-因子的限制来确定唯一性。

## 三、定理的严格表述

设 $F$ 为特征零局部域。存在唯一双射 $\pi\mapsto\mathrm{L\varphi}_\pi$：
$$
\mathrm{Irr}(\operatorname{GL}_n(F))\longleftrightarrow\{\text{半单参数 }\varphi:W_F\times SL_2(\mathbb{C})\to GL_n(\mathbb{C})\}/\text{共轭}
$$
满足以下性质：对每个满足充分约化的参数，$GL_n(F)$ 的相应 $L$-群元给出 $L(s,\pi)=L(s,\varphi)$ 与 $\varepsilon(s,\pi,\psi)=\varepsilon(s,\varphi,\psi)$，且与每一个良定义的局部 $\gamma$-因子相容。

## 四、证明过程

关键步骤是用归纳与压缩方法先对 $n=1$ 建立（类体论），再对超cuspidal 表示用 explicit local correspondence（Bushnell–Henniart / Harris–Taylor）构建参数，然后通过"诱导保持"将一般表示分解为超cuspidal 表示的抛物诱导，从而拼出完整对应。Henniart 用"特征理想"论证以及 $\varepsilon$-因子强单调性确定了对应唯一性；Harris–Taylor 则从简单 Bershtein 表示出发构造并验证了全部 L-与 $\varepsilon$-因子。

## 五、应用与意义

局部Langlands对应是 Langlands 纲领的基石之一：它给出局部 Langlands 函子性、局部上同调（Shimura 簇）的自守分解，以及在 $p$-adic Langlands 与算术几何（陷阱奇点、模形式局部行为）中扮演分析中枢。任何全局对应的验证最终都要求逐位局部对应成立。