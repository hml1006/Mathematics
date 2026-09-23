# Alexander–Whitney 映射与 Eilenberg–Zilber 定理

> **一句话大白话**：乘积空间 $X\times Y$ 的链复形，与两个因子链复形的张量积复形，在链同伦意义下是"同一台机器"；Alexander–Whitney 映射与 Eilenberg–Zilber 映射就是这两台机器之间互为逆的一对翻译器。
>
> **小例子**：取 $X=Y=S^1$。定理把 $H_1(S^1\times S^1)\cong\mathbb{Z}^2$ 的来源说清楚：两个生成元分别来自 $H_1(S^1)\otimes H_0(S^1)$ 与 $H_0(S^1)\otimes H_1(S^1)$，正是 Künneth 分裂的雏形。

## 介绍

设 $R$ 为交换环。奇异链复形 $C_*(X;R)$ 与张量积复形 $C_*(X;R)\otimes_R C_*(Y;R)$ 各自计算着乘积 $X\times Y$ 与两个因子的同调。但二者在链水平上并不相等：$C_n(X\times Y;R)$ 由全体奇异单形 $\Delta^n\to X\times Y$ 自由生成，而 $\bigoplus_{p+q=n}C_p(X;R)\otimes_R C_q(Y;R)$ 由"一对奇异单形"生成，两者的生成元个数与代数结构都不同。

Eilenberg–Zilber 定理断言：只要允许"链同伦"这一弱化，二者就完全等价。这里需要两个显式的链映射：

- **Alexander–Whitney 映射** $AW$：把一个乘积单形沿前 $p$ 个顶点、后 $q$ 个顶点切成两半，得到一对单形；
- **Eilenberg–Zilber（shuffle，洗牌）映射** $EZ$：把一对单形按所有可能的交错方式"织"进乘积，得到乘积中的一串单形。

它们是链同伦逆，于是同调层面给出 Künneth 同构。这一结论是上同调杯积、Leray–Serre 谱序列、Künneth 公式等一切"乘积构造"的链层基石。

## 分析

**前置依赖**：奇异同调群、链复形与链映射、张量积复形、链同伦、acyclic models 定理、自由模与线性代数。

**定理内容**：设 $X,Y$ 为拓扑空间，$R$ 为交换环。

1. 存在自然的链映射
$$AW:C_*(X\times Y;R)\to C_*(X;R)\otimes_R C_*(Y;R),$$
以及反向的自然链映射
$$EZ:C_*(X;R)\otimes_R C_*(Y;R)\to C_*(X\times Y;R);$$
2. $AW\circ EZ=\mathrm{id}$；
3. 存在自然链同伦 $EZ\circ AW\simeq \mathrm{id}$，即 $EZ$ 是链同伦等价，$AW$ 是它的同伦逆；
4. 于是同调同构
$$H_n(X\times Y;R)\cong H_n\big(C_*(X;R)\otimes_R C_*(Y;R)\big),$$
并且当 $H_*(X;R)$ 或 $H_*(Y;R)$ 为自由 $R$-模时（例如 $R$ 为域），进一步有 Künneth 分裂
$$H_n(X\times Y;R)\cong\bigoplus_{p+q=n}H_p(X;R)\otimes_R H_q(Y;R).$$

记号约定：$\Delta^n=[e_0,\dots,e_n]$ 是标准 $n$-单形。对 $0\le p\le n$，记 $\Delta^n$ 的**前 $p$-面**为 $\Delta^{p}\xrightarrow{f_{p,n}}\Delta^n$（由 $e_i\mapsto e_i$ 决定），**后 $q=n-p$ 面**为 $\Delta^{q}\xrightarrow{b_{q,n}}\Delta^n$（由 $e_j\mapsto e_{p+j}$ 决定）。对单形 $\sigma:\Delta^n\to X$ 记 $\sigma^{(p)}=\sigma\circ f_{p,n}$、$\sigma_{(q)}=\sigma\circ b_{q,n}$。

