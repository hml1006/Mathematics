# Fourier 乘子定理（Mikhlin 乘子定理）

> **一句话大白话**：在频域给函数"乘上一个频率函数"（乘子）再变回来，这种做法在时间空间的很多范数下是"温和有界"的——只要这个频率函数满足一定光滑与衰减条件，就不用担心把信号放大到失控。
>
> **小例子**：$Tf$ 满足 $\widehat{Tf}(\xi)=m(\xi)\hat f(\xi)$，Mikhlin 定理说若 $|\xi^{|\alpha|}\partial^\alpha m(\xi)|\le C$ 对 $|\alpha|\le\lfloor n/2\rfloor+1$ 成立，则 $T$ 在 $L^p$（$1<p<\infty$）上有界——"光滑且衰减的乘子不会破坏 $L^p$ 范数"。

## 一、定理介绍

Fourier 乘子理论研究的是：给定一个有界函数 $m(\xi)$，定义算子 $T_m f = \mathcal{F}^{-1}[m \cdot \hat{f}]$，问 $T_m$ 在 $L^p$ 空间上是否有界？这样的 $m$ 称为 $L^p$ 乘子。

Mikhlin 乘子定理（1956年）给出了 $L^p$（$1 < p < \infty$）乘子的充分条件：若 $m(\xi)$ 满足适当的光滑性和衰减条件（对各阶导数的控制），则 $m$ 是 $L^p$ 乘子。这个定理统一并推广了许多经典结果（如 Riesz 变换的 $L^p$ 有界性），是现代调和分析中最实用的工具之一。

Mikhlin 定理的意义在于，它将算子的 $L^p$ 有界性问题转化为对其 Fourier 符号（symbol）的点态估计问题，极大地简化了偏微分方程中各类算子的分析。

## 二、原理思路

**基本设定**：算子 $T_m$ 在物理空间中是卷积算子 $T_m f = K * f$，其中 $K = \check{m}$（$m$ 的逆 Fourier 变换）。当 $m$ 是光滑函数时，$K$ 一般不是 $L^1$ 函数（否则 $T_m$ 的有界性由 Young 不等式直接得到），但 $K$ 可能是一个奇异积分核。

**与奇异积分的联系**：Mikhlin 定理本质上可以归结为 Calderón-Zygmund 理论。若 $m(\xi)$ 满足 Mikhlin 条件，则其逆 Fourier 变换 $K(x)$ 满足：
- $|K(x)| \le C/|x|^n$（大小条件）；
- $|\nabla K(x)| \le C/|x|^{n+1}$（光滑性条件）。

因此 $T_m$ 是一个 Calderón-Zygmund 奇异积分算子，由 Calderón-Zygmund 定理得到 $L^p$ 有界性。

**证明策略**：

1. **Littlewood-Paley 分解方法**：将频率空间二进分解，$m(\xi) = \sum_j m(\xi)\varphi(2^{-j}\xi)$。在每个二进环上，$m$ 近似为一个常数（由导数条件保证），因此 $T_m$ 在每个频率块上近似为恒等算子的倍数。

2. **核的估计**：利用 Littlewood-Paley 分解和导数条件，估计 $K(x)$ 的大小和光滑性，将其分解为"好部分"和"奇异部分"。

3. **应用 Calderón-Zygmund 理论**：验证 $K$ 满足 Hörmander 条件，然后直接应用 Calderón-Zygmund 定理。

**关键洞察**：Mikhlin 条件 $|\partial^\alpha m(\xi)| \le C|\xi|^{-|\alpha|}$ 的标度不变性是关键——它与二进分解自然匹配。

## 三、定理的严格表述

**定理（Mikhlin 乘子定理）**：设 $m: \mathbb{R}^n \setminus \{0\} \to \mathbb{C}$ 是局部有界且局部 Lipschitz 连续的函数。假设存在常数 $C > 0$ 使得对所有满足 $|\alpha| \le [n/2] + 1$ 的多重指标 $\alpha$，
$$|\partial^\alpha m(\xi)| \le C |\xi|^{-|\alpha|}, \quad \forall \xi \ne 0. \tag{M}$$

则 $m$ 是 $L^p(\mathbb{R}^n)$ 乘子，即算子 $T_m$ 定义为
$$T_m f(x) = \mathcal{F}^{-1}[m(\xi)\hat{f}(\xi)](x)$$
可以延拓为 $L^p(\mathbb{R}^n)$ 上的有界线性算子，对任意 $1 < p < \infty$，存在 $C_p > 0$ 使得
$$\|T_m f\|_{L^p} \le C_p \|f\|_{L^p}, \quad \forall f \in L^p(\mathbb{R}^n).$$

常数 $C_p$ 仅依赖于 $n, p$ 和条件 (M) 中的常数 $C$。

**注记**：
- 条件中 $|\alpha| \le [n/2] + 1$ 阶导数的要求是最优的（在 Mikhlin 原始论文中）。Hörmander 后来将其改进为 $|\alpha| \le [n/2] + 1$ 且用 $L^2$ 平均条件替代点态条件。
- 当 $n = 1$ 时，需要 $|\alpha| \le 1$，即只需 $|m(\xi)| \le C$ 和 $|m'(\xi)| \le C/|\xi|$。

**推论 1（Riesz 变换的 $L^p$ 有界性）**：Riesz 变换 $R_j$ 的 Fourier 符号为 $m(\xi) = -i\xi_j/|\xi|$。直接验证：
$$\partial_{\xi_k} \frac{\xi_j}{|\xi|} = \frac{\delta_{jk}}{|\xi|} - \frac{\xi_j\xi_k}{|\xi|^3},$$
满足 $|\partial^\alpha m(\xi)| \le C_\alpha |\xi|^{-|\alpha|}$。由 Mikhlin 定理，$R_j$ 在 $L^p$ 上有界，$1 < p < \infty$。

