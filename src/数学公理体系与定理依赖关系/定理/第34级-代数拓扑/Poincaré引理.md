# Poincaré 引理

> **一句话大白话**：在一个没有"洞"的区域里，任何一个环路积分都为零的场必是某个函数的梯度；用形式语言说，闭形式一定是恰当形式。
>
> **小例子**：在 $\mathbb R^2$ 上，若 $\omega=P\,dx+Q\,dy$ 满足 $\partial_yP=\partial_xQ$（闭），则存在 $f$ 使 $df=\omega$，即 $\omega$ 恰当。

## 介绍

Poincaré 引理是 de Rham 理论中最基本的局部结果，其精神可追溯到庞加莱关于单连通区域上保守场的讨论。它断言：在可缩（特别地，星形）的开区域上，外微分复形在正次数处正合——每个闭形式都是恰当形式，即

$$d\omega=0\implies\omega=d\eta.$$

用上同调语言，这就是 $H^k_{dR}(U)=0$（$k\ge1$）对可缩区域 $U$ 成立。它说明"局部上处处如此"是微分形式的普遍性质，算子上同调之所以有趣，正因为整体（有洞）的区域会破坏这一结论。

Poincaré 引理是 de Rham 上同调计算与 Mayer–Vietoris 论证的局部基础，也在辛几何（Darboux 定理）、规范场论（局部势的存在）以及热力学（状态函数的存性）中反复使用。

## 分析

**前置依赖**：外微分与 $d^2=0$、微分形式的拉回、Cartan 公式（$\mathcal L_X=d\iota_X+\iota_Xd$）、闭形式与恰当形式、星形区域与同伦、变上限积分

**定理内容**：设 $U\subseteq\mathbb R^n$ 是星形开集（存在 $x_0\in U$，使对每个 $x\in U$ 与 $t\in[0,1]$ 有 $x_0+t(x-x_0)\in U$；不妨设 $x_0=0$）。若 $\omega\in\Omega^k(U)$ 满足 $d\omega=0$（$k\ge1$），则存在 $\eta\in\Omega^{k-1}(U)$ 使

$$\omega=d\eta.$$

因此 $H^k_{dR}(U)=0$ 对一切 $k\ge1$ 成立（可缩光滑流形亦如此）。

**关键要点**：

- 结论是"整体存在（原函数 $\eta$）"，其构造来自沿收缩同伦的积分；
- 只需星形（或可缩），一般区域若带"洞"则结论失效，例如 $\mathbb R^2\setminus\{0\}$ 上的 $\frac{-y\,dx+x\,dy}{x^2+y^2}$ 闭而不恰当；
- 对 $k=0$，闭形式即常函数，恰当形式只有 $0$；故 $H^0_{dR}(U)=\mathbb R$（$U$ 连通）。

## 思考过程

核心工具是"同伦算子的积分表示"。考虑收缩同伦 $H_t(x)=tx$，$t\in[0,1]$，把 $U$ 连续缩到原点。它诱导拉回 $H_t^*:\Omega^k(U)\to\Omega^k(U)$，且 $H_0^*\omega=0$（$k\ge1$，因 $H_0$ 是常映射，拉回 $k\ge1$ 形式为零），$H_1^*\omega=\omega$。

对 $t$ 求导并借助 Cartan 公式，把 $\frac{d}{dt}H_t^*\omega$ 写成"外微分的边界项"与"含 $d\omega$ 的项"之和。把 $t$ 从 $0$ 到 $1$ 积分，左边就是 $\omega-0=\omega$，右边第一项自动是某个形式的外微分（记作 $dK\omega$），第二项是 $K d\omega$。于是得到同伦公式

$$\omega=dK\omega+Kd\omega.$$

当 $d\omega=0$ 时第二项消失，$\omega=d(K\omega)$ 即恰当。要做的是把 $K$ 写成显式积分算子，并说明它在 $U$ 上光滑、良定义。关键细节是对 $k\ge1$ 时 $t=0$ 端的贡献为零，$\frac1t$ 型奇异项会与 $H_t^*$ 的 $t^{k-1}$ 阶衰减相消。

