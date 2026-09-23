# Fekete引理

> **一句话大白话**：若一个数列满足"分成两段再相加不会变小"（次可加），那么它除以 $n$ 之后一定收敛，且极限正好是所有 $a_n/n$ 中最小的那一个。
>
> **小例子**：由范数的次乘性 $\|T^{m+n}\|\le\|T^m\|\|T^n\|$ 取对数得 $a_n=\log\|T^n\|$ 是次可加序列，于是 $\frac1n\log\|T^n\|$（即 $\log\|T^n\|^{1/n}$）收敛——这正是谱半径公式中"极限存在且等于下确界"那一半的根据。

## 一、定理介绍

> **前置依赖**：实数系的下确界与完备性、上极限与下极限 $\limsup,\liminf$ 的夹逼性质、带余除法（$n=qm+r$，$0\le r<m$）、有限数集的最大值与最小值、对数与指数函数的单调性。

Fekete 引理（Fekete's subadditive lemma）由匈牙利数学家 Mihály Fekete 于 1923 年在研究代数方程根分布的工作中提出，其内容是：次可加序列的平均值必然收敛。它是数学分析中最简单却又最有用的"极限存在性"工具之一。在许多问题中，困难并不在于求极限的值，而在于先证明极限存在；Fekete 引理恰好把"极限存在"这件事化归为一条极易验证的不等式 $a_{m+n}\le a_m+a_n$，并同时给出极限等于下确界这一强结论。

引理的证明关键只有一步：把任意指标 $n$ 拆成 $q$ 个固定指标 $m$ 与一个余数 $r$，由次可加性反复展开即得 $a_n\le q a_m+a_r$。除以 $n$ 后，$q/n\to1/m$ 而余数项 $a_r/n\to0$，于是立刻得到 $\limsup_n a_n/n\le a_m/m$；再对 $m$ 取下确界即得结论。这一"先估计上极限、再优化参照项"的模式在分析中极为常见。

## 二、原理思路

证明由四步构成。

1. **固定参照项**：取定 $m\ge1$，用带余除法写作 $n=qm+r$，$0\le r<m$，由次可加性反复展开得 $a_n\le q\,a_m+a_r$。

2. **除以 $n$ 取上极限**：除以 $n$ 后 $q/n\to1/m$，而余数只取有限多个值使 $a_r/n\to0$，于是对每个 $m$ 都有 $\limsup_n a_n/n\le a_m/m$。

3. **对 $m$ 取下确界**：上式对一切 $m$ 成立，故 $\limsup_n a_n/n\le\inf_m a_m/m$。

4. **夹逼**：由下确界的定义又有 $\inf_m a_m/m\le\liminf_n a_n/n$，于是上极限不大于下极限，二者相等，极限存在。

此外，若序列有下界 $a_n\ge-C$，则 $a_n/n\ge-C/n\ge-C$，下确界不会取到 $-\infty$，极限为有限实数。

## 三、定理的严格表述

**（Fekete 次可加引理）** 设实数列 $\{a_n\}_{n\ge1}$ 满足次可加性
$$a_{m+n}\le a_m+a_n,\qquad \forall\,m,n\ge1.$$
则平均值序列 $\left\{\dfrac{a_n}{n}\right\}_{n\ge1}$ 收敛（在扩充实数系 $\overline{\mathbb R}$ 中），且
$$\lim_{n\to\infty}\frac{a_n}{n}=\inf_{n\ge1}\frac{a_n}{n}.$$

**有限性补充**：若还存在常数 $C>0$ 使 $a_n\ge-C$ 对一切 $n\ge1$ 成立，则上述极限是有限实数，且下确界在 $\mathbb R$ 中取到。

**对偶形式（超可加）**：若 $a_{m+n}\ge a_m+a_n$ 对一切 $m,n\ge1$ 成立，则
$$\lim_{n\to\infty}\frac{a_n}{n}=\sup_{n\ge1}\frac{a_n}{n}.$$

