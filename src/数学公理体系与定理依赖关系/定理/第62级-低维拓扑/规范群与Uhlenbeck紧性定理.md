# 规范群与 Uhlenbeck 紧性定理

> **一句话大白话**：曲率能量有界的连接列，经过适当的规范变换后，会"除有限个点之外"收敛；没能收敛的那些点正是曲率能量像气泡一样集中的地方。这使杨–米尔斯模空间可以被紧化。
>
> **小例子**：在四维小球上若 $U(1)$ 连接的曲率满足 $\lVert F_A\rVert_{L^2}<\varepsilon$（能量很小），就存在规范变换把 $A$ 化到库仑规范并有 $\lVert A\rVert_{W^{1,2}}\leq C\lVert F_A\rVert_{L^2}$；于是"小能量"的连接完全受控，收敛失败的只是有限个能量集中点。

## 一、定理介绍

> **前置依赖**：Uhlenbeck紧性定理、四维流形理论、规范场论与 Yang–Mills 方程、Hodge分解定理、Sobolev嵌入定理、椭圆正则性定理。

规范群与 Uhlenbeck 紧性定理是 Karen Uhlenbeck 在 1982 年两篇论文中建立的分析工具：第一篇给出"局部规范修补引理"（gauge fixing lemma，用规范群把连接化到库仑规范并给出 $W^{1,2}$ 估计），第二篇给出 Yang–Mills 场的可去奇点定理；两者的结合给出一般 $L^2$ 曲率界下的紧性定理（Uhlenbeck compactness），即本条目所述内容。

其动机是为 Donaldson 在 1980 年代发展的四维流形不变量理论提供解析基础。Donaldson 用反自对偶（ASD）连接模空间来定义流形不变量，而模空间在自然拓扑下不紧；要让"计数"有意义，必须理解模空间的紧化。Uhlenbeck 的结论说明：极限对象是"除有限点外光滑的 Yang–Mills 连接 $+$ 有限个气泡"，能量在极限下守恒，于是有可控的紧化。

定理的意义有四个层面。其一，它确立了规范理论中"局部规范 + 椭圆估计"的标准技术路线。其二，它给出曲率能量的量化（每个坏点至少携带 $\varepsilon$ 的能量），从而坏点个数受总能量控制。其三，它支撑 Donaldson 与 Seiberg–Witten 不变量的整体理论，以及四维光滑结构的分类结果。其四，它被推广到 $L^p$ 曲率界、一般维数、一般紧李群与特殊和乐几何的紧性定理，成为几何分析的通用工具。

## 二、原理思路

1. **局部化**：用测地凸的小球覆盖流形并取主丛的平凡化，把问题拉到 $\mathbb R^4$ 的球上处理。

2. **规范修补**：在小能量的球上，用规范群把连接化到库仑规范 $d^*A=0$，再由椭圆估计与临界嵌入 $W^{1,2}\subset L^4$ 吸收非线性项，得到 $\lVert A\rVert_{W^{1,2}}\leq C\lVert F_A\rVert_{L^2}$。

3. **有限覆盖下的拼装**：在每个小球的 Coulomb 规范下取收敛子列；只有能量始终超过阈值 $\varepsilon$ 的球才可能不收敛，而这些球（坏点）个数由总能量除以 $\varepsilon$ 控制，故有限。

4. **气泡与能量量化**：在坏点处作"吹起"（blow-up）伸缩，四维共形不变性使曲率 $L^2$ 范数不变量，得到不可延拓的极限（气泡），每份至少贡献能量 $\varepsilon$。

5. **极限与紧化**：去掉坏点后连接弱 $W^{1,2}$ 收敛到 Yang–Mills 连接，能量在极限下守恒，从而得到模空间的 Uhlenbeck 紧化。

## 三、定理的严格表述

