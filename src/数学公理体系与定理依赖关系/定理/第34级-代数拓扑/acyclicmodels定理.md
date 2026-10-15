# Acyclic Models 定理

> **一句话大白话**：想从一个只记录"连通分支"信息（$H_0$）的自然变换出发，造出整个链层次的"翻译器"（自然链映射），只要起点那一侧是被"标准模型"自由生成的、终点那一侧在模型上是无圈的，翻译器就一定存在，而且差一个自然链同伦是唯一的。
>
> **小例子**：奇异链函子 $C_*(X\times Y)$ 与张量积函子 $C_*(X)\otimes C_*(Y)$ 都以标准单形 $\Delta^n$ 为模型，前者在模型上自由、后者在模型上无圈。于是 $H_0$ 上的恒等映射自动提升为 Eilenberg–Zilber 映射，无需手工写出"洗牌"公式。

## 介绍

设 $\mathcal{C}$ 是范畴（典型例子：拓扑空间范畴 $\mathbf{Top}$，或单形范畴 $\Delta$），$F,G:\mathcal{C}\to\mathbf{Ch}_{\ge0}(R\text{-}\mathbf{Mod})$ 是两个取值于非负次数链复形的函子。如果我们已经知道 $F$ 与 $G$ 在 $0$ 维同调 $H_0$ 上"长得一样"（存在自然同构或自然变换），能否把它提升为链层次的自然链映射？一般来说不行：链层次携带的信息远多于 $H_0$，任意自然变换未必能提升。

**Acyclic Models 定理**（无圈模型方法）给出了一个极其实用的充分条件：只要 $F$ 是"在模型上自由生成的"，而 $G$ 是"在模型上无圈的"，提升就存在。它的价值在于把"构造自然链映射"这一全局问题化归为"在每个模型上解一个边界方程"这一局部问题——而模型通常只是几个标准对象（如 $\Delta^n$），计算量极小。

这个方法是 Eilenberg、Mac Lane、Moore 等人发展起来的，是代数拓扑中"自然性"论证的万能工具：Eilenberg–Zilber 定理、Alexander–Whitney 映射、Künneth 定理、奇异同调与胞腔同调的比较映射、以及群上同调中标准分解的存在性，都是它的直接产物。

## 分析

**前置依赖**：链复形与链映射、链同伦、自由模与基、奇异同调群、张量积复形。

**定理内容**：设 $R$ 是交换环，$\mathcal{C}$ 是范畴，$\mathcal{M}$ 是 $\mathcal{C}$ 中一族对象，称为**模型**。设 $F,G:\mathcal{C}\to\mathbf{Ch}_{\ge0}(R\text{-}\mathbf{Mod})$ 是协变函子，即对每个 $X\in\mathcal{C}$ 有链复形 $F(X)=\big(F_q(X),\partial_q\big)$，对每个态射 $f:X\to Y$ 有链映射 $F(f):F(X)\to F(Y)$。

**(a) 在模型上自由**：称 $F$ **在模型上自由**，若存在模型 $M_j\in\mathcal{M}$（$j$ 属于某指标集）与元素 $e_j^q\in F_q(M_j)$，使得对每个 $X\in\mathcal{C}$ 与每个次数 $q\ge0$，集合

$$\big\{\,F(f)(e_j^q)\ \big|\ f:M_j\to X\ \text{遍历}\ \mathcal{C}\ \text{中一切态射}\,\big\}$$

构成自由 $R$-模 $F_q(X)$ 的一组基。

**(b) 在模型上无圈**：称 $G$ **在模型上无圈**，若对每个 $M\in\mathcal{M}$ 与每个 $q>0$ 都有 $H_q(G(M))=0$。

**定理**：若 $F$ 在模型上自由、$G$ 在模型上无圈，则对任一自然变换 $\eta:H_0F\to H_0G$，存在自然链映射 $\Phi:F\to G$ 使得 $H_0\Phi=\eta$；并且这样的 $\Phi$ 在自然链同伦意义下唯一：若 $\Phi,\Psi$ 都满足 $H_0\Phi=H_0\Psi=\eta$，则存在自然链同伦 $s:\Phi\simeq\Psi$。

**证明策略**：对次数归纳。$F$ 的"模型自由性"让我们只需在每个模型生成元 $e_j^q$ 上指定 $\Phi_q$ 的值（其余靠线性性与自然性决定）；$G$ 的"模型无圈性"保证归纳中出现的那个循环 $\Phi_{q-1}(\partial e_j^q)$ 一定是边界，于是能把 $\Phi_q(e_j^q)$ 解出来。唯一性同样归纳，但目标换成一个自然链同伦方程。

