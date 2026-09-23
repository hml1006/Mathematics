# McKean-Singer公式

> **一句话大白话**：把"热的扩散"（热核 $e^{-tD^2}$）按正负分次带符号求和，得到的数竟完全不随扩散时间 $t$ 变化——它只能由"零能量"部分（Dirac 算子的核，即零模）贡献，因此就等于指标。
>
> **小例子**：设 $D$ 是奇的自伴算子，写成分块形式 $D=\begin{pmatrix}0&D_-\\ D_+&0\end{pmatrix}$。对 $\lambda>0$，$D$ 把 $H_+$ 中的 $\lambda$-特征向量与 $H_-$ 中的 $\lambda$-特征向量一一配对，热核的贡献相消；于是只剩下 $\lambda=0$，超迹 $=\dim\ker D_+-\dim\ker D_-=\mathrm{Ind}(D_+)$。

## 一、定理介绍

> Hilbert 空间与自伴算子、谱定理紧自伴算子、$\mathbb{Z}_2$-分次与超迹、Fredholm 算子与解析指标、热核

McKean-Singer 公式由 H. McKean 与 I. Singer 于 1967 年提出，是 Atiyah-Singer 指标定理"热方程证明"的起点。它指出：对分次 Hilbert 空间上的奇自伴 Dirac 算子 $D$，热核的超迹 $\mathrm{Str}(e^{-tD^2})$ 与 $t>0$ 无关，且恒等于 $D$ 的解析指标。

这一公式把"指标"这一整体（拓扑）不变量，转化为可以用局部热核渐近展开逐点计算的对象：一方面 $t$ 可以趋于 $0$，另一方面 $t$ 可以趋于 $\infty$。前者给出局部指标公式（Atiyah-Singer 的证明路线），后者自动只剩下零模的信息。它也是非交换几何中"谱三元组"与谱作用原理的技术基石。

公式的证明只用到谱定理与一条简单的配对观察，是"深刻结论来自简单结构"的范例。它的威力在于把指标写成热核对角值的超迹之积分：$\mathrm{Str}(e^{-tD^2})=\int_M\mathrm{str}\,k_t(x,x)\,dx$，从而可由 Seeley-deWitt 系数（局部几何量）计算。

## 二、原理思路

核心想法只有一条：$D$ 在"非零能量"部分不改变正负谱的"数量差"。

1. $D^2$ 是偶算子且在分次子空间上封闭，因此 $e^{-tD^2}$ 保持每个分次分量，可分块写为 $\mathrm{diag}(e^{-tD_-D_+},e^{-tD_+D_-})$。
2. 对 $\lambda>0$，$D$ 给出线性同构 $\ker(D^2-\lambda)\cap H_+\to\ker(D^2-\lambda)\cap H_-$，其逆为 $\lambda^{-1}D$；因此两个分次中非零特征值的重数完全一致，超迹相消。
3. 只有 $\ker D^2=\ker D$ 幸存，故超迹等于 $\dim\ker D_+-\dim\ker D_-$。

## 三、定理的严格表述

**定理（McKean-Singer 公式）**：设 $\mathcal{H}=\mathcal{H}_+\oplus\mathcal{H}_-$ 是 $\mathbb{Z}_2$-分次的可分 Hilbert 空间，$D$ 是（可能无界的）自伴算子，满足
$$D\,\mathcal{H}_\pm\subseteq\mathcal{H}_\mp,\qquad D^2\ \text{具有紧预解式（故谱离散、特征空间有限维）}.$$
记 $D_+:\mathcal{H}_+\to\mathcal{H}_-$ 为 $D$ 的正部分，$D_-=D_+^{*}$。则：

(1) 对一切 $t>0$，$e^{-tD^2}$ 是迹类算子，且其超迹与 $t$ 无关：
$$\mathrm{Str}\big(e^{-tD^2}\big):=\mathrm{tr}\big(e^{-tD^2}\big|_{\mathcal{H}_+}\big)-\mathrm{tr}\big(e^{-tD^2}\big|_{\mathcal{H}_-}\big)=\text{常数};$$

(2) 若 $D_+$ 是 Fredholm 算子，则该常数为解析指标：
$$\mathrm{Str}\big(e^{-tD^2}\big)=\dim\ker D_+-\dim\ker D_-=\mathrm{Ind}(D_+).$$

**推论（局部指标公式的起点）**：若 $D$ 是紧流形上的 Dirac 型算子，$e^{-tD^2}$ 有光滑积分核 $k_t(x,y)$，则
$$\mathrm{Ind}(D_+)=\int_M\mathrm{str}\,k_t(x,x)\,dx\qquad(\forall t>0),$$
令 $t\to0^+$ 并用热核渐近展开，即可把指标写成局部曲率量的积分。

