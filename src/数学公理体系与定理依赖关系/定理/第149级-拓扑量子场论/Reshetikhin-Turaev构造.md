# Reshetikhin-Turaev构造
>
> **一句话大白话**：从量子群在根单位处的表示论构造三维流形和纽结的不变量与 TQFT——这就是 Reshetikhin–Turaev 构造，一个纯代数-图论配方。
>
> **小例子**：对 $U_q(\mathfrak{sl}_2)$（$q$ 根单位），赋给三维流形不变量经手术——把流形表示为 $S^3$ 沿链环的手术，再用量子 $6j$ 计算。得到 RT 不变量 / TQFT。

## 一、定理介绍

> **前置依赖**：量子群$U_q(\mathfrak{g})$、R-矩阵与辫结、模块化张量范畴、编织tangle赋值、Dehn手术定理

Reshetikhin–Turaev 构造（RT，Reshetikhin–Turaev 1991）以量子群（$U_q(\mathfrak g)$、$q=\exp(2\pi i/(k+h^\vee))$）的有限维表示构造出一个模块化张量范畴，再用"手术 + R-矩阵"给出三维定向流形与纽结的量子不变量，并进而得到一个三维 TQFT。它与 Witten 的 Chern–Simons 理论相符，是 Jones 型不变量的严谨代数实现。

## 二、原理思路

构造分四步：(1) 令 $q$ 为根单位，得半单模数 Tensor 范畴 $\operatorname{Rep}(U_q(\mathfrak g))$（+脊 $\theta$、S-矩阵）；(2) 用范畴的 R-矩阵/辫结数据给 **带边图（tangle）** 赋值（图画演算是范畴的"布线"）；(3)把三维流形表示为沿链环的**手术**（$S^3\setminus$ tubular），其不变量为对这些链接的编织求值经 S-矩阵求和；(4) 验证 Atiyah 公理得 TQFT。

## 三、定理的严格表述

对单 Lie 代数 $\mathfrak g$，level $k$，$q=e^{2\pi i/(k+h^\vee)}$（$h^\vee$ 对偶 Coxeter 数），存在模块化张量范畴 $\mathcal C=\operatorname{Rep}_f(U_q(\mathfrak g))$ 与三维 TQFT
$$
Z_q^{\mathrm{RT}}:\operatorname{Cob}_3^{\mathrm{or}}\to\operatorname{Vect}_{\mathbb C}.
$$
对闭三流形 $M$（$S^3$ 沿 link $L$ 手术），其不变量由图示全息求出，如
$$
Z_q^{\mathrm{RT}}(S^3)=1,\qquad \langle W_R(L)\rangle_{\mathrm{RT}}=V_L(q^{-2})…\text{（对应情形）}.
$$

## 四、证明过程

先验证 $\mathcal C$ 满足模块化公理（辫 S-、$\theta$，S 可逆）——模数条件须 $q$ 根单位；定义编织图的赋值（对咕w/右-目标用 R + 迹）；把三流形"手术分解"（Dehn 手术沿 framed link），将对 link 各部分算得的量子不变量的 S-转会求和给出流形不变量；逐一验证 Atiyah 公理（配分、粘合、规范化），得到 TQFT。

## 五、应用与意义

RT 构造使 Witten 的不变量成为严格数学对象，奠基了量子群-TQFT 与低维拓扑的现代交互，产出 Turaev–Viro、RT/WRT 不变量与胞腔代数、模范畴理论，是模张量范畴与 TQFT 分类的基础工具，广泛应用于拓扑、表示论与数学物理。

## 课堂问答

**老师**：RT 构造为什么不直接用 Chern–Simons 路径积分，而要走量子群的表示论？

**学生**：结论：为了给出严格且纯代数的定义。取 $q=\exp\!\big(\frac{2\pi i}{k+h^\vee}\big)$ 为根单位，则 $\mathcal C=\operatorname{Rep}_f(U_q(\mathfrak g))$ 是半单模张量范畴，带 R-矩阵（辫结）与 S-矩阵，于是三维流形与纽结的不变量都能用"图 + 量子 $6j$ 求和"算出：

$$
Z_q^{\mathrm{RT}}:\operatorname{Cob}_3^{\mathrm{or}}\to\operatorname{Vect}_{\mathbb C},\qquad Z_q^{\mathrm{RT}}(S^3)=1 .
$$

**老师（追问）**：为什么一定要 $q$ 是根单位？S-矩阵在这里扮演什么角色？

**学生**：只有当 $q$ 是根单位时，$U_q(\mathfrak g)$ 的表示范畴才"几乎半单"、可约到有限多个对象，S-矩阵才可逆，模块化公理才成立。S-矩阵实现 Dehn 手术的换基：把 $S^3$ 沿 framed link 手术，就是把各链环分量的赋值再用 S-矩阵求和，从而得到与手术表示无关的不变量。常见误区：把 $Z_q^{\mathrm{RT}}(S^3)=1$ 当成全部结论，其实它只是归一化条件。

**老师（拓展）**：这与 Witten 的 Chern–Simons 不变量到底是什么关系？

**学生**：两者在 $SU(2)$ 情形下于 $t=e^{2\pi i/(k+2)}$ 处吻合，RT 正是 Witten 路径积分的严格代数实现。更一般地，Turaev–Viro 给出对应的态和模型，把不变量变成有限求和，从而使低维拓扑的计算进入纯组合的领域。
