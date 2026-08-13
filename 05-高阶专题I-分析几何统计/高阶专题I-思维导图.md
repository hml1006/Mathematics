# 第五阶段：高阶专题I - 分析、几何、统计

## 第53级：调和分析

### 核心概念
- **Fourier 级数基础**：将周期函数分解为三角函数的叠加，$f(x) \sim \sum_{n=-\infty}^{\infty} c_n e^{inx}$，其中 $c_n = \frac{1}{2\pi}\int_0^{2\pi} f(x)e^{-inx}dx$
- **Fourier 变换**：将非周期函数从时域转换到频域，$\hat{f}(\xi) = \int_{\mathbb{R}} f(x)e^{-2\pi ix\xi}dx$，实现时间-频率对偶
- **Littlewood-Paley 分解**：将函数按频率尺度分解，$f = \sum_j \Delta_j f$，每个 $\Delta_j f$ 捕获特定频段的成分，类似音响均衡器分离高低音

### 重要定理
- **Calderón-Zygmund 理论**：研究奇异积分算子的有界性，建立 $L^p$ 空间（$1 < p < \infty$）上的估计，核心工具是 Calderón-Zygmund 分解
- **平方函数估计**：Littlewood-Paley 平方函数 $Sf = (\sum_j |\Delta_j f|^2)^{1/2}$ 满足 $\|Sf\|_p \sim \|f\|_p$，表明频率分解不丢失信息
- **Hardy 空间与 BMO**：$H^1$ 空间是 Fourier 分析的天然定义域，BMO（有界平均振荡）是 $H^1$ 的对偶空间

### 实际应用
- **信号处理**：音频均衡器将音乐分解为不同频段，Littlewood-Paley 理论保证分解的数学严谨性
- **偏微分方程**：通过频率分解研究 PDE 的正则性，高频成分对应解的光滑性
- **数论**：调和方法用于研究素数分布和指数和估计

---

## 第54级：傅立叶分析

### 核心概念
- **Fourier 级数收敛性**：Dirichlet-Jordan 定理给出逐点收敛条件，Fejér 定理保证 Cesàro 平均的一致收敛
- **Gibbs 现象**：在不连续点附近，Fourier 部分和会出现约 9% 的过冲，$\lim_{N\to\infty} \max S_N f(x) - f(x_0^+) = \frac{f(x_0^+)-f(x_0^-)}{2} \cdot G$，其中 $G \approx 0.17898$
- **离散 Fourier 变换（DFT）**：$X_k = \sum_{n=0}^{N-1} x_n e^{-2\pi ikn/N}$，将连续变换离散化，是数字信号处理的基础

### 重要定理
- **Plancherel 定理**：Fourier 变换是 $L^2$ 上的酉算子，$\|\hat{f}\|_2 = \|f\|_2$，保证能量守恒
- **Heisenberg 测不准原理**：$\Delta x \cdot \Delta \xi \geq \frac{1}{4\pi}$，时间和频率不能同时任意集中，等号在 Gauss 函数时成立
- **Nyquist-Shannon 采样定理**：带限函数 $f$（最高频率 $W$）可由采样点 $\{f(n/2W)\}$ 完全恢复，$f(x) = \sum_n f(n/2W)\text{sinc}(2W(x-n/2W))$

### 实际应用
- **数字音频**：CD 采样率 44.1kHz 足以还原人耳可听的 20kHz 频率，采样率不足会产生混叠（如电影中车轮倒转）
- **图像压缩**：JPEG 使用 DCT（离散余弦变换）压缩图像，保留主要频率成分
- **热方程求解**：通过 Fourier 变换将 $\partial_t u = \partial_x^2 u$ 转化为常微分方程 $\partial_t \hat{u} = -4\pi^2\xi^2 \hat{u}$

---

## 第55级：位势论

