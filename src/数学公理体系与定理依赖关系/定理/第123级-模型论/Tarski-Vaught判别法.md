# Tarski-Vaught 判别法

> **一句话大白话**：要判断一个小结构是不是大结构的“初等部分”（对每条带参数的语句看法完全一致），只需检查一件事——大结构说“存在某个元素满足 $\varphi$”时，小结构里必须已经有一个这样的元素当见证。
>
> **小例子**：有理数集 $\mathbb Q$ 是实数集 $\mathbb R$（视为稠密线性序结构）的初等子结构：若 $\mathbb R$ 中有 $x$ 满足某个含参数（参数在 $\mathbb Q$ 中）的公式，由量词消去它归结为一组有理端点开区间约束，而 $\mathbb Q$ 稠密且无端点，故必有一个有理数也在该区间内。

## 一、定理介绍

> **前置依赖**：一阶语言与 $\mathcal L$-结构、一阶逻辑的语法与语义、子结构与嵌入、一阶逻辑的语法与语义、量词消去（用于例子）、初等链引理与 Löwenheim–Skolem 定理

模型论中最重要的关系之一是**初等子结构**：$\mathcal N\preceq\mathcal M$ 表示 $\mathcal N$ 是 $\mathcal M$ 的子结构，并且对每一条参数取自 $\mathcal N$ 的公式，两个结构的真值完全一致。这个定义是对无穷多条公式提出的要求，直接验证通常不可能。Tarski 与 Vaught 在 1957 年的论文《Arithmetical extensions of relational systems》中给出了一个只需检查“存在量词型的见证”的判别准则，把无穷多条要求压缩为一条可操作的检验条件。

判别法的形式极其简洁：只要 $\mathcal M$ 中任何以 $\mathcal N$ 的元素为参数的公式 $\exists v\,\varphi(v,\bar a)$ 为真时，都能在 $\mathcal N$ 内找到见证 $b$，就自动保证了全部公式的真值一致性。也就是说，唯一可能出错的地方是“存在性”，而全称量词的错误恰好由前者的失败暴露出来。

该判别法是模型论中使用频率最高的技术工具之一：Löwenheim–Skolem 下降定理、初等链定理、省略类型定理、饱和模型的构造、Morley 范畴性定理以及代数闭域、实闭域、稠密线性序等理论的模型分析，都以它为核心推理步骤。在代数中它给出“代数闭子域是初等子结构”“实闭子域是初等子结构”等深刻结论。

## 几何直观

![大圆 A 内含绿色虚线圈 B，橙色解集与 B 相交，交点是红色见证点](images/th-123-03-tarski-vaught.svg)

图意在说明：只要每个存在公式的见证元都能在 B 内找到，B 就与 A 初等等价，无需逐条公式核对。

## 二、原理思路

证明是一个“反向归纳”：

1. **必要性（$\Rightarrow$）几乎显然**：若 $\mathcal N\preceq\mathcal M$ 且 $\mathcal M\models\exists v\,\varphi(v,\bar a)$，由初等性 $\mathcal N\models\exists v\,\varphi(v,\bar a)$，取出 $\mathcal N$ 中的见证 $b$，再由初等性回到 $\mathcal M$。
2. **充分性（$\Leftarrow$）对公式复杂度归纳**：要证对一切 $\bar a\in N^n$ 有 $\mathcal N\models\varphi(\bar a)\iff\mathcal M\models\varphi(\bar a)$。
3. **原子公式靠“项的值一致”**：子结构对函数符号封闭，故同一个项在 $\mathcal N$ 与 $\mathcal M$ 中的解释相同，这是整个归纳的基座。
4. **布尔组合靠归纳假设**：$\neg,\wedge,\vee$ 可直接处理。
5. **量词情形靠判别条件与归纳假设“双向对接”**：$\exists$ 的两个方向分别由“见证在内”和“真值一致”完成；$\forall$ 化为 $\neg\exists\neg$。

## 三、定理的严格表述

**（Tarski–Vaught 判别法）** 设 $\mathcal L$ 为一阶语言（可含函数符号与常数符号），$\mathcal M$ 为 $\mathcal L$-结构，$\mathcal N\subseteq\mathcal M$ 为 $\mathcal M$ 的**子结构**（即 $N\subseteq M$ 非空，且 $\mathcal N$ 在 $\mathcal M$ 的函数符号与常数符号下封闭，$\mathcal N$ 中的谓词与函数取 $\mathcal M$ 中的相应限制）。则

$$
\mathcal N\preceq\mathcal M
\qquad\Longleftrightarrow\qquad
\begin{array}{l}
\text{对每个 }\mathcal L\text{-公式 }\varphi=\varphi(v,w_1,\dots,w_n)\text{ 与每个 }\bar a=(a_1,\dots,a_n)\in N^n:\\
\mathcal M\models\exists v\,\varphi(v,\bar a)\ \Longrightarrow\ \exists b\in N\text{ 使 }\mathcal M\models\varphi(b,\bar a).
\end{array}
$$

