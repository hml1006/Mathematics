# Hom函子与表示定理

> **一句话大白话**：把对象 $A$ 与其它对象之间的所有态射打包起来，就得到一个"Hom 函子"；若一个集合值函子与某个 Hom 函子自然同构，就说它**可表**。表示定理说：可表当且仅当存在一个"万能元素"，且表示对象在同构意义下唯一。
>
> **小例子**：在集合范畴中，$\mathrm{Hom}_{\mathbf{Set}}(A,-)$ 把集合 $X$ 送到"从 $A$ 到 $X$ 的全部映射"。对固定元素 $a\in A$，"求值 $f\mapsto f(a)$"给出自然变换 $\mathrm{Hom}(A,-)\Rightarrow \mathrm{Id}$，其中恒等函子 $\mathrm{Id}$ 就是被表示者，泛元素就是 $a$。

## 一、定理介绍

> **前置依赖**：Yoneda引理、极限与余极限的表示定理、伴随函子保持极限、伴随函子定理

对范畴 $\mathcal C$ 中的对象 $A$，共变 Hom 函子 $\mathrm{Hom}_\mathcal C(A,-):\mathcal C\to\mathbf{Set}$ 把 $X$ 送到态射集 $\mathrm{Hom}_\mathcal C(A,X)$；反变 Hom 函子 $\mathrm{Hom}_\mathcal C(-,A):\mathcal C^{\mathrm{op}}\to\mathbf{Set}$ 把 $X$ 送到 $\mathrm{Hom}_\mathcal C(X,A)$。这两族函子是范畴论中最基本的研究对象：一切"可表"概念都从它们出发。

本条目给出三条相互关联的结论：(1) Hom 函子保持（余）极限；(2) **表示定理**——集合值函子 $F$ 可表当且仅当存在泛元素，且表示对象唯一；(3) 极限自身可由 Hom 函子表示，即 $\mathrm{Hom}(X,\lim D)\cong\lim\mathrm{Hom}(X,D(-))$。三者联用，是伴随函子理论、单子理论与可表性论证的技术核心。

## 二、原理思路

1. **Hom 是函子**：态射 $f:X\to Y$ 通过"左复合 $g\mapsto f\circ g$"（共变）或"右复合 $g\mapsto g\circ f$"（反变）诱导映射。
2. **保极限**：一个锥在 $\mathcal C$ 中是极限锥，当且仅当对每个 $X$，经 $\mathrm{Hom}(X,-)$ 作用后在 $\mathbf{Set}$ 中仍是极限锥。极限的普遍性（存在且唯一的填充态射）恰好翻译成 $\mathrm{Hom}(X,L)\cong\lim\mathrm{Hom}(X,D(-))$。
3. **表示定理**：由 Yoneda 引理，自然变换 $\mathrm{Hom}(A,-)\Rightarrow F$ 与元素 $F(A)$ 一一对应；该自然变换逐点双射（即表示）等价于对应元素是"泛元素"。
4. **唯一性**：由 Yoneda 嵌入满忠实，表示对象在同构下唯一。

## 三、定理的严格表述

设 $\mathcal C$ 为局部小范畴，$A,X\in\mathcal C$。

**（Hom 函子）** 对应 $X\mapsto\mathrm{Hom}_\mathcal C(A,X)$ 与 $X\mapsto\mathrm{Hom}_\mathcal C(X,A)$ 分别给出函子

$$
\mathrm{Hom}_\mathcal C(A,-):\mathcal C\to\mathbf{Set},\qquad
\mathrm{Hom}_\mathcal C(-,A):\mathcal C^{\mathrm{op}}\to\mathbf{Set}.
$$

**（Hom 保极限）** 对任意小图表 $D:\mathcal J\to\mathcal C$，若 $\lim D$ 存在，则 $\mathrm{Hom}_\mathcal C(X,-)$ 保持该极限：

