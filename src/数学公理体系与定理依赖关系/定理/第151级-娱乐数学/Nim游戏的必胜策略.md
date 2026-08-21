# Nim游戏的必胜策略
>
> **一句话大白话**：Nim 游戏里，把各堆石子的数目做异或，异或为 0 时后手必胜、否则先手必胜，且必胜走法就是"把异或调回 0"。
>
> **小例子**：$(3,4,5)$：$3\oplus4\oplus5=2\ne0$，先手把 $3$ 变为 $3\oplus2=1$（取走 2 枚），得到 $(1,4,5)$，其异或为 0——后手落入必败。

## 一、定理介绍

Nim 游戏必胜策略定理：若干堆石子轮流取（每次从一堆取任意正整数枚、至少一枚），最后取完者胜。判定
$$
a_1\oplus a_2\oplus\cdots\oplus a_n=0\quad\Longleftrightarrow\quad\text{必败（P-局面）},
$$
其异或和 $x=a_1\oplus\cdots\oplus a_n\ne0$ 时为必胜（N-局面），胜着在于使 $x'=0$。这给出全称的、可一步验证的策略。

## 二、原理思路

思路是刻画 P/N 局面并显式给出胜着。关键两条：(1) 若 $x=0$，任何一动只改变一堆 $a_i\to a_i'$，因 $a_i=a_i$（其余异或）而 $a_i'\ne a_i$，故新异或 $x'=a_i\oplus a_i'\ne0$——必败局面的所有出招都到必胜；(2) 若 $x\ne0$，取 $x$ 最高二进制位 $k$，选该位为 1 的堆 $a_i$，令 $a_i'=a_i\oplus x<a_i$，则 $x'=0$——必胜且存在一步到必败。

## 三、定理的严格表述

设 Nim 局面 $(a_1,\dots,a_n)$，$a_i\ge0$，$x=a_1\oplus\cdots\oplus a_n$。则
1. 若 $x=0$：所有合法移动都导致 $x'\ne0$（即都到必胜局面），故 $(a_1,\dots,a_n)$ 为 P-局面（必败）。
2. 若 $x\ne0$：存在一步使 $x'=0$（取第 $i$ 堆，$a_i'=a_i\oplus x<a_i$），故为 N-局面（必胜）。
3. 最优策略：始终保持 $x=0$。

## 四、证明过程

记 $x=a_1\oplus\cdots\oplus a_n$。先证 $x=0\Rightarrow$ 全出招到 $x'\ne0$：只改第 $i$ 堆 $a_i\to a_i'<a_i$，故 $x'=(\text{其余异或})\oplus a_i'=a_i\oplus a_i'$（因其余异或 $=a_i$ 当 $x=0$）；$a_i'\ne a_i$ 推出 $a_i\oplus a_i'\ne0$。再证 $x\ne0\Rightarrow\exists$ 一步到 $x'=0$：取 $x$ 最高位 $k$，有堆 $a_i$ 第 $k$ 位为 1；设 $a_i'=a_i\oplus x$，则 $a_i'$ 第 $k$ 位为 0 而 $a_i$ 为 1，故 $a_i'<a_i$，取走 $a_i-a_i'$ 枚；新异或 $x'=(a_1\oplus\cdots\oplus a_n)\oplus x=x\oplus x=0$。对总数归纳封闭判定。

## 五、应用与意义

Nim 是组合博弈的"标准模型"，其异或策略是 Sprague–Grundy 理论的原型，被百余种取石子游戏与算法竞赛沿用；它展示"位运算 + 归纳"直取必败分类的优雅力，是博弈论入门与 XOR 应用的典范。