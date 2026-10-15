# Hadamard引理

> **一句话大白话**：一个光滑函数在原点附近总可以写成"常数项加上每个坐标乘一个光滑函数"的形式；Taylor 展开的余项不再只是"余项"，而是被显式写成了光滑因子。

> **小例子**：对 $f(x,y)=e^{x}\sin y$，因 $f(0,0)=0$，引理给出 $f=x g_1+y g_2$，其中 $g_1(x,y)=\int_0^1 e^{tx}\sin(ty)\,\mathrm dt$、$g_2(x,y)=\int_0^1 t\,e^{tx}\cos(ty)\,\mathrm dt$ 都是光滑函数。

## 介绍

Hadamard 引理（Hadamard's lemma）由法国数学家 Jacques Hadamard 提出，是多元微积分中关于"光滑函数可被坐标整除"的基本结论。它的背景是一个很自然的问题：一个在原点取值为零的光滑函数，凭什么可以写成 $f=\sum_i x_i g_i$ 而 $g_i$ 仍然光滑？对多项式这是显然的（逐项提取公因子），对一般光滑函数则需要论证。Hadamard 的观察是：不需要任何收敛性假设，只需沿射线使用一元微积分基本定理。该引理是现代微分学与奇点理论的常用工具：它是 Morse 引理的证明起点，是反函数定理"局部坐标化简"的代数外壳，也是指标理论中把向量场的零点局部化的技术基础。它的多重指标版本还是"函数在一点消没到 $k$ 阶"这一概念的标准刻画。

## 分析

**前置依赖**：多重指标与偏导数、链式法则多变量、微积分基本定理、光滑函数（$C^\infty$）、Taylor 展开。

**定理内容**：设 $U$ 是 $\mathbb R^n$ 中包含原点的开集，$f\in C^\infty(U)$。则存在 $g_1,\dots,g_n\in C^\infty(U)$，使得对一切 $x\in U$，

$$
f(x)=f(0)+\sum_{i=1}^n x_i\,g_i(x),
$$

并且 $g_i(0)=\partial_i f(0)$。特别地，若 $f(0)=0$，则 $f(x)=\sum_{i=1}^n x_i g_i(x)$。

一个显式的取法是

$$
g_i(x)=\int_0^1 \partial_i f(tx)\,\mathrm dt .
$$

**推论**：若 $f$ 在原点处所有阶数小于 $k$ 的偏导数都为零（即 $f$ 在原点消没到 $k$ 阶），则存在 $g_\alpha\in C^\infty(U)$ 使得

$$
f(x)=\sum_{|\alpha|=k} x^\alpha g_\alpha(x).
$$

## 思考过程

证明的关键是把"多元"问题化为"一元"问题：固定点 $x$，考察射线 $t\mapsto f(tx)$，它是 $t$ 的一元光滑函数。函数在 $t=0$ 与 $t=1$ 的差可以用一元微积分基本定理写成导数的积分，而按链式法则这个导数恰好是 $\sum_i x_i\partial_i f(tx)$，于是 $x_i$ 自然被提到积分号外，剩下的部分就是 $g_i$。难点有两个：一是要说明 $g_i$ 确实光滑，这靠"积分号下求导"；二是要算出 $g_i(0)$，只需把 $x=0$ 代入积分即得 $\partial_i f(0)$。至于消没到 $k$ 阶的推论，对 $f$ 反复使用本引理即可。

## 证明过程

**步骤 1：沿射线求导。** 为使 $tx\in U$ 对一切 $t\in[0,1]$ 成立，先把 $x$ 限制在 $U$ 中一个以原点为中心、关于原点星形的球内。定义

$$
h(t)=f(tx),\qquad t\in[0,1].
$$

由多变量链式法则，

$$
h'(t)=\sum_{i=1}^n x_i\,\partial_i f(tx).
$$

**步骤 2：对 $h$ 用一元微积分基本定理。**

$$
f(x)-f(0)=h(1)-h(0)=\int_0^1 h'(t)\,\mathrm dt=\int_0^1\sum_{i=1}^n x_i\,\partial_i f(tx)\,\mathrm dt.
$$

