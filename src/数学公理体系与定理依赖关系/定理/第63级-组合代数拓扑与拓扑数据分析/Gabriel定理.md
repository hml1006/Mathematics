# Gabriel 定理

> **一句话大白话**：一个箭图（有限的有向图）上的"表示"只有有限多个积木块，当且仅当它的底图是 A、D、E 型 Dynkin 图；此时积木块与根系的正根一一对应。
>
> **小例子**：$A_3$ 型箭图 $1\to2\to3$ 恰有 $6$ 个不可分解表示，对应 $A_3$ 的 $6$ 个正根，分别是区间表示 $I[1,1)$、$I[2,2)$、$I[3,3)$、$I[1,2)$、$I[2,3)$、$I[1,3)$——即长度 $1$、$2$、$3$ 的区间模各一个。

## 一、定理介绍

> **前置依赖**：主理想整环上的有限生成模结构定理、箭图与路径代数、Krull–Schmidt定理、Dynkin图与根系（概念）、反射函子（概念）。

Gabriel 定理（Gabriel's theorem）由 Pierre Gabriel 于 1972 年在《Unzerlegbare Darstellungen I》中证明，是箭图表示论的开创性结果。它回答了"哪些代数是有限表示型"这一基本问题：有限连通箭图 $Q$ 上的有限维表示只有有限多个不可分解对象，当且仅当 $Q$ 的底图属于 $A_n$、$D_n$、$E_6$、$E_7$、$E_8$ 这五类 Dynkin 图；并且此时不可分解表示与对应根系的正根一一对应，由维数向量分类。

定理的动机来自 1960—1970 年代表示论对"分类问题"的追求：对有限维代数 $A$，其有限维模的不可分解对象何时只有有限多个？Gabriel 的答案把这一代数问题转化为纯组合的分类（Dynkin 图），并用 Tits 二次型的正定性作为判据。稍后 Bernstein–Gelfand–Ponomarev 的反射函子给出了构造性的证明，Kac 进一步把结论推广到一般箭图（不可分解表示与正根系对应，虚根对应无穷多表示）。

定理的意义有四层。其一，它把有限表示型代数与 Dynkin 图、根系、Coxeter 群联系在一起，是代数表示论的纲领性结果，并催生了丛倾斜（cluster tilting）、预投射代数等理论。其二，$A_n$ 型情形恰是拓扑数据分析中持久模的代数模型：$A_n$ 型箭图的表示就是持久模，Gabriel 定理直接给出区间分解与 barcode（参见区间分解定理）。其三，它是 Kac–Moody 代数、量子群与箭图表示之间联系的组合起点。其四，它与主理想整环上有限生成模结构定理、Krull–Schmidt 定理共同构成"分解定理"的三根支柱。

## 二、原理思路

1. **表示与路径代数**：箭图 $Q$ 的 $k$-线性表示就是路径代数 $kQ$ 的有限维模；"不可分解"即不能写成两个非零表示的直和，"有限型"即不可分解对象只有有限多个同构类。

2. **Tits 二次型判据**：定义 $q_Q(x)=\sum_i x_i^2-\sum_{a:i\to j}x_ix_j$。$q_Q$ 正定当且仅当底图是 Dynkin 图；半正定（含零根）当且仅当底图是 extended/affine Dynkin 图。

3. **必要性（affine 情形喷出无穷多表示）**：若底图含 affine 子图，其零根 $\delta$ 上可构造以 $k^*$ 为参数的不可分解表示族，故非有限型。

4. **充分性（反射函子的归纳）**：用 BGP 反射函子沿源/汇顶点改变箭图定向并保持不可分解性，把任意 Dynkin 箭图的表示逐步约化到更小的 Dynkin 图，归纳得有限型。

5. **根系对应**：用维数向量 $\underline{\dim}M$ 把不可分解表示映到正根，反射函子的等价性保证这是双射。

## 三、定理的严格表述

**定理（Gabriel 1972）**：设 $Q$ 是有限的连通箭图，$k$ 是域，$\operatorname{rep}_k(Q)$ 为 $Q$ 的有限维 $k$-线性表示范畴。则 $\operatorname{rep}_k(Q)$ 是有限表示型（即不可分解对象只有有限多个同构类）当且仅当 $Q$ 的底图 $\bar Q$ 是 Dynkin 图
$$\bar Q\in\{A_n\ (n\geq1),\ D_n\ (n\geq4),\ E_6,\ E_7,\ E_8\}.$$
此时不可分解表示的同构类与相应根系的正根 $\Phi^+$ 一一对应：
$$\{\text{不可分解表示的同构类}\}\ \longleftrightarrow\ \Phi^+,\qquad [M]\mapsto\underline{\dim}M,$$
并且维数向量唯一决定同构类，故不可分解表示的个数为 $\lvert\Phi^+\rvert$。

**$A_n$ 情形的显式分类**：取 $A_n$ 型箭图 $1\to2\to\cdots\to n$。其正根为 $\epsilon_i+\epsilon_{i+1}+\cdots+\epsilon_j$（$1\leq i\leq j\leq n$），共 $\frac{n(n+1)}{2}$ 个。对应的不可分解表示恰为区间表示
$$I[i,j):\quad (I[i,j))_t=\begin{cases}k,&i\leq t<j,\\ 0,&\text{否则},\end{cases}\qquad \text{箭头为恒等映射},$$
共 $\frac{n(n+1)}{2}$ 个。

