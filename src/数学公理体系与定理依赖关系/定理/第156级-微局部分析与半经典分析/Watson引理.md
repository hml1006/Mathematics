# Watson 引理

> **一句话大白话**：大参数 Laplace 变换几乎只看积分在原点附近的脸色；把被积函数在那里按幂展开，就能逐项积分，Gamma 函数自动给出每一项的系数。
>
> **小例子**：$I(\lambda)=\int_0^\infty e^{-\lambda t}(1+t)^{-1}\,\mathrm dt$。由 $(1+t)^{-1}=\sum_{k\ge0}(-1)^kt^k$ 得 $I(\lambda)\sim\sum_{k\ge0}(-1)^kk!\lambda^{-k-1}$。

## 介绍

Watson 引理把函数在积分端点的局部渐近展开转化为整个 Laplace 积分的渐近展开。它允许端点有可积幂奇性，也不要求函数全局解析；远离端点的部分在适当可积条件下是指数小量。该引理是 Laplace 方法、特殊函数渐近和最速下降展开的基础工具。

## 分析

**前置依赖**：Gamma 函数、渐近级数、支配收敛与指数衰减估计。

**定理内容**：设 $0<A\le\infty$，$\phi$ 可测，并考虑 $\lambda\to+\infty$ 时

$$
I(\lambda)=\int_0^Ae^{-\lambda t}\phi(t)\,\mathrm dt .
$$

假设当 $t\to0^+$ 时

$$
\phi(t)\sim\sum_{k=0}^{\infty}a_kt^{\alpha_k},
\qquad -1<\alpha_0<\alpha_1<\cdots,
\qquad \alpha_k\to\infty,
$$

并存在 $\lambda_0\ge0$，使 $e^{-\lambda_0t}\phi(t)$ 在积分尾部可积。则

$$
\boxed{I(\lambda)\sim\sum_{k=0}^{\infty}
 a_k\Gamma(\alpha_k+1)\lambda^{-\alpha_k-1}.}
$$

更便于估计误差的有限项版本是：若

$$
\phi(t)=\sum_{k=0}^{N}a_kt^{\alpha_k}+O(t^\beta),
\qquad \beta>\alpha_N,
$$

则

$$
I(\lambda)=
\sum_{k=0}^{N}a_k\Gamma(\alpha_k+1)\lambda^{-\alpha_k-1}
+O(\lambda^{-\beta-1}).
$$

条件 $\alpha_0>-1$ 保证端点局部可积。若只展开到某有限阶，上述余项就是对应阶；截断后远离 $0$ 的积分为 $O(e^{-c\lambda})$，小于任何固定负幂项。

## 思考过程

当 $\lambda$ 很大时，尺度 $t\asymp\lambda^{-1}$ 的区域贡献主要积分，因为 $e^{-\lambda t}$ 在那里仍不衰减，而固定 $t>0$ 处会指数衰减。于是把局部展开逐项代入，并用 $u=\lambda t$ 换元：

$$
\int_0^\infty e^{-\lambda t}t^\alpha\,\mathrm dt
=\lambda^{-\alpha-1}\int_0^\infty e^{-u}u^\alpha\,\mathrm du
=\Gamma(\alpha+1)\lambda^{-\alpha-1}.
$$

剩下的工作只是控制局部展开余项和截断尾部。

## 证明过程

**证明纲要**：

1. **截断**：选取很小的 $\delta>0$，使局部有限展开在 $(0,\delta)$ 内有效。对 $\lambda$ 充分大，
   $$
   \int_\delta^Ae^{-\lambda t}\phi(t)\,\mathrm dt
   =O(e^{-(\lambda-\lambda_0)\delta}),
   $$
   因而比任意 $\lambda^{-M}$ 都小。
2. **代入主项**：对每个 $k\le N$，
   $$
   \int_0^\delta e^{-\lambda t}a_kt^{\alpha_k}\,\mathrm dt
   =a_k\Gamma(\alpha_k+1)\lambda^{-\alpha_k-1}
   +O(e^{-c\lambda}),
   $$
   因为补到无穷远所产生的误差仍是指数小量。
3. **控制局部余项**：若 $|R(t)|\le Ct^\beta$，则
   $$
   \left|\int_0^\delta e^{-\lambda t}R(t)\,\mathrm dt\right|
   \le C\int_0^\infty e^{-\lambda t}t^\beta\,\mathrm dt
   =C\Gamma(\beta+1)\lambda^{-\beta-1}.
   $$
4. **合并**：主项、局部余项和指数小的尾部合并即得有限项公式。依次令 $N\to\infty$（这里指取渐近展开的更多项，而非固定 $\lambda$ 下令级数收敛）就得到完整 Poincaré 渐近展开。$\square$

## 课堂问答

**老师**：为什么 Watson 引理不要求 $\phi$ 在整个积分区间解析？

**学生**：因为大参数下只有 $t=0$ 的任意小邻域贡献固定负幂阶，远处只剩指数小量。只要局部有渐近幂展开、尾部有基本的指数可积控制，就能逐项算出整个展开。

**老师（追问）**：为什么首项指数是 $-\alpha_0-1$，而系数含 $\Gamma(\alpha_0+1)$？

**学生**：换元 $u=\lambda t$ 会同时让 $t^{\alpha_0}$ 给出 $\lambda^{-\alpha_0}$、让 $\mathrm dt$ 给出 $\lambda^{-1}$，剩下的积分正是 $\Gamma(\alpha_0+1)$。所以幂次和系数都来自同一个 Gamma 积分。

**老师（拓展）**：Watson 引理的渐近级数是否应当收敛？

**学生**：不必。例子中的 $\sum(-1)^kk!\lambda^{-k-1}$ 对固定 $\lambda$ 发散，但截到任意 $N$ 项都有 $O(\lambda^{-N-2})$ 余项。渐近展开关注固定项数、$\lambda\to\infty$ 的误差，不关注固定 $\lambda$、项数趋于无穷的收敛性。

## 相关条目

- [Laplace 方法](./Laplace方法.md)
- [最速下降法](./最速下降法.md)
- [主教程第59级：渐近分析](../../../05-高阶专题I-分析几何统计/第59级-渐近分析.md)
