# Daubechies小波的构造

> **一句话大白话**：按"正交、消失矩、归一"三条条件去解小波滤波器的系数方程，就能成套造出既紧支集又正交的小波（dbN）——$N$ 越大消失矩越高、越光滑，只是支集更宽、更不对称。
>
> **小例子**：$dbN$ 的尺度滤波器 $\{h_k\}_{k=0}^{2N-1}$ 满足正交 $\sum_kh_kh_{k+2m}=\delta_{m0}$、消失矩 $\sum_k(-1)^kk^mh_k=0$、归一 $\sum_kh_k=\sqrt2$；$db1$ 就是 Haar 小波。

## 一、定理介绍

> **前置依赖**：尺度方程与多分辨率分析、消失矩条件、Fejér-Riesz谱分解、Bezout恒等式

Daubechies 小波族断言：对任意正整数 $N$，存在紧支集正交小波 $\psi_N$，具 $N$ 阶消失矩、支集长 $2N-1$。其尺度滤波器系数由求解以下条件构得：
$$
\sum_kh_kh_{k+2m}=\delta_{m0},\qquad \sum_k(-1)^kk^m h_k=0\ (m=0,\dots,N-1),\qquad \sum_kh_k=\sqrt2.
$$

## 二、原理思路

构造靠"从幅度谱到滤波器"的谱分解路线。正交条件等价于 $|H(\omega)|^2+|H(\omega+\pi)|^2=1$；消失矩使传递函数在 $\omega=\pi$ 处有 $N$ 阶零点，故 $|H(\omega)|^2=(\cos^2\frac\omega2)^N Q(\sin^2\frac\omega2)$。待定 $Q$ 由 Bezout 恒等式 $(1-y)^NQ(y)+y^NQ(1-y)=1$ 唯一确定；再经 **Fejér-Riesz 谱分解**把幅度 $|H|^2$ 化为最小相位因果滤波器 $H$，最后用 Cascade 迭代构造尺度函数与小波。

## 三、定理的严格表述

对任意 $N\ge1$，存在长度为 $2N-1$ 的紧支集正交小波 $\psi_N$ 与对应尺度函数 $\phi_N$，其尺度滤波 $H(\omega)=\sum_{k=0}^{2N-1}h_ke^{-ik\omega}$ 满足：

1. 正交：$|H(\omega)|^2+|H(\omega+\pi)|^2=1$；
2. 消失矩：$H$ 在 $\omega=\pi$ 处有 $N$ 阶零点（等价 $\sum_k(-1)^kk^mh_k=0$，$m<N$）；
3. 归一：$\sum_kh_k=\sqrt2$。

其中 $|H(\omega)|^2=(\cos^2\frac\omega2)^NQ(\sin^2\frac\omega2)$，$Q(y)=\sum_{k=0}^{N-1}\binom{N+k-1}{k}y^k$。

## 四、证明过程

**步骤1：构造传递函数。** $|H(\omega)|^2+|H(\omega+\pi)|^2=1$；消失矩使 $H(\omega)=(\frac{1+e^{-i\omega}}2)^NL(\omega)$。

**步骤2：写幅度的参数化。** 令 $P(\omega)=|H(\omega)|^2=\big(\cos^2\frac\omega2\big)^N Q(\sin^2\frac\omega2)$，$Q$ 为 $N-1$ 次多项式。

**步骤3：求解 $Q$。** 正交条件化为 Bezout 恒等式
$$
(1-y)^NQ(y)+y^NQ(1-y)=1;
$$
由 Bezout 定理存在唯一多项式解
$$
Q(y)=\sum_{k=0}^{N-1}\binom{N+k-1}{k}y^k.
$$

**步骤4：谱分解。** 令 $z=e^{i\omega}$，$P(z)$ 为非负三角多项式；由 Fejér-Riesz 定理 $P(z)=H(z)H(z^{-1})$，取 $H$ 的根全在单位圆内（最小相位）得唯一因果过滤器系数。

**步骤5：验证正交与归一。** 谱分解保证 $|H|^2+|H(\omega+\pi)|^2=1$；$H(0)=\sqrt2$（因 $P(0)=|H(0)|^2=2$）即 $\sum_kh_k=\sqrt2$。

**步骤6：验证消失矩。** $H$ 在 $\omega=\pi$ 有 $N$ 阶零点：$H^{(m)}(\pi)=(-i)^m\sum_k(-1)^kk^mh_k=0$，$m<N$。

**步骤7：Cascade 构造尺度函数。** 迭代 $\phi^{(n+1)}=\sqrt2\sum_kh_k\phi^{(n)}(2t-k)$ 由初值收敛到 $\phi_N$，再由 $\psi(t)=\sqrt2\sum_k(-1)^k\bar h_{1-k}\phi(2t-k)$ 得小波 $\psi_N$。

**结论（$\square$）**：对每个 $N$，db$N$ 尺度滤波与小波存在且具 $N$ 阶消失矩、支集长 $2N-1$。

## 五、应用与意义

Daubechies 小波是理论与工程兼得的紧支正交小波族，用于图像压缩、去噪、特征提取与数值分析；其"最小相位紧支"设计是滤波器组设计和小波构造的经典样板。$N$ 调节光滑/支集/消失矩的权衡，成为实际小波应用的默认选择之一。