# Koebe 1/4 定理

> **一句话大白话**：单叶全纯函数在一点附近"张开"的像，至少包含以该点为心、半径为正则化尺度四分之一的圆盘。
>
> **小例子**：Koebe 函数 $k(z)=\dfrac{z}{(1-z)^2}$ 在 $\mathbb{D}$ 上单叶，$k(0)=0$、$k'(0)=1$，其像为 $\mathbb{C}\setminus(-\infty,-1/4]$；它恰好不含半径大于 $1/4$ 的以原点为心的圆盘，说明常数 $1/4$ 不能再改进。

## 介绍

Koebe 1/4 定理是单叶函数论中最著名的一条定量结论：单叶（univalent）函数在一点的局部像不会"太瘦"，它一定张开出一个半径与 $|f'(0)|$ 成正比的圆盘。这与多值/非单叶函数的病态行为（如 $e^z$ 或 $z^n$ 的局部像可以很窄）形成鲜明对比。

定理的价值在于"覆盖信息"：它把导数这一局部量转化为像的全局覆盖范围，因此成为 Bloch 定理、双曲度量估计、Riemann 映射的边界行为分析的基本工具。它的证明通常走 Grönwall 面积定理这条路：先证明外域单叶函数的 Laurent 系数满足平方和估计，再把它转成系数不等式，最后拼出 $1/4$。

## 分析

**前置依赖**：全纯函数、单叶（一一）函数、Laurent 展开、Möbius 变换的单射性、第二类曲线积分公式、最大模原理。

