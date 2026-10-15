# 分次Leibniz 法则

> **一句话大白话**：在"带次数"的代数里，奇次元素交换位置时要变号；因此求导算子作用到乘积上不再是简单分配，而是要多带一个符号 $(-1)^{\text{算子次数}\,\times\,\text{被越过元素的次数}}$——这就是分次 Leibniz 法则。
>
> **小例子**：外微分 $d$ 作用在 $p$-形式 $\alpha$ 与任意形式 $\beta$ 的楔积上：$d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^{p}\alpha\wedge d\beta$。那个 $(-1)^{p}$ 正是"把奇次的 $d$ 移过次数为 $p$ 的 $\alpha$"所付出的代价。

## 介绍

分次 Leibniz 法则（graded Leibniz rule），又称带符号的 Leibniz 法则，是分次代数上"导子"这一概念的定义性公式，是把普通微积分中 $(fg)'=f'g+fg'$ 推广到带次数的代数结构的结果。设 $A=\bigoplus_{n\ge0}A^n$ 是分次代数，其乘法满足分次交换律：对 $\alpha\in A^p$、$\beta\in A^q$ 有 $\alpha\beta=(-1)^{pq}\beta\alpha$。若线性算子 $D:A\to A$ 满足 $D(A^n)\subseteq A^{n+k}$，且对一切齐次元素成立

$$
D(\alpha\beta)=D(\alpha)\,\beta+(-1)^{k|\alpha|}\,\alpha\,D(\beta),
$$

则称 $D$ 是次数为 $k$ 的**分次导子**（graded derivation）。这个额外的符号因子完全源于"越过一个奇次元素要变号"的分次交换律，它绝非装饰。

在微分几何与数学物理中，它是几乎所有"求导与乘法相容"命题的统一形式：外微分 $d$ 是次数 $1$ 的分次导子，向量丛上的协变外微分 $d^\nabla$ 也是；分次交换子 $[D,E]$ 仍为分次导子，故 $d^2=0$ 可以表述为 $[d,d]=0$；Bianchi 恒等式、Chern–Weil 同态、超对称变换、BRST 量子化的全部代数骨架，都是这条符号规则的直接后果。

## 分析

**前置依赖**：楔积的结合律、张量积的泛性质、行列式的Leibniz公式、协变外微分与Bianchi恒等式、Stokes定理流形形式。

**定理内容**：设 $\Omega^\bullet(M)=\bigoplus_{p}\Omega^p(M)$ 是流形上的微分形式代数，$\wedge$ 是楔积，满足分次交换律

$$
\alpha\wedge\beta=(-1)^{pq}\,\beta\wedge\alpha,\qquad \alpha\in\Omega^p,\ \beta\in\Omega^q .
$$

则外微分 $d$ 是次数 $+1$ 的分次导子：对 $\alpha\in\Omega^p$ 与任意齐次 $\beta\in\Omega^q$ 成立

$$
d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^{p}\,\alpha\wedge d\beta .
$$

**推论**：（1）若 $D,E$ 分别是次数 $k,l$ 的分次导子，则分次交换子 $[D,E]_{\mathrm{gr}}=DE-(-1)^{kl}ED$ 是次数 $k+l$ 的分次导子；（2）$d^2=0$，因为 $[d,d]_{\mathrm{gr}}=2d^2$ 是次数 $2$ 的分次导子且在生成元上为零；（3）$(\Omega^\bullet(M),d,\wedge)$ 构成微分分次代数（DGA）。

**依赖的概念**：分次代数与齐次元素、分次交换律、导子与分次导子、楔积、外微分、微分分次代数。

## 思考过程

证明策略是"先对单项式验证，再用线性性推广"。由于 $\Omega^\bullet(M)$ 由形如 $dx^I=dx^{i_1}\wedge\cdots\wedge dx^{i_p}$ 的基元张成，而 $\wedge$ 与 $d$ 都是 $\mathbb R$-线性的，只需验证 $\omega=f\,dx^I$、$\eta=g\,dx^J$ 这一形状的乘积。

