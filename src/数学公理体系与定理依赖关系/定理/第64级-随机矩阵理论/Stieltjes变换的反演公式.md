# Stieltjes 变换的反演公式

> **一句话大白话**：想知道未知的谱分布长什么样，就在复平面上"取样"它的 Stieltjes 变换，再从上方向实轴贴近取虚部——虚部在实轴上的极限直接还原出原来的密度。
>
> **小例子**：半圆律的 Stieltjes 变换为 $m(z)=\frac{-z+\sqrt{z^2-4}}{2}$，取 $z=x+i\varepsilon$ 并令 $\varepsilon\to0^+$，则 $\frac1\pi\operatorname{Im}m(x+i0^+)=\frac{1}{2\pi}\sqrt{4-x^2}$，正是 $[-2,2]$ 上的半圆密度。

## 一、定理介绍

> **前置依赖**：有限 Borel 测度与弱收敛、上半平面解析函数与 Cauchy 积分、Poisson 核与近似恒等核、$\frac{1}{u-z}$ 的实虚部分解、控制收敛定理与 Fubini 定理。

Stieltjes 变换（又称 Cauchy 变换或预解式）是随机矩阵理论中沟通"经验谱分布"与"矩阵预解式"的桥梁：对谱测度 $\mu$，其 Stieltjes 变换定义为

$$
m(z)=\int_{\mathbb R}\frac{d\mu(x)}{x-z},\qquad z\in\mathbb C\setminus\mathbb R .
$$

它的重要性在于两点：其一，换元后 $m(z)$ 恰是矩阵预解式 $(W-zI)^{-1}$ 的归一化迹，因而热力学与组合方法可以直接计算；其二，$m$ 作为上半平面上的解析函数，其边界值完整编码了 $\mu$。反演公式正是把"$m$ 的虚部边界值"还原为"$\mu$ 的密度"的桥梁，是推导 Wigner 半圆律、Marchenko–Pastur 律以及各类极限谱密度的标准最后一步。

## 二、原理思路

关键是一个初等恒等式。对 $x\in\mathbb R$、$\varepsilon>0$，把复数 $\frac{1}{x-z}$ 写成实部与虚部：

$$
\frac{1}{x-(u+i\varepsilon)}=\frac{x-u}{(x-u)^2+\varepsilon^2}+i\,\frac{\varepsilon}{(x-u)^2+\varepsilon^2}.
$$

右端的虚部

$$
P_\varepsilon(x-u)=\frac{\varepsilon}{(x-u)^2+\varepsilon^2}
$$

正是上半平面 Poisson 核。它满足 $\int_{\mathbb R}P_\varepsilon(t)\,dt=\pi$，且当 $\varepsilon\to0^+$ 时质量集中到原点，故 $P_\varepsilon/\pi$ 构成一对近似恒等核（good kernel）。因此对测度 $\mu$ 作"卷积"$\operatorname{Im}m(x+i\varepsilon)=\int P_\varepsilon(x-u)\,d\mu(u)$ 后，令 $\varepsilon\to0^+$ 就恢复出 $\mu$。反过来，若已知 Stieltjes 变换而想求密度，只需取虚部并除以 $\pi$。

## 三、定理的严格表述

设 $\mu$ 为 $\mathbb R$ 上的有限 Borel 测度，其 Stieltjes 变换为

$$
m(z)=\int_{\mathbb R}\frac{d\mu(x)}{x-z},\qquad z\in\mathbb C\setminus\mathbb R .
$$

则 $m$ 在上半平面 $\{\operatorname{Im}z>0\}$ 内解析，且 $\operatorname{Im}m(z)>0$（Nevanlinna 性质）。反演公式有以下三种等价形式。

**定理（Stieltjes–Perron 反演公式，区间形式）.** 对任意 $a<b$，若 $a,b$ 均为 $\mu$ 的连续点（即 $\mu(\{a\})=\mu(\{b\})=0$），则

$$
\mu\bigl((a,b)\bigr)=\frac{1}{\pi}\lim_{\varepsilon\to0^+}\int_a^b \operatorname{Im}m(x+i\varepsilon)\,dx .
$$

**定理（密度形式）.** 若 $\mu$ 有界且关于 Lebesgue 测度绝对连续，密度为 $\rho\in L^1(\mathbb R)$，则在 $\rho$ 的 Lebesgue 连续点 $x$ 处

$$
\rho(x)=\frac{1}{\pi}\lim_{\varepsilon\to0^+}\operatorname{Im}m(x+i\varepsilon)
=\frac{1}{\pi}\lim_{\varepsilon\to0^+}\int_{\mathbb R}\frac{\varepsilon\,d\mu(u)}{(x-u)^2+\varepsilon^2}.
$$

