# Ngô 基本引理

> **一句话大白话**：在内窥对应把两个群的共轭类配好以后，一个群上按 $\kappa$ 加权的轨道积分，恰好等于较小内窥群上的稳定轨道积分；Langlands 稳定化需要的这条局部恒等式，Ngô 用 Hitchin 纤维化的几何方法证明了。
>
> **小例子**：在 $GL(1)$ 的平凡内窥情形，$H=G$、$\kappa=1$，稳定共轭类就是一个共轭类，基本引理退化为单位测试函数下 $O_\gamma(\mathbf1_{G(\mathcal O)})=SO_\gamma(\mathbf1_{G(\mathcal O)})$。一般群的难点则是同一稳定共轭类内有多个有理共轭类，必须正确加权后才能匹配。

## 介绍

基本引理原是 Langlands 与 Shelstad 为稳定化 Arthur-Selberg 迹公式提出的**猜想**。Ngô 的证明使其标准非分歧形式成为**定理**：他先处理正特征局部域上的李代数版本，关键工具是 Hitchin 纤维化、Picard 栈作用、perverse 层上同调分解与支持定理。结合 Waldspurger 等人的李代数—群版本转换、正特征到特征零的转移以及内窥技术，可得到通常的 $p$-adic 非分歧基本引理表述。不能把这一历史简化为“Ngô 单篇论文直接证明了所有群、所有扭曲及加权推广”。

## 分析

**前置依赖**：非 Archimedes 局部域上的约化群及其李代数、非分歧群与内窥数据、稳定共轭、轨道积分与稳定轨道积分、$\kappa$-轨道积分、转移因子、Hitchin 纤维化、$\ell$-进层与 Grothendieck-Lefschetz 迹公式、迹公式的稳定化。

**定理内容**：以下采用 Ngô 几何证明直接对应的**李代数、单位测试函数**形式。设 $F$ 为非 Archimedes 局部域，$G$ 为非分歧连通约化群，$H$ 为由椭圆内窥数据给出的非分歧内窥群，$\kappa$ 为相应的内窥特征。取相容的 Haar 测度与 Langlands-Shelstad 转移因子规范。设 $\mathfrak g,\mathfrak h$ 为它们的李代数，$\mathbf1_{\mathfrak g(\mathcal O)}$、$\mathbf1_{\mathfrak h(\mathcal O)}$ 为相应整点的特征函数。

若 $a_H\in\mathfrak h(F)$ 与 $a\in\mathfrak g(F)$ 是匹配的正则半单元，则基本引理断言

$$
\boxed{
\Delta(a_H,a)\,O_a^{G,\kappa}\!\left(\mathbf1_{\mathfrak g(\mathcal O)}\right)
=SO_{a_H}^{H}\!\left(\mathbf1_{\mathfrak h(\mathcal O)}\right)
}
$$

其中稳定轨道积分按 $H(F)$-共轭类求和，

