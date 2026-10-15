# Gronwall 不等式

> **一句话大白话**：若一个非负量最多只是"自身积分的线性放大"再加一个小源头，那它其实已被源头按指数方式控制住了，绝不会无端爆炸。
>
> **小例子**：若 $u(t)\le C+\int_0^t u(s)\,ds$ 且 $u\ge0$，则取 $\beta\equiv1$，立即得 $u(t)\le C e^{t}$。

## 介绍

Gronwall 不等式（Gronwall inequality），也称 Gronwall 引理，是常微分方程与分析中估计解的增长的基本工具，由 Thomas Hakon Grönwall 于 1919 年提出。它刻画了满足"积分不等式"的非负连续函数的增长上界：若一个函数被自身的积分与一个已知项共同控制，则该函数被已知项按指数因子控制住。

Gronwall 不等式最重要的用途是证明微分方程解的唯一性以及解对初值、参数的连续依赖性。在 Picard-Lindelöf 定理中，正是它把逐次逼近序列相邻两项之差的估计整理成一个可求和的控制量，从而保证收敛；在稳定性分析、能量估计与数值方法的收敛阶证明中，它同样反复出现。

从方法论看，Gronwall 不等式是"先验估计"的典型范例：不需要知道解的显式表达式，只要能写出关于解的积分不等式，就能推出定量上界。

## 分析

**前置依赖**：一阶线性微分方程通解公式、常数变易法（积分因子法）、微积分基本定理、解对初值的连续依赖性

**定理内容（积分形式）**：设 $u,\alpha,\beta$ 是区间 $[a,b]$ 上的实值连续函数，且 $\beta\ge0$、$u\ge0$。若对一切 $t\in[a,b]$ 有

$$u(t)\le\alpha(t)+\int_a^t\beta(s)u(s)\,ds,$$

则对一切 $t\in[a,b]$，

$$u(t)\le\alpha(t)+\int_a^t\alpha(s)\beta(s)\exp\!\Big(\int_s^t\beta(r)\,dr\Big)ds.$$

**常用特例（常数源）**：若 $\alpha\equiv C\ge0$ 为常数，则

$$u(t)\le C\exp\!\Big(\int_a^t\beta(s)\,ds\Big).$$

**关键要点**：

- 条件 $\beta\ge0$ 是本质的，它保证积分因子单调、指数因子指向增长而非衰减；
- 结论只用到积分不等式本身，无需 $u$ 的显式表达式，因此对未知解极为有用；
- 当 $\alpha\equiv0$ 时结论退化为 $u\equiv0$，这正是证明唯一性的关键形态。

## 思考过程

证明的核心想法是把"含未知函数 $u$ 的积分项"整体看作一个新的未知函数

$$v(t)=\int_a^t\beta(s)u(s)\,ds,$$

从而把积分不等式转化为关于 $v$ 的微分不等式。这样做的理由有三：其一，$v$ 作为变上限积分可微，且 $v(a)=0$；其二，$v'(t)=\beta(t)u(t)$ 把 $u$ 与 $v'$ 联系起来；其三，$u\le\alpha+v$ 使我们可以用 $v$ 控制 $u$。

于是 $v'=\beta u\le\beta\alpha+\beta v$，即 $v'-\beta v\le\beta\alpha$。这正是"一阶线性微分不等式"，用常数变易法：乘以积分因子 $e^{-\int_a^t\beta}$ 后左端成为全导数，两边从 $a$ 到 $t$ 积分即可。最后用 $u\le\alpha+v$ 还原。

## 证明过程

**步骤 1：引入 $v$ 并写出微分不等式。** 令

$$v(t)=\int_a^t\beta(s)u(s)\,ds.$$

由微积分基本定理，$v$ 在 $[a,b]$ 上可微，$v(a)=0$，且 $\beta\ge0$、$u\ge0$ 使 $v\ge0$。由假设 $u(t)\le\alpha(t)+v(t)$，求导得

$$v'(t)=\beta(t)u(t)\le\beta(t)\big(\alpha(t)+v(t)\big),$$

即

$$v'(t)-\beta(t)v(t)\le\beta(t)\alpha(t).$$

**步骤 2：乘积分因子。** 令 $A(t)=\exp\!\big(-\int_a^t\beta(r)\,dr\big)>0$，则 $A'(t)=-\beta(t)A(t)$。用 $A(t)$ 乘步骤 1 的不等式，左端恰为全导数：