### 核心概念
- **Newton 位势**：$U^\mu(x) = \int_{\mathbb{R}^n} \frac{1}{|x-y|^{n-2}} d\mu(y)$（$n \geq 3$），描述电荷分布 $\mu$ 产生的静电势
- **调和函数**：满足 $\Delta u = 0$ 的函数，具有平均值性质 $u(x) = \frac{1}{|B_r|}\int_{B_r(x)} u(y)dy$ 和极值原理
- **Green 函数**：$G_\Omega(x,y) = \Gamma(x-y) - h(x,y)$，其中 $h$ 调和，用于求解 Dirichlet 问题

### 重要定理
- **最大值原理**：调和函数在区域内部不能达到最大值，$\max_{\overline{\Omega}} u = \max_{\partial\Omega} u$，除非 $u$ 是常数
- **Perron 方法**：通过构造次调和函数族的上确界求解 Dirichlet 问题，$u(x) = \sup\{v(x) : v \in \mathcal{F}_f\}$
- **Wiener 准则**：边界点 $x_0$ 正则的充要条件是 $\sum_{k=1}^\infty 2^{k(n-2)}\text{Cap}(B(x_0,2^{-k})\setminus\Omega) = \infty$

### 实际应用
- **热传导稳态**：金属板达到热平衡后，温度场 $u(x,y)$ 满足 $\Delta u = 0$，内部无热点或冷点
- **静电场**：点电荷产生的势场 $U(x) \propto 1/|x-y|$，等势线为同心圆，Green 函数描述点源的影响
- **概率论**：Brown 运动与调和函数密切相关，调和函数是 Brown 运动的鞅

---

## 第56级：算子代数

### 核心概念
- **C*-代数**：配备对合运算 $*$ 的 Banach 代数，满足 $\|a^*a\| = \|a\|^2$，如 $\mathcal{B}(H)$（Hilbert 空间上的有界算子）
- **von Neumann 代数**：弱算子拓扑闭的 $*$-子代数，等价于 $\mathcal{M} = \mathcal{M}''$（双交换子定理）
- **谱理论**：算子 $a$ 的谱 $\sigma(a) = \{\lambda \in \mathbb{C} : \lambda 1 - a \text{ 不可逆}\}$，自伴算子的谱为实数

### 重要定理
- **Gelfand-Naimark 定理**：交换 C*-代数等距同构于 $C_0(X)$，建立代数与拓扑空间的对偶
- **GNS 构造**：每个态 $\varphi$ 对应一个表示 $(\pi_\varphi, H_\varphi, \xi_\varphi)$，使得 $\varphi(a) = \langle \pi_\varphi(a)\xi_\varphi, \xi_\varphi \rangle$
- **因子分类**：Murray-von Neumann 将因子分为 I 型（有极小投影）、II 型（无有限投影）、III 型（无有限投影）

### 实际应用
- **量子力学**：可观测量对应自伴算子，谱对应测量值（如氢原子能级 $E_n = -13.6/n^2$ eV），态给出概率分布
- **量子统计**：II$_1$ 因子描述无穷粒子系统的统计力学，迹给出期望值
- **非交换几何**：Connes 纲领将 C*-代数视为"非交换空间"的代数

---

## 第57级：几何分析

### 核心概念
- **Laplace-Beltrami 算子**：$\Delta f = -\frac{1}{\sqrt{\det g}}\partial_i(\sqrt{\det g} g^{ij}\partial_j f)$，Riemann 流形上的 Laplace 算子
- **热核**：热方程 $(\partial_t + \Delta_x)p_t(x,y) = 0$ 的基本解，$p_t(x,y) \sim (4\pi t)^{-n/2}e^{-d(x,y)^2/4t}$（$t \to 0$）
- **Ricci 流**：$\partial_t g = -2\text{Ric}(g)$，通过几何流均匀化曲率，Perelman 用于证明 Poincaré 猜想

