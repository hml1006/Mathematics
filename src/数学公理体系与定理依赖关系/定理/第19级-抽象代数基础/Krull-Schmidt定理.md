# Krull-Schmidt 定理

> **一句话大白话**：把一块积木拆成"不可再分的零件"的直和，无论怎么拆，零件清单（到同构）都唯一——数目相同，种类一一对应。

> **小例子**：$12=2^2\cdot3$ 是整数版的唯一分解；在 $\mathbb Z$ 上看模，$\mathbb Z/12\cong\mathbb Z/4\oplus\mathbb Z/3$，拆出的不可分解块 $\mathbb Z/4$、$\mathbb Z/3$ 在同构意义（含次序）下唯一。

## 介绍

唯一分解是人类对"结构"最古老的信念：整数分解为素因子、多项式分解为不可约因子，都说明"零件清单"是对象的指纹。但当分解从数推广到模、群、表示等一般代数对象时，"不可再分"（不可分解）比"素"更弱，此时唯一性还能否成立？这就是 Krull–Schmidt 问题。Wolfgang Krull 与 Otto Schmidt 在 1920 年代前后分别对阿廷模与有限长度模给出肯定回答，Wedderburn 在更早的有限维代数情形已证类似结论，故该定理也称 Krull–Remak–Schmidt 定理。

定理断言：只要模的"长度"有限，任何分解为不可分解模直和的方式都给出同构意义下唯一的因子多重集。它是代数表示论、Jordan–Hölder 型理论、有限群表示与持久同调中"分解为积木块"这套语言的合法性依据；对有限生成 Abel 群、有限维半单代数的模、箭图表示的分类都不可或缺。

## 分析

**前置依赖**：不可分解模与局部环、幂等元与直和分解、模的有限长度与合成列、环同态基本定理、模的直和与投影。

**定理内容**：设模 $M$ 具有有限长度（即存在有限合成列，等价于 $M$ 既是 Artin 模又是 Noether 模），且
$$
M=M_1\oplus\cdots\oplus M_r=N_1\oplus\cdots\oplus N_s,
$$
其中每个 $M_i,N_j$ 都是非零不可分解模。则 $r=s$，且存在置换 $\sigma$ 使 $M_i\cong N_{\sigma(i)}$（$i=1,\dots,r$）。

证明的枢纽是 Fitting 分解：对有限长度模 $M$ 与自同态 $f$，链 $\ker f\subseteq\ker f^2\subseteq\cdots$ 与 $\mathrm{im}\,f\supseteq\mathrm{im}\,f^2\supseteq\cdots$ 都在某个 $n$ 处稳定，于是 $M=\ker f^n\oplus\mathrm{im}\,f^n$。由此可证不可分解模的自同态环是局部环，再借助"局部环中诸元之和为单位则至少一项为单位"这一简单事实，在两个分解之间构造出把 $M_1$ 同构地送到某个 $N_j$ 的映射，最后用消去法归纳。

## 思考过程

第一，为什么需要"有限长度"？Fitting 分解依赖两个链的稳定：$\ker f^n$ 递增需要 Noether 性，$\mathrm{im}\,f^n$ 递减需要 Artin 性。有限长度同时提供两者，并在证明"单射即双射"时给出长度守恒。这也说明 Krull–Schmidt 并非无条件成立——反例通常出现在既非 Artin 又非 Noether 的模上。

第二，局部自同态环是关键。两个分解的比较需要判断"从 $M_1$ 出发经投影与包含复合而成的自同态是否可逆"。局部环保证：$\sum_j \psi_j\varphi_j=\mathrm{id}$ 为单位，则某个 $\psi_j\varphi_j$ 必为单位，从而可逆。这一步把"存在同构"从模糊比较变成一次可逆性判定。

第三，得到同构后为什么可以"消去"？因为若 $M_1\cong N_j$ 且两侧都是同一 $M$ 的直和加项，取商 $M/M_1$ 便同时得到 $\bigoplus_{i\ge2}M_i$ 与 $\bigoplus_{k\ne j}N_k$，于是两者同构，归纳即可。这一步用的是直和加项的良定义与商模的交换图。

## 证明过程

**步骤 1：Fitting 分解。** 设 $M$ 有限长度，$f\in\operatorname{End}_R(M)$。因 $M$ 是 Noether 模，$\ker f\subseteq\ker f^2\subseteq\cdots$ 稳定，取 $n$ 使 $\ker f^n=\ker f^{2n}$；又因 $M$ 是 Artin 模，$\mathrm{im}\,f\supseteq\mathrm{im}\,f^2\supseteq\cdots$ 稳定，可把 $n$ 取得更大使 $\mathrm{im}\,f^n=\mathrm{im}\,f^{2n}$。此时对任意 $x\in M$，有 $f^n(x)\in\mathrm{im}\,f^n=\mathrm{im}\,f^{2n}$，故存在 $y$ 使 $f^n(x)=f^{2n}(y)$，于是 $x=(x-f^n(y))+f^n(y)$，而 $f^n(x-f^n(y))=f^n(x)-f^{2n}(y)=0$，故 $x\in\ker f^n+\mathrm{im}\,f^n$。又若 $z\in\ker f^n\cap\mathrm{im}\,f^n$，写 $z=f^n(w)$ 且 $f^n(z)=0$，则 $f^{2n}(w)=0$，即 $w\in\ker f^{2n}=\ker f^n$，从而 $z=f^n(w)=0$。故
$$
M=\ker f^n\oplus\mathrm{im}\,f^n .
$$