验证中只有两个要点。第一，$0$-形式满足普通 Leibniz 法则 $d(fg)=df\cdot g+f\cdot dg$，这是第二阶混合偏导对称（即 $d^2=0$ 在函数上）与 Leibniz 法则的直接推论。第二，把 $d$ 从 $\omega$ 一侧"移"到 $\eta$ 一侧时，$d$ 是奇次算子、$dx^I$ 是次数 $p$ 的偶/奇对象，交换一次就要产生 $(-1)^{p}$；这一步正是分次交换律给出的。两处合并，符号规则立刻出现，无需任何坐标计算之外的工具。

得到单项式情形后，一般情形由双线性性与分次交换律自动成立。至于 $d^2=0$ 与分次交换子，则利用"分次导子由它在代数生成元上的取值唯一决定"这一事实归约即可。

## 证明过程

**步骤 1：分次交换律与"移过一个因子"的规则。**

由定义，对 $\alpha\in\Omega^p$、$\beta\in\Omega^q$ 有 $\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha$。特别地，一个 $1$-形式 $\theta$ 越过一个 $p$-形式 $\alpha$ 时满足

$$
\alpha\wedge\theta=(-1)^{p}\,\theta\wedge\alpha .
$$

这一步是后面所有符号的唯一来源。

**步骤 2：函数上的 Leibniz 法则。**

对光滑函数 $f,g$，由 $d$ 在坐标下为 $d=\sum_i\frac{\partial}{\partial x^i}dx^i$ 得

$$
d(fg)=\sum_i\frac{\partial(fg)}{\partial x^i}dx^i=\sum_i\Big(\frac{\partial f}{\partial x^i}g+f\frac{\partial g}{\partial x^i}\Big)dx^i=df\cdot g+f\cdot dg .
$$

**步骤 3：单项式验证。**

取 $\omega=f\,dx^I$（$|I|=p$）与 $\eta=g\,dx^J$，则 $\omega\wedge\eta=fg\,dx^I\wedge dx^J$。由步骤 2 与 $d(dx^I)=0$，

$$
d(\omega\wedge\eta)=d(fg)\wedge dx^I\wedge dx^J=(g\,df+f\,dg)\wedge dx^I\wedge dx^J .
$$

另一方面，

$$
d\omega\wedge\eta=(df\wedge dx^I)\wedge(g\,dx^J)=g\,df\wedge dx^I\wedge dx^J,
$$

而用步骤 1 把 $dg$ 移过 $dx^I$ 得

$$
\omega\wedge d\eta=f\,dx^I\wedge(dg\wedge dx^J)=(-1)^{p}f\,dg\wedge dx^I\wedge dx^J .
$$

于是

$$
d\omega\wedge\eta+(-1)^{p}\omega\wedge d\eta
=\big(g\,df+f\,dg\big)\wedge dx^I\wedge dx^J=d(\omega\wedge\eta),
$$

即单项式情形成立。

一般 $\alpha,\beta$ 是单项式的实线性组合，而 $\wedge$ 与 $d$ 都是 $\mathbb R$-线性的，故对分量线性叠加即得

$$
d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^{p}\alpha\wedge d\beta .
$$

**步骤 4：分次交换子与 $d^2=0$。** 设 $D,E$ 是次数为 $k,l$ 的分次导子，代入定义可验证 $[D,E]_{\mathrm{gr}}=DE-(-1)^{kl}ED$ 仍是分次导子（交叉项两两相消）；取 $D=E=d$ 得 $[d,d]_{\mathrm{gr}}=2d^2$，它是次数 $2$ 的分次导子。
$\Omega^\bullet(M)$ 作为分次代数由 $\Omega^0(M)$ 与 $\Omega^1(M)$ 生成（每个 $dx^I$ 是 $1$-形式的楔积）。次数 $2$ 的分次导子由它在生成元上的值唯一确定。在函数上 $d^2f=\sum_{i,j}\frac{\partial^2 f}{\partial x^j\partial x^i}dx^j\wedge dx^i=0$，这里用了混合偏导对称与 $dx^j\wedge dx^i=-dx^i\wedge dx^j$；在 $1$-形式 $df$ 上同样有 $d^2(df)=0$。故 $2d^2=0$ 在生成元上成立，从而 $d^2=0$ 处处成立，$(\Omega^\bullet(M),d,\wedge)$ 是微分分次代数。

