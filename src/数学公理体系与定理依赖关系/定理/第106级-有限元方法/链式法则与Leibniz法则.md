# 链式法则与 Leibniz 法则

> **一句话大白话**：微分运算有两条"运算律"——链式法则管复合函数怎么求导（变化率沿管道一层层传导、逐段相乘），Leibniz 法则管乘积怎么求高阶导（把 $n$ 阶导数按二项式系数分摊给两个因子）。有限元里把物理单元映到参考单元的缩放求导、以及高阶误差估计，全靠这两条。
>
> **小例子**：$(x^2e^{x})'''$ 无须逐次硬算，Leibniz 法则直接给出 $x^2e^x+6xe^x+6e^x$；而 $\dfrac{d}{dt}f(x(t),y(t))=f_xx'+f_yy'$ 与二阶形式 $\dfrac{d^2}{dt^2}f\big|_{g(t)}=\nabla f^\top g''+g'^\top\nabla^2f\,g'$ 正是链式法则。

## 一、定理介绍

> **前置依赖**：单变量链式法则、链式法则多变量、乘积求导法则、高阶导数公式、方向导数与梯度的关系。

**链式法则**回答"复合函数的导数是什么"：导数（微分）就是最佳线性逼近，而线性映射的复合仍是线性映射，其矩阵恰为 Jacobi 矩阵的乘积。**Leibniz 法则**（广义乘积法则）回答"乘积的高阶导数是什么"：它把 $n$ 阶导数按二项式系数分配给两个因子，是一元乘积求导法则在任意阶的推广。

两条法则是微分算子"代数化"的两根支柱：前者处理复合结构（坐标变换、缩放映射），后者处理乘法结构（分部积分、幂级数乘积、高次多项式的导数估计）。在有限元分析中，逆估计里物理元与参考元之间的导数换算、以及后验误差估计中对高阶导数的处理，都直接调用它们。

## 二、原理思路

1. **链式法则**的本质是"可微即线性逼近"：$f(g(t+h))=f(g(t))+\nabla f(g(t))^\top\big(g(t+h)-g(t)\big)+o\big(\|g(t+h)-g(t)\|\big)$，而 $g(t+h)-g(t)=J_g(t)h+o(\|h\|)$。把二者代入，$o$ 项仍然是小量，得到一阶展开即结论。
2. 一般维数的情形完全同构，只是标量换成矩阵：$J_{F\circ G}(t)=J_F(G(t))J_G(t)$。
3. **二阶链式法则**只需把一阶结论再求一次导，此时用到乘积求导法则（两个因子相乘）与链式法则本身（对 $\nabla f(g(t))$ 求导）。
4. **Leibniz 法则**用对 $n$ 的归纳法：$(fg)^{(n)}$ 求一次导后，把同类项按 $k$ 合并，系数由 Pascal 恒等式 $\binom nk+\binom n{k-1}=\binom{n+1}k$ 收拢，恰好仍是二项式系数。
5. **多指标形式**在每个坐标方向各用一次一元 Leibniz 法则，二项式系数相乘即得多项式系数。

## 三、定理的严格表述

**（一）链式法则。** 设 $G:\mathbb R^p\to\mathbb R^n$ 在 $t$ 处可微、$F:\mathbb R^n\to\mathbb R^m$ 在 $G(t)$ 处可微，则 $F\circ G$ 在 $t$ 处可微且
$$
J_{F\circ G}(t)=J_F\big(G(t)\big)\,J_G(t).
$$
一维参数 + 标量值的情形即 $\dfrac{d}{dt}f(G(t))=\nabla f(G(t))^\top G'(t)$；分量形式为
$$
\frac{\partial}{\partial t_j}f\big(x_1(t),\dots,x_n(t)\big)=\sum_{i=1}^{n}\frac{\partial f}{\partial x_i}\,\frac{\partial x_i}{\partial t_j}.
$$

**（二）二阶链式法则。** 在（一）的假设下再设 $F,G$ 二阶连续可微、$p=1$，则
$$
\frac{d^2}{dt^2}f(G(t))=G'(t)^\top\nabla^2f(G(t))\,G'(t)+\nabla f(G(t))^\top G''(t).
$$

**（三）Leibniz 法则（一元）。** 设 $f,g\in C^n(I)$，则
$$
(fg)^{(n)}=\sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)} .
$$
取 $n=1$ 即退化为通常的乘积求导法则 $(fg)'=f'g+fg'$。

**（四）Leibniz 法则（多指标）。** 设重指标 $\alpha=(\alpha_1,\dots,\alpha_d)$，$\binom{\alpha}{\beta}=\prod_{i=1}^{d}\binom{\alpha_i}{\beta_i}$，则对 $f,g\in C^{|\alpha|}$
$$
D^{\alpha}(fg)=\sum_{\beta\le\alpha}\binom{\alpha}{\beta}\,D^{\beta}f\;D^{\alpha-\beta}g .
$$
三个因子的情形（多元积）则由多项式系数 $\dfrac{\alpha!}{\beta!\gamma!(\alpha-\beta-\gamma)!}$ 给出。

## 四、证明过程

**步骤 1（链式法则）。** 由 $G$ 在 $t$ 可微，存在矩阵（Jacobi 矩阵）$J_G(t)$ 使
$$
G(t+h)-G(t)=J_G(t)h+o(\|h\|)\qquad(h\to0).
$$
由 $F$ 在 $s=G(t)$ 可微，存在矩阵 $J_F(s)$ 使
$$
F(s+v)-F(s)=J_F(s)v+o(\|v\|)\qquad(v\to0).
$$
取 $v=G(t+h)-G(t)=J_G(t)h+o(\|h\|)$，则 $\|v\|=O(\|h\|)$，于是
$$
F\big(G(t+h)\big)-F\big(G(t)\big)=J_F(s)\big[J_G(t)h+o(\|h\|)\big]+o(\|h\|)=J_F(s)J_G(t)\,h+o(\|h\|).
$$
最后一步用到线性映射的有界性（$\|J_F(s)\,o(\|h\|)\|\le C\|o(\|h\|)\|$）以及 $o$ 项的运算性质。按可微的定义，这恰说明 $F\circ G$ 在 $t$ 可微且 Jacobi 矩阵为 $J_F(G(t))J_G(t)$。（一维情形矩阵退化为 $1\times n$ 与 $n\times1$，取梯度内积即得标量公式。）

**步骤 2（二阶链式法则）。** 记 $u(t)=\nabla f(G(t))\in\mathbb R^n$。由步骤 1（用于向量值映射 $\nabla f\circ G$，其 Jacobi 矩阵为 $\nabla^2f(G(t))J_G(t)$）得
$$
u'(t)=\nabla^2f(G(t))\,G'(t)\in\mathbb R^n .
$$
对一阶公式 $\dfrac{d}{dt}f(G(t))=u(t)^\top G'(t)$ 再用乘积求导法则：
$$
\frac{d^2}{dt^2}f(G(t))=u'(t)^\top G'(t)+u(t)^\top G''(t)=G'(t)^\top\nabla^2f(G(t))G'(t)+\nabla f(G(t))^\top G''(t),
$$
其中用了对称性 $u'^\top G'=(G'^\top\nabla^2f)G'=G'^\top\nabla^2f\,G'$。

**步骤 3（Leibniz 法则，$n=1$ 与归纳奠基）。** $n=1$ 即乘积求导法则。假设 $n$ 时等式成立，对 $(fg)^{(n)}=\sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)}$ 再求一次导（对每一项使用乘积法则）：
$$
(fg)^{(n+1)}=\sum_{k=0}^{n}\binom nk\Big[f^{(k+1)}g^{(n-k)}+f^{(k)}g^{(n-k+1)}\Big].
$$
把第一个求和中 $k$ 换成 $k-1$，两项合并为同一个 $f^{(k)}g^{(n+1-k)}$：
$$
(fg)^{(n+1)}=\sum_{k=0}^{n+1}\Big[\binom n{k-1}+\binom nk\Big]f^{(k)}g^{(n+1-k)} .
$$
（这里约定越界二项式系数为 $0$。）由 Pascal 恒等式 $\binom n{k-1}+\binom nk=\binom{n+1}k$，右端化为 $\sum_{k=0}^{n+1}\binom{n+1}kg^{(n+1-k)}f^{(k)}$，归纳完成。

**步骤 4（多指标情形）。** 先在一维方向 $x_i$ 上反复使用步骤 3：
$$
\partial_i^{\alpha_i}(fg)=\sum_{\beta_i=0}^{\alpha_i}\binom{\alpha_i}{\beta_i}\,\partial_i^{\beta_i}f\;\partial_i^{\alpha_i-\beta_i}g .
$$
对 $i=1,\dots,d$ 逐次作用并展开，系数是各方向二项式系数之积，即 $\binom{\alpha}{\beta}=\prod_i\binom{\alpha_i}{\beta_i}$，且各方向的微分算子可交换（混合偏导数相等），整理即得 (四)。$\blacksquare$

**注（三因子与更一般情形）。** 对有限个因子，反复使用 (三) 得多项式系数公式；这是 (三) 的同型推广，证明只需对因子个数归纳。

## 五、应用与意义

- **坐标变换与逆估计**：物理单元 $T$（直径 $h_T$）与参考元 $\hat T$ 间由 $x=x_T+h_T\hat x$ 相联系，链式法则给出 $\nabla_x=\frac1{h_T}\nabla_{\hat x}$，是有限元逆估计与误差估计中 $h^{-1}$ 因子的来源。
- **高阶导数估计**：Leibniz 法则把 $D^\alpha(uv)$ 拆成低阶导数的乘积之和，是插值误差、分片多项式范数等价与 Sobolev 范数换算中的标准工具。
- **分部积分与弱形式**：乘积求导法则 $(uv)'=u'v+uv'$ 移项即得分部积分公式，是 Lax–Milgram 弱形式与守恒律 Rankine–Hugoniot 条件的代数基础。
- **幂级数与组合结构**：Leibniz 法则解释了 $(1+x)^n$ 的二项式系数来源，也是生成函数乘积与 Taylor 余项估计的基本手段。
