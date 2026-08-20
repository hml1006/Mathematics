# Reshetikhin–Turaev不变量

> **一句话大白话**：给每个组成结"项链"的珠子（不可约表示）配上颜色，按拆解规则搭积木，最终得到的不变量不仅能区分纽结，还能给整个三维空间贴一个数字标签。
>
> **小例子**：取 $SU(2)$ 在二级别 $r$ 的模表示，用其 $6j$ 符号沿三角剖分求和，即得三维流形的不变量，并可计算如 $L(3,1)$ 等透镜空间的不变量。

## 一、定理介绍
Reshetikhin–Turaev 不变量是由 N. Reshetikhin 与 V. Turaev 在 1991 年严格构造的一类量子纽结不变量。它们从 ribbon/modular Hopf 代数的表示出发，不仅给纽结着色，还能进一步构造三维闭流形的不变量。

## 二、原理思路
将链环的每个分量用量子群的有限维表示“着色”，交叉由 $R$–矩阵表示，上下弯由对偶映射表示；这样整个链环图对应到单位对象上的一个标量。若表示范畴是模化的，则该标量在 Kirby 移动下不变，从而成为三维流形的不变量。

## 三、定理的严格表述
设 $H$ 为 ribbon Hopf 代数，其表示范畴 $\mathcal{C}=\operatorname{Rep}(H)$ 是 ribbon 范畴。对定向带框链环 $L=L_1\cup\cdots\cup L_m$，取简单模 $V_1,\dots,V_m\in\mathcal{C}$ 着色各分量，定义
$$
J_L(V_1,\dots,V_m)\in\operatorname{End}_{\mathcal{C}}(\mathbf{1})\cong\mathbb{C}
$$
为按链环图将 $R$–矩阵、余单位、对偶映射复合而成的态射。

若 $\mathcal{C}$ 是模 ribbon 范畴，令 $\{V_i\}_{i\in I}$ 为一组互不同构的简单对象的代表元，记 $\dim_i=\dim V_i$，且
$$
D^2=\sum_{i\in I}(\dim_i)^2,\qquad \Delta=\sum_{i\in I}(\dim_i)^2\theta_i^{-1}
$$
（$\theta_i$ 为 twist）。则对由带框链环 $L\subset S^3$ 经 Dehn 手术得到的闭定向三维流形 $M$，其 Reshetikhin–Turaev 不变量为
$$
\tau_{\mathcal{C}}(M)=\Delta^{\sigma(L)}D^{-\sigma(L)-m-1}\sum_{\lambda_1,\dots,\lambda_m\in I}
\left(\prod_{j=1}^m\dim_{\lambda_j}\right)
J_L(V_{\lambda_1},\dots,V_{\lambda_m}),
$$
其中 $\sigma(L)$ 为 $L$ 的 linking 矩阵的符号差，$m$ 为 $L$ 的分量数。

## 四、证明过程
1. **Ribbon 范畴不变性**：在 ribbon 范畴中，$R$–矩阵满足 Yang–Baxter 方程，twist $\theta_V$ 满足 ribbon 条件。于是任意带框链环图的着色值在 Reidemeister 移动（包括带框 R-I）下不变。
2. **手术表示**：Lickorish–Wallace 定理断言任意闭定向三维流形可由 $S^3$ 沿某带框链环 $L$ 的 Dehn 手术得到。
3. **Kirby 定理**：两个带框链环给出同胚的三维流形当且仅当它们可通过 Kirby 移动（handle slide 与 blow-up/down）互化。
4. **模性保证 Kirby 不变性**：模 ribbon 范畴的可逆 $S$–矩阵恰好对应 linking 矩阵的 handle slide；twist 与量子维数保证 blow-up/down 不变。因此上述求和式在 Kirby 移动下不变。
5. **结论**：$\tau_{\mathcal{C}}(M)$ 只依赖于 $M$ 的微分同胚类。

## 五、应用与意义
Reshetikhin–Turaev 不变量为 Witten 的 Chern–Simons 路径积分不变量提供了严格的代数实现，是拓扑量子场论与量子群表示论的交汇点；它们在拓扑量子计算、三维流形分类以及范畴化同调理论中都有深远影响。
