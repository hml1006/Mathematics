# Fréchet–Kolmogorov 紧性准则

> **一句话大白话**：一族 $L^p$ 函数能在 $L^p$ 中抽出收敛子列，当且仅当三件事同时成立——它们一致有界、平移一点点时一致地不变（"等度连续"），而且质量一致地不跑到无穷远（"一致胎紧"）。
>
> **小例子**：取 $u_m(x)=\varphi(x-m)$（$\varphi\in C_c^\infty$ 固定非零），则 $\|u_m\|_p$ 一致有界、平移连续性也一致成立，但质量跑向无穷远，故任何子列都不在 $L^p(\mathbb R)$ 中收敛；反之若把 $\varphi$ 换成紧支函数列的"分块平移"，只要支集落在一个固定的大球内，就必有收敛子列。

## 介绍

在有限维空间里，"有界闭集紧"（Bolzano–Weierstrass）是紧性论证的全部；但在 $L^p(\Omega)$ 这样的无穷维空间中，有界远不足以保证紧性。Fréchet–Kolmogorov 紧性准则（也称 Kolmogorov–Riesz(–Sudakov) 定理）给出了 $L^p$ 中**相对紧**的等价的、可以逐条验证的判据：一致有界 + 平移的等度连续性 + 质量的一致集中。

这条准则的本质是"用有限维逼近无穷维"：平移连续性使得可以用卷积（磨光）把函数变成光滑的，光滑性带来等度连续性，从而在某个足够大的紧子集上可以调用 Arzelà–Ascoli 定理得到有限网；而一致胎紧保证了被丢掉的那部分质量可以忽略。于是整个族被有限个球覆盖（完全有界），再由 $L^p$ 的完备性（Riesz–Fischer）得到相对紧。

它是分析中所有紧嵌入定理的技术心脏：Rellich–Kondrachov 定理、Aubin–Lions 紧性引理，都是在某个 Sobolev 空间中验证这三条判据。

## 分析

**前置依赖**：$L^p$ 空间及其完备性（Riesz–Fischer 定理）、紧支连续函数在 $L^p$ 中的稠密性、平移算子的强连续性、Hölder 不等式与 Young 卷积不等式、Minkowski不等式、Arzelà–Ascoli 定理、度量空间中"完全有界 + 完备 $\Leftrightarrow$ 相对紧"。

**定理内容**：设 $1\le p<\infty$，$\mathcal{F}\subseteq L^p(\mathbb R^n)$。则 $\mathcal{F}$ 在 $L^p(\mathbb R^n)$ 中相对紧（即任意序列有在 $L^p$ 中强收敛的子列）当且仅当以下三条同时成立：

**(FK1) 一致有界**：$\displaystyle M:=\sup_{u\in\mathcal{F}}\|u\|_{L^p}<\infty$。

**(FK2) 平移的等度连续性**：$\displaystyle\lim_{|h|\to0}\ \sup_{u\in\mathcal{F}}\big\|u(\cdot+h)-u\big\|_{L^p(\mathbb R^n)}=0$，其中 $u(\cdot+h)(x):=u(x+h)$。

**(FK3) 质量的一致集中**：$\displaystyle\lim_{R\to\infty}\ \sup_{u\in\mathcal{F}}\int_{|x|>R}|u(x)|^p\,dx=0$。

若 $\Omega\subset\mathbb R^n$ 是有界区域，则把 (FK3) 换为"质量一致地不堆积在边界"：

$$\lim_{\delta\to0}\ \sup_{u\in\mathcal{F}}\int_{\Omega\cap\{d(x,\partial\Omega)<\delta\}}|u|^p\,dx=0,$$

并把 (FK2) 限制在内部集合上：$\lim_{|h|\to0}\sup_{u\in\mathcal{F}}\|u(\cdot+h)-u\|_{L^p(\Omega_{|h|})}=0$，其中 $\Omega_\epsilon=\{x\in\Omega: d(x,\partial\Omega)>\epsilon\}$，$u$ 在 $\Omega_{|h|}$ 外视为 $0$。