## 思考过程

关键观察有三条。

第一，**自由性把问题局部化**。$F_q(X)$ 以 $\{F(f)(e_j^q)\}$ 为基，所以一个自然映射 $\Phi_q:F_q\to G_q$ 一旦在每个 $e_j^q$ 上取值，就被迫唯一确定：必须令 $\Phi_q(F(f)e_j^q)=G(f)\Phi_q(e_j^q)$。反过来，只要而且只要这样的定义与基的表示无关，它自动是自然的。因此我们只需关心"模型生成元"。

第二，**无圈性提供了"解边界方程"的能力**。链映射的要求是在每个生成元上有 $\partial\Phi_q(e_j^q)=\Phi_{q-1}(\partial e_j^q)$。右端必是循环：因为 $\partial\big(\Phi_{q-1}(\partial e_j^q)\big)=\Phi_{q-2}(\partial\partial e_j^q)=0$（低次数的链映射性质已归纳地成立）。在正次数上无圈意味着这个循环是边界，于是可以解出 $\Phi_q(e_j^q)$。

第三，**次数 $0$ 不构成额外障碍**。归纳在 $q=1$ 时需要 $\Phi_0(\partial e_j^1)$ 是 $G_0(M_j)$ 中的边界。由于 $\partial e_j^1$ 本身就是 $F$ 中的边界，它在 $H_0F(M_j)$ 里的类为零，而 $\Phi_0$ 在 $H_0$ 上诱导的正是 $\eta$，故 $\big[\Phi_0(\partial e_j^1)\big]=\eta\big[\partial e_j^1\big]=0$：这个元素确实是边界。换句话说，"$\Phi_0$ 在 $H_0$ 上诱导 $\eta$"与"归纳能够起步"是同一件事的两面。

唯一性方向的做法是把两个提升相减，得到一个在 $H_0$ 上诱导零的自然链映射 $\Theta$，然后逐次构造自然链同伦 $s$ 满足 $\Theta=\partial s+s\partial$。这里再用一次无圈性：每一层要解的元素都是循环。

## 证明过程

**步骤 0：记号与一个基本观察。**

对模型 $M_j$ 与生成元 $e_j^q\in F_q(M_j)$，同一元素 $e_j^q$ 在不同的态射 $f:M_j\to X$ 下给出 $F_q(X)$ 的不同基元。于是任意 $x\in F_q(X)$ 可唯一写成有限和

$$x=\sum_{j,f}c_{j,f}\,F(f)(e_j^q),\qquad c_{j,f}\in R .$$

**基本观察**：若对每个 $j,q$ 选定 $g_j^q\in G_q(M_j)$，并定义 $\Phi_q\big(F(f)(e_j^q)\big):=G(f)(g_j^q)$ 再线性延拓，则 $\Phi_q$ 是良定义的自然同态；若对一切 $u:X\to Y$ 与一切 $j,f$ 还有 $\Phi_q$ 的相容性，则由 $G$ 的函子性立即得到 $\Phi_q\big(F(u)\circ F(f)e_j^q\big)=G(u)\circ\Phi_q\big(F(f)e_j^q\big)$。以下每次构造都沿用这一模式，故只验证良定义与自然性，不再重复细节。

**步骤 1：构造 $\Phi_0$。**

对每个模型 $M_j$ 与 $0$ 次生成元 $e_j^0$，考虑类 $[e_j^0]\in H_0F(M_j)$ 的像

$$\eta_{M_j}\big([e_j^0]\big)\in H_0G(M_j)=G_0(M_j)\big/\partial G_1(M_j),$$

选取代表元 $g_j^0\in G_0(M_j)$，即 $[g_j^0]=\eta_{M_j}[e_j^0]$。按步骤 0 定义 $\Phi_0\big(F(f)e_j^0\big):=G(f)g_j^0$ 并线性延拓，得自然同态 $\Phi_0:F_0\to G_0$。由于 $\partial$ 在 $0$ 次上为零（链复形非负），$\Phi_0$ 平凡地满足 $\partial\Phi_0=\Phi_{-1}\partial=0$。

**步骤 2：$\Phi_0$ 在 $H_0$ 上诱导 $\eta$，并由此得到归纳的起点。**

先验证 $\Phi_0$ 把边界映到边界，从而在 $H_0$ 上有定义：设 $x\in F_1(X)$，把它写成步骤 0 中的有限和 $x=\sum_{j,f}c_{j,f}F(f)e_j^0$（这里用 $0$ 次生成元的基表示 $\partial x$）。则由自然性（步骤 0 的相容性）、$[g_j^0]=\eta_{M_j}[e_j^0]$ 与 $\eta$ 的自然性，

