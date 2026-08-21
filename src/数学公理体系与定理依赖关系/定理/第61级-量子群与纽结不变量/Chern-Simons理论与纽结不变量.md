# Chern–Simons理论与纽结不变量

> **一句话大白话**：一个纯拓扑的"作用量积分"定义的三维量子场论，把它一算，就能数出纽结的"打结程度"和三维空间的形状不变量——把抽象的量子物理转成了看得见的多项式。
>
> **小例子**：对 $SU(2)$ 的 Chern–Simons 理论，Wilson 圈的期望值给出 $SU(2)$ 量子不变量；沿二级别 $\,k\,$ 取极限还能回到经典的 Jones 多项式。

## 一、定理介绍

> **前置依赖**：Chern–Simons 作用量与规范不变性、Wilson 圈与紧 Lie 群的表示论、路径积分与典范量子化、WZW 模型共形块、Reshetikhin–Turaev 不变量。

1988 年 Edward Witten 提出，紧 Lie 群 $G$ 在三维流形上的 Chern–Simons 规范理论可以自然产生纽结与三维流形的量子不变量。该理论的配分函数与 Wilson 圈的期望值分别给出三维流形不变量与着色链环不变量。

## 二、原理思路
Chern–Simons 作用只依赖于联络的规范等价类与三维流形的拓扑，因而是拓扑场论。沿纽结插入带群表示的 Wilson 圈后，其路径积分期望值应当只依赖于纽结的同痕类；Witten 论证这些期望值与量子群/Reshetikhin–Turaev 不变量一致。

## 三、定理的严格表述
设 $M$ 为闭定向三维流形，$G$ 为紧 Lie 群，$\mathfrak{g}$ 为其李代数，$A\in\Omega^1(M,\mathfrak{g})$ 为 $\mathfrak{g}$–联络。Chern–Simons 作用为
$$
S_{CS}(A)=\frac{k}{4\pi}\int_M\operatorname{Tr}\left(A\wedge dA+\frac{2}{3}A\wedge A\wedge A\right),
$$
其中 $k\in\mathbb{Z}$ 为 level。

对定向纽结 $K\subset M$ 及 $G$ 的有限维表示 $R$，定义 Wilson 圈
$$
W_R(K)=\operatorname{Tr}_R\operatorname{P}\exp\left(\oint_K A\right).
$$

则链环 $L=\bigcup_{i=1}^m K_i$ 的期望值为
$$
\left\langle\prod_{i=1}^m W_{R_i}(K_i)\right\rangle
=\frac{1}{Z_k(S^3)}\int_{\mathcal{A}/\mathcal{G}}\mathcal{D}A\;
e^{iS_{CS}(A)}\prod_{i=1}^m W_{R_i}(K_i),
$$
其中配分函数 $Z_k(M)=\int_{\mathcal{A}/\mathcal{G}}\mathcal{D}A\,e^{iS_{CS}(A)}$。

Witten 断言：当 $M=S^3$ 且 $q=e^{2\pi i/(k+h^\vee)}$ 时，
$$
\left\langle\prod_{i=1}^m W_{R_i}(K_i)\right\rangle
=J_L(R_1,\dots,R_m),
$$
其中 $J_L$ 为对应量子群着色表示的 Reshetikhin–Turaev 不变量，$h^\vee$ 为 $\mathfrak{g}$ 的对偶 Coxeter 数。

## 四、证明过程
Chern–Simons 理论的严格数学证明目前仍部分依赖启发式路径积分，但可通过以下步骤与 Reshetikhin–Turaev 构造对应：
1. **规范不变性**：$S_{CS}(A^g)=S_{CS}(A)+2\pi k\cdot\mathrm{deg}(g)$，故 $e^{iS_{CS}}$ 在规范变换下不变。
2. **典范量子化**：取 $M=\Sigma\times\mathbb{R}$，Hilbert 空间 $\mathcal{H}_\Sigma$ 同构于 WZW 模型在 level $k$ 时的共形块空间。
3. **Wilson 圈作为算子**：沿曲面 $\Sigma$ 上曲线插入的 Wilson 圈给出 $\mathcal{H}_\Sigma$ 上的算子；其矩阵元只依赖于曲线的同痕类。
4. **配分函数与粘合**：对一般三维流形，沿曲面切割并粘合相应的共形块；所得结果与链环的 Reshetikhin–Turaev 值一致。
5. **手术/扰动对应**：对 $S^3$ 沿链环 $L$ 的 Dehn 手术，路径积分给出 Kirby 移动下的不变量；微扰展开则产生 Vassiliev 有限型不变量。

## 五、应用与意义
Chern–Simons 理论揭示了量子场论、量子群表示论与低维拓扑之间的深刻统一；它催生了拓扑量子场论的公理化，推动了 Gromov–Witten/拓扑弦对偶，并在量子引力与拓扑量子计算中持续发挥重要作用。