其中 $\mathcal N\preceq\mathcal M$ 意为：$\mathcal N$ 是 $\mathcal M$ 的**初等子结构**，即对每个公式 $\varphi(w_1,\dots,w_n)$ 与每个 $\bar a\in N^n$，
$$
\mathcal N\models\varphi(\bar a)\quad\Longleftrightarrow\quad\mathcal M\models\varphi(\bar a).
$$

**等价表述**：

- （带参数的初等等价）$\mathcal N\preceq\mathcal M$ 当且仅当对每个 $\bar a\in N^n$，扩张结构 $(\mathcal N,\bar a)$ 与 $(\mathcal M,\bar a)$ 在语言 $\mathcal L_N=\mathcal L\cup\{c_a:a\in N\}$ 下初等等价。
- （只查存在量词）判别条件中只需对**形如 $\exists v\,\varphi$**（$v$ 为被存在量词约束的变元，$\varphi$ 任意）的公式验证；等价地，只需验证：凡在 $\mathcal M$ 中可取到满足某个含参数公式的元素，该元素即可在 $\mathcal N$ 中取到。

## 四、证明过程

**步骤 0：记号与基座事实**

“$\mathcal N$ 是 $\mathcal M$ 的子结构”意味着：$N\subseteq M$，$N\ne\varnothing$；每个常数符号 $c$ 有 $c^{\mathcal N}=c^{\mathcal M}\in N$；每个 $k$ 元函数符号 $f$ 满足 $f^{\mathcal N}=f^{\mathcal M}\restriction N^k$ 且 $f^{\mathcal M}(N^k)\subseteq N$；每个 $k$ 元谓词符号 $R$ 满足 $R^{\mathcal N}=R^{\mathcal M}\cap N^k$。

**基座事实（项的值一致）**：对每个项 $t(w_1,\dots,w_n)$ 与每个 $\bar a\in N^n$，由对项的结构归纳可得
$$
t^{\mathcal N}(\bar a)=t^{\mathcal M}(\bar a)\in N .
$$
（$t=x_i$ 时两边为 $a_i$；$t=c$ 时两边为 $c^{\mathcal M}\in N$；$t=f(t_1,\dots,t_k)$ 时由归纳假设 $t_j^{\mathcal N}(\bar a)=t_j^{\mathcal M}(\bar a)\in N$，再由 $f^{\mathcal N}=f^{\mathcal M}\restriction N^k$ 及封闭性得结论。）特别地，这保证了原子公式的真值一致。$\square$

**步骤 1：必要性（$\Rightarrow$）**

设 $\mathcal N\preceq\mathcal M$，$\bar a\in N^n$ 且 $\mathcal M\models\exists v\,\varphi(v,\bar a)$。由初等性（对公式 $\exists v\,\varphi$）得 $\mathcal N\models\exists v\,\varphi(v,\bar a)$，故存在 $b\in N$ 使 $\mathcal N\models\varphi(b,\bar a)$；再对该公式使用初等性得 $\mathcal M\models\varphi(b,\bar a)$。故判别条件成立。$\square$

**步骤 2：充分性的归纳框架（$\Leftarrow$）**

设判别条件成立。我们取连接词 $\neg,\wedge$ 与量词 $\exists$ 为原始符号（$\vee,\to,\forall$ 视为派生符号：$\varphi\vee\psi:=\neg(\neg\varphi\wedge\neg\psi)$，$\forall v\varphi:=\neg\exists v\neg\varphi$）。对公式 $\varphi$ 的结构作归纳，证明命题

$$
(\star_\varphi)\qquad \text{对每个 }n\text{ 与每个 }\bar a\in N^n:\quad \mathcal N\models\varphi(\bar a)\iff\mathcal M\models\varphi(\bar a).
$$

（约定 $\varphi$ 的自由变元包含于 $w_1,\dots,w_n$；对自由变元个数不同的公式，同一陈述按其实际自由变元数理解。）

**步骤 3：原子公式**

设 $\varphi$ 为 $t_1=t_2$ 或 $R(t_1,\dots,t_k)$。由步骤 0 的基座事实，$t_i^{\mathcal N}(\bar a)=t_i^{\mathcal M}(\bar a)$（$i=1,2$）。于是
$$
\mathcal N\models t_1=t_2\iff t_1^{\mathcal N}(\bar a)=t_2^{\mathcal N}(\bar a)\iff t_1^{\mathcal M}(\bar a)=t_2^{\mathcal M}(\bar a)\iff\mathcal M\models t_1=t_2 .
$$
同理，$\mathcal N\models R(t_1,\dots,t_k)\iff(t_1^{\mathcal N}(\bar a),\dots)\in R^{\mathcal N}\iff(t_1^{\mathcal M}(\bar a),\dots)\in R^{\mathcal M}\iff\mathcal M\models R(t_1,\dots,t_k)$，因为 $R^{\mathcal N}=R^{\mathcal M}\cap N^k$。故 $(\star_{\text{原子}})$ 成立。$\square$

