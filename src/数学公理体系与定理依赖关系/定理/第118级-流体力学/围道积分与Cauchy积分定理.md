# 围道积分与Cauchy积分定理

> **一句话大白话**：复变函数沿一条曲线做的积分叫围道积分；Cauchy 积分定理说：只要函数在这条闭曲线围成的区域里全纯（处处可导），绕一圈积出来一定是零。这条"绕圈为零"把复杂的边界积分变成只依赖少数奇点的计算。
>
> **小例子**：$\oint_{|z|=1}\frac{dz}{z}=2\pi i\ne0$——因为它在围道内有一个奇点 $z=0$，全纯条件被破坏；而对处处全纯的 $e^{z}$，有 $\oint_{|z|=1}e^{z}\,dz=0$。

## 一、定理介绍

> **前置依赖**：柯西积分定理、Cauchy-Riemann方程、Stokes定理、柯西积分公式。

设 $\gamma:[a,b]\to\mathbb C$ 是分段 $C^1$ 曲线，$f$ 在 $\gamma$ 上连续。**围道积分**定义为
$$
\int_\gamma f(z)\,dz:=\int_a^b f(\gamma(t))\,\gamma'(t)\,dt .
$$
**Cauchy 积分定理**（Cauchy–Goursat）：若 $f$ 在单连通区域 $D$ 上全纯，$\gamma\subseteq D$ 为分段 $C^1$ 闭曲线，则
$$
\oint_\gamma f(z)\,dz=0 .
$$
它是复分析的中心定理：由此推出**围道变形原理**（同伦的闭曲线积分相等）与 **Cauchy 积分公式**，Blasius 定理中把物体边界积分化为远场大圆积分正是它的应用。

## 二、原理思路

先设 $f=u+iv$ 且偏导连续，把 $f\,dz$ 按实部、虚部拆开，围道积分化为两个实线积分；用 Stokes 定理的平面情形（Green 公式）换成区域上的二重积分，再用 Cauchy–Riemann 方程 $u_x=v_y,\ u_y=-v_x$ 把被积函数化为零，即得 $\oint f\,dz=0$。对一般的全纯函数（只假设可导，导数未必连续），改用 Goursat 的三角形剖分：把一个三角形不断四等分，用可微性把余项压到 $o(\text{面积})$，令细分步数趋于无穷即得三角形上的积分为零，再拼出一般闭曲线与任意区域。

## 三、定理的严格表述

**（Cauchy 积分定理）** 设 $D\subseteq\mathbb C$ 为单连通开集，$f\in H(D)$（$D$ 上全纯），$\gamma$ 为 $D$ 内分段 $C^1$ 闭曲线，则 $\oint_\gamma f(z)\,dz=0$。

**（围道变形原理）** 若 $\gamma_0,\gamma_1$ 是 $D$ 内定端同伦的两条分段 $C^1$ 曲线，则 $\oint_{\gamma_0}f\,dz=\oint_{\gamma_1}f\,dz$。

**（Cauchy 积分公式）** 若 $f\in H(D)$，$\overline{B(z_0,\rho)}\subseteq D$，则 $f(z_0)=\dfrac{1}{2\pi i}\oint_{|z-z_0|=\rho}\dfrac{f(z)}{z-z_0}\,dz$。

## 四、证明过程

1. **$C^1$ 情形的 Green 公式证明**。写 $f=u+iv$、$dz=dx+i\,dy$，则
   $$
   \oint_\gamma f\,dz=\oint_\gamma(u\,dx-v\,dy)+i\oint_\gamma(v\,dx+u\,dy).
   $$
2. **化为二重积分**。设 $\gamma$ 正向围成区域 $R\subseteq D$，由 Stokes 定理的平面情形（Green 公式）
   $$
   \oint_\gamma(u\,dx-v\,dy)=-\iint_R(u_y+v_x)\,dA,\qquad \oint_\gamma(v\,dx+u\,dy)=\iint_R(u_x-v_y)\,dA .
   $$
3. **用 Cauchy–Riemann 化零**。全纯性给出 $u_x=v_y$ 与 $u_y=-v_x$，故两个被积函数 $u_y+v_x=0$、$u_x-v_y=0$ 恒为零，于是 $\oint_\gamma f\,dz=0$。这给出了导数连续时的证明。

4. **Goursat 三角形引理（去掉导数连续性假设）**。设 $T\subseteq D$ 为三角形，$I=\big|\oint_{\partial T}f\,dz\big|$。把 $T$ 四等分成 $T_1,\dots,T_4$，则 $\oint_{\partial T}=\sum_{k=1}^{4}\oint_{\partial T_k}$（内部边两两反向抵消），故至少有一个 $T^{(1)}$ 满足 $\big|\oint_{\partial T^{(1)}}f\,dz\big|\ge I/4$。迭代得嵌套三角形 $T^{(0)}\supset T^{(1)}\supset\cdots$，其公共点记为 $z_0$，且
   $$
   \Big|\oint_{\partial T^{(m)}}f\,dz\Big|\ \ge\ \frac{I}{4^{m}} .
   $$
5. **用可微性估计余项**。由 $f$ 在 $z_0$ 可微，$f(z)=f(z_0)+f'(z_0)(z-z_0)+r(z)$，其中当 $|z-z_0|<\delta$ 时 $|r(z)|\le\varepsilon|z-z_0|$。对每个 $T^{(m)}$，由围道积分的线性与 $\oint_{\partial T^{(m)}}dz=\oint_{\partial T^{(m)}}z\,dz=0$，只剩余项：
   $$
   \Big|\oint_{\partial T^{(m)}}f\,dz\Big|=\Big|\oint_{\partial T^{(m)}}r(z)\,dz\Big|\le\varepsilon\,\mathrm{diam}\big(T^{(m)}\big)\cdot\mathrm{length}\big(\partial T^{(m)}\big)\le C\,\varepsilon\,4^{-m}.
   $$
   于是 $I/4^{m}\le C\varepsilon 4^{-m}$，即 $I\le C\varepsilon$；令 $\varepsilon\to0$ 得 $I=0$，三角形上积分为零。

6. **拼出一般闭曲线与推论**。任意多边形可剖分为三角形，由第 4 步得沿其边界的积分为零；一般分段 $C^1$ 闭曲线可用内接折线逼近（围道积分对围道的连续依赖性），得 $\oint_\gamma f\,dz=0$。若 $\gamma_0,\gamma_1$ 定端同伦，则 $\gamma_0$ 与反向的 $\gamma_1$ 拼成一条闭曲线，积分为零，即 $\oint_{\gamma_0}=\oint_{\gamma_1}$，这就是围道变形原理。最后取 $g(z)=\dfrac{f(z)}{z-z_0}$（在 $z_0$ 处留一极点），由变形原理把围道移到小圆 $|z-z_0|=\rho$ 上并令 $\rho\to0$，利用 $\oint_{|z-z_0|=\rho}\dfrac{dz}{z-z_0}=2\pi i$ 与 $f$ 的连续性，即得 Cauchy 积分公式。$\blacksquare$

## 五、应用与意义

- **围道变形与留数**：把复杂的边界积分收缩到奇点附近的小圆，是留数定理与 Blasius 定理中远场大圆计算的理论依据。
- **解析函数的性质**：由积分公式推出全纯函数无穷可微、Cauchy 估计与 Liouville 定理等整套结论。
- **跨学科工具**：在流体力学（复势、升力计算）、电磁学与渐近分析中，围道积分是"用解析方法求全局量"的标准范式。