**证明策略**：必要性用"相对紧 $\Rightarrow$ 完全有界"，用有限个紧支连续函数去逼近整个族，再对这几个函数直接验证三条。充分性分三步：先由 (FK2) 证明磨光 $u*\rho_\delta$ 在全族上一致地逼近 $u$；再对固定的 $\delta$ 证明光滑族 $\{u*\rho_\delta\}$ 一致有界、一致 Lipschitz，用 (FK3) 把注意力限制在固定的大球上，由 Arzelà–Ascoli 得到有限 $\epsilon$-网；最后拼起来得到 $\mathcal{F}$ 完全有界，配合 $L^p$ 完备得到相对紧。

## 思考过程

**必要性**为什么只能是这样三条？相对紧意味着完全有界：对每个 $\epsilon$，存在有限多个 $v_1,\dots,v_m$，其 $\epsilon$-球覆盖 $\mathcal{F}$。我们可以把这 $v_i$ 换成紧支光滑函数（稠密性）而不改变本质。于是对任意 $u\in\mathcal{F}$，取最近的 $v_i$，三角不等式把 $\|u(\cdot+h)-u\|_p$ 拆成 $\|u-v_i\|_p+\|v_i(\cdot+h)-v_i\|_p+\|v_i(\cdot+h)-u(\cdot+h)\|_p$，前末两项都小于 $\epsilon$，中间项因为 $v_i$ 一致连续且有紧支集而对小 $|h|$ 一致地小。把 $L^p$ 换成 $\{|x|>R\}$ 上的范数，则中间项在大 $R$ 时消失，这就是 (FK3)。所以三条是紧性的"影子"。

**充分性**的直觉是"先磨光、再离散、后拼接"。磨光的价值在于把"平移连续性"转化为可用的估计：

$$u*\rho_\delta(x)-u(x)=\int \rho_\delta(y)\big(u(x-y)-u(x)\big)\,dy,$$

用 Minkowski 积分不等式（积分取 $L^p$ 范数可以穿过积分号）就得到 $\|u*\rho_\delta-u\|_p\le\sup_{|y|\le\delta}\|u(\cdot-y)-u\|_p$。这条不等式的右端**与 $u$ 无关**，全族一致，正是 (FK2) 的用处。

对固定的 $\delta$，磨光过的函数是光滑的：它们是一致有界的（Young 不等式 / Hölder），其梯度被 $\|u\|_p\|\nabla\rho_\delta\|_q$ 一致控制，因此一致 Lipschitz，等度连续。再加上 (FK3) 使它们在球外的质量一致地小，于是只需在**一个固定的紧集**（大闭球）上工作，Arzelà–Ascoli 立即给出有限 $\epsilon$-网。把三层误差（磨光误差、球外质量、球内逼近误差）加在一起，就得到 $\mathcal{F}$ 的有限网。

最后一步是纯拓扑的：度量空间中"完全有界 + 完备 $\Leftrightarrow$ 相对紧"。$L^p$ 的完备性由 Riesz–Fischer 定理保证。

## 证明过程

记 $\rho\in C_c^\infty(\mathbb R^n)$ 为标准的非负磨光核，$\int\rho=1$，$\operatorname{supp}\rho\subseteq B(0,1)$，并令 $\rho_\delta(x)=\delta^{-n}\rho(x/\delta)$，$q=p/(p-1)$ 为共轭指数。

**第一步：必要性。**

设 $\mathcal{F}$ 相对紧，即 $\overline{\mathcal{F}}$ 紧，等价地 $\mathcal{F}$ 完全有界。

**(FK1)**：紧集在连续函数 $\|\cdot\|_p$ 下像紧，故有界；于是 $\sup_{u\in\mathcal{F}}\|u\|_p<\infty$。

**(FK2)**：给定 $\epsilon>0$。由完全有界性，取 $v_1,\dots,v_m\in L^p$ 使 $\mathcal{F}\subseteq\bigcup_{i}B(v_i,\epsilon/3)$；因 $C_c(\mathbb R^n)$ 在 $L^p$ 中稠密，不妨设每个 $v_i$ 紧支且连续（否则用 $w_i$ 替换并调整半径）。$v_i$ 一致连续且紧支，故存在 $\delta_i>0$ 使 $|h|<\delta_i$ 时 $\|v_i(\cdot+h)-v_i\|_\infty<\epsilon/(3|K_i+1|^{1/p})$，其中 $K_i$ 是含 $\operatorname{supp}v_i$ 及其 $1$-邻域的紧集；于是 $\|v_i(\cdot+h)-v_i\|_p<\epsilon/3$。取 $\delta=\min_i\delta_i$。对任意 $u\in\mathcal{F}$ 取 $i$ 使 $\|u-v_i\|_p<\epsilon/3$，则当 $|h|<\delta$ 时

