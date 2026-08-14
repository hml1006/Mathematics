# HOMFLY多项式

## 一、定理介绍
HOMFLY 多项式是 Jones 多项式的双参数推广，由 Hoste、Ocneanu、Millett、Freyd、Lickorish 与 Yetter 在 1985 年左右独立发现。通过参数 specialization 后可得到 Jones、Alexander–Conway 等多项式。

## 二、原理思路
与 Jones 多项式类似，HOMFLY 多项式通过辫群到 Hecke 代数的表示以及两个自由参数的 Ocneanu 型迹来构造；这两个参数分别控制拆接关系中 $L_+$ 与 $L_-$ 的系数。

## 三、定理的严格表述
设 $L$ 为定向链环。存在唯一 Laurent 多项式
$$
P_L(\ell,m)\in\mathbb{Z}[\ell^{\pm1},m^{\pm1}]
$$
称为 $L$ 的 HOMFLY 多项式，满足：
1. 规范化：$P_{\bigcirc}(\ell,m)=1$；
2. 拆接关系：
   $$
   \ell P_{L_+}(\ell,m)+\ell^{-1}P_{L_-}(\ell,m)+mP_{L_0}(\ell,m)=0;
   $$
3. 同痕不变性：若 $L\simeq L'$，则 $P_L=P_{L'}$。

在变量替换 $a=\ell^{-1}$、$z=-m/\ell$ 下，该关系也常写为
$$
a^{-1}P_{L_+}-aP_{L_-}=zP_{L_0}.
$$

## 四、证明过程
1. **Hecke 代数与双参数迹**：考虑 Hecke 代数 $H_n(\ell,m)$，其生成元 $g_i$ 满足辫关系及二次关系
   $$
   (g_i-\ell)(g_i+\ell^{-1})=0\quad\text{或等价地}\quad g_i^2+m g_i=1.
   $$
   构造线性迹 $\operatorname{tr}$ 满足循环性与 Markov 条件
   $$
   \operatorname{tr}(wg_n)=z\operatorname{tr}(w)
   $$
   对 $w\in H_n$ 成立。
2. **Markov 参数确定**：要求迹在 Markov I 型（共轭）与 II 型（稳定化）下不变。共轭不变由循环性保证；稳定化给出参数约束，解得
   $$
z=-\frac{\ell-\ell^{-1}}{m}.
   $$
3. **闭辫公式**：对 $\beta\in B_n$，定义
   $$
   P_{\widehat{\beta}}(\ell,m)=\left(\frac{\ell-\ell^{-1}}{-m}\right)^{n-1}\ell^{-e(\beta)}\operatorname{tr}\bigl(\rho(\beta)\bigr).
   $$
   由 Markov 定理，此式只依赖于闭辫的同痕类。
4. **唯一性**：拆接关系允许对交叉数进行归纳；结合规范化条件，可唯一确定任意链环图的 $P_L$。

## 五、应用与意义
HOMFLY 多项式统一了 Jones、Alexander–Conway 与 $sl_N$ 量子不变量，是纽结分类与表格编制的重要工具，并在弦论、拓扑弦以及卫星纽结的研究中具有深刻应用。
