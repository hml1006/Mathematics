# 欧几里得整环是 PID

## 介绍

欧几里得整环（Euclidean Domain）是一类具有"带余除法"的整环，而主理想整环（Principal Ideal Domain，PID）是指每个理想都是主理想的整环。本定理断言：每个欧几里得整环都是主理想整环。这个结论建立了欧几里得算法与理想结构之间的联系，使我们可以利用带余除法来研究理想的性质。$\mathbb{Z}$ 和域上的多项式环 $F[x]$ 都是欧几里得整环，因此也是 PID。

## 分析

**定义**：整环 $R$ 称为欧几里得整环，如果存在函数 $\varphi: R \setminus \{0\} \to \mathbb{N}$（称为欧几里得函数），满足：
1. 对任意 $a, b \in R$，$b \neq 0$，存在 $q, r \in R$ 使得 $a = bq + r$，且 $r = 0$ 或 $\varphi(r) < \varphi(b)$；
2. 对任意非零 $a, b \in R$，$\varphi(a) \le \varphi(ab)$。

**主理想整环**：整环 $R$ 称为主理想整环，如果 $R$ 的每个理想都是主理想，即对任意理想 $I \trianglelefteq R$，存在 $a \in R$ 使得 $I = (a) = Ra$。

**定理的精确表述**：若 $R$ 是欧几里得整环，则 $R$ 是主理想整环。

## 思考过程

欧几里得整环是 PID 的证明思路非常直接：设 $I$ 是 $R$ 的非零理想，取 $I$ 中欧几里得函数值最小的非零元 $a$，则 $I = (a)$。这是因为对任意 $b \in I$，由带余除法，$b = aq + r$，其中 $r = 0$ 或 $\varphi(r) < \varphi(a)$。由 $r = b - aq \in I$ 及 $\varphi(a)$ 的最小性，必有 $r = 0$，故 $b = aq$，即 $b \in (a)$。

这个证明体现了欧几里得算法的核心思想：通过带余除法，最小的非零元生成整个理想。

## 证明过程

**证明**：设 $R$ 是欧几里得整环，$\varphi$ 是欧几里得函数。设 $I \trianglelefteq R$ 是 $R$ 的理想。

若 $I = \{0\}$，则 $I = (0)$ 是主理想。

若 $I \neq \{0\}$，考虑集合 $\{\varphi(a): a \in I \setminus \{0\}\}$。由自然数的良序性，存在 $a \in I \setminus \{0\}$ 使得 $\varphi(a)$ 取最小值。

下证 $I = (a)$。显然 $(a) \subseteq I$。对任意 $b \in I$，由欧几里得整环的定义，存在 $q, r \in R$ 使得

$$
b = aq + r,
$$

其中 $r = 0$ 或 $\varphi(r) < \varphi(a)$。

由于 $r = b - aq \in I$（因为 $b, a \in I$），且 $\varphi(a)$ 是 $I$ 中非零元的最小值，故不可能有 $\varphi(r) < \varphi(a)$ 且 $r \neq 0$。因此 $r = 0$，从而 $b = aq \in (a)$。

因此 $I \subseteq (a)$，结合 $(a) \subseteq I$ 得 $I = (a)$。$\square$

**例 1**：$\mathbb{Z}$ 是欧几里得整环（$\varphi(n) = |n|$），故 $\mathbb{Z}$ 是 PID。$\mathbb{Z}$ 的理想都是形如 $n\mathbb{Z}$ 的主理想。

**例 2**：域 $F$ 上的多项式环 $F[x]$ 是欧几里得整环（$\varphi(f) = \deg f$），故 $F[x]$ 是 PID。$F[x]$ 的理想都由某个多项式生成。

**推论**：欧几里得整环是 UFD。

**证明**：PID 是 UFD，因此欧几里得整环作为 PID 的子类，也是 UFD。$\square$