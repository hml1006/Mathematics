# 整扩张与Going-up定理

## 介绍

整扩张（Integral Extension）是交换代数中研究环扩张的基本概念，它推广了域论中的代数扩张。环 $B$ 称为环 $A$ 的整扩张，如果 $B$ 中的每个元素都是某个首一多项式 $f(x) \in A[x]$ 的根。Going-up 定理（以及 Going-down 定理）是整扩张理论中关于素理想提升的核心结果，它描述了整扩张中素理想之间的对应关系，在代数数论和代数几何中具有重要应用。

## 分析

**前置依赖**：交换代数、环扩张、素理想、局部化、整性。

**数学内涵**：

**定义**：
- $b \in B$ 在 $A$ 上**整**，如果存在首一多项式 $f(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0 \in A[x]$ 使得 $f(b) = 0$。
- $B$ 是 $A$ 的**整扩张**，如果 $B$ 中每个元素都在 $A$ 上整。
- $A$ 在 $B$ 中的**整闭包**是 $B$ 中所有在 $A$ 上整的元素构成的集合。

**Going-up 定理**：设 $A \subseteq B$ 是整扩张，$\mathfrak{p}_1 \subseteq \mathfrak{p}_2 \subseteq \cdots \subseteq \mathfrak{p}_n$ 是 $A$ 的素理想升链，$\mathfrak{q}_1 \subseteq \mathfrak{q}_2 \subseteq \cdots \subseteq \mathfrak{q}_m$（$m < n$）是 $B$ 的素理想升链，且 $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ 对 $i \le m$。则存在 $B$ 的素理想 $\mathfrak{q}_{m+1}, \ldots, \mathfrak{q}_n$ 使得 $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ 且 $\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1}$。

**推论**：若 $A \subseteq B$ 是整扩张，$\mathfrak{p} \subseteq A$ 是素理想，则存在 $B$ 的素理想 $\mathfrak{q}$ 使得 $\mathfrak{q} \cap A = \mathfrak{p}$。

**数学内涵**：Going-up 定理断言，$A$ 中的素理想可以"提升"到 $B$ 中，且保持包含关系。这是整扩张最重要的性质之一。

**证明策略**：利用局部化将问题化为局部环的情形，通过 Nakayama 引理等工具证明。

## 思考过程

整扩张中的"Going-up"性质可以通过以下直观理解：$A \subseteq B$ 是整扩张时，$B$ 可以看作 $A$ 上的一个"有限"扩张（虽然不是有限生成模，但每个元素满足首一多项式）。素理想 $\mathfrak{p} \subseteq A$ 对应着 $B$ 中"覆盖"它的素理想 $\mathfrak{q}$（即 $\mathfrak{q} \cap A = \mathfrak{p}$），且这种覆盖关系保持包含顺序。

在代数几何中，这对应着有限态射 $\operatorname{Spec} B \to \operatorname{Spec} A$ 的满射性。在代数数论中，整扩张 $A \subseteq B$ 对应着数域的扩张，Going-up 定理描述了素理想在扩张中的分解行为。

## 证明过程

### 整性的基本性质

**引理 1**：$b \in B$ 在 $A$ 上整当且仅当 $A[b]$ 是有限生成 $A$-模。

**证明**：若 $b^n + a_{n-1}b^{n-1} + \cdots + a_0 = 0$，则 $A[b]$ 由 $1, b, \ldots, b^{n-1}$ 生成。反之，若 $A[b]$ 是有限生成 $A$-模，由 Cayley-Hamilton 定理可得整性方程。$\square$

**引理 2**：若 $B$ 是 $A$ 上的有限生成模，则 $B$ 在 $A$ 上整。

**证明**：对任意 $b \in B$，$A[b] \subseteq B$ 是 $A$-子模，故有限生成，由引理 1，$b$ 在 $A$ 上整。$\square$

### Going-up 定理

**定理 1**（Going-up 定理）：设 $A \subseteq B$ 是整扩张，$\mathfrak{p} \subseteq A$ 是素理想。则存在 $B$ 的素理想 $\mathfrak{q}$ 使得 $\mathfrak{q} \cap A = \mathfrak{p}$。

**证明**：

**步骤 1**：考虑局部化 $A_{\mathfrak{p}}$，令 $S = A \setminus \mathfrak{p}$。$S^{-1}B = B_{\mathfrak{p}}$ 是 $A_{\mathfrak{p}}$ 的整扩张（因为整性在局部化下保持）。

