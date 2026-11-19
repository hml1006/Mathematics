# Dold-Kan 对应

> **一句话大白话**：单纯阿贝尔群看似装着许多“重复退化的单形”，链复形则只保留真正能产生同调的规范化部分；把退化部分系统地丢掉、又能按所有退化方式装回去，两边其实是同一个数学对象的两种表达。
>
> **小例子**：若链复形只有 $C_0=M$、$C_1=N$、边缘 $\partial:N\to M$，其余为 $0$，则其对应单纯对象的第 $0$ 层是 $M$，第 $1$ 层是 $M\oplus N$，第 $2$ 层是 $M\oplus N\oplus N$：多出的两个 $N$ 对应 $[2]\twoheadrightarrow[1]$ 的两种保序满射。

## 介绍

Dold-Kan 对应把组合同伦论与同调代数连接起来。对任意 Abel 范畴 $\mathcal A$，非负链复形范畴 $\mathrm{Ch}_{\geq0}(\mathcal A)$ 与单纯对象范畴 $s\mathcal A=\mathcal A^{\Delta^{\mathrm{op}}}$ 通过规范化链函子 $N$ 和逆方向的 $\Gamma$ 函子等价。它不只是在对象集合上建立一一对应，而是保持态射、自然变换，并把单纯同伦群对应到链复形同调。

## 分析

**前置依赖**：Abel 范畴、链复形及链映射、单纯范畴 $\Delta$、面映射与退化映射、单纯对象、核与直和、规范化 Moore 复形。

**定理内容**：对单纯对象 $A_\bullet\in s\mathcal A$，其非规范化链复形为

$$
C_n(A)=A_n,
\qquad
\partial=\sum_{i=0}^n(-1)^i d_i:A_n\to A_{n-1}.
$$

取规范化子复形

$$
N_n(A)=\bigcap_{i=0}^{n-1}\ker(d_i:A_n\to A_{n-1}),
\qquad N_0(A)=A_0,
$$

并以最后面映射 $d_n$ 为微分

$$
\partial_N=d_n:N_n(A)\to N_{n-1}(A).
$$

采用 $\partial_N=(-1)^n d_n$ 的等价符号约定也很常见；两种规范化复形通过逐项变号自然同构。单纯恒等式保证 $d_n$ 确实把 $N_n(A)$ 映入 $N_{n-1}(A)$，且 $\partial_N^2=0$。

反方向函子 $\Gamma$ 在第 $n$ 层由

$$
\boxed{
\Gamma(C)_n
=\bigoplus_{\substack{[n]\twoheadrightarrow[k]\\
0\leq k\leq n}}C_k
}
$$

给出，直和遍历 $\Delta$ 中所有以 $[n]$ 为定义域的保序满射；面与退化结构由这些满射的复合以及 $C$ 的链微分自然诱导。

**Dold-Kan 定理**：函子

$$
N:s\mathcal A\longrightarrow\mathrm{Ch}_{\geq0}(\mathcal A),
\qquad
\Gamma:\mathrm{Ch}_{\geq0}(\mathcal A)\longrightarrow s\mathcal A
$$

互为逆等价，即存在自然同构

$$
N\Gamma(C)\cong C,
\qquad
\Gamma N(A)\cong A.
$$

并且对任意单纯对象 $A$，

$$
\boxed{\pi_n(A,0)\cong H_n(N(A)),\qquad n\geq0.}
$$

特别地，$\mathcal A=\mathbf{Ab}$ 时，单纯阿贝尔群都是 Kan 复形，其通常单纯同伦群与规范化链复形的同调群一致。

## 思考过程

非规范化复形把每个 $A_n$ 全保留下来，因此同一非退化信息的各个退化副本会重复出现。规范化交核把“还能被某个前面面映射看见”的退化方向消去，只留下 Moore 复形中的新信息。关键不是随意丢弃，而是证明退化部分确实构成一个互补直和项。

反过来，要从链复形重建第 $n$ 层，就必须为每个源次数 $k\leq n$ 补上它到达第 $n$ 层的所有退化方式。$\Delta$ 中的保序满射 $[n]\twoheadrightarrow[k]$ 正好枚举这些方式，所以 $\Gamma(C)_n$ 的直和指标不是人为排列，而是单纯范畴自身的组合结构。规范化时，所有真正经过退化的直和项都消失，只剩恒等满射 $[n]\to[n]$ 对应的 $C_n$。

## 证明过程

### 1. 分离退化部分

令 $D_n(A)\subseteq A_n$ 为所有退化映射像所生成的子对象，即由

$$
s_j(A_{n-1})\subseteq A_n,
\qquad 0\leq j\leq n-1
$$

