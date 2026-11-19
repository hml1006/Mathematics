# Lehmann–Scheffé 定理

> **一句话大白话**：若一个充分统计量还“完备”，那么由它组成的无偏估计之间不会有多个互相竞争的选择；把任意无偏估计向它条件平均，就得到唯一的一致最小方差无偏估计。
>
> **小例子**：对独立同分布的 $\operatorname{Bernoulli}(\theta)$ 样本，$T=\sum_{i=1}^nX_i$ 在 $0<\theta<1$ 上完备充分。因为 $\bar X=T/n$ 无偏，所以它就是 $\theta$ 的唯一 UMVU 估计量，方差为 $\theta(1-\theta)/n$。

## 介绍

Lehmann–Scheffé 定理把 Rao–Blackwell 改进与完备性结合起来：充分性使条件期望成为统计量，完备性则排除两个不同的无偏函数。由此可在整个无偏估计类中得到一致最小方差与几乎必然唯一性，而不仅是在某个狭小估计类中最优。

## 分析

**前置依赖**：Rao–Blackwell 定理、充分统计量、完备统计量、无偏估计、条件期望与方差。

**定理内容**：设 $\{P_\theta:\theta\in\Theta\}$ 为统计模型，$T$ 是 $\theta$ 的**完备充分统计量**。完备性指：对可积的 $h(T)$，若

$$
\mathbb E_\theta h(T)=0\qquad\text{对所有 }\theta\in\Theta,
$$

则对每个 $\theta$ 都有 $P_\theta(h(T)=0)=1$。

若 $g(\theta)$ 存在一个二阶矩有限的无偏估计 $\delta(X)$，定义

$$
\eta(T)=\mathbb E[\delta(X)\mid T].
$$

则：

1. $\eta$ 不依赖 $\theta$，且 $\mathbb E_\theta\eta=g(\theta)$，即仍为无偏估计；
2. 对 $g(\theta)$ 的任意无偏估计 $W$，都有
   $$
   \operatorname{Var}_\theta\eta\leq\operatorname{Var}_\theta W
   \qquad\text{对所有 }\theta\in\Theta;
   $$
3. 因而 $\eta$ 是 $g(\theta)$ 的**一致最小方差无偏估计量**（UMVUE）；
4. 在二阶矩有限的无偏估计类中，UMVUE 唯一，唯一性按每个 $P_\theta$ 的几乎处处相等理解。

等价且常用的表述是：若 $U(T)$ 是完备充分统计量 $T$ 的无偏函数，则 $U(T)$ 就是其期望 $g(\theta)=\mathbb E_\theta U(T)$ 的唯一 UMVUE。

充分条件不可随意删弱：$T$ 必须同时充分且完备；至少要有可估计目标的一个无偏估计作为起点。只有充分性时，Rao–Blackwell 化只能保证改进，不能保证在所有无偏估计中唯一最优。

## 思考过程

任意两个无偏估计关于同一个 $T$ 条件平均后，仍然是 $T$ 的无偏函数，两者差的期望对所有 $\theta$ 都为零。完备性正好把“期望恒为零”升级成“函数本身几乎处处为零”，所以所有估计量 Rao–Blackwell 化后都落到同一个 $\eta$。再用 Rao–Blackwell 定理，$\eta$ 的方差不超过任何原始无偏估计的方差。

## 证明过程

充分性保证 $\eta(T)=\mathbb E[\delta\mid T]$ 不依赖 $\theta$；全期望公式给出

$$
\mathbb E_\theta\eta=\mathbb E_\theta\delta=g(\theta).
$$

由 Rao–Blackwell 定理，$\operatorname{Var}_\theta\eta\leq\operatorname{Var}_\theta\delta<\infty$，故 $\eta$ 自身属于二阶矩有限的无偏估计类。

任取 $g(\theta)$ 的无偏估计 $W$。若其方差无限，则方差不等式自动成立；若其二阶矩有限，定义

$$
V(T)=\mathbb E[W\mid T].
$$

同样由充分性和全期望公式，$V$ 是不依赖 $\theta$ 的无偏统计量。于是

$$
\mathbb E_\theta[\eta(T)-V(T)]=0
\qquad\text{对所有 }\theta.
$$

由 $T$ 的完备性，$\eta(T)=V(T)$ 对每个 $P_\theta$ 几乎处处成立。再由 Rao–Blackwell 定理，

$$
\operatorname{Var}_\theta\eta
=\operatorname{Var}_\theta V
\leq\operatorname{Var}_\theta W.
$$

这证明一致最小方差性。若 $W$ 也是 UMVUE，则上述方差必须相等；Rao–Blackwell 方差分解中的条件方差项只能为零，所以 $W=V(T)=\eta(T)$ 几乎处处成立，得到唯一性。$\square$

## 课堂问答

**老师**：Lehmann–Scheffé 定理需要哪些完整条件，结论又是什么？

**学生**：需要 $T$ 完备充分，并且目标 $g(\theta)$ 至少有一个二阶矩有限的无偏估计 $\delta$。令 $\eta=\mathbb E[\delta\mid T]$，则 $\eta$ 无偏，并且对所有 $\theta$、所有无偏 $W$ 都有 $\operatorname{Var}_\theta\eta\leq\operatorname{Var}_\theta W$；因此 $\eta$ 是唯一 UMVUE，唯一性按各 $P_\theta$ 几乎处处理解。

**老师（追问）**：完备性在证明的哪一步不可替代？充分而不完备时会怎样？

**学生**：对任意无偏 $W$，令 $V=\mathbb E[W\mid T]$，则 $\mathbb E_\theta(\eta-V)=0$ 对所有 $\theta$ 成立。完备性把这一点变成 $\eta=V$ 几乎处处，从而所有条件平均都相同。若只有充分性，可能有多个不同的 $T$ 的无偏函数，Rao–Blackwell 化仍会降低方差，却不能保证得到统一的最优估计。

**老师（拓展）**：找到一个 UMVUE 最实用的方法是什么？为什么 Bernoulli 样本均值符合要求？

**学生**：最实用的是先找完备充分统计量 $T$，再直接构造一个只依赖 $T$ 的无偏估计，或把任意无偏估计对 $T$ 条件平均。Bernoulli 模型中 $T=\sum X_i$ 完备充分，而 $\bar X=T/n$ 的期望为 $\theta$，无需再计算复杂条件期望，所以立即是 $\theta$ 的唯一 UMVUE。

## 相关条目

- [Rao–Blackwell 定理](./Rao-Blackwell定理.md)
- [充分统计量因子分解定理](./充分统计量因子分解定理.md)
