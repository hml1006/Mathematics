# 第二 Bianchi 恒等式

> **一句话大白话**：把黎曼曲率张量再求一次协变导数，然后对三个指标做轮换求和，结果恒为零——曲率沿流形"怎么变"被一条恒等式锁死，它的缩并还直接给出 Einstein 张量的散度为零。

> **小例子**：在 Einstein 流形（$R_{ij}=\lambda g_{ij}$）上，缩并形式 $2\nabla^aR_{ac}=\nabla_cS$ 的左端为零，于是 $\nabla_cS=0$：Einstein 流形的标量曲率必为常数。

## 介绍

第二 Bianchi 恒等式（second Bianchi identity）是黎曼几何中与第一 Bianchi 恒等式并列的基本恒等式，由 Luigi Bianchi 在 1902 年整理黎曼几何张量演算时给出。第一 Bianchi 恒等式描述的是曲率张量在**同一点**上的代数对称性（对三个指标的轮换反对称求和为零 $R_{ijkl}+R_{jkil}+R_{kijl}=0$）；第二 Bianchi 恒等式则是一条**微分恒等式**：它约束曲率场沿流形的一阶变化。

该恒等式的意义远超一条计算技巧。对它作一次指标缩并，立刻得到"缩并的 Bianchi 恒等式" $\nabla^aR_{abcd}=\nabla_cR_{bd}-\nabla_dR_{bc}$；再缩并一次便得出 $\nabla^aR_{ac}=\frac12\nabla_cS$，等价地 $\nabla^iG_{ij}=0$，其中 $G_{ij}=R_{ij}-\frac12Sg_{ij}$ 是 Einstein 张量。Einstein 张量散度为零，正是广义相对论中 Einstein 场方程"自动满足能量守恒 $\nabla^iT_{ij}=0$"的几何根源，因此这条恒等式是引力理论自洽性的基础。

在几何分析中，它也是 Ricci 流通量单调性、Ricci 孤立子方程以及 Weitzenböck 公式等后续结果的重要工具；凡是要对曲率作积分分部估计的地方，都离不开它。

## 分析

**前置依赖**：Riemann 曲率张量的对称性、Levi-Civita 联络与协变导数、Christoffel 符号、测地法坐标、协变外微分与 Bianchi 恒等式、Ricci 曲率与标量曲率、Einstein 张量。

**定理内容**：设 $(M^n,g)$ 是黎曼流形，$R_{ijkl}$ 为（0,4）型黎曼曲率张量。则

$$\nabla_mR_{ijkl}+\nabla_kR_{ijlm}+\nabla_lR_{ijmk}=0,$$

即对后三个指标 $(k,l,m)$ 轮换求和为零；用分号记协变导数，即

$$R_{ijkl;m}+R_{ijlm;k}+R_{ijmk;l}=0.$$

**缩并形式（Contracted Bianchi identity）**：

$$\nabla^aR_{abcd}=\nabla_cR_{bd}-\nabla_dR_{bc}.$$

再缩并 $b,d$ 得

$$2\nabla^aR_{ac}=\nabla_cS,\qquad\text{等价地}\qquad \nabla^iG_{ij}=0,$$

其中 $S=g^{ac}R_{ac}$ 为标量曲率，$G_{ij}=R_{ij}-\frac12Sg_{ij}$。

**依赖的概念**：Christoffel 符号、测地法坐标、协变导数的交换子（Ricci 恒等式）、Ricci 张量与标量曲率。

## 思考过程

证明的策略是"在特制的坐标系里做一次纯计算"。张量恒等式是坐标无关的，因此只需在一点 $p$ 处选一个最方便的坐标验证即可。取测地法坐标（以 $p$ 为原点的法坐标，此时 $\Gamma^l_{ij}(p)=0$，且 $\partial_m g_{ij}(p)=0$）。在这样的坐标下，协变导数在 $p$ 点退化为普通偏导数，$R_{ijkl}$ 也退化为度量的纯二阶导数表达式：

$$R_{ijkl}=\tfrac12\bigl(\partial_i\partial_kg_{jl}+\partial_j\partial_lg_{ik}-\partial_i\partial_lg_{jk}-\partial_j\partial_kg_{il}\bigr)+O(\Gamma^2).$$

关键在于，$R$ 中出现的 $\Gamma\Gamma$ 项对 $\nabla R$ 的贡献含因子 $\Gamma$，在 $p$ 点为零，而二阶导表达式中的每一个三次偏导数都对称（偏导可交换）、度量的指标也对称。于是把三项 $\nabla_mR_{ijkl}$、$\nabla_kR_{ijlm}$、$\nabla_lR_{ijmk}$ 写成这样的三次偏导之和后，逐项按"偏导指标多重集 + 度量指标对"配对，恰好两两相消。

剩下的缩并是形式的指标运算：把 $\nabla^aR_{abcd}$ 与 Ricci 张量、标量曲率的标准定义比对即可；关键是缩并时利用曲率张量的成对反对称性，将两个指标收缩成 Ricci 与 $S$。整条思路是"用测地法坐标把微分恒等式化归为偏导数的对称性，再做指标配对"。

## 证明过程

**步骤 1：引入测地法坐标。** 固定 $p\in M$，取以 $p$ 为中心的法坐标，使

$$g_{ij}(p)=\delta_{ij},\qquad \Gamma^l_{ij}(p)=0,\qquad \partial_m\Gamma^l_{ij}\ \text{一般不消失}.$$

