# Matsumoto 定理

> **一句话大白话**：对域 $F$，$K_2(F)$ 完全由符号 $\{a,b\}$（$a,b\in F^\times$）生成，只需满足双线性性和 Steinberg 关系 $\{a,1-a\}=1$——这相当于给 $K_2(F)$ 提供了"生成与关系"的显式展示。
>
> **小例子**：对有限域 $\mathbb{F}_q$，乘法群循环，可证所有 $\{a,b\}=1$，故 $K_2(\mathbb{F}_q)=1$；对 $\mathbb{Q}$ 则有 $K_2(\mathbb{Q})\cong\{\pm1\}\oplus\bigoplus_p(\mathbb{Z}/2\mathbb{Z})_p$。

## 一、定理介绍

> **前置依赖**：Steinberg 群与初等矩阵群、$K_2(F)$ 的定义、Steinberg 关系、群同态的泛性质。

Matsumoto 定理将 $K_2(F)$（Steinberg 群 $St(F)\to E(F)$ 的核）完全显式化：它由符号生成并满足上述关系，还给出泛性质。这把抽象的 $K_2$ 转化为域上的组合数据，是代数 K 理论与数论（二次互反律、Milnor K 理论）之间的关键桥梁。

## 二、原理思路

证明分三步。先用 Weyl 元素 $w_{ij}(a)=x_{ij}(a)x_{ji}(-a^{-1})x_{ij}(a)$ 与 $h_{ij}(a)=w_{ij}(a)w_{ij}(-1)$ 构造符号 $\{a,b\}=[h_{ij}(a),h_{ik}(b)]\in St(F)$，并验证它在 $\varphi$ 下的像为 $1$（故落在 $K_2(F)$）；再验证双线性与 Steinberg 关系；最后由泛性质唯一确定整个群。

## 三、定理的严格表述

设 $F$ 为域。则 $K_2(F)$ 由符号 $\{a,b\}$（$a,b\in F^\times$）生成，满足以下关系：
1. **双线性性：** $\{a_1a_2,b\}=\{a_1,b\}\{a_2,b\}$，$\{a,b_1b_2\}=\{a,b_1\}\{a,b_2\}$。
2. **Steinberg 关系：** $\{a,1-a\}=1$ 对 $a\neq0,1$。

**泛性质：** 设 $A$ 为阿贝尔群，$\psi:F^\times\times F^\times\to A$ 为双线性映射且满足 $\psi(a,1-a)=1$，则存在唯一群同态 $\tilde{\psi}:K_2(F)\to A$ 使 $\tilde{\psi}(\{a,b\})=\psi(a,b)$。

## 四、证明过程

**证明：**

**第一步：构造映射 $F^\times\times F^\times\to K_2(F)$。** 定义 $w_{ij}(a)=x_{ij}(a)x_{ji}(-a^{-1})x_{ij}(a)$，$h_{ij}(a)=w_{ij}(a)w_{ij}(-1)$；可证 $\varphi(h_{ij}(a))=\operatorname{diag}(a,a^{-1},1,\dots,1)$。令 $\{a,b\}=[h_{ij}(a),h_{ik}(b)]$（$i,j,k$ 互异），则 $\varphi(\{a,b\})=1$，故 $\{a,b\}\in K_2(F)$。

**第二步：验证关系。**
- 双线性性来自 $h_{ij}(ab)=h_{ij}(a)h_{ij}(b)$：$[h_{ij}(ab),h_{ik}(c)]=[h_{ij}(a)h_{ij}(b),h_{ik}(c)]=\{a,c\}\{b,c\}$。
- Steinberg 关系利用恒等式 $w_{ij}(a)x_{ij}(1-a)w_{ij}(a)^{-1}=x_{ji}((a-1)/a)$，经 $St(F)$ 内计算得 $\{a,1-a\}=1$。

**第三步：泛性质。** 对满足条件的 $\psi$，存在唯一群同态 $\tilde{\psi}$ 使 $\tilde{\psi}(\{a,b\})=\psi(a,b)$，从而 $K_2(F)$ 由生成元与关系唯一确定。$\square$

## 五、应用与意义

Matsumoto 定理是 $K_2$ 研究的枢纽。它使计算 $K_2(F)$ 如同处理"符号代数"，并导向 Milnor K 理论（$K_n^M(F)$）与 Bloch-Lichtenbaum 的模猜想。由它可算出 $K_2(\mathbb{F}_q)=1$、$K_2(\mathbb{Q})$ 的结构，且 $K_2$ 与二次互反律、Hilbert 符号、Norm 剩余符号及 Galois 上同调（Hilbert 定理 90 的推广）紧密相连，是类域论、代数几何与 K 理论在数论问题中交汇的工具。

## 课堂问答

**老师**：$K_2(F)$ 结构相当抽象，Matsumoto 定理怎样把它变成"可算"的对象？

**学生**：结论是 $K_2(F)$ 由符号 $\{a,b\}$（$a,b\in F^\times$）生成，只有两类关系：双线性 $\{a_1a_2,b\}=\{a_1,b\}\{a_2,b\}$，以及 Steinberg 关系 $\{a,1-a\}=1$。它还带泛性质：任何满足这两条的双线性 $\psi:F^\times\times F^\times\to A$ 唯一地经过 $K_2(F)$ 分解。

**老师（追问）**：符号 $\{a,b\}$ 凭什么落在 $K_2(F)=\ker(St(F)\to E(F))$ 里？

**学生**：用 Weyl 元素 $w_{ij}(a)=x_{ij}(a)x_{ji}(-a^{-1})x_{ij}(a)$、$h_{ij}(a)=w_{ij}(a)w_{ij}(-1)$，可算出 $\varphi(h_{ij}(a))=\operatorname{diag}(a,a^{-1},1,\dots,1)$。再令
$$
\{a,b\}=[h_{ij}(a),h_{ik}(b)],
$$
对角矩阵相互交换，故它的像为 $1$，即属于核 $K_2(F)$。

**老师（拓展）**：拿它算几个具体的 $K_2$，顺带说说常见误区。

**学生**：有限域 $\mathbb{F}_q$ 的乘法群循环，由双线性可推所有符号 $\{a,b\}=1$，故 $K_2(\mathbb{F}_q)=1$；对 $\mathbb{Q}$ 则有 $K_2(\mathbb{Q})\cong\{\pm1\}\oplus\bigoplus_p(\mathbb{Z}/2\mathbb{Z})_p$。误区是以为 Steinberg 关系只是"额外技术条件"，其实它正是把 $K_2$ 与 Hilbert 符号、二次互反律连起来的核心。
