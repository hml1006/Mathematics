# Robinson-Schensted 对应

> **一句话大白话**：任意一个置换都可以被唯一地"整理"成一对形状相同的标准 Young 表 $(P,Q)$：插入表 $P$ 记录排列，记录表 $Q$ 记录每个数字何时被放入。整个 $S_n$ 与"同形状双标准表"构成一一对应。
>
> **小例子**：置换 $\pi=3142$ 经 RSK 算法得插入表 $P=\begin{smallmatrix}1&2\\3&4\end{smallmatrix}$ 与记录表 $Q=\begin{smallmatrix}1&3\\2&4\end{smallmatrix}$（形状 $(2,2)$）。故存在双射 $S_4\leftrightarrow\bigcup_{\lambda\vdash4}\text{SYT}(\lambda)\times\text{SYT}(\lambda)$。

## 一、定理介绍

> **前置依赖**：Young 图与标准 Young 表、RSK 插入算法、钩长公式。

Robinson-Schensted 对应（RS 对应，RSK 算法）建立 $S_n$ 与 $\bigcup_{\lambda\vdash n}\text{SYT}(\lambda)\times\text{SYT}(\lambda)$ 之间的一一对应，把每个置换 $\pi$ 映射到一对同形状的标准 Young 表。它揭示 $n!=\sum_{\lambda\vdash n}(f^\lambda)^2$，是组合与表示论最深刻的统一对应之一。

## 二、原理思路

用 RSK 插入算法。"玩挤牌"式插入：把 $\pi_k$ 从第一行往里插——找到行中第一个比它大的元素并替换、把被替换者挤到下一行递归，无处可挤就放行尾；同时在被放的新格位置向记录表 $Q$ 写 $k$。逐项处理得 $P,Q$。可逆性由"反过来找最大记录元素逆向吸回"证明，双向算法互逆故为双射。

## 三、定理的严格表述

对每个 $\pi\in S_n$，RSK 算法给出唯一一对同形状标准 Young 表 $(P,Q)$，从而
$$\text{RS}:S_n\,\xrightarrow{\,\sim\,}\,\bigcup_{\lambda\vdash n}\text{SYT}(\lambda)\times\text{SYT}(\lambda),\qquad n!=\sum_{\lambda\vdash n}(f^\lambda)^2,$$
其中 $f^\lambda=|\text{SYT}(\lambda)|=\#\{\text{形状 }\lambda\text{ 的标准表}\}$ 由钩长公式 $f^\lambda=\frac{n!}{\prod_{(i,j)\in\lambda}\text{hook}(i,j)}$ 给出。

## 四、证明过程

**证明（RSK 算法）：**

**步骤 1：算法描述。** 初始化 $P=Q=\varnothing$。对 $k=1,\dots,n$：(a) 将 $\pi_k$ 插入 $P$——从第一行起，找到该行首个 $>\pi_k$ 的元素 $x$，用 $\pi_k$ 替换之，并将 $x$ 递归插入下一行；若行中无更大元素（或行满），将 $\pi_k$ 加在行尾。(b) 在 $Q$ 中与 $P$ 新增格相同位置填入 $k$。$\blacksquare$

**步骤 2：结果为 SYT。** $P$ 每行：替换算法保行内严格递增（$a$ 代 $b$（$a<b$）时 $b$ 下移，原位左右保持序）。列方向：归纳证插入不破坏列递增（挤插保持严格）。$Q$ 填 $1,2,\dots,n$，因 $k$ 递增且格位是 $P$ 已有格位，$Q$ 行、列均严格递增。$\blacksquare$

**步骤 3：可逆性。** 给定 $(P,Q)$：找 $Q$ 中最大元素 $k$ 所在位置，在 $P$ 同位置取出元素（它是最后插入的），逆向"从上线逆向挤"直至第一行得 $\pi_k$，从 $Q$ 删 $k$。循环即恢复 $\pi$。$\blacksquare$

**步骤 4：双射。** 正、逆算法皆确定性互逆，故 RS 对应为双射。由此 $|S_n|=n!=\sum_{\lambda\vdash n}(f^\lambda)^2$，$f^\lambda$ 另由钩长公式计算。$\square$

## 五、应用与意义

RSK 对应是组合表示论的核心工具：它给出置换与标准表的双射、钩长公式（$f^\lambda$）、Schensted 插入与最长递增子序列的联系（对应 $\lambda_1$ 为最长递增子序列长度），并用于对数凸与长 Bijection 的改进。RSK 还推广到矩阵（矩阵-PRoux）、词，与对称函数、crystal 理论、Young 表相交织，连接 Ulam 问题、随机矩阵理论（Tracy-Widom）与可积概率。