**定理内容**：设 $f$ 在单位圆盘 $\mathbb{D}$ 上全纯且单叶。则
$$f(\mathbb{D})\ \supset\ B\Big(f(0),\frac{|f'(0)|}{4}\Big),$$
即以 $f(0)$ 为心、半径 $|f'(0)|/4$ 的圆盘完全含于像中。

**证明路线**（四步）：

1. **Grönwall 面积定理**：若 $g(z)=z+b_0+\sum_{n\ge1}b_nz^{-n}$ 在 $|z|>1$ 上单叶，则 $\sum_{n\ge1}n|b_n|^2\le1$；
2. **系数推论**：若 $f(z)=z+a_2z^2+\cdots$ 在 $\mathbb{D}$ 上单叶，则 $|a_2|\le2$；
3. **$w$-变换**：若 $w\notin g(\mathbb{D})$，则 $h(z)=\dfrac{wg(z)}{w-g(z)}$ 也单叶、$h(0)=0$、$h'(0)=1$，且其二次系数为 $a_2+1/w$；
4. **拼装**：对 $g$ 与 $h$ 各用一次 $|a_2|\le2$，由三角不等式得 $1/|w|\le4$。

## 思考过程

面积定理的思想是"以面积换系数信息"：外域的单叶映射 $g$ 把 $|z|=r$ 映成一条简单闭曲线，曲线所围面积总非负；而用曲线积分把面积算成 Laurent 系数的表达式，就得到 $\pi(r^2-\sum n|b_n|^2r^{-2n})\ge0$，令 $r\to1$ 得到平方和估计。

要从"外域形式"得到"圆盘形式"的 $|a_2|\le2$，标准技巧是**平方根技巧**：$f$ 在 $0$ 有单零点，故 $1/f(1/z^2)$ 在 $|z|>1$ 有全纯平方根（该区域单连通），这个平方根本身单叶，且其 Laurent 展开的一次负幂系数恰为 $-a_2/2$，代入面积定理即得。

最后一步是"两函数同时约束"。若 $w$ 不在像中，Möbius 变换 $u\mapsto wu/(w-u)$ 把外域映成"删去 $w$ 的世界"，把 $g$ 变成另一个单叶正规化函数 $h$，它的二次系数是 $a_2+1/w$。两个二次系数都被 $|a_2|\le2$ 卡住，而它们的差恰为 $1/w$，于是 $1/|w|\le4$。

## 证明过程

**步骤 0：归一化。**

由单叶性 $f'\not\equiv0$，特别 $f'(0)\ne0$（若 $f'(0)=0$，则 $f(z)-f(0)$ 在 $0$ 有重零点，$f$ 在 $0$ 附近不单射）。定义
$$g(z)=\frac{f(z)-f(0)}{f'(0)}.$$
则 $g$ 在 $\mathbb{D}$ 上单叶，$g(0)=0$、$g'(0)=1$，且
$$f(\mathbb{D})=f(0)+f'(0)\,g(\mathbb{D}).$$
故只需证明：**若 $g$ 在 $\mathbb{D}$ 上单叶、$g(0)=0$、$g'(0)=1$，则 $B(0,1/4)\subset g(\mathbb{D})$**。

**步骤 1：Grönwall 面积定理。**

**引理**：设 $G(z)=z+b_0+\sum_{n\ge1}b_nz^{-n}$ 在 $|z|>1$ 上单叶。则
$$\sum_{n\ge1}n|b_n|^2\le1.$$

**证明**：固定 $r>1$。因 $G$ 单叶且 $G'(z)=1-\sum_{n\ge1}nb_nz^{-n-1}\ne0$ 于 $|z|>1$，像曲线 $\gamma_r=G(\{|z|=r\})$ 是简单闭曲线，设其所围面积为 $A_r\ge0$。由 Green 公式（复形式）
$$A_r=\frac{1}{2i}\oint_{|z|=r}\overline{G(z)}\,dG(z)=\frac{1}{2i}\oint_{|z|=r}\overline{G(z)}\,G'(z)\,dz.$$
在 $|z|=r$ 上 $\bar z=r^2/z$，故
$$\overline{G(z)}=\bar z+\bar b_0+\sum_{n\ge1}\bar b_n\bar z^{-n}=\frac{r^2}{z}+\bar b_0+\sum_{n\ge1}\frac{\bar b_n z^n}{r^{2n}},$$
$$G'(z)=1-\sum_{m\ge1}mb_mz^{-m-1}.$$
乘积 $\overline{G}G'$ 中产生 $z^{-1}$ 的项：(i) $\frac{r^2}{z}\cdot1$ 给出 $r^2$；(ii) $\frac{\bar b_nz^n}{r^{2n}}\cdot(-nb_nz^{-n-1})$ 给出 $-\frac{n|b_n|^2}{r^{2n}}$（当 $n=m$）。故
$$\operatorname{Res}_{z=0}\big(\overline{G}G'\big)=r^2-\sum_{n\ge1}\frac{n|b_n|^2}{r^{2n}}.$$
由留数定理
$$A_r=\pi\Big(r^2-\sum_{n\ge1}\frac{n|b_n|^2}{r^{2n}}\Big)\ge0.$$
曲线族随 $r$ 单调外扩，$A_r$ 关于 $r$ 单调不增，故其极限（即 $r\to1^+$ 的极限）也 $\ge0$。令 $r\to1^+$ 得
$$\pi\Big(1-\sum_{n\ge1}n|b_n|^2\Big)\ge0,\qquad\text{即}\qquad\sum_{n\ge1}n|b_n|^2\le1.$$

**步骤 2：系数推论 $|a_2|\le2$。**

设 $f(z)=z+a_2z^2+a_3z^3+\cdots$ 在 $\mathbb{D}$ 上单叶。在 $|z|>1$ 上定义
$$\Phi(z)=\sqrt{\frac{1}{f(1/z^2)}}.$$
良定义性：$|z|>1$ 时 $u=1/z^2$ 满足 $|u|<1$；由 $f$ 单叶与 $f(0)=0$ 知 $f(u)\ne0$（$u\ne0$），故 $1/f(u)$ 全纯且处处非零；域 $|z|>1$ 单连通，故全纯平方根 $\Phi$ 存在。

**展开**：由 $f(u)=u(1+a_2u+O(u^2))$，
$$\frac{1}{f(1/z^2)}=z^2\Big(1-\frac{a_2}{z^2}+O(z^{-4})\Big)=z^2-a_2+O(z^{-2}),$$
$$\Phi(z)=z\Big(1-\frac{a_2}{2z^2}+O(z^{-4})\Big)=z-\frac{a_2}{2z}+O(z^{-3}).$$
即 $\Phi(z)=z+b_0+\sum_{n\ge1}b_nz^{-n}$，其中 $b_1=-a_2/2$。

**单叶性**：若 $\Phi(z_1)=\Phi(z_2)$，平方得 $f(1/z_1^2)=f(1/z_2^2)$，由 $f$ 单射得 $z_2=\pm z_1$。又 $\Phi(-z)=\sqrt{1/f(1/z^2)}=\Phi(z)$，而由展开 $\Phi(z)=z+O(1/z)$ 知 $\Phi$ 是奇函数：$\Phi(-z)=-\Phi(z)$。于是 $\Phi(z_2)=\Phi(-z_1)=-\Phi(z_1)$；结合 $\Phi(z_1)=\Phi(z_2)$ 得 $\Phi(z_1)=0$，但 $1/f(1/z^2)\ne0$ 故 $\Phi\ne0$。故 $z_2=z_1$，$\Phi$ 单叶。

**代入面积定理**：$1\cdot|b_1|^2\le\sum n|b_n|^2\le1$，即 $|a_2|^2/4\le1$，故
$$|a_2|\le2. \tag{$\star$}$$

**步骤 3：$w$-变换的单叶化。**

设 $g(z)=z+a_2z^2+\cdots$ 在 $\mathbb{D}$ 上单叶、$g(0)=0$、$g'(0)=1$，且 $w\notin g(\mathbb{D})$，$w\ne0$。令
$$h(z)=\frac{w\,g(z)}{w-g(z)}\qquad(z\in\mathbb{D}).$$
（分母不为零，因 $g(z)\ne w$。）

**全纯性与展开**：$h$ 在 $\mathbb{D}$ 上全纯。由 $g(z)=z+a_2z^2+O(z^3)$，
$$h(z)=\frac{w\big(z+a_2z^2+\cdots\big)}{w-\big(z+a_2z^2+\cdots\big)}=\big(z+a_2z^2+\cdots\big)\Big(1+\frac{z}{w}+O(z^2)\Big)=z+\Big(a_2+\frac1w\Big)z^2+O(z^3).$$
故 $h(0)=0$，$h'(0)=1$，二次系数为 $a_2+\frac1w$。

**单叶性**：Möbius 变换 $\phi(u)=\frac{wu}{w-u}$ 在 $\mathbb{C}\setminus\{w\}$ 上单射（它是 Möbius 变换，在其定义域上双射到 $\mathbb{C}\setminus\{w\}$）。由 $g(\mathbb{D})\subset\mathbb{C}\setminus\{w\}$，得 $h=\phi\circ g$ 在 $\mathbb{D}$ 上单射。

**步骤 4：拼装得 $|w|\ge1/4$。**

对 $g$ 用 $(\star)$：$|a_2|\le2$。对 $h$ 用 $(\star)$（$h$ 满足步骤 2 的全部假设）：
$$\Big|a_2+\frac1w\Big|\le2.$$
于是
$$\frac{1}{|w|}=\Big|\Big(a_2+\frac1w\Big)-a_2\Big|\le\Big|a_2+\frac1w\Big|+|a_2|\le2+2=4,$$
即 $|w|\ge1/4$。因此凡是满足 $0<|w|<1/4$ 的 $w$ 必属于 $g(\mathbb{D})$，即
$$B(0,1/4)\subset g(\mathbb{D}).$$

**步骤 5：回到一般情形。**

由步骤 0，$f(\mathbb{D})=f(0)+f'(0)g(\mathbb{D})\supset f(0)+f'(0)B(0,1/4)=B\big(f(0),\frac{|f'(0)|}{4}\big)$，定理得证。

**步骤 6：尖锐性。**

考虑 Koebe 函数 $k(z)=\dfrac{z}{(1-z)^2}$。它在 $\mathbb{D}$ 上单叶，$k(0)=0$、$k'(0)=1$，且可以验证
$$k(\mathbb{D})=\mathbb{C}\setminus\Big(-\infty,-\tfrac14\Big].$$
（$k$ 是"把圆盘映到 slit 平面"的极值函数：$k$ 把 $\mathbb{D}$ 共形映到沿负实轴从 $-1/4$ 到 $-\infty$ 切开的平面。）该像不含任何点 $w<-1/4$，故不含以 $0$ 为心、半径 $>1/4$ 的圆盘。因此定理中的常数 $1/4$ 是最佳的，无法用更大的常数替换。等号情形（$f(\mathbb{D})$ 恰不含某点 $|w|=1/4$）只在 $f$ 为 Koebe 函数的旋转/平移缩放时发生。

## 课堂问答

**老师**：Koebe 1/4 定理的 $1/4$ 到底是怎么"算"出来的？

**学生**：结论：$f$ 在 $\mathbb D$ 上单叶则 $f(\mathbb D)\supset B\big(f(0),\frac{|f'(0)|}{4}\big)$。归一化到 $g(0)=0$、$g'(0)=1$ 后，走 Grönwall 面积定理：外域单叶的 $G(z)=z+b_0+\sum_{n\ge1}b_nz^{-n}$ 满足 $\sum n|b_n|^2\le1$。

**老师（追问）**：从这个平方和估计怎样一路走到 $|w|\ge1/4$？

**学生**：先用平方根技巧把它转成系数不等式 $|a_2|\le2$（对 $g(z)=z+a_2z^2+\cdots$）。再取 $w\notin g(\mathbb D)$，令 Möbius 变换 $h(z)=\frac{wg(z)}{w-g(z)}$，则 $h$ 单叶、$h(0)=0$、$h'(0)=1$，其二次系数为 $a_2+1/w$。对 $h$ 再用一次 $|a_2|\le2$，得
$$\frac{1}{|w|}=\Big|\Big(a_2+\frac1w\Big)-a_2\Big|\le\Big|a_2+\frac1w\Big|+|a_2|\le4,$$
故 $|w|\ge1/4$。

**老师（拓展）**：常数还能再改进吗？

**学生**：不能，$1/4$ 是尖锐的。Koebe 函数 $k(z)=\frac{z}{(1-z)^2}$ 在 $\mathbb D$ 上单叶，$k(0)=0$、$k'(0)=1$，其像恰为 $\mathbb C\setminus(-\infty,-1/4]$，不含半径大于 $1/4$ 的以原点为心的圆盘，故无法用更大的常数替换。

## 相关条目

- [Bloch定理](./Bloch定理.md)：用 Koebe 1/4 定理把单叶子圆盘的覆盖信息拼成 Bloch 常数的正下界。
- [Schwarz引理](./Schwarz引理.md)：同为圆盘上单叶/全纯函数的定量估计，二者常配合使用。
- [Montel定理](./Montel定理.md)：单叶函数族的正规性与极值函数的存在性论证依赖正规族理论。
