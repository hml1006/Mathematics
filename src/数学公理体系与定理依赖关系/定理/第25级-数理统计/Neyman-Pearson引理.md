# Neyman-Pearson 引理

> **一句话大白话**：在两个单点假设 $H_0$ 与 $H_1$ 之间，"最优"的检验就是把量似然比 $\frac{L(x;\theta_1)}{L(x;\theta_0)}$ 大于某个门槛就拒绝 $H_0$，即似然比检验是最优势检验。
>
> **小例子**：$X\sim B(n,p)$，比较 $P=1/2$ 与 $P=3/5$，拒绝域取为"成功次数足够大"（等价于似然比 $>k$），即在给定显著性水平下功效最大。

## 介绍

Neyman-Pearson 引理（Neyman-Pearson Lemma）是假设检验理论中最基本的定理之一，由耶日·内曼（Jerzy Neyman）和埃贡·皮尔逊（Egon Pearson）在 1933 年提出。该引理指出：在两个简单假设 $H_0: \theta = \theta_0$ 与 $H_1: \theta = \theta_1$ 之间，最优势检验（MP test）是似然比检验。具体地，拒绝域为 $L(x; \theta_1)/L(x; \theta_0) > k$ 的检验具有最大功效（即在给定显著性水平下具有最大的检验功效）。这一定理为假设检验提供了最优性准则，是统计推断理论的核心结果之一。

## 分析

**前置依赖**：测度论、概率论、假设检验的基本概念（显著性水平、功效、两类错误）。

**数学内涵**：
- 考虑简单假设 $H_0: \theta = \theta_0$ 与 $H_1: \theta = \theta_1$。
- 似然比 $\Lambda(x) = L(x; \theta_1)/L(x; \theta_0)$。
- Neyman-Pearson 引理：对显著性水平 $\alpha$，存在常数 $k \geq 0$，使得拒绝域 $R = \{x: \Lambda(x) > k\}$ 的检验是显著性水平 $\alpha$ 下的最优势检验（MP 检验）。
- 最优势检验的含义：在所有显著性水平不超过 $\alpha$ 的检验中，该检验的功效（$H_1$ 下拒绝 $H_0$ 的概率）最大。

**结构**：
1. 构造似然比检验。
2. 证明对任意其他检验，其功效不超过似然比检验的功效。
3. 讨论随机化检验（当分布是离散时）。

## 思考过程

Neyman-Pearson 引理的证明利用 Neyman-Pearson 不等式，通过比较似然比检验和其他检验的"优势"来证明最优性。核心思想是：如果 $\phi(x)$ 是似然比检验（$\phi(x) = 1$ 当 $\Lambda(x) > k$，$\phi(x) = 0$ 当 $\Lambda(x) < k$），$\psi(x)$ 是任意其他检验，则
$$(\phi(x) - \psi(x))(L(x; \theta_1) - k L(x; \theta_0)) \geq 0$$
对两边积分，利用 $\phi$ 的显著性水平条件，可得 $\phi$ 的功效不低于 $\psi$ 的功效。

## 证明过程

**定理**（Neyman-Pearson 引理）：设 $H_0$ 和 $H_1$ 是简单假设，对应的密度函数为 $f_0(x)$ 和 $f_1(x)$。对给定的显著性水平 $\alpha \in (0, 1)$，存在常数 $k \geq 0$ 和随机化常数 $\gamma \in [0, 1]$，使得检验函数
$$\phi(x) = \begin{cases}
1, & f_1(x) > k f_0(x) \\
\gamma, & f_1(x) = k f_0(x) \\
0, & f_1(x) < k f_0(x)
\end{cases}$$
满足 $E_0[\phi(X)] = \alpha$，且对任意满足 $E_0[\psi(X)] \leq \alpha$ 的检验函数 $\psi$，有
$$E_1[\phi(X)] \geq E_1[\psi(X)]$$

**证明**：

### 1. 构造 $k$ 和 $\gamma$

令 $\phi_k(x) = I_{\{f_1(x) > k f_0(x)\}}$，定义 $\alpha(k) = E_0[\phi_k(X)]$。$\alpha(k)$ 是 $k$ 的递减右连续函数，$\lim_{k \to 0} \alpha(k) = 1$，$\lim_{k \to \infty} \alpha(k) = 0$。因此存在 $k$ 使得 $\alpha(k-) \leq \alpha \leq \alpha(k)$。取 $\gamma$ 使得
$$\gamma P_0(f_1(X) = k f_0(X)) + P_0(f_1(X) > k f_0(X)) = \alpha$$

### 2. 最优性证明

设 $\psi$ 是任意满足 $E_0[\psi] \leq \alpha$ 的检验函数。考虑差值
$$\Delta(x) = (\phi(x) - \psi(x))(f_1(x) - k f_0(x))$$

当 $\phi(x) = 1$ 时，$f_1(x) \geq k f_0(x)$，且 $\phi(x) - \psi(x) \geq 0$，故 $\Delta(x) \geq 0$。
当 $\phi(x) = 0$ 时，$f_1(x) \leq k f_0(x)$，且 $\phi(x) - \psi(x) \leq 0$，故 $\Delta(x) \geq 0$。
因此 $\Delta(x) \geq 0$ 对所有 $x$ 成立。

积分得：
$$\int (\phi - \psi)(f_1 - k f_0) dx \geq 0$$
即
$$\int \phi f_1 dx - \int \psi f_1 dx \geq k\left(\int \phi f_0 dx - \int \psi f_0 dx\right)$$

由于 $\int \phi f_0 dx = \alpha$ 且 $\int \psi f_0 dx \leq \alpha$，有 $\int \phi f_0 dx - \int \psi f_0 dx \geq 0$，故
$$\int \phi f_1 dx - \int \psi f_1 dx \geq 0$$

即 $E_1[\phi] \geq E_1[\psi]$。$\square$