$$
\mathrm{Hom}_\mathcal C\big(X,\lim D\big)\cong\lim_{j\in\mathcal J}\mathrm{Hom}_\mathcal C\big(X,D(j)\big),
$$

且该同构在 $X$ 中自然。对偶地，$\mathrm{Hom}_\mathcal C(-,X)$ 把余极限化为极限：$\mathrm{Hom}_\mathcal C(\mathrm{colim}\,D,X)\cong\lim\mathrm{Hom}_\mathcal C(D(-),X)$。

**（表示定理）** 函子 $F:\mathcal C\to\mathbf{Set}$ **可表**，若存在 $A\in\mathcal C$ 与自然同构 $\varphi:\mathrm{Hom}_\mathcal C(A,-)\xrightarrow{\ \sim\ }F$。则以下等价：

(i) $F$ 可表；

(ii) 存在**泛元素**：某个 $a\in F(A)$，使得对每个 $B\in\mathcal C$ 与每个 $b\in F(B)$，存在唯一态射 $f:A\to B$ 使 $F(f)(a)=b$；

(iii) $\mathrm{Nat}(\mathrm{Hom}_\mathcal C(A,-),F)$ 中存在逐点双射的自然变换。

此时把 $A$（及 $a$）称为 $F$ 的**表示对象**（与泛元素）；且表示对象在 $\mathcal C$ 的同构意义下唯一。

## 四、证明过程

**步骤 1：Hom 是函子**

固定 $A$。对态射 $f:X\to Y$ 定义 $\mathrm{Hom}(A,f):\mathrm{Hom}(A,X)\to\mathrm{Hom}(A,Y)$，$g\mapsto f\circ g$。由结合律 $\mathrm{Hom}(A,g\circ f)=\mathrm{Hom}(A,g)\circ\mathrm{Hom}(A,f)$，且 $\mathrm{Hom}(A,\mathrm{id}_X)=\mathrm{id}_{\mathrm{Hom}(A,X)}$，故 $\mathrm{Hom}(A,-)$ 是函子。反变的 $\mathrm{Hom}(-,A)$ 由 $f\mapsto(f\circ-)$ 定义，复合方向相反，故是 $\mathcal C^{\mathrm{op}}$ 上的函子。$\square$

**步骤 2：Hom 保持极限**

设 $D:\mathcal J\to\mathcal C$ 有极限锥 $(L,\ (p_j:L\to D(j))_{j})$，即对任意锥 $(X,\ (u_j:X\to D(j))_j)$ 存在唯一态射 $u:X\to L$ 使 $p_j\circ u=u_j$ 对一切 $j$。

用 $\mathrm{Hom}(X,-)$ 作用后，$(u_j)$ 变成 $\mathbf{Set}$ 中相容族 $(u_j\in\mathrm{Hom}(X,D(j)))_j$（相容性即 $D(\alpha)\circ u_j=u_k$），而 $\mathrm{Hom}(X,p_j):\mathrm{Hom}(X,L)\to\mathrm{Hom}(X,D(j))$ 使 $u\mapsto p_j\circ u$。极限的普遍性说：对每个相容族 $(u_j)$ 存在唯一 $u\in\mathrm{Hom}(X,L)$ 满足 $\mathrm{Hom}(X,p_j)(u)=u_j$。这恰是 $\mathbf{Set}$ 中"$\mathrm{Hom}(X,L)$ 是图表 $\mathrm{Hom}(X,D(-))$ 的极限"的定义，故

$$
\mathrm{Hom}_\mathcal C(X,L)\cong\lim_j\mathrm{Hom}_\mathcal C(X,D(j)).
$$

同构由 $u\mapsto(\mathrm{Hom}(X,p_j)(u))_j$ 给出，且在 $X$ 中自然。取 $L=\lim D$ 即得结论。对偶地把 $\mathcal C$、$\mathcal C^{\mathrm{op}}$ 互换，得 $\mathrm{Hom}(- ,X)$ 把余极限化为极限。$\square$

