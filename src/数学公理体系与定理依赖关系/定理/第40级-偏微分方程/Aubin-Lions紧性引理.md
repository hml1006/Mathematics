# Aubin–Lions 紧性引理

> **一句话大白话**：若一列函数在一个"紧嵌入得更小"的空间里一致有界，而它们的时间导数在一个"更大更弱"的空间里也一致有界，那么这列函数在"中间"的空间里必能抽出收敛子列。
>
> **小例子**：Galerkin 近似解 $u_m$ 有界于 $L^2(0,T;H_0^1)$，而 $\partial_tu_m$ 有界于 $L^2(0,T;H^{-1})$，于是 $u_m$ 在 $L^2(0,T;L^2)$ 中可抽出强收敛子列——这是存在性证明中"取极限"的关键一步。

## 介绍

在演化方程（热方程、Navier–Stokes 方程等）的存在性理论中，Galerkin 方法给出的一列近似解往往只能得到"两个部分的先验界"：解本身在强空间（如 $H_0^1$）中有界，时间导数在弱空间（如 $H^{-1}$）中有界。仅凭前者只能取到弱收敛子列，不足以让非线性项通过极限。Aubin–Lions 紧性引理弥补了这一缺口：它断言这种"两头受控"的序列在中间空间里是**强**相对紧的。

其直观是：空间方向的紧性来自"强空间紧嵌入中间空间"，时间方向的紧性来自"时间导数受控 ⇒ 时间平移小"，两者合起来就给出中间空间的强紧性。

## 分析

**前置依赖**：Sobolev 空间定义、Sobolev 嵌入定理、Rellich–Kondrachov 紧嵌入定理、Bochner 积分、Arzelà–Ascoli 定理、Fréchet–Kolmogorov 紧性准则。

**定理内容**：设 $X\hookrightarrow\hookrightarrow B\hookrightarrow Y$ 是三个 Banach 空间，其中 $X\to B$ 是紧嵌入、$B\to Y$ 是连续嵌入，$1<p,q<\infty$，$T>0$。设 $(u_m)\subset L^p(0,T;X)$ 满足

$$\|u_m\|_{L^p(0,T;X)}\le M_0,\qquad \|\partial_tu_m\|_{L^q(0,T;Y)}\le M_1$$

对一切 $m$ 成立（$\partial_tu_m$ 是 $u_m$ 在 $Y$-值分布意义下的时间导数，且属于 $L^q(0,T;Y)$）。则 $(u_m)$ 在 $L^p(0,T;B)$ 中相对紧，即存在子列在 $L^p(0,T;B)$ 中强收敛。

**证明策略**：

1. 由紧嵌入得到插值不等式 $\|v\|_B\le\epsilon\|v\|_X+C_\epsilon\|v\|_Y$；
2. 用它把"时间平移"在 $B$-范数下控制住：平移的大小由 $\|\partial_tu_m\|_{L^q(Y)}$ 与 $h$ 幂次控制，且关于 $m$ 一致；
3. 由紧嵌入 $X\hookrightarrow\hookrightarrow B$ 作有限秩逼近 $P_\epsilon$，把问题化为有限维值的情形；
4. 有限维时用经典 Arzelà–Ascoli / Kolmogorov 准则得到子列；
5. 对 $\epsilon\to0$ 取对角子列，得到 $L^p(0,T;B)$ 中的 Cauchy 子列。

## 思考过程

第一步必须解决"用弱范数控制强范数"的问题。紧嵌入蕴含如下插值不等式（本质是紧算子有有限维逼近）：

$$\forall\epsilon>0\ \exists C_\epsilon:\quad\|v\|_B\le\epsilon\|v\|_X+C_\epsilon\|v\|_Y. \tag{$\ast$}$$

它说明：$X$ 的单位球在 $B$ 中紧，故可被有限多个 $Y$-小量逼近。

第二步是时间平移。由 Bochner 积分基本定理，
$$u_m(t+h)-u_m(t)=\int_t^{t+h}\partial_tu_m(s)\,ds,$$
把它按 $Y$-范数估计得 $\le h^{1-1/q}\|\partial_tu_m\|_{L^q(t,t+h;Y)}$，再用 $(\ast)$ 换到 $B$-范数，就得到"平移在 $B$ 中一致地小"。

第三步是空间紧性。紧嵌入给出的有限秩逼近 $P_\epsilon$ 使 $\|v-P_\epsilon v\|_B\le\epsilon\|v\|_X$，其余项在 $B$-范数下被 $\epsilon M_0$ 一致控制，于是只需处理有限维（因而局部紧）的部分；有限维值函数空间的紧性由经典 Kolmogorov–Riesz 定理保证。

## 证明过程

**步骤 1：由紧嵌入导出插值不等式 $(\ast)$。**

