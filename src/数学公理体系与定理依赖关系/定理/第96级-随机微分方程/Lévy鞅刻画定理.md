# Lévy 鞅刻画定理

> **一句话大白话**：一个连续鞅若其"波动强度"（二次变差）恰好等于时间 $t$，那它必定是布朗运动——"连续鞅 + 二次变差为 $t$"完全刻画了布朗运动。
>
> **小例子**：Itô 积分 $W_t$ 满足 $[W]_t=t$，故是 Brown 运动；反之任何满足 $[M]_t=ct$ 的连续局部鞅，经时间缩放 $M_t/\sqrt c$ 也是标准 Brown 运动。

## 一、定理介绍

> **前置依赖**：鞅与连续局部鞅、二次变差与协变差、Brown 运动的存在性、鞅收敛定理、Itô 积分。

Lévy 鞅刻画定理（Lévy's characterization of Brownian motion）断言：若连续局部鞅 $M$ 满足 $M_0=0$ 且二次变差 $[M]_t=t$，则 $M$ 是标准布朗运动。它由 Paul Lévy 于 1948 年在研究布朗运动的鞅性质时给出，是随机分析中"用二次变差识别布朗运动"的奠基结果。其证明思路——直接验证 $e^{i\lambda M_t+\lambda^2t/2}$ 是鞅从而定出高斯特征函数——成为鞅问题（martingale problem）理论的模板，并催生了刻画跳跃过程的 Lévy–Itô 分解。该定理在扩散过程、随机微分方程弱解的存在唯一性以及 Tanaka 公式中反复被引用。

## 二、原理思路

1. 对固定 $\lambda$，用 Itô 公式作用于 $Z_t=\exp(i\lambda M_t+\lambda^2t/2)$，因 $d\langle M\rangle_t=dt$ 使二阶项与漂移相消，得 $dZ_t=Z_t\cdot i\lambda\,dM_t$，故 $Z$ 是局部鞅。
2. 由 $Z$ 的非负性与 $[0,t]$ 上的有界性（$|Z_s|=e^{\lambda^2s/2}$）用有界停止把局部鞅化为真鞅，取条件期望得增量的特征函数 $\mathbb{E}[e^{i\lambda(M_t-M_s)}\mid\mathcal F_s]=e^{-\lambda^2(t-s)/2}$。
3. 由该式得增量独立且服从 $\mathcal N(0,t-s)$；结合轨道连续性与 Lévy 连续性定理，$M$ 的有限维分布与标准布朗运动一致。

## 三、定理的严格表述

设 $M=(M_t)_{t\ge0}$ 为适应于滤流 $(\mathcal{F}_t)$ 的连续局部鞅，$M_0=0$，且二次变差满足

$$
[M]_t=t\qquad\forall t\ge0\ (\text{a.s.}).
$$

则 $M$ 是标准 $(\mathcal F_t)$-布朗运动：$M$ 是连续 Gauss 过程，且对 $s<t$ 有增量 $M_t-M_s\sim\mathcal N(0,t-s)$、与 $\mathcal F_s$ 独立。

推广：若 $[M]_t=ct$（$c>0$ 常数），则 $M_t/\sqrt c$ 是标准布朗运动。

## 四、证明过程

**步骤 1（构造指数局部鞅）。** 对固定 $\lambda\in\mathbb{R}$ 令

$$
Z_t=\exp\Big(i\lambda M_t+\frac{\lambda^2}{2}t\Big).
$$

因 $M$ 连续且 $[M]_t=t$，对 $Z_t=f(t,M_t)$ 用 Itô 公式（$f(t,x)=e^{i\lambda x+\lambda^2t/2}$）：

$$
dZ_t=Z_t\Big(i\lambda\,dM_t+\frac{\lambda^2}{2}dt\Big)+\frac12 Z_t\,(i\lambda)^2\,d[M]_t=Z_t\Big(i\lambda\,dM_t+\frac{\lambda^2}{2}dt\Big)-\frac{\lambda^2}{2}Z_t\,dt=Z_t\cdot i\lambda\,dM_t .
$$

因 $dM$ 为局部鞅微分、系数 $Z$ 局部有界，故 $Z$ 是局部鞅。