$$\frac{d}{dt}\big[A(t)v(t)\big]=A(t)\big(v'(t)-\beta(t)v(t)\big)\le A(t)\beta(t)\alpha(t).$$

**步骤 3：积分。** 对 $s$ 从 $a$ 到 $t$ 积分，注意 $A(a)=1$、$v(a)=0$，得

$$A(t)v(t)\le\int_a^t A(s)\beta(s)\alpha(s)\,ds.$$

两端除以 $A(t)>0$，并注意 $\frac{A(s)}{A(t)}=\exp\!\big(\int_s^t\beta(r)\,dr\big)$，得

$$v(t)\le\int_a^t \alpha(s)\beta(s)\exp\!\Big(\int_s^t\beta(r)\,dr\Big)ds.$$

**步骤 4：还原 $u$ 的界。** 由 $u(t)\le\alpha(t)+v(t)$，代入步骤 3 得

$$u(t)\le\alpha(t)+\int_a^t\alpha(s)\beta(s)\exp\!\Big(\int_s^t\beta(r)\,dr\Big)ds.$$

当 $\alpha\equiv C$ 为常数时，由于 $\frac{d}{ds}e^{\int_s^t\beta(r)dr}=-\beta(s)e^{\int_s^t\beta(r)dr}$，

$$\int_a^t C\beta(s)e^{\int_s^t\beta(r)dr}ds=C\Big(e^{\int_a^t\beta(r)dr}-1\Big),$$

故 $u(t)\le C e^{\int_a^t\beta(s)ds}$。$\square$

**应用（解的唯一性）**：设 $y_1,y_2$ 是 $y'=f(t,y)$ 在 $[a,b]$ 上满足同一初值 $y(a)=y_0$ 的两个解，且 $f$ 关于 $y$ 以 $L$ 为 Lipschitz 常数。由 $y_i(t)=y_0+\int_a^t f(s,y_i(s))ds$ 作差得

$$|y_1(t)-y_2(t)|\le\int_a^t L\,|y_1(s)-y_2(s)|\,ds.$$

取 $\alpha\equiv0$、$\beta\equiv L$，由 Gronwall 不等式得 $|y_1(t)-y_2(t)|\le0$，即 $y_1=y_2$。

## 课堂问答

**老师**：设 $u\ge 0$ 连续，满足 $u(t)\le\alpha(t)+\int_a^t\beta(s)u(s)\,ds$，$\beta\ge0$。若取 $\alpha\equiv0$，你能立刻断定什么？

**学生**：结论是 $u\equiv0$，这正是唯一性的关键形态。理由是把 $v(t)=\int_a^t\beta u$ 分离出来，由 $u\le v$ 得 $v'\le\beta v$，再用积分因子 $e^{-\int\beta}$ 积分得 $v\le 0$；又 $v\ge0$，所以 $v\equiv0$，从而 $u\equiv0$。常见误区是此时仍写 $u\le Ce^{\int\beta}$——那只能给出 $u\le0$，本质是"零源不能被放大"。

**老师（追问）**：为什么条件 $\beta\ge0$ 不能去掉？若 $\beta$ 变号，积分因子还单调吗？

**学生**：不能去。$\beta<0$ 时 $e^{\int\beta}$ 变成衰减因子，$v(t)\ge0$ 不再被约束，结论会失效。证明里用 $\frac{A(s)}{A(t)}=\exp\!\big(\int_s^t\beta\big)$，只有当 $\beta\ge0$、$s\le t$ 时它才 $\ge1$，才给出"增长型"控制。这正是它能与解对初值连续依赖无缝配合的原因。

**老师（拓展）**：回到一般形式，源项 $\alpha$ 不是常数时，上界长什么样？这对依赖初值的估计有什么用？

**学生**：一般上界是
$$u(t)\le\alpha(t)+\int_a^t\alpha(s)\beta(s)\exp\!\Big(\int_s^t\beta(r)\,dr\Big)ds.$$
当 $\alpha\equiv C$ 时化为 $u(t)\le Ce^{\int_a^t\beta}$。在解对初值连续依赖里取 $\beta\equiv L$，就得到 $|y-\bar y|\le A e^{L(x-x_0)}$，把"初值的小扰动"变成"全区间的一致小偏差"。

## 相关条目

- [解对初值的连续依赖性](./解对初值的连续依赖性.md)：用 Gronwall 不等式估计不同初值对应解之间的偏差。
- [Picard-Lindelöf定理](./Picard-Lindelöf定理.md)：逐次逼近的收敛与解的唯一性证明都依赖本不等式。
