# Gauss方程

> **一句话大白话**：子流形自己"有多弯"（内蕴曲率）由两样东西共同负责——外面大空间的弯曲，加上子流形在空间里的扭动（第二基本形式）。Gauss 方程就是把这个朴素的账目写成一个精确的等式。

> **小例子**：$\mathbb R^3$ 中的球面 $S^2_R$：环境是平的（曲率为零），故内蕴曲率全部来自第二基本形式，Gauss 方程给出 $K=\det A=\dfrac{1}{R^2}$；球面越大越平，$K\to0$。反过来，平面（$A\equiv0$）与柱面（$A\ne0$ 但 $\det A=0$）的 $K$ 都是 $0$——这正是 Gauss 绝妙定理的著名例子。

## 一、定理介绍

> **前置依赖**：第一基本形式、第二基本形式、Riemann曲率张量、Gauss绝妙定理、极小曲面理论、Simons不等式

Gauss 方程是子流形几何的**基本方程**，由 Gauss 在 1827 年的曲面论工作中发现，其深远推论即著名的 Gauss 绝妙定理（Theorema Egregium）：Gauss 曲率只依赖第一基本形式。用现代语言说，子流形 $M^n\subset N^{n+k}$ 的内蕴曲率由环境曲率在切方向的限制与第二基本形式 $A$ 的二次项共同决定：

$$\langle R^N(X,Y)Z,W\rangle=\langle R^M(X,Y)Z,W\rangle+\langle A(X,Z),A(Y,W)\rangle-\langle A(X,W),A(Y,Z)\rangle .$$

它出自对 Gauss 公式与 Weingarten 公式的纯代数计算：把环境联络 $\nabla^N$ 分解为切向部分（内蕴联络加第二基本形式）与法向部分，代入曲率定义后按切/法方向分离——切向部分给出 Gauss 方程，法向部分给出 Codazzi 方程。二者合称 **Gauss–Codazzi 方程组**，是子流形理论中一切局部不变量关系（可积性定理、超曲面分类）的出发点。

在几何分析中，Gauss 方程的作用是把"内蕴曲率"与"外在的 $A$"互换，使曲率估计化为对 $|A|^2$ 的分析。Simons 不等式正沿着这条路线：先用 Gauss 方程把内蕴 Ricci 曲率写成 $A$ 的表达式，再用 Ricci 恒等式把 $\nabla\nabla A$ 的交换子化为曲率项，得到 $|A|^2$ 的 Bochner 型恒等式。极小曲面理论、平均曲率流与常平均曲率超曲面的刚性分类，都以 Gauss 方程为第一块基石。

## 二、原理思路

1. **分解环境联络**（Gauss 公式 + Weingarten 公式）：$\nabla^N_XY=\nabla^M_XY+A(X,Y)$（$X,Y$ 切），$\nabla^N_X\xi=-A_\xi X+\nabla^\perp_X\xi$（$\xi$ 法）。这是全部计算的输入，它把环境联络按切/法分量拆开。

2. **计算环境曲率并分离分量**：按定义 $R^N(X,Y)Z=\nabla^N_X\nabla^N_YZ-\nabla^N_Y\nabla^N_XZ-\nabla^N_{[X,Y]}Z$，逐项代入第 1 步。分离后切向部分含 $R^M(X,Y)Z$ 与两个 $A_{A(\cdot,\cdot)}(\cdot)$ 型项，法向部分则是 $(\nabla_XA)(Y,Z)-(\nabla_YA)(X,Z)$。

3. **取内积读出方程**：把切向部分与切向量 $W$ 作内积，用形状算子与第二基本形式的伴随关系 $\langle A_\xi X,W\rangle=\langle A(X,W),\xi\rangle$ 把 $A_\xi X$ 换成内积形式，即得 Gauss 方程；法向部分给出 Codazzi 方程。对超曲面写出分量形式并令环境曲率为零，即得 $\det A$ 的公式与绝妙定理。