### 重要定理
- **Hodge 分解**：$\Omega^k(M) = \mathcal{H}^k(M) \oplus \text{Im} d \oplus \text{Im} \delta$，$k$-形式分解为调和部分、恰当部分和余恰当部分
- **Yamabe 问题**：存在共形度量 $\tilde{g} = u^{4/(n-2)}g$ 具有常数量曲率，等价于求解非线性椭圆方程
- **Perelman 熵公式**：$\mathcal{F}$-熵和 $\mathcal{W}$-熵沿 Ricci 流单调递增，用于排除奇点中的非平凡稀释

### 实际应用
- **Poincaré 猜想证明**：Perelman 利用 Ricci 流证明任何单连通三维闭流形同胚于 $S^3$
- **极小曲面**：平均曲率 $H = 0$ 的曲面，如悬链面 $x^2+y^2 = \cosh^2 z$，是面积泛函的临界点
- **谱几何**：通过 Laplace 算子的特征值研究流形的几何性质，"听出鼓的形状"

---

## 第58级：最优传输

### 核心概念
- **Monge 问题**：求映射 $T: X \to Y$ 满足 $T_\#\mu = \nu$，最小化 $\int_X c(x,T(x))d\mu(x)$，约束强导致存在性问题
- **Kantorovich 松弛**：求耦合 $\gamma \in \Pi(\mu,\nu)$ 最小化 $\int_{X\times Y} c(x,y)d\gamma$，线性规划框架保证存在性
- **Wasserstein 距离**：$W_p(\mu,\nu) = (\inf_{\gamma\in\Pi(\mu,\nu)}\int |x-y|^p d\gamma)^{1/p}$，度量概率分布间的"搬运成本"

### 重要定理
- **Kantorovich 对偶性**：$\min_\gamma \int c d\gamma = \sup_{(\varphi,\psi)\in\Phi_c} (\int \varphi d\mu + \int \psi d\nu)$，其中 $\varphi(x)+\psi(y) \leq c(x,y)$
- **Brenier 定理**：当 $c(x,y) = |x-y|^2/2$ 且 $\mu$ 绝对连续时，最优映射 $T = \nabla\phi$ 是凸函数的梯度
- **Benamou-Brenier 公式**：$W_2^2(\mu_0,\mu_1) = \inf_{(\rho,v)}\int_0^1\int |v_t|^2 d\rho_t dt$，其中 $\partial_t\rho + \nabla\cdot(\rho v) = 0$

### 实际应用
- **人口迁移规划**：将人口分布 $\mu$ 最优地搬到 $\nu$，Wasserstein 距离度量"最少需要搬多远"
- **图像配准**：通过最优传输将一幅图像变形到另一幅，保持质量守恒
- **机器学习**：Wasserstein 距离用于生成对抗网络（WGAN），比 KL 散度更稳定

---

## 第59级：渐近分析

### 核心概念
- **渐近展开**：$f(x) \sim \sum_{n=0}^\infty a_n\phi_n(x)$（$x \to \infty$），其中 $\phi_{n+1} = o(\phi_n)$，级数可发散但截断后提供好近似
- **$O$ 与 $o$ 符号**：$f(x) = O(g(x))$ 表示 $|f| \leq C|g|$，$f(x) = o(g(x))$ 表示 $f/g \to 0$
- **Poincaré 渐近展开**：在 $x_0$ 处，$f(x) - \sum_{n=0}^{N-1}a_n z_n(x) = o(z_{N-1}(x))$

### 重要定理
- **Watson 引理**：$\int_0^\infty e^{-xt}q(t)dt \sim \sum_{n=0}^\infty a_n \frac{\Gamma((n+\alpha)/\beta)}{x^{(n+\alpha)/\beta}}$，将积分渐近转化为 Gamma 函数
- **Laplace 方法**：$\int_a^b h(x)e^{-\lambda f(x)}dx \sim h(c)\sqrt{\frac{2\pi}{\lambda f''(c)}}e^{-\lambda f(c)}$，主贡献来自 $f$ 的最小值点 $c$
- **Stirling 公式**：$n! \sim \sqrt{2\pi n}(n/e)^n$，相对误差 $O(1/n)$，用简洁公式捕获阶乘的量级骨架

