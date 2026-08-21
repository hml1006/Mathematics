# Minkowski 线性型定理

> **一句话大白话**：给定 $n$ 个线性型，只要它们的常数乘积比系数的行列式大（$c_1\cdots c_n>|\det A|$），就存在一个非零整点使每个线性型的值都小于对应的常数——"格上必有一点压过每条线的界限"。
>
> **小例子**：两个线性型 $L_1=x$、$L_2=\sqrt2 x+y$，$\det A=\sqrt2\approx1.414$。取 $c_1=c_2=1.2$ 则 $1.44>|\det A|$，存在非零整点使 $|x|<1.2,\ |\sqrt2x+y|<1.2$（如 $x=1,y=-1$：$|1|<1.2$，$|\sqrt2-1|<1.2$）。

## 一、定理介绍

Minkowski 线性型定理是线性型的同名逼近定理，亦为 Minkowski 凸体定理的直接推论。它统一刻画"对称凸体"与"线性型的小值"，是丢番图逼近与 Diophantine 不等式（线性型逼近）的基础性工具。

## 二、原理思路

把线性型向量 $T(x)=(L_1(x),\dots,L_n(x))=Ax$ 视为到 $\mathbb{R}^n$ 的可逆线性变换。对称凸体 $K=\{y:|y_i|<c_i\}$ 体积 $2^nc_1\cdots c_n$。其原像 $T^{-1}(K)=\{x:|L_i(x)|<c_i\}$ 亦对称凸，体积 $\frac{2^nc_1\cdots c_n}{|\det A|}>2^n$（因 $c_1\cdots c_n>|\det A|$）。对标准格 $\mathbb{Z}^n$（$\det=1$）应用 Minkowski 凸体定理即得非零整点。

## 三、定理的严格表述

设 $L_1,\dots,L_n$ 为 $\mathbb{R}^n$ 上线性型，$L_i(x)=\sum_ja_{ij}x_j$，$A=(a_{ij})$ 可逆。若 $c_i>0$ 且 $c_1\cdots c_n>|\det A|$，则存在非零 $x\in\mathbb{Z}^n$ 使 $|L_i(x)|<c_i\ (i=1,\dots,n)$。齐次形式：$c_1\cdots c_n\ge|\det A|$ 时 $|L_i(x)|\le c_i$。

## 四、证明过程

**证明：**

**步骤 1：线性变换。** $T(x)=(L_1(x),\dots,L_n(x))$ 由 $A$ 给出，$|\det T|=|\det A|$。$\blacksquare$

**步骤 2：构造凸体。** $K=\{y:|y_i|<c_i,\ i=1,\dots,n\}$ 中心对称凸，$\operatorname{vol}(K)=2^nc_1\cdots c_n$。$\blacksquare$

**步骤 3：原像体积。** $T^{-1}(K)=\{x:|L_i(x)|<c_i\}$ 对称凸，且
$$\operatorname{vol}(T^{-1}(K))=\frac{\operatorname{vol}(K)}{|\det A|}=\frac{2^nc_1\cdots c_n}{|\det A|}>2^n.$$
（$\det(\mathbb{Z}^n)=1$。）$\blacksquare$

**步骤 4：Minkowski 定理。** 由 Minkowski 凸体定理，存在非零 $x\in\mathbb{Z}^n$ 使 $x\in T^{-1}(K)$，即 $|L_i(x)|<c_i\ (i=1,\dots,n)$。$\square$

## 五、应用与意义

线性型定理是把连续几何结论转化为整数不等式的高效桥梁，是 Minkowski 线性形式逼近理论的核心。它用于 Diophantine 逼近的 Dirichlet-type 存在性、同余系统与格的问题、金素数近似，也在密码与算法（线性同余与 Diophantine 不等式）中有用。推广形式（对复数线性型、多组线性型）见于现代算术逼近与遍历论（如 Littlewood 猜想研究）。