## 三、定理的严格表述

设 $M^n$ 是 Riemann 流形 $N^{n+k}$ 的等距浸入子流形，$g=\langle\cdot,\cdot\rangle$；$\nabla^N,\nabla^M$ 为 Levi-Civita 联络，$\nabla^\perp$ 为法丛联络，$A:TM\times TM\to NM$ 为第二基本形式，形状算子 $A_\xi$ 由 $\langle A_\xi X,W\rangle=\langle A(X,W),\xi\rangle$ 定义。

**Gauss 公式**：$\nabla^N_XY=\nabla^M_XY+A(X,Y)$；**Weingarten 公式**：$\nabla^N_X\xi=-A_\xi X+\nabla^\perp_X\xi$。

**定理（Gauss 方程）**：对任意切向量场 $X,Y,Z,W$，

$$\langle R^N(X,Y)Z,W\rangle=\langle R^M(X,Y)Z,W\rangle+\langle A(X,Z),A(Y,W)\rangle-\langle A(X,W),A(Y,Z)\rangle .$$

**定理（Codazzi 方程）**：$R^N(X,Y)Z$ 的法向部分满足

$$\bigl(R^N(X,Y)Z\bigr)^\perp=(\nabla_XA)(Y,Z)-(\nabla_YA)(X,Z),\qquad(\nabla_XA)(Y,Z):=\nabla^\perp_XA(Y,Z)-A(\nabla^M_XY,Z)-A(Y,\nabla^M_XZ).$$

特别地当 $N$ 是常曲率空间时 $(\nabla_XA)(Y,Z)=(\nabla_YA)(X,Z)$，即 $\nabla A$ 关于前两个变元对称。

**推论 1（超曲面形式）**：设 $M^n\subset N^{n+1}$、$\nu$ 为单位法向、$A(X,Y)=h(X,Y)\nu$，在 $g$-正交规范标架 $\{e_i\}$ 下记 $h_{ij}=h(e_i,e_j)$、$H=\tfrac1n\sum_ih_{ii}$，则

$$R^M_{ijkl}=\bar R^N_{ijkl}+h_{ik}h_{jl}-h_{il}h_{jk},\qquad \mathrm{Ric}^M(e_j,e_j)=\sum_k\bar R^N_{jk kj}+\sum_k h_{jk}^2-nH\,h_{jj}.$$

**推论 2（Gauss 绝妙定理）**：对曲面 $M^2\subset\mathbb R^3$，取正交规范标架得 $K=\langle R^M(e_1,e_2)e_2,e_1\rangle=h_{11}h_{22}-h_{12}^2=\det A$；由于 $K$ 只依赖第一基本形式 $g$，故 $K$ 是内蕴量，与浸入方式无关。

**推论 3（极小超曲面的曲率）**：若 $M^n\subset\mathbb R^{n+1}$ 极小（$H\equiv0$），则 $\mathrm{Ric}^M(e_j,e_j)=-\sum_kh_{jk}^2$。特别地极小超曲面的 Ricci 曲率非正，且 $|\mathrm{Ric}^M|\le|A|^2$——这正是 Simons 不等式计算中"好符号项"的来源。

## 四、证明过程

**步骤 1：环境曲率的分量展开。**

对切 $X,Y,Z$，用 Gauss 公式展开第一层并用 Weingarten 公式分解法向的 $A(Y,Z)$：

$$\nabla^N_X\nabla^N_YZ=\underbrace{\nabla^M_X\nabla^M_YZ}_{\text{切}}+\underbrace{A(X,\nabla^M_YZ)}_{\text{法}}+\underbrace{\bigl(-A_{A(Y,Z)}X\bigr)}_{\text{切}}+\underbrace{\nabla^\perp_XA(Y,Z)}_{\text{法}} .$$