### 实际应用
- **量子隧穿（WKB）**：粒子穿越势垒的概率 $\sim e^{-2\int\sqrt{V-E}/\hbar}$，扫描隧道显微镜利用此效应观察原子
- **大数估计**：Stirling 公式用于估计 $n!$，无需逐次相乘，$n$ 越大越精确
- **振荡积分**：驻相法计算 $\int e^{i\lambda f(x)}\phi(x)dx$，主贡献来自相位 $f$ 的驻点

---

## 第60级：积分方程

### 核心概念
- **Fredholm 方程**：$\varphi(x) - \lambda\int_a^b K(x,y)\varphi(y)dy = f(x)$，核 $K(x,y)$ 定义在全区域 $[a,b]\times[a,b]$
- **Volterra 方程**：$\varphi(x) - \lambda\int_a^x K(x,y)\varphi(y)dy = f(x)$，核定义在三角区域 $y \leq x$，具有因果结构
- **积分算子**：$(\mathcal{K}\varphi)(x) = \int_a^b K(x,y)\varphi(y)dy$，Hilbert-Schmidt 核满足 $\iint|K|^2 < \infty$

### 重要定理
- **Fredholm 择一性**：要么方程对任意 $f$ 有唯一解，要么齐次方程有非平凡解且非齐次方程有解当且仅当 $f$ 与所有齐次解正交
- **Hilbert-Schmidt 展开**：对称核 $K(x,y) = \sum_{n=1}^\infty \frac{\varphi_n(x)\overline{\varphi_n(y)}}{\lambda_n}$，特征函数构成 $L^2$ 正交基
- **Mercer 定理**：连续对称正定核的展开绝对一致收敛，$K(x,y) = \sum_{n=1}^\infty \frac{\varphi_n(x)\varphi_n(y)}{\lambda_n}$

### 实际应用
- **辐射传热**：表面间辐射能量交换满足 Fredholm 方程 $\varphi(x) - \int K(x,y)\varphi(y)dy = f(x)$，$K(x,y)$ 是视角因子
- **Neumann 级数迭代**：$\varphi = \sum_{n=0}^\infty \lambda^n \mathcal{K}^n f$，类似"敲钟的回响"，逐次逼近精确解
- **Volterra 因果系统**：当前状态只依赖过去，如人口增长模型 $\varphi(x) = f(x) + \int_0^x K(x,y)\varphi(y)dy$

---

## 第61级：仿射几何

### 核心概念
- **仿射空间**：点集 $\mathbb{A}$ 配备平移空间 $V$，满足 $A + \mathbf{v} \in \mathbb{A}$，$\overrightarrow{AB} = \mathbf{v}$，去原点化的向量空间
- **仿射变换**：$F(\mathbf{x}) = A\mathbf{x} + \mathbf{b}$，其中 $A \in \text{GL}(V)$，保持共线性、平行性和简单比
- **重心坐标**：$P = \sum_{i=0}^n \lambda_i A_i$，$\sum \lambda_i = 1$，用顶点权重表示点的位置

### 重要定理
- **仿射基本定理**：$n+1$ 个仿射无关点唯一确定仿射变换，$F(A_i) = A_i'$ 决定唯一的 $F$
- **Cevian 定理**：三角形三线 $AD, BE, CF$ 共点当且仅当 $\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB} = 1$
- **Desargues 定理**：两三角形对应顶点连线共点，则对应边交点共线

### 实际应用
- **卫星影像校正**：倾斜拍摄的照片经仿射变换 $F(\mathbf{x}) = A\mathbf{x} + \mathbf{b}$ 校正为正射影像，保持平行性和比例
- **计算机图形学**：仿射变换用于图像的拉伸、旋转、错切，保持平行线仍平行
- **有限元方法**：重心坐标用于三角形单元上的插值，权重决定物理量的分布
