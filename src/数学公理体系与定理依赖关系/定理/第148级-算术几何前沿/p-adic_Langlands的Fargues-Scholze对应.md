# p-adic Langlands的Fargues-Scholze对应
>
> **一句话大白话**：p(≠ℓ) 局部 Langlands 对应可以"几何化"到 Fargues–Fontaine 曲线的层/向量丛语言，得到一个拟凝聚层层的整体对应（Fargues–Scholze）。
>
> **小例子**：$G(K)$（$K/\mathbb Q_p$）的光滑表示的 $D$-模块的"解析范畴"与 $G$-向量丛的category 拟凝聚层对应，Hecke 态射把开邦与 $\widehat G$ 参数联系。

## 一、定理介绍

> **前置依赖**：Fargues-Fontaine曲线的构造与性质、$\varphi$-模块、$G$-向量丛与$\operatorname{Bun}_G$、拟凝聚层范畴、Hecke算子与$\mathbf{L}$-参数

p-adic Langlands 的 Fargues–Scholze 对应（Fargues–Scholze 2021）把 $p$-adic（特征 $p\ne \ell$）局部 Langlands 对应几何化到 Fargues–Fontaine 曲线：拟结出 $(G(K)$ 的光滑表示) 的 $(\infty,\ell)$-范畴到（$Fargues\–Fontaine$ 曲线上 $G$-向量丛的层）的拟凝聚层范畴的等价，并使其 Hecke 作用与 $\ell$-adic 表示一致——成为 p-adic Langlands 的现代几何实现。

## 二、原理思路

利用 Fargues–Fontaine 曲线的向量丛分类与 $\varphi$-模块：$G(K)$ 的不可约表示经由其 $\mathbf L$-参数（$\varphi$-模块）编码成曲线上 $^LG$-向量丛。定义表示范畴的"解析"核与层范畴的 Hecke 动作（供给层／关键层），经对偶构造得到整体等价：它把对象（如光滑表示、超cuspidal）映为拟凝聚层，并满足 Iwahori 与 orbital 的配方。

## 三、定理的严格表述（主断言）

设 $K/\mathbb Q_p$，$G$ 为 $K$-拓扑约化群，$\widehat G$ 为对偶群，$\ell\ne p$。设 $\mathcal C_{G}$ 为 $G(K)$ 的 $d$-g 光滑表示合成范畴（$(\infty)-$完全列群），$\operatorname{QCoh}([\operatorname{Bun}_{G}]/…)$ 为 Fargues–Fontaine 局部曲线上 $G$-向量丛的拟凝聚层范畴。则存在 $(\infty)$-范畴等价
$$
\mathcal C_{G(K)}\;\cong\;\operatorname{QCoh}(\operatorname{Bun}_{G}),
$$
使 Hecke 算子族的动作与 $\mathbf L$-参数（由 $\varphi$-模块/局部系统）匹配。

## 四、证明过程

路线（Fargues–Scholze 纲要）：先用 $\varphi$-模块与 Fargues–Fontaine 曲线建立 $G$-向量丛与分级（过完备）对象的一一；定义向量丛层的拟凝聚层范的 Hecke 积（经关键层 $\mathbb B$ 的融合对象）；构造从光滑表示到"关键层"的降低（Bernstein–Zelevinsky/几何化）；把构成重解释为拟凝聚，并用公开的 $\mathbf L$-参数（$\varphi$-semilinear 的 Garding 谱数据）验证 Hecke 匹配，从而得到范畴对应。

## 五、应用与意义

此对应是 $p$-adic Langlands（尤其 $\ell\ne p$ 情形）几何化研究方向：统一局部 Langlands、向量丛与 $\widehat T$、模空间 $\operatorname{Bun}_G$ 的结构，其整体性（层论）使之能承接深度、棱与缠绕分析，并延伸到 $\mathbf L$-函子性与算术几何的现代问题。

## 课堂问答

**老师**：Fargues–Scholze 对应的主断言是什么？

**学生**：结论：存在 $(\infty)$-范畴等价 $\mathcal C_{G(K)}\cong\operatorname{QCoh}(\operatorname{Bun}_G)$，把 $G(K)$ 的光滑表示范畴对应到 Fargues–Fontaine 曲线上 $G$-向量丛的拟凝聚层范畴，并使 Hecke 算子的作用与 $\mathbf L$-参数匹配（$\ell\ne p$）。

**老师（追问）**：Hecke 对应在层那一侧是怎样实现的？

**学生**：借 $\varphi$-模块把 $G(K)$ 的不可约表示编码成曲线上 ${}^LG$-向量丛；Hecke 算子由关键层（如 $\mathbb B$ 的融合积）的作用给出，其谱数据正是 $\mathbf L$-参数（$\varphi$-半线性 / Garding 谱）。构造从光滑表示到"关键层"的下降（Bernstein–Zelevinsky / 几何化），再把整体形式重解释为拟凝聚层，从而验证 Hecke 与局部 Langlands 参数对齐。

**老师（拓展）**：这个对应为什么重要？

**学生**：它把局部 Langlands（$\ell\ne p$）几何化，统一了表示论、$\operatorname{Bun}_G$ 与对偶群理论，是 Fargues 猜想的现代实现。其层论整体性使它能够承接棱（prism）、缠绕与 $\mathbf L$-函子性问题，并通向算术几何与"几何局部 Langlands"的前沿。 一句话：它把 p-adic 局部 Langlands 从表示论搬到了 Fargues–Fontaine 曲线上的层论舞台。