**定理（Uhlenbeck 紧性定理）**：设 $M$ 是紧、可定向的 $4$ 维 Riemann 流形，$G$ 是紧李群，$P\to M$ 为主 $G$-丛，$\{A_k\}$ 是 $P$ 上连接的序列，且
$$\sup_k\lVert F_{A_k}\rVert_{L^2(M)}<\infty .$$
则存在子列（仍记 $A_k$）、有限点集 $\Sigma=\{x_1,\dots,x_m\}\subset M$、$M\setminus\Sigma$ 上的规范变换 $u_k\in\Gamma(\operatorname{Ad}P)$ 与连接 $A_\infty$，使
$$u_k(A_k)\ \rightharpoonup\ A_\infty\quad\text{于}\ W^{1,2}_{\operatorname{loc}}(M\setminus\Sigma),$$
且 $A_\infty$ 是 $M\setminus\Sigma$ 上的 Yang–Mills 连接，即满足
$$\nabla_{A_\infty}^*F_{A_\infty}=0 .$$
每个坏点满足能量量化：存在常数 $\varepsilon=\varepsilon(G)>0$（与 $k$、$M$ 无关）使对一切 $r>0$
$$\liminf_{k\to\infty}\int_{B_r(x_j)}\lvert F_{A_k}\rvert^2\ \geq\ \varepsilon ,\qquad j=1,\dots,m .$$
于是
$$m\ \leq\ \frac{1}{\varepsilon}\liminf_{k\to\infty}\lVert F_{A_k}\rVert_{L^2(M)}^2 .$$

**定理（小能量规范修补引理）**：存在 $\varepsilon>0$、$C>0$ 使：若 $A$ 是 $B^4$ 上的连接且 $\lVert F_A\rVert_{L^2(B^4)}<\varepsilon$，则存在规范变换 $u$ 使 $u(A)$ 满足库仑规范 $d^*u(A)=0$、$u(A)\cdot\nu=0$（法向分量消灭，边界条件）且
$$\lVert u(A)\rVert_{W^{1,2}(B^4)}\ \leq\ C\,\lVert F_A\rVert_{L^2(B^4)} .$$

**定理（可去奇点定理）**：若 $A$ 是 $B^4\setminus\{0\}$ 上的 Yang–Mills 连接且 $\lVert F_A\rVert_{L^2(B^4)}<\varepsilon$，则存在规范变换使 $A$ 光滑延拓到整个 $B^4$，且延拓后仍是 Yang–Mills 连接。

## 四、证明过程

**步骤 1（局部平凡化与 Hodge 分解）。** 取 $M$ 的一个由测地凸球 $\{B_\alpha=B_{r_\alpha}(x_\alpha)\}$ 组成的有限覆盖，在每个 $B_\alpha$ 上取 $P$ 的平凡化，使连接表示为 $\mathfrak g$-值 1-形式 $A_\alpha$。在 $B_\alpha$ 上用 Hodge 分解定理把 $A_\alpha$ 正交分解为
$$A_\alpha=d\xi+d^*\eta+h,\qquad h\ \text{调和（有限维空间）},$$
其中 $d\xi$ 部分可由规范变换 $u=e^{\xi}$ 消去。于是可用规范群把 $A_\alpha$ 化为满足库仑规范的部分，问题归结为对满足 $d^*A=0$ 的连接的估计。

**步骤 2（小能量的 Coulomb 规范化与估计）。** 设 $d^*A=0$，且 $A$ 在 $B^4$ 上曲率 $L^2$ 范数小于待定常数 $\varepsilon$。由 $F_A=dA+\tfrac12[A\wedge A]$ 与 $d^*A=0$ 得椭圆方程组
$$\Delta A=d^*F_A+\ \text{（关于 }A\text{ 的二次项）}.$$
由椭圆正则性定理与四维临界 Sobolev 嵌入定理 $W^{1,2}(B^4)\subset L^4(B^4)$，用 bootstrap 得到先验估计
$$\lVert A\rVert_{W^{1,2}(B)}\ \leq\ C_1\big(\lVert F_A\rVert_{L^2(B)}+\lVert A\rVert_{L^4(B)}^2\big)\ \leq\ C_2\big(\lVert F_A\rVert_{L^2(B)}+\lVert A\rVert_{W^{1,2}(B)}^2\big).$$
当 $\lVert F_A\rVert_{L^2}<\varepsilon$ 且 $\varepsilon$ 足够小时，令 $a=\lVert A\rVert_{W^{1,2}}$，上式给出 $a\leq C_2(\varepsilon+C_2a^2)$；由连续性方法（先在小球或作伸缩使 $a$ 足够小，再放大回去）可解出 $a\leq C\lVert F_A\rVert_{L^2}$。这就是规范修补引理，它把"曲率小"升级为"连接在 Coulomb 规范下 $W^{1,2}$ 小"。