**步骤 5：对协变外微分与 Bianchi 恒等式的应用。**

把 $\Omega^\bullet(M)$ 换成取值于向量丛 $E$ 的形式 $\Omega^\bullet(M;E)$，$d$ 换成 $d^\nabla=d+A\wedge$。完全相同的计算给出 $d^\nabla$ 也是次数 $1$ 的分次导子：$d^\nabla(\alpha\wedge\xi)=d\alpha\wedge\xi+(-1)^{p}\alpha\wedge d^\nabla\xi$（$\alpha\in\Omega^p$、$\xi\in\Omega^\bullet(M;E)$）。而曲率算子 $\Omega\wedge\cdot=d^\nabla d^\nabla$ 是偶次（次数 $2$）算子，它是无符号的分次导子。于是对 $d^\nabla d^\nabla d^\nabla\xi$ 作两种展开即得

$$
(d^\nabla\Omega)\wedge\xi=0\quad\Longrightarrow\quad d^\nabla\Omega=0,
$$

这正是第二 Bianchi 恒等式。可见 Bianchi 恒等式不过是分次 Leibniz 法则（外加 $d^\nabla d^\nabla=\Omega\wedge\cdot$）三行推导的产物。$\square$

## 课堂问答

**老师**：$d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^p\alpha\wedge d\beta$ 里那个 $(-1)^p$ 到底从哪来？

**学生**：结论：来自把奇次算子 $d$ 移过 $p$-形式 $\alpha$ 时的一次换序。理由：只需验证单项式 $\omega=f\,dx^I$、$\eta=g\,dx^J$，用 $d(fg)=df\,g+f\,dg$ 与 $\alpha\wedge\theta=(-1)^p\theta\wedge\alpha$，得两边的 $d\beta$ 项相差 $(-1)^p$。常见误区：把符号当装饰丢掉。

**老师（追问）**：$d^2=0$ 怎么用这套语言看出？

**学生**：因为 $[d,d]_{\mathrm{gr}}=2d^2$ 是次数 $2$ 的分次导子，而分次导子由它在生成元上的值唯一决定；在函数上 $d^2f=\sum_{i,j}\partial_j\partial_i f\,dx^j\wedge dx^i=0$，用了混合偏导对称与 $dx^j\wedge dx^i=-dx^i\wedge dx^j$。

**老师（拓展）**：Bianchi 恒等式与它的关系？

**学生**：把 $d$ 换成 $d^\nabla=d+A\wedge$ 后仍满足分次 Leibniz 法则，而曲率算子 $\Omega\wedge\cdot=d^\nabla d^\nabla$ 是偶次算子；对 $d^\nabla d^\nabla d^\nabla\xi$ 作两种展开即 $(d^\nabla\Omega)\wedge\xi=0$，即第二 Bianchi 恒等式。

## 相关条目

- [协变外微分与Bianchi恒等式](./协变外微分与Bianchi恒等式.md)：其全部符号技巧都建立在分次 Leibniz 法则之上。
- [楔积的结合律](../第15级-多重线性代数/楔积的结合律.md)：保证 $\wedge$ 的结合性，使分次代数的定义良定。
- [行列式的Leibniz公式](../第15级-多重线性代数/行列式的Leibniz公式.md)：另一处"带符号的求和"结构，与分次交换律同源。
- [Stokes定理流形形式](../第33级-微分几何/Stokes定理流形形式.md)：与外微分 $d$ 的公理化刻画并列，共同确定 DGA 结构。
