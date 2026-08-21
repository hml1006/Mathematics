# 量子迹与 Jones 多项式的关系

> **一句话大白话**：Jones 纽结多项式可以由量子群 $U_q(\mathfrak{sl}_2)$ 的表示"加权求和"（量子迹）算出：$V_L(t)=\operatorname{qtr}_{V_1^{\otimes|L|}}(\text{缠绕算子})$，其中 $t=q^4$。
>
> **小例子**：三叶结 $\mathrm{Trefoil}$ 经闭辫子表示后取量子迹，算得 $V_{\mathrm{Trefoil}}(t)=t^{-1}+t^{-3}-t^{-4}$——这个多项式是纽结不变量，反映了量子群编码的"辫子信息"。

## 一、定理介绍

> **前置依赖**：Kauffman 括号与 skein 关系、R-矩阵与辫子群表示、Markov 定理、Alexander 定理、$U_q(\mathfrak{sl}_2)$ 的表示分类。

该定理（Turaev-Reshetikhin 定理的特例，源出 Jones 1985）把纽结的 Jones 多项式用量子群表示论的量子迹实现：通过 $U_q(\mathfrak{sl}_2)$ 的二维表示与 $R$-矩阵，把纽结配成辫子，再由 $K$ 加权的量子迹取迹，得到一个纽结不变量。它搭建了量子群与低维拓扑之间的桥梁。

## 二、原理思路

Jones 多项式先由 Kauffman 括号（满足 skein 关系）构造。量子方面，$R$-矩阵在二维表示 $V_1$ 上给出辫子群 $B_n$ 的表示，量子迹 $\operatorname{qtr}(f)=\operatorname{tr}(f\circ K^{\otimes n})$（$K$ 对第 $i$ 个因子按权加权）把封闭辫子映射到数字。关键是验证量子迹满足 Kauffman 括号的 skein 关系（令 $t=q^4$），再由 Markov 移动不变性证明所得确是纽结不变量，并与 Jones 多项式一致。

## 三、定理的严格表述

设 $L$ 是纽结或链环，$V_L(t)$ 是 Jones 多项式。则存在 $U_q(\mathfrak{sl}_2)$ 的二维不可约表示 $V_1$，使 Jones 多项式可表示为量子迹：
$$
V_L(t)=\operatorname{qtr}_{V_1^{\otimes|L|}}(\text{缠绕算子}),
$$
其中 $|L|$ 是 $L$ 的分支数，$t=q^4$，缠绕算子由 $R$-矩阵与辫子作用给出。等价地，对闭辫子 $\beta$：$V_L(t)=\frac{(-t^{-3/4})^{w(\beta)}}{d^{n-1}}\operatorname{qtr}(\beta)$，其中 $d=q+q^{-1}$。

## 四、证明过程

**证明（框架）：**

**步骤 1：Kauffman 括号与 Jones 多项式。** $V_L(t)=(-t^{-3/4})^{w(L)}\langle L\rangle$，其中括号由 skein 关系定义。

**步骤 2：量子群表示与辫子表示。** $V_1$ 上的 $R$-矩阵给出 $B_n$ 表示：$\sigma_i\mapsto\operatorname{id}^{\otimes(i-1)}\otimes\check{R}\otimes\operatorname{id}^{\otimes(n-i-1)}$，$\check{R}=\tau\circ R$。

**步骤 3：$R$ 在 $V_1\otimes V_1$ 上的作用。** 在基 $\{v_0,v_1\}$ 上：
$$
R(v_0\otimes v_0)=q^{1/2}v_0\otimes v_0,\quad R(v_0\otimes v_1)=q^{-1/2}v_1\otimes v_0+(q^{-1/2}-q^{3/2})v_0\otimes v_1.
$$
（其余两组对称类似。）

**步骤 4：量子迹定义。** $\operatorname{qtr}(f)=\operatorname{tr}(f\circ K^{\otimes n})$。

**步骤 5：验证 skein 关系。** 直接计算得 $\operatorname{qtr}(\operatorname{id})=q+q^{-1}=d$，以及 $\operatorname{qtr}(\sigma_i)-\operatorname{qtr}(\sigma_i^{-1})=(t^{1/4}-t^{-1/4})\operatorname{qtr}(\operatorname{id})$，即括号的 skein 关系。

**步骤 6：构造 Jones 多项式。** 任一纽结可配成闭辫子 $\beta$（Alexander 定理），定义 $V_L(t)=\frac{(-t^{-3/4})^{w(\beta)}}{d^{n-1}}\operatorname{qtr}(\beta)$，验证其在 Markov 移动下不变且满足 Jones 多项式公理，故与 Jones 多项式一致。$\square$

## 五、应用与意义

该定理使 Jones 多项式有了深刻的量子群诠释，开创了"量子不变量"研究：把它推广到任意量子群与任意表示即得 Reshetikhin-Turaev 不变量、Witten-Turaev-Viro 3 流形不变量，与 Chern-Simons 拓扑量子场论（$SU(2)$）对应。它在低维拓扑、拓扑量子计算（拓扑维度、简并基态的信息编码）与统计力学（可积模型）之间架起桥梁，也是纽结表、DNA 拓扑与链环分类研究的重要工具。