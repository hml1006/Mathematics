# 离散 Morse 理论（Forman）

> **一句话大白话**：给构成空间的每个小方块记一个数字，把"没有意义"的方块两两配对消掉，剩下少数几个"关键方块"就决定了这个空间长什么样——只留下精华，计算量大为减小。
>
> **小例子**：对一张已三角剖分的曲面，指定一个离散 Morse 函数；配对数（critical cells）满足 $\# c_0-\# c_1+\# c_2=\chi$，且关键胞腔可拼出同伦等价的空间。

## 一、定理介绍

离散 Morse 理论由 Robin Forman 提出，是光滑 Morse 理论的细胞/单纯复形版本。它通过在每个胞腔（cell）上赋值，把复形中“非临界”的胞腔两两配对并消去，从而把原复形的同伦类型归结为仅由临界胞腔构成的更小的 Morse 复形。该理论极大地简化了代数拓扑计算，并在拓扑数据分析、图论与组合学中有广泛应用。

## 二、原理思路

1. **离散 Morse 函数**：在有限 CW 复形 $K$ 的胞腔集上定义实值函数 $f$，使得对每个 $p$ 维胞腔 $\sigma$，满足以下二者之一的 $(p-1)$ 维面 $\tau$（$\tau<\sigma$）最多一个：$f(\tau)\ge f(\sigma)$；以及满足以下二者之一的 $(p+1)$ 维胞腔 $\nu$（$\sigma<\nu$）最多一个：$f(\nu)\le f(\sigma)$。
2. **正则对与临界胞腔**：若存在这样的 $\tau$ 与 $\sigma$ 使得 $\tau<\sigma$ 且 $f(\tau)\ge f(\sigma)$，则 $(\tau,\sigma)$ 称为正则配对（regular pair），可从复形中消去；未被配对的胞腔称为临界胞腔（critical cell）。
3. **Morse 复形**：所有临界胞腔生成一个新的链复形，其边界算子由原复形中沿梯度路径（gradient path）的胞腔配对计数给出。

## 三、定理的严格表述

设 $K$ 为有限 CW 复形，$f: K^{(\mathrm{cells})} \to \mathbb{R}$ 为离散 Morse 函数。称胞腔 $\sigma$ 是临界的，若它既不存在满足 $f(\tau)\ge f(\sigma)$ 的余一维面 $\tau<\sigma$，也不存在满足 $f(\nu)\le f(\sigma)$ 的余一维 coface $\nu>\sigma$。

**Forman 定理**：$K$ 同伦等价于一个 CW 复形 $K'$，其中 $K'$ 对每个 $p$ 维临界胞腔恰有一个 $p$ 维胞腔，且没有其他胞腔。换言之，
$$
K \simeq K' = \bigvee_{\sigma \text{ critical}} e^{\dim\sigma}_{\sigma},
$$
更精确地，$K'$ 的胞腔分解中 $p$ 维胞腔数等于 $K$ 的 $p$ 维临界胞腔数 $m_p$。

进一步，可构造 Morse 复形 $(C_*^{\mathcal{M}}, \partial^{\mathcal{M}})$，其中 $C_p^{\mathcal{M}}$ 由 $p$ 维临界胞腔生成的自由 Abel 群（或 $\mathbb{F}$ 向量空间），边界 $\partial_p^{\mathcal{M}}$ 定义为
$$
\partial_p^{\mathcal{M}}(\sigma) = \sum_{\tau \text{ critical},\, \dim\tau=p-1} n(\sigma,\tau)\, \tau,
$$
这里 $n(\sigma,\tau)$ 是连接 $\sigma$ 到 $\tau$ 的梯度路径数（模 2 或按定向取符号）。该 Morse 复形的同调群与原复形同构：
$$
H_*(C_*^{\mathcal{M}}) \cong H_*(K).
$$

## 四、证明过程

**步骤 1：正则配对的可消去性。**
若 $(\tau,\sigma)$ 是正则对，且 $\tau$ 是 $\sigma$ 的余一维面，则 $K$ 可通过对 $\sigma$ 作基本坍缩（elementary collapse）沿 $\tau$ 消去这对胞腔。由 Whitehead 定理，基本坍缩保持简单同伦型，因而保持同伦型。

**步骤 2：所有正则对可被同时消去。**
离散 Morse 函数的定义保证正则对之间不存在循环依赖：沿面–coface 关系定义的偏序不会出现闭合链。因此可按函数值递增顺序逐个或批量消去所有正则对，最终留下仅由临界胞腔构成的复形 $K'$。

**步骤 3：Morse 复形的构造。**
把原链复形 $C_*(K)$ 按离散 Morse 函数的正则对分裂为 $C_*^{\mathrm{matched}} \oplus C_*^{\mathrm{critical}}$。正则对的边界子矩阵可逆，因此可用链同伦把 $C_*^{\mathrm{matched}}$ 缩掉。诱导的边界算子正是由临界胞腔之间的梯度路径计数给出。该链映射与原包含映射互为链同伦等价，从而同调同构。

**步骤 4：强 Morse 不等式。**
由 Morse 复形的存在性，可得弱/强 Morse 不等式：对任意 $n$，
$$
\sum_{p=0}^{n} (-1)^{n-p} m_p \ge \sum_{p=0}^{n} (-1)^{n-p} \beta_p,
$$
其中 $m_p$ 为临界 $p$ 胞腔数，$\beta_p$ 为 Betti 数；取 $n=\dim K$ 时等号成立，即欧拉示性数相等。

## 五、应用与意义

- **计算简化**：离散 Morse 理论可把大规模单纯复形的计算规模降低数个数量级，是持久同调软件中常用的预处理技术。
- **组合结构**：在图论和组合拓扑中，离散 Morse 函数常用于证明欧拉特征公式、Kneser 猜想等。
- **数据分析**：通过选取合适的 Morse 函数，可提取数据的“骨架”与下降流形，用于聚类、流形学习与可视化。
