# 强 Markov 性

> **一句话大白话**：普通 Markov 性说“从固定时刻重新出发”，强 Markov 性则说：只要这个时刻是按规则停下来的停时，哪怕它本身是随机的，过程也能从当时的位置重新出发。
>
> **小例子**：标准 Brown 运动 $B$ 首次到达 $a>0$ 的时刻为 $\tau_a$。在 $\tau_a<\infty$ 上，$W_t=B_{\tau_a+t}-a$ 仍是标准 Brown 运动，并且与 $\mathcal F_{\tau_a}$ 独立，就像从 $a$ 重新启动了一条 Brown 运动。

## 介绍

强 Markov 性把固定时间的无记忆性推广到停时。它是首达时分解、反射原理、常返性分析和随机过程拼接的基本工具。并非所有仅满足逐时刻 Markov 性质的过程都自动具有这一强化版本；常见充分框架是离散时间 Markov 链，以及具有 càdlàg 轨道的时齐 Feller 过程。

## 分析

**前置依赖**：Markov 性、滤过与适应过程、停时及其 $\sigma$-代数 $\mathcal F_\tau$、条件期望、转移半群、右连续轨道。

**定理内容**：设 $(X_t)_{t\geq0}$ 是取值于 Polish 空间 $E$ 的时齐 Feller 过程，具有 càdlàg 轨道，滤过满足通常条件，转移半群为

$$
(P_tf)(x)=\mathbb E_x[f(X_t)],
\qquad f\in B_b(E).
$$

若 $\tau$ 是该滤过的停时，则对有界可测函数 $f$ 和固定 $t\geq0$，

$$
\mathbb E_x\!\left[\mathbf 1_{\{\tau<\infty\}}f(X_{\tau+t})\mid\mathcal F_\tau\right]
=\mathbf 1_{\{\tau<\infty\}}(P_tf)(X_\tau),
\qquad \mathbb P_x\text{-a.s.}
$$

更一般地，对路径空间上的有界可测泛函 $Y$，

$$
\mathbb E_x\!\left[\mathbf 1_{\{\tau<\infty\}}Y(X_{\tau+\cdot})\mid\mathcal F_\tau\right]
=\mathbf 1_{\{\tau<\infty\}}\mathbb E_{X_\tau}[Y].
$$

这表示：在 $\{\tau<\infty\}$ 上，给定截至停时的全部信息后，未来过程的条件分布只由当前状态 $X_\tau$ 决定，并与从该状态独立重启的过程相同。

离散时间时齐 Markov 链的表述更直接：若 $\tau$ 为停时，则在 $\{\tau<\infty\}$ 上

$$
\mathbb P(X_{\tau+1}=x_1,\dots,X_{\tau+k}=x_k\mid\mathcal F_\tau)
=p(X_\tau,x_1)p(x_1,x_2)\cdots p(x_{k-1},x_k).
$$

这里的 $\tau$ 必须是停时，即 $\{\tau\leq t\}\in\mathcal F_t$；任意随机时刻不满足这一信息约束时，结论可能失败。

## 思考过程

若 $\tau$ 只取可数个时间值，可以在每个 $\{\tau=t_n\}$ 上应用普通 Markov 性，再合并条件期望。连续时间的一般停时用从上方逼近的离散停时 $\tau_n\downarrow\tau$ 处理；右连续轨道保证 $X_{\tau_n}\to X_\tau$，Feller 性保证 $(P_tf)(X_{\tau_n})\to(P_tf)(X_\tau)$，于是可用控制收敛取极限。

## 证明过程

**证明纲要**：先设 $\tau$ 只取值于可数集 $\{t_j\}$，并暂时假设 $\tau<\infty$。对任意 $A\in\mathcal F_\tau$，有 $A\cap\{\tau=t_j\}\in\mathcal F_{t_j}$。普通 Markov 性给出

$$
\begin{aligned}
\mathbb E_x[\mathbf 1_A f(X_{\tau+t})]
&=\sum_j\mathbb E_x[\mathbf 1_{A\cap\{\tau=t_j\}}f(X_{t_j+t})]\\
&=\sum_j\mathbb E_x[\mathbf 1_{A\cap\{\tau=t_j\}}(P_tf)(X_{t_j})]\\
&=\mathbb E_x[\mathbf 1_A(P_tf)(X_\tau)].
\end{aligned}
$$

这正是一般条件期望的定义性质。对可无限停时，在各等式中乘以 $\mathbf 1_{\{\tau<\infty\}}$ 即可。

对一般有限停时，取

$$
\tau_n=2^{-n}\left(\lfloor2^n\tau\rfloor+1\right),
$$

则 $\tau_n$ 是只取可数值的停时，且 $\tau_n\downarrow\tau$。对离散停时结论使用轨道右连续性、Feller 转移函数对连续有界函数的连续性以及有界收敛，可过渡到 $\tau$。无穷停时通过同一截断因子处理，路径泛函形式再用逐点有界逼近或单调类定理推广。以上省略通常条件带来的技术验证。$\square$

## 课堂问答

**老师**：强 Markov 性比普通 Markov 性强在哪里？

**学生**：普通 Markov 性在固定时刻 $s$ 描述未来只依赖 $X_s$；强 Markov 性把 $s$ 换成任意停时 $\tau$，在 $\tau<\infty$ 上有 $\mathbb E[f(X_{\tau+t})\mid\mathcal F_\tau]=(P_tf)(X_\tau)$。所以首次到达、首次穿越等随机但可停的时刻也能作为重启时刻。

**老师（追问）**：为什么要求 $\tau$ 是停时？证明连续时间版本为何还需要右连续和 Feller 条件？

**学生**：停时条件保证 $\{\tau=s\}$ 或 $\{\tau\leq s\}$ 与当时信息相容，才能逐段使用普通 Markov 性。一般停时先由离散停时从上方逼近，右连续性保证状态收敛，Feller 性保证重启半群值也连续收敛；没有这些条件，取极限的步骤缺乏依据。

**老师（拓展）**：Brown 运动的反射原理怎样体现强 Markov 性？

**学生**：在首次击中 $a$ 的 $\tau_a$ 后，将路径 $B_{\tau_a+t}$ 重启为从 $a$ 出发的 Brown 运动。把重启后的增量关于水平线 $a$ 反射，不改变其分布；强 Markov 性保证这段未来与停时前的信息具有正确的条件独立性，从而可把“时刻 $t$ 前曾到 $a$ 且终点低于某水平”的概率改写为未反射路径的终点概率。

## 相关条目

- [Doob 可选停止定理](./Doob可选停止定理.md)
- [Brown 运动的存在性](./Brown运动的存在性.md)