$$\big[\Phi_0(\partial x)\big]=\sum_{j,f}c_{j,f}\,\big[G(f)g_j^0\big]=\sum_{j,f}c_{j,f}\,G(f)\,\eta_{M_j}\big[e_j^0\big]=\eta_{X}\Big[\sum_{j,f}c_{j,f}F(f)e_j^0\Big]=\eta_X\big[\partial x\big].$$

特别地取 $X=M_j$、$x=e_j^1$，并注意 $\partial e_j^1\in\partial F_1(M_j)$ 在 $H_0F(M_j)$ 中的类为零，即得

$$\big[\Phi_0(\partial e_j^1)\big]=\eta_{M_j}\big[\partial e_j^1\big]=0\ \in H_0G(M_j).$$

这正是归纳在 $q=1$ 时所需的"$\Phi_0(\partial e_j^1)$ 是 $G_0(M_j)$ 中的边界"，因为 $H_0G(M_j)=G_0(M_j)/\partial G_1(M_j)$。

**步骤 3：归纳构造 $\Phi_q$（$q\ge1$）。**

设已构造自然同态 $\Phi_0,\dots,\Phi_{q-1}$，满足 $\partial\Phi_r=\Phi_{r-1}\partial$（$1\le r\le q-1$）。对每个模型 $M_j$ 与 $q$ 次生成元 $e_j^q$，令

$$c_j:=\Phi_{q-1}\big(\partial e_j^q\big)\in G_{q-1}(M_j).$$

先说明 $c_j$ 是循环。当 $q\ge2$：由归纳假设与 $\partial\partial=0$，

$$\partial c_j=\partial\Phi_{q-1}\big(\partial e_j^q\big)=\Phi_{q-2}\big(\partial\partial e_j^q\big)=0 .$$

当 $q=1$：$c_j\in G_0(M_j)$，而 $\partial$ 在 $0$ 次上为零，故 $c_j$ 平凡地是循环；并且由步骤 2 已知 $[c_j]=0$。

现在使用无圈性。若 $q\ge2$，则 $c_j$ 是正次数 $q-1$ 中的循环，$H_{q-1}(G(M_j))=0$ 给出 $g_j^q\in G_q(M_j)$ 使

$$\partial g_j^q=c_j=\Phi_{q-1}\big(\partial e_j^q\big).$$

若 $q=1$，则由 $[c_j]=0$ 在 $H_0G(M_j)=G_0(M_j)/\partial G_1(M_j)$ 中，同样存在 $g_j^1\in G_1(M_j)$ 使 $\partial g_j^1=c_j$。

于是按步骤 0 定义 $\Phi_q\big(F(f)e_j^q\big):=G(f)g_j^q$ 并线性延拓，得自然同态 $\Phi_q:F_q\to G_q$。它在生成元上满足链映射方程：

$$\partial\Phi_q\big(F(f)e_j^q\big)=\partial G(f)g_j^q=G(f)\partial g_j^q=G(f)c_j=G(f)\Phi_{q-1}\big(\partial e_j^q\big)=\Phi_{q-1}\partial\big(F(f)e_j^q\big),$$

其中最后一步用了 $\Phi_{q-1}$ 的自然性。两边都是线性的，故 $\partial\Phi_q=\Phi_{q-1}\partial$ 在 $F_q$ 上处处成立。归纳完成，得到自然链映射 $\Phi:F\to G$，且由步骤 2 有 $H_0\Phi=\eta$。**存在性得证。**

**步骤 4：唯一性——构造自然链同伦。**

设 $\Phi,\Psi:F\to G$ 都是自然链映射且 $H_0\Phi=H_0\Psi=\eta$。令 $\Theta:=\Phi-\Psi$，则 $\Theta$ 是自然链映射且在 $H_0$ 上诱导零映射。下面归纳地构造自然同态 $s_q:F_q\to G_{q+1}$（$q\ge0$，并约定 $s_{-1}=0$ 为零映射 $F_{-1}=0\to G_0$），使

$$\Theta_q=\partial_{q+1}s_q+s_{q-1}\partial_q\qquad(q\ge0).$$

