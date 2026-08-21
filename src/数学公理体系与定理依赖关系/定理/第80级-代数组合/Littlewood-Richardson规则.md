# Littlewood-Richardson 规则

> **一句话大白话**：两个 Schur 函数的乘积仍可拆成 Schur 函数的和，系数 $c_{\lambda\mu}^\nu$ 是非负整数，等于"把 $\mu$ 的格子按 LR 条件镶到 $\lambda$ 旁边得到 $\nu$"的填数方式数。"乘积系数 = 组合填法数"。
>
> **小例子**：$s_{(2)}\cdot s_{(1)}=s_{(3)}+s_{(2,1)}$，系数 $c_{(2)(1)}^{(3)}=1$、$c_{(2)(1)}^{(2,1)}=1$：把一行加一格可以拼出 $(3)$ 或 $(2,1)$，各 1 种方式。

## 一、定理介绍

> **前置依赖**：Schur 函数与半标准 Young 表、Skew Schur 函数、Yamanouchi 词（逆格序词）、Young 图的形状与填数规则。

Littlewood-Richardson 规则用一个显式的组合计数给出 Schur 函数乘积的展开系数 $c_{\lambda\mu}^\nu$（Littlewood-Richardson 系数）。这些系数出现在对称函数、$GL_n$ 与 $S_n$ 表示张量积、以及代数簇（Schubert 微）之中，是组合与表示论交汇的中心量。

## 二、原理思路

将问题化为 Skew Schur 函数 $s_{\nu/\lambda}=\sum_\mu c_{\lambda\mu}^\nu s_\mu$。$s_{\nu/\lambda}$ 是形状 $\nu/\lambda$ 的半标准 Young 表权重和 $s_{\nu/\lambda}=\sum_{T\in\text{SSYT}(\nu/\lambda)}x^T$。获 $c_{\lambda\mu}^\nu$ 需抽取 $s_\mu$ 的系数：逐行读表得词 $w(T)$，当其（右边起）为逆格序词（Yamanouchi 词：任一前缀中 $i$ 的次数 $\ge i+1$ 的次数）时，对应 $s_\mu$ 的贡献，从而 $c_{\lambda\mu}^\nu$ 等于如此 LR 填写的个数。

## 三、定理的严格表述

系数 $c_{\lambda\mu}^\nu$ 定义为 $s_\lambda\cdot s_\mu=\sum_\nu c_{\lambda\mu}^\nu s_\nu$。Littlewood-Richardson 规则：$c_{\lambda\mu}^\nu$ 等于把 $\mu$ 的 Young 图（格子带数字 $1,2,3,\dots$）镶补到 $\lambda$ 的 Young 图旁边得到 $\nu$ 的方式数，满足：
1. 每次加一格均保持 Young 图形状；
2. 逐行读出（自右向左、自上而下）的数字序列是逆格序词，即任一前缀中 $i$ 的出现次数不少于 $i+1$ 的出现次数；
3. 同行不严格递减，同列严格递增（即在 $\nu/\lambda$ 中构成反格序标准填）。

## 四、证明过程

**证明思路：**

**步骤 1：转为 Skew Schur。** $s_{\nu/\lambda}=\sum_\mu c_{\lambda\mu}^\nu s_\mu$，故 $c_{\lambda\mu}^\nu$ 是 $s_{\nu/\lambda}$ 中 $s_\mu$ 的系数。$\blacksquare$

**步骤 2：SSYT 加权和。** $s_{\nu/\lambda}=\sum_{T\in\text{SSYT}(\nu/\lambda)}x^T$，$x^T=\prod_i x_i^{m_i(T)}$，$m_i(T)$ 为 $i$ 在 $T$ 中的次数。$\blacksquare$

**步骤 3：抽取 $s_\mu$ 系数。** 把 $s_{\nu/\lambda}$ 用单表上的 Young 组合展开（Kostka 对），$s_\mu$ 由权重为 $\mu$（即 $m_i$ 组成 $\mu$）且满足 LR 条件的表格贡献。具体地，对每个权重组成 $\mu$ 的 LR 表格贡献恰对应一个 $s_\mu$。$\blacksquare$

**步骤 4：一一对应。** 每个满足 LR 条件的表格（其数字 $i$ 总数为 $\mu_i$）与 $c_{\lambda\mu}^\nu$ 的一个单位贡献对应，且映射双射，故 $c_{\lambda\mu}^\nu$ 等于这样表格的个数。$\square$

**注：** 上述"抽取系数"需用同位族表格与 Yamanouchi 词的标准论证（把 $s_{\nu/\lambda}$ 词的逆格序条件与 $\{s_\mu\}$ 基里的单调性匹配），其准确性由 RSK/双向词理论保证。

## 五、应用与意义

Littlewood-Richardson 系数贯穿组合与表示：$GL_n$ 与 $S_n$ 张量积分解、对称函数乘法、Schubert 计算的交积、行列式匹配置（双杨表恒等式）。LR 规则提供这些抽象的显式组合计数，是计算代数与枚举组合的核心算法。其验证与更深的勾稽（crystal、Lascoux-Schützenberger）构成现代组合表示论的活跃主题。