## 思考过程

第一件事是把"切"与"织"写成公式。对于一个乘积单形 $\sigma:\Delta^n\to X\times Y$，通过投影它等价于一对单形 $\sigma_X=p_X\circ\sigma:\Delta^n\to X$、$\sigma_Y=p_Y\circ\sigma:\Delta^n\to Y$。最自然的"切法"是：枚举所有分成前 $p$ 段与后 $q$ 段的位置，得到
$$AW(\sigma)=\sum_{p+q=n}\sigma_X^{(p)}\otimes\sigma_Y{}_{(q)}.$$
它把次数 $n$ 映到双次数 $(p,q)$ 的和，正是张量积复形里应有的次数。

反方向没有"唯一"的写法，因为一个 $n$-单形要拆成一对 $(p,q)$-单形，需决定顶点如何交错，于是应对所有 $(p,q)$-shuffle 求和，并配上符号以使所得是链映射。

最困难的一步是 $EZ\circ AW\simeq\mathrm{id}$。对 $AW\circ EZ$ 可以直接验证它是恒等（组合恒等式）；但 $EZ\circ AW$ 与恒等只差一个链同伦，因为乘积空间里"把单形切开再重新交织"并不逐项还原，而只能差出一些"退化组合"。处理这类"只能到同伦"的构造，标准工具是 **acyclic models 定理**：只要源复形自由、且目标复形在"模型"（这里是 $\Delta^p\times\Delta^q$）上无正次数同调，则任何在 $H_0$ 上正确的自然链映射都自然链同伦于恒等。

## 证明过程

**步骤 1：$AW$ 是链映射。**

其定义是"前 $p$-面 $\otimes$ 后 $q$-面"。要证 $AW\circ d=(d\otimes 1+1\otimes d)\circ AW$。两边都等于把 $\sigma$ 的每个 $(n-1)$-面按其被删顶点落在前段或后段来归类：

$$\sum_{i=0}^{p}(-1)^i(\sigma\circ\delta_i)^{(p-1)}\otimes(\sigma\circ\delta_i)_{(q)}+\sum_{i=p+1}^{n}(-1)^i(\sigma\circ\delta_i)^{(p)}\otimes(\sigma\circ\delta_i)_{(q-1)}.$$

其中 $\delta_i:\Delta^{n-1}\to\Delta^n$ 是第 $i$ 个面映射。依据的键事实是面映射的交换律

$$f_{p,n}\circ\delta_i^{(p)}=\delta_i^{(n)}\circ f_{p-1,n-1}\quad(0\le i\le p),\qquad b_{q,n}\circ\delta_{i-p-1}^{(q)}=\delta_i^{(n)}\circ b_{q-1,n-1}\quad(p<i\le n),$$

它说"先取前/后段再删顶点"与"先删顶点再取前/后段"一致。把 $d\sigma=\sum_i(-1)^i\sigma\circ\delta_i$ 代入 $AW$，再对 $(d\otimes 1)AW(\sigma)=\sum_{p+q=n}d(\sigma_X^{(p)})\otimes\sigma_Y{}_{(q)}$ 与 $(-1)^p(1\otimes d)AW(\sigma)$ 分别展开，逐项比较即得两式相同，故 $AW$ 是链映射。

**步骤 2：$AW$ 是自然的。**

若 $u:X\to X'$、$v:Y\to Y'$ 连续，则 $(u\times v)\circ\sigma$ 的投影恰为 $u\circ\sigma_X$ 与 $v\circ\sigma_Y$，且单形的面（前/后段）与 $u,v$ 的复合相容。逐项比较定义即得 $AW\circ (u\times v)_\#=(u_\#\otimes v_\#)\circ AW$，这里 $(u\times v)_\#$ 表示链水平诱导映射，$u_\#\otimes v_\#$ 是张量积上诱导的链映射。

