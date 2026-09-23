# Simons 不等式

> **一句话大白话**：极小曲面的"弯曲程度"（第二基本形式）并不自由，它满足一个恒等式：拉普拉斯 = 梯度平方 − 曲率四次方 + 环境曲率项；把负项丢掉就得到一条不等式，把曲率牢牢锁住，这就是 Simons 不等式。

> **小例子**：单位球面 $\mathbb{S}^{n+1}$ 中的闭极小超曲面若处处 $|A|^2\le n$，则只能 $|A|^2\equiv0$（赤道大球面）或 $|A|^2\equiv n$（Clifford 环面），中间值不可能出现。

## 一、定理介绍

> **前置依赖**：极小曲面理论、第二基本形式、第一变分公式、Riemann 曲率张量、Bochner 公式、Laplacian 比较定理、极大值原理。

Simons 不等式出自 James Simons 1968 年的论文《Minimal varieties in Riemannian manifolds》。在此之前的极小曲面研究主要依赖一阶变分（极小 ⟺ 平均曲率 $H\equiv0$）与整体技巧；Simons 第一次系统地计算了面积泛函的**二阶**信息，即第二基本形式 $A$ 的平方模长 $|A|^2$ 的拉普拉斯，得到著名的 **Simons 恒等式**。该恒等式说明：对极小子流形，$\Delta|A|^2$ 可以被"梯度项""曲率自乘项"与"环境曲率项"精确表达，而不含 $A$ 的三阶以上的未知量。

把恒等式中的符号丢入恰当方向即得 **Simons 不等式**：极小曲面越弯，$\Delta|A|^2$ 就越被负的 $-|A|^4$ 项往下压，于是极大值原理立刻给出"曲率不能太弯"的定量限制。由此得到的推论包括：

1. **pinching 定理**：闭极小超曲面 $M^n\subset\mathbb{S}^{n+1}$ 若 $0\le|A|^2\le n$，则 $|A|^2\equiv0$ 或 $\equiv n$（后者由 Chern–do Carmo–Kobayashi 与 Lawson 分类为 Clifford 环面）。
2. **Bernstein 型定理**：稳定极小超曲面在 $\mathbb R^{n+1}$（$n\le6$）中必为超平面；Simons 用它证明"稳定极小锥必为全测地"对维数 $n\le6$ 成立。
3. **曲率估计**：配合第一变分公式与单调公式，给出 $|A|^2(x)\le C/r^2$ 的点估计，是奇点分析与紧性理论的基本输入。

它不是一条孤立的技巧，而是"把二阶变分写成 Bochner 型恒等式"这一范式的原型：同样的计算方式后来被推广为 Chern–Yau 对 Codazzi 张量的 Simons 型公式、Nomizu–Smyth 对常平均曲率超曲面的公式，以及各类几何流中的张量极值原理。

## 二、原理思路

1. **把目标量写成双线性形式**：由 $\tfrac12\Delta|A|^2=|\nabla A|^2+\langle A,\Delta A\rangle$，问题化为计算 $\langle A,\Delta A\rangle$，即要把 $\Delta A$ 用低阶量表达。

2. **用 Codezzi 方程消去 $A$ 的三阶导数**：极小曲面（更一般地空间中常曲率超曲面）满足 Codazzi 方程 $\nabla_i h_{jk}=\nabla_j h_{ik}$，它允许交换 $A$ 的协变导数指标。

3. **用 Ricci 恒等式把交换子换成曲率**：对 $h_{ij}$ 交换 $\nabla_k,\nabla_l$ 会得到 Riemann 曲率张量的线性项；再用 Gauss 方程把内蕴曲率换成 $h$ 的二次项与环境的常曲率 $c$。

4. **合并同类项**：所有项都化为 $|A|^4$、$c\,|A|^2$、$|\nabla A|^2$ 的组合，得到 Simons 恒等式；丢掉符号较好或可忽略的项，就得到可用于极大值原理的不等式。

5. **用极大值原理收割**：在使 $|A|^2$ 取最大值的点处 $\Delta|A|^2\ge0$（按本文件约定），与不等式联立迫使 $|A|^2$ 只能取临界值，从而得到刚性结论。

## 三、定理的严格表述

以下均取 $\Delta:=g^{ij}\nabla_i\nabla_j$（联络 Laplacian，即迹 Laplacian），$A$ 为第二基本形式，$|A|^2$ 为其平方模长，$c$ 为环境空间形式的截面曲率。

