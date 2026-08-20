# Bochner-Riesz 平均

> **一句话大白话**：把函数的频率按"圆盘分带"逐段拉回来时，切得越圆滑（加衰减因子）越可能稳定收敛——研究"按圆盘取频率分量的和到底收不收敛、在哪个空间收敛"的温和版截断问题。
>
> **小例子**：经典部分和对应 Bochner-Riesz 平均指数 $\delta=0$，$L^p$ 收敛只在 $p=2$ 保真；对 $\delta>\max\{(n-1)|1/p-1/2|-1/2,0\}$（或类似）时才有 $L^p$ 收敛——指数越大截得越柔、越不易出事。

## 一、定理介绍

Bochner-Riesz 平均是 Fourier 级数和 Fourier 积分的一种正则化求和方法，由 S. Bochner 和 M. Riesz 在 20 世纪 20-30 年代引入。在 $\mathbb{R}^n$ 上，$\delta$ 阶 Bochner-Riesz 平均定义为
$$T_R^\delta f(x) = \int_{|\xi| \le R} \left(1 - \frac{|\xi|^2}{R^2}\right)^\delta \hat{f}(\xi) e^{2\pi i x \cdot \xi}\, d\xi,$$
其 Fourier 乘子为 $m_R^\delta(\xi) = (1 - |\xi|^2/R^2)_+^\delta$。

当 $\delta = 0$ 时，这就是简单的球面截断（Fourier 部分和），对应的算子在 $L^p$（$p \ne 2$）上无界（Fefferman 球乘子定理，1971年）。当 $\delta$ 充分大时，Bochner-Riesz 平均在 $L^p$ 上有界。Bochner-Riesz 猜想试图确定使 $T_R^\delta$ 在 $L^p$ 上一致有界的最小 $\delta$，这是调和分析中最著名的未解决问题之一。

## 二、原理思路

**为什么需要 Bochner-Riesz 平均**：

Fourier 积分的部分和 $S_R f(x) = \int_{|\xi|\le R} \hat{f}(\xi)e^{2\pi i x\cdot\xi}\,d\xi$ 对应的乘子为 $\chi_{B(0,R)}(\xi)$，它在球面 $|\xi| = R$ 处不连续。这种不连续性导致 $S_R$ 在 $L^p$（$p \ne 2$）上的无界性（Fefferman 定理）。

Bochner-Riesz 平均通过在边界处引入光滑因子 $(1 - |\xi|^2/R^2)^\delta$ 来"软化"截断，使得乘子更加光滑，从而改善算子的有界性。

**关键参数**：$\delta$ 越大，乘子越光滑，算子的有界性越好。核心问题是找到临界指数 $\delta(p)$ 使得 $T_R^\delta$ 在 $L^p$ 上一致有界当且仅当 $\delta > \delta(p)$。

**已知结果**：
- 当 $p = 2$ 时，由 Plancherel 定理，$\delta > -1/2$ 即可（实际上 $\delta \ge 0$ 是自然要求）。
- 当 $p \ne 2$ 时，Bochner 和 Riesz 证明了 $\delta > n|1/p - 1/2| - 1/2$ 是充分的。
- Fefferman (1971) 证明 $\delta = 0$ 时 $L^p$ 无界（$n \ge 2$，$p \ne 2$）。
- 临界猜想：$\delta(p) = \max\{n|1/p - 1/2| - 1/2, 0\}$。

**证明方法**：
1. **核的渐近分析**：Bochner-Riesz 核 $K_R^\delta(x)$ 可以通过 Bessel 函数计算，其渐近行为决定了算子的性质。
2. **Littlewood-Paley 分解**：将乘子在频率空间二进分解，在每个二进块上利用不同的估计方法。
3. **插值方法**：结合 $L^2$ 有界性和端点估计，通过复插值或实插值得到中间 $L^p$ 的有界性。

## 三、定理的严格表述

**定义（Bochner-Riesz 平均）**：设 $\delta \ge 0$，$R > 0$。$\delta$ 阶 Bochner-Riesz 平均定义为
$$T_R^\delta f(x) = \int_{\mathbb{R}^n} \left(1 - \frac{|\xi|^2}{R^2}\right)_+^\delta \hat{f}(\xi) e^{2\pi i x \cdot \xi}\, d\xi,$$
其中 $(t)_+ = \max(t, 0)$。等价地，$T_R^\delta f = K_R^\delta * f$，其中
$$K_R^\delta(x) = R^n \int_{\mathbb{R}^n} (1 - |\eta|^2)_+^\delta e^{2\pi i R x \cdot \eta}\, d\eta.$$

**定理 1（Bochner-Riesz 核的显式表达）**：
$$K^\delta(x) = \frac{\pi^{-\delta} \Gamma(\delta+1)}{|x|^{\delta + n/2}} J_{\delta + n/2}(2\pi|x|),$$
其中 $J_\nu$ 是第一类 Bessel 函数。其渐近行为为：
$$K^\delta(x) \sim \begin{cases} C, & |x| \to 0, \\ |x|^{-(\delta + (n+1)/2)}, & |x| \to \infty. \end{cases}$$

**定理 2（经典充分条件——Bochner-Riesz 定理）**：设 $n \ge 2$，$1 \le p \le \infty$。若
$$\delta > n\left|\frac{1}{p} - \frac{1}{2}\right| - \frac{1}{2},$$
则存在常数 $C_{p,\delta}$ 使得对所有 $R > 0$，
$$\|T_R^\delta f\|_{L^p} \le C_{p,\delta} \|f\|_{L^p}.$$