$$\|u(\cdot+h)-u\|_p\le\|u(\cdot+h)-v_i(\cdot+h)\|_p+\|v_i(\cdot+h)-v_i\|_p+\|v_i-u\|_p<\epsilon .$$

故 $\lim_{|h|\to0}\sup_{u\in\mathcal{F}}\|u(\cdot+h)-u\|_p=0$，即 (FK2)。

**(FK3)**：同法，对 $u\in\mathcal{F}$ 取 $\|u-v_i\|_p<\epsilon/3$，则

$$\|u\|_{L^p(|x|>R)}\le\|u-v_i\|_{L^p(|x|>R)}+\|v_i\|_{L^p(|x|>R)}<\frac{\epsilon}{3}+\frac{\epsilon}{3},$$

只要 $R$ 大于一切 $\operatorname{supp}v_i$ 的半径（有限多个），且右端与 $u$ 无关。故 (FK3) 成立。必要性得证。

**第二步：充分性之磨光逼近。**

对 $u\in L^p(\mathbb R^n)$，由 $u*\rho_\delta(x)-u(x)=\int\rho_\delta(y)\big(u(x-y)-u(x)\big)dy$ 与 Minkowski 积分不等式，

$$\|u*\rho_\delta-u\|_p\le\int \rho_\delta(y)\,\|u(\cdot-y)-u\|_p\,dy\le\sup_{|y|\le\delta}\|u(\cdot-y)-u\|_p ,$$

最后一步用了 $\operatorname{supp}\rho_\delta\subseteq B(0,\delta)$ 与 $\int\rho_\delta=1$。由 (FK2)，给定 $\epsilon>0$ 可取 $\delta>0$ 使

$$\sup_{u\in\mathcal{F}}\|u-u*\rho_\delta\|_p<\epsilon .\tag{1}$$

**第三步：固定 $\delta$ 后，光滑族完全有界。**

固定满足 (1) 的 $\delta$，记 $\mathcal{F}_\delta:=\{u*\rho_\delta: u\in\mathcal{F}\}$。

**一致有界**：由 Young 不等式 $\|u*\rho_\delta\|_p\le\|u\|_p\|\rho_\delta\|_1=\|u\|_p\le M$；并且由 Hölder 不等式，对一切 $x$，

$$|u*\rho_\delta(x)|\le\|u\|_p\|\rho_\delta\|_q\le M\|\rho_\delta\|_q=:C_0 .$$

**一致 Lipschitz**：因 $\nabla(u*\rho_\delta)=u*\nabla\rho_\delta$，同理

$$|\nabla(u*\rho_\delta)(x)|\le\|u\|_p\|\nabla\rho_\delta\|_q\le M\|\nabla\rho_\delta\|_q=:L_\delta ,$$

故每个 $u*\rho_\delta$ 都是 $L_\delta$-Lipschitz 的，等度连续。

**球外一致小**：由 (FK3) 取 $R>0$ 使 $\sup_{u}\|u\|_{L^p(|x|>R)}<\epsilon$。若 $|x|>R+\delta$，则 $u*\rho_\delta(x)$ 只用到 $|y|>R$ 处的 $u$ 值，用概率测度 $\rho_\delta\,dy$ 上的 Minkowski 不等式得

$$\|u*\rho_\delta\|_{L^p(|x|>R+\delta)}\le\|u\|_{L^p(|x|>R)}<\epsilon .\tag{2}$$

**Arzelà–Ascoli**：在紧集 $\overline{B(0,R+\delta)}$ 上，族 $\mathcal{F}_\delta$ 一致有界且等度连续，故存在有限多个 $v_1,\dots,v_m\in C(\overline{B(0,R+\delta)})$ 使

$$\sup_{u\in\mathcal{F}}\ \min_{1\le i\le m}\ \sup_{|x|\le R+\delta}|u*\rho_\delta(x)-v_i(x)|<\frac{\epsilon}{\big|\{x:|x|\le R+\delta\}\big|^{1/p}} .$$

