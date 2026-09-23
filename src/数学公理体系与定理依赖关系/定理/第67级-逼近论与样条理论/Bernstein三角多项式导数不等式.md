# Bernstein 三角多项式导数不等式

> **一句话大白话**：一个 $n$ 次三角多项式不管长什么样，它的变化速度都被次数锁死：导数最多是把原函数放大 $n$ 倍，再想更快就得提高次数。

> **小例子**：$T(\theta)=\cos n\theta$ 的变化最快处出现在它穿过零点的位置，那里 $|T'|=n$，恰好取到界 $n\|T\|_\infty$，说明常数 $n$ 不能改进。

## 一、定理介绍

> **前置依赖**：三角多项式与 Fourier 级数、连续模（连续性模）的定义与性质、Dirichlet 核及其导数、拉格朗日中值定理、一致收敛与逐项求导。

Bernstein 三角多项式导数不等式由 Sergei Bernstein 于 1912 年证明：次数不超过 $n$ 的三角多项式，其导数算子范数恰为 $n$。它不是一条技术性估计，而是"**光滑性由次数决定**"这一逼近论基本原则的解析形式：

1. **逼近阶的上界**：若 $T_n$ 是 $f$ 的最佳三角逼近多项式，则 $\|f-T_n\|\le E_n(f)$ 与 $\|T_n'\|\le n\|T_n\|$ 联立，可把 $f$ 的光滑性（连续模）与 $E_n(f)$ 的大小互相控制，这正是 Jackson 定理与 Bernstein 逆定理的骨架；
2. **整体可导性**：对 $2\pi$-周期函数，若 $E_n(f)=O(n^{-k-\alpha})$，则由 Bernstein 不等式可逐阶求导并得到 $f\in C^{k,\alpha}$；
3. **唯一性常数**：$n$ 是最优常数，等式在 $T=a\cos n\theta+b\sin n\theta$ 处取到，这使其成为"导数阶数 = 次数"的精确刻画；
4. **推广**：对代数多项式有 Markov 不等式 $\|p'\|_{[-1,1]}\le n^2\|p\|_{[-1,1]}$，其 $n^2$ 因子正是"三角情形 $n$ 乘以 Chebyshev 变量替换带来的 Jacobi 因子"的反映。

## 二、原理思路

1. **归一化**：由线性与平移不变性，可设 $T$ 实值、$\|T\|_\infty\le1$，并只需在固定点 $\theta_0=0$ 处估计 $T'(0)$。
2. **只留奇分量**：$T$ 的偶分量对 $T'(0)$ 无贡献，故只需处理奇三角多项式 $U(\theta)=\sum_{k=1}^{n}b_k\sin k\theta$，此时 $U'(0)=\sum_{k=1}^{n}kb_k$，问题化为"系数加权和的大小被 $\|U\|_\infty$ 控制"。
3. **用核表示显式化**：次数 $\le n$ 的三角多项式可由 Dirichlet 核的导数作卷积表示 $T'=T*D_n'$，于是导数算子范数不超过 $\|D_n'\|_{L^1}/2\pi$，得到与次数和 $n\log n$ 同阶的初等估计。
4. **提升到精确常数**：Bernstein 的原始论证把辅助函数 $A^2-T(\theta)^2$（在 $|T|$ 的极值点处有双重零点且非负）与 $\sin^2\frac{n(\theta-\theta_0)}{2}$ 作比较，利用"非负三角多项式在同一频率上不能振荡过快"这一事实，把上一步的 $n\log n$ 收紧为恰好 $n$。

## 三、定理的严格表述

**定理 1（Bernstein 三角不等式）**：设 $T_n$ 是次数不超过 $n$ 的实系数三角多项式，则
$$
\|T_n'\|_\infty\le n\,\|T_n\|_\infty .
$$
常数 $n$ 不能改进：对 $T_n(\theta)=a\cos n\theta+b\sin n\theta$（$a^2+b^2>0$），在 $T_n$ 的零点处 $|T_n'|=n\|T_n\|_\infty$。

**定理 2（第二 Bernstein 不等式）**：在同样假设下
$$
\|T_n''\|_\infty\le n^2\,\|T_n\|_\infty ,
$$
更一般地 $\|T_n^{(k)}\|_\infty\le n^k\|T_n\|_\infty$。

**定理 3（Markov 不等式，代数形式，对照）**：设 $p$ 是次数不超过 $n$ 的实系数多项式，则
$$
\max_{[-1,1]}|p'|\le n^2\max_{[-1,1]}|p| .
$$

**推论（Bernstein 逆定理的输入）**：对 $2\pi$-周期函数 $f$，若其最佳三角逼近误差满足 $E_n(f)\le Cn^{-\alpha}$（$0<\alpha<1$），则 $f\in\operatorname{Lip}\alpha$，即 $\omega(f,\delta)\le C'\delta^{\alpha}$。

## 四、证明过程

**证明（定理 1）。**

**步骤 1（归一化）。** 由齐次性与平移、符号对称性，只需对实值、$\|T_n\|_\infty\le1$ 的三角多项式证明 $|T_n'(0)|\le n$。

