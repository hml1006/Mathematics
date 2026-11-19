# M/M/c 稳态公式与 Erlang-C

> **一句话大白话**：$c$ 个服务台共同接待泊松到达、指数服务的顾客，只要总服务能力 $c\mu$ 大于到达率 $\lambda$，就能算稳态队长；Erlang-C 则专门回答“新顾客到场后需要排队”的概率。
>
> **小例子**：若 $\lambda=2$、$c=2$、每个服务台 $\mu=2$，则 $a=\lambda/\mu=1$、$\rho=1/2$。公式给出空闲概率 $P_0=1/3$、等待概率 $C=1/3$，平均排队等待时间为 $W_q=C/(c\mu-\lambda)=1/6$。

## 介绍

M/M/c 队列假设泊松到达率 $\lambda$、每个服务台独立的指数服务率 $\mu$、$c$ 个并列服务台、无限等待室和先到先服务。其稳态分布由生灭过程求出，Erlang-C 公式及平均等待公式广泛用于呼叫中心和多服务台容量规划。

## 分析

**前置依赖**：泊松过程、指数分布、生灭过程、全局平衡方程、PASTA 性质、Little 定律、几何级数。

**定理内容**：定义提供负荷 $a=\lambda/\mu$ 和利用率

$$
\rho=\frac{\lambda}{c\mu}=\frac ac.
$$

系统存在稳态分布的充要条件是 $\boxed{\rho<1}$。在此条件下，

$$
P_n=
\begin{cases}
P_0\dfrac{a^n}{n!},&0\le n\le c,\\[6pt]
P_0\dfrac{a^c}{c!}\rho^{\,n-c},&n\ge c,
\end{cases}
$$

其中

$$
P_0=\left[\sum_{n=0}^{c-1}\frac{a^n}{n!}
+\frac{a^c}{c!(1-\rho)}\right]^{-1}.
$$

顾客到达时所有服务台都忙、因而必须等待的概率为 **Erlang-C**：

$$
\boxed{
C(c,a)=P(N\ge c)=
\frac{\dfrac{a^c}{c!(1-\rho)}}
{\displaystyle\sum_{n=0}^{c-1}\frac{a^n}{n!}
+\dfrac{a^c}{c!(1-\rho)}} }.
$$

平均排队等待时间、排队人数以及含服务的平均逗留指标分别为

$$
\boxed{W_q=\frac{C(c,a)}{c\mu-\lambda}},\qquad
L_q=\lambda W_q=\frac{\rho}{1-\rho}C(c,a),
$$

$$
W=W_q+\frac1\mu,\qquad L=\lambda W=a+L_q.
$$

对已经被迫等待的顾客，其条件平均等待时间为 $W_q/C=1/(c\mu-\lambda)$。

## 思考过程

当系统中有 $n<c$ 个顾客时，只有 $n$ 个服务台工作，总服务率为 $n\mu$；当 $n\ge c$ 时，全部服务台工作，总服务率固定为 $c\mu$。这使稳态概率先按阶乘型递推，随后转为几何递推。

几何尾 $\rho^{n-c}$ 只有在 $\rho<1$ 时可归一化，这正是稳定性来源。到达者看到的时间平均分布由 PASTA 保证，所以 $P(N\ge c)$ 就是 Erlang-C 等待概率；等待指标再由 Little 定律得到。

## 证明过程

系统中顾客数 $N(t)$ 是生灭过程，出生率恒为 $\lambda$，死亡率在状态 $n$ 为 $\mu_n=\min(n,c)\mu$。稳态的局部平衡给出

$$
\lambda P_{n-1}=\min(n,c)\mu P_n.
$$

当 $1\le n\le c$ 时递推得 $P_n=P_0a^n/n!$；当 $n>c$ 时递推得 $P_n=P_c\rho^{n-c}$。两式在 $n=c$ 处一致，合并即为分段公式。

将各概率相加，

$$
1=P_0\left[\sum_{n=0}^{c-1}\frac{a^n}{n!}
+\frac{a^c}{c!}\sum_{n=c}^{\infty}\rho^{n-c}\right].
$$

几何级数收敛当且仅当 $\rho<1$，其和为 $1/(1-\rho)$，从而得到 $P_0$。当 $\rho\ge1$ 时级数不能归一化，生灭链不存在所述有限稳态分布。

由 PASTA，到达顾客需要等待的概率为

$$
C=\sum_{n=c}^{\infty}P_n
=P_0\frac{a^c}{c!(1-\rho)}.
$$

在全忙期间，完成服务的间隔服从率 $c\mu$ 的指数分布，排队人数的离开与到达形成剩余等待分析；解相应生灭链的条件期望，或直接求 $L_q=\sum_{n=c}^{\infty}(n-c)P_n$ 并用 $L_q=\lambda W_q$，得到

$$
L_q=\frac{\rho}{1-\rho}C,
\qquad W_q=\frac{C}{c\mu-\lambda}.
$$

最后利用 $W=W_q+1/\mu$ 和 $L=\lambda W$ 完成证明。$\square$

## 课堂问答

**老师**：M/M/c 为什么必须要求 $\rho=\lambda/(c\mu)<1$？

**学生**：状态超过 $c$ 后，稳态概率按 $\rho^{n-c}$ 几何下降。只有 $\rho<1$ 时几何级数收敛并能归一化；这也等价于长期到达率小于全部服务台的总服务能力。

**老师（追问）**：Erlang-C 和 Erlang-B 是一回事吗？

**学生**：不是。Erlang-C 适用于无限等待室的 M/M/c 延迟系统，给出等待概率 $P(N\ge c)$；Erlang-B 适用于无等待室的损失系统，给出到达被拒的概率。二者模型和公式都不同。

**老师（拓展）**：$W_q$ 为什么还要除以 $c\mu-\lambda$？

**学生**：由稳态概率直接求平均排队人数得 $L_q=\rho C/(1-\rho)$，再用 Little 定律 $L_q=\lambda W_q$，便有 $W_q=C/(c\mu-\lambda)$。分母正是系统接近饱和时控制等待时间发散的速度。

## 相关条目

- [Little 定律](./Little定律.md)：把 Erlang-C 导出的 $L_q$ 与平均等待时间 $W_q$ 相互转换。
- [M/M/1 队列的稳态分布](./M_M-1队列的稳态分布.md)：$c=1$ 时本条目退化为单服务台几何稳态分布。
- [Erlang-B 公式](./Erlang-B公式.md)：对应无排队、会拒绝顾客的损失系统，可与延迟系统对照。