生成的退化部分。利用单纯恒等式

$$
d_is_j=
\begin{cases}
s_{j-1}d_i,&i<j,\\
\operatorname{id},&i=j,j+1,\\
s_jd_{i-1},&i>j+1,
\end{cases}
$$

可构造投影并证明非规范化复形的 Moore 分解

$$
C_n(A)\cong N_n(A)\oplus D_n(A).
$$

且 $D_\bullet(A)$ 是同调为零的退化子复形。这一步说明 $N(A)$ 保留了 $C(A)$ 的全部同调，而退化部分不贡献同调。

### 2. 验证 $\Gamma$ 后再规范化

考察 $\Gamma(C)_n$ 的一个直和项，其指标为 $\sigma:[n]\twoheadrightarrow[k]$。若 $k<n$，则 $\sigma$ 可分解为一个余退化与后续满射，对应项落在退化子对象中，经过规范化后为零。若 $k=n$，唯一保序满射是 $\operatorname{id}_{[n]}$。故

$$
N_n(\Gamma C)\cong C_n.
$$

规范化微分只保留最后面映射；在唯一非退化直和项上，它正是原复形的 $\partial:C_n\to C_{n-1}$。这些同构与链映射相容，得到自然同构 $N\Gamma\cong\operatorname{id}$。

### 3. 从单纯对象重建所有层

对 $A\in s\mathcal A$，利用第 1 步的退化—规范化分解，把 $A_n$ 按满射 $\sigma:[n]\twoheadrightarrow[k]$ 分解为规范化部分 $N_k(A)$ 的各退化副本。逐项比较可得自然同构

$$
A_n\cong
\bigoplus_{[n]\twoheadrightarrow[k]}N_k(A)
=\Gamma(N(A))_n.
$$

单纯恒等式进一步说明该同构与所有面映射、退化映射相容，故是单纯对象的同构，并给出 $\Gamma N\cong\operatorname{id}$。

### 4. 同伦与同调的识别

单纯阿贝尔群（更一般地，Abel 范畴中的相应内部同伦表述）的同伦类可用规范化 Moore 链表示：两个规范化 $n$-链同伦，当且仅当它们相差一个规范化边界。因此

$$
\pi_n(A,0)=Z_n(N(A))/B_n(N(A))=H_n(N(A)).
$$

至此，对象、态射及基本同伦不变量都完成了对应。$\square$

## 课堂问答

**老师**：Dold-Kan 对应的两个范畴是什么，规范化函子具体怎样定义？

**学生**：它给出 $s\mathcal A$ 与 $\mathrm{Ch}_{\geq0}(\mathcal A)$ 的范畴等价。规范化取 $N_n(A)=\bigcap_{i=0}^{n-1}\ker d_i$、$N_0(A)=A_0$，以 $d_n$ 为微分；逆函子为 $\Gamma(C)_n=\bigoplus_{[n]\twoheadrightarrow[k]}C_k$，并有 $N\Gamma\cong\mathrm{id}$、$\Gamma N\cong\mathrm{id}$。

**老师（追问）**：为什么 $\Gamma$ 的直和要用保序满射编号，而不能每个 $C_k$ 只复制一次？

**学生**：因为从第 $k$ 层到第 $n$ 层的退化方式本身由 $\Delta$ 中的满射记录，不同满射代表不同退化路径，重建时都必须保留。规范化后，$k<n$ 的项都落入退化部分并消失，只有恒等满射对应的 $C_n$ 留下，所以恰好恢复原链复形。

**老师（拓展）**：Dold-Kan 是否把所有关于单纯对象的结构都原样变成普通链复形结构？

**学生**：它保持范畴、态射和同伦/同调信息，给出 $\pi_n(A,0)\cong H_n(N(A))$，但不意味着任意额外结构都无需修正地严格对应。例如乘法结构涉及 Alexander-Whitney、Eilenberg-Zilber 等比较映射，通常要讨论 lax/oplax 或同伦相干性，不能仅由“范畴等价”一句话推出严格monoidal等价。

## 相关条目

- [单纯集与 Quillen 模型结构](./单纯集与Quillen模型结构.md)
- [Alexander-Whitney 映射与 Eilenberg-Zilber 定理](../第34级-代数拓扑/Alexander-Whitney映射与Eilenberg-Zilber定理.md)
- [导出函子 Ext 和 Tor](../第35级-同调代数/导出函子Ext和Tor.md)
- [同伦极限与同伦余极限](./同伦极限与同伦余极限.md)
- [Abel 范畴](../第47级-高等范畴论/Abel范畴.md)：直接前置依赖。