**乘积形式（次可乘）**：若 $b_n>0$ 且 $b_{m+n}\le b_mb_n$，则数列 $\left\{b_n^{1/n}\right\}$ 收敛且
$$\lim_{n\to\infty}b_n^{1/n}=\inf_{n\ge1}b_n^{1/n}.$$

## 四、证明过程

以下约定 $a_0=0$，这既与记号相符，也不影响任何估计。

**步骤 1：先给出下界。**

令
$$L=\inf_{n\ge1}\frac{a_n}{n}\in[-\infty,+\infty).$$
由下确界的定义，$L\le a_n/n$ 对一切 $n\ge1$ 成立。对 $n\to\infty$ 取下极限保序，得
$$L\le\liminf_{n\to\infty}\frac{a_n}{n}.$$
当 $L=-\infty$ 时此式平凡成立。

**步骤 2：固定 $m$ 并对 $a_n$ 拆项。**

取定 $m\ge1$。对任意 $n\ge1$ 作带余除法
$$n=qm+r,\qquad q=\left\lfloor\frac{n}{m}\right\rfloor,\qquad 0\le r<m.$$
当 $r=0$ 时，反复使用次可加性 $q-1$ 次得
$$a_n=a_{qm}\le q\,a_m.$$
当 $r\ge1$ 时，先用一次次可加性再用上面的估计，
$$a_n=a_{qm+r}\le a_{qm}+a_r\le q\,a_m+a_r.$$
两种情形合并为
$$a_n\le q\,a_m+a_r,\qquad 0\le r<m.$$

**步骤 3：除以 $n$ 并取上极限。**

由步骤 2，两边除以 $n>0$ 得
$$\frac{a_n}{n}\le \frac{q}{n}\,a_m+\frac{a_r}{n}.$$
由 $q=(n-r)/m$ 得
$$\frac{q}{n}=\frac{1}{m}-\frac{r}{mn}\longrightarrow\frac{1}{m}\qquad(n\to\infty).$$
又 $r$ 只取有限多个值 $0,1,\dots,m-1$，而 $a_0,a_1,\dots,a_{m-1}$ 是有限个实数，故
$$\left|\frac{a_r}{n}\right|\le\frac{\max_{0\le r<m}|a_r|}{n}\longrightarrow0\qquad(n\to\infty).$$
于是
$$\limsup_{n\to\infty}\frac{a_n}{n}\le \frac{a_m}{m}.$$

**步骤 4：对 $m$ 取下确界。**

步骤 3 的不等式对每个 $m\ge1$ 都成立，而对右端取下确界不改变不等式方向，故
$$\limsup_{n\to\infty}\frac{a_n}{n}\le\inf_{m\ge1}\frac{a_m}{m}=L.$$

**步骤 5：夹逼，得极限存在。**

综合步骤 1 与步骤 4，
$$L\le\liminf_{n\to\infty}\frac{a_n}{n}\le\limsup_{n\to\infty}\frac{a_n}{n}\le L.$$
四者相等，故 $\left\{a_n/n\right\}$ 收敛且
$$\lim_{n\to\infty}\frac{a_n}{n}=L=\inf_{n\ge1}\frac{a_n}{n}.\qquad\square$$

**步骤 6：有下界时极限有限。**

设 $a_n\ge-C$ 对一切 $n\ge1$ 成立。则
$$\frac{a_n}{n}\ge-\frac{C}{n}\ge-C\qquad(\forall n\ge1),$$
故 $L=\inf_n a_n/n\ge-C>-\infty$，由步骤 5 极限为有限实数 $L\in[-C,+\infty)$。（更精细地，$a_n/n\ge-C/n\to0$ 还给出 $L\ge0$，但这并不必要。）

**步骤 7：两个变形形式的证明。**