**$q=0$。** 对 $0$ 次生成元 $e_j^0$，$\Theta_0(e_j^0)\in G_0(M_j)$ 是循环，且由 $H_0\Theta=0$ 知它在 $H_0G(M_j)=G_0(M_j)/\partial G_1(M_j)$ 中的类为零，故存在 $g_j^1\in G_1(M_j)$ 使 $\partial g_j^1=\Theta_0(e_j^0)$。定义 $s_0\big(F(f)e_j^0\big):=G(f)g_j^1$ 并线性延拓。于是 $s_0$ 自然，且 $\partial s_0=\Theta_0$（左端 $s_{-1}\partial=0$）在生成元上成立，从而处处成立。

**归纳步。** 设 $s_0,\dots,s_{q-1}$ 已构造且 $\Theta_r=\partial s_r+s_{r-1}\partial$ 对 $r\le q-1$ 成立（$q\ge1$）。对 $q$ 次生成元 $e_j^q$，令

$$d_j:=\Theta_q\big(e_j^q\big)-s_{q-1}\big(\partial e_j^q\big)\in G_q(M_j).$$

利用 $\Theta$ 是链映射、归纳假设以及 $\partial\partial=0$：

$$\partial d_j=\partial\Theta_q(e_j^q)-\partial s_{q-1}\big(\partial e_j^q\big)=\Theta_{q-1}\big(\partial e_j^q\big)-\big(\Theta_{q-1}-s_{q-2}\partial\big)\big(\partial e_j^q\big)=s_{q-2}\big(\partial\partial e_j^q\big)=0 .$$

故 $d_j$ 是次数 $q\ge1$ 中的循环，由 $G$ 在模型上无圈，存在 $g_j^{q+1}\in G_{q+1}(M_j)$ 使 $\partial g_j^{q+1}=d_j$。定义 $s_q\big(F(f)e_j^q\big):=G(f)g_j^{q+1}$ 并线性延拓。则 $s_q$ 自然，且

$$\partial s_q\big(F(f)e_j^q\big)=G(f)\partial g_j^{q+1}=G(f)d_j=\Theta_q\big(F(f)e_j^q\big)-s_{q-1}\partial\big(F(f)e_j^q\big),$$

即在生成元上成立，进而处处成立。归纳完成，$\Theta=\partial s+s\partial$ 为自然链同伦。**唯一性得证。** $\square$

**推论（常用形式）**：在定理的假设下，若 $\eta$ 是同构（例如 $H_0F\cong H_0G$），则 $\Phi$ 是链同伦等价。特别地，$F$ 与 $G$ 的自然链同伦型由它们在模型上的 $H_0$ 数据唯一决定。这正是 Eilenberg–Zilber 定理的证法：取 $F=C_*(X)\otimes C_*(Y)$（在模型 $\Delta^n$ 上自由）、$G=C_*(X\times Y)$（在模型上无圈，因为 $\Delta^n$ 与 $\Delta^n\times\Delta^m$ 可缩），则由 $H_0$ 上的恒等映射得到 Eilenberg–Zilber 映射，并自动得到其同伦逆的存在性与唯一性。

## 课堂问答

**老师**：acyclic models 定理的假设与结论？

**学生**：若 $F$ 在模型上自由、$G$ 在模型上无圈，则任一自然变换 $\eta:H_0F\to H_0G$ 可提升为自然链映射 $\Phi:F\to G$ 使 $H_0\Phi=\eta$，且这样的提升在自然链同伦下唯一。

**老师（追问）**：为什么自由与无圈正好配套？

**学生**：自由性把构造局部化到模型生成元 $e_j^q$，只需在这些元素上取值再线性延拓；无圈性保证归纳中出现的循环 $\Phi_{q-1}(\partial e_j^q)$ 是边界，从而能解出 $\Phi_q(e_j^q)$。$q=1$ 时 $\Phi_0(\partial e_j^1)$ 为边界正由 $\eta$ 在 $H_0$ 上诱导给出。

**老师（拓展）**：典型应用与常见误区？

**学生**：用于证明 Eilenberg-Zilber 定理、Künneth 定理、奇异与胞腔同调的比较映射。常见误区是以为任意自然变换都能提升——缺少自由或无圈假设时提升可能不存在，也不唯一。

## 相关条目

- [Alexander-Whitney映射与Eilenberg-Zilber定理](./Alexander-Whitney映射与Eilenberg-Zilber定理.md)：其证明正是本定理的标准应用（模型取标准单形）。
- [奇异同调群](./奇异同调群.md)：本定理的模型自由性直接来自奇异链复形在每个空间上由单形自由生成。
- [胞腔同调](./胞腔同调.md)：奇异链与胞腔链之间的自然比较映射由本定理唯一确定。
