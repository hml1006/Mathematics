# 三维Chern-Simons理论与Jones多项式
>
> **一句话大白话**：Jones 多项式不是"发明"的，而是 $SU(2)$ Chern–Simons 理论中沿纽结的 Wilson 圈期望值——Witten 给出了它的几何涵义。
>
> **小例子**：对 $SU(2)$、level $k$，Jones 多项式
$$
V_L(t)\;\text{与}\;\langle W_L\rangle = Z_{SU(2),k}(M,L),\qquad t=e^{2\pi i/(k+2)},
$$
经 Witten 由路径积分得到。

## 一、定理介绍

三微 Chern–Simons 理论与 Jones 多项式（Witten 1989）：$d=3$、规范群 $G$、level $k\in\mathbb Z$ 的 Chern–Simons 理论给出一个三维 TQFT，其对纽结 $L$ 的 Wilson 圈期望值正比于 $L$ 的 Jones 多项式（$G=SU(2)$ 基本表示时）。由此 Jones 多项式获数学意义下的微-几何表述，并作为 $q=e^{2\pi i/(k+2)}$ 处的亏照（值）。

## 二、原理思路

三维 Chern–Simons 作用量 $S_{\mathrm{CS}}=\frac{k}{4\pi}\int_M\operatorname{Tr}(A\wedge dA+\frac23 A\wedge A^3)$ 是拓扑（高规不变、只在 $k\in\mathbb Z$ 时量子化）。其配分函数
$$
Z_{\mathrm{CS}}(M)=\int_{\mathcal A/\mathcal G}\mathcal DA\,e^{iS_{\mathrm{CS}}(A)}
$$
与 Jones 多项式经"Wilson 圈 + 用量子群表示论/skein 恒等式"联系：Witten 从路径积分推导出 skein 关系（$L_+,L_-,L_0$），其系数蕴含 level $\leftrightarrow t$。

## 三、定理的严格表述

对三维定向闭流形 $M$、紧 Lie 群 $G$、level $k$，Chern–Simons 配分函数
$$
Z_{\mathrm{CS}}(M)=\int_{\mathcal A/\mathcal G}\mathcal DA\; e^{\,i\frac{k}{4\pi}\int_M\operatorname{Tr}(A\wedge dA+\frac23 A\wedge A\wedge A)}
$$
对纽结 $L$ 与表示 $R$ 定义 Wilson 圈期望 $\langle W_R(L)\rangle$。则（$G=SU(2)$，$R$ 基本）：
$$
\langle W_R(L)\rangle \;=\; V_L\big(e^{2\pi i/(k+2)}\big),
$$
当 $M$ 为合适三流形且规范化 ${V_{\text{unknot}}}=1$。

## 四、证明过程

Witten 论证分：(1) 用路径积分反推 skein 关系——考虑 crossing 微变，Wilson 圈期望满足 $t^{-1}\langle W(L_+)\rangle-t\langle W(L_-)\rangle=(t^{-1/2}-t^{1/2})\langle W(L_0)\rangle$，设 $t=e^{2\pi i/(k+2)}$；(2) 由 skein + 规范化 $V_{\text{unknot}}=1,H$ 得 Jones 多项式；(3) Reshetikhin–Turaev 用 $U_q(\mathfrak{sl}_2)$（$q$ 根单位）R-矩阵给出严格代数证明，使 $t^{…}$ 精确。

## 五、应用与意义

Witten 的这项发现在 3-流形不变量（Turaev–Viro、RT）与纽结理论间架桥，把 Jones 多项式、量子 $6j$-符号与 Chern–Simons TQFT 统一，并催生 TQFT 与"几何拓扑—量子场论"深入交互；其产物（skein、模范畴）至今是低维拓扑与量子群研究的动力。