## 证明过程

**步骤 1：构造同伦算子 $K$。** 定义光滑同伦

$$H:[0,1]\times U\to U,\qquad H(t,x)=tx.$$

固定 $t$，沿 $H$ 的"速度场"为 $V_t(y)=\dfrac{1}{t}\sum_{i=1}^n y_i\dfrac{\partial}{\partial y_i}$（当 $t>0$；在 $y=H_t(x)=tx$ 处 $\partial H/\partial t=x=y/t$）。定义

$$K\omega=\int_0^1 H_t^*\big(\iota_{V_t}\omega\big)\,dt,\qquad \omega\in\Omega^k(U),\ k\ge1,$$

其中 $H_t^*$ 是按 $H_t(x)=tx$ 的拉回，积分点态进行（对每个 $x$，被积函数是 $\Lambda^kT_x^*U$ 中的光滑曲线积分）。

**步骤 2：说明 $K$ 良定义且光滑。** 对 $k$-形式 $\omega$，$\iota_{V_t}\omega$ 是 $(k-1)$-形式；$H_t^*(\iota_{V_t}\omega)$ 的分量形如 $t^{\,k-2}$ 乘以 $x$ 与 $\omega$ 在 $tx$ 处分量之积（因 $(k-1)$-形式拉回贡献 $t^{k-1}$，$V_t$ 贡献 $t^{-1}$）。于是对 $k\ge1$ 被积函数在 $t\to0^+$ 有界可积，积分在 $U$ 上光滑。故 $K:\Omega^k(U)\to\Omega^{k-1}(U)$ 良定义。

**步骤 3：同伦公式。** 对固定 $t>0$，由 Cartan 公式（$\mathcal L_{V_t}=d\iota_{V_t}+\iota_{V_t}d$）与"拉回的导数等于李导数的拉回"

$$\frac{d}{dt}\big(H_t^*\omega\big)=H_t^*\big(\mathcal L_{V_t}\omega\big)=H_t^*\big(d(\iota_{V_t}\omega)+\iota_{V_t}(d\omega)\big)=d\big(H_t^*\iota_{V_t}\omega\big)+H_t^*\big(\iota_{V_t}(d\omega)\big),$$

其中末步用了拉回与外微分交换 $H_t^*d=dH_t^*$。对 $t$ 从 $0$ 到 $1$ 积分：

$$\omega-H_0^*\omega=\int_0^1\frac{d}{dt}\big(H_t^*\omega\big)dt=d\Big(\int_0^1H_t^*\iota_{V_t}\omega\,dt\Big)+\int_0^1H_t^*\iota_{V_t}(d\omega)\,dt.$$

因 $k\ge1$，$H_0$ 是常映射，$H_0^*\omega=0$。由步骤 1 中 $K$ 的定义，

$$\omega=dK\omega+Kd\omega.$$

**步骤 4：闭形式必恰当。** 设 $d\omega=0$。则步骤 3 给出 $\omega=d(K\omega)+K(0)=d(K\omega)$。令 $\eta=K\omega\in\Omega^{k-1}(U)$，得 $\omega=d\eta$，即 $\omega$ 恰当。

**步骤 5：上同调结论。** 由 $d^2=0$，每个恰当形式都是闭形式；步骤 4 说明反之亦真。故对 $k\ge1$，

$$H^k_{dR}(U)=\frac{\ker(d:\Omega^k\to\Omega^{k+1})}{\operatorname{im}(d:\Omega^{k-1}\to\Omega^k)}=0.$$

（当 $k=0$ 时，$\ker d$ 由局部常函数组成，连通时 $H^0_{dR}(U)=\mathbb R$。）对可缩流形，取收缩同伦按上述同一论证即得相同结论。$\square$

## 相关条目

- [deRham定理](./deRham定理.md)：de Rham 上同调与奇异上同调的同构以本引理为其局部可缩情形的起点。
- [奇异同调群](./奇异同调群.md)：本引理给出可缩区域上同调为零，是奇异同调"锥化"论证的微分形式对偶。
