# Rao–Blackwell 定理

> **一句话大白话**：如果某个统计量已经保留了参数的全部信息，就把原估计量在“已知这个统计量”时取条件平均；这样不会增加偏差，还能削掉与参数无关的多余波动。
>
> **小例子**：$X_1,\dots,X_n\overset{\mathrm{iid}}{\sim}\operatorname{Bernoulli}(\theta)$ 时，$X_1$ 是 $\theta$ 的无偏估计，但只用第一个样本太浪费。取 $T=\sum_iX_i$，则 $\mathbb E[X_1\mid T]=T/n=\bar X$，方差从 $\theta(1-\theta)$ 降为 $\theta(1-\theta)/n$。

## 介绍

Rao–Blackwell 定理给出了系统改进估计量的方法：关于充分统计量取条件期望。充分性保证这个新估计量不含未知参数，条件 Jensen 不等式或条件方差分解则保证风险不增。它不要求充分统计量完备；完备性是在 Lehmann–Scheffé 定理中进一步保证唯一最优时才需要。

## 分析

**前置依赖**：充分统计量、条件期望、全期望公式、条件方差、条件 Jensen 不等式、均方误差。

**定理内容**：设统计模型为 $\{P_\theta:\theta\in\Theta\}$，$T(X)$ 是 $\theta$ 的充分统计量，$\delta(X)$ 是实值估计量，并对每个 $\theta$ 有 $\mathbb E_\theta|\delta|<\infty$。定义

$$
\eta(T)=\mathbb E_\theta[\delta(X)\mid T].
$$

由于 $T$ 充分，给定 $T$ 后 $X$ 的条件分布与 $\theta$ 无关，因此可以选择一个不依赖 $\theta$ 的条件期望版本，使 $\eta(T)$ 真正成为不含未知参数的统计量。

该统计量具有以下性质：

1. **期望保持**：对每个 $\theta$，
   $$
   \mathbb E_\theta\eta(T)=\mathbb E_\theta\delta(X).
   $$
   因而两者偏差相同；若 $\delta$ 是 $g(\theta)$ 的无偏估计，则 $\eta$ 也无偏。
2. **凸损失风险不增**：若损失 $L_\theta(\cdot)$ 对估计值为凸函数，且有关风险存在，则
   $$
   R_\theta(\eta)=\mathbb E_\theta L_\theta(\eta(T))
   \leq \mathbb E_\theta L_\theta(\delta(X))=R_\theta(\delta).
   $$
3. **方差与平方误差改进**：若 $\mathbb E_\theta\delta^2<\infty$，则
   $$
   \operatorname{Var}_\theta\eta
   =\operatorname{Var}_\theta\delta
   -\mathbb E_\theta\operatorname{Var}_\theta(\delta\mid T)
   \leq\operatorname{Var}_\theta\delta.
   $$
   因为偏差不变，均方误差也不增。严格来说，若 $\delta\ne\eta(T)$ 以正 $P_\theta$ 概率成立，则该 $\theta$ 处方差和均方误差严格减小。

这里的关键充分条件是：$T$ 必须充分、$\delta$ 必须可积以便定义条件期望；要得到凸损失结论还需损失凸且风险可定义，要引用方差比较则需二阶矩有限。**无偏性不是 Rao–Blackwell 化的必要条件，完备性也不是。**

## 思考过程

条件期望会把同一 $T$ 水平集上的估计值平均掉。全期望公式说明这种平均不改变总体均值；条件 Jensen 不等式说明凸损失的平均不小于平均后的损失。平方损失还可直接通过全方差公式看清改进量恰好是条件方差的期望，永远非负。

## 证明过程

由充分性，$P_\theta(X\in\cdot\mid T)$ 存在不依赖 $\theta$ 的版本，所以 $\eta(T)=\mathbb E[\delta\mid T]$ 是合法统计量。全期望公式立即给出

$$
\mathbb E_\theta\eta
=\mathbb E_\theta\mathbb E[\delta\mid T]
=\mathbb E_\theta\delta.
$$

若 $L_\theta$ 为凸函数，由条件 Jensen 不等式，

$$
\mathbb E[L_\theta(\delta)\mid T]
\geq L_\theta(\mathbb E[\delta\mid T])
=L_\theta(\eta).
$$

两边取期望即得 $R_\theta(\delta)\geq R_\theta(\eta)$。

对于平方损失，也可利用全方差公式：

$$
\operatorname{Var}_\theta(\delta)
=\operatorname{Var}_\theta(\eta)
+\mathbb E_\theta\operatorname{Var}(\delta\mid T).
$$

末项非负，且若 $\delta$ 不是 $P_\theta$-几乎处处等于 $\eta$，末项严格为正。由 $\operatorname{MSE}_\theta(\delta)=\operatorname{Var}_\theta(\delta)+\operatorname{Bias}_\theta(\delta)^2$，且两者偏差相同，得到均方误差的相应不等式与严格性结论。$\square$

## 课堂问答

**老师**：Rao–Blackwell 化的完整操作和保证是什么？

**学生**：对充分统计量 $T$ 和可积估计量 $\delta$，定义 $\eta(T)=\mathbb E[\delta\mid T]$。充分性保证 $\eta$ 不含 $\theta$；全期望公式保证期望与偏差不变；凸损失下风险不增，二阶矩有限时方差不增，平方误差也因偏差不变而不增。若原估计量无偏，新估计量仍无偏。

**老师（追问）**：为什么必须要求 $T$ 充分？是否还要假设 $T$ 完备、$\delta$ 无偏？

**学生**：若不充分，$\mathbb E_\theta[\delta\mid T]$ 可能依赖 $\theta$，就不能作为只由数据计算的估计量。完备性不需要，它用于后续的 Lehmann–Scheffé 唯一最优结论；无偏性也不需要，Rao–Blackwell 化对一般有偏估计仍保持偏差并降低方差，只是在无偏估计类中尤其常用。

**老师（拓展）**：方差严格减少的量是什么？能否用它解释 $\bar X$ 对 $X_1$ 的改进？

**学生**：减少量是 $\mathbb E_\theta\operatorname{Var}(\delta\mid T)$，即给定 $T$ 后残余波动的平均。Bernoulli 样本中，给定 $T=t$ 时 $X_1$ 仍以概率 $t/n$ 取 $1$，所以原估计有残余波动；取条件均值后成为 $T/n$，把这层波动完全消去，方差恰缩小为原来的 $1/n$。

## 相关条目

- [充分统计量因子分解定理](./充分统计量因子分解定理.md)
- [Lehmann–Scheffé 定理](./Lehmann-Scheffé定理.md)
- [全期望公式](../第24级-概率论基础/全期望公式.md)：直接前置依赖。
- [Jensen 不等式](../第24级-概率论基础/Jensen不等式.md)：直接前置依赖。
