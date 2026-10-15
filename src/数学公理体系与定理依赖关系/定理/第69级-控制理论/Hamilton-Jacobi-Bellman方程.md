# Hamilton-Jacobi-Bellman 方程

> **一句话大白话**：HJB 方程是最优控制版的"最优化条件"——它说最优值函数在每点、每时刻都必须满足一个含下确界的偏微分方程，"即时代价加上未来值的变化率"再对控制取最小，等于零。

> **小例子**：线性系统 $\dot x=Ax+Bu$ 上最小化 $\int(x^{\mathsf T}Qx+u^{\mathsf T}Ru)\,dt$ 时，HJB 方程被二次型值函数 $V=x^{\mathsf T}Px$ 满足，从而导出代数 Riccati 方程。

## 一、定理介绍

> **前置依赖**：Bellman最优性原理、Pontryagin极大值原理、泰勒定理、Lyapunov稳定性定理。

Hamilton–Jacobi–Bellman（HJB）方程是连续时间最优控制的中心方程，由 Bellman 最优性原理经无穷小化得到。它把"在无穷多个控制函数上取极小"这一泛函最优化问题，改写为一个关于最优值函数的非线性偏微分方程；一旦求得并验证其解，最优控制便由该方程中的极小元显式给出。

HJB 方程与 Pontryagin 极大值原理互为补充：前者是**充分条件**且天然给出反馈形式的控制律，后者是**必要条件**且以开环路形式表述；当值函数足够光滑时，二者可互相转化。

## 二、原理思路

设最优值函数为 $V(t,x)$（从 $(t,x)$ 出发的最优剩余代价）。在极短时段 $[t,t+h]$ 内先施加常数控制 $u$，之后执行最优策略。由 Bellman 最优性原理，

$$
V(t,x)=\inf_{u\in U}\left\{\int_t^{t+h}L\bigl(x(s),u\bigr)\,ds+V\bigl(t+h,x(t+h)\bigr)\right\}.
$$

把后一项用泰勒定理在 $(t,x)$ 处展开，并用状态方程 $\dot x=f(x,u)$ 得

$$
V(t+h,x(t+h))=V(t,x)+h\bigl[\partial_tV+\nabla_xV\cdot f(x,u)\bigr]+o(h),
$$

而积分项为 $hL(x,u)+o(h)$。两边相减、除以 $h$ 并令 $h\to0^+$，即得 HJB 方程。求极小得到最优（反馈）控制 $u^*(t,x)$。

## 三、定理的严格表述

考虑最优控制问题：状态方程与代价泛函为

$$
\dot x(s)=f\bigl(x(s),u(s)\bigr),\qquad
J(t,x;u)=\int_t^{T}L\bigl(x(s),u(s)\bigr)\,ds+\phi\bigl(x(T)\bigr),
$$

其中 $x\in\mathbb{R}^n$、$u(s)\in U\subseteq\mathbb{R}^m$，$f,L,\phi$ 光滑。定义值函数

$$
V(t,x)=\inf_{u(\cdot)}J(t,x;u).
$$

**定理（HJB 方程与验证定理）**：设 $V\in C^1\bigl([0,T]\times\mathbb{R}^n\bigr)$ 为上述问题的值函数，则 $V$ 满足

$$
-\partial_tV(t,x)=\inf_{u\in U}\Bigl\{L(x,u)+\nabla_xV(t,x)\cdot f(x,u)\Bigr\},\qquad V(T,x)=\phi(x).
$$

反之（验证定理），若 $W\in C^1$ 满足该方程与终端条件，且对每个 $(t,x)$ 存在达到下确界的 $u^*(t,x)$，则 $W=V$，且 $u^*$ 为最优反馈控制，闭环系统在 $u^*$ 下的轨迹使 $W$ 沿程取极值。

**无穷时域折扣情形**：若 $L$ 带折扣因子 $e^{-\rho t}$ 且值函数与 $t$ 无关，则

$$
\rho V(x)=\inf_{u\in U}\Bigl\{L(x,u)+\nabla V(x)\cdot f(x,u)\Bigr\}.
$$

定义 Hamilton 函数 $H(x,p)=\inf_{u\in U}\bigl\{L(x,u)+p\cdot f(x,u)\bigr\}$，上式即 $\rho V=H(x,\nabla V)$。

## 四、证明过程

**（必要性）由动态规划原理导出 HJB。** 固定 $(t,x)$。对任意 $h>0$ 与任意常数控制 $u\in U$（在 $[t,t+h]$ 上取 $u$，之后取最优），由最优性原理 $V(t,x)\le J$，即

$$
V(t,x)\le\int_t^{t+h}L\bigl(x(s),u\bigr)\,ds+V\bigl(t+h,x(t+h)\bigr).
$$

由泰勒定理与状态方程，令 $x(t)=x$，

$$
V\bigl(t+h,x(t+h)\bigr)=V(t,x)+h\Bigl[\partial_tV+\nabla_xV\cdot f(x,u)\Bigr]+o(h),
$$

且 $\int_t^{t+h}L\,ds=h\,L(x,u)+o(h)$。代回并除以 $h$、令 $h\to0^+$：

$$
0\le L(x,u)+\partial_tV+\nabla_xV\cdot f(x,u).
$$