**步骤 4：布尔连接词**

设 $(\star_\varphi)$、$(\star_\psi)$ 成立，$\bar a\in N^n$。则
$$
\mathcal N\models\neg\varphi(\bar a)\iff\mathcal N\not\models\varphi(\bar a)\iff\mathcal M\not\models\varphi(\bar a)\iff\mathcal M\models\neg\varphi(\bar a),
$$
$$
\mathcal N\models\varphi\wedge\psi(\bar a)\iff\big(\mathcal N\models\varphi(\bar a)\text{ 且 }\mathcal N\models\psi(\bar a)\big)\iff\big(\mathcal M\models\varphi(\bar a)\text{ 且 }\mathcal M\models\psi(\bar a)\big)\iff\mathcal M\models\varphi\wedge\psi(\bar a).
$$
故 $(\star_{\neg\varphi})$、$(\star_{\varphi\wedge\psi})$ 成立。$\square$

**步骤 5：存在量词（两个方向分别对接）**

设 $(\star_\varphi)$ 成立（其中 $\varphi=\varphi(v,\bar w)$），需证 $(\star_{\exists v\varphi})$。取任意 $\bar a\in N^n$。

（方向一：$\mathcal N\Rightarrow\mathcal M$）设 $\mathcal N\models\exists v\,\varphi(v,\bar a)$。则存在 $b\in N$ 使 $\mathcal N\models\varphi(b,\bar a)$（这里用了 $b\in N$，即 $\mathcal N$ 的论域对量词封闭）。由 $(\star_\varphi)$ 得 $\mathcal M\models\varphi(b,\bar a)$，故 $\mathcal M\models\exists v\,\varphi(v,\bar a)$。

（方向二：$\mathcal M\Rightarrow\mathcal N$）设 $\mathcal M\models\exists v\,\varphi(v,\bar a)$。由判别条件，存在 $b\in N$ 使 $\mathcal M\models\varphi(b,\bar a)$。由 $(\star_\varphi)$ 得 $\mathcal N\models\varphi(b,\bar a)$，故 $\mathcal N\models\exists v\,\varphi(v,\bar a)$。

两个方向合起来即 $(\star_{\exists v\varphi})$。注意方向二正是判别条件被使用的地方：它把 $\mathcal M$ 中的见证“搬进”了 $\mathcal N$。由归纳法（步骤 3–5），$(\star_\varphi)$ 对一切公式成立。$\square$

**步骤 6：全称量词（作为派生情形）**

$\forall v\,\varphi=\neg\exists v\neg\varphi$，由步骤 4、5 立得。也可直接验证：设 $\mathcal M\models\forall v\,\varphi(v,\bar a)$，则对一切 $b\in N\subseteq M$ 有 $\mathcal M\models\varphi(b,\bar a)$，由 $(\star_\varphi)$ 得 $\mathcal N\models\varphi(b,\bar a)$ 对一切 $b\in N$ 成立，故 $\mathcal N\models\forall v\,\varphi(v,\bar a)$；反之若 $\mathcal M\not\models\forall v\,\varphi(v,\bar a)$，则 $\mathcal M\models\exists v\neg\varphi(v,\bar a)$，由判别条件（对公式 $\neg\varphi$ 使用）取 $b\in N$ 使 $\mathcal M\models\neg\varphi(b,\bar a)$，由 $(\star_\varphi)$ 得 $\mathcal N\models\neg\varphi(b,\bar a)$，故 $\mathcal N\not\models\forall v\,\varphi(v,\bar a)$。$\square$

**步骤 7：结论**

步骤 3–6 表明：判别条件成立时，对一切公式 $\varphi$ 与一切参数 $\bar a\in N^n$，$\mathcal N$ 与 $\mathcal M$ 的真值一致。连同 $\mathcal N$ 是子结构这一事实，即 $\mathcal N\preceq\mathcal M$。与步骤 1 合并，判别法得证。$\blacksquare$

**步骤 8：例子的验证（$\mathbb Q\preceq\mathbb R$）**

