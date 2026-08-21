# Wigner猜测（GOE最近邻间距分布）
>
> **一句话大白话**：GOE（实对称随机矩阵）相邻特征值的间距，其分布在无穷极限由 Wigner 猜测的半圆-启发塔（surmise）给出——与泊松间距判然不同，体现特征值的"排斥"。
>
> **小例子**：GOE 的本征相邻间距 $s$（经单位平均间距归一）分布近似为 $p(s)=\frac{\pi s}{2}e^{-\pi s^2/4}$（Wigner surmise），且超可积 GOE 的实际极限分布即此（对 $s\to0$ 排斥 $p(s)\sim s$）。

## 一、定理介绍

Wigner猜测（Wigner surmise）断言：GOE 的最近邻特征值间距在适当归一（平均间距=1）后的分布 $p(s)$ 由公式给出
$$
p(s)=\frac{\pi s}{2}e^{-\pi s^2/4},
$$
其依据是 $2\times 2$ 正交约化的精确计算。对 GOE 在 $n\to\infty$ 极限，该分布确实是精确的极限（由 sine-核点过程的 EFP with $\beta=1$ 得到），且在 $s\to0$ 时线性排斥 $p(s)\sim s$ — 与泊松不同。

## 二、原理思路

用行列式/Pfaffian 点过程表达 GOE 边界间距。GOE 的特征值是 $\beta=1$ 的 Pfaffian 点过程，其 gap 概率由某核（含广义 sine 核与积分项）的 Fredholm/Pfaffian 行列式表出。对 $s\to0$ 展开与适当地改写给出 $p(s)\sim s$；对较大 $n$ 的精确可积 GOE 极限密度由该核算到实用精度，数值与 surmise 接近。

## 三、定理的严格表述

设 $\lambda_1\le\dots\le\lambda_n$ 为 $n\times n$ GOE 成比例的（soft-edge 前）特征值，定义间距间距（bulk scaling）：平均间距。
Wigner 猜测其 $n\to\infty$ 的最近邻间距密度
$$
p(s)\;\simeq\;\frac{\pi s}{2}e^{-\pi s^2/4}.
$$
严格版本：GOE 在 bulk 的 Gap 概率由 sine 核（$\beta=1$）决定，其前提下 $p'(0^{+})$ 满足排斥且上述 surmise 精确至首阶。

## 四、证明过程

方法为把 GOE 特征值框为 Pfaffian 点过程：写出相邻间距密度的 Pfaffian（gap）表示，用带核（含 $\int_0^s$ 的 sine 核）求值；对 $s$ 考虑微元导数得到 $p(s)$ 的表达式，并展示 $p(s)\sim s$（排斥）与大 $s$ 的指数衰减。数值/常队确认 surmise 为良好近似，而其确切极限由（推广的） sine 核 Gap 得。

## 五、应用与意义

Wigner 猜测及其兄弟的间距统计是"量子弹跳"（量子混沌 BGS 关联）的核心概念，也是随机矩阵普适性的物理实证：系统的谱在经典混沌时展示 GUE/GOE 排斥，而可积系统是泊松。用于能级统计、无规矩阵在大核数据中的评估。