**步骤 3：$EZ$ 的定义。**

一个 $(p,q)$-shuffle 是集合 $\{0,1,\dots,n\}$（$n=p+q$）的一个划分 $\{i_0<\dots<i_p\}\sqcup\{j_0<\dots<j_q\}$；等价地是一个置换 $\pi$。对每个 shuffle 定义仿射映射
$$\lambda_\pi:\Delta^n\to\Delta^p\times\Delta^q,\qquad \lambda_\pi(t_0,\dots,t_n)=\Big(\sum_{a=0}^{p}t_{i_a}e_a,\ \sum_{b=0}^{q}t_{j_b}e_b\Big).$$
它对顶点保序，是单形之间的嵌入。定义

$$EZ(\alpha\otimes\beta)=\sum_{\pi\in Sh(p,q)}(-1)^{\pi}\,(\alpha\times\beta)\circ\lambda_\pi,$$

其中 $(-1)^\pi$ 是 shuffle 的符号（$\mathrm{sgn}$ 约定），$Sh(p,q)$ 为全体 $(p,q)$-shuffle。这是双次数 $(p,q)\to n$ 的 $R$-线性映射，且显然对 $(X,Y)$ 自然。

**步骤 4：$EZ$ 是链映射。**

每个 shuffle $\lambda_\pi$ 把 $\Delta^n$ 的每个面 $\delta_i^{(n)}$ 分解为"$p$ 段的面与 $q$ 段的面的乘积"。因此 shuffle 集合与"在 $p$ 段或 $q$ 段中删一个顶点"的所有方式一一对应，符号也按 shuffle 的符号约定与面的正负号相容（删去 $p$ 段第 $a$ 个顶点等价于置换中做一次换位，符号相差 $(-1)^a$）。代入面公式逐项比较，即得 $EZ\circ(d\otimes 1+1\otimes d)=d\circ EZ$。

**步骤 5：$AW\circ EZ=\mathrm{id}$（shuffle 恒等式）。**

设 $\alpha:\Delta^p\to X$、$\beta:\Delta^q\to Y$，$n=p+q$。对每个 shuffle，$(\alpha\times\beta)\circ\lambda_\pi$ 的前 $p$-面在 $X$ 上的分量是 $\alpha$（当 $\lambda_\pi$ 把前 $p$-面映到 $\Delta^p\times\{e_0\}$ 时），后 $q$-面在 $Y$ 上的分量是 $\beta$；其余 shuffle 给出的是退化单形或"前后段错位"的项。逐项代入 $AW$ 的定义，得

$$AW\big(EZ(\alpha\otimes\beta)\big)=\Big(\sum_{\pi\in Sh(p,q)}(-1)^\pi\Big)\,\alpha\otimes\beta,$$

而难处在于符号。用一个配对论证：若不是对应"恒等划分"的 shuffle，则在序列 $(t)$ 中按从左到右第一个"交错"位置把 shuffle 与其"交换一对相邻顶点"的 shuffle 配对；两个配对成员的符号相反，且所贡献的单形项经 $AW$（前 $p$-面/后 $q$-面）后完全相同，故成对相消。只有唯一的 shuffle 与其配对的符号之和不被抵消，其总贡献恰为 $+\alpha\otimes\beta$。于是 $AW\circ EZ=\mathrm{id}$。

**步骤 6：acyclic models 定理。**

要比较 $EZ\circ AW$ 与 $\mathrm{id}$，先用一个一般的同伦构造引理。

**定理（acyclic models）**：设 $F,G:\mathcal{C}\to Ch(R)_{\ge 0}$ 是两个自然函子，$F$ 在每个次数上自由，且存在"模型"族 $\{M_\alpha\}\subset\mathcal{C}$ 使 $F(M_\alpha)$ 的自由生成元覆盖所有次数；设 $G$ 在模型上无正次数同调，即 $H_n(G(M_\alpha))=0\ (n>0)$。若 $f,g:F\to G$ 是自然链映射且在 $H_0$ 上满足 $H_0(f)=H_0(g)$，则 $f$ 与 $g$ 自然链同伦。

