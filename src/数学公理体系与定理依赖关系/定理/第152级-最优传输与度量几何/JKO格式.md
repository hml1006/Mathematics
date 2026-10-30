# JKO 格式（Wasserstein 梯度流）

> **一句话大白话**：想在一个能量地形上沿最陡下降方向滑到谷底，每步先"就近走一小段"，再用"搬土的代价" $W_2^2$ 惩罚走太远，于是极小化 $\frac{1}{2\tau}W_2^2(\mu,\mu_k)+\mathcal F(\mu)$ 就定义了这一步；步长趋于零时，这条离散轨道就是能量的连续梯度流。
>
> **小例子**：取 $\mathcal F(\mu)$ 为相对熵、步长 $\tau=0.1$，从 $\mu_0=\delta_0$ 出发，每步都朝"更分散"的方向移动，极限满足热方程 $\partial_t\rho=\Delta\rho$，其显式解是 $\rho_t(x)=(4\pi t)^{-1/2}e^{-x^2/(4t)}$。

## 介绍

JKO 格式由 Jordan、Kinderlehrer 与 Otto 于 1998 年提出：在 Wasserstein 空间 $(\mathcal P_2,W_2)$ 上用隐式欧拉法离散梯度流。它把一个在度量空间中本无定义的"$\partial_t\mu=-\nabla\mathcal F(\mu)$"替换成一列变分问题，每一步都是"能量 + 距离惩罚"的极小化。其价值在于三点：极小元存在且唯一、无需预先知道极限方程、并且能自动给出能量耗散等式。当 $\mathcal F$ 取相对熵时，极限恰是 Fokker–Planck 方程，这为一大类扩散方程提供了统一的变分构造。

## 几何直观

![四个方框横向排列，依次是当前分布、加上距离惩罚后的变分问题、解出下一步分布、步长趋零得到连续轨道](images/th-152-07-jko-scheme.svg)

图意在说明：每个方框是一次隐式欧拉步，中间那个极小化把"离上一步太远"与"能量太高"两种代价折中；最右的方框表示把无数小步连起来，得到的曲线满足能量沿程严格下降，其切向速度就是负的能量梯度。

## 分析

**前置依赖**：Benamou–Brenier 公式、相对熵与 Fisher 信息、Fokker–Planck 方程、$W_2$ 空间的测地凸性。

**数学内涵**：
- 单步极小元存在唯一：$W_2^2(\cdot,\mu_k)$ 沿 $W_2$ 测地线严格凸，$\mathcal F$ 下半连续且下有界，紧性由二次矩控制。
- 一阶条件：设 $T_\tau$ 是把 $\mu_{k+1}$ 送回 $\mu_k$ 的最优映射，则 $v_\tau=(T_\tau-\mathrm{id})/\tau$ 满足 $v_\tau=-\nabla\frac{\delta\mathcal F}{\delta\mu}(\mu_{k+1})$，这正是"速度 = 负梯度"的离散版本。
- 常见误区：$W_2$ 不是向量空间，"$\mu_{k+1}=\mu_k-\tau\nabla\mathcal F$"没有意义；JKO 用"最优映射的位移除以 $\tau$"作为速度的替代物，而且要取 $T_\tau$ 的反向才能与下降方向对齐。

**结构**：
1. 证明每一步的极小元存在唯一。
2. 对竞争测度作变分，得速度场的一阶条件。
3. 用 $\mu_k$ 作竞争对手得离散能量估计，从而速度场一致有界，可提取极限曲线。
4. 让 $\tau\to0$，极限曲线满足连续性方程与能量耗散等式，即梯度流。
5. 取相对熵，把速度代入连续性方程，读出 Fokker–Planck 方程。

## 思考过程

Otto 在 1998 年前后发现 $W_2$ 空间形式上是黎曼流形，梯度流应当写成 $\partial_t\mu+\nabla\cdot(\mu\nabla\frac{\delta\mathcal F}{\delta\mu})=0$，但这个式子只是形式演算，缺乏存在性理论。障碍是：$W_2$ 的切空间依赖于测度本身，无法像欧氏空间那样直接做显式欧拉步。Jordan、Kinderlehrer 与 Otto 的突破是把隐式欧拉步写成一个极小化问题——隐式格式只需要"距离"和"能量"，这两样在度量空间里都有，于是形式演算变成了可证明的构造。此后 Ambrosio、Gigli 与 Savaré 在 2005 年前后把这套论证系统化为度量空间梯度流理论，覆盖了从热方程到多孔介质方程的一整类演化方程。

## 证明过程