**步骤 3（有限覆盖下的拼装与坏点的有限性）。** 设 $\lVert F_{A_k}\rVert_{L^2(M)}\leq E$ 对一切 $k$。加细覆盖使每个球都可取到满足步骤 2 的尺度（球的半径由单射半径与 $\varepsilon$ 决定）。对每个球 $\alpha$：
$$\text{若}\ \limsup_{k}\int_{B_\alpha}\lvert F_{A_k}\rvert^2<\varepsilon,\ \text{则由步骤 2 得 }\lVert A_k\Vert_{W^{1,2}(B_\alpha)}\ \text{一致有界}.$$
由 Rellich–Kondrachov 紧嵌入（在略小的球上）与可数对角化，在这些球上存在符合 Coulomb 规范的 $W^{1,2}$ 收敛子列。对不满足该能量条件的球，通过二分（把球半径减半并考察能量的稳定性）可定位出有限个"坏点" $x_j$：每个坏点的任意小邻域内能量始终 $\geq\varepsilon$，且不同坏点可取不交的小球。由能量总上界 $E^2$，坏点个数满足 $m\leq E^2/\varepsilon$，故有限。

**步骤 4（坏点处的能量量化与气泡）。** 固定坏点 $x_j$。由能量沿半径的连续性，取 $r_k\downarrow0$ 使
$$\int_{B_{r_k}(x_j)}\lvert F_{A_k}\rvert^2=\varepsilon .$$
作伸缩（blow-up）
$$\hat A_k(y):=r_k\,A_k\big(x_j+r_k\,y\big),\qquad y\in B_{1}(0)\subset\mathbb R^4 .$$
四维 Yang–Mills 能量在共形伸缩下不变：$\lVert F_{\hat A_k}\rVert_{L^2(B_1)}^2=\lVert F_{A_k}\rVert_{L^2(B_{r_k}(x_j))}^2=\varepsilon$，故 $\hat A_k$ 仍有界的曲率能量，且按尺度 $r_k\to0$，其"坏点"被放大为有限能量对象。若 $\hat A_k$ 在 $B_1$ 上有界，则由步骤 2、3 与其能量恰为 $\varepsilon$ 得极限连接 $\hat A_\infty$；由于 $\varepsilon$ 是"可规范化"与"不可规范化"的分界（步骤 2 中的常数），$\hat A_\infty$ 不可能由规范变换平凡化（否则其能量可被吸收，与 $\varepsilon$ 的选择矛盾）。因此每个坏点至少携带一份能量 $\varepsilon$，此即能量量化。

**步骤 5（极限连接满足 Yang–Mills 方程）。** 固定 $M\setminus\Sigma$ 的一个紧子集 $K$。由步骤 3，$K$ 可被有限个"好球"覆盖，故存在规范变换使 $A_k$ 在 $K$ 上 $W^{1,2}$ 一致有界，从而子列弱收敛到 $A_\infty\in W^{1,2}(K)$。证方程：对任一紧支试验 1-形式 $\varphi$，$F_{A_k}$ 弱收敛于 $F_{A_\infty}$（弱收敛与二次项的一致性由 $W^{1,2}\subset L^4$ 的嵌入与弱收敛乘积定理保证），而 Yang–Mills 方程 $\nabla^*_{A_k}F_{A_k}=0$ 的弱形式是线性与二次项的组合，取极限得 $\nabla^*_{A_\infty}F_{A_\infty}=0$。故 $A_\infty$ 是 Yang–Mills 连接。

**步骤 6（可去奇点与紧化结论）。** 若把坏点集 $\Sigma$ 选得足够细，使每个坏点附近"未计入气泡"的能量小于 $\varepsilon$，则由可去奇点定理，$A_\infty$ 可规范地延拓过该点成为光滑 Yang–Mills 连接；反之，$A_\infty$ 在那里确实奇异，能量就在该点集中并表现为一个气泡（理想 instanton）。因此极限对象为"$M\setminus\Sigma$ 上的 Yang–Mills 连接 $+$ $\Sigma$ 处的气泡个数"，且能量满足
$$\lim_{k\to\infty}\lVert F_{A_k}\rVert_{L^2(M)}^2=\lVert F_{A_\infty}\rVert_{L^2(M)}^2+\sum_{j=1}^{m}E_j,\qquad E_j\geq\varepsilon .$$
这就是 Yang–Mills 模空间的 Uhlenbeck 紧化。$\square$