**步骤 2（局部鞅化为真鞅）。** 对固定 $t>0$，有 $|Z_s|=e^{\lambda^2s/2}\le e^{\lambda^2t/2}$ 对 $s\in[0,t]$ 一致有界。用停止时间 $\tau_k=\inf\{s: |Z_s|\ge k\}\wedge t$ 把 $Z$ 在 $[0,t]$ 上有界停止，得真鞅，故对 $s<t$，

$$
\mathbb{E}\big[Z_t\mid\mathcal F_s\big]=Z_s .
$$

**步骤 3（求增量特征函数）。** 把 $Z$ 的表达式代入并整理 $e^{\lambda^2 t/2}$、$e^{\lambda^2 s/2}$：

$$
\mathbb{E}\Big[e^{i\lambda M_t}\,e^{\lambda^2 t/2}\ \Big|\ \mathcal F_s\Big]=e^{i\lambda M_s}\,e^{\lambda^2 s/2}
\ \Longrightarrow\ \mathbb{E}\big[e^{i\lambda(M_t-M_s)}\mid\mathcal F_s\big]=e^{-\lambda^2(t-s)/2}.
$$

右端与 $\mathcal F_s$ 无关，故 $M_t-M_s$ 与 $\mathcal F_s$ 独立，且其特征函数为 $e^{-\lambda^2(t-s)/2}$。

**步骤 4（识别为高斯与布朗运动）。** 在步骤 3 中取 $s=0$ 得 $\mathbb{E}[e^{i\lambda M_t}]=e^{-\lambda^2t/2}$，即 $M_t\sim\mathcal N(0,t)$。对 $0=t_0<t_1<\cdots<t_n$，反复用步骤 3 得增量 $M_{t_i}-M_{t_{i-1}}$ 相互独立、分别服从 $\mathcal N(0,t_i-t_{i-1})$。故 $M$ 的有限维分布与标准布朗运动一致；再由 $M$ 的轨道连续性与 Lévy 连续性定理，$M$ 是布朗运动。推广情形对 $M_t/\sqrt c$ 直接验证 $[M/\sqrt c]_t=t$ 并套用上述结论。$\square$

## 五、应用与意义

- 给出布朗运动的鞅刻画，是鞅问题理论的原型与扩散过程弱解唯一性判定的核心。
- 结合鞅表示定理，把扩散过程与 Itô 积分的性质化归为二次变差的计算。
- 推广为 Lévy–Itô 分解与 Lévy 过程刻画，用于金融建模中的跳跃扩散模型。

## 课堂问答

**老师**：凭什么"连续 + 二次变差等于 $t$"就能断定一个鞅是布朗运动？

**学生**：先给结论——若连续局部鞅 $M_0=0$、$[M]_t=t$，则 $M$ 是标准布朗运动。关键是证出增量的特征函数为 $e^{-\lambda^2(t-s)/2}$。

**老师（追问）**：这个特征函数是怎么算出来的？

**学生**：对 $Z_t=\exp(i\lambda M_t+\frac{\lambda^2}2t)$ 用 Itô 引理，因 $d[M]_t=dt$ 使二阶项恰好抵消漂移，得 $dZ_t=Z_t\,i\lambda\,dM_t$，故 $Z$ 为局部鞅；由 $|Z_s|\le e^{\lambda^2t/2}$ 有界，用停止时间化真鞅，取条件期望即得 $\mathbb{E}[e^{i\lambda(M_t-M_s)}\mid\mathcal F_s]=e^{-\lambda^2(t-s)/2}$。

**老师（拓展）**：由此能推出什么、推广是什么？

**学生**：右端与 $\mathcal F_s$ 无关，故增量独立且 $\sim\mathcal N(0,t-s)$，配合轨道连续性即有限维分布与布朗运动一致；若 $[M]_t=ct$，则 $M_t/\sqrt c$ 是标准布朗运动。它是鞅问题理论与 Lévy-Itô 分解的模板。常见误区是丢掉"连续"或"局部"二字。

## 相关条目

- [Itô引理](./Itô引理.md)：本定理步骤 1 中构造指数鞅所用的工具。
- [SDE解的存在唯一性定理](./SDE解的存在唯一性定理.md)：用鞅刻画判定解的存在唯一性。
- [Girsanov定理](./Girsanov定理.md)：在等价测度变换下保持布朗性，与本定理配合使用。
- [Brown运动的存在性](../第41级-随机过程/Brown运动的存在性.md)：布朗运动的构造。
- [鞅收敛定理](../第41级-随机过程/鞅收敛定理.md)：步骤 2 中真鞅性质的理论依据。