**定理**：设 $\mathcal F:\mathcal P_2(\mathbb R^d)\to(-\infty,+\infty]$ 下半连续、下有界且满足 $\mathcal F(\mu)\ge-C(1+\int|x|^2\,\mathrm d\mu)$。给定 $\mu_0\in\mathcal P_2$、$\tau>0$，递归定义
$$
\mu_{k+1}^{\tau}\in\arg\min_{\mu\in\mathcal P_2}\left\{\frac{1}{2\tau}W_2^2(\mu,\mu_k^{\tau})+\mathcal F(\mu)\right\}.
$$
则每步极小元存在唯一；当 $\tau\to0$ 且 $k\tau\to t$ 时，分段常值插值 $\mu^\tau$ 在 $W_2$ 下收敛到 $\mathcal F$ 的梯度流 $(\mu_t)$，它满足能量耗散等式
$$
\mathcal F(\mu_t)+\frac12\int_0^t|\mu'|^2(s)\,\mathrm ds+\frac12\int_0^t|\partial\mathcal F|^2(\mu_s)\,\mathrm ds=\mathcal F(\mu_0),
$$
其中 $|\mu'|$ 为度量导数、$|\partial\mathcal F|$ 为 $\mathcal F$ 的度量斜率。若 $\mathcal F(\mu)=\mathrm{Ent}(\mu|\nu)$、$\nu=e^{-V}\mathcal L^d$，则 $\mu_t=\rho_t\mathcal L^d$ 且 $\partial_t\rho=\nabla\cdot(\nabla\rho+\rho\nabla V)$。

**证明**：

### 1. 单步极小元的存在唯一

令 $G(\mu)=\frac{1}{2\tau}W_2^2(\mu,\mu_k)+\mathcal F(\mu)$。取极小化序列 $\mu_j$，由 $G(\mu_j)\le G(\mu_k)<\infty$ 得 $W_2^2(\mu_j,\mu_k)\le2\tau(\mathcal F(\mu_k)-\inf\mathcal F)$，故 $(\mu_j)$ 一致紧并保持二次矩，有弱收敛子列 $\mu_j\to\mu$。$W_2$ 对第二变量弱下半连续、$\mathcal F$ 下半连续，故 $G$ 下半连续，$\mu$ 为极小元。唯一性：若 $\mu\ne\mu'$ 都是极小元，取 $W_2$ 测地线中点 $\mu_{1/2}$，由 $W_2^2$ 的测地凸性 $W_2^2(\mu_{1/2},\mu_k)<\frac12W_2^2(\mu,\mu_k)+\frac12W_2^2(\mu',\mu_k)$，与 $\mathcal F$ 的凸性相加得 $G(\mu_{1/2})<G(\mu)$，矛盾。

### 2. 一阶条件：速度等于负梯度

设 $\mu_{k+1}$ 绝对连续，$T_\tau$ 为把 $\mu_{k+1}$ 推前成 $\mu_k$ 的最优映射（Brenier 定理）。对任意光滑紧支向量场 $\xi$ 与 $s>0$，取竞争测度 $\sigma_s=(\mathrm{id}+s\xi)_\#\mu_{k+1}$。映射 $T_\tau\circ(\mathrm{id}+s\xi)^{-1}$ 把 $\sigma_s$ 推前成 $\mu_k$，故
$$
W_2^2(\sigma_s,\mu_k)\le\int\big|x+s\xi(x)-T_\tau(x)\big|^2\,\mathrm d\mu_{k+1}.
$$
又 $\frac{\mathrm d}{\mathrm ds}\big|_{0}\mathcal F(\sigma_s)=-\int\left\langle\nabla\frac{\delta\mathcal F}{\delta\mu},\xi\right\rangle\mathrm d\mu_{k+1}$。由 $G(\sigma_s)\ge G(\mu_{k+1})$ 在 $s=0$ 处右导非负，得
$$
\int\left\langle\xi,\ \frac{\mathrm{id}-T_\tau}{\tau}-\nabla\frac{\delta\mathcal F}{\delta\mu}\right\rangle\mathrm d\mu_{k+1}\ge0
$$
对一切 $\xi$ 成立，故 $v_\tau:=\frac{T_\tau-\mathrm{id}}{\tau}=-\nabla\frac{\delta\mathcal F}{\delta\mu}(\mu_{k+1})$。

### 3. 离散能量估计与紧性

在极小化中以 $\mu_k$ 为竞争对手，得 $\frac{1}{2\tau}W_2^2(\mu_{k+1},\mu_k)\le\mathcal F(\mu_k)-\mathcal F(\mu_{k+1})$。由第 2 步 $W_2(\mu_{k+1},\mu_k)=\tau\|v_\tau\|_{L^2(\mu_{k+1})}$，求和得 $\frac12\int_0^T\|v^\tau_t\|^2_{L^2(\mu^\tau_t)}\,\mathrm dt\le\mathcal F(\mu_0)-\inf\mathcal F<\infty$。于是速度场一致有界、$\mu^\tau$ 的 $W_2$ 模一致有界，由度量空间梯度流的紧性定理（Ambrosio–Gigli–Savaré）可抽子列使 $\mu^\tau\to\mu$ 局部一致、$v^\tau\rightharpoonup v$，且 $\partial_t\mu+\nabla\cdot(v\mu)=0$、$\frac12\int\|v\|^2\le\liminf\frac12\int\|v^\tau\|^2$。