**推论 2（分数次 Laplacian）**：算子 $(-\Delta)^{s/2}$ 的符号为 $|\xi|^s$。虽然它不满足 Mikhlin 条件（因为 $|m(\xi)| = |\xi|^s$ 无界），但 $(-\Delta)^{s/2}(I - \Delta)^{-s/2}$ 的符号为 $|\xi|^s/(1+|\xi|^2)^{s/2}$ 满足 Mikhlin 条件，因此该算子在 $L^p$ 上有界。

## 四、证明过程

**第一步：Littlewood-Paley 分解。**

选取径向函数 $\varphi \in C_c^\infty(\mathbb{R}^n)$，$\text{supp}\,\varphi \subset \{1/2 \le |\xi| \le 2\}$，使得 $\sum_{j \in \mathbb{Z}} \varphi(2^{-j}\xi) = 1$（$\xi \ne 0$）。令 $m_j(\xi) = m(\xi)\varphi(2^{-j}\xi)$，$K_j = \check{m}_j$。则
$$T_m f = \sum_{j \in \mathbb{Z}} K_j * f.$$

**第二步：估计 $K_j$。**

令 $K_j(x) = \int_{\mathbb{R}^n} m_j(\xi) e^{2\pi i x \cdot \xi}\, d\xi$。由于 $m_j$ 支在 $2^{j-1} \le |\xi| \le 2^{j+1}$ 上，通过变量替换 $\xi = 2^j \eta$：
$$K_j(x) = 2^{jn} \int m(2^j\eta)\varphi(\eta) e^{2\pi i 2^j x \cdot \eta}\, d\eta.$$

利用 $m$ 的导数条件和分部积分，可以证明：
$$|K_j(x)| \le C_N 2^{jn}(1 + 2^j|x|)^{-N}, \quad \forall N > 0.$$

具体地，利用 Laplacian $(1 - \Delta_\eta)^M$ 作用产生 $(1 + |2^j x|^2)^{-M}$ 的衰减。导数条件 $|\partial^\alpha m(2^j\eta)| \le C 2^{-j|\alpha|}$ 与 $\varphi$ 的紧支集相结合，给出一致估计。

**第三步：核的全局估计。**

令 $K(x) = \sum_j K_j(x)$。对 $x \ne 0$，将求和分为两部分：
- 当 $2^j \le 1/|x|$ 时（低频部分）：利用 $|K_j(x)| \le C 2^{jn}$，这部分贡献 $\lesssim |x|^{-n}$。
- 当 $2^j > 1/|x|$ 时（高频部分）：利用快速衰减 $|K_j(x)| \le C_N 2^{jn}(2^j|x|)^{-N}$，取 $N$ 充分大，这部分也 $\lesssim |x|^{-n}$。

因此 $|K(x)| \le C/|x|^n$。

**第四步：验证 Hörmander 条件。**

类似地估计 $\nabla K(x)$：
$$|\nabla K_j(x)| \le C_N 2^{j(n+1)}(1 + 2^j|x|)^{-N}.$$

对 $|x| > 2|y|$，
$$\int_{|x|>2|y|} |K(x-y) - K(x)|\,dx \le |y| \int_{|x|>2|y|} |\nabla K(x)|\,dx.$$

将积分区域按 $|x| \sim 2^k$ 分层，利用 $|\nabla K(x)| \le C/|x|^{n+1}$，得到
$$|y| \int_{|x|>2|y|} \frac{1}{|x|^{n+1}}\,dx \le C.$$

因此 $K$ 满足 Hörmander 条件。

**第五步：应用 Calderón-Zygmund 定理。**

$T_m$ 的核 $K$ 满足 $|K(x)| \le C/|x|^n$ 和 Hörmander 条件。由 Mikhlin 条件中的 $L^\infty$ 界 $|m(\xi)| \le C$（$|\alpha| = 0$ 的情形），$T_m$ 在 $L^2$ 上有界（由 Plancherel 定理）。

由 Calderón-Zygmund 定理，$T_m$ 是弱 (1,1) 型的，且对 $1 < p < \infty$ 在 $L^p$ 上有界。$\square$

## 五、应用与意义

1. **偏微分方程的先验估计**：Mikhlin 定理是建立椭圆方程 $L^p$ 估计的核心工具。例如，对椭圆算子 $L = \sum a_{jk}\partial_j\partial_k$，其二阶导数 $\partial_j\partial_k L^{-1}$ 的 Fourier 符号满足 Mikhlin 条件，因此 $L^p$ 有界。

2. **Bochner-Riesz 乘子**：虽然 Bochner-Riesz 乘子 $(1 - |\xi|^2)_+^\delta$ 在原点不光滑，Mikhlin 定理为研究其 $L^p$ 有界性提供了基本框架。

3. **谱乘子**：在紧 Lie 群或对称空间上，Laplacian 的谱乘子 $m(\Delta)$ 的 $L^p$ 有界性可以通过 Mikhlin 型条件来研究（Hörmander 谱乘子定理）。

4. **时频分析**：Mikhlin 定理的变体（如 Hörmander-Mikhlin 定理）在时频分析中用于研究伪微分算子的有界性。

5. **非线性 PDE**：在非线性色散方程的研究中，分数次链式法则（fractional chain rule）和乘子估计依赖于 Mikhlin 定理的推广形式。

6. **最优性**：Mikhlin 条件在某种意义上是最优的。Marcinkiewicz 乘子定理给出了更弱的条件（对每个变量的分离导数估计），而 Hörmander 的 $L^2$ 平均条件进一步推广了 Mikhlin 定理。
