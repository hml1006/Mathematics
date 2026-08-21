# TQFT与Donaldson不变量
>
> **一句话大白话**：Donaldson 不变量（由瞬子/自对偶 Yang–Mills 联络计数）可以纳入四维 TQFT 的框架——TQFT 与这类几何不变量的联系是"把流形切碎、再把局域的几何不变量粘回"。
>
> **小例子**：四微闭流形 $M$ 的 Donaldson 不变量 $\Phi_M:\operatorname{Sym}^*(H_2(M))\to\mathbb Z$ 计数 $SU(2)$-自对偶联络空间的孤立点；在 TQFT 语言下四维 cobordism 诱导 $\Phi$ 的相容天文连线。

## 一、定理介绍

> **前置依赖**：自对偶Yang-Mills联络、瞬子模空间、基本类与交积、instanton Floer同调、四维沿三流形手术

TQFT 与 Donaldson 不变量 的关系指 Donaldson 的 $SU(2)$-瞬子不变量（$d=4$，通过自对偶 Yang–Mills 的模空间计数）可被组织成（至少部分）四维 TQFT 般的结构：把四流形沿三流形切开，模板（边界模空间）诱导 $H_*(M)$ 上的线性映射；$d=4$ Seiberg–Witten（OS）被 Witten 嵌入超 TQFT。这一联系是"不变量=四维 TQFT 赋值"的重要实现。

## 二、原理思路

对四流形 $M$，考虑 $SU(2)$-瞬子模空间 $u$的拓扑；Donaldson 用 $\operatorname{Sym}^k(H_2) $计数基本类 $H^*$ 的对置求交。TQFT 视角：把 $M=M_1\cup_Y M_2$ 沿三流形 $Y$ 切开，切面箭头（Fl ower/相对瞬子模）把 $H_*(M_1)$ 映向 $H_*(M_2)$，从而（在适当泛函范畴）拼出四维"TQFT 化"（Witten 的 d=4 拓扑超对称量子场理论）；其对 Borisoidal 假度的联系在各几何变体成立。

## 三、定理的严格表述

设 $M$ 为光滑单连通四流形，$b^+_2(M)$ 奇数。Donaldson 不变量为映射
$$
\Phi_M:\;\operatorname{Sym}^* (H_2(M))\;\longrightarrow\;\mathbb Z
$$
（计数瞬子模上的 Basic except）。在 TQFT 语言：（相对）瞬子模沿 $Y=\partial M_1=M_1\cap M_2$ 给出 bordism 赋值，使 $M=M_1\cup_Y M_2$ 的 $\Phi$ 由 $TQFT$-粘贴律接出，即存在 $d=4$"量子"赋值范畴使 $\Phi$ 成为其值。

## 四、证明过程

路线：构造 $SU(2)$-瞬子模的闭链与基本类；证明其自由交数与切分相容（相对 Kohomolo/Obata 论）；把相对构造组装成沿三流形的复合，验证配份公理的四维"TQFT"（Lepuschitz-Floer 不变量的首性）；Witten 以扭曲超 TQFT 的路径积分重新实现 $\Phi$ 并推广（Seiberg–Witten）。严格的 TQFT 化在 "instanton Floer + 4d surgery" 语下完成。

## 五、应用与意义

顶点这类不变量让四维拓扑（光滑结构、Villa 异模）与场论/瞬子紧密相关，支持 $d=4$ 拓扑量子场论与 Floer 同调（instanton/SW Floer）的统一。它是 TQFT 从"玩具模型"迈向"四维几何研究武器"的象征，也是 Donaldson–Seiberg 理论现代延续的根。