**步骤 3：提取坐标因子并定义 $g_i$。** 由于 $x_i$ 与积分变量 $t$ 无关，可提到积分号外：

$$
f(x)-f(0)=\sum_{i=1}^n x_i\int_0^1\partial_i f(tx)\,\mathrm dt =\sum_{i=1}^n x_i\,g_i(x),
$$

其中 $g_i(x):=\int_0^1\partial_i f(tx)\,\mathrm dt$。

**步骤 4：证明 $g_i$ 光滑。** 被积函数 $(t,x)\mapsto\partial_i f(tx)$ 关于 $x$ 光滑，其在紧集 $[0,1]\times K$（$K$ 为 $x$ 所在的紧邻域）上有各阶 $x$-偏导数的连续上界。由积分号下求导（Leibniz 法则的积分形式），

$$
\partial_j g_i(x)=\int_0^1 t\,\partial_j\partial_i f(tx)\,\mathrm dt,
$$

且此过程可反复进行任意多次，故 $g_i\in C^\infty(U)$。

**步骤 5：计算 $g_i(0)$。** 代入 $x=0$ 得

$$
g_i(0)=\int_0^1\partial_i f(0)\,\mathrm dt=\partial_i f(0).
$$

**步骤 6：多重指标推论。** 若 $f$ 消没到 $k$ 阶，先由步骤 3 得 $f=\sum_{|\alpha|=1}x^\alpha g_\alpha$，其中各 $g_\alpha$ 消没到 $k-1$ 阶（因为对 $f$ 求一阶导后各阶低于 $k-1$ 的导数在原点为零）。对每个 $g_\alpha$ 再用本引理得 $g_\alpha=\sum_{|\beta|=1}x^\beta g_{\alpha\beta}$，代入并对 $k$ 归纳，即得

$$
f(x)=\sum_{|\alpha|=k}x^\alpha g_\alpha(x),\qquad g_\alpha\in C^\infty(U).
$$

证毕。

## 课堂问答

**老师**：为什么对一般 $C^\infty$ 函数也能写出 $f(x)=f(0)+\sum_i x_i g_i(x)$ 且 $g_i$ 光滑？

**学生**：结论：把多元问题化为一元。沿射线 $h(t)=f(tx)$，由微积分基本定理 $f(x)-f(0)=\int_0^1\sum_i x_i\partial_i f(tx)\,\mathrm dt$，把 $x_i$ 提到积分号外即得 $g_i(x)=\int_0^1\partial_i f(tx)\,\mathrm dt$。常见误区：以为需要 Taylor 级数的收敛性。

**老师（追问）**：$g_i$ 的光滑性与 $g_i(0)=\partial_i f(0)$ 分别怎么来？

**学生**：光滑性来自 $\partial_j g_i(x)=\int_0^1 t\,\partial_j\partial_i f(tx)\,\mathrm dt$ 可反复进行；$g_i(0)$ 只需代入 $x=0$，得 $\int_0^1\partial_i f(0)\,\mathrm dt=\partial_i f(0)$。

**老师（拓展）**：消没到 $k$ 阶的版本怎么推？

**学生**：对 $f=\sum_{|\alpha|=1}x^\alpha g_\alpha$ 反复使用引理（各 $g_\alpha$ 消没到 $k-1$ 阶），归纳得 $f=\sum_{|\alpha|=k}x^\alpha g_\alpha$。这正是 Morse 引理把函数整理成 $x_ix_j a_{ij}(x)$ 的依据。

## 相关条目

- [Morse函数与Morse引理](./Morse函数与Morse引理.md)：Morse 引理在临界点附近把函数化为二次型，其代数基础正是 Hadamard 引理。
- [Morse理论](../第52级-微分拓扑/Morse理论.md)：临界点的局部标准模型依赖 Hadamard 引理给出的光滑分解。
- [反函数定理](../第12级-多变量微积分/反函数定理.md)：Hadamard 引理是反函数定理证明中局部化简函数的标准工具。
- [泰勒级数展开定理](../第13级-级数理论/泰勒级数展开定理.md)：本引理给出 Taylor 展开余项的光滑表达式，是余项估计的起点。