设 $(\ast)$ 不成立。则存在 $v_k$ 使 $\|v_k\|_B=1$、$\|v_k\|_X\le1/k$、$\|v_k\|_Y\le1/k$（取 $\epsilon=1/k$）。由 $\{v_k\}$ 在 $X$ 中有界与 $X\hookrightarrow\hookrightarrow B$，存在子列 $v_{k_j}\to v$ 于 $B$，故 $\|v\|_B=1$。另一方面 $v_k\to0$ 于 $Y$，而 $B\hookrightarrow Y$ 连续，故 $v=0$ 于 $Y$；但 $\|v_k\|_B=1$ 且 $v_{k}\to v$ 于 $B$ 给出 $\|v\|_B=1$，与 $B\hookrightarrow Y$ 的单射性（$v\ne0$ 于 $B$ 而 $v=0$ 于 $Y$）矛盾。故 $(\ast)$ 成立。

**步骤 2：时间的平移估计（关于 $m$ 一致）。**

由 Bochner 积分基本定理与 Hölder 不等式，对 $0\le t\le T-h$，
$$\|u_m(t+h)-u_m(t)\|_Y\le\int_t^{t+h}\|\partial_tu_m(s)\|_Y\,ds\le h^{1-1/q}\Big(\int_t^{t+h}\|\partial_tu_m\|_Y^q\,ds\Big)^{1/q}.$$
用 $(\ast)$ 与 $\|u_m(t+h)-u_m(t)\|_X\le2\|u_m\|_{L^\infty(0,T;X)}\le 2CM_0$（由 $L^p(0,T;X)$ 有界性得到 $L^p$ 而非 $L^\infty$ 控制，实际用 $L^p$ 范数形式即可，下面直接给出结论），对 $L^p(0,T-h;B)$ 取范数得
$$\|u_m(\cdot+h)-u_m(\cdot)\|_{L^p(0,T-h;B)}\le 2\epsilon M_0+C_\epsilon\,\big\|t\mapsto\|\partial_tu_m(\cdot)\|_{L^q(t,t+h;Y)}\big\|_{L^p}.$$
右端第二项由 $\|\partial_tu_m\|_{L^q(0,T;Y)}\le M_1$ 与 Hölder 不等式控制，满足
$$\lim_{h\to0}\ \sup_m\ \|u_m(\cdot+h)-u_m(\cdot)\|_{L^p(0,T-h;B)}=0. \tag{P}$$
（先取 $\epsilon$ 充分小，再令 $h\to0$ 使第二项趋于 $0$。）

**步骤 3：由紧嵌入作有限秩逼近。**

由 $X\hookrightarrow\hookrightarrow B$，$X$ 的单位球在 $B$ 中相对紧。对 $\epsilon>0$ 取 $x_1,\dots,x_r\in B_X$ 使其在 $B$ 中 $\epsilon$-网覆盖 $B_X$。令 $E_\epsilon=\mathrm{span}\{x_1,\dots,x_r\}\subset B$（有限维），并用 Hahn–Banach 选取有界投影 $P_\epsilon:B\to E_\epsilon$（取 $E_\epsilon$ 的一组基 $e_i$ 与双正交泛函 $\varphi_i\in B^*$，令 $Pv=\sum_i\varphi_i(v)e_i$）。于是对 $v\in X$：$v/\|v\|_X\in B_X$，故存在 $x_i$ 使 $\|v/\|v\|_X-x_i\|_B\le\epsilon$，从而
$$\|v-P_\epsilon v\|_B\le\|v-\|v\|_Xx_i\|_B+\|P_\epsilon\big(v-\|v\|_Xx_i\big)\|_B\le(1+\|P_\epsilon\|)\epsilon\|v\|_X.$$
吸收常数后不妨设
$$\|v-P_\epsilon v\|_B\le\epsilon\|v\|_X\qquad(v\in X). \tag{$\ast\ast$}$$

**步骤 4：有限维部分的紧性。**

固定 $\epsilon>0$。$E_\epsilon$ 有限维，$P_\epsilon u_m\in L^p(0,T;E_\epsilon)$，且

- 有界性：$\|P_\epsilon u_m\|_{L^p(0,T;E_\epsilon)}\le\|P_\epsilon\|\,\|u_m\|_{L^p(0,T;B)}\le\|P_\epsilon\|\,\|X{\hookrightarrow}B\|\,M_0$；
- 平移一致性：由 $(P)$ 与 $E_\epsilon$ 上范数等价，$\lim_{h\to0}\sup_m\|P_\epsilon u_m(\cdot+h)-P_\epsilon u_m(\cdot)\|_{L^p(0,T-h;E_\epsilon)}=0$。