**证明**：对次数 $n$ 归纳构造自然同伦 $h:F_n\to G_{n+1}$，使其满足 $dh+hd=f-g$。取任意模型 $M_\alpha$ 与 $F_n(M_\alpha)$ 的一个自由生成元 $e$。由归纳假设，$h$ 已在次数 $<n$ 上定义，故 $de$ 已处理好；于是

$$c:=f(e)-g(e)-h(de)\in G_n(M_\alpha)$$

满足 $dc=f(de)-g(de)-h(d\,de)=f(de)-g(de)-d\,h(de)$，结合 $h$ 在低次数上使 $f-g=dh+hd$，得 $dc=0$，即 $c$ 是 $G_n(M_\alpha)$ 中的闭链。若 $n>0$，由 $H_n(G(M_\alpha))=0$ 存在 $y\in G_{n+1}(M_\alpha)$ 使 $dy=c$，定义 $h(e)=y$；若 $n=0$，则 $H_0(f)=H_0(g)$ 意味着 $f(e)-g(e)$ 是 $G_0(M_\alpha)$ 中的边界（在高次同调为零与 $H_0$ 一致下成立），同样可取 $h(e)$。由于 $F$ 自由，把 $h$ 在每个生成元上的取值用 $R$-线性与自然性延拓，即得全局定义的自然同伦。

**步骤 7：$EZ\circ AW\simeq\mathrm{id}$。**

取 $\mathcal{C}$ 为空间对的范畴（对象是空间偶，含两个变元 $X,Y$ 的乘积则由二元函子处理，或固定 $Y$ 视 $X$ 为变元，结论对每个变元自然），$F(X,Y)=C_*(X\times Y)$，$G(X,Y)=C_*(X\times Y)$，$f=EZ\circ AW$，$g=\mathrm{id}$，模型取 $\{(\Delta^m,\Delta^k)\}$。两个函子都自然、自由。需验证 $H_0(EZ\circ AW)=H_0(\mathrm{id})$：次数 $0$ 时 $\sigma$ 是点 $(\xi,\eta)$，$AW(\sigma)=[\xi]\otimes[\eta]$，$EZ([\xi]\otimes[\eta])=(\xi,\eta)$ 对应的常单形，即 $\sigma$ 本身，故在 $H_0$ 上相同。由步骤 6 的 acyclic models 定理（模型 $\Delta^m\times\Delta^k$ 是可缩的，故 $C_*(\Delta^m\times\Delta^k)$ 在正次数无同调），得自然链同伦 $EZ\circ AW\simeq\mathrm{id}$。

**步骤 8：推论（同调/Künneth）。**

$EZ$ 是链同伦等价，故诱导同调同构 $H_n(X\times Y;R)\cong H_n(C_*(X)\otimes_R C_*(Y))$。当 $H_*(X;R)$ 为自由（或 $H_*(Y;R)$ 为自由、或 $R$ 为域）时，Künneth 短正合列退化，得到
$$H_n(X\times Y;R)\cong\bigoplus_{p+q=n}H_p(X;R)\otimes_R H_q(Y;R).$$
上同调层面经由 $\operatorname{Hom}(-;R)$ 与杯积得到同样的分裂，这正是杯积定义的链层来源。

## 相关条目

- [上同调与杯积结构](./上同调与杯积结构.md)：杯积正是用对角线映射复合 $AW$ 后（转置）在链水平定义的，本定理保证其良定义与乘法结构。
- [Eilenberg-Steenrod公理](./Eilenberg-Steenrod公理.md)：乘积公理（Künneth）是 Eilenberg–Steenrod 同调公理体系的一条，本定理给出其实现。
- [奇异同调群](./奇异同调群.md)：本定理的比较对象正是奇异链复形与张量积复形。