**定理（弱反演形式）.** 对任意有界连续函数 $f:\mathbb R\to\mathbb R$，

$$
\int_{\mathbb R}f\,d\mu=\frac{1}{\pi}\lim_{\varepsilon\to0^+}\int_{\mathbb R}f(x)\,\operatorname{Im}m(x+i\varepsilon)\,dx .
$$

由此得到唯一性：若两个有限测度的 Stieltjes 变换在上半平面相等，则两个测度相等。

## 四、证明过程

**步骤 1：写出 Stieltjes 变换的虚部.** 对 $z=x+i\varepsilon$ 与实变量 $u$，

$$
\frac{1}{u-z}=\frac{1}{u-x-i\varepsilon}
=\frac{u-x+i\varepsilon}{(u-x)^2+\varepsilon^2}.
$$

对测度积分，得

$$
\operatorname{Im}m(x+i\varepsilon)=\int_{\mathbb R}\frac{\varepsilon\,d\mu(u)}{(u-x)^2+\varepsilon^2}
=\bigl(P_\varepsilon*\mu\bigr)(x),
$$

其中 $P_\varepsilon(t)=\frac{\varepsilon}{t^2+\varepsilon^2}$。这步是全部论证的出发点：虚部恰是 Poisson 核关于 $\mu$ 的卷积。

**步骤 2：Poisson 核是近似恒等核.** 直接计算

$$
\int_{\mathbb R}P_\varepsilon(t)\,dt=\Bigl[\arctan\frac{t}{\varepsilon}\Bigr]_{-\infty}^{+\infty}=\pi ,
$$

且对任意 $\delta>0$，

$$
\sup_{|t|\ge\delta}P_\varepsilon(t)=\frac{\varepsilon}{\delta^2+\varepsilon^2}\le\frac{\varepsilon}{\delta^2}\xrightarrow{\varepsilon\to0^+}0 .
$$

于是 $P_\varepsilon/\pi$ 是标准的近似恒等核：总质量恒为 $1$，且质量在原点外一致趋于零。

**步骤 3：弱收敛.** 设 $f$ 有界连续。由 Fubini 定理（$f$ 有界、$\mu$ 有限、$P_\varepsilon$ 可积），

$$
\frac{1}{\pi}\int_{\mathbb R}f(x)\operatorname{Im}m(x+i\varepsilon)\,dx
=\int_{\mathbb R}\left(\frac{1}{\pi}\int_{\mathbb R}f(x)P_\varepsilon(x-u)\,dx\right)d\mu(u).
$$

记内层积分为 $f_\varepsilon(u)$。对固定的 $u$，由近似恒等核的基本收敛定理（先对 $u$ 的一个邻域用中值估计，邻域外由步骤 2 的衰减控制）得

$$
f_\varepsilon(u)=\frac{1}{\pi}\int_{\mathbb R}f(x)P_\varepsilon(x-u)\,dx
\xrightarrow{\varepsilon\to0^+}f(u).
$$

同时 $|f_\varepsilon(u)|\le\|f\|_\infty$，与 $\varepsilon$ 无关。由控制收敛定理（以常函数 $\|f\|_\infty$ 为控制函数，对测度 $\mu$ 可积），

$$
\frac{1}{\pi}\int_{\mathbb R}f(x)\operatorname{Im}m(x+i\varepsilon)\,dx
=\int_{\mathbb R}f_\varepsilon(u)\,d\mu(u)
\xrightarrow{\varepsilon\to0^+}\int_{\mathbb R}f\,d\mu .
$$

这就是弱反演形式，也是密度形式的核心。

**步骤 4：区间形式.** 取 $f=\mathbf 1_{(a,b)}$。先用有界连续函数 $f_n$ 满足 $0\le f_n\le1$ 且 $f_n\uparrow\mathbf 1_{(a,b)}$（或分别逼近开区间与 $\mu$-零集）去逼近。由步骤 3 对每个 $f_n$ 成立，再令 $n\to\infty$；因 $a,b$ 是 $\mu$ 的连续点，$\int f_n\,d\mu\to\mu((a,b))$。左端同理，交换两个极限（单调性保证）得

$$
\mu\bigl((a,b)\bigr)=\frac{1}{\pi}\lim_{\varepsilon\to0^+}\int_a^b\operatorname{Im}m(x+i\varepsilon)\,dx .
$$

**步骤 5：密度形式.** 设 $\mu$ 的密度为 $\rho$。由步骤 1，

