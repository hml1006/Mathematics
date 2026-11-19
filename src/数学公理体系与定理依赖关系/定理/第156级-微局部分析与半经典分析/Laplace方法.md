# Laplace 方法

> **一句话大白话**：形如 $\int g e^{-\lambda f}$ 的积分，大 $\lambda$ 时几乎全由 $f$ 的最低点贡献；内部非退化谷底给高斯型的 $\lambda^{-1/2}$，有非零斜率的端点则给 $\lambda^{-1}$。
>
> **小例子**：$f(x)=x^2$ 在 $[-1,1]$ 的唯一内点最小值为 $0$，所以 $\int_{-1}^1e^{-\lambda x^2}\,\mathrm dx=\sqrt{\pi/\lambda}+O(e^{-c\lambda})$，与 Laplace 公式 $\sqrt{2\pi/(\lambda f''(0))}$ 完全一致。

## 介绍

Laplace 方法研究实指数积分的渐近主项和展开。核心不是把 Taylor 级数形式代入就结束，而是先证明唯一最小值附近有真正的主导性，再用局部坐标把积分化成高斯积分。最小值位于内部还是边界、是否同时是驻点，会改变宽度、系数与误差阶。

## 分析

**前置依赖**：渐近等价、Taylor 展开、高斯积分、指数局部化、Watson 引理。

**定理内容：内点非退化最小值**：设

$$
I(\lambda)=\int_a^b g(x)e^{-\lambda f(x)}\,\mathrm dx,
\qquad \lambda\to+\infty.
$$

设 $f,g$ 连续，$f$ 在唯一全局最小值点 $c\in(a,b)$ 附近有 $C^2$ 光滑性，$f'(c)=0$、$f''(c)>0$，且在 $c$ 的任一去心邻域外，$f$ 的下确界严格大于 $f(c)$。则

$$
\boxed{I(\lambda)=e^{-\lambda f(c)}
\left[g(c)\sqrt{\frac{2\pi}{\lambda f''(c)}}+o(\lambda^{-1/2})\right].}
$$

若进一步 $f$ 在 $c$ 附近为 $C^4$、$g$ 为 $C^2$，则误差可加强为

$$
I(\lambda)=e^{-\lambda f(c)}
\left[g(c)\sqrt{\frac{2\pi}{\lambda f''(c)}}+O(\lambda^{-3/2})\right].
$$

这里默认 $g(c)\ne0$ 以显示主项；若 $g(c)=0$，需继续展开并使用更高阶项。

**端点贡献**：若唯一全局最小值在左端点 $a$，且 $f'(a)>0$，则首项为

$$
I(\lambda)\sim \frac{g(a)}{\lambda f'(a)}e^{-\lambda f(a)}.
$$

当 $f$ 为 $C^2$、$g$ 在端点附近 Lipschitz 时，可写

$$
I(\lambda)=e^{-\lambda f(a)}
\left[\frac{g(a)}{\lambda f'(a)}+O(\lambda^{-2})\right].
$$

右端点相应地把 $f'(a)$ 换成 $-f'(b)>0$。但若端点同时是驻点，即 $f'(a)=0$、$f''(a)>0$，贡献是半高斯：

$$
I(\lambda)=e^{-\lambda f(a)}
\left[\frac{g(a)}2\sqrt{\frac{2\pi}{\lambda f''(a)}}+O(\lambda^{-1})\right]
$$

（足够光滑时）。因此不能把所有端点都写成 $\lambda^{-1}$。若多个彼此分离的非退化最小值同为全局最低，应将各项相加。

## 思考过程

在内部最小值附近，$f(x)-f(c)\approx\frac12f''(c)(x-c)^2$。令 $y=\sqrt{\lambda}(x-c)$，则有意义的区域宽度为 $\lambda^{-1/2}$，积分变成标准高斯积分。普通端点没有驻点条件，局部近似是线性的，$f(x)-f(a)\approx f'(a)(x-a)$；换元 $u=\lambda(x-a)$ 后留下尺度 $\lambda^{-1}$。最小值之外若函数值高出固定正数，其贡献相对主指数是指数小的。

## 证明过程

**证明纲要**：

1. **指数局部化**：取 $c$ 的小邻域 $U$。由全局间隔条件，存在 $\eta>0$ 使 $f\ge f(c)+\eta$ 于 $U$ 外，所以外部积分相对 $e^{-\lambda f(c)}$ 至多含因子 $e^{-\lambda\eta}$，不影响代数阶展开。
2. **内部高斯化**：在 $U$ 内写
   $$
   f(c+t)=f(c)+\frac12f''(c)t^2+o(t^2),
   \qquad g(c+t)=g(c)+o(1).
   $$
   作 $t=y/\sqrt{\lambda}$，则积分化为
   $$
   \frac{e^{-\lambda f(c)}}{\sqrt\lambda}
   \int g(c+ y/\sqrt\lambda)
   e^{-\frac12f''(c)y^2+o(1)}\,\mathrm dy.
   $$
   用截断和支配收敛把积分区间延拓到 $\mathbb R$，即得首项 $g(c)\sqrt{2\pi/f''(c)}$。
3. **误差阶**：仅有 $C^2$ 与连续性时，上述 $o(1)$ 只给相对 $o(1)$。有 $C^4,C^2$ 展开后，奇次项积分相消，首个未写出的非零修正来自下一阶高斯矩，故绝对误差为 $e^{-\lambda f(c)}O(\lambda^{-3/2})$。
4. **端点线性化**：普通左端点时令 $t=x-a\ge0$、$u=\lambda t$。则
   $$
   \int_0^\delta g(a+t)e^{-\lambda(f'(a)t+O(t^2))}\,\mathrm dt
   =\frac{g(a)}{\lambda f'(a)}+O(\lambda^{-2}),
   $$
   尾部同样指数小。端点驻点则使用同一高斯论证，但积分只有 $y\ge0$ 的半轴，故系数为内点的一半。$\square$

## 课堂问答

**老师**：内部最小值为什么贡献 $\lambda^{-1/2}$，而普通端点贡献 $\lambda^{-1}$？

**学生**：内部非退化最小值附近是二次谷底，满足 $\lambda(f-f(c))\lesssim1$ 的宽度为 $\lambda^{-1/2}$。普通端点若斜率非零，局部是线性坡面，对应宽度为 $\lambda^{-1}$，所以幂次不同。

**老师（追问）**：$O(\lambda^{-3/2})$ 的误差是否能从 $f\in C^2$、$g$ 连续直接得到？

**学生**：不能。仅有这些条件只能稳妥写出首项后的 $o(\lambda^{-1/2})$。要得到明确的下一阶大 O 界，需要更多局部光滑性，例如 $f\in C^4$、$g\in C^2$，以便控制 Taylor 余项和下一阶系数。

**老师（拓展）**：端点最小值一定比内部最小值低一个半阶吗？

**学生**：不一定。只有端点斜率非零时才是 $\lambda^{-1}$。若端点也是非退化驻点，就是半高斯贡献，仍为 $\lambda^{-1/2}$，系数是相应内点公式的一半；若二阶导数也为零，则幂次还会继续改变。

## 相关条目

- [Watson 引理](./Watson引理.md)
- [最速下降法](./最速下降法.md)
- [主教程第59级：渐近分析](../../../05-高阶专题I-分析几何统计/第59级-渐近分析.md)
