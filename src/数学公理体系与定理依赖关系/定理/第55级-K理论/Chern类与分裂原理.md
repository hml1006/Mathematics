# Chern 类与分裂原理

> **一句话大白话**：复向量丛的"陈类"是刻画丛扭曲程度的拓扑不变量；而"分裂原理"说，为了验证关于陈类的任何恒等式，可以放心地假设丛是若干线丛的直和——因为总能把丛拉回到一个更大的空间里把它拆成线丛，而拉回映射在上同调上是单射（拆开不丢信息）。
>
> **小例子**：$T\mathbb{CP}^{n}$ 满足 $c(T\mathbb{CP}^{n})=(1+h)^{n+1}$（$h$ 为 $H^{2}(\mathbb{CP}^{n})$ 的生成元）；故 $c_{n}(T\mathbb{CP}^{n})=(n+1)h^{n}$，与欧拉数 $\chi(\mathbb{CP}^{n})=n+1$ 相印证。

## 一、定理介绍

> **前置依赖**：复向量丛与结构群 $GL_n(\mathbb C)$、射影丛 $\mathbb P(E)$ 与重言线丛、上同调环 $H^*(M;\mathbb Z)$、Leray–Hirsch 定理与 Gysin 序列（沿纤维积分）、Thom 同构、Whitney 和与拉回、旗丛（flag bundle）

Chern 类（陈省身类，1946 年前后由陈省身、Ehresmann、Grothendieck 等人建立）是复向量丛最基本的特征类：对复向量丛 $E\to M$ 的秩 $n$，可赋予上同调类
$$c_i(E)\in H^{2i}(M;\mathbb Z),\qquad i=0,1,\dots,n,\qquad c_0(E)=1,$$
它们满足自然性、Whitney 和公式 $c(E\oplus F)=c(E)c(F)$ 与归一化条件。Chern 类是同伦不变量，且在复流形上可通过 Chern–Weil 理论用曲率形式直接表示
$$c(E)=\left[\det\left(I+\frac{\sqrt{-1}}{2\pi}\Omega\right)\right],$$
其中 $\Omega$ 是 $E$ 上任意联络的曲率。

**分裂原理**（splitting principle）是把 Chern 类的计算从一般丛化归为线丛之和的技术性原则。它断言：对任意 $E\to M$ 存在一个"旗丛" $\pi:Fl(E)\to M$，使得
$$\pi^*:H^*(M;\mathbb Z)\longrightarrow H^*(Fl(E);\mathbb Z)$$
是**单射**，且 $\pi^*E$ 同构于若干线丛的直和 $L_1\oplus\cdots\oplus L_n$。因此，任何关于特征类的恒等式只需在"完全分裂"的情形验证；由于 $\pi^*$ 单射，"在 $Fl(E)$ 上成立"可回推到 $M$ 上。分裂原理是 Whitney 和公式、Riemann–Roch 定理中特征类计算、以及 K 理论中 Chern 特征标定义的技术基石。

## 二、原理思路

分裂原理由两个相互配合的结果构成。

1. **射影丛定理（Grothendieck 的 Chern 类定义）**：对秩 $n$ 复向量丛 $E\to M$，设 $\mathbb P(E)\xrightarrow{\pi}M$ 为射影丛，$\mathcal O(1)$ 为重言线丛的对偶，记 $\xi=c_1(\mathcal O(1))$。则 $H^*(\mathbb P(E);\mathbb Z)$ 是自由 $H^*(M;\mathbb Z)$-模，以 $1,\xi,\dots,\xi^{n-1}$ 为基，且存在唯一的一组类 $c_i(E)\in H^{2i}(M)$ 使关系
$$\xi^{n}+c_1(E)\xi^{n-1}+\cdots+c_{n}(E)=0$$
成立。这组 $c_i(E)$ 就是 $E$ 的 Chern 类（Grothendieck 的定义）。关键工具是"沿纤维积分"给出的 $H^*(M)$-线性左逆 $\pi_*$（Thom 同构/Gysin 序列），它使 $\pi^*$ 单射成为自由性的直接推论。

2. **递归分裂**：在 $\mathbb P(E)$ 上有重言正合列 $0\to\mathcal O(-1)\to\pi^*E\to\mathcal Q\to0$，其中 $\mathcal Q$ 是商丛，秩 $n-1$。对 $\mathcal Q$ 再作射影丛，如此递归，最后构造出**完全旗丛**
$$Fl(E)\longrightarrow\mathbb P(\mathcal Q_{n-2})\longrightarrow\cdots\longrightarrow\mathbb P(\mathcal Q_1)\longrightarrow M,$$
每一层的拉回都是单射，复合仍单射，而 $\pi^*E$ 在旗丛上被逐步"剥出"一条线丛，最终分解为 $n$ 条线丛之和。

