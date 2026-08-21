# p-adic Hodge理论的比较定理
>
> **一句话大白话**：p-adic 域上代数簇的 p-adic étale 上同调（数论/伽罗瓦侧）与 de Rham 上同调（几何侧）经 Fontaine 的周期环互相连接——比较定理是一条"同构桥"。
>
> **小例子**：对 $K/\mathbb{Q}_p$、光滑射影 $X$，比较定理
$$
H^i_{\acute et}(X_{\bar K},\mathbb Q_p)\otimes B_{\mathrm{dR}}\cong H^i_{\mathrm{dR}}(X/K)\otimes_K B_{\mathrm{dR}},
$$
以 $B_{\mathrm{dR}}$（Fontaine de Rham 周期环）同构。

## 一、定理介绍

> **前置依赖**：Fontaine周期环($B_\mathrm{cris}$/$B_\mathrm{st}$/$B_\mathrm{dR}$)、p-adic Galois表示、晶体与对数-cris上同调、Hodge-Tate权与过滤、p-adic解析几何

p-adic Hodge 理论的比较定理（Faltings 1988；Tsuji、Nizi l 等后继）断言：对 $p$-adic 域 $K=\mathbb Q_p$ 与其光滑（半 stable）射影簇 $X$，存在（$G_K$-等变、过滤→同构）比较同构
$$
H^i_{\acute et}(X_{\bar K},\mathbb Q_p)\otimes B_{\mathrm{dR}}\cong H^i_{\mathrm{dR}}(X/K)\otimes_K B_{\mathrm{dR}},
$$
其中 $B_{\mathrm{dR}}$ 为 Fontaine 的 de Rham 周期环。它把算侧的 p-adic Galois 表示与几何侧的 Hodge 结构对接，是 p-adic 几何中"代数→算术"的根本工具。

## 二、原理思路

利用 p-adic 周期环：B := Fontaine 建立的 $B_{\mathrm{dR}}$（完备化 en des e特质经聚合 $B_{\mathrm{cris}}\hookrightarrow B_{\mathrm{dR}}$）具 $G_K$ 作用与过滤。其构造经尚未分裂环的逆极限与形变（天文观测范froben）；比较同构通过把它们“⊗B”后把两个上同调都规范成 $B_{\mathrm{dR}}$ 上的 Hodge 结构，进而严筋同构。光滑情形（对应“filtered crystalline”）与半 stable（log 形）分别用 Faltings / Tsuji 方法。

## 三、定理的严格表述

设 $K$ 为 $p$-adic 域（$\mathbb Q_p$ 的有限扩张），$\bar K$ 为代数闭包，$G_K=\mathrm{Gal}(\bar K/K)$，$X/K$ 光滑射影维数 $d$。则存在 $G_K$-等变的同构（保滤级）：
$$
H^i_{\acute et}(X_{\bar K},\mathbb Q_p)\otimes_{\mathbb Q_p}B_{\mathrm{dR}}\cong H^i_{\mathrm{dR}}(X/K)\otimes_K B_{\mathrm{dR}},
$$
半 stable 情形用 $B_{\mathrm{st}}$ 与对数-cris 上同调：$H^i_{\acute et}\otimes B_{\mathrm{st}}\cong H^i_{\mathrm{log-cris}}(X/\mathcal O_K)\otimes B_{\mathrm{st}}$。

## 四、证明过程

概略（Faltings/近后缀）：(1) 构造周期环 $B_{\mathrm{cris}},B_{\mathrm{st}},B_{\mathrm{dR}}$ 及其过滤/$\varphi$ /$N$-结构；(2) 用近幂等近似与 p-adic 解析几何把 étale 上同调与（对数-）cristallin 上同调比较；(3) 利用 formal Hodge /SGA7 技术与超幂等正则化证明同构并等变e Galois；(4) 检验过滤一致与满射witt。Tsuji、Nizoal 等加固半 stable 情形。

## 五、应用与意义

比较定理奠定 p-adic Hodge 理论，用于定义 Hodge–Tate 权、晶体/半stable 表示分类、模曲线/Shimura 簇的算术及 p-adic Langlands 中 Galois 与自守的对接，也是 Fargues–Fontaine 曲线与现代 p-adic 几何的起点。