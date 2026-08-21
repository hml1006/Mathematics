# Loś 定理

> **一句话大白话**：在超积 $M^I/\mathcal{U}$ 里，一个含参公式 $\phi([f_1],\dots,[f_k])$ 是否为真，当且仅当"在超滤 $\mathcal{U}$ 中的几乎所有坐标 $i$ 上 $\phi(f_1(i),\dots,f_k(i))$ 在 $M$ 里为真"——超积中"多数的真"就是"整体的真"。
>
> **小例子**：$f=(1,2,3,\dots)$ 表示超实数里的"无限大元素" $[n]$。对标准实数 $r$，因为 $\{n:n>r\}$ 是余有限的（在超滤里是"几乎所有"），Loś 定理保证 $[n]>r$ 在 $^*\mathbb{R}$ 中成立——从而非标准里有比所有标准实数都大的元素。

## 一、定理介绍

Loś 定理（超幂基本定理）是超幂/超积构造的核心定理：它刻画了超积 $\prod_{i\in I}M_i/\mathcal{U}$ 中命题真假的判定方式，说明一阶公式在超积中的真值由其在"$\mathcal{U}$-大坐标集"上的真值决定。它是非标准分析构造超实数、以及模型论中构造超积的关键，也是转移原理的模型论根据。

## 二、原理思路

证明对公式复杂度作结构归纳。原子公式（等式 $f_1=f_2$、关系 $R$）的真值由超积中等价/关系的定义直接给出（$[f_1]=[f_2]\iff\{i:f_1(i)=f_2(i)\}\in\mathcal{U}$）。联结词 $\neg,\land$ 由超滤的补封闭与对有限交封闭给出。存在量词 $\exists v\phi$ 是难点：$\mathcal{U}$-大集方向用选择公理在满足的坐标上选见证 $g(i)$，反之由子集关系与滤的单调性推出。

## 三、定理的严格表述

**定理（Loś 定理，超幂基本定理）**：设 $\mathcal{U}$ 是 $I$ 上的超滤，$M$ 是结构。对超幂 $M^I/\mathcal{U}$ 中元素 $[f_1],\dots,[f_k]$ 与任意一阶公式 $\phi(v_1,\dots,v_k)$：
$$
M^I/\mathcal{U}\models\phi([f_1],\dots,[f_k])\iff\{i\in I:M\models\phi(f_1(i),\dots,f_k(i))\}\in\mathcal{U}.
$$

**推论（转移原理）**：若 $\phi$ 是闭语句（无自由变量），则 $\mathbb{R}\models\phi\iff{}^*\mathbb{R}\models\phi$。

## 四、证明过程

**证明（对公式结构归纳）**：

**步骤1（原子公式）**：对 $v_1=v_2$ 或 $R(v_1,\dots,v_k)$，由超幂中相等的定义：$[f_1]=[f_2]\iff\{i:f_1(i)=f_2(i)\}\in\mathcal{U}$；关系同理，结论直接成立。

**步骤2（联结词）**：
- 对 $\neg\phi$：$M^I/\mathcal{U}\models\neg\phi\iff\{i:M\models\phi(f(i))\}\notin\mathcal{U}\iff$ 其补 $=\{i:M\models\neg\phi\}\in\mathcal{U}$（超滤）；
- 对 $\phi\land\psi$：成立集为两成立集之交，由超滤对有限交封闭属于 $\mathcal{U}$。

**步骤3（存在量词）**：
- （$\Rightarrow$）若 $M^I/\mathcal{U}\models\exists v\phi(v,[f_1],\dots)$，取见证 $[g]$；则 $A=\{i:M\models\phi(g(i),f_1(i),\dots)\}\in\mathcal{U}$。因 $A\subseteq B=\{i:M\models\exists v\phi(v,f_1(i),\dots)\}$，由滤的单调性 $B\in\mathcal{U}$；
- （$\Leftarrow$）若 $B\in\mathcal{U}$，对 $i\in B$ 选 $g(i)$ 使 $M\models\phi(g(i),f_1(i),\dots)$，$i\notin B$ 任选。则 $M^I/\mathcal{U}\models\phi([g],[f_1],\dots)$，故 $\exists$ 成立。

**步骤4（全称量词）**：$\forall v\phi\equiv\neg\exists v\neg\phi$，由步骤2、3推出。

**步骤5（归纳完成）**：按公式复杂度归纳，Loś 定理得证；对闭语句即得转移原理。$\square$

## 五、应用与意义

Loś 定理是超幂构造合法性的核心：它保证超积的原子结构由坐标系归纳给出、一阶真值可由"几乎所有坐标"判定，从而让超积成为构造初等扩张、非标准模型（$^*\mathbb{R}$、$^*\mathbb{N}$）与饱和模型的普遍工具。它与超滤性质配合支撑转移原理，也是非标准分析与模型论交界的枢纽定理。