**步骤 2（只留奇分量）。** 写 $T_n(\theta)=E(\theta)+U(\theta)$，$E$ 为偶分量、$U(\theta)=\sum_{k=1}^{n}b_k\sin k\theta$ 为奇分量。因 $E'(0)=0$，故 $T_n'(0)=U'(0)=\sum_{k=1}^{n}kb_k$。又 $|U(\theta)|=\frac{|T_n(\theta)-T_n(-\theta)|}{2}\le1$，故问题等价于：**对次数 $\le n$、$\|U\|_\infty\le1$ 的奇三角多项式，证明 $\bigl|\sum_{k=1}^{n}kb_k\bigr|\le n$。**

**步骤 3（核表示：一个严格但较粗的估计）。** 对次数 $\le n$ 的三角多项式成立卷积恒等式
$$
T_n'(\theta)=\frac{1}{2\pi}\int_{-\pi}^{\pi}T_n(\theta-t)\,D_n'(t)\,dt,\qquad D_n(t)=\sum_{k=-n}^{n}e^{ikt}.
$$
（理由：$D_n'(t)=\sum_{|k|\le n}ik\,e^{ikt}$ 是次数 $\le n$ 的三角多项式在 $\theta=0$ 处求导的"再生核"，与 $T_n$ 卷积即得 $T_n'$。）于是
$$
\|T_n'\|_\infty\le\frac{\|D_n'\|_{L^1}}{2\pi}\,\|T_n\|_\infty=C\,n\log n\,\|T_n\|_\infty ,
$$
因为 $D_n(t)=\frac{\sin((n+\frac12)t)}{\sin(t/2)}$ 使 $\|D_n'\|_{L^1}=O(n\log n)$。这给出阶数正确的初等估计，但常数不是最优。

**步骤 4（精确常数 $n$ 的论证要点）。** 步骤 3 已给出阶数正确的估计 $O(n\log n)$，但要得到最优常数 $n$，需要 Bernstein 的辅助函数论证，其要点如下。

设 $\|T_n\|_\infty=A$，考察非负三角多项式
$$
F(\theta)=A^2-T_n(\theta)^2\ \ge\ 0 .
$$
在 $|T_n|$ 取到最大值 $A$ 的点 $\theta_0$ 处有 $T_n'(\theta_0)=0$，故 $F$ 在 $\theta_0$ 处的零点是**双重零点**。关键的非负性事实是：

> **引理（非负三角多项式的频率约束）**：次数 $\le 2n$ 的非负三角多项式 $F$ 若在 $\theta_0$ 处有双重零点，则它在 $\theta_0$ 附近不能比 $\sin^2 n(\theta-\theta_0)$ 下降得更快；等价地，其二阶展开系数满足 $|F''(\theta_0)|\le 4n^2\max F$。

对 $F=A^2-T_n^2$ 在 $\theta_0$ 处作二阶展开（用 $T_n'(\theta_0)=0$）：
$$
F(\theta_0+\tau)=-A\,T_n''(\theta_0)\,\tau^2+O(\tau^3),
$$
与引理比较即得：在每个极值点处
$$
|T_n''(\theta_0)|\le n^2A .
$$
再对 $T_n'$（它仍是次数 $\le n$ 的三角多项式）应用同一估计，并配合导数中值定理（在 $T_n'$ 的相邻极值点与零点之间取差分），即把常数由 $O(\log n)$ 修正为 $n$，得到定理 1 与定理 2。引理本身可由把 $F$ 按 $\cos k(\theta-\theta_0)$ 展开、并利用非负三角多项式对应的 Toeplitz 型半正定性证明，细节见逼近论标准教材。

**步骤 5（等式情形与常数最优性）。** 取 $T_n(\theta)=a\cos n\theta+b\sin n\theta$，$A=\sqrt{a^2+b^2}$。在 $T_n$ 的零点 $\theta_*$ 处 $|T_n'(\theta_*)|=n\sqrt{a^2+b^2}=nA$，故常数 $n$ 不能改进。$\square$

## 五、应用与意义

- **Jackson 定理与逆定理**：Bernstein 不等式是"逼近速度 ⟺ 光滑性"这对定理的技术支点，见 [Jackson定理与Bernstein定理](./Jackson定理与Bernstein定理.md)。
- **Chebyshev 逼近**：在最佳一致逼近中给出导数的先验界，用于 Chebyshev 交错定理的稳定性与收敛速度分析，见 [Chebyshev逼近理论](./Chebyshev逼近理论.md)。
- **样条与小波**：三角多项式导数界是细分格式（subdivision）收敛性、以及 [小波逼近](./小波逼近.md) 中正则性估计的基础。
- **信号处理**：带限信号（次数对应带宽）的导数幅度与带宽成正比的定量形式，用于滤波器设计与采样理论。

## 相关条目

- [Jackson定理与Bernstein定理](./Jackson定理与Bernstein定理.md)：本不等式与 Jackson 定理合起来刻画逼近阶与光滑性。
- [Chebyshev逼近理论](./Chebyshev逼近理论.md)：代数多项式的 Markov/Bernstein 型不等式与交错定理。
- [正交多项式理论](./正交多项式理论.md)：由 Bernstein 不等式可导出正交多项式 Christoffel 函数的增长估计。
- [Weierstrass逼近定理](./Weierstrass逼近定理.md)：多项式逼近的存在性定理。
- [小波逼近](./小波逼近.md)：细分与多分辨分析中的导数估计。
