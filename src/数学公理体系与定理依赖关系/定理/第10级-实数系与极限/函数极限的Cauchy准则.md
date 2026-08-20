# 函数极限的 Cauchy 准则

> **一句话大白话**：判断函数在某点有没有极限，可以不用先知道极限是多少——只需看“足够靠近 $a$ 的任意两个点，函数值是否也凑得一样近”。
>
> **小例子**：$f(x)=\sin\frac1x$ 在 $0$ 附近可取到任意接近、函数值却相差 $1$ 的两点，不满足 Cauchy 条件，故 $\lim_{x\to0}\sin\frac1x$ 不存在。

## 介绍

函数极限的 Cauchy 准则是函数极限存在的充要条件：$\lim_{x \to a} f(x)$ 存在当且仅当对任意 $\varepsilon > 0$，存在 $\delta > 0$，使得当 $0 < |x - a| < \delta$ 和 $0 < |y - a| < \delta$ 时，$|f(x) - f(y)| < \varepsilon$。该准则在不需要知道极限值的情况下即可判断函数极限是否存在。

## 分析

**前置依赖**：海涅定理、Cauchy 收敛准则。

## 思考过程

函数极限的 Cauchy 准则与数列的 Cauchy 收敛准则在本质上是一致的，只是将"充分靠后的两项"替换为"充分靠近 $a$ 的两个点"。数列 Cauchy 准则要求对任意 $\varepsilon > 0$，存在 $N$ 使得 $m, n > N$ 时 $|a_m - a_n| < \varepsilon$；而函数极限的 Cauchy 准则要求对任意 $\varepsilon > 0$，存在 $\delta > 0$ 使得 $0 < |x-a|, |y-a| < \delta$ 时 $|f(x) - f(y)| < \varepsilon$。

该准则的 $\varepsilon$-$\delta$ 表述不依赖于具体的极限值，因此特别适合用于判断函数极限是否存在（而不需要知道极限值是多少）。例如，要证明 $\lim_{x\to 0} \sin\frac{1}{x}$ 不存在，可以取 $x_n = \frac{1}{2n\pi}$ 和 $y_n = \frac{1}{(2n+1/2)\pi}$，它们在 $0$ 附近任意接近，但函数值之差恒为 $1$，不满足 Cauchy 条件。

在证明中，充分性部分通过海涅定理和数列的 Cauchy 收敛准则来完成，体现了分析学中不同定理之间的相互联系。

## 证明过程

**证明**：
必要性：设 $\lim_{x\to a} f(x) = L$，则对 $\varepsilon > 0$，$\exists \delta > 0$，$0 < |x-a| < \delta$ 时 $|f(x) - L| < \varepsilon/2$。故 $0 < |x-a|, |y-a| < \delta$ 时 $|f(x) - f(y)| \leq |f(x)-L| + |L-f(y)| < \varepsilon$。

充分性：假设 $f$ 满足 Cauchy 条件。对任意 $x_n \to a$（$x_n \neq a$），由数列 Cauchy 收敛准则，$\{f(x_n)\}$ 收敛。由海涅定理，$\lim_{x\to a} f(x)$ 存在。$\square$