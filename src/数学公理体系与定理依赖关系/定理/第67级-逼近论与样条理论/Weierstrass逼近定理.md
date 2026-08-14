# Weierstrass 逼近定理

## 一、定理介绍

Weierstrass 逼近定理是逼近论中最基本、最重要的结果之一。它断言：闭区间上的任意连续函数都可以用多项式一致逼近到任意精度。这一结果建立了多项式函数在连续函数空间中的稠密性，说明多项式虽然形式简单，却具有极强的表达能力。

该定理由 Karl Weierstrass 于 1885 年证明，是函数逼近理论的奠基性定理。它不仅从理论上保证了多项式逼近的可能性，也为数值分析、计算机辅助几何设计、信号处理等领域提供了坚实基础。

## 二、原理思路

Weierstrass 逼近定理的核心思想是：通过构造一列多项式（或其他简单函数），使其在闭区间上一致收敛于目标连续函数。常见的证明思路包括：

1. **Bernstein 多项式构造法**：对 $[0,1]$ 上的连续函数 $f$，定义 Bernstein 多项式
   $$
   B_n(f;x) = \sum_{k=0}^{n} f\left(\frac{k}{n}\right) \binom{n}{k} x^k (1-x)^{n-k},
   $$
   利用概率论中大数定律的思想证明 $B_n(f;x)$ 一致收敛到 $f(x)$。

2. **卷积光滑化方法**：用一族多项式核函数与 $f$ 做卷积，得到光滑逼近。

3. **先逼近折线函数**：连续函数可用折线函数一致逼近，而折线函数又可表示为一次样条，进一步用多项式逼近每个线性片段。

其中 Bernstein 构造法最为经典，它同时给出了显式逼近多项式。

## 三、定理的严格表述

**定理（Weierstrass 逼近定理）**：设 $f$ 是闭区间 $[a,b]$ 上的连续函数，则对任意 $\varepsilon > 0$，存在多项式 $P(x)$，使得
$$
\sup_{x \in [a,b]} |f(x) - P(x)| < \varepsilon.
$$
等价地说，多项式空间 $\mathcal{P}[a,b]$ 在 $C[a,b]$ 中关于上确界范数 $\|\cdot\|_\infty$ 是稠密的。

**推论（复值情形）**：若 $f \in C([a,b];\mathbb{C})$，则同样存在复系数多项式一致逼近 $f$。

## 四、证明过程

下面采用 Bernstein 多项式的方法证明 $[0,1]$ 上的情形，一般区间 $[a,b]$ 可通过线性变换得到。

**证明**：

设 $f \in C[0,1]$。定义 $f$ 的 $n$ 次 Bernstein 多项式为
$$
B_n(f;x) = \sum_{k=0}^{n} f\left(\frac{k}{n}\right) \binom{n}{k} x^k (1-x)^{n-k}, \quad x \in [0,1].
$$

记 $p_{n,k}(x) = \binom{n}{k} x^k(1-x)^{n-k}$。熟知恒等式：
$$
\sum_{k=0}^{n} p_{n,k}(x) = 1,
$$
$$
\sum_{k=0}^{n} \left(k - nx\right)^2 p_{n,k}(x) = nx(1-x).
$$

对任意 $\varepsilon > 0$，由 $f$ 在 $[0,1]$ 上一致连续，存在 $\delta > 0$，使得当 $|x-y| < \delta$ 时 $|f(x)-f(y)| < \varepsilon/2$。设 $M = \|f\|_\infty$。

估计差值：
$$
|f(x) - B_n(f;x)| = \left| \sum_{k=0}^{n} \left(f(x) - f\left(\frac{k}{n}\right)\right) p_{n,k}(x) \right|.
$$

将求和按 $|k/n - x|$ 分为两部分。当 $|k/n - x| < \delta$ 时，
$$
\left|f(x) - f\left(\frac{k}{n}\right)\right| < \frac{\varepsilon}{2}.
$$

当 $|k/n - x| \geq \delta$ 时，利用切比雪夫不等式思想：
$$
\left|f(x) - f\left(\frac{k}{n}\right)\right| \leq 2M \leq \frac{2M}{\delta^2}\left(\frac{k}{n} - x\right)^2.
$$

因此
$$
|f(x) - B_n(f;x)| \leq \frac{\varepsilon}{2} \sum_{k=0}^{n} p_{n,k}(x) + \frac{2M}{\delta^2} \sum_{k=0}^{n} \left(\frac{k}{n} - x\right)^2 p_{n,k}(x).
$$

由于 $\sum p_{n,k}(x) = 1$，且
$$
\sum_{k=0}^{n} \left(\frac{k}{n} - x\right)^2 p_{n,k}(x) = \frac{x(1-x)}{n} \leq \frac{1}{4n},
$$

得到
$$
|f(x) - B_n(f;x)| \leq \frac{\varepsilon}{2} + \frac{M}{2n\delta^2}.
$$

取 $N > \dfrac{M}{\varepsilon \delta^2}$，则当 $n \geq N$ 时对所有 $x \in [0,1]$ 有
$$
|f(x) - B_n(f;x)| < \varepsilon.
$$

对一般区间 $[a,b]$，令 $t = \dfrac{x-a}{b-a}$，将 $f(x)$ 转化为 $g(t) = f(a + (b-a)t) \in C[0,1]$，再用上述多项式逼近即可。

**证毕**。

## 五、应用与意义

1. **理论基础**：Weierstrass 定理说明多项式在连续函数空间中稠密，是逼近论、数值分析许多后续结果（如 Jackson 定理、Bernstein 定理）的出发点。

2. **数值计算**：为函数的数值逼近、积分近似、微分方程谱方法等提供了理论依据。虽然高次多项式全局逼近可能产生 Runge 现象，但分片低次多项式（样条）能有效克服。

3. **概率与统计**：Bernstein 多项式证明本身揭示了大数定律与函数逼近之间的深刻联系，在概率论中有广泛应用。

4. **计算机图形学**：Bezier 曲线正是基于 Bernstein 多项式，是计算机辅助几何设计（CAGD）的核心工具。

5. **泛函分析**：该定理可推广为 Stone-Weierstrass 定理，刻画了一般紧 Hausdorff 空间上连续函数代数的稠密子代数，是泛函分析中的经典结果。
