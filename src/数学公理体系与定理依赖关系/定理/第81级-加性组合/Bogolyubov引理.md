# Bogolyubov 引理

> **一句话大白话**：只要一个集合密度不低，那么把"两次和减两次差"反复组合起来，就必然盖住一大块"频率一致"的区域（Bohr 集）——零散的加法结构里藏着规则的周期结构。
>
> **小例子**：在 $\mathbb{Z}_N$ 中取 $|A|=\alpha N$，则 $2A-2A$ 含有一个由至多 $4\alpha^{-2}$ 个频率定义的 Bohr 集；密度越高（$\alpha$ 越大），这块规则区域越大。

## 一、定理介绍

> **前置依赖**：有限阿贝尔群 $\mathbb{Z}_N$ 上的 Fourier 变换与 Parseval 恒等式、Bohr 集、差集与和集 $2A-2A$、卷积

Bogolyubov 引理（Bogolyubov，1939；后由 Ruzsa、Green 等在加性组合中重新发掘）断言：密度为 $\alpha$ 的集合 $A\subseteq\mathbb{Z}_N$，其"二阶差集" $2A-2A$ 必包含一个由**少量**频率定义的 Bohr 集。Bohr 集是"近似周期结构"，故此引理把"集合密度不低"升级为"含有大块的周期子结构"。

它是 Freiman 定理证明链条中的核心一步：先在 $\mathbb{Z}_p$ 中把 $A$ 换成 $2A-2A$ 中的 Bohr 集，再把它参数化为广义等差数列。它也是 Ruzsa 关于"密度增量""结构定理"以及 Green–Tao、Gowers 范数理论的基本部件。

## 几何直观

![两排格点上 A 只有四个点，A+A 却填满九个点，其中一段被绿色 Bohr 集框住](images/th-081-01-bogolyubov.svg)

图意在说明：A+A 一旦稠密，内部就含有结构规整的 Bohr 集，即大块等差数列。

## 二、原理思路

证明是一个纯粹的 Fourier 分析计算。把 $x\in 2A-2A$ 的判定写成卷积

$$
T(x)=\sum_{a_1+a_2-a_3-a_4=x}\mathbf{1}_A(a_1)\mathbf{1}_A(a_2)\mathbf{1}_A(a_3)\mathbf{1}_A(a_4),
$$

$T(x)>0$ 即等价于 $x\in 2A-2A$。其 Fourier 展开中，零频率项给出主项 $\alpha^4N^3$，其余项都带相位 $e^{2\pi i\xi x/N}$。

关键观察：$\hat{\mathbf{1}_A}(\xi)$ 的**大系数只有一个**（至多 $4\alpha^{-2}$ 个），把频率分成"大系数集 $\Gamma$"与"小系数集"：
- 在小系数集上，用 Parseval 控制总贡献；
- 在大系数集上，只要 $x$ 使所有相位 $e^{2\pi i\xi x/N}$ 都接近 $1$（即 $x\in B(\Gamma,\rho)$），贡献也小。

于是主项压倒误差，$T(x)>0$，得到 $B(\Gamma,\rho)\subseteq 2A-2A$。

## 三、定理的严格表述

定义 Bohr 集：对 $\Gamma\subseteq\widehat{\mathbb{Z}_N}\cong\mathbb{Z}_N$ 与 $\rho>0$，

$$
B(\Gamma,\rho)=\Big\{x\in\mathbb{Z}_N:\ \Big\|\tfrac{\xi x}{N}\Big\|\le\rho\ \ \forall\,\xi\in\Gamma\Big\},
$$

其中 $\|t\|$ 表示 $t$ 到最近整数的距离。

（Bogolyubov 引理）设 $A\subseteq\mathbb{Z}_N$ 满足 $|A|=\alpha N$（$\alpha>0$）。则存在频率集 $\Gamma$ 使

$$
B(\Gamma,\rho)\subseteq 2A-2A:=A+A-A-A,\qquad |\Gamma|\le 4\alpha^{-2},\qquad \rho=\frac{\alpha}{8\pi}.
$$

特别地 $|2A-2A|\ge \rho^{|\Gamma|}N\ge\left(\frac{\alpha}{8\pi}\right)^{4\alpha^{-2}}N$。