*（i）超可加情形。* 令 $c_n=-a_n$。由 $a_{m+n}\ge a_m+a_n$ 得
$$c_{m+n}=-a_{m+n}\le-a_m-a_n=c_m+c_n,$$
即 $\{c_n\}$ 次可加。对 $\{c_n\}$ 用本引理得 $\lim c_n/n=\inf_n c_n/n$，等价地
$$\lim_{n\to\infty}\frac{a_n}{n}=-\inf_{n}\left(-\frac{a_n}{n}\right)=\sup_{n\ge1}\frac{a_n}{n}.$$

*（ii）次可乘情形。* 令 $a_n=\log b_n$（良定义，因 $b_n>0$）。由 $b_{m+n}\le b_mb_n$ 及对数单调性得
$$a_{m+n}=\log b_{m+n}\le\log(b_mb_n)=a_m+a_n,$$
故 $\{a_n\}$ 次可加。由步骤 5，
$$\lim_{n\to\infty}\frac{1}{n}\log b_n=\inf_{n\ge1}\frac{1}{n}\log b_n.$$
两边取指数（指数函数连续且单调）得
$$\lim_{n\to\infty}b_n^{1/n}=\inf_{n\ge1}b_n^{1/n}.\qquad\square$$

**注（$L=-\infty$ 的情形）**：若 $\{a_n\}$ 无下界，则可能 $L=-\infty$，此时步骤 5 给出 $\limsup a_n/n=-\infty$，即 $a_n/n\to-\infty$，结论仍成立，只是极限为 $-\infty$。

## 五、应用与意义

**理论意义**：

1. **极限存在性的通用工具**：凡遇到"某个量的增长速度"问题，只要验证次可加（或次可乘）不等式，就能立刻得到平均值的收敛性，无需任何光滑性或单调性假设。

2. **谱理论与算子代数**：对 Banach 代数中的元素 $T$，$a_n=\log\|T^n\|$ 次可加，Fekete 引理给出 $\lim\|T^n\|^{1/n}=\inf\|T^n\|^{1/n}$ 的存在性，这是 Gelfand 谱半径公式 $r(T)=\lim\|T^n\|^{1/n}$ 的两大支柱之一（另一支柱为多项式谱映射给出的下界估计）。

3. **熵与维数的定义**：拓扑熵 $h(f)=\lim\frac1n\log N(f^n)$、Hausdorff 维数的计盒公式、以及 Shannon–McMillan–Breiman 定理中 $\frac1n\log$ 型极限的存在性，都以 Fekete 引理为出发点，保证定义中的极限确实存在。

**应用领域**：

1. **数值线性代数与迭代法**：迭代矩阵 $T$ 的收敛判据 $r(T)<1$ 依赖 $\|T^n\|^{1/n}$ 的极限存在，从而可用任一项 $\|T^n\|^{1/n}$ 作上界估计。

2. **组合与计数**：次可乘的计数序列（如长度为 $n$ 的禁词数、图的同态计数）给出指数增长率的存在性；Fekete 引理也是 de Bruijn–Erdős 定理等组合结论的常用引理。

3. **概率论中的次可加遍历定理**：Kingman 的次可加遍历定理把 Fekete 引理推广到随机情形，断言次可加平稳过程的平均几乎必然收敛，是遍历理论与随机矩阵乘积（Lyapunov 指数）的基石。

4. **动力系统与几何**：周期轨计数、测地线长度的增长、体积熵等量的指数增长率均可由 Fekete 引理严格定义。

**推广**：次可加（次可乘）条件可以减弱为"最终次可加"或"渐近次可加"，结论不变；在非交换情形需改用算子代数中的相应版本。

## 相关条目

- [谱半径公式](./谱半径公式.md)：其证明中"极限存在"与"极限等于下确界"两步正是 Fekete 引理对 $\log\|T^n\|$ 的直接应用。
- [谱映射定理](./谱映射定理.md)：与 Fekete 引理同为谱半径公式证明的两个关键输入，分别给出上界与下界。
- [Gelfand-Mazur定理](./Gelfand-Mazur定理.md)：依赖谱半径公式与谱的非空性，从而间接用到本引理。