$$
SO_{a_H}^{H}(f^H)
=\sum_{\substack{a_H'\sim_{\mathrm{st}}a_H\\
a_H'/\!\sim_{H(F)}}}O_{a_H'}^H(f^H),
$$

而 $\kappa$-轨道积分为

$$
O_a^{G,\kappa}(f)
=\sum_{\substack{a'\sim_{\mathrm{st}}a\\
a'/\!\sim_{G(F)}}}
\langle\kappa,\operatorname{inv}(a,a')\rangle\,O_{a'}^G(f).
$$

这里 $\operatorname{inv}(a,a')$ 记录同一稳定类内两个有理共轭类的差异，$\Delta$ 是转移因子；不同文献把 $\Delta$ 放在等式哪一侧的约定不同，但不能无说明地删去。单个轨道积分具有伴随轨道上的标准形式

$$
O_a^G(f)=
\int_{G_a(F)\backslash G(F)}f(g^{-1}ag)\,d\dot g .
$$

在相应的非分歧群版本中，把匹配元素换为群中的正则半单元，把测试函数换为 $\mathbf1_{G(\mathcal O)}$ 与 $\mathbf1_{H(\mathcal O)}$，可写成同类恒等式

$$
\Delta(\gamma_H,\gamma)\,O_\gamma^{G,\kappa}(\mathbf1_{G(\mathcal O)})
=SO_{\gamma_H}^{H}(\mathbf1_{H(\mathcal O)}).
$$

基本引理说的是**经过转移因子与测度规范后的轨道积分相等**，并不是说两个积分都必然等于 $1$，也不是 Langlands 函子性猜想本身的证明。

## 思考过程

局部轨道积分看似是单个局部域上的积分，直接逐项比较稳定类非常困难。Ngô 的转变是把这些积分放入整体曲线上的 Hitchin 模问题：固定整体数据后，迹公式把 Hitchin 模空间的点计数写成各局部轨道积分的乘积。另一方面，Hitchin 纤维化的直接像层带有 Picard 栈作用，其 $\kappa$-同型部分携带的正是 $\kappa$-轨道积分信息。

因此问题被改写为几何稳定化：证明 Hitchin 纤维化的 $\kappa$-部分与内窥群 Hitchin 纤维化的稳定部分具有相同的 perverse 上同调贡献。这里的核心技术障碍是“支持”可能很小，普通的整数纤维计数不足以控制导出层；Ngô 的支持定理恰好排除了多余的支撑，使几何比较能够成立。最后再选择整体情形，把未知只留在一个局部位置，从整体恒等式读出该处的局部恒等式。

## 证明过程

**诚实证明纲要（不是自足的逐步证明）**。以下步骤依赖上述测度、转移因子、整体 Hitchin 模型及适用范围内的正则性条件；完整证明横跨长篇论文，不能用几句纤维计数代替。

### 1. 整体化局部问题

在有限域 $\mathbb F_q$ 上的光滑射影曲线及相应函数域中构造整体群、内窥数据和 Hitchin 基底，使一个选定位置 $v$ 给出待证的局部李代数轨道积分。通过 Adele 化与 Hitchin 模空间的点计数，Grothendieck-Lefschetz 迹公式把 $\ell$-进上同调的迹转化为整体轨道和，再写成各局部轨道积分的乘积。

### 2. 用 Picard 作用提取 $\kappa$-部分

在正则半单 Hitchin 基底上，Hitchin 纤维化 $f:\mathcal M\to\mathcal A$ 带有 Picard 栈 $\mathcal P$ 的作用。稳定共轭类内部的不同有理形式由相应 Picard/组件群的 $\mathbb F_q$-点控制。对 $Rf_*\overline{\mathbb Q}_\ell$ 按 $\kappa$ 取同型成分，得到的迹正对应局部 $\kappa$-轨道积分，而内窥群一侧相应给出稳定轨道积分。

### 3. 应用 Ngô 支持定理

对 Hitchin 纤维化的 perverse 上同调层作支撑分析。Ngô 支持定理识别了不可约组成因子的可能支撑：在椭圆及相应非退化范围内，支撑由 $G$ 自身及其内窥群的 Hitchin 基底给出，排除了会妨碍稳定化的额外支撑。此处必须使用 perverse 层和导出直接像，不能仅用普通顶层函数或只数光滑纤维的点。

### 4. 几何稳定化并比较两侧

利用 Picard 作用的分解、支持定理以及内窥 Hitchin 基底之间的映射，把 $G$ 的 $\kappa$-同型上同调贡献与 $H$ 的稳定上同调贡献匹配。对两侧分别应用 Grothendieck-Lefschetz 迹公式，再把所得整体恒等式整理成局部轨道积分乘积的恒等式。

### 5. 隔离一个局部因子并转移特征

选取其余位置的数据，使相应局部恒等式已由分裂、拓扑平凡或其他已知情形处理，同时保证所比较的整体项非退化。约去已知因子后，在位置 $v$ 留下所需的单位测试函数基本引理。标准延展与局部化论证给出正特征局部域版本；特征零情形再结合 Waldspurger 等人的转移结果获得。

这些步骤说明证明的逻辑骨架，但不替代支持定理、整体化构造、测度相容性和隔离局部因子的详细论证，也不把其它未解决的内窥或函子性推广冒充为本定理的推论。

## 课堂问答

**老师**：Ngô 基本引理究竟是定理还是猜想，核心等式是什么？

**学生**：它最初是 Langlands-Shelstad 猜想，标准非分歧形式现已成为定理。李代数单位测试函数版本写作 $\Delta(a_H,a)O_a^{G,\kappa}(\mathbf1_{\mathfrak g(\mathcal O)})=SO_{a_H}^H(\mathbf1_{\mathfrak h(\mathcal O)})$：左边含转移因子以及按 $\kappa$ 加权的有理共轭类轨道积分和，右边是内窥群上的稳定轨道积分。

**老师（追问）**：为什么不能把等式简单说成“两个群同一元素的轨道积分相同”？

**学生**：因为匹配发生在稳定共轭类之间，同一稳定类可含多个 $G(F)$-共轭类。左边必须按 $\operatorname{inv}(a,a')$ 引入 $\kappa$ 权重，并配合转移因子与 Haar 测度规范；右边则取稳定轨道积分和。积分本身也不必等于 $1$。

**老师（拓展）**：Ngô 的几何方法解决了什么旧方法难以处理的障碍，又留下了哪些问题？

**学生**：Hitchin 纤维化把局部轨道积分整体化，Picard 作用提取 $\kappa$-部分，支持定理控制 perverse 上同调的可能支撑，从而使 $\kappa$ 部分与内窥群的稳定部分可比较。它证明了基本引理并推动迹公式稳定化，但不等于证明完整的 Langlands 函子性；扭曲、加权及其它推广各有额外假设与后续工作，不能一概归入同一个已证结论。

## 相关条目

- [稳定迹公式](./稳定迹公式.md)
- [局部 Langlands 对应](./局部Langlands对应.md)
- [Langlands 函子性猜想](./Langlands函子性猜想.md)
- [Hitchin 纤维化与可积系统](../第142级-几何朗兰兹/Hitchin纤维化与可积系统.md)
- [Lefschetz迹公式](../第143级-椭圆曲线与模形式/Lefschetz迹公式.md)：直接前置依赖。
