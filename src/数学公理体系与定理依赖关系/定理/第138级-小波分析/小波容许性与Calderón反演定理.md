# 小波容许性与 Calderón 反演定理

> **一句话大白话**：同一个波形经过平移和缩放后，若想不丢信息地记录任意信号，它在频域原点必须足够“安静”，高频端也不能太坏；容许常数有限时，所有尺度的分析系数可以按固定权重重新叠回原信号。
>
> **小例子**：墨西哥帽小波是 Gaussian 的二阶导数，时域均值为零，频域形如 $\widehat\psi(\xi)=c\xi^2e^{-\xi^2/2}$。它在 $\xi=0$ 处有二阶零点、在无穷远指数衰减，所以 $\int|\widehat\psi(\xi)|^2/|\xi|\,d\xi$ 有限，满足 Calderón 容许条件。

## 介绍

连续小波变换把一个一维信号展开成尺度 $a$ 与位置 $b$ 两个变量上的系数。系数增多带来冗余，但冗余本身不自动保证能够稳定反演。Calderón 反演定理指出：容许常数 $C_\psi$ 有限正是连续小波分析满足能量恒等式并可在 $L^2$ 中重构信号的判据。这里的反演是已证明的分析恒等式，不是数值算法的经验近似。

## 分析

**前置依赖**：$L^1$ 与 $L^2$ Fourier 变换、Plancherel 定理、Fubini-Tonelli 定理、卷积、稠密子空间与弱收敛。

**定理内容**：采用归一化

$$
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-ix\xi}\,dx,
\qquad
\psi_{a,b}(x)=|a|^{-1/2}\psi\!\left(\frac{x-b}{a}\right),
\quad a\in\mathbb R\setminus\{0\},\ b\in\mathbb R.
$$

定义连续小波变换

$$
W_\psi f(a,b)=\langle f,\psi_{a,b}\rangle
=|a|^{-1/2}\int_{\mathbb R}f(x)
\overline{\psi\!\left(\frac{x-b}{a}\right)}\,dx .
$$

对 $\psi\in L^2(\mathbb R)$，定义容许常数

$$
\boxed{C_\psi=\int_{\mathbb R}\frac{|\widehat\psi(\xi)|^2}{|\xi|}\,d\xi}.
$$

若 $0<C_\psi<\infty$，则对任意 $f\in L^2(\mathbb R)$ 有 Calderón 能量恒等式

$$
\boxed{\int_{\mathbb R\setminus\{0\}}\int_{\mathbb R}
|W_\psi f(a,b)|^2\,db\,\frac{da}{a^2}
=C_\psi\|f\|_2^2}
$$

以及反演公式

$$
\boxed{f=\frac1{C_\psi}
\int_{\mathbb R\setminus\{0\}}\int_{\mathbb R}
W_\psi f(a,b)\,\psi_{a,b}\,db\,\frac{da}{a^2}}.
$$

二重积分按截断区域扩张后的 $L^2$ 弱极限理解，不必把它解释为对任意 $L^2$ 信号都绝对收敛的普通逐点积分。等价地，对任意 $g\in L^2$，

$$
\langle f,g\rangle
=\frac1{C_\psi}\int\int W_\psi f(a,b)
\overline{W_\psi g(a,b)}\,db\,\frac{da}{a^2}.
$$

反之，若上述尺度—位置分析对所有 $f\in L^2$ 给出有限且与 $\|f\|_2^2$ 成固定正比的能量，则频率局部化论证迫使 $C_\psi$ 有限且等于比例常数。故“$C_\psi<\infty$”不是无关紧要的附加正则性，而是这一等距反演机制的核心条件。

若进一步 $\psi\in L^1\cap L^2$，则 $\widehat\psi$ 连续，容许条件蕴含

$$
\widehat\psi(0)=\int_{\mathbb R}\psi(x)\,dx=0.
$$

但仅有零均值一般并不充分；还需控制在 $\xi=0$ 与 $|\xi|\to\infty$ 时使上述积分收敛的衰减条件。

## 思考过程

固定尺度 $a$，小波变换关于位置 $b$ 仍是一个一维函数。对其作 Fourier 变换，得到

$$
\widehat{W_\psi f(a,\cdot)}(\xi)
=|a|^{1/2}\widehat f(\xi)\overline{\widehat\psi(a\xi)}.
$$

于是 Plancherel 定理可以先积掉 $b$，留下 $|\widehat f(\xi)|^2$ 与尺度滤波器 $|\widehat\psi(a\xi)|^2$。再积掉尺度时，代换 $\eta=a\xi$ 把每个非零频率上的尺度积分都化成同一个常数 $C_\psi$。因此左边恰为 $C_\psi\|f\|_2^2$。能量恒等式又说明分析算子除以 $\sqrt{C_\psi}$ 后是等距，其伴随在等距值域上就是逆算子，这就是反演公式的算子含义。

## 证明过程

### 1. 固定尺度应用 Plancherel 定理

