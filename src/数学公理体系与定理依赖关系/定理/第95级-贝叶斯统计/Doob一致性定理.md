# 后验分布的正则性（Doob 一致性定理）

> **一句话大白话**：只要先验没有"故意漏掉"真相，随着数据越来越多，后验分布会把概率质量都集中在真实参数附近——贝叶斯估计几乎总是能"学对"。
>
> **小例子**：用一个不太离谱的先验估计某产品的次品率，样本越积越多，后验分布越来越紧地贴住真实次品率。

## 一、定理介绍

设观测 $\boldsymbol{x}_n=(x_1,\dots,x_n)$ 独立同分布于 $P_{\theta_0}$，先验为 $\pi$。则对几乎所有 $\theta_0$（在先验支集上，除去可识别性问题对应的零测集），后验 $\pi(\theta\mid\boldsymbol{x}_n)$ 在 $\theta_0$ 处一致：

$$
\pi(\theta\in U\mid\boldsymbol{x}_n) \xrightarrow[n\to\infty]{P_{\theta_0}} 1 \quad\text{对 }\theta_0\text{ 的任何邻域 }U.
$$

## 二、原理思路

依赖关于真实 $\theta_0$ 的似然比鞅与 Kullback-Leibler 散度。固定 $\theta$ 时似然比 $L_n(\theta)$ 是鞅，故几乎必然收敛；由大数定律 $\frac1n\log L_n(\theta)\to -K(\theta_0,\theta)<0$（$\theta\neq\theta_0$），从而 $L_n(\theta)\to0$，说明掉在真实点之外的先验"权重"在似然比的缩放下消失。

## 三、定理的严格表述

定义似然比 $L_n(\theta)=\prod_{i=1}^n\frac{f(x_i\mid\theta)}{f(x_i\mid\theta_0)}$ 与 KL 散度 $K(\theta_0,\theta)=\mathbb{E}_{\theta_0}\big[\log\frac{f(x\mid\theta_0)}{f(x\mid\theta)}\big]$。则对 $\pi$-几乎所有 $\theta_0$（满足 $K(\theta_0,\theta)>0$ 对所有 $\theta\neq\theta_0$），有

$$
\pi(\theta\in U\mid\boldsymbol{x}_n) = \frac{\int_U L_n(\theta)\pi(d\theta)}{\int_\Theta L_n(\theta)\pi(d\theta)} \to 1 \quad(\text{a.s.}).
$$

## 四、证明过程

1. **鞅构造**：对固定 $\theta$，$\mathbb{E}_{\theta_0}\big[\frac{f(x\mid\theta)}{f(x\mid\theta_0)}\big]=1$，故 $L_n(\theta)$ 是鞅。
2. **大数定律**：$\frac1n\log L_n(\theta)\to -K(\theta_0,\theta)<0$，故 $L_n(\theta)\to0$ a.s. 对 $\theta\neq\theta_0$。
3. **邻域划分**：将 $U^c$ 分解为可数紧集，每个紧集上 $\int L_n\pi\to0$。
4. **结论**：分子（$U^c$ 上的权重）趋于 0，分母（全空间积分）有正下界，故后验质量集中在 $U$。
5. **例外集**：使 $K(\theta_0,\theta_1)=0$（不可区分）的 $\theta_0$ 组成先验零测集。

## 五、应用与意义

Doob 一致性定理从原理上保证了贝叶斯方法"数据足够时收敛到真相"，为贝叶斯推断提供了大样本合理性。它给出的是关于先验"几乎所有"点成立的一致性（不要求正则性条件），比频率的逐点一致性更宽松，并与频率大样本理论（如后验正态性 Bernstein-von Mises）衔接。