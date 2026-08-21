# Riemann Zeta 函数的函数方程

> **一句话大白话**：Zeta 函数看似只在 $\operatorname{Re}(s)>1$ 上有定义，但它能被"无缝延伸"到整个复平面（除 $s=1$ 外），且满足对称的自我指涉方程 $\zeta(s)=2^s\pi^{s-1}\sin\frac{\pi s}{2}\,\Gamma(1-s)\,\zeta(1-s)$——左边与右边隔着"对折 $s\leftrightarrow1-s$"。
>
> **小例子**：函数方程把"整值" $\zeta(2)=\frac{\pi^2}{6}$ 与"半值" $\zeta(-1)$ 联系起来：由方程可算出 $\zeta(-1)=-\frac{1}{12}$，这个"几乎天方夜谭"的值正是方程与平凡零点结构的推论。

## 一、定理介绍

> **前置依赖**：Gamma 函数及其积分表示、Theta 函数、Poisson 求和公式、解析延拓。

函数方程是 Zeta 函数最深层的结构性质之一，由 Riemann 于 1859 年给出。它说明"完备化"的 Zeta 函数 $\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ 关于直线 $\operatorname{Re}(s)=\frac12$ 对称。该方程同时给出了 $\zeta(s)$ 的解析延拓：由右侧的 $\Gamma$ 与 $\sin$ 因子，右半平面可向左延拓，从而得到整函数（除 $s=1$ 处的简单极点）。

## 二、原理思路

关键的桥梁是 Theta 函数 $\theta(t)=\sum_{n=-\infty}^{\infty}e^{-\pi n^2 t}$。由 Poisson 求和公式得 $\theta$ 的变换公式 $\theta(t)=\frac1{\sqrt t}\theta(1/t)$（"娘梅顽皮的自对称"）。将 $\Gamma(s/2)\pi^{-s/2}\zeta(s)$ 写成 $t$ 的积分，利用 $\theta$ 的对称性把积分拆成 $[0,1]$ 与 $[1,\infty)$ 两段重组，得到在 $s\mapsto1-s$ 下不变的表达式，从而导出函数方程与解析延拓。

## 三、定理的严格表述

函数方程：对一切 $s\in\mathbb{C}$（除去极点的 $s=1$），有
$$\xi(s)=\xi(1-s),\qquad \xi(s):=\frac12 s(s-1)\pi^{-s/2}\Gamma\left(\frac{s}{2}\right)\zeta(s).$$
等价形式：
$$\zeta(s)=2^s\pi^{s-1}\sin\left(\frac{\pi s}{2}\right)\Gamma(1-s)\zeta(1-s).$$

## 四、证明过程

**证明（基于 Poisson 求和）：**

**步骤 1：Theta 变换。** 定义 $\theta(t)=\sum_{n\in\mathbb{Z}}e^{-\pi n^2 t}$（$t>0$）。对 $f(x)=e^{-\pi x^2 t}$，其 Fourier 变换 $\hat f(y)=\frac1{\sqrt t}e^{-\pi y^2/t}$，由 Poisson 求和 $\sum_n f(n)=\sum_n\hat f(n)$ 得
$$\theta(t)=\frac1{\sqrt t}\,\theta\left(\frac1t\right).$$

**步骤 2：与 $s$ 的积分关联。** 利用 $\Gamma(s/2)=\int_0^\infty t^{s/2-1}e^{-t}dt$，令 $t=\pi n^2u$，对 $n\ge1$ 求和得（$\operatorname{Re}(s)>1$）
$$\pi^{-s/2}\Gamma\left(\frac s2\right)\zeta(s)=\int_0^\infty u^{s/2-1}\frac{\theta(u)-1}{2}du.$$

**步骤 3：拆分积分。** 把积分拆成 $[0,1]$ 与 $[1,\infty)$，对 $[0,1]$ 段用步骤 1 的变换 $u\mapsto1/u$ 换元、重组：

$$\pi^{-s/2}\Gamma\left(\frac s2\right)\zeta(s)=\frac{1}{s(s-1)}+\int_1^\infty\left(u^{s/2}+u^{(1-s)/2}\right)u^{-1}\frac{\theta(u)-1}{2}du.$$

**步骤 4：对称性与综述。** 上式右边在替换 $s\mapsto1-s$ 下不变（第一项 $\frac1{s(s-1)}$ 不变，积分内 $u^{s/2}$ 与 $u^{(1-s)/2}$ 互换），故
$$\pi^{-s/2}\Gamma\left(\frac s2\right)\zeta(s)=\pi^{-(1-s)/2}\Gamma\left(\frac{1-s}{2}\right)\zeta(1-s),$$
即 $\xi(s)=\xi(1-s)$。此式同时也把所有 $s$ 上的值经由右边解析延拓到整个复平面（$u^{s/2}$ 对一切复 $s$ 解析、$\theta$ 在无穷远指数衰减），且由 $\frac1{s(s-1)}$ 知 $\zeta$ 在 $s=1$ 为简单极点留数 $1$。利用 $\Gamma$ 的反射公式可得引言的等价形式。$\square$

## 五、应用与意义

函数方程是 Zeta 函数理论的支柱。其一，它确定平凡零点 $s=-2,-4,-6,\dots$：当 $\sin(\pi s/2)=0$ 且 $\Gamma(1-s)$ 无极点时 $\zeta(s)=0$。其二，它把临界带 $0<\operatorname{Re}(s)<1$ 内非平凡零点的研究化为全场问题——Riemann 假设的对称表述正基于此。其三，它是证明素数定理及获得高阶误差项的关键步骤。该方程还推广到 Dirichlet L-函数（得到 Hecke-Groß 理论）与椭圆曲线 $L$-函数，是算术对偶与模形式的深层联系。