**步骤 3：表示定理（由 Yoneda 引理）**

由 Yoneda 引理，映射

$$
\Phi:\mathrm{Nat}\big(\mathrm{Hom}_\mathcal C(A,-),F\big)\ \longrightarrow\ F(A),\qquad \eta\mapsto\eta_A(\mathrm{id}_A)
$$

是双射，其逆为 $\Psi(a)_B(f)=F(f)(a)$（$a\in F(A)$，$f:A\to B$）。

先证 (i)$\Rightarrow$(iii)$\Rightarrow$(ii)。设 $\varphi:\mathrm{Hom}(A,-)\xrightarrow{\sim}F$，令 $a=\Phi(\varphi)=\varphi_A(\mathrm{id}_A)$，则 $\varphi=\Psi(a)$。因 $\varphi_B$ 是双射，对每个 $b\in F(B)$ 存在唯一 $f:A\to B$ 使

$$
b=\varphi_B(f)=\Psi(a)_B(f)=F(f)(a),
$$

这正是 (ii) 中泛元素 $a$ 的性质。

再证 (ii)$\Rightarrow$(i)。设 $a\in F(A)$ 满足泛元素条件，令 $\varphi=\Psi(a)$。对每个 $B$，$\varphi_B(f)=F(f)(a)$；由泛元素条件（对给定的 $b=F(f)(a)$）映射 $f\mapsto F(f)(a)$ 是单射（唯一性），又是满射（存在性），故 $\varphi_B$ 是双射。因 $\varphi$ 是自然变换，逐点双射即自然同构，$F$ 可表。三条等价。$\square$

**步骤 4：表示对象的唯一性**

设 $F$ 分别被 $A$ 与 $A'$ 表示，则 $\mathrm{Hom}(A,-)\cong F\cong\mathrm{Hom}(A',-)$。由 Yoneda 嵌入 $Y:\mathcal C\to\mathbf{Set}^{\mathcal C^{\mathrm{op}}}$（$Y(A)=\mathrm{Hom}(- ,A)$）满忠实，共变形式亦可改为 $\mathrm{Hom}(A,-)\cong\mathrm{Hom}(A',-)$ 等价于 $Y A'\cong Y A$；满忠实性给出 $A\cong A'$。故表示对象在同构意义下唯一。$\square$

**步骤 5：与极限表示、伴随的关系**

步骤 2 的不等式即"极限由 Hom 函子表示"，与极限与余极限的表示定理中"$\lim D$ 通过其 Hom 函子被刻画"的表述一致。另一方面，在带积的范畴中 $\mathrm{Hom}(A,-)$ 是函子 $-\times A$ 的右伴随（tensor-hom 伴随），故由伴随函子保持极限立即推出它保极限，印证步骤 2；反过来，伴随函子定理用"保极限 $+$ 溶液集条件"从保持性构造左伴随，说明"可表"正是伴随性的具体形态。$\blacksquare$

## 五、应用与意义

**在范畴论中的作用**：

1. **可表性与普适构造**：自由群、张量积、完备化、极限与余极限等一切普适构造都等价于某函子的可表性，表示定理提供了统一的判别与唯一性依据。
2. **伴随函子的计算**：$\mathrm{Hom}(F A,B)\cong\mathrm{Hom}(A,G B)$ 型同构是伴随函子的定义式，其存在性检验与自然性验证都归结为 Hom 函子的函子性与保极限性。
3. **代数几何与表示论**：可表函子给出模空间与概形的函子式定义；Yoneda 视角下的 Hom 函子是层与表示函子的原型。

**理论意义**：表示定理把"抽象函子"还原为"与一个对象的所有态射"，这正是 Yoneda 原理的几何化：对象由它发出的箭头决定。Hom 函子保持极限说明"取态射集"是连续操作，使范畴论中的极限计算可在 $\mathbf{Set}$ 中逐点进行，为一切"逐点验证"式的论证提供合法性。