**步骤 2**：设 $\mathfrak{m} = \mathfrak{p} A_{\mathfrak{p}}$ 是 $A_{\mathfrak{p}}$ 的极大理想。需要证明 $\mathfrak{m} B_{\mathfrak{p}} \ne B_{\mathfrak{p}}$。若 $\mathfrak{m} B_{\mathfrak{p}} = B_{\mathfrak{p}}$，则 $1 = \sum a_i b_i$，其中 $a_i \in \mathfrak{m}$，$b_i \in B_{\mathfrak{p}}$。由于 $B_{\mathfrak{p}}$ 是 $A_{\mathfrak{p}}$ 的整扩张，$B_{\mathfrak{p}}$ 是 $A_{\mathfrak{p}}$ 上的有限生成模（可由整性方程导出），由 Nakayama 引理，$B_{\mathfrak{p}} = 0$，矛盾。

**步骤 3**：$\mathfrak{m} B_{\mathfrak{p}}$ 是 $B_{\mathfrak{p}}$ 的真理想，包含在某个极大理想 $\mathfrak{q}' \subseteq B_{\mathfrak{p}}$ 中。令 $\mathfrak{q} = \mathfrak{q}' \cap B$，则 $\mathfrak{q} \cap A = \mathfrak{p}$。$\square$

**定理 2**（Going-up 定理 - 链的提升）：设 $A \subseteq B$ 是整扩张，$\mathfrak{p}_1 \subseteq \mathfrak{p}_2 \subseteq \cdots \subseteq \mathfrak{p}_n$ 是 $A$ 的素理想升链，$\mathfrak{q}_1 \subseteq \mathfrak{q}_2 \subseteq \cdots \subseteq \mathfrak{q}_m$（$m < n$）是 $B$ 的素理想升链，且 $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ 对 $i \le m$。则存在 $B$ 的素理想 $\mathfrak{q}_{m+1}, \ldots, \mathfrak{q}_n$ 使得 $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ 且 $\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1}$。

**证明**：对 $m+1$ 归纳。考虑 $A/\mathfrak{p}_m \subseteq B/\mathfrak{q}_m$，这是整扩张。由定理 1，存在 $\mathfrak{p}_{m+1}/\mathfrak{p}_m$ 在 $B/\mathfrak{q}_m$ 中的提升，对应 $B$ 中的素理想 $\mathfrak{q}_{m+1}$ 满足 $\mathfrak{q}_{m+1} \supseteq \mathfrak{q}_m$ 且 $\mathfrak{q}_{m+1} \cap A = \mathfrak{p}_{m+1}$。$\square$

### Going-down 定理

**定理 3**（Going-down 定理）：设 $A \subseteq B$ 是整扩张，$A$ 是整闭整环（即 $A$ 在其分式域中整闭），$B$ 是整环。设 $\mathfrak{p}_1 \supseteq \mathfrak{p}_2 \supseteq \cdots \supseteq \mathfrak{p}_n$ 是 $A$ 的素理想降链，$\mathfrak{q}_1 \supseteq \mathfrak{q}_2 \supseteq \cdots \supseteq \mathfrak{q}_m$（$m < n$）是 $B$ 的素理想降链，且 $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ 对 $i \le m$。则存在 $B$ 的素理想 $\mathfrak{q}_{m+1}, \ldots, \mathfrak{q}_n$ 使得 $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ 且 $\mathfrak{q}_i \supseteq \mathfrak{q}_{i+1}$。

**证明**：利用局部化和整闭包的性质，通过类似 Going-up 的论证（但方向相反）。$\square$

### 推论

**推论 1**（比较定理）：设 $A \subseteq B$ 是整扩张，则 $\dim A = \dim B$，其中 $\dim$ 表示 Krull 维数。

**证明**：Going-up 定理保证 $A$ 中的素理想链可提升为 $B$ 中的素理想链，且不同素理想提升后不同（因为 $\mathfrak{q} \cap A = \mathfrak{p}$ 是满射），故 $\dim A \le \dim B$。Going-down 定理保证 $\dim B \le \dim A$。因此相等。$\square$

**推论 2**（极大理想对应）：若 $A \subseteq B$ 是整扩张，则 $\mathfrak{m} \subseteq A$ 是极大理想当且仅当存在 $B$ 的极大理想 $\mathfrak{n}$ 使得 $\mathfrak{n} \cap A = \mathfrak{m}$。

**应用**：整扩张和 Going-up 定理是代数数论（研究数域的整数环）、代数几何（研究有限态射）和交换代数中维数理论的基本工具。$\square$