由此，Chern 类的所有运算律（Whitney 和公式、与拉回交换）都可以通过在分裂情形 $E=\bigoplus_j L_j$ 上验证
$$c(E)=\prod_{j=1}^{n}\bigl(1+c_1(L_j)\bigr)$$
而得到；这一乘积形式又直接来自上面的关系式（$\xi^{n}+\cdots+c_n=\prod_j(\xi+c_1(L_j))=0$）。

## 三、定理的严格表述

**（射影丛定理）** 设 $E\to M$ 是秩 $n\ge1$ 的复向量丛，$M$ 仿紧（故有 $CW$/仿紧结构，上同调理论可用）。设 $\pi:\mathbb P(E)\to M$ 为射影丛，$\mathcal O(-1)\subset\pi^*E$ 为重言子线丛，$\mathcal O(1)=\mathcal O(-1)^{*}$，$\xi=c_1(\mathcal O(1))$。则
$$H^{*}\bigl(\mathbb P(E);\mathbb Z\bigr)\cong H^{*}(M;\mathbb Z)\otimes\mathbb Z[\xi]/(\xi^{n}+c_1(E)\xi^{n-1}+\cdots+c_n(E))$$
作为 $H^{*}(M)$-模是自由模，基为 $1,\xi,\dots,\xi^{n-1}$；其中的 $c_i(E)\in H^{2i}(M;\mathbb Z)$ 即为 $E$ 的 **Chern 类**。

**（Chern 类的基本性质）**
1. **自然性**：对连续映射 $f:M'\to M$ 有 $c_i(f^{*}E)=f^{*}c_i(E)$。
2. **归一化**：对线丛 $L$，$c(L)=1+c_1(L)$，且 $c_1$ 是 $H^2(M;\mathbb Z)$ 中的第一 Chern 类（由 $\mathbb P^1$ 上的重言线丛归一化确定）。
3. **Whitney 和公式**：$c(E\oplus F)=c(E)\,c(F)$，其中 $c(E)=\sum_{i}c_i(E)$。
4. **消失性**：$c_i(E)=0\ (i>n=\operatorname{rank}E)$。

**（分裂原理）** 设 $E\to M$ 是秩 $n$ 复向量丛。则存在 $M$ 上的纤维丛 $\pi:Fl(E)\to M$（纤维为完全旗流形 $Fl_n=GL_n(\mathbb C)/B$，$B$ 为 Borel 子群），以及线丛 $L_1,\dots,L_n\to Fl(E)$，使得
$$\pi^{*}E\cong L_1\oplus L_2\oplus\cdots\oplus L_n,\qquad\text{且}\qquad \pi^{*}:H^{*}(M;\mathbb Z)\hookrightarrow H^{*}(Fl(E);\mathbb Z)\ \text{单射}.$$
从而对任意只涉及特征类运算的恒等式 $P$，"$P$ 对一切复向量丛成立"当且仅当"$P$ 对一切线丛直和 $L_1\oplus\cdots\oplus L_n$ 成立"。

**（推论：Weyl 公式）** 在旗丛上
$$c_i(E)=\sigma_i\bigl(c_1(L_1),\dots,c_1(L_n)\bigr),$$
即 $c_i(E)$ 等于 $c_1(L_j)$ 的第 $i$ 个初等对称多项式（由 $\pi^{*}$ 单射，等式回推到 $M$ 上有意义）。

## 四、证明过程

**步骤 1：沿纤维积分 $\pi_*$ 的存在（Thom 同构）。**

设 $D(E),S(E)$ 分别为 $E$ 的单位圆盘丛与单位球丛，$D(E)\to M$ 的纤维为 $2n$ 维圆盘，$S(E)\to M$ 的纤维为 $S^{2n-1}$。存在**Thom 同构**
$$\mathscr T:H^{k}(M;\mathbb Z)\xrightarrow{\ \cong\ }H^{k+2n}_{c}\bigl(D(E),S(E);\mathbb Z\bigr),\qquad \mathscr T(a)=\pi^{*}(a)\cup u,$$
其中 $u\in H^{2n}_c(D(E),S(E))$ 是 Thom 类（因纤维可定向，$u$ 存在且唯一）。配合切除与长正合列，得到球丛 $S(E)\to M$ 的 **Gysin 序列**
$$\cdots\to H^{k}(M)\xrightarrow{\ \cup e(E)\ }H^{k+2n}(M)\xrightarrow{\ \pi^*\ }H^{k+2n}(S(E))\xrightarrow{\ \pi_*\ }H^{k+1}(M)\to\cdots,$$
其中 $\pi_*$ 是"沿纤维积分"（把 $S^{2n-1}$ 上的类积分到基上）。$\pi_*$ 是 $H^*(M)$-线性（投影公式 $\pi_*(\pi^*a\cup b)=a\cup\pi_*(b)$）。

