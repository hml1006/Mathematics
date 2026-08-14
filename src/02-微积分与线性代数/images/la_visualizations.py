#!/usr/bin/env python3
"""生成线性代数可视化图形"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.patches import FancyArrowPatch, Polygon, Circle, Arc
from matplotlib.collections import PatchCollection
import os

# 注册中文字体
_cjk_font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fm.fontManager.addfont(_cjk_font_path)
_fp = fm.FontProperties(fname=_cjk_font_path)
# 设置全局字体
plt.rcParams['font.sans-serif'] = [_fp.get_name()] + plt.rcParams.get('font.sans-serif', [])
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'cm'

# 全局设置
plt.rcParams.update({
    'figure.dpi': 150,
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'axes.grid': True,
    'grid.alpha': 0.3,
})

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save_fig(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)
    print(f"  Saved: {name}")


# ============================================================
# 图1: 向量空间与子空间
# ============================================================
def plot_vector_space_subspace():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    # (a) R^2 向量空间
    ax = axes[0]
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.set_title(r'$(a)\;\mathbb{R}^2$ 向量空间', fontsize=12)
    # 画网格
    for i in range(-3, 4):
        ax.axhline(i, color='gray', alpha=0.15)
        ax.axvline(i, color='gray', alpha=0.15)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    # 画几个向量
    vectors = [(2, 1), (-1, 2), (1, -1), (2, -2)]
    colors = ['#e74c3c', '#2ecc71', '#3498db', '#9b59b6']
    for v, c in zip(vectors, colors):
        ax.annotate('', xy=v, xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=c, lw=2))
        ax.text(v[0]+0.15, v[1]+0.15, f'$({v[0]},{v[1]})$', fontsize=9, color=c)
    ax.text(2.2, -2.8, r'任意向量 $\in \mathbb{R}^2$', fontsize=10, color='gray')

    # (b) 子空间（过原点的直线）
    ax = axes[1]
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.set_title(r'$(b)\;\mathbb{R}^3$ 的子空间（过原点的直线）', fontsize=12)
    for i in range(-3, 4):
        ax.axhline(i, color='gray', alpha=0.15)
        ax.axvline(i, color='gray', alpha=0.15)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    # 画一条过原点的直线
    t = np.linspace(-3, 3, 100)
    ax.plot(t, 0.5*t, 'b-', alpha=0.3, linewidth=3)
    ax.annotate('', xy=(2, 1), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.annotate('', xy=(-1, -0.5), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2))
    ax.annotate('', xy=(1, 0.5), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2))
    ax.text(2.2, 1.3, r'$v_1$', fontsize=11, color='#e74c3c')
    ax.text(-1.6, -0.9, r'$v_2$', fontsize=11, color='#2ecc71')
    ax.text(1.2, 0.8, r'$v_1+v_2$', fontsize=11, color='#3498db')
    ax.text(-2.8, -2.5, '子空间中的向量\n对加法和数乘封闭', fontsize=9, color='gray')

    # (c) 不是子空间的例子
    ax = axes[2]
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.set_title(r'$(c)$ 不是子空间的例子', fontsize=12)
    for i in range(-3, 4):
        ax.axhline(i, color='gray', alpha=0.15)
        ax.axvline(i, color='gray', alpha=0.15)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    # 画一条不过原点的直线
    ax.plot(t, 0.5*t + 1, 'r-', alpha=0.3, linewidth=3)
    ax.annotate('', xy=(2, 2), xytext=(0, 1),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.annotate('', xy=(-2, 0), xytext=(0, 1),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2))
    # 和向量不在集合中
    ax.annotate('', xy=(0, 2), xytext=(0, 1),
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2, linestyle='--'))
    ax.text(0.2, 2.3, r'$v_1+v_2$ 不在集合中!', fontsize=9, color='#e74c3c')
    ax.text(-2.8, -2.5, '不过原点 → 不是子空间', fontsize=9, color='gray')

    fig.tight_layout()
    save_fig(fig, 'la-01-vector-space-subspace.svg')


# ============================================================
# 图2: 线性组合与张成空间
# ============================================================
def plot_span_linear_combination():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # (a) 两个向量的张成空间
    ax = axes[0]
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.set_title(r'$(a)\;\operatorname{span}(v_1, v_2) = \mathbb{R}^2$（线性无关）', fontsize=11)
    for i in range(-4, 5):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    v1 = np.array([2, 1])
    v2 = np.array([1, 2])
    # 画张成空间（整个平面用浅色填充）
    ax.fill([-4, 4, 4, -4], [-4, -4, 4, 4], color='#3498db', alpha=0.05)
    # 画线性组合
    c1, c2 = 1.0, 0.8
    combo = c1*v1 + c2*v2
    # 平行四边形法则
    ax.annotate('', xy=v1, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.annotate('', xy=c2*v2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2))
    ax.annotate('', xy=combo, xytext=v1,
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2, linestyle='--'))
    ax.annotate('', xy=combo, xytext=c2*v2,
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2, linestyle='--'))
    ax.annotate('', xy=combo, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#9b59b6', lw=2.5))
    ax.text(2.2, 0.5, r'$c_1 v_1$', fontsize=11, color='#e74c3c')
    ax.text(0.5, 2.0, r'$c_2 v_2$', fontsize=11, color='#2ecc71')
    ax.text(combo[0]+0.2, combo[1]+0.2, r'$c_1v_1+c_2v_2$', fontsize=11, color='#9b59b6')
    ax.text(v1[0]+0.1, v1[1]-0.4, r'$v_1$', fontsize=12, color='#e74c3c', fontweight='bold')
    ax.text(v2[0]-0.5, v2[1]+0.1, r'$v_2$', fontsize=12, color='#2ecc71', fontweight='bold')

    # (b) 共线向量只能张成一条直线
    ax = axes[1]
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.set_title(r'$(b)\;\operatorname{span}(v_1, v_2)$（线性相关）$= $ 一条直线', fontsize=11)
    for i in range(-4, 5):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    v1 = np.array([2, 1])
    v2 = np.array([1, 0.5])  # v2 = 0.5*v1
    t = np.linspace(-3, 3, 100)
    ax.plot(t*2, t, 'b-', alpha=0.2, linewidth=6)
    ax.annotate('', xy=v1, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.annotate('', xy=v2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2))
    ax.annotate('', xy=-v1, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#9b59b6', lw=2))
    ax.text(2.2, 0.6, r'$v_1$', fontsize=12, color='#e74c3c')
    ax.text(1.2, 0.0, r'$v_2$', fontsize=12, color='#2ecc71')
    ax.text(-2.5, -1.3, r'$-v_1$', fontsize=12, color='#9b59b6')
    ax.text(-3.5, -3.2, r'$v_2 = \frac{1}{2}v_1$，线性相关', fontsize=10, color='gray')
    ax.text(-3.5, -3.8, r'张成空间只有 1 维', fontsize=10, color='gray')

    fig.tight_layout()
    save_fig(fig, 'la-02-span-linear-combination.svg')


# ============================================================
# 图3: 线性变换的几何意义
# ============================================================
def plot_linear_transformations():
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    def draw_grid(ax, title, transform=None, color_grid='gray'):
        ax.set_xlim(-3.5, 3.5); ax.set_ylim(-3.5, 3.5)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=11)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        # 画变换后的网格线
        for i in np.linspace(-3, 3, 7):
            # 竖线
            pts_v = np.array([[i, i], [-3, 3]])
            if transform is not None:
                pts_v = transform @ pts_v
            ax.plot(pts_v[0], pts_v[1], color=color_grid, alpha=0.3, linewidth=0.8)
            # 横线
            pts_h = np.array([[-3, 3], [i, i]])
            if transform is not None:
                pts_h = transform @ pts_h
            ax.plot(pts_h[0], pts_h[1], color=color_grid, alpha=0.3, linewidth=0.8)
        # 画基向量
        e1 = np.array([1, 0]); e2 = np.array([0, 1])
        if transform is not None:
            e1 = transform @ e1; e2 = transform @ e2
        ax.annotate('', xy=e1, xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5))
        ax.annotate('', xy=e2, xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2.5))
        ax.text(e1[0]+0.15, e1[1]-0.2, r'$e_1$', fontsize=11, color='#e74c3c', fontweight='bold')
        ax.text(e2[0]-0.4, e2[1]+0.1, r'$e_2$', fontsize=11, color='#2ecc71', fontweight='bold')

    # (a) 恒等变换
    draw_grid(axes[0, 0], r'$(a)$ 恒等变换 $I$', color_grid='#3498db')

    # (b) 旋转 45°
    theta = np.pi/4
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    draw_grid(axes[0, 1], r'$(b)$ 旋转 $45°$', color_grid='#e67e22')

    # (c) 缩放
    S = np.array([[2, 0], [0, 0.5]])
    draw_grid(axes[0, 2], r'$(c)$ 缩放 $\operatorname{diag}(2, 0.5)$', color_grid='#9b59b6')

    # (d) 剪切
    SH = np.array([[1, 1], [0, 1]])
    draw_grid(axes[1, 0], r'$(d)$ 剪切 $(1,1;\,0,1)$', color_grid='#e74c3c')

    # (e) 投影到 x 轴
    P = np.array([[1, 0], [0, 0]])
    draw_grid(axes[1, 1], r'$(e)$ 投影到 $x$ 轴', color_grid='#1abc9c')

    # (f) 反射
    REF = np.array([[1, 0], [0, -1]])
    draw_grid(axes[1, 2], r'$(f)$ 关于 $x$ 轴的反射', color_grid='#c0392b')

    fig.tight_layout()
    save_fig(fig, 'la-03-linear-transformations.svg')


# ============================================================
# 图4: 特征值与特征向量
# ============================================================
def plot_eigenvalues_eigenvectors():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # (a) 矩阵 A = [[4,2],[1,3]] 的特征向量
    ax = axes[0]
    ax.set_xlim(-3, 4); ax.set_ylim(-3, 4)
    ax.set_aspect('equal')
    ax.set_title(r'$(a)\;A=(4,2;\,1,3)$ 的特征向量', fontsize=11)
    for i in range(-3, 5):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    A = np.array([[4, 2], [1, 3]])
    # lambda_1 = 5, v1 = (2, 1)
    # lambda_2 = 2, v2 = (1, -1)
    v1 = np.array([2, 1]) / np.sqrt(5) * 2
    v2 = np.array([1, -1]) / np.sqrt(2) * 2
    Av1 = A @ v1
    Av2 = A @ v2

    # 特征方向
    t = np.linspace(-3, 3, 100)
    ax.plot(t*v1[0], t*v1[1], 'r-', alpha=0.15, linewidth=4)
    ax.plot(t*v2[0], t*v2[1], 'b-', alpha=0.15, linewidth=4)

    # 原向量
    ax.annotate('', xy=v1, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.annotate('', xy=Av1, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2, linestyle='--'))
    ax.text(v1[0]+0.1, v1[1]+0.2, r'$v_1$', fontsize=12, color='#e74c3c', fontweight='bold')
    ax.text(Av1[0]+0.1, Av1[1]-0.3, r'$Av_1=5v_1$', fontsize=10, color='#e74c3c')

    ax.annotate('', xy=v2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2))
    ax.annotate('', xy=Av2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2, linestyle='--'))
    ax.text(v2[0]+0.1, v2[1]-0.4, r'$v_2$', fontsize=12, color='#3498db', fontweight='bold')
    ax.text(Av2[0]-0.3, Av2[1]-0.5, r'$Av_2=2v_2$', fontsize=10, color='#3498db')

    ax.text(-3, -2.7, r'特征向量在变换下只伸缩，不改变方向', fontsize=9, color='gray')

    # (b) 单位圆在矩阵变换下的像
    ax = axes[1]
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.set_title(r'$(b)$ 矩阵变换对单位圆的作用', fontsize=11)
    for i in range(-4, 5):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    theta = np.linspace(0, 2*np.pi, 100)
    circle = np.array([np.cos(theta), np.sin(theta)])
    transformed = A @ circle

    ax.plot(circle[0], circle[1], 'b-', alpha=0.3, linewidth=1.5, label='单位圆')
    ax.fill(circle[0], circle[1], color='blue', alpha=0.05)
    ax.plot(transformed[0], transformed[1], 'r-', alpha=0.5, linewidth=2, label=r'$A$ 变换后')
    ax.fill(transformed[0], transformed[1], color='red', alpha=0.05)

    # 画特征向量方向
    ax.annotate('', xy=v1*1.5, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.annotate('', xy=v2*1.5, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2))
    ax.text(v1[0]*1.5+0.1, v1[1]*1.5+0.2, r'$\lambda_1=5$ 方向', fontsize=9, color='#e74c3c')
    ax.text(v2[0]*1.5+0.1, v2[1]*1.5-0.4, r'$\lambda_2=2$ 方向', fontsize=9, color='#3498db')

    ax.legend(fontsize=9, loc='upper left')
    ax.text(-3.8, -3.5, '圆被拉伸为椭圆\n半轴长度 = 特征值', fontsize=9, color='gray')

    fig.tight_layout()
    save_fig(fig, 'la-04-eigenvalues-eigenvectors.svg')


# ============================================================
# 图5: 行列式的几何意义
# ============================================================
def plot_determinant_geometry():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    # (a) det > 0: 面积放大
    ax = axes[0]
    ax.set_xlim(-1, 4); ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.set_title(r'$(a)\;\det(A) = 2 > 0$（面积放大 2 倍）', fontsize=11)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    # 原单位正方形
    sq = np.array([[0, 1, 1, 0], [0, 0, 1, 1]])
    ax.fill(sq[0], sq[1], color='blue', alpha=0.15)
    ax.plot(np.append(sq[0], sq[0, 0]), np.append(sq[1], sq[1, 0]), 'b-', linewidth=1.5)
    # 变换后
    A = np.array([[2, 0], [0, 1]])
    tsq = A @ sq
    ax.fill(tsq[0], tsq[1], color='red', alpha=0.15)
    ax.plot(np.append(tsq[0], tsq[0, 0]), np.append(tsq[1], tsq[1, 0]), 'r--', linewidth=1.5)
    ax.text(0.3, 0.3, '1', fontsize=12, color='blue', fontweight='bold')
    ax.text(1.2, 0.3, '2', fontsize=12, color='red', fontweight='bold')

    # (b) det < 0: 翻转
    ax = axes[1]
    ax.set_xlim(-3, 3); ax.set_ylim(-1, 3)
    ax.set_aspect('equal')
    ax.set_title(r'$(b)\;\det(A) = -1 < 0$（翻转 + 面积不变）', fontsize=11)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    A2 = np.array([[-1, 0], [0, 1]])
    tsq2 = A2 @ sq
    ax.fill(sq[0], sq[1], color='blue', alpha=0.15)
    ax.plot(np.append(sq[0], sq[0, 0]), np.append(sq[1], sq[1, 0]), 'b-', linewidth=1.5)
    ax.fill(tsq2[0], tsq2[1], color='red', alpha=0.15)
    ax.plot(np.append(tsq2[0], tsq2[0, 0]), np.append(tsq2[1], tsq2[1, 0]), 'r--', linewidth=1.5)
    ax.text(0.3, 0.3, '+1', fontsize=12, color='blue', fontweight='bold')
    ax.text(-1.6, 0.3, '−1', fontsize=12, color='red', fontweight='bold')

    # (c) det = 0: 坍缩
    ax = axes[2]
    ax.set_xlim(-1, 3); ax.set_ylim(-1, 3)
    ax.set_aspect('equal')
    ax.set_title(r'$(c)\;\det(A) = 0$（坍缩到低维）', fontsize=11)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    A3 = np.array([[1, 2], [0.5, 1]])  # det = 1-1 = 0
    tsq3 = A3 @ sq
    ax.fill(sq[0], sq[1], color='blue', alpha=0.15)
    ax.plot(np.append(sq[0], sq[0, 0]), np.append(sq[1], sq[1, 0]), 'b-', linewidth=1.5)
    ax.plot(tsq3[0], tsq3[1], 'r-', linewidth=2.5)
    ax.annotate('', xy=tsq3[:, 2], xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(0.3, 0.3, '1', fontsize=12, color='blue', fontweight='bold')
    ax.text(2.0, 1.3, '0（面积为 0）', fontsize=11, color='red', fontweight='bold')
    ax.text(-0.8, -0.8, '正方形坍缩为线段', fontsize=9, color='gray')

    fig.tight_layout()
    save_fig(fig, 'la-05-determinant-geometry.svg')


# ============================================================
# 图6: Gram-Schmidt 正交化过程
# ============================================================
def plot_gram_schmidt():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    v1 = np.array([2, 1])
    v2 = np.array([0, 2])
    u1 = v1 / np.linalg.norm(v1)
    proj = np.dot(v2, u1) * u1
    w2 = v2 - proj
    u2 = w2 / np.linalg.norm(w2)

    # (a) 原始向量
    ax = axes[0]
    ax.set_xlim(-0.5, 3); ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.set_title(r'$(a)$ 原始向量 $v_1, v_2$', fontsize=11)
    for i in range(0, 4):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.annotate('', xy=v1, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5))
    ax.annotate('', xy=v2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2.5))
    ax.text(v1[0]+0.1, v1[1]-0.2, r'$v_1=(2,1)$', fontsize=11, color='#e74c3c')
    ax.text(v2[0]-0.8, v2[1]+0.1, r'$v_2=(0,2)$', fontsize=11, color='#2ecc71')

    # (b) 投影过程
    ax = axes[1]
    ax.set_xlim(-0.5, 3); ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.set_title(r'$(b)$ 从 $v_2$ 减去在 $v_1$ 方向的投影', fontsize=11)
    for i in range(0, 4):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    # v1 方向
    t = np.linspace(-0.5, 3, 100)
    ax.plot(t*v1[0]/np.linalg.norm(v1), t*v1[1]/np.linalg.norm(v1), 'r-', alpha=0.15, linewidth=3)
    ax.annotate('', xy=v1, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5))
    ax.annotate('', xy=v2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2.5))
    # 投影
    ax.annotate('', xy=proj, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#f39c12', lw=2))
    # 垂直分量
    ax.plot([v2[0], proj[0]], [v2[1], proj[1]], 'b--', linewidth=1.5)
    # 直角标记
    angle_size = 0.15
    ax.plot([proj[0]+angle_size*u1[1], proj[0]+angle_size*u1[1], proj[0]],
            [proj[1]-angle_size*u1[0], proj[1], proj[1]], 'k-', linewidth=0.8)
    ax.text(proj[0]+0.1, proj[1]-0.3, r'$\operatorname{proj}_{v_1}v_2$', fontsize=9, color='#f39c12')
    ax.text(v2[0]-1.0, v2[1]+0.1, r'$v_2$', fontsize=11, color='#2ecc71')
    ax.text(v1[0]+0.1, v1[1]-0.2, r'$v_1$', fontsize=11, color='#e74c3c')
    ax.text((v2[0]+proj[0])/2-0.8, (v2[1]+proj[1])/2+0.1, r'$w_2$', fontsize=11, color='#3498db')

    # (c) 正交化结果
    ax = axes[2]
    ax.set_xlim(-0.5, 3); ax.set_ylim(-0.5, 3)
    ax.set_aspect('equal')
    ax.set_title(r'$(c)$ 正交化结果 $u_1 \perp u_2$', fontsize=11)
    for i in range(0, 4):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.annotate('', xy=u1*2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5))
    ax.annotate('', xy=u2*2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2.5))
    # 直角标记
    ax.plot([0.2*u1[0]+0.2*u2[0], 0.2*u1[0], 0.2*u2[0]],
            [0.2*u1[1]+0.2*u2[1], 0.2*u1[1], 0.2*u2[1]], 'k-', linewidth=1)
    ax.text(u1[0]*2+0.1, u1[1]*2-0.2, r'$u_1$', fontsize=12, color='#e74c3c', fontweight='bold')
    ax.text(u2[0]*2-0.5, u2[1]*2+0.1, r'$u_2$', fontsize=12, color='#3498db', fontweight='bold')
    ax.text(-0.3, -0.3, r'$\langle u_1, u_2 \rangle = 0$', fontsize=10, color='gray')

    fig.tight_layout()
    save_fig(fig, 'la-06-gram-schmidt.svg')


# ============================================================
# 图7: 正交投影
# ============================================================
def plot_orthogonal_projection():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # (a) 向量在子空间上的投影
    ax = axes[0]
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.set_title(r'$(a)$ 向量在子空间 $W$ 上的正交投影', fontsize=11)
    for i in range(-1, 6):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    v = np.array([3, 4])
    w_dir = np.array([1, 0.5])
    w_dir = w_dir / np.linalg.norm(w_dir)
    proj = np.dot(v, w_dir) * w_dir
    perp = v - proj

    # 子空间 W（直线）
    t = np.linspace(-1, 5, 100)
    ax.plot(t*w_dir[0], t*w_dir[1], 'b-', alpha=0.2, linewidth=5)
    ax.fill_between(t*w_dir[0]-0.05, t*w_dir[1]-0.1, t*w_dir[1]+0.1,
                    color='blue', alpha=0.05)

    ax.annotate('', xy=v, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=2.5))
    ax.annotate('', xy=proj, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
    ax.plot([v[0], proj[0]], [v[1], proj[1]], 'g--', linewidth=2)

    # 直角标记
    n = np.array([-w_dir[1], w_dir[0]])
    s = 0.2
    ax.plot([proj[0]+s*n[0], proj[0]+s*n[0]+s*w_dir[0], proj[0]+s*w_dir[0]],
            [proj[1]+s*n[1], proj[1]+s*n[1]+s*w_dir[1], proj[1]+s*w_dir[1]],
            'k-', linewidth=0.8)

    ax.text(v[0]+0.15, v[1]+0.1, r'$v$', fontsize=13, color='#2c3e50', fontweight='bold')
    ax.text(proj[0]+0.1, proj[1]-0.4, r'$\operatorname{proj}_W(v)$', fontsize=11, color='#e74c3c')
    ax.text((v[0]+proj[0])/2+0.2, (v[1]+proj[1])/2, r'$v - \operatorname{proj}_W(v)$', fontsize=9, color='#27ae60')
    ax.text(3.5, 0.3, r'$W$', fontsize=12, color='blue')
    ax.text(-0.8, -0.7, r'$v - \operatorname{proj}_W(v) \perp W$', fontsize=9, color='gray')

    # (b) 最小距离原理
    ax = axes[1]
    ax.set_xlim(-1, 5); ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.set_title(r'$(b)$ 最小距离原理', fontsize=11)
    for i in range(-1, 6):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # 子空间
    t = np.linspace(-1, 5, 100)
    ax.plot(t*w_dir[0], t*w_dir[1], 'b-', alpha=0.2, linewidth=5)

    # 投影
    ax.annotate('', xy=proj, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))

    # v
    ax.annotate('', xy=v, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#2c3e50', lw=2.5))

    # 垂直距离（最短）
    ax.plot([v[0], proj[0]], [v[1], proj[1]], 'g-', linewidth=2)
    ax.text((v[0]+proj[0])/2+0.15, (v[1]+proj[1])/2, r'最短距离', fontsize=9, color='#27ae60')

    # 其他点（更远的距离）
    for offset in [-1.5, 2.5]:
        other = proj + offset * w_dir
        ax.plot([v[0], other[0]], [v[1], other[1]], 'r--', linewidth=1, alpha=0.5)
        ax.plot(other[0], other[1], 'ro', markersize=5, alpha=0.5)

    ax.text(v[0]+0.15, v[1]+0.1, r'$v$', fontsize=13, color='#2c3e50', fontweight='bold')
    ax.text(proj[0]+0.1, proj[1]-0.4, r'$\operatorname{proj}_W(v)$', fontsize=11, color='#e74c3c')
    ax.text(3.5, 0.3, r'$W$', fontsize=12, color='blue')
    ax.text(-0.8, -0.7, '投影是 $W$ 中离 $v$ 最近的点', fontsize=9, color='gray')

    fig.tight_layout()
    save_fig(fig, 'la-07-orthogonal-projection.svg')


# ============================================================
# 图8: 二次型的等高线
# ============================================================
def plot_quadratic_forms():
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    x = np.linspace(-3, 3, 200)
    y = np.linspace(-3, 3, 200)
    X, Y = np.meshgrid(x, y)

    # (a) 正定: x^2 + y^2
    ax = axes[0, 0]
    Z = X**2 + Y**2
    cs = ax.contour(X, Y, Z, levels=[0.5, 1, 2, 3, 5, 7], cmap='Reds')
    ax.clabel(cs, inline=True, fontsize=8)
    ax.set_aspect('equal')
    ax.set_title(r'$(a)$ 正定 $Q = x^2 + y^2$', fontsize=11)
    ax.set_xlabel(r'$x$'); ax.set_ylabel(r'$y$')

    # (b) 不定: x^2 - y^2 (鞍面)
    ax = axes[0, 1]
    Z = X**2 - Y**2
    cs = ax.contour(X, Y, Z, levels=[-4, -2, -1, 0, 1, 2, 4], cmap='coolwarm')
    ax.clabel(cs, inline=True, fontsize=8)
    ax.set_aspect('equal')
    ax.set_title(r'$(b)$ 不定 $Q = x^2 - y^2$（鞍点）', fontsize=11)

    # (c) 半正定: x^2
    ax = axes[0, 2]
    Z = X**2
    cs = ax.contour(X, Y, Z, levels=[0.25, 1, 2, 4, 6], cmap='Greens')
    ax.clabel(cs, inline=True, fontsize=8)
    ax.set_aspect('equal')
    ax.set_title(r'$(c)$ 半正定 $Q = x^2$（退化）', fontsize=11)

    # (d) 正定: 2x^2 + xy + 3y^2
    ax = axes[1, 0]
    Z = 2*X**2 + X*Y + 3*Y**2
    cs = ax.contour(X, Y, Z, levels=[1, 2, 4, 6, 10], cmap='Oranges')
    ax.clabel(cs, inline=True, fontsize=8)
    ax.set_aspect('equal')
    ax.set_title(r'$(d)$ 正定 $Q = 2x^2 + xy + 3y^2$', fontsize=11)

    # (e) 负定: -x^2 - y^2
    ax = axes[1, 1]
    Z = -X**2 - Y**2
    cs = ax.contour(X, Y, Z, levels=[-7, -5, -3, -1, -0.5], cmap='Blues_r')
    ax.clabel(cs, inline=True, fontsize=8)
    ax.set_aspect('equal')
    ax.set_title(r'$(e)$ 负定 $Q = -x^2 - y^2$', fontsize=11)

    # (f) 不定: xy
    ax = axes[1, 2]
    Z = X*Y
    cs = ax.contour(X, Y, Z, levels=[-4, -2, -1, 0, 1, 2, 4], cmap='PuOr')
    ax.clabel(cs, inline=True, fontsize=8)
    ax.set_aspect('equal')
    ax.set_title(r'$(f)$ 不定 $Q = xy$', fontsize=11)

    fig.tight_layout()
    save_fig(fig, 'la-08-quadratic-forms.svg')


# ============================================================
# 图9: 秩-零化度定理
# ============================================================
def plot_rank_nullity():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # (a) T: R^3 -> R^2, rank=2, nullity=1
    ax = axes[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_title(r'$(a)\;T:\mathbb{R}^3 \to \mathbb{R}^2$，秩=2，零化度=1', fontsize=11)

    # 左边 R^3
    ax.add_patch(plt.Rectangle((0.5, 1), 2.5, 4, fill=False, edgecolor='#3498db', linewidth=2))
    ax.text(1.75, 5.3, r'$\mathbb{R}^3$', fontsize=14, ha='center', color='#3498db', fontweight='bold')
    ax.text(1.75, 0.5, r'$\dim = 3$', fontsize=10, ha='center', color='gray')
    # 核
    ax.add_patch(plt.Rectangle((0.8, 2.5), 0.8, 1, fill=True, facecolor='#e74c3c', alpha=0.3, edgecolor='#e74c3c'))
    ax.text(1.2, 2.2, r'$\ker(T)$', fontsize=9, ha='center', color='#e74c3c')
    ax.text(1.2, 1.8, r'$\dim=1$', fontsize=8, ha='center', color='#e74c3c')

    # 箭头
    ax.annotate('', xy=(6, 3), xytext=(3.5, 3),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text(4.75, 3.3, r'$T$', fontsize=14, ha='center', fontweight='bold')

    # 右边 R^2
    ax.add_patch(plt.Rectangle((6.5, 1.5), 2, 3, fill=False, edgecolor='#2ecc71', linewidth=2))
    ax.text(7.5, 4.8, r'$\mathbb{R}^2$', fontsize=14, ha='center', color='#2ecc71', fontweight='bold')
    ax.text(7.5, 1.0, r'$\dim = 2$', fontsize=10, ha='center', color='gray')
    # 像
    ax.add_patch(plt.Rectangle((6.7, 1.8), 1.6, 2.4, fill=True, facecolor='#2ecc71', alpha=0.2, edgecolor='#2ecc71'))
    ax.text(7.5, 2.8, r'$\operatorname{im}(T)$', fontsize=9, ha='center', color='#2ecc71')
    ax.text(7.5, 2.3, r'$\dim=2$', fontsize=8, ha='center', color='#2ecc71')

    # 公式
    ax.text(5, 0.3, '零化度(1) + 秩(2) = dim(R³) = 3',
            fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='gray'))

    # (b) T: R^3 -> R^3, rank=1, nullity=2
    ax = axes[1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_title(r'$(b)\;T:\mathbb{R}^3 \to \mathbb{R}^3$，秩=1，零化度=2', fontsize=11)

    # 左边
    ax.add_patch(plt.Rectangle((0.5, 1), 2.5, 4, fill=False, edgecolor='#3498db', linewidth=2))
    ax.text(1.75, 5.3, r'$\mathbb{R}^3$', fontsize=14, ha='center', color='#3498db', fontweight='bold')
    ax.text(1.75, 0.5, r'$\dim = 3$', fontsize=10, ha='center', color='gray')
    ax.add_patch(plt.Rectangle((0.8, 2), 1.5, 2, fill=True, facecolor='#e74c3c', alpha=0.3, edgecolor='#e74c3c'))
    ax.text(1.55, 2.7, r'$\ker(T)$', fontsize=9, ha='center', color='#e74c3c')
    ax.text(1.55, 2.2, r'$\dim=2$', fontsize=8, ha='center', color='#e74c3c')

    # 箭头
    ax.annotate('', xy=(6, 3), xytext=(3.5, 3),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text(4.75, 3.3, r'$T$', fontsize=14, ha='center', fontweight='bold')

    # 右边
    ax.add_patch(plt.Rectangle((6.5, 1.5), 2, 3, fill=False, edgecolor='#2ecc71', linewidth=2))
    ax.text(7.5, 4.8, r'$\mathbb{R}^3$', fontsize=14, ha='center', color='#2ecc71', fontweight='bold')
    ax.text(7.5, 1.0, r'$\dim = 3$', fontsize=10, ha='center', color='gray')
    ax.add_patch(plt.Rectangle((7.2, 2.5), 0.6, 1, fill=True, facecolor='#2ecc71', alpha=0.3, edgecolor='#2ecc71'))
    ax.text(7.5, 2.2, r'$\operatorname{im}(T)$', fontsize=9, ha='center', color='#2ecc71')
    ax.text(7.5, 1.7, r'$\dim=1$', fontsize=8, ha='center', color='#2ecc71')

    ax.text(5, 0.3, '零化度(2) + 秩(1) = dim(R³) = 3',
            fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='gray'))

    fig.tight_layout()
    save_fig(fig, 'la-09-rank-nullity.svg')


# ============================================================
# 图10: 谱定理与对称矩阵
# ============================================================
def plot_spectral_theorem():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # (a) 对称矩阵 A = [[3, 1], [1, 3]] 的谱分解
    ax = axes[0]
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.set_title(r'$(a)\;A=(3,1;\,1,3)$ 的谱分解', fontsize=11)
    for i in range(-4, 5):
        ax.axhline(i, color='gray', alpha=0.1)
        ax.axvline(i, color='gray', alpha=0.1)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # 特征向量: lambda_1=4, u1=(1,1)/sqrt(2); lambda_2=2, u2=(1,-1)/sqrt(2)
    u1 = np.array([1, 1]) / np.sqrt(2)
    u2 = np.array([1, -1]) / np.sqrt(2)

    # 画特征方向
    t = np.linspace(-3, 3, 100)
    ax.plot(t*u1[0], t*u1[1], 'r-', alpha=0.15, linewidth=4)
    ax.plot(t*u2[0], t*u2[1], 'b-', alpha=0.15, linewidth=4)

    ax.annotate('', xy=u1*2.5, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5))
    ax.annotate('', xy=u2*2.5, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#3498db', lw=2.5))

    # 直角标记
    ax.plot([0.3*u1[0]+0.3*u2[0], 0.3*u1[0], 0.3*u2[0]],
            [0.3*u1[1]+0.3*u2[1], 0.3*u1[1], 0.3*u2[1]], 'k-', linewidth=1)

    ax.text(u1[0]*2.5+0.1, u1[1]*2.5+0.2, r'$u_1$（$\lambda_1=4$）', fontsize=10, color='#e74c3c')
    ax.text(u2[0]*2.5+0.1, u2[1]*2.5-0.4, r'$u_2$（$\lambda_2=2$）', fontsize=10, color='#3498db')
    ax.text(-3.5, -3.5, r'$A = 4u_1u_1^T + 2u_2u_2^T$', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='gray'))
    ax.text(-3.5, -3.0, '特征向量正交 → 可正交对角化', fontsize=9, color='gray')

    # (b) 二次型 x^T A x 的等高线与特征方向
    ax = axes[1]
    x = np.linspace(-3, 3, 200)
    y = np.linspace(-3, 3, 200)
    X, Y = np.meshgrid(x, y)
    # A = [[3,1],[1,3]], Q = 3x^2 + 2xy + 3y^2
    Z = 3*X**2 + 2*X*Y + 3*Y**2
    cs = ax.contour(X, Y, Z, levels=[1, 2, 4, 6, 8, 10], cmap='viridis')
    ax.clabel(cs, inline=True, fontsize=8)
    ax.set_aspect('equal')
    ax.set_title(r'$(b)\;Q = 3x^2 + 2xy + 3y^2$ 的等高线', fontsize=11)

    # 画特征方向
    ax.plot(t*u1[0], t*u1[1], 'r--', alpha=0.5, linewidth=1.5)
    ax.plot(t*u2[0], t*u2[1], 'b--', alpha=0.5, linewidth=1.5)
    ax.text(2.2, 2.5, r'$\lambda_1=4$ 方向（窄轴）', fontsize=9, color='#e74c3c')
    ax.text(2.2, -1.5, r'$\lambda_2=2$ 方向（宽轴）', fontsize=9, color='#3498db')
    ax.text(-2.8, -2.5, '等高线是椭圆\n主轴沿特征向量方向', fontsize=9, color='gray')

    fig.tight_layout()
    save_fig(fig, 'la-10-spectral-theorem.svg')


# ============================================================
# 运行所有绘图
# ============================================================
if __name__ == '__main__':
    print("生成线性代数可视化图形...")
    plot_vector_space_subspace()
    plot_span_linear_combination()
    plot_linear_transformations()
    plot_eigenvalues_eigenvectors()
    plot_determinant_geometry()
    plot_gram_schmidt()
    plot_orthogonal_projection()
    plot_quadratic_forms()
    plot_rank_nullity()
    plot_spectral_theorem()
    print("\n全部完成！")