## 五、应用与意义

- **Donaldson 理论**：ASD 连接模空间的紧化、不变量定义与定向问题都依赖本定理；坏点处的气泡对应"理想解"，使计数与拓扑不变量一致。
- **Seiberg–Witten 理论**：解析基础同样是 Uhlenbeck 型紧性与小能量可去奇点定理，Taubes 的工作进一步给出四维流形的不变量与标准形。
- **曲率集中与气泡分析**：四维共形不变性导致的"气泡"现象与调和映射热流、Ricci 流手术中的奇点分析同源，构成几何分析的通用手法。
- **规范群的作用**：规范修补引理说明在"小能量"区域，规范群可把连接空间局部化为 Coulomb 切片，从而用有限维切片研究模空间。
- **推广**：$L^p$ 曲率界下的 Uhlenbeck 紧性、一般维数与一般紧李群的情形、以及 Spin(7)、$G_2$ 等特殊和乐几何中的紧性定理，都沿用"局部规范 $+$ 能量量化"的框架。

## 课堂问答

**老师**：这条条目与 Uhlenbeck 紧性定理有何区别？它强调什么？

**学生**：结论：这里强调规范群的作用与三层结构——小能量规范修补引理、能量量化、可去奇点定理。核心估计：若 $\|F_A\|_{L^2(B^4)}<\epsilon$，则存在规范 $u$ 使 $d^*u(A)=0$、$u(A)\cdot\nu=0$ 且 $\|u(A)\|_{W^{1,2}}\le C\|F_A\|_{L^2}$。即规范群把连接空间局部化为库仑切片，使模空间可用有限维切片研究。

**老师（追问）**：能量量化的常数从何而来？

**学生**：$\epsilon$ 是可规范化与不可规范化的分界。先用 Hodge 分解 $A=d\xi+d^*\eta+h$ 消去 $d\xi$ 部分，再得估计 $a\le C_2(\epsilon+C_2a^2)$，$\epsilon$ 取到使二次项可吸收（$C_2a\le\tfrac12$）。坏点处吹起后的极限若能量恰为 $\epsilon$ 且不可规范平凡化，就给出每点至少 $\epsilon$ 的能量量化。

**老师（拓展）**：极限为什么满足 Yang–Mills 方程？

**学生**：在 $M\setminus\Sigma$ 的紧集上，好球覆盖给出 $W^{1,2}$ 一致界，子列弱收敛到 $A_\infty$。取试验形式 $\varphi$，由 $W^{1,2}\subset L^4$ 与弱收敛乘积定理 $F_{A_k}\rightharpoonup F_{A_\infty}$，对弱形式 $\nabla^*_{A_k}F_{A_k}=0$ 取极限得 $\nabla^*_{A_\infty}F_{A_\infty}=0$。故极限是 Yang–Mills 连接，并有能量恒等式 $\lim\|F_{A_k}\|^2=\|F_{A_\infty}\|^2+\sum_jE_j$，$E_j\ge\epsilon$。

## 相关条目

- [Uhlenbeck紧性定理](./Uhlenbeck紧性定理.md)：本条目给出其局部规范修补、能量量化与气泡分析的具体机制。
- [四维流形理论](./四维流形理论.md)：Donaldson、Seiberg–Witten 不变量与模空间紧化的拓扑背景。
- [双曲化定理](./双曲化定理.md)：同为几何拓扑中"紧性与退化（气泡 / cusp）"结构的核心定理。
- [Hodge分解定理](../第49级-黎曼几何/Hodge分解定理.md)：步骤 1 中把连接作 Hodge 正交分解的工具。
- [Sobolev嵌入定理](../第40级-偏微分方程/Sobolev嵌入定理.md)：四维临界嵌入 $W^{1,2}\subset L^4$ 与非紧性（气泡）的来源。
- [椭圆正则性定理](../第40级-偏微分方程/椭圆正则性定理.md)：步骤 2 中把曲率界提升为 $W^{1,2}$ 界。
- [Fréchet-Kolmogorov紧性准则](../第40级-偏微分方程/Fréchet-Kolmogorov紧性准则.md)：紧性判据在取收敛子列时的使用。