**步骤 2：把 $\mathbb P(E)$ 与球丛联系起来。**

球丛 $S(E)$ 是 $E$ 中单位向量组成的丛，射影化 $S(E)\to\mathbb P(E)$ 是 $S^{1}$-主丛（每条复直线中的单位向量构成 $S^1$）。故有映射 $p:S(E)\to\mathbb P(E)$，且 $p$ 沿 $S^1$-纤维的积分给出 $H^{*}(\mathbb P(E))\cong H^{*}(S(E))$ 的"不变量部分"；\(\mathbb P(E)\) 的胞腔链与 Gysin 序列结合，等价地得到以 $\xi$ 为生成元的 Leray–Hirsch 结构。具体地，$\mathbb P(E)\to M$ 的纤维 $\mathbb{CP}^{n-1}$ 的（整系数）上同调由 $1,\xi,\dots,\xi^{n-1}$ 生成（限制到纤维上，$\xi|_{\text{fiber}}=c_1(\mathcal O(1)|_{\mathbb{CP}^{n-1}})$ 是超平面类的生成元）。

**步骤 3：证明自由性与关系式。**

**（a）生成性**：对 $k$ 归纳。$\pi_*(\xi^{n-1})$ 是 $M$ 上的一个类，把它归一化后记为 $1$（必要时用 $\xi$ 平移）；可验证
$$\pi_*(\xi^{i})=0\quad(0\le i<n-1),\qquad \pi_*(\xi^{n-1})=1.$$
验证方法：在 $E$ 为线丛直和 $L_1\oplus\cdots\oplus L_n$ 时的特例中，$\mathbb P(E)$ 可分解为若干射影空间丛的"塔"，用 $\mathbb{CP}^{k}$ 的胞腔结构直接计算（$H^*(\mathbb{CP}^{k})=\mathbb Z[h]/(h^{k+1})$，$\int_{\mathbb{CP}^k}h^k=1$），得到上述等式；一般情形由下面的分裂原理（步骤 5）回推。因此 $\pi_*(\pi^*a\cup\xi^{i})=a\cdot\pi_*(\xi^i)$。
**（b）关系式**：由投影公式与 $\pi_*$ 的 Gysin 序列性质，
$$\pi_*\bigl(\xi^{n}+c_1(E)\xi^{n-1}+\cdots+c_n(E)\bigr)=0$$
对一切基类成立；定义 $c_i(E)=(-1)^{i}\pi_*(\xi^{n+i-?})$ 型公式（更明确地：把 $\xi^{n}$ 在 $\mathbb P(E)$ 的 $H^*(M)$-基中展开
$$\xi^{n}=-\sum_{i=1}^{n}\bigl(-1\bigr)^{?}c_i(E)\xi^{n-i},$$
其系数给出 $c_i(E)$；在分裂情形 $E=\bigoplus_j L_j$ 下，$\prod_j(\xi+c_1(L_j))=0$ 即所求关系，且 $c_i(E)=e_i(c_1(L_1),\dots,c_1(L_n))$）。由此 $\xi^{n}+c_1(E)\xi^{n-1}+\cdots+c_n(E)=0$，并且该关系使 $1,\xi,\dots,\xi^{n-1}$ 在 $H^*(M)$ 上**线性无关**（用 $\pi_*$ 作用：若 $\sum_{i<n}a_i\xi^{i}=0$，则对 $\xi^{n-1-i}$ 用投影公式得 $a_i=0$）。

综合 (a)(b)，$H^*(\mathbb P(E))$ 是以 $1,\dots,\xi^{n-1}$ 为基的自由 $H^*(M)$-模，且 $c_i(E)$ 满足所述关系。$\square$

**步骤 4：$\pi^*$ 单射。**

由投影公式 $\pi_*(\pi^{*}a\cup\xi^{n-1})=a$，故 $\pi_*(\pi^*a\cup\xi^{n-1})=0\Rightarrow a=0$，即 $\pi^*a=0\Rightarrow a=0$。故 $\pi^*:H^*(M)\to H^*(\mathbb P(E))$ 单射。

**步骤 5：递归构造旗丛与分解。**