**Kac 定理（一般箭图的推广）**：对任意箭图 $Q$，不可分解表示存在当且仅当其维数向量是正根；实根恰有一个不可分解表示，虚根则对应无穷多个。Gabriel 定理是"实根 + 有限型"这一正定情形的精确版本。

## 四、证明过程

**步骤 1（表示与路径代数的对应）。** 定义 $Q$ 的 $k$-线性表示为一族 $(V_i)_{i\in Q_0}$（每个有限维 $k$-向量空间）与一族线性映射 $(f_a:V_i\to V_j)_{a:i\to j}$；表示间的态射是逐顶点的线性映射 $(\varphi_i)$ 满足 $f_a\varphi_i=\varphi_jf_a$。则 $\operatorname{rep}_k(Q)$ 与路径代数 $kQ$ 的有限维模范畴 $\operatorname{mod}kQ$ 等价，其中 $kQ$ 以 $Q$ 的所有有向路径为基、以路径拼接为乘法。有限型即 $\operatorname{mod}kQ$ 只有有限多个不可分解对象。由 Krull–Schmidt 定理，任何表示唯一分解为不可分解表示直和，故有限型等价于"分解的积木块只有有限多种"。

**步骤 2（Tits 二次型与判据）。** 定义 Tits（Euler）二次型
$$q_Q(x)=\sum_{i\in Q_0}x_i^2-\sum_{a:i\to j}x_ix_j,\qquad x\in\mathbb Z^{Q_0}.$$
对箭图 $Q$ 有 $q_Q(\underline{\dim}M)=\dim_k\operatorname{Hom}(M,M)-\dim_k\operatorname{Ext}^1(M,M)$（用 $\operatorname{Hom}$ 与 $\operatorname{Ext}$ 的维数计算，即前投射性质），故对不可分解 $M$ 有 $q_Q(\underline{\dim}M)\geq1$（$\operatorname{Hom}(M,M)$ 含标量而 $\operatorname{End}$ 局部）。另一方面，经典的二次型分类给出：

- $q_Q$ 正定 $\Longleftrightarrow$ $\bar Q$ 是 Dynkin 图；
- $q_Q$ 半正定且有非零的零根 $\delta$ $\Longleftrightarrow$ $\bar Q$ 是 extended（affine）Dynkin 图 $\tilde A_{p,q}$、$\tilde D_n$、$\tilde E_6,\tilde E_7,\tilde E_8$；
- 其余情形 $q_Q$ 不定。

这一步把表示论问题化为纯组合判据。

**步骤 3（必要性：非 Dynkin 情形无穷多不可分解表示）。** 设 $\bar Q$ 不是 Dynkin 图，则它含一个 extended Dynkin 子图 $\bar Q'$（或含双箭头/blanchard 型子图，均可用下述构造处理）。$\bar Q'$ 的 Tits 型半正定，有零根 $\delta>0$ 且 $q(\delta)=0$。取 $\bar Q'$ 的一个定向使其中存在一个"源—汇"链，向相应顶点赋值参数 $\lambda\in k^*$，可得一族表示 $\{M(\lambda)\}$，其维数向量为 $\delta$，$\dim_k\operatorname{End}(M(\lambda))=k$（故不可分解），且 $\lambda\neq\mu\Rightarrow M(\lambda)\not\cong M(\mu)$。

最简模型是 Kronecker 箭图 $1\rightrightarrows 2$（即 $\tilde A_{1,1}$）：取 $V_1=V_2=k$，箭头映射为 $(1,\lambda)$。若 $(1,\lambda)$ 与 $(1,\mu)$ 合同（即存在 $c,d\in k^*$ 使 $c(1,\lambda)d^{-1}=(1,\mu)$），则 $c=d$ 且 $\lambda=\mu$；故 $\lambda\mapsto M(\lambda)$ 给出 $k^*$ 参数族，$k$ 无限时即为无穷多个不可分解表示。把该表示在其余顶点取零并沿单射扩张为 $Q$ 的表示，则由 $\operatorname{End}$ 仍为一维知这些表示在 $Q$ 上仍不可分解且互不同构。故非 Dynkin 情形不是有限型，"有限型 $\Longrightarrow$ Dynkin"得证。