先取 $f$ 位于 $L^1\cap L^2$ 的适当稠密子空间，并令频率支撑远离原点与无穷远，以保证下面交换积分合法。由卷积的 Fourier 公式，

$$
\begin{aligned}
&\int_{\mathbb R}|W_\psi f(a,b)|^2db\\
&\quad=\frac1{2\pi}\int_{\mathbb R}
|a|\,|\widehat f(\xi)|^2|\widehat\psi(a\xi)|^2d\xi .
\end{aligned}
$$

### 2. 计算全部尺度的能量

两边乘以 $a^{-2}$ 并对 $a\in\mathbb R\setminus\{0\}$ 积分，再交换积分次序，得到

$$
\frac1{2\pi}\int_{\mathbb R}|\widehat f(\xi)|^2
\left(\int_{\mathbb R\setminus\{0\}}
|\widehat\psi(a\xi)|^2\frac{da}{|a|}\right)d\xi .
$$

对每个 $\xi\neq0$ 作代换 $\eta=a\xi$，无论 $\xi$ 正负都有

$$
\int_{\mathbb R\setminus\{0\}}
|\widehat\psi(a\xi)|^2\frac{da}{|a|}
=\int_{\mathbb R}|\widehat\psi(\eta)|^2\frac{d\eta}{|\eta|}
=C_\psi.
$$

单点 $\xi=0$ 不影响 Lebesgue 积分。再次使用 Plancherel 定理即得能量恒等式。有限能量的稠密子空间结论再通过一致有界延拓推广到整个 $L^2$。

### 3. 极化得到双线性恒等式

对 $f,g$ 的能量恒等式作极化，可得

$$
\int\int W_\psi f(a,b)\overline{W_\psi g(a,b)}
\,db\,\frac{da}{a^2}
=C_\psi\langle f,g\rangle .
$$

由于（先按 $a,b$ 的截断积分理解）

$$
\int_{\mathbb R}W_\psi f(a,b)\overline{W_\psi g(a,b)}\,db
=\left\langle\int_{\mathbb R}W_\psi f(a,b)\psi_{a,b}\,db,g\right\rangle,
$$

再对 $a$ 积分并交换内积与截断积分，所以

$$
\left\langle \frac1{C_\psi}\int\int
W_\psi f(a,b)\psi_{a,b}\,db\,\frac{da}{a^2},g\right\rangle
=\langle f,g\rangle .
$$

### 4. 得到弱 $L^2$ 反演

上式对所有 $g\in L^2$ 成立，故括号中的截断小波叠加在 $L^2$ 弱意义下收敛到 $f$，即 Calderón 反演公式。若 $f,\psi$ 具有额外的时频衰减，还可把弱极限加强为更强的范数或逐点收敛，但这些结论需要另列假设，不能由容许条件单独推出。$\square$

## 课堂问答

**老师**：为什么小波要满足 $C_\psi=\int|\widehat\psi(\xi)|^2/|\xi|d\xi<\infty$，零均值又从哪里来？

**学生**：因为积掉全部尺度时会出现代换 $\eta=a\xi$，恰好留下 $C_\psi$ 这个共同因子；它有限才能使能量恒等式成立。若 $\psi\in L^1\cap L^2$，则 $\widehat\psi$ 连续，而积分在 $\xi=0$ 要收敛就迫使 $\widehat\psi(0)=0$，也就是时域零均值；但零均值单独并不保证高频端和原点两侧积分都收敛。

**老师（追问）**：Calderón 公式中的 $da/a^2$ 和 $|a|^{-1/2}$ 是任意选的吗？

**学生**：不是。$|a|^{-1/2}$ 使 $\|\psi_{a,b}\|_2=\|\psi\|_2$，固定尺度变换的频域公式因而含 $|a|^{1/2}$。Plancherel 后再乘尺度测度 $a^{-2}da$，留下 $|a|^{-1}da$，经 $\eta=a\xi$ 才正好得到 $|\eta|^{-1}d\eta$ 与 $C_\psi$。换归一化时必须同步改公式。

**老师（拓展）**：连续反演公式是否说明每个 $L^2$ 函数都能被普通的绝对收敛二重积分逐点重建？

**学生**：不能这样加强结论。标准定理给的是截断积分的 $L^2$ 弱极限，等价于对所有 $g$ 的双线性恒等式；额外正则性才能换取更强收敛。离散小波框架则是另一层理论：连续容许性不自动说明某个离散网格 $a_j,b_{j,k}$ 能形成框架，离散情形还要检查框架上下界。

## 相关条目

- [小波框架的稳定性](./小波框架的稳定性.md)
- [多分辨率分析的基本定理](./多分辨率分析的基本定理.md)
- [Plancherel 定理](../第51级-调和分析/Plancherel定理.md)
- [Fourier 变换与逆变换公式](../第51级-调和分析/Fourier变换与逆变换公式.md)
- [Fubini-Tonelli 定理](../第32级-高等实分析/Fubini-Tonelli定理.md)：直接前置依赖。