把 $X,Y$ 互换再相减（第一项中 $A(Y,Z)$ 换成 $A(X,Z)$），并减去 $\nabla^N_{[X,Y]}Z=\nabla^M_{[X,Y]}Z+A([X,Y],Z)$，即得 $R^N(X,Y)Z$ 的分解。

**步骤 2：分离切向与法向。**

由步骤 1，$R^N(X,Y)Z$ 的**切向部分**为 $R^M(X,Y)Z-A_{A(Y,Z)}X+A_{A(X,Z)}Y$，**法向部分**为

$$A(X,\nabla^M_YZ)-A(Y,\nabla^M_XZ)-A([X,Y],Z)+\nabla^\perp_XA(Y,Z)-\nabla^\perp_YA(X,Z).$$

**步骤 3：切向部分给出 Gauss 方程。**

取切向部分与切向量 $W$ 作内积，法向部分与 $W$ 正交而消失，于是

$$\langle R^N(X,Y)Z,W\rangle=\langle R^M(X,Y)Z,W\rangle-\bigl\langle A_{A(Y,Z)}X,W\bigr\rangle+\bigl\langle A_{A(X,Z)}Y,W\bigr\rangle .$$

用伴随关系 $\langle A_\xi X,W\rangle=\langle A(X,W),\xi\rangle$ 改写后两项为 $-\langle A(X,W),A(Y,Z)\rangle+\langle A(Y,W),A(X,Z)\rangle$，即得 Gauss 方程。$\square$

**步骤 4：法向部分给出 Codazzi 方程。**

对步骤 2 的法向部分用对称性 $A(X,\nabla^M_YZ)=A(\nabla^M_YZ,X)$、$A(Y,\nabla^M_XZ)=A(\nabla^M_XZ,Y)$，并展开 $[X,Y]=\nabla^M_XY-\nabla^M_YX$，得

$$A(\nabla^M_YZ,X)-A(\nabla^M_XZ,Y)-A(\nabla^M_XY,Z)+A(\nabla^M_YX,Z)+\nabla^\perp_XA(Y,Z)-\nabla^\perp_YA(X,Z).$$

把 $(\nabla_XA)(Y,Z)=\nabla^\perp_XA(Y,Z)-A(\nabla^M_XY,Z)-A(Y,\nabla^M_XZ)$ 与 $(\nabla_YA)(X,Z)=\nabla^\perp_YA(X,Z)-A(\nabla^M_YX,Z)-A(X,\nabla^M_YZ)$ 代入（再用对称性 $A(Y,\nabla^M_XZ)=A(\nabla^M_XZ,Y)$、$A(X,\nabla^M_YZ)=A(\nabla^M_YZ,X)$），两边逐项相消，即得 $(R^N(X,Y)Z)^\perp=(\nabla_XA)(Y,Z)-(\nabla_YA)(X,Z)$。$\square$

**步骤 5：超曲面形式与绝妙定理。**

设 $A(X,Y)=h(X,Y)\nu$，则 $\langle A(e_i,e_j),A(e_k,e_l)\rangle=h_{ij}h_{kl}$。代入 Gauss 方程得 $R^M_{ijkl}=\bar R^N_{ijkl}+h_{ik}h_{jl}-h_{il}h_{jk}$。对 $N=\mathbb R^3$（$\bar R^N\equiv0$）取 $i=k=1$、$j=l=2$：

$$K=R^M_{1212}=h_{11}h_{22}-h_{12}h_{21}=h_{11}h_{22}-h_{12}^2=\det A .$$

因 $R^M$ 完全由 Levi-Civita 联络（即由 $g$）决定，且 $h_{ij}$ 与 $g$ 又由 Gauss–Codazzi 方程组相互确定，故 $K$ 是 $g$ 的内蕴量：这就是 Gauss 绝妙定理。$\square$

**步骤 6：极小超曲面的曲率与 Simons 不等式的接口。**