**步骤 4（充分性：反射函子的归纳）。** 设 $Q$ 是 Dynkin 箭图。取顶点 $i$ 为汇（sink，无出边；源情形对偶）。BGP 反射函子 $S_i^+:\operatorname{rep}(Q)\to\operatorname{rep}(\sigma_iQ)$（$\sigma_iQ$ 为只在 $i$ 处反转所有箭头的箭图）定义为：对表示 $M$，
$$(S_i^+M)_i=\ker\Big(\bigoplus_{a:j\to i}M_j\xrightarrow{(\text{各 }f_a)}M_i\Big),\qquad (S_i^+M)_j=M_j\ (j\neq i),$$
箭头按投射自然诱导。它是范畴等价（在 $M$ 不含 $L_i$ 型单表示作为直和项时），并且把不可分解表示变为不可分解表示，把维数向量变为对根 $\underline{\dim}M$ 作反射 $\sigma_i$。由于 Dynkin 图的反射群（Weyl 群）作用传递地连接所有定向，且任何 Dynkin 箭图都可用"消去汇/源"的次序逐步约化到更小的 Dynkin 箭图（$A_n\to A_{n-1}\to\cdots\to A_1$ 等），反复使用反射函子可把任意表示约化到顶点更少的情形。基础情形 $\lvert Q_0\rvert=1$ 只有一个不可分解表示（$k$，维数向量为唯一的正根）。对 $\lvert Q_0\rvert$ 归纳得：Dynkin 情形是有限型，且不可分解表示个数为 $\lvert\Phi^+\rvert$。

**步骤 5（维数向量与正根的双射）。** 对不可分解表示 $M$，由步骤 2，$q_Q(\underline{\dim}M)\geq1$，且用 BGP 反射函子（它在 $\operatorname{Hom}/\operatorname{Ext}$ 上的作用由反射公式给出）可把 $\underline{\dim}M$ 沿 Weyl 群反射到某个单根 $\epsilon_i$（因为 $q_Q(\underline{\dim}M)>0$ 且 Weyl 群在实根上作用传递，而 Dynkin 情形所有正根都是实根）。逆向应用反射函子（等价性保证唯一到同构）即得：每个正根 $\alpha$ 恰对应一个不可分解表示，且该表示的维数向量为 $\alpha$; 同一维数向量的不可分解表示彼此同构（对根的"高度"归纳，每次用反射把一个分量化到零）。因此
$$\{\text{不可分解表示}\}\ \cong\ \Phi^+,\qquad \lvert\{\text{不可分解}\}\rvert=\lvert\Phi^+\rvert .$$

**步骤 6（$A_n$ 情形与区间模）。** $A_n$ 型箭图 $1\to2\to\cdots\to n$ 的根系正根为 $\epsilon_i+\cdots+\epsilon_j$（$1\leq i\leq j\leq n$）。由步骤 5，不可分解表示由维数向量唯一决定；维数向量为 $\epsilon_i+\cdots+\epsilon_j$ 的表示在第 $i,\dots,j$ 个空间上维数为 $1$、其余为 $0$，箭头只能取非零线性映射（否则分解），故同构于
$$I[i,j):\ (I[i,j))_t=k\ \text{当}\ i\leq t<j,\ \text{否则}\ 0,\ \text{箭头取恒等}.$$
再由 Krull–Schmidt 定理，$A_n$ 型任意有限维表示唯一分解为区间模直和。这正是持久模 barcode 分解的代数来源：把 filtration 的同调群与诱导映射看作 $A_m$ 型表示，即得持久同调基本定理与区间分解定理。$\square$

**注**：Gabriel 定理的结论对任意域 $k$ 成立（不要求代数闭）；Tits 型的正定性与域无关。$A_n$ 情形所对应的正是"单参数、有限支撑"的持久模；多参数持久模对应任意箭图（如 $A_n\times A_m$），一般不再是有限型，故 barcode 分解无法推广到多参数情形。

## 五、应用与意义

- **有限表示型代数的分类**：把代数问题化为 Dynkin 图，催生了预投射代数、丛倾斜代数、$\tau$-倾斜理论等现代研究方向。
- **拓扑数据分析**：$A_n$ 型箭图表示就是持久模，Gabriel 定理给出区间分解与 barcode 的存在唯一性，是持久同调基本定理与区间分解定理的代数基础。
- **Kac 定理与量子群**：一般箭图的不可分解表示由正根系刻画（Kac 定理），是 Kac–Moody 代数、量子群与箭图表示理论之间的桥梁。
- **反射函子与根系**：BGP 反射函子把表示论与 Weyl 群作用联系起来，是丛代数（cluster algebra）与导出范畴（丛范畴）构造的原型。
- **同调代数与层论**：Gabriel 定理的思想（用有限维表示分类对象）在层与凝聚态、箭图簇的导出等价中反复出现。

## 相关条目

- [持久同调基本定理](./持久同调基本定理.md)：$A_n$ 型表示分解为区间模的直接应用，给出 barcode。
- [主理想整环上的有限生成模结构定理](./主理想整环上的有限生成模结构定理.md)：另一条通往区间分解的路线（分次 $k[x]$-模），与 Gabriel 定理互为镜鉴。
- [区间分解定理](./区间分解定理.md)：把 Gabriel 定理的 $A_n$ 情形推广到分次模与连续参数，并给出秩函数刻画。
- [单纯复形与simplicial同调](./单纯复形与simplicial同调.md)：filtration 与同调群是持久模的具体来源。
- [Mapper算法](./Mapper算法.md)：以拓扑数据分析中的分块与聚类为出发点的算法，其代数背景与持久模相关。
- [稳定性定理](./稳定性定理.md)：barcode 的稳定性使 Gabriel 定理给出的分解在扰动下可比较。