**步骤 2：不可分解模的自同态环是局部环。** 设 $M\ne0$ 不可分解且有限长度，$f\in\operatorname{End}_R(M)$。由步骤 1，$M=\ker f^n\oplus\mathrm{im}\,f^n$；由不可分解性，$\ker f^n=0$ 或 $\mathrm{im}\,f^n=0$。若 $\ker f^n=0$，则 $f^n$ 单射；对有限长度模，单射自同态保长度，故 $f^n$ 双射，从而 $f$ 可逆。若 $\mathrm{im}\,f^n=0$，则 $f$ 幂零，几何级数 $\mathrm{id}+f+\cdots+f^{n-1}$ 给出 $(\mathrm{id}-f)^{-1}$，即 $\mathrm{id}-f$ 可逆。因此 $\operatorname{End}_R(M)$ 中每个元素或本身可逆、或使 $\mathrm{id}-f$ 可逆，即非可逆元构成理想，$\operatorname{End}_R(M)$ 是局部环；特别地，若 $\sum_j u_j$ 可逆，则至少一个 $u_j$ 可逆。

**步骤 3：把第一个因子送到第二分解的某个因子。** 记 $\pi_i:M\to M_i$、$\iota_i:M_i\to M$ 为标准投影与包含，$\pi'_j,\iota'_j$ 类似。由 $\sum_i\iota_i\pi_i=\mathrm{id}_M$，得
$$
\sum_{j=1}^{s}\big(\pi_{1}\iota'_{j}\big)\big(\pi'_{j}\iota_{1}\big)=\pi_1\Big(\sum_j\iota'_j\pi'_j\Big)\iota_1=\pi_1\iota_1=\mathrm{id}_{M_1}.
$$
由环同态基本定理，这些复合是 $M_1$ 的自同态；再由步骤 2 的局部性，存在 $j$ 使 $u:=\psi_j\varphi_j$ 可逆，其中 $\varphi_j=\pi'_j\iota_1:M_1\to N_j$，$\psi_j=\pi_1\iota'_j:N_j\to M_1$。于是 $\varphi_j$ 单射（若 $\varphi_j(x)=0$ 则 $u(x)=0$），$\psi_j$ 满射。考虑 $N_j$ 的分解
$$
N_j=\varphi_j(M_1)\oplus\ker\psi_j .
$$
右边求和直接：任意 $y=\varphi_j\psi_j(y)+(y-\varphi_j\psi_j(y))$，而 $\psi_j\big(y-\varphi_j\psi_j(y)\big)=\psi_j(y)-\psi_j\varphi_j\psi_j(y)=0$；交为零：若 $y=\varphi_j(x)$ 且 $\psi_j(y)=0$，则 $u(x)=\psi_j\varphi_j(x)=0$，由 $u$ 可逆得 $x=0$，故 $y=0$。由 $N_j$ 不可分解且 $\varphi_j$ 单射使 $\varphi_j(M_1)\ne0$，必有 $\ker\psi_j=0$，从而 $\psi_j$ 单射、$\varphi_j$ 满射，即 $\varphi_j:M_1\to N_j$ 是同构。

**步骤 4：消去并归纳。** 由步骤 3，$M_1\cong N_j$。取商模
$$
M/M_1\cong M_2\oplus\cdots\oplus M_r,\qquad M/N_j\cong\bigoplus_{k\ne j}N_k .
$$
同构 $\varphi_j$ 把 $M_1$ 送到 $N_j$，在商上诱导 $M/M_1\cong M/N_j$，故
$$
M_2\oplus\cdots\oplus M_r\cong\bigoplus_{k\ne j}N_k .
$$
对因子个数 $r$ 作归纳（$r=1$ 时 $M$ 不可分解，故 $s=1$），即得 $r-1=s-1$ 与因子的一一同构对应。补上 $M_1\cong N_j$ 即得 $r=s$ 与所求置换 $\sigma$。证毕。

## 相关条目

- [主理想整环上有限生成模结构定理](./主理想整环上有限生成模结构定理.md)：把有限生成模分解为循环模，其分解唯一性与 Krull–Schmidt 相互印证。
- [有限生成Abel群基本定理](./有限生成Abel群基本定理.md)：$\mathbb Z$-模情形最经典的分解定理，唯一性论证可用本定理统一处理。
- [环同态基本定理](./环同态基本定理.md)：步骤 3 中判定复合映射的像与核时所用的基本工具。
- [PID是UFD](./PID是UFD.md)：整环层次的"唯一分解"对照，与本定理的模分解唯一性互为类比。
