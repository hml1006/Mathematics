# Kronecker-Weber定理

## 介绍

Kronecker-Weber定理是代数数论中的一个经典结果，它完整刻画了有理数域 $\mathbb{Q}$ 的阿贝尔扩张。该定理由利奥波德·克罗内克于 1853 年提出猜想，由海因里希·韦伯于 1886 年首次证明。定理断言：$\mathbb{Q}$ 的每个有限阿贝尔扩张都包含在某个分圆域 $\mathbb{Q}(\zeta_n)$ 中。换言之，$\mathbb{Q}$ 的最大阿贝尔扩张 $\mathbb{Q}^{\text{ab}}$ 是所有分圆域的并集。这一定理是类域论中一般性结果的先驱，也是代数数论中最优美的定理之一。

## 分析

**前置依赖**：伽罗瓦理论、分圆域理论、阿贝尔扩张、域扩张。

**数学内涵**：

**定理内容**：设 $L/\mathbb{Q}$ 是有限阿贝尔伽罗瓦扩张（即 $\operatorname{Gal}(L/\mathbb{Q})$ 是交换群）。则存在正整数 $n$ 使得 $L \subseteq \mathbb{Q}(\zeta_n)$，其中 $\zeta_n$ 是 $n$ 次本原单位根。

**等价表述**：$\mathbb{Q}$ 的最大阿贝尔扩张 $\mathbb{Q}^{\text{ab}} = \bigcup_{n \ge 1} \mathbb{Q}(\zeta_n)$。

**数学内涵**：Kronecker-Weber定理表明，有理数域的所有阿贝尔扩张都可以通过添加单位根得到。这是分圆域理论发展的顶峰，也是类域论中一般性结果（任意数域的阿贝尔扩张由射线类域刻画）的特殊情形。

**证明策略**：经典证明通过局部化方法（在 $p$-adic 域中分析）或利用类域论。现代证明常用局部域上的 Kronecker-Weber 定理。

## 思考过程

Kronecker-Weber 定理的直观含义是：$\mathbb{Q}$ 的每个阿贝尔扩张都可以通过单位根生成。例如：
- 二次扩张 $\mathbb{Q}(\sqrt{2})$ 包含在 $\mathbb{Q}(\zeta_8)$ 中，因为 $\sqrt{2} = \zeta_8 + \zeta_8^{-1}$。
- 二次扩张 $\mathbb{Q}(\sqrt{-1})$ 就是 $\mathbb{Q}(\zeta_4)$。
- $\mathbb{Q}(\sqrt{p^*})$ 包含在 $\mathbb{Q}(\zeta_p)$ 中（高斯和的经典结果）。

证明思路大致如下：
1. 首先证明对素数幂 $p^n$，$\mathbb{Q}(\zeta_{p^n})$ 的子域覆盖了所有 $p$-分圆扩张。
2. 利用局部域上的 Kronecker-Weber 定理（$\mathbb{Q}_p$ 的每个阿贝尔扩张包含在某个 $\mathbb{Q}_p(\zeta_n)$ 中）。
3. 通过全局-局部原则（Chebotarev 密度定理或 Minkowski 定理）将局部结论提升到全局。

## 证明过程

### 预备知识

**引理 1**（判别式判别法）：设 $L/\mathbb{Q}$ 是有限扩张，$\Delta_L$ 是 $L$ 的判别式。若 $p$ 在 $L$ 中分歧，则 $p \mid \Delta_L$。

**引理 2**（分圆域的子域）：$\mathbb{Q}(\zeta_n)$ 的子域都是 $\mathbb{Q}$ 的阿贝尔扩张。反之，$\mathbb{Q}$ 的每个阿贝尔扩张都是某个 $\mathbb{Q}(\zeta_n)$ 的子域（Kronecker-Weber 定理的结论）。

### 全局域的 Kronecker-Weber 定理

**定理**（Kronecker-Weber）：$\mathbb{Q}$ 的每个有限阿贝尔扩张 $L$ 包含在某个分圆域 $\mathbb{Q}(\zeta_n)$ 中。

**证明**（经典证明思路）：

**步骤 1**：分解为素数幂情形。

由于 $\mathbb{Q}(\zeta_{mn}) = \mathbb{Q}(\zeta_m)\mathbb{Q}(\zeta_n)$ 且 $\gcd(m,n)=1$ 时 $\mathbb{Q}(\zeta_{mn})$ 是 $\mathbb{Q}(\zeta_m)$ 和 $\mathbb{Q}(\zeta_n)$ 的复合，只需证明对每个素数 $p$，$L$ 的 $p$ 部分（即 $p$ 次幂扩张的部分）包含在某个 $\mathbb{Q}(\zeta_{p^k})$ 中。