考虑语言 $\mathcal L=\{<\}$ 与结构 $\mathcal M=\mathbb R$、$\mathcal N=\mathbb Q$。$\mathbb Q$ 是子结构（常元与函数符号均无，只需论域非空）。设 $\bar a\in\mathbb Q^n$ 且 $\mathbb R\models\exists v\,\varphi(v,\bar a)$。稠密线性序理论 DLO 具有量词消去，故 $\varphi$ 在 $\mathbb R$ 中等价于一个无量词公式，即有限个原子公式 $v<a_i$ 或 $a_i<v$ 的布尔组合。于是 $\{x\in\mathbb R:\mathbb R\models\varphi(x,\bar a)\}$ 是 $\mathbb R$ 中有限个有理端点开区间的布尔组合。若它非空，由于 $\mathbb Q$ 在 $\mathbb R$ 中稠密，则它含有理点：最精细的非退化开分量是一个开区间，其端点或为某个 $a_i\in\mathbb Q$、或为 $\pm\infty$，而 $\mathbb Q$ 无端点，故该开区间必含有理数。取 $b\in\mathbb Q$ 使其满足，即得 $\mathbb R\models\varphi(b,\bar a)$。故判别条件成立，$\mathbb Q\preceq\mathbb R$。$\blacksquare$

## 五、应用与意义

**在模型论中的应用**：

1. **Löwenheim–Skolem 下降定理**：给定 $\mathcal M$ 与 $X\subseteq M$，用判别法不断为 $\mathcal M$ 中的存在性公式添加见证（对可数语言，只需处理 $|\mathcal L|$ 多个公式），构造初等链 $X\subseteq\mathcal N_0\preceq\mathcal N_1\preceq\cdots$，取并得基数 $\le\max(|X|,|\mathcal L|)$ 的初等子结构 $\mathcal N\preceq\mathcal M$ 且 $X\subseteq N$。
2. **代数中的初等子结构**：代数闭域理论 ACF 具有量词消去，故代数闭域的代数闭子域是初等子结构（用判别法：解在代数闭包中）；实闭域理论 RCF 亦然，故实闭子域 $\preceq$ 实闭域。
3. **饱和模型与省略类型定理**：判别法把“实现某个型”归结为“为存在性公式提供见证”，是构造 $\omega$-饱和模型与证明类型省略的核心手段。

**理论意义**：判别法给出初等子结构的“局部”刻画——只需验证存在性见证，从而把检验无穷多条公式的困难化为对每个公式验证一个可用具体元素实现的条件。它同时说明：初等性失效的唯一来源是“论域太贫乏以至缺少见证”。

**推广**：对抽象初等类（abstract elementary classes）有对应的 Tarski–Vaught 定理（此时“满足存在性公式的见证”升级为“存在闭包/饱和性条件”）；对无穷语言（$L_{\kappa\lambda}$）有相应判别法；在集合论中，$H_\kappa\prec V$ 的论证（对适当的大基数 $\kappa$）正是判别法的标准应用。

## 课堂问答

**老师**：判断 $\mathcal N\preceq\mathcal M$ 要对无穷多条公式逐条查，Tarski-Vaught 怎么把无穷检验压成一条？

**学生**：结论：当且仅当对每个公式 $\varphi(v,\bar w)$ 与每个 $\bar a\in N^n$，只要 $\mathcal M\models\exists v\,\varphi(v,\bar a)$，就存在 $b\in N$ 使 $\mathcal M\models\varphi(b,\bar a)$——只查存在量词的"见证是否落在 $\mathcal N$ 内"。

**老师（追问）**：为什么只查存在量词就够？全称量词那类错误怎么被顺带覆盖？

**学生**：充分性对公式复杂度归纳。原子公式靠子结构使同一个项在两边取值相同，即 $t^{\mathcal N}(\bar a)=t^{\mathcal M}(\bar a)\in N$；$\neg,\wedge$ 由归纳假设处理；关键是 $\mathcal M\Rightarrow\mathcal N$ 方向：$\mathcal M$ 中的见证由判别条件被"搬进" $\mathcal N$，再由归纳假设回读真值。全称量词写成 $\neg\exists\neg$，其反例恰是一次存在性失败。常见误区是只验证"$\mathcal N$ 中的元素 $\mathcal M$ 中也有"这一显然方向，漏掉真正非平凡的 $\mathcal M\Rightarrow\mathcal N$。

**老师（拓展）**：用这个判别法，$\mathbb Q\preccurlyeq\mathbb R$ 该怎样论证？

**学生**：$\mathbb Q$ 是稠密线性序子结构。DLO 具有量词消去，故任意含参数 $\varphi$ 在 $\mathbb R$ 中等价于有限个 $v<a_i$ 或 $a_i<v$ 的布尔组合，其解集是有限个有理端点开区间的布尔组合；若非空，最精细的非退化开分量以某 $a_i\in\mathbb Q$ 或 $\pm\infty$ 为端点，而 $\mathbb Q$ 稠密且无端点，该开区间必含有理数 $b$，即为见证。故判别条件成立。
