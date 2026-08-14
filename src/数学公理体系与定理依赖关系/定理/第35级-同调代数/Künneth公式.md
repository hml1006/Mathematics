# Künneth公式

## 介绍

Künneth公式（Künneth Formula）是同调代数中计算张量积复形的同调的基本公式。它给出了两个链复形的张量积的同调与各复形同调的张量积和 $\operatorname{Tor}$ 修正项之间的关系。在代数拓扑中，Künneth公式用于计算两个拓扑空间的乘积空间的同调群，是代数拓扑中最基本的计算工具之一。

## 分析

**前置依赖**：链复形、张量积、同调群、$\operatorname{Tor}$ 函子、谱序列。

**数学内涵**：

**定理内容**：设 $R$ 是主理想整环（PID），$C_\bullet$ 和 $D_\bullet$ 是 $R$ 上的链复形，则存在短正合列：
$$
0 \to \bigoplus_{p+q=n} H_p(C) \otimes_R H_q(D) \to H_n(C \otimes_R D) \to \bigoplus_{p+q=n-1} \operatorname{Tor}^R_1(H_p(C), H_q(D)) \to 0
$$

该正合列**分裂**但不自然分裂。

**特殊情形**：若 $R$ 是域（或更一般地，若 $H_p(C)$ 或 $H_q(D)$ 是平坦 $R$-模），则 $\operatorname{Tor}$ 项消失，得到同构：
$$
H_n(C \otimes_R D) \cong \bigoplus_{p+q=n} H_p(C) \otimes_R H_q(D)
$$

**数学内涵**：Künneth公式揭示了"复形的同调"与"同调的张量积"之间的差异恰好由 $\operatorname{Tor}$ 函子衡量。

**证明策略**：利用谱序列或代数Künneth定理，通过链复形的截断和正合列推导。

## 思考过程

Künneth公式的直观理解：两个链复形的张量积的同调，大致上等于它们同调的张量积，但需要加上一个 $\operatorname{Tor}$ 修正项。这个修正项来源于同调群中的挠（torsion）信息。

例如，在拓扑中计算 $S^1 \times S^1$（环面）的同调群时，Künneth公式给出：
- $H_0(S^1 \times S^1) \cong \mathbb{Z}$
- $H_1(S^1 \times S^1) \cong \mathbb{Z} \oplus \mathbb{Z}$
- $H_2(S^1 \times S^1) \cong \mathbb{Z}$

这与直接计算的结果一致。

当系数环是 PID 时，Künneth公式有简洁的形式；对更一般的系数环，需要更复杂的谱序列工具。

## 证明过程

### 代数Künneth定理

**定理**（代数Künneth公式）：设 $R$ 是主理想整环，$C_\bullet$ 和 $D_\bullet$ 是 $R$ 上的链复形。则对每个 $n$，存在分裂的短正合列：
$$
0 \to \bigoplus_{p+q=n} H_p(C) \otimes_R H_q(D) \to H_n(C \otimes_R D) \to \bigoplus_{p+q=n-1} \operatorname{Tor}^R_1(H_p(C), H_q(D)) \to 0
$$

**证明**：

**步骤 1**：化为标准形。由于 $R$ 是 PID，每个 $R$-模的子模是自由的当且仅当它是无挠的。考虑链复形 $C_\bullet$ 的截断。

设 $Z_p(C) = \ker(d_p: C_p \to C_{p-1})$ 是 $p$-轮缘，$B_p(C) = \operatorname{Im}(d_{p+1}: C_{p+1} \to C_p)$ 是 $p$-边界。则 $H_p(C) = Z_p(C)/B_p(C)$。

**步骤 2**：构造短正合列。对每个 $p$，有短正合列：
$$
0 \to Z_p(C) \to C_p \xrightarrow{d_p} B_{p-1}(C) \to 0
$$
由于 $B_{p-1}(C)$ 是 $R$-子模，且 $R$ 是 PID，$B_{p-1}(C)$ 是自由模，故该正合列分裂：
$$
C_p \cong Z_p(C) \oplus B_{p-1}(C)
$$

**步骤 3**：张量积分解。考虑 $C_\bullet \otimes_R D_\bullet$ 的 $n$ 次链群：
$$
(C \otimes_R D)_n = \bigoplus_{p+q=n} C_p \otimes_R D_q
$$

利用 $C_p \cong Z_p(C) \oplus B_{p-1}(C)$，可以分解 $(C \otimes_R D)_n$ 为若干部分的和。

**步骤 4**：计算同调。通过直接计算 $H_n(C \otimes_R D)$，得到：
- 轮缘部分对应于 $\bigoplus_{p+q=n} Z_p(C) \otimes_R Z_q(D)$
- 边界部分对应于 $\bigoplus_{p+q=n} (B_{p-1}(C) \otimes_R Z_q(D) + Z_p(C) \otimes_R B_{q-1}(D))$

经商后得到 $H_n(C \otimes_R D)$ 与 $\bigoplus_{p+q=n} H_p(C) \otimes_R H_q(D)$ 的关系，以及 $\operatorname{Tor}$ 修正项。

**步骤 5**：正合性与分裂性。通过构造链映射证明正合列是分裂的（但分裂不是自然的）。

$\square$

### 拓扑Künneth公式

**定理**（拓扑Künneth公式）：设 $X$ 和 $Y$ 是拓扑空间，$R$ 是主理想整环。则存在分裂的短正合列：
$$
0 \to \bigoplus_{p+q=n} H_p(X; R) \otimes_R H_q(Y; R) \to H_n(X \times Y; R) \to \bigoplus_{p+q=n-1} \operatorname{Tor}^R_1(H_p(X; R), H_q(Y; R)) \to 0
$$

**证明**：取 $X$ 和 $Y$ 的奇异链复形 $C_\bullet(X; R)$ 和 $C_\bullet(Y; R)$，由 Eilenberg-Zilber 定理，存在链等价：
$$
C_\bullet(X; R) \otimes_R C_\bullet(Y; R) \simeq C_\bullet(X \times Y; R)
$$
然后应用代数Künneth公式。$\square$

### 推论

**推论 1**（域系数）：若 $R = k$ 是域，则：
$$
H_n(X \times Y; k) \cong \bigoplus_{p+q=n} H_p(X; k) \otimes_k H_q(Y; k)
$$

**推论 2**（整数系数）：若 $H_p(X; \mathbb{Z})$ 或 $H_q(Y; \mathbb{Z})$ 是无挠的，则：
$$
H_n(X \times Y; \mathbb{Z}) \cong \bigoplus_{p+q=n} H_p(X; \mathbb{Z}) \otimes_{\mathbb{Z}} H_q(Y; \mathbb{Z})
$$

**例**：计算 $S^2 \times S^1$ 的同调群：
- $H_0 \cong \mathbb{Z}$
- $H_1 \cong \mathbb{Z}$
- $H_2 \cong \mathbb{Z}$
- $H_3 \cong \mathbb{Z}$
- 其他为零

**应用**：Künneth公式是代数拓扑中计算乘积空间同调群的标准方法，也是代数几何中Künneth公式的起源。$\square$