**步骤 2**：局部化。

设 $L/\mathbb{Q}$ 是阿贝尔扩张，$p$ 是素数。考虑 $p$ 在 $L$ 中的素理想分解，以及完备化 $L_{\mathfrak{p}}/\mathbb{Q}_p$。$L_{\mathfrak{p}}/\mathbb{Q}_p$ 也是阿贝尔扩张。

**局部 Kronecker-Weber 定理**：$\mathbb{Q}_p$ 的每个有限阿贝尔扩张包含在某个 $\mathbb{Q}_p(\zeta_n)$ 中。

*证明概要*：$\mathbb{Q}_p$ 的绝对伽罗瓦群的结构已知，其阿贝尔商同构于 $\hat{\mathbb{Z}}^\times$，而 $\mathbb{Q}_p(\zeta_n)$ 的伽罗瓦群是 $(\mathbb{Z}/n\mathbb{Z})^\times$ 的子群，覆盖了所有有限阿贝尔商。$\square$

**步骤 3**：全局化。

由局部 Kronecker-Weber 定理，对每个素数 $p$，存在 $n_p$ 使得 $L_{\mathfrak{p}} \subseteq \mathbb{Q}_p(\zeta_{n_p})$。通过选择适当的 $n$（如所有 $n_p$ 的最小公倍数），可以证明 $L \subseteq \mathbb{Q}(\zeta_n)$。

具体地，考虑 $L' = L\mathbb{Q}(\zeta_n)$，则 $L'/\mathbb{Q}$ 是阿贝尔扩张，且在 $p$ 处的完备化与 $\mathbb{Q}(\zeta_n)$ 相同。由 Minkowski 定理或判别式判别法，$L' = \mathbb{Q}(\zeta_n)$，故 $L \subseteq \mathbb{Q}(\zeta_n)$。$\square$

### 二次域嵌入分圆域

**推论 1**：每个二次域 $\mathbb{Q}(\sqrt{d})$（$d$ 是无平方因子整数）包含在某个分圆域中。

**证明**：设 $d$ 无平方因子。由二次互反律，存在 $n$ 使得 $\mathbb{Q}(\sqrt{d}) \subseteq \mathbb{Q}(\zeta_n)$。具体地：

- 若 $d$ 是奇数，则 $\sqrt{d^*} \in \mathbb{Q}(\zeta_d)$，其中 $d^* = (-1)^{(d-1)/2}d$。
- 若 $d > 0$，$\sqrt{d} \in \mathbb{Q}(\zeta_{4d})$。
- 若 $d < 0$，$\sqrt{d} \in \mathbb{Q}(\zeta_{4|d|})$。

$\square$

**推论 2**：$\mathbb{Q}^{\text{ab}} = \bigcup_{n \ge 1} \mathbb{Q}(\zeta_n)$，且 $\operatorname{Gal}(\mathbb{Q}^{\text{ab}}/\mathbb{Q}) \cong \hat{\mathbb{Z}}^\times = \prod_p \mathbb{Z}_p^\times$。

**证明**：$\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times$，取逆向极限即得 $\operatorname{Gal}(\mathbb{Q}^{\text{ab}}/\mathbb{Q}) \cong \varprojlim (\mathbb{Z}/n\mathbb{Z})^\times \cong \hat{\mathbb{Z}}^\times$。$\square$

### 意义与推广

**意义**：
- Kronecker-Weber 定理是类域论中"阿贝尔扩张由射线类域刻画"这一一般性结果在 $\mathbb{Q}$ 上的特例。
- 它揭示了分圆域在代数数论中的核心地位。
- 定理的名称"Kronecker-Weber"纪念了克罗内克（提出猜想）和韦伯（首次证明）的贡献。

**推广**（Kronecker 青春之梦）：对于虚二次域 $K$，克罗内克猜想 $K$ 的最大阿贝尔扩张可以通过添加 $j$-函数值和椭圆曲线的挠点得到。这是希尔伯特第 12 问题的一部分，至今尚未完全解决。

**应用**：Kronecker-Weber 定理在代数数论、类域论和模形式理论中具有广泛的应用，是理解 $\mathbb{Q}$ 的阿贝尔扩张的完整分类的基础。$\square$