在推论 1 的 Ricci 公式中取 $\bar R^N\equiv0$ 与 $H\equiv0$，得 $\mathrm{Ric}^M(e_j,e_j)=-\sum_kh_{jk}^2\le0$，于是内蕴曲率被 $|A|^2$ 控制（$|\mathrm{Ric}^M|\le|A|^2$）。这一步把"交换协变导数"产生的 Riemann 曲率项换成 $A$ 的二次项，使 $\tfrac12\Delta|A|^2$ 的右端只剩 $|\nabla A|^2$、$|A|^4$ 与环境曲率项，得到 Simons 恒等式

$$\tfrac12\Delta|A|^2=|\nabla A|^2-|A|^4+c\,n\,|A|^2 .$$

配合极小性条件 $\vec H=0$ 与极大值原理，即可得到极小超曲面的曲率 pinching 与 Bernstein 型定理——Gauss 方程在此完成了"从外在弯曲到内蕴曲率"的翻译。$\square$

## 五、应用与意义

**理论意义**：Gauss 方程（连同 Codazzi 方程）是子流形几何的基本定理：它说明内蕴几何与外在几何如何互相制约，并直接给出 Gauss 绝妙定理——曲率是内蕴量。它也是 Riemann 几何与子流形可积性理论（Bonnet 定理：$g$ 与 $A$ 满足 Gauss–Codazzi 即可局部实现浸入）的出发点。

**应用领域**：在极小曲面与几何分析中，它把内蕴曲率估计化为 $|A|^2$ 的估计，是 Simons不等式、曲率 pinching、稳定性不等式与平均曲率流奇点分析的基础；在常平均曲率超曲面与 Weingarten 曲面的分类中，它给出 Ricci 曲率与 $h_{ij}$ 的代数关系；在广义相对论中，它用于导出约束方程（initial data 的 Gauss–Codazzi 约束），是正质量定理与 Yamabe 问题相关论证的标准工具。

## 课堂问答

**老师**：子流形的内蕴曲率到底由什么决定？

**学生**：结论是 Gauss 方程 $\langle R^N(X,Y)Z,W\rangle=\langle R^M(X,Y)Z,W\rangle+\langle A(X,Z),A(Y,W)\rangle-\langle A(X,W),A(Y,Z)\rangle$，即内蕴曲率 = 环境曲率限制到切向 + 第二基本形式 $A$ 的二次项。当 $N=\mathbb R^3$ 且 $M^2$ 是曲面时，$K=h_{11}h_{22}-h_{12}^2=\det A$。

**老师（追问）**：$\det A$ 明明由浸入给出，凭什么说 $K$ 是内蕴量？

**学生**：因为 $R^M$ 完全由 Levi-Civita 联络、即由第一基本形式 $g$ 决定，而 $h_{ij}$ 又被 Gauss–Codazzi 方程组与 $g$ 相互确定，所以 $\det A$ 只依赖 $g$，与具体浸入方式无关——这就是 Gauss 绝妙定理。常见误区是把"外在量"与"内蕴量"混淆：平面与柱面的 $A$ 差别很大，但 $\det A$ 都为零，故 $K$ 都为 $0$。

**老师（拓展）**：Gauss 方程怎样和 Simons 恒等式接上？

**学生**：对极小超曲面 $H\equiv0$，Gauss 方程的 Ricci 分量给出 $\mathrm{Ric}^M(e_j,e_j)=\sum_k\bar R^N_{jkkj}-\sum_kh_{jk}^2$；在 $\mathbb R^{n+1}$ 中化为 $-\sum_kh_{jk}^2\le0$，于是 $|\mathrm{Ric}^M|\le|A|^2$。把这个"内蕴曲率换成 $A$"的翻译代入 $\frac12\Delta|A|^2$ 的 Bochner 型计算，就得到 $\frac12\Delta|A|^2=|\nabla A|^2-|A|^4+cn|A|^2$。
