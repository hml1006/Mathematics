# Volterra 积分方程的预解核

> **一句话大白话**：连续核的第二类 Volterra 方程可以靠反复迭代求解；每次迭代多出一个阶乘压低误差，所以不像一般 Fredholm 方程那样要求参数足够小。
>
> **小例子**：方程 $\varphi(x)=1+\lambda\int_0^x\varphi(t)\,\mathrm dt$ 的迭代核为 $(x-t)^{m-1}/(m-1)!$，预解核为 $e^{\lambda(x-t)}$，最终得到 $\varphi(x)=e^{\lambda x}$。

## 介绍

第二类 Volterra 积分方程把当前未知值与“过去”的积分联系起来。三角积分区域使迭代核自带组合体积因子 $(x-t)^{m-1}/(m-1)!$，于是 Neumann 级数对任意复参数都收敛，并能写成一个连续的预解核。这同时给出连续解的存在、唯一性和可计算的截断误差。

## 分析

**前置依赖**：连续函数空间与一致收敛、积分算子、Neumann 级数、压缩映射思想。

**定理内容**：设 $f\in C[a,b]$，$K$ 在三角区域

$$
\Delta=\{(x,t):a\le t\le x\le b\}
$$

上连续，$\lambda\in\mathbb C$。考虑

$$
\varphi(x)=f(x)+\lambda\int_a^xK(x,t)\varphi(t)\,\mathrm dt .
$$

定义 Volterra 算子 $V$ 和迭代核

$$
(V\psi)(x)=\int_a^xK(x,t)\psi(t)\,\mathrm dt,
\qquad K_1=K,
$$

$$
K_m(x,t)=\int_t^xK(x,s)K_{m-1}(s,t)\,\mathrm ds,
\qquad m\ge2.
$$

则预解核级数

$$
R(x,t;\lambda)=\sum_{m=1}^{\infty}\lambda^{m-1}K_m(x,t)
$$

在 $\Delta$ 上对 $\lambda$ 的每个有界集一致收敛，$R$ 连续，并且方程的唯一连续解为

$$
\boxed{\varphi(x)=f(x)+\lambda\int_a^xR(x,t;\lambda)f(t)\,\mathrm dt.}
$$

等价地，$\varphi=\sum_{m=0}^{\infty}\lambda^mV^mf$。若 $|K|\le M$，则

$$
|K_m(x,t)|\le \frac{M^m(x-t)^{m-1}}{(m-1)!},
\qquad
|R(x,t;\lambda)|\le M e^{|\lambda|M(x-t)}.
$$

因此不存在 $|\lambda|\|V\|<1$ 这类额外限制。取部分和 $\varphi_N=\sum_{m=0}^N\lambda^mV^mf$，并令 $L=b-a$，还有

$$
\|\varphi-\varphi_N\|_\infty
\le \|f\|_\infty\sum_{m=N+1}^{\infty}\frac{(|\lambda|ML)^m}{m!}.
$$

## 思考过程

若直接把 $V$ 当作 Fredholm 积分算子估计，只能得到粗略显的算子范数界 $ML$，进而要求 $|\lambda|ML<1$。但这个估计没有利用积分上限是 $x$。每次复合都把积分区域缩成高一维的单纯形，其体积带阶乘分母；正是这种“因果嵌套”让任意高阶迭代最终都可忽略。

## 证明过程

**证明纲要**：

1. **迭代核估计**：$m=1$ 时估计显然。若它对 $m-1$ 成立，则
   $$
   |K_m(x,t)|
   \le\int_t^xM\frac{M^{m-1}(s-t)^{m-2}}{(m-2)!}\,\mathrm ds
   =\frac{M^m(x-t)^{m-1}}{(m-1)!}.
   $$
   归纳即得全部估计，Weierstrass 判别法给出预解核级数的一致收敛与连续性。
2. **Neumann 级数收敛**：把上述核估计从 $t=a$ 到 $x$ 积分，得
   $$
   |(\lambda^mV^mf)(x)|
   \le\|f\|_\infty\frac{(|\lambda|M(x-a))^m}{m!}.
   $$
   指数级数控制所有项，故部分和在 $C[a,b]$ 中一致收敛，并得到所述截断误差。
3. **验证是解**：一致收敛允许求和与积分交换：
   $$
   f+\lambda V\varphi
   =f+\sum_{m=0}^{\infty}\lambda^{m+1}V^{m+1}f
   =\varphi .
   $$
   将 $(V^mf)(x)=\int_a^xK_m(x,t)f(t)\,\mathrm dt$ 代入并重排求和，即得到预解核公式。
4. **唯一性**：两个连续解之差 $\psi$ 满足 $\psi=\lambda V\psi$，故 $\psi=\lambda^mV^m\psi$。因此
   $$
   |\psi(x)|\le\|\psi\|_\infty\frac{(|\lambda|M(x-a))^m}{m!}\to0,
   $$
   所以 $\psi\equiv0$。$\square$

## 课堂问答

**老师**：为什么这里的 Neumann 级数对任意 $\lambda$ 都收敛？

**学生**：第 $m$ 次迭代的估计含 $1/m!$，它来自三角区域反复积分的体积，而不是来自 $\lambda$ 很小。任意固定的 $|\lambda|ML$ 都会被阶乘最终压过，所以级数总收敛。

**老师（追问）**：预解核 $R$ 与迭代核 $K_m$ 的求和式会不会差一个 $\lambda$？

**学生**：要按解公式核对。这里定义 $R=\sum_{m\ge1}\lambda^{m-1}K_m$，解写成 $\varphi=f+\lambda\int Rf$；乘在外面的 $\lambda$ 与 $R$ 中的 $\lambda^{m-1}$ 合成 $\lambda^m$，恰对应 $V^m$。若改用别的预解核约定，公式也要同步改。

**老师（拓展）**：这与 Volterra 算子的谱有何联系？

**学生**：连续核 Volterra 算子的谱半径为零，是拟幂零算子，所以 $I-\lambda V$ 对所有复 $\lambda$ 可逆。预解核级数就是这个全参数预解的显式核表示；一般 Fredholm 紧算子可能有非零特征值，不能期待同样结论。

## 相关条目

- [Fredholm 二择一定理](./Fredholm二择一定理.md)
- [Banach 不动点定理](../第89级-分形几何/Banach不动点定理.md)
- [Hilbert–Schmidt 核展开定理](./Hilbert-Schmidt核展开定理.md)
- [主教程第60级：积分方程](../../../05-高阶专题I-分析几何统计/第60级-积分方程.md)