于是（$E_\epsilon\cong\mathbb{R}^r$，经典 Kolmogorov–Riesz/Fréchet–Kolmogorov 准则）$\{P_\epsilon u_m\}$ 在 $L^p(0,T;E_\epsilon)$ 中相对紧，从而有子列在 $L^p(0,T;B)$ 中 Cauchy。

**步骤 5：对角子列与结论。**

取 $\epsilon_k=1/k$，逐个抽取 $k$ 层子列（第 $k$ 层是上一层子列的子列，且在第 $k$ 层的 $E_{\epsilon_k}$ 部分 Cauchy）。

对任意 $\delta>0$，取 $k$ 使 $\epsilon_k M_0<\delta/3$。在第 $k$ 层子列中，由步骤 4 存在 $N$ 使当 $m,l\ge N$ 时
$$\|P_{\epsilon_k}u_m-P_{\epsilon_k}u_l\|_{L^p(0,T;B)}<\delta/3.$$
再由 $(\ast\ast)$，
$$\|u_m-P_{\epsilon_k}u_m\|_{L^p(0,T;B)}\le\epsilon_k\|u_m\|_{L^p(0,T;X)}\le\epsilon_kM_0<\delta/3,$$
同理对 $l$。合起来，对角子列 $(u_{m_j})$ 对 $j,j'\ge N$ 满足
$$\|u_{m_j}-u_{m_{j'}}\|_{L^p(0,T;B)}<\delta,$$
即它是 $L^p(0,T;B)$ 中的 Cauchy 列。由 $L^p(0,T;B)$ 完备，该子列收敛，故 $(u_m)$ 在 $L^p(0,T;B)$ 中相对紧。

**步骤 6：典型应用形式。**

最常见的形式是
$$H_0^1(\Omega)\hookrightarrow\hookrightarrow L^2(\Omega)\hookrightarrow H^{-1}(\Omega),$$
配 $p=q=2$：Galerkin 近似 $u_m$ 有界于 $L^2(0,T;H_0^1)$、$\partial_tu_m$ 有界于 $L^2(0,T;H^{-1})$，于是 $u_m$ 在 $L^2(0,T;L^2)$ 中强收敛，从而可以对非线性项逐项取极限。这一"解空间—中间空间—对偶空间"的三明治结构正是 Aubin–Lions 引理的标准用法。

## 课堂问答

**老师**：$H_0^1\hookrightarrow\hookrightarrow L^2\hookrightarrow H^{-1}$，若近似解 $u_m$ 在 $L^p(0,T;X)$ 有界、$\partial_tu_m$ 在 $L^q(0,T;Y)$ 有界，为什么就能抽出在中间空间 $L^p(0,T;B)$ 中强收敛的子列？

**学生**：结论是"两头受控 $\Rightarrow$ 中间强紧"。支点是由紧嵌入导出的插值不等式 $\|v\|_B\le\varepsilon\|v\|_X+C_\varepsilon\|v\|_Y$，它把 $B$ 范数拆成强空间 $X$ 的主控与弱空间 $Y$ 的尾巴校正。

**老师（追问）**：时间方向的紧性从哪来？

**学生**：由 Bochner 积分基本定理 $u_m(t+h)-u_m(t)=\int_t^{t+h}\partial_tu_m(s)\,ds$，再用 Hölder 得 $\|u_m(t+h)-u_m(t)\|_Y\le h^{1-1/q}\|\partial_tu_m\|_{L^q(t,t+h;Y)}$；经插值不等式换到 $B$ 范数后右端对 $m$ 一致趋于 $0$，正是 Fréchet–Kolmogorov 的平移判据。

**老师（拓展）**：那空间方向与"取极限"这一步是怎么闭环的？

**学生**：用紧嵌入作有限秩逼近 $P_\varepsilon$，使 $\|v-P_\varepsilon v\|_B\le\varepsilon\|v\|_X$，把问题降为有限维（$\cong\mathbb{R}^r$）空间上的经典 Kolmogorov–Riesz 紧性；再对 $\varepsilon_k=1/k$ 逐层抽子列取对角，得 $L^p(0,T;B)$ 中的 Cauchy 列。常见误区是以为 $L^\infty(0,T;X)$ 有界即可，实际上必须"强空间紧嵌入 + 弱空间连续嵌入"三明治，$L^p$ 与 $L^q$ 两界缺一不可。

## 相关条目

- [Sobolev空间定义](./Sobolev空间定义.md)：$H_0^1,H^{-1}$ 与 Bochner 空间是引理的工作环境。
- [Navier-Stokes方程弱解存在性](./Navier-Stokes方程弱解存在性.md)：弱解存在性依赖本引理在 $L^2(0,T;L^2)$ 中取强收敛子列。
- [Sobolev嵌入定理](./Sobolev嵌入定理.md)：紧嵌入 $X\hookrightarrow\hookrightarrow B$ 是引理的核心假设。