**推论（小和集情形）。** 若 $A\subseteq\mathbb{Z}_p$ 满足 $|A+A|\le K|A|$ 且 $\alpha=|A|/p$，则 $2A-2A$ 含秩 $\le 4\alpha^{-2}$ 的 Bohr 集；在 Freiman 定理的证明中，这个 Bohr 集被进一步参数化为广义等差数列／子群结构。

## 四、证明过程

**步骤 1：Fourier 化。** 记 $\hat f(\xi)=\sum_{x\in\mathbb{Z}_N}f(x)e^{-2\pi i\xi x/N}$。对 $f=\mathbf{1}_A$，$\hat f(0)=|A|=\alpha N$，且 Parseval 给出

$$
\sum_{\xi\in\mathbb{Z}_N}|\hat f(\xi)|^2=N\sum_{x}|f(x)|^2=N|A|=\alpha N^2 . \tag{1}
$$

**步骤 2：定义大频率集。** 令

$$
\Gamma=\Big\{\xi\in\mathbb{Z}_N:\ |\hat f(\xi)|>\tfrac12\alpha^{3/2}N\Big\}.
$$

由 (1)，每个 $\xi\in\Gamma$ 贡献 $|\hat f(\xi)|^2>\tfrac14\alpha^3N^2$，故

$$
|\Gamma|\cdot\tfrac14\alpha^3N^2<\sum_\xi|\hat f(\xi)|^2=\alpha N^2
\ \Longrightarrow\ |\Gamma|<4\alpha^{-2}. \tag{2}
$$

**步骤 3：卷积的 Fourier 展开。** 令 $T=\mathbf{1}_A*\mathbf{1}_A*\mathbf{1}_{-A}*\mathbf{1}_{-A}$，即

$$
T(x)=\#\{(a_1,a_2,a_3,a_4)\in A^4:\ a_1+a_2-a_3-a_4=x\},
$$

则 $x\in 2A-2A\iff T(x)>0$。卷积的 Fourier 系数相乘，故

$$
T(x)=\frac1N\sum_{\xi}|\hat f(\xi)|^4\,e^{2\pi i\xi x/N}
=\alpha^4N^3+\frac1N\sum_{\xi\ne0}|\hat f(\xi)|^4\,e^{2\pi i\xi x/N}, \tag{3}
$$

这里主项来自 $\xi=0$：$\frac1N|\hat f(0)|^4=\frac1N\alpha^4N^4=\alpha^4N^3$。

**步骤 4：估计误差。** 设 $x\in B(\Gamma,\rho)$，此时对每个 $\xi\in\Gamma$ 有 $|e^{2\pi i\xi x/N}-1|\le 2\pi\|\xi x/N\|\le 2\pi\rho$。把 (3) 的误差分裂为 $\xi\in\Gamma\setminus\{0\}$ 与 $\xi\notin\Gamma$ 两部分。

对大频率部分，用 $|\hat f(\xi)|^4\le\big(\max_\xi|\hat f(\xi)|^2\big)|\hat f(\xi)|^2\le\alpha^2N^2|\hat f(\xi)|^2$ 与 (1)：

$$
\frac1N\sum_{\xi\in\Gamma}|\hat f(\xi)|^4\big|e^{2\pi i\xi x/N}-1\big|
\le\frac{2\pi\rho}{N}\cdot\alpha^2N^2\sum_\xi|\hat f(\xi)|^2
=2\pi\rho\,\alpha^3N^3 . \tag{4}
$$

对小频率部分，用 $|\hat f(\xi)|^4\le\big(\tfrac12\alpha^{3/2}N\big)^2|\hat f(\xi)|^2$ 与 (1)：

$$
\frac1N\sum_{\xi\notin\Gamma}\big|\hat f(\xi)\big|^4\cdot 2
\le\frac1N\cdot\tfrac14\alpha^3N^2\cdot 2\sum_\xi|\hat f(\xi)|^2
=\tfrac12\alpha^4N^3 . \tag{5}
$$

**步骤 5：主项占优。** 合并 (3)(4)(5)，对 $x\in B(\Gamma,\rho)$，

$$
T(x)\ge\alpha^4N^3-2\pi\rho\,\alpha^3N^3-\tfrac12\alpha^4N^3
=\alpha^3N^3\Big(\tfrac{\alpha}{2}-2\pi\rho\Big).
$$