## 四、证明过程

**步骤 1：谱分解**

$D^2$ 非负、自伴、偶，且具紧预解式。由紧自伴算子的谱定理，存在完备正交特征基 $\{\psi_j\}$ 使 $D^2\psi_j=\lambda_j\psi_j$，其中 $0\le\lambda_j\to\infty$，且每个特征空间 $\ker(D^2-\lambda)$ 有限维。由于 $D^2$ 是偶算子，$\ker(D^2-\lambda)$ 关于分次稳定，故 $\{\psi_j\}$ 可取为分次齐次的。

**步骤 2：非零谱上的配对同构**

固定 $\lambda>0$，记 $E_\lambda=\ker(D^2-\lambda)$，$E_\lambda^\pm=E_\lambda\cap\mathcal{H}_\pm$。断言 $D_+\big|_{E_\lambda^+}:E_\lambda^+\to E_\lambda^-$ 是线性同构。对 $\psi\in E_\lambda^+$ 有
$$D^2(D\psi)=D(D^2\psi)=\lambda\,D\psi,\qquad \|D\psi\|^2=\langle D^2\psi,\psi\rangle=\lambda\|\psi\|^2,$$
故 $D\psi\in E_\lambda^-$ 且 $\psi\ne0\Rightarrow D\psi\ne0$，即 $D_+\big|_{E_\lambda^+}$ 单射。反之若 $\phi\in E_\lambda^-$，取 $\psi=\lambda^{-1}D_-\phi\in E_\lambda^+$，则 $D_+\psi=\lambda^{-1}D^2\phi=\phi$，故为满射。于是
$$\dim E_\lambda^+=\dim E_\lambda^-.$$

**步骤 3：超迹的相消**

$e^{-tD^2}$ 在 $E_\lambda$ 上等于 $e^{-t\lambda}\mathrm{id}$，故它对超迹的贡献为
$$e^{-t\lambda}\big(\dim E_\lambda^+-\dim E_\lambda^-\big)=0\qquad(\lambda>0).$$
对 $\lambda=0$：$\ker D^2=\ker D=\ker D_+\oplus\ker D_-$，$e^{-tD^2}$ 在其上是恒等算子，贡献为 $\dim\ker D_+-\dim\ker D_-$。由步骤 1 的谱分解，把这些有限维特征空间的贡献沿正交分解求和（对可数直和用迹类性与单调收敛定理控制极限），得
$$\mathrm{Str}\big(e^{-tD^2}\big)=\dim\ker D_+-\dim\ker D_-$$
对一切 $t>0$ 成立。右端与 $t$ 无关，这同时证明了 (1) 与 (2)。

**步骤 4：迹类性与积分核（推论的证明）**

迹类性：$\mathrm{tr}\,e^{-tD^2}=\sum_j e^{-t\lambda_j}<\infty$（$t>0$ 且 $\lambda_j\to\infty$ 保证收敛）。当 $D$ 是紧流形上的椭圆微分算子时，热半群 $e^{-tD^2}$ 由光滑核给出：$e^{-tD^2}u(x)=\int_M k_t(x,y)u(y)\,dy$（由拟基本解构造与 Duhamel 公式的标准论证），并且
$$\mathrm{tr}\big(e^{-tD^2}\big|_{\mathcal{H}_\pm}\big)=\int_M\mathrm{tr}\,k_t^\pm(x,x)\,dx.$$
两式相减即得 $\mathrm{Ind}(D_+)=\int_M\mathrm{str}\,k_t(x,x)\,dx$，且与 $t$ 无关。

## 五、应用与意义

1. **指标定理的热核证明**：Atiyah-Singer 指标定理的标准证明取 $t\to0^+$，用 Seeley-deWitt 展开把 $\int\mathrm{str}\,k_t(x,x)$ 展开为局部曲率多项式，得到局部指标公式；McKean-Singer 公式保证该展开与 $t$ 无关，故任意 $t$ 都可用来计算指标。

2. **非交换几何**：在谱三元组 $(\mathcal{A},\mathcal{H},D)$ 中，$\mathrm{Str}(e^{-tD^2})$ 给出与谱作用原理、Wodzicki 留数相容的"指标迹"；Connes 指标定理的局部指标公式正是由此推出。

3. **推广**：对 $D$ 的连续族、Clifford 模与 twisted Dirac 算子，同样的配对论证给出 $\mathrm{Ind}(D\otimes E)=\int_M\mathrm{str}\,k_t^{D\otimes E}(x,x)\,dx$，这是族指标定理的出发点；公式也推广到 $D$ 为超对称生成元（Witten 指标、等变指标）的情形。