**定理 1（Simons 恒等式，极小超曲面）**：设 $M^n$ 是常曲率空间形式 $M^{n+1}(c)$ 中的极小超曲面（$H\equiv0$），则
$$
\frac12\Delta|A|^2=|\nabla A|^2-|A|^4+cn\,|A|^2 .
$$

两个最重要的特例是：

- $\mathbb R^{n+1}$（$c=0$）：
$$
\frac12\Delta|A|^2=|\nabla A|^2-|A|^4 ;
$$
- $\mathbb S^{n+1}$（$c=1$）：
$$
\frac12\Delta|A|^2=|\nabla A|^2+\bigl(n-|A|^2\bigr)|A|^2 .
$$

**定理 2（Simons 恒等式，单位球面中一般余维的极小子流形）**：设 $M^n\subset\mathbb S^{n+q}(1)$ 为极小子流形，$S=|A|^2$，$A_\alpha$（$\alpha=1,\dots,q$）为沿局部标准法标架的形算子（shape operator），则
$$
\frac12\Delta S=|\nabla A|^2+nS-\sum_{\alpha,\beta=1}^{q}\langle A_\alpha,A_\beta\rangle^2-\sum_{\alpha,\beta=1}^{q}\bigl\|[A_\alpha,A_\beta]\bigr\|^2 .
$$
当 $q=1$ 时 $\sum_\beta\langle A_1,A_\beta\rangle^2=|A|^4$ 且交换子为零，公式退化为定理 1（$c=1$）的形式。

**定理 3（Simons 不等式与 pinching）**：设 $M^n\subset\mathbb S^{n+1}$ 是闭极小超曲面，且
$$
0\le |A|^2\le n .
$$
则 $|A|^2\equiv0$（$M$ 为全测地大球面）或 $|A|^2\equiv n$（$M$ 为 Clifford 环面）。

**推论（Simons 积分不等式）**：设 $\Sigma^m\subset\mathbb S^n(1)$ 是闭极小子流形，则
$$
\int_\Sigma |A|^2\Bigl(|A|^2-c(n,m)\Bigr)\,d\Sigma\ \ge\ 0,\qquad c(n,m)=\frac{m(n-m)}{2(n-m)-1},
$$
且等号情形给出 Clifford 环面与 Veronese 曲面。

## 四、证明过程

**一、Simons 恒等式（定理 1）的证明。**

**步骤 1（写成双线性形式）。** 由导数的乘积法则，
$$
\frac12\Delta|A|^2=\langle A,\Delta A\rangle+|\nabla A|^2 ,
$$
故只需计算 $\langle A,\Delta A\rangle=\sum_{i,j}h_{ij}(\Delta h)_{ij}$。

**步骤 2（Codazzi 方程）。** 常曲率环境空间的超曲面满足 Codazzi 方程
$$
\nabla_i h_{jk}=\nabla_j h_{ik}.
$$

**步骤 3（Ricci 恒等式）。** 对 $(0,2)$-张量 $h$ 有
$$
(\nabla_k\nabla_l-\nabla_l\nabla_k)h_{ij}=-R_{kil}^{\ \ m}h_{mj}-R_{kjl}^{\ \ m}h_{im},
$$
其中 $R$ 是 $M$ 的内蕴 Riemann 曲率张量。由 Gauss 方程
$$
R_{ijkl}=c\bigl(\delta_{ik}\delta_{jl}-\delta_{il}\delta_{jk}\bigr)+\bigl(h_{ik}h_{jl}-h_{il}h_{jk}\bigr).
$$
把 Gauss 方程代入并利用 Codazzi 方程整理（对 $k,l$ 缩并、对指标求和），在 $H\equiv0$ 时得到
$$
(\Delta h)_{ij}=-|A|^2h_{ij}+cn\,h_{ij}.
$$

**步骤 4（合并）。** 将步骤 3 代入步骤 1：
$$
\langle A,\Delta A\rangle=-|A|^4+cn\,|A|^2 ,
$$
即得
$$
\frac12\Delta|A|^2=|\nabla A|^2-|A|^4+cn\,|A|^2.\qquad\square
$$