$$
\operatorname{Im}m(x+i\varepsilon)=\int_{\mathbb R}P_\varepsilon(x-u)\rho(u)\,du
=\pi\,(P_\varepsilon/\pi*\rho)(x).
$$

由近似恒等核的 Lebesgue 点收敛定理，在 $\rho$ 的 Lebesgue 连续点 $x$ 处，右端趋于 $\pi\rho(x)$。除以 $\pi$ 即得

$$
\rho(x)=\frac{1}{\pi}\lim_{\varepsilon\to0^+}\operatorname{Im}m(x+i\varepsilon).
$$

**步骤 6：唯一性.** 若 $m_{\mu_1}=m_{\mu_2}$ 于上半平面，则由步骤 3 对一切有界连续 $f$ 有 $\int f\,d\mu_1=\int f\,d\mu_2$，由 Riesz 表示定理的弱收敛唯一性得 $\mu_1=\mu_2$。这保证了"由极限 Stieltjes 变换反推极限谱分布"的做法是合法的。$\square$

**注（解析性与 Nevanlinna 性质）.** $m$ 的解析性来自 $\frac{1}{x-z}$ 在 $z\notin\mathbb R$ 上解析且积分绝对收敛。$\operatorname{Im}m(z)=\int\frac{\operatorname{Im}z}{|x-z|^2}\,d\mu(x)>0$ 当 $\operatorname{Im}z>0$，故 $m$ 是从上半平面到上半平面的解析函数，这保证了边界值反演的存在性（Fatou 定理与 Herglotz 表示）。

## 五、应用与意义

- **极限谱密度**：Wigner 半圆律、Marchenko–Pastur 律、自由卷积与自由中心极限定理的密度都由 Stieltjes 变换的自洽方程解出后用反演公式还原。
- **预解式方法**：随机矩阵的局部律、Green 函数比较（Lindeberg 替换法）都以 $m(z)$ 与 $G(z)=(W-zI)^{-1}$ 的对应为出发点。
- **自由概率论**：Stieltjes 变换即 Cauchy 变换，与 R 变换、S 变换一起构成自由概率的"特征函数"体系，反演公式给出测度与变换的双向对应。
- **正交多项式与连分数**：Stieltjes 变换是测度的连分数展开（J 分式）与正交多项式递推系数的编码，反演公式沟通矩问题与谱测度。

## 课堂问答

**老师**：反演公式为什么长成取虚部除以 $\pi$ 这样？

**学生**：因为对 $z=x+i\varepsilon$ 有 $\frac{1}{u-z}=\frac{u-x}{(u-x)^2+\varepsilon^2}+i\frac{\varepsilon}{(u-x)^2+\varepsilon^2}$，虚部恰是 Poisson 核 $P_\varepsilon(x-u)=\frac{\varepsilon}{(x-u)^2+\varepsilon^2}$。于是 $\operatorname{Im}m(x+i\varepsilon)=\int P_\varepsilon(x-u)\,d\mu(u)=(P_\varepsilon*\mu)(x)$，而 $P_\varepsilon/\pi$ 是近似恒等核，$\varepsilon\to0^+$ 时恢复出 $\mu$，故 $\rho(x)=\frac1\pi\lim_{\varepsilon\to0^+}\operatorname{Im}m(x+i\varepsilon)$。

**老师（追问）**：为什么 $P_\varepsilon/\pi$ 是好核，它满足哪两条？

**学生**：两条：其一，$\int_{\mathbb R}P_\varepsilon(t)\,dt=\pi$，即归一化后总质量为 $1$；其二，对任意 $\delta>0$，$\sup_{|t|\ge\delta}P_\varepsilon(t)\le\varepsilon/\delta^2\to0$，即质量在原点外一致消失。有了这两条，由 Fubini 与控制收敛定理，$\frac1\pi\int f\operatorname{Im}m(x+i\varepsilon)\,dx\to\int f\,d\mu$ 对一切有界连续 $f$ 成立，这就是弱反演形式。

**老师（拓展）**：这条反演为什么是随机矩阵推导的最后一步？

**学生**：因为自洽方程只解出 Stieltjes 变换 $m(z)$，要得到谱密度必须靠它反演。半圆律、Marchenko–Pastur 律、自由卷积都走这条路。它还给出唯一性：若两个有限测度的 Stieltjes 变换在上半平面相等则测度相等，这保证了由极限 $m$ 反推极限谱分布是合法的。常见误区是把 $\varepsilon\to0$ 与 $N\to\infty$ 的次序搞混，应先在有限 $N$ 下对固定 $z$ 取值，再令 $\varepsilon\to0^+$。
