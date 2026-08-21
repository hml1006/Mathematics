# 模糊控制的稳定性（Lyapunov方法）

> **一句话大白话**：模糊控制器的稳定性也能用"找 Lyapunov 函数"这套经典办法担保：只要找到一个沿系统轨迹单调下降的"能量"函数，模糊闭环系统就不会发散、能稳定到目标点。
>
> **小例子**：对一个用模糊规则 (Takagi-Sugeno) 描述的非线性系统，若能找到共同正定矩阵 $P$ 满足每条规则的 LMIs，则 $V(x)=x'Px$ 沿轨迹下降，闭环稳定——把稳定性证明化为可求解的线性矩阵不等式（LMI）。

## 一、定理介绍

模糊控制的稳定性（Lyapunov 方法）把 T-S 模糊系统的稳定性分析化为 LMI 求解。T-S 模糊模型把非线性系统用"IF-THEN 规则 + 局部线性模型"描述：
$$
\text{Rule } i:\ \text{If }\theta_1(t)\text{ is }M_{i1}\text{ and }\dots\ \text{Then }\dot x=A_ix+B_iu.
$$
闭环取全局为加权系统 $\dot x=\sum_i\mu_i(\theta)(A_ix+B_iu)$。若存在共同正定 $P$ 使 $A_i'P+PA_i<0$（开环）或闭环 LMIs 成立，则系统 Lyapunov 稳定。

## 二、原理思路

体系化的直观是"逐条规则局部稳定 + 整体共享 Lyapunov 函数"。对并接局部线性模型，取同一的二次 Lyapunov 函数 $V(x)=x'Px$，沿闭环轨迹
$$
\dot V=\sum_i\mu_i(\theta)\,x'\big(A_i'P+PA_i\big)x.
$$
若每条规则的二次型对应矩阵 $A_i'P+PA_i\prec0$（或含反馈设计的 LMI 变体），因 $\mu_i\ge0$、$\sum_i\mu_i=1$，$\dot V<0$，从而一致渐近稳定。这样把连续非线性稳定性问题离散成有限个 LMI 的可行性问题。

## 三、定理的严格表述

设 T-S 模糊闭环系统 $\dot x=\sum_{i=1}^r\mu_i(\theta)(A_i-B_iK_i)x$（局部反馈 $u=-K_ix$），其中权重 $\mu_i\ge0$ 且 $\sum_i\mu_i=1$。若存在 $P=P'>0$ 使
$$
(A_i-B_iK_i)'P+P(A_i-B_iK_i)<0\qquad\forall i=1,\dots,r,
$$
则系统在原点一致渐近稳定；Lyapunov 函数为 $V(x)=x'Px$。实际 LMIs 中取 $X=P^{-1}$、$M_i=K_iX$ 化为（若跨项不需 Riemann 型）$XA_i'+A_iX-B_iM_i-M_i'B_i'<0$。

## 四、证明过程

**步骤1：写出 T-S 加权系统。** 将规则后件线性模型按隶属度权重（叠加 $\mu_i$）求加权和，得 $\dot x=\sum_i\mu_i(\theta)(A_i-B_iK_i)x$。

**步骤2：取候选 Lyapunov 函数。** 令 $V(x)=x'Px$，$P=P'>0$ 待定。

**步骤3：沿轨迹求导。**
$$
\dot V=2x'P\dot x=2x'P\sum_i\mu_i(A_i-B_iK_i)x=\sum_i\mu_i\,x'\big[(A_i-B_iK_i)'P+P(A_i-B_iK_i)\big]x.
$$

**步骤4：逐条 LMI 保证下降。** 若每条 $(A_i-B_iK_i)'P+P(A_i-B_iK_i)\prec0$，则对 $x\ne0$ 每项 $<0$；乘正 $\mu_i$ 相加仍 $<0$，故 $\dot V<0$。

**步骤5：得出稳定性。** $\dot V<0$、$V>0$、$V$ 径向无界，故原点一致渐近稳定（Lyapunov 定理）。

**步骤6：化为 LMI。** 左乘右乘 $X=P^{-1}$，令 $M_i=K_iX$，把每条规则化为关于 $X,M_i$ 的线性矩阵不等式，可用凸优化工具求解。

**结论（$\square$）**：存在共同 $P$ 满足各规则 LMI ⇔ 模糊闭环一致渐近稳定。

## 五、应用与意义

该方法把模糊控制的稳定性验证变成可计算的 LMI 可行性问题，是现代非线性模糊控制（T-S 模型）分析与综合的主流手段。它广泛应用于复杂非线性被控对象的稳定控制器设计、鲁棒与 $H_\infty$ 模糊控制，使模糊控制从启发式走向具备严格稳定性保证的工程方法。