取 $\rho=\alpha/(8\pi)$，则 $\tfrac{\alpha}{2}-2\pi\rho=\tfrac{\alpha}{2}-\tfrac{\alpha}{4}=\tfrac{\alpha}{4}>0$，故 $T(x)>0$，即 $x\in 2A-2A$。结合 (2) 得

$$
B(\Gamma,\rho)\subseteq 2A-2A,\qquad |\Gamma|\le 4\alpha^{-2},\qquad \rho=\frac{\alpha}{8\pi} . \tag{6}
$$

**步骤 6：Bohr 集的大小。** 由 $\|t\|\le\rho$ 定义的每个频率限制掉的测度至多 $2\rho$，逐次剥离得 $|B(\Gamma,\rho)|\ge (1-2\rho)^{|\Gamma|}N\ge\rho^{|\Gamma|}N$（取 $\rho\le1/4$）。代入 (6) 即得结论。$\blacksquare$

## 五、应用与意义

**理论意义：**

1. **Freiman 定理**：$|A+A|\le C|A|$ 时，先经 Ruzsa 建模转到 $\mathbb{Z}_p$，再用 Bogolyubov 得到 $2A-2A$ 中的 Bohr 集，其正交补／参数化给出包含 $A$ 的大广义等差数列。

2. **Roth 定理与密度增量**：Bohr 集是密度增量法中的"结构返回"，$3$-进级数的多余密度必须由 Bohr 集结构解释。

3. **逆定理**：Bogolyubov 是"Fourier 逆定理"系列中最早、最强的一例，启发了 $U^k$ 范数与 Gowers 逆定理。

**应用领域：** 加性组合（和集结构）、遍历理论（多重回归的结构分析）、数论（素数中的等差数列）、理论计算机科学（伪随机与去随机化）。

**推广：** 对一般有限阿贝尔群 $G$ 有同型结论（Bohr 集定义为对偶群上的特征限制）；在 $\mathbb{Z}_p$ 上，Bohr 集可视为"近似子群"，配合 Freiman 同构即得显式的子群/等差数列结构。

## 课堂问答

**老师**：密度不低的集合，为什么一定含有"周期性子结构"？

**学生**：Bogolyubov 引理：若 $A\subseteq\mathbb{Z}_N$、$|A|=\alpha N$，则存在频率集 $\Gamma$ 使 Bohr 集 $B(\Gamma,\rho)\subseteq 2A-2A=A+A-A-A$，且 $|\Gamma|\le 4\alpha^{-2}$、$\rho=\alpha/(8\pi)$，于是 $|2A-2A|\ge\rho^{|\Gamma|}N$。证明是纯 Fourier：把 $x\in 2A-2A$ 的判定写成四重卷积 $T(x)=\#\{a_1+a_2-a_3-a_4=x\}$，其 Fourier 展开主项为 $\alpha^4N^3$；由 Parseval 只有至多 $4\alpha^{-2}$ 个大系数频率，小系数用 Parseval 控、大系数在 $B(\Gamma,\rho)$ 上相位接近 $1$ 也控，主项占优即得 $T(x)>0$。

**老师（追问）**：为什么频率集的大小能被 $\alpha$ 控制？

**学生**：关键取大频率集 $\Gamma=\{\xi:|\hat f(\xi)|>\tfrac12\alpha^{3/2}N\}$，每个贡献 $|\hat f(\xi)|^2>\tfrac14\alpha^3N^2$，而 Parseval 给出总和 $\sum_\xi|\hat f(\xi)|^2=\alpha N^2$，故 $|\Gamma|<4\alpha^{-2}$。误区：以为要列出全部频率；实际上频率空间虽大，能"说话"的少数几个就够了，这是不确定性原理的定量版。

**老师（拓展）**：它在加性组合里扮演什么角色？

**学生**：它是 Freiman 定理证明链的关键一步：先把小和集经 Ruzsa 建模搬到 $\mathbb{Z}_p$，再用 Bogolyubov 在 $2A-2A$ 中取出大子群/Bohr 集并参数化为广义等差数列；也是 Roth 密度增量中"结构返回"与 Gowers 范数逆定理的思想源头。