在 $\mathbb P(E)$ 上有重言正合列
$$0\longrightarrow\mathcal O(-1)\longrightarrow\pi^{*}E\longrightarrow\mathcal Q\longrightarrow 0,\qquad \mathcal O(-1)\ \text{线丛},\ \operatorname{rank}\mathcal Q=n-1.$$
对 $\mathcal Q\to\mathbb P(E)$ 重复步骤 3–4，得 $\pi_1:\mathbb P(\mathcal Q)\to\mathbb P(E)$，使 $\pi_1^*\mathcal Q\supset\mathcal O(-1)_{\mathcal Q}$ 并单射地在 $\mathcal Q$ 上剥出一条线丛，且 $\pi_1^*$ 单射。记
$$Fl(E)=\mathbb P(\mathcal Q_{n-2}),\qquad \pi=\pi_1\circ\pi_2\circ\cdots\circ\pi_{n-1}:Fl(E)\to M,$$
其中每一步都是射影丛投射。复合的单射性：单射的复合仍单射，故 $\pi^{*}:H^{*}(M)\hookrightarrow H^{*}(Fl(E))$ 单射。而在 $Fl(E)$ 上，正合列被逐层分裂，存在线丛 $L_1,\dots,L_n$ 使
$$\pi^{*}E\cong L_1\oplus\cdots\oplus L_n.$$
（几何上，$Fl(E)$ 的每一点是 $E_x$ 的一个完全旗，$L_j$ 取该旗的第 $j$ 条直线。）$\square$

**步骤 6：Whitney 和公式与恒等式回推。**

在分裂情形下，由步骤 3 的关系式 $\prod_j(\xi+c_1(L_j))=0$ 与根—系数关系，$c_i(E)=e_i(c_1(L_j))$，故
$$c(E)=\sum_i c_i(E)t^{i}=\prod_{j}\bigl(1+c_1(L_j)t\bigr).$$
设 $E,F$ 为任意两丛。取 $\pi:Fl(E\oplus F)\to M$（或分别取旗丛的纤维积）使 $\pi^*(E\oplus F)=\bigoplus_j L_j\oplus\bigoplus_k L'_k$；在旗丛上
$$c(\pi^*(E\oplus F))=\prod_j(1+c_1(L_j))\prod_k(1+c_1(L'_k))=c(\pi^*E)\,c(\pi^*F).$$
由自然性 $c(\pi^*(E\oplus F))=\pi^*c(E\oplus F)$，两边相等给出 $\pi^*(c(E\oplus F)-c(E)c(F))=0$，再由 $\pi^*$ 单射得 $c(E\oplus F)=c(E)c(F)$。其他恒等式（如 $c_i$ 的对称多项式表达、Chern 特征标公式）同理：在分裂情形成立 + $\pi^*$ 单射 ⇒ 一般成立。$\square$

## 五、应用与意义

**理论意义**：
1. **特征类理论的公理化起点**：Grothendieck 用射影丛关系定义 Chern 类，使 Whitney 和公式等成为可以"逐线丛验证"的代数事实。
2. **上同调运算的自然来源**：Chern 类给出 $K^0(M)\to H^{2*}(M)$ 的环同态（Chern 特征标），是 K 理论与上同调之间的桥梁。
3. **指标定理的输入**：Atiyah–Singer 指标定理中的拓扑指标由 Chern 类的多项式（$\hat A$、$\operatorname{td}$、$\operatorname{ch}$）给出，其计算完全依赖分裂原理。

**应用领域**：
1. **复代数几何**：Riemann–Roch–Hirzebruch 定理、Kodaira 嵌入/消没定理、陈类的相交理论。
2. **代数拓扑**：复配边理论、Bott 周期性、Steenrod 运算（Chern 类的模 $p$ 约化）。
3. **微分几何**：Chern–Weil 理论与示性类、复流形的示性数与 Gauss–Bonnet 型定理。
4. **数学物理**：规范场论中的瞬子数、指数定理与反常消除，都用 Chern 类及其分裂计算。

**推广**：
- **实丛的 Pontryagin 类与 Stiefel–Whitney 类**：有相应的分裂原理（复化后分裂为线丛）。
- **一般特征类与同调论**：在任意乘法上同调理论中，只需 $BU(n)$ 的胞腔结构即可定义 Chern 类；分裂原理由 $BU(1)^n\to BU(n)$ 的同调性质保证。
- **等变与代数情形**：等变 Chern 类、晶体上同调中的 Chern 类（Grothendieck 原始动机正是 Weil 猜想）都沿用"旗丛拉回单射"的分裂思想。