### 4. 极限满足能量耗散等式

把第 3 步的估计取极限，得 $\mathcal F(\mu_T)+\frac12\int_0^T\|v_t\|^2\,\mathrm dt\le\mathcal F(\mu_0)$。另一方面，对任意光滑试验场 $\xi$，由第 2 步逐项取极限得
$$
\int\langle v_t,\xi\rangle\,\mathrm d\mu_t=-\int\left\langle\nabla\frac{\delta\mathcal F}{\delta\mu}(\mu_t),\xi\right\rangle\mathrm d\mu_t,
$$
即 $v_t=-\nabla\frac{\delta\mathcal F}{\delta\mu}(\mu_t)$，这就是梯度流的定义。再由链式法则 $|\mu'|(t)=|\partial\mathcal F|(\mu_t)$ 得耗散等式中的两个积分相等，且不等式必为等式。

### 5. 相对熵给出 Fokker–Planck

取 $\mathcal F(\mu)=\mathrm{Ent}(\mu|\nu)=\int\rho\log\rho\,\mathrm dx+\int V\,\mathrm d\mu$（$\mu=\rho\mathcal L^d$）。其第一变分为 $\frac{\delta\mathcal F}{\delta\mu}=\log\rho+V+1$，故
$$
v=-\nabla\Big(\log\rho+V\Big)=-\frac{\nabla\rho}{\rho}-\nabla V .
$$
代入连续性方程 $\partial_t\rho+\nabla\cdot(\rho v)=0$，
$$
\partial_t\rho=\nabla\cdot\Big(\rho\Big(\frac{\nabla\rho}{\rho}+\nabla V\Big)\Big)=\Delta\rho+\nabla\cdot(\rho\nabla V),
$$
这正是 Fokker–Planck 方程；$V\equiv0$ 时退化为热方程 $\partial_t\rho=\Delta\rho$。此时耗散等式读作 $\frac{\mathrm d}{\mathrm dt}\mathrm{Ent}(\mu_t|\nu)=-\int|\nabla\log(\rho/\nu)|^2\,\mathrm d\rho$，右端是相对 Fisher 信息。

### 6. 结论

第 1 步保证格式可运行，第 2 至 4 步保证 $\tau\to0$ 的极限是梯度流并满足能量耗散，第 5 步把抽象结论落地为 Fokker–Planck 方程。$\square$

## 课堂问答

**老师**：为什么非要写成隐式欧拉？显式格式"$\mu_{k+1}$ 沿梯度挪一小步"不行吗？

**学生**：$W_2$ 的切空间随测度变化，"沿梯度挪一步"没有直接意义；而且显式格式在能量不光滑时不稳定。隐式格式只用到距离和能量两个度量概念，既有定义又能保证每步有唯一解，还能自动给出能量单调下降。

**老师（追问）**：一阶条件里为什么是 $\frac{T_\tau-\mathrm{id}}{\tau}$ 而不是 $\frac{\mathrm{id}-T_\tau}{\tau}$？

**学生**：$T_\tau$ 把 $\mu_{k+1}$ 推回 $\mu_k$，所以它指向"上一步"，而梯度流要往下坡走，两者方向相反。变分计算给的是 $\int\langle\xi,\frac{\mathrm{id}-T_\tau}{\tau}-\nabla\frac{\delta\mathcal F}{\delta\mu}\rangle\ge0$，即 $\frac{\mathrm{id}-T_\tau}{\tau}=\nabla\frac{\delta\mathcal F}{\delta\mu}$，等价于 $\frac{T_\tau-\mathrm{id}}{\tau}=-\nabla\frac{\delta\mathcal F}{\delta\mu}$，与 $v=-\nabla\frac{\delta\mathcal F}{\delta\mu}$ 一致。符号搞反就会得到反向的热方程。

**老师（拓展）**：这套格式能处理哪些方程？边界在哪里？

**学生**：取 $\mathcal F$ 为内能 $\int U(\rho)$ 得多孔介质方程 $\partial_t\rho=\Delta\rho^m$；取 $\mathcal F$ 为相对熵得 Fokker–Planck；取 $\mathcal F$ 为交互能量得聚集–扩散方程；取 $\mathcal F$ 为指示函数（硬约束）得 Hele-Shaw 型自由边界问题。边界在于：$\mathcal F$ 必须下有界且下半连续，若 $\mathcal F$ 无下界（如某些非凸泛函），格式可能不收敛，需要改用更细的粘性结构或限制在子类测度上。