由 $\Gamma^l_{ij}=\frac12g^{la}(\partial_jg_{ia}+\partial_ig_{ja}-\partial_ag_{ij})$ 在 $p$ 点求一次导数，并利用 $\partial g_{ij}(p)=0$，可得

$$R_{ijkl}(p)=\tfrac12\bigl(\partial_i\partial_kg_{jl}-\partial_i\partial_lg_{jk}+\partial_j\partial_lg_{ik}-\partial_j\partial_kg_{il}\bigr)\Big|_p,\qquad \nabla_m\big|_p=\partial_m\big|_p.$$

**步骤 2：写出三项。** 由步骤 1，在 $p$ 点

$$\nabla_mR_{ijkl}=\tfrac12\partial_m\bigl(\partial_i\partial_kg_{jl}-\partial_i\partial_lg_{jk}+\partial_j\partial_lg_{ik}-\partial_j\partial_kg_{il}\bigr),$$

$$\nabla_kR_{ijlm}=\tfrac12\partial_k\bigl(\partial_i\partial_lg_{jm}-\partial_i\partial_mg_{jl}+\partial_j\partial_mg_{il}-\partial_j\partial_lg_{im}\bigr),$$

$$\nabla_lR_{ijmk}=\tfrac12\partial_l\bigl(\partial_i\partial_mg_{jk}-\partial_i\partial_kg_{jm}+\partial_j\partial_kg_{im}-\partial_j\partial_mg_{ik}\bigr).$$

**步骤 3：逐项配对相消。** 把三式相加，按"度量指标对"归并，用 $\partial$ 可交换与 $g$ 对称。

- 含 $g_{jl}$ 的两项：$+\partial_m\partial_i\partial_kg_{jl}$ 与 $-\partial_k\partial_i\partial_mg_{jl}$。两个三次偏导的指标多重集同为 $\{i,k,m\}$，故相消。
- 含 $g_{ik}$ 的两项：$+\partial_m\partial_j\partial_lg_{ik}$ 与 $-\partial_l\partial_j\partial_mg_{ik}$，多重集同为 $\{j,l,m\}$，相消。
- 含 $g_{jk}$ 的两项：$-\partial_m\partial_i\partial_lg_{jk}$ 与 $+\partial_l\partial_i\partial_mg_{jk}$，多重集同为 $\{i,l,m\}$，相消。
- 含 $g_{il}$ 的两项：$-\partial_m\partial_j\partial_kg_{il}$ 与 $+\partial_k\partial_j\partial_mg_{il}$，多重集同为 $\{j,k,m\}$，相消。
- 含 $g_{jm}$ 的两项：$+\partial_k\partial_i\partial_lg_{jm}$ 与 $-\partial_l\partial_i\partial_kg_{jm}$，多重集同为 $\{i,k,l\}$，相消。
- 含 $g_{im}$ 的两项：$-\partial_k\partial_j\partial_lg_{im}$ 与 $+\partial_l\partial_j\partial_kg_{im}$，多重集同为 $\{j,k,l\}$，相消。

六组两两抵消，故 $\nabla_mR_{ijkl}+\nabla_kR_{ijlm}+\nabla_lR_{ijmk}=0$ 在 $p$ 点成立。由于 $p$ 任意而恒等式是张量等式，它在 $M$ 上处处成立。

**步骤 4：缩并。** 在恒等式 $\nabla_mR_{ijkl}+\nabla_kR_{ijlm}+\nabla_lR_{ijmk}=0$ 中，把 $i$ 与 $l$ 用 $g^{il}$ 缩并，并利用 $\nabla g=0$ 把度量移入导数内，再由成对反对称性把收缩出的曲率项辨识为 Ricci 张量，得

$$\nabla^aR_{abcd}=\nabla_cR_{bd}-\nabla_dR_{bc}.$$

再以 $g^{bd}$ 缩并：左端 $g^{bd}\nabla^aR_{abcd}=\nabla^aR_{ac}$；右端 $g^{bd}(\nabla_cR_{bd}-\nabla_dR_{bc})=\nabla_cS-\nabla^bR_{bc}$。于是

$$\nabla^aR_{ac}=\nabla_cS-\nabla^aR_{ac}\ \Longrightarrow\ 2\nabla^aR_{ac}=\nabla_cS.$$

最后把它改写为 Einstein 张量的形式：

$$\nabla^iG_{ij}=\nabla^iR_{ij}-\tfrac12\nabla_jS=\tfrac12\nabla_jS-\tfrac12\nabla_jS=0.$$

证毕。

## 相关条目

- [Riemann曲率张量的对称性](./Riemann曲率张量的对称性.md)：第一 Bianchi 恒等式与成对反对称性，是本定理缩并步骤的基础。
- [协变外微分与Bianchi恒等式](../第48级-数学物理/协变外微分与Bianchi恒等式.md)：用外微分把两条 Bianchi 恒等式统一表述。
- [Bochner公式](./Bochner公式.md)：Weitzenböck/Bochner 型恒等式的推导要反复交换协变导数，用到本恒等式。
- [Ricci流与Poincare猜想](./Ricci流与Poincare猜想.md)：Einstein 张量散度为零是 Ricci 流方程与孤立子分析的基本恒等式。
- [截面曲率Ricci曲率标量曲率](./截面曲率Ricci曲率标量曲率.md)：缩并形式的左侧即 Ricci 与标量曲率，本定理给出它们的微分关系。
