# Mallat算法的正确性

> **一句话大白话**：怎么把小波系数算得快？Mallat 算法是"过两把互补的筛子再下采样"：低通筛出平缓趋势（近似系数），高通筛出抖动细节（细节系数），每层对"近似"递归加倍筛——而且这套拆开再拼回的流程严格精确、复杂度只要 $O(N)$。
>
> **小例子**：近似系数 $a_{j+1}[k]=\sum_nh[2k-n]a_j[n]=(a_j*\bar h)[2k]$，重构 $a_j[n]=\sum_k a_{j+1}[k]h[2k-n]+\sum_k d_{j+1}[k]g[2k-n]$，两式由双尺度关系互相精确还原。

## 一、定理介绍

Mallat 算法（快速小波变换）的正确性给出分解与重构的精确公式。设 MRA、尺度函数 $\phi$、小波 $\psi$、滤波 $h_k,g_k$，近似系数 $a_j[k]=\langle f,\phi_{j,k}\rangle$、细节系数 $d_j[k]=\langle f,\psi_{j,k}\rangle$。则分解
$$
a_{j+1}[k]=\sum_nh[2k-n]a_j[n],\qquad d_{j+1}[k]=\sum_ng[2k-n]a_j[n],
$$
与重构
$$
a_j[n]=\sum_k a_{j+1}[k]h[2k-n]+\sum_k d_{j+1}[k]g[2k-n]
$$
精确成立，总复杂度为 $O(N)$。

## 二、原理思路

公式源于尺度/小波方程的双尺度关系。把 $\phi_{j+1,k}=\sum_nh_n\phi_{j,2k+n}$、$\psi_{j+1,k}=\sum_ng_n\phi_{j,2k+n}$ 代入系数定义，利用 $f$ 在 $V_j$/$W_j$ 上的投影正交直和 $V_j=V_{j+1}\oplus W_{j+1}$，即得分解公式；反向用 $\phi_{j,n}$ 线性无关合并正交补中的两个表示，即得重构公式。均为卷积再抽样/零插值，故复杂度线性。

## 三、定理的严格表述

对 $f\in L^2(\mathbb R)$ 与标准正交小波基，双尺度关系
$$
\phi_{j+1,k}=\sum_n h_n\phi_{j,2k+n},\qquad \psi_{j+1,k}=\sum_n g_n\phi_{j,2k+n}
$$
给出分解
$$
a_{j+1}[k]=\sum_n h_n a_j[2k+n]=(a_j*\bar h)[2k],\qquad
d_{j+1}[k]=\sum_n g_n a_j[2k+n]=(a_j*\bar g)[2k],
$$
其中 $\bar h[k]=h[-k]$；重构
$$
a_j[n]=\sum_k a_{j+1}[k]h_{n-2k}+\sum_k d_{j+1}[k]g_{n-2k}.
$$
每层 $O(NL)$，总 $O(N)$（$L$ 为滤波长度）。

## 四、证明过程

**步骤1：双尺度关系。** 由 $\phi_{j+1,k}=2^{-(j+1)/2}\phi(2^{-(j+1)}t-k)$ 与尺度方程代入，
$$
\phi_{j+1,k}(t)=2^{-(j+1)/2}\sqrt2\sum_nh_n\phi(2^{-j}t-2k-n)=\sum_n h_n\phi_{j,2k+n}(t),
$$
小波同理 $\psi_{j+1,k}=\sum_ng_n\phi_{j,2k+n}$。

**步骤2：推导分解公式。** $a_{j+1}[k]=\langle f,\phi_{j+1,k}\rangle=\sum_nh_n\langle f,\phi_{j,2k+n}\rangle=\sum_nh_na_j[2k+n]$。令 $\bar h[k]=h[-k]$，则 $\sum_nh_na_j[2k+n]=\sum_mh[m-2k]a_j[m]=(a_j*\bar h)[2k]$；$d_{j+1}$ 同理。

**步骤3：推导重构公式。** $V_j=V_{j+1}\oplus W_{j+1}$ 使 $f_j=f_{j+1}+w_{j+1}$，分别用各自基展开并代入 $\phi_{j+1,k}=\sum_nh_{n-2k}\phi_{j,n}$、$\psi_{j+1,k}=\sum_ng_{n-2k}\phi_{j,n}$，合并 $\phi_{j,n}$ 的系数（线性无关）得
$$
a_j[n]=\sum_ka_{j+1}[k]h_{n-2k}+\sum_kd_{j+1}[k]g_{n-2k}.
$$

**步骤4：复杂度分析。** 每层近似与细节卷积 + 下采样，输入长 $N$、滤波长 $L$，每层 $O(NL)$；层数 $O(\log N)$ 但每层数据减半，总 $O(NL)$；$L$ 固定即 $O(N)$。

**结论（$\square$）**：Mallat 分解/重构公式精确，复杂度 $O(N)$。

## 五、应用与意义

Mallat 算法使小波变换得以实时高效实现（快于 FFT），是图像压缩（JPEG2000）、信号去噪、数据压缩与小波神经网络等大规模应用的性能根基。它把抽象的高维小波系数转化为可编程的滤波器组流水线，是小波分析从理论走向工程的关键桥梁。