把每个 $v_i$ 在球外延拓为 $0$。于是对任意 $u\in\mathcal{F}$，取相应的 $v_i$，由 (2) 与上式的 $L^p$ 范数估计（在球上用 $\|v\|_p\le|B|^{1/p}\|v\|_\infty$），

$$\|u*\rho_\delta-v_i\|_{L^p(\mathbb R^n)}\le\epsilon+\epsilon+\epsilon=3\epsilon .$$

**第四步：拼接并取极限。**

对任意 $u\in\mathcal{F}$，取第三步中对应的 $v_i$，由 (1) 得

$$\|u-v_i\|_p\le\|u-u*\rho_\delta\|_p+\|u*\rho_\delta-v_i\|_p<4\epsilon .$$

故对每个 $\epsilon>0$，$\mathcal{F}$ 可被有限个半径 $4\epsilon$ 的球覆盖，即 $\mathcal{F}$ 完全有界。由 Riesz–Fischer 定理，$L^p(\mathbb R^n)$ 完备；在完备度量空间中，完全有界等价于相对紧。因此 $\mathcal{F}$ 在 $L^p$ 中相对紧。**充分性得证。** $\square$

**推论（序列形式）**：若 $(u_m)\subseteq L^p(\mathbb R^n)$ 满足 $\|u_m\|_p\le M$、$\sup_m\|u_m(\cdot+h)-u_m\|_p\to0\ (|h|\to0)$ 且 $\sup_m\|u_m\|_{L^p(|x|>R)}\to0\ (R\to\infty)$，则存在子列在 $L^p$ 中强收敛。这是 PDE 中"先验估计 $\Rightarrow$ 取极限"的标准接口。

## 课堂问答

**老师**：判定一族 $L^p(\mathbb{R}^n)$ 函数相对紧，要逐条验证哪几个条件？

**学生**：三条缺一不可——(FK1) 一致有界 $\sup_{u\in\mathcal{F}}\|u\|_{L^p}<\infty$；(FK2) 平移等度连续 $\lim_{|h|\to0}\sup_{u\in\mathcal{F}}\|u(\cdot+h)-u\|_{L^p}=0$；(FK3) 质量一致集中 $\lim_{R\to\infty}\sup_{u\in\mathcal{F}}\int_{|x|>R}|u|^p\,dx=0$。

**老师（追问）**：充分性证明为什么第一步要磨光？

**学生**：磨光把"平移连续性"转成可直接估计的形式：由 $u*\rho_\delta(x)-u(x)=\int\rho_\delta(y)\big(u(x-y)-u(x)\big)\,dy$ 与 Minkowski 积分不等式得 $\|u*\rho_\delta-u\|_p\le\sup_{|y|\le\delta}\|u(\cdot-y)-u\|_p$，右端对全族一致，(FK2) 恰好把它压小。

**老师（拓展）**：磨光之后怎样落到有限 $\epsilon$-网？

**学生**：固定 $\delta$，$\{u*\rho_\delta\}$ 一致有界且 $|\nabla(u*\rho_\delta)|\le M\|\nabla\rho_\delta\|_q$，故一致 Lipschitz、(FK3) 把质量限制在固定大球上，Arzelà–Ascoli 给出有限 $\epsilon$-网；再由"完全有界 + 完备 $\Leftrightarrow$ 相对紧"（$L^p$ 完备由 Riesz–Fischer 保证）收尾。误区是以为"有界 + 平移连续"就够：无界区域上 (FK3) 不能省，像 $u_m(x)=\varphi(x-m)$ 质量跑到无穷远，任何子列都不收敛；必要性则靠紧支连续函数逼近验证三条。

## 相关条目

- [Sobolev嵌入定理](./Sobolev嵌入定理.md)：紧嵌入所需的"平移估计 + 质量集中"正是本准则的三条判据。
- [Rellich-Kondrachov紧嵌入定理](./Rellich-Kondrachov紧嵌入定理.md)：以本准则为核心工具证明 $W^{k,p}$ 到 $L^q$ 的紧嵌入。
- [Aubin-Lions紧性引理](./Aubin-Lions紧性引理.md)：演化方程中把本准则与时间平移估计结合，得到中间空间的强紧性。