**定理 3（Fefferman 球乘子定理）**：设 $n \ge 2$，$p \ne 2$，$1 \le p \le \infty$。则球乘子 $\chi_{B(0,R)}$ 对应的算子 $S_R$ 在 $L^p(\mathbb{R}^n)$ 上不是一致有界的，即
$$\sup_{R > 0}\|S_R f\|_{L^p} = \infty \quad (\text{对某些 } f \in L^p).$$

**猜想（Bochner-Riesz 猜想）**：设 $n \ge 2$，$1 \le p \le \infty$，$p \ne 2$。$T_R^\delta$ 在 $L^p(\mathbb{R}^n)$ 上一致有界当且仅当
$$\delta > \delta(p) := \max\left\{n\left|\frac{1}{p} - \frac{1}{2}\right| - \frac{1}{2}, 0\right\}.$$

等价地，在 $(1/p, \delta)$ 平面上，有界性区域为以 $(1/2, 0)$ 为顶点、斜率为 $\pm n$ 的锥形区域与 $\delta \ge 0$ 半平面的交集。

## 四、证明过程

**Bochner 充分性定理的证明概要**：

**第一步：核的估计。**

由 Bessel 函数的渐近展开，Bochner-Riesz 核满足
$$|K^\delta(x)| \le C(1 + |x|)^{-(\delta + (n+1)/2)}.$$

当 $\delta + (n+1)/2 > n$，即 $\delta > (n-1)/2$ 时，$K^\delta \in L^1(\mathbb{R}^n)$，由 Young 不等式直接得到 $L^p$ 有界性对所有 $p$ 成立。

**第二步：$L^2$ 有界性。**

由 Plancherel 定理，$\|T_R^\delta f\|_2 \le \|m_R^\delta\|_\infty \|f\|_2 \le \|f\|_2$（因为 $|m_R^\delta| \le 1$）。

**第三步：$L^1$ 端点估计。**

将核分解为 $K^\delta = K^\delta_{\text{near}} + K^\delta_{\text{far}}$，其中 $K^\delta_{\text{near}}$ 支在 $|x| \le 1$ 上，$K^\delta_{\text{far}}$ 支在 $|x| > 1$ 上。

$K^\delta_{\text{near}}$ 有界，其 $L^1$ 范数有限。$K^\delta_{\text{far}}$ 利用衰减估计：
$$\|K^\delta_{\text{far}}\|_{L^1} \le C \int_1^\infty r^{-(\delta + (n+1)/2)} r^{n-1}\,dr = C \int_1^\infty r^{n-1-\delta-(n+1)/2}\,dr.$$

此积分收敛当 $n - 1 - \delta - (n+1)/2 < -1$，即 $\delta > (n-1)/2$。

但我们需要更精细的估计。利用 $K^\delta$ 的振荡性质（来自 Bessel 函数的振荡），通过稳相法可以更精确地估计 $K^\delta$ 的 $L^1$ 范数，得到 $\|K^\delta\|_{L^1} \le C$ 当 $\delta > (n-1)/2$。

**第四步：插值。**

由 $L^2$ 有界性和 $\|K^\delta\|_{L^1} \le C$（$\delta > (n-1)/2$ 时）的 $L^1$ 有界性，通过 Riesz-Thorin 插值得到 $L^p$ 有界性。

更精细的论证利用 $K^\delta$ 的 $L^q$ 范数估计和 Hardy-Littlewood-Sobolev 型不等式，通过插值将条件推广到 $\delta > n|1/p - 1/2| - 1/2$。$\square$

**Fefferman 球乘子定理的证明思路**：

Fefferman 的证明利用了 Knapp 例子。构造测试函数 $f$ 使得 $\hat{f}$ 支在一个细长的椭球体内（沿球面的一个法线方向拉长），使得 $S_R f$ 的 $L^p$ 范数在 $p \ne 2$ 时发散。

具体地，设 $\hat{f}(\xi) = \chi_E(\xi)$，其中 $E = \{\xi : |\xi_1 - R| \le 1, |\xi'| \le R^{-1/2}\}$（$\xi' = (\xi_2, \ldots, \xi_n)$）。则 $|E| \sim R^{-(n-1)/2}$。

通过计算 $S_R f$ 在适当区域上的下界和 $f$ 的 $L^p$ 范数的上界，可以证明当 $p \ne 2$ 时，$\|S_R f\|_p / \|f\|_p \to \infty$（$R \to \infty$）。$\square$

## 五、应用与意义

1. **Fourier 级数的收敛性**：Bochner-Riesz 平均是研究 Fourier 级数和 Fourier 积分收敛性的基本工具。在 $L^p$ 空间中，Bochner-Riesz 平均提供了比简单部分和更好的收敛行为。

2. **调和分析的核心未解决问题**：Bochner-Riesz 猜想是调和分析中最著名的开放问题之一。它在 $n = 2$ 时已由 Carleson 和 Sjölin（1971）以及后续工作基本解决，但在高维情形仍然困难。

3. **与 Kakeya 猜想的联系**：Bochner-Riesz 猜想的解决与 Kakeya 猜想和限制性猜想有深刻的联系。三者构成了现代调和分析中"限制性理论"的核心。

4. **偏微分方程**：Bochner-Riesz 平均与波动方程和 Schrödinger 方程的解的正则性有关。Bochner-Riesz 算子的 $L^p$ 有界性等价于相应演化方程的局部光滑性估计。

5. **几何测度论**：Bochner-Riesz 核的渐近行为与球面的曲率密切相关，这使得该问题与几何测度论中的限制性问题自然联系。

6. **最新进展**：Bourgain (1991) 利用双线性方法取得了突破性进展；Tao (2002) 利用多项式方法进一步改善了结果。目前 $n \ge 3$ 时的最佳结果仍然与猜想有差距。