对 $u$ 取下确界得到 $0\le\partial_tV+\inf_u\bigl\{L+\nabla_xV\cdot f\bigr\}$。

另一方面，取 $u^*$ 为 HJB 中的极小元并要求 $h\to0$ 时不等式反向（因 $V$ 为下确界，可取近似最优控制使右端任意接近），得

$$
0\ge\partial_tV+\inf_u\bigl\{L+\nabla_xV\cdot f\bigr\}.
$$

两式合并即得 $- \partial_tV=\inf_u\{L+\nabla_xV\cdot f\}$。终端条件由 $V(T,x)=\phi(x)$ 直接给出。

**（充分性）验证定理。** 设 $W$ 满足 HJB 方程与终端条件，$u^*(t,x)$ 为极小元。对任意容许控制 $u(\cdot)$，沿其轨迹 $x(\cdot)$ 计算 $\dfrac{d}{ds}W(s,x(s))$：

$$
\frac{d}{ds}W=\partial_sW+\nabla_xW\cdot f(x,u)\ge -L(x,u),
$$

其中不等式用到 HJB 方程给出的下确界性质。对 $s\in[t,T]$ 积分：

$$
W(T,x(T))-W(t,x)\ge-\int_t^{T}L\bigl(x(s),u(s)\bigr)\,ds .
$$

结合 $W(T,\cdot)=\phi$ 得 $W(t,x)\le J(t,x;u)$，对一切 $u$ 取下确界得 $W\le V$。当取 $u=u^*$ 时上式取等号，故 $W(t,x)=J(t,x;u^*)\ge V$，从而 $W=V$，且 $u^*$ 最优。

**（无穷时域与稳定性）**。折扣情形中把 $t=0$ 的无穷积分分段，同样的泰勒展开（此时无 $\partial_tV$ 项）给出 $\rho V=\inf_u\{L+\nabla V\cdot f\}$。若进一步 $L(x,u)$ 关于 $x$ 正定，则可取 $V$ 作为 Lyapunov 函数：沿闭环轨迹

$$
\dot V=\nabla V\cdot f(x,u^*)=\rho V-L(x,u^*)\le\rho V,
$$

配合 $V>0$、$L>0$ 即可判定闭环系统渐近稳定（或具指数衰减界）。$\square$

## 五、应用与意义

- **线性二次调节器**：以二次型 $V=x^{\mathsf T}Px$ 代入 HJB，即得代数 Riccati 方程与最优反馈 $u^*=-R^{-1}B^{\mathsf T}Px$。
- **非线性最优控制**：HJB 给出一般非线性问题的充分最优性条件，是反步法、微分博弈与最优停时问题的统一框架。
- **黏性解理论**：值函数常不可微，需在黏性解意义下理解 HJB 方程，这是 Crandall–Lions 理论的出发点。
- **强化学习与动态规划**：离散化 HJB 得到值迭代与 Q-learning 的连续时间对应物；"维度灾难"促使近似动态规划与神经网络求解方法的发展。
- **与极大值原理的关系**：由 HJB 的最优性条件 $L_u+p^{\mathsf T}f_u=0$ 引入协态 $p=\nabla V$，即得 Pontryagin 极大值原理的正则方程。

## 课堂问答

**老师**：HJB 方程在连续时间最优控制里扮演什么角色？请写出它。

**学生**：它是**充分**最优性条件，把"在无穷多个控制函数上取极小"化为一个非线性偏微分方程 $-\partial_tV=\inf_{u\in U}\{L+\nabla_xV\cdot f\}$，终值 $V(T,x)=\phi(x)$。这里 $V(t,x)$ 是从 $(t,x)$ 出发的最优剩余代价，达到下确界的 $u^*(t,x)$ 就是反馈形式的最优控制。

**老师（追问）**：HJB 是充分条件、PMP 是必要条件，二者如何互推？

**学生**：把协态定义为值函数的梯度 $p=\nabla_xV$，则 PMP 的最优性条件 $L_u+p^{\mathsf T}f_u=0$ 与协态方程 $\dot p=-\partial_x(L+p^{\mathsf T}f)$ 恰好复现 PMP 的正则方程组；反之光滑情形下沿最优轨线积分 PMP 系统可构造出 $V$。差别在于 HJB 天然给出**状态反馈**且是充分条件，PMP 以**开环**形式给出必要条件，能处理控制集非凸、控制不连续（bang-bang）等值函数不可微的情形。

**老师（拓展）**：值函数常常不可微，这时方程还有意义吗？稳定性又怎么读出来？

**学生**：有，要用 Crandall–Lions 的**黏性解**理论：不要求 $V$ 可微，而用光滑测试函数在接触点处的不等式替代方程，从而保证解存在唯一。这也是二次型 $V=x^{\mathsf T}Px$ 能代入并导出代数 Riccati 方程的依据。稳定性上，若 $L$ 正定且取 $V$ 作 Lyapunov 函数，沿闭环 $\dot V=\nabla V\cdot f(x,u^*)=\rho V-L(x,u^*)$，配合 $V>0$、$L>0$ 即可判定渐近稳定或指数衰减。黏性解还支撑微分博弈与最优停时问题的统一处理。