**二、一般余维恒等式（定理 2）的证明思路。** 对每个法方向 $\alpha$ 重复上述计算，得到关于 $A_\alpha$ 的方程；区别在于法丛非平凡，交换协变导数时除内蕴曲率外还会出现法丛曲率项，而法丛曲率由 $A_\alpha,A_\beta$ 的交换子 $[A_\alpha,A_\beta]$ 表示。把 $\alpha$ 求和整理后，$|A|^4$ 被分解为 $\sum_{\alpha,\beta}\langle A_\alpha,A_\beta\rangle^2$ 与 $\sum_{\alpha,\beta}\|[A_\alpha,A_\beta]\|^2$ 两项之和，环境球面的曲率贡献为 $nS$，即得定理 2。$\square$

**三、pinching 定理（定理 3）的证明。**

**步骤 1（积分掉梯度项）。** 由定理 1（$c=1$）在闭流形上积分，散度项积分为零：
$$
0=\int_{M}\Bigl(|\nabla A|^2+\bigl(n-|A|^2\bigr)|A|^2\Bigr)\,d\mu .
$$
被积函数两项均非负（因 $|A|^2\le n$），故
$$
|\nabla A|^2\equiv0,\qquad \bigl(n-|A|^2\bigr)|A|^2\equiv0 .
$$

**步骤 2（读出结论）。** 由第二式，每个连通分支上或者 $|A|^2\equiv0$，或者 $|A|^2\equiv n$（连续性）。$|A|^2\equiv0$ 即全测地；$|A|^2\equiv n$ 且 $|\nabla A|\equiv0$ 的情形由 Chern–do Carmo–Kobayashi 与 Lawson 的等距分类给出：恰为 $\mathbb S^k(\sqrt{k/n})\times\mathbb S^{n-k}(\sqrt{(n-k)/n})$ 型 Clifford 环面（以及 $n=2$ 时的 Veronese 曲面）。$\square$

**四、积分不等式（推论）的证明思路。** 对进入 $\mathbb S^n$ 的极小子流形，把定理 2 型的恒等式在闭流形上积分并消去梯度项，右端的二次型由 DDVV（Dajczer–do Carmo–Vanhecke / Lu）矩阵不等式
$$
\sum_{\alpha,\beta}\langle A_\alpha,A_\beta\rangle^2+\sum_{\alpha,\beta}\bigl\|[A_\alpha,A_\beta]\bigr\|^2\le \frac32\,S^2
$$
控制；在余维 $n-m$ 与维数 $m$ 的算术约束下把系数优化，得到 $c(n,m)=\frac{m(n-m)}{2(n-m)-1}$ 的积分不等式。$\square$

## 五、应用与意义

- **极小曲面的刚性**：pinching 与积分不等式给出"曲率小 ⟹ 全测地"的定量判据，是球面中极小超曲面分类（Chern 猜想、第二间隙问题）的出发点。
- **Bernstein 问题**：Simons 用稳定极小锥的刚性把 Bernstein 定理推到 $n\le7$（$n\le6$ 时为超平面，$n=7$ 时 Bombieri–De Giorgi–Giusti 给出反例），成为几何测度论方法解决经典问题的范例。
- **奇点分析**：Simons 型恒等式配合单调公式给出 $|A|^2(x)\le C/r^2$ 的点估计与 $\varepsilon$-正则性，是平均曲率流与极小曲面奇点理论的技术基础。
- **推广**：Chern–Yau 把该计算推广到 Codazzi 张量，Nomizu–Smyth 推广到常平均曲率超曲面，Hamilton 与 Böhm–Wilking 的张量极值原理则把"曲率条件在流下保持"系统化。

## 相关条目

- [极小曲面理论](./极小曲面理论.md)：Simons 不等式是其刚性结论的核心工具。
- [第一变分公式](./第一变分公式.md)：一阶变分给出极小性，Simons 恒等式是一阶变分的二阶对应物。
- [第二基本形式](../第33级-微分几何/第二基本形式.md)：$A$、$|A|^2$ 与 Codazzi 方程的定义来源。
- [Bochner公式](../第49级-黎曼几何/Bochner公式.md)：同属"拉普拉斯 = 梯度 + 曲率"的计算范式。
- [曲率估计与单调公式](./曲率估计与单调公式.md)：把 Simons 不等式与单调公式结合得到曲率点估计。
- [稳定性不等式](./稳定性不等式.md)：二阶变分的另一条直接推论。
