# -*- coding: utf-8 -*-
"""第16级-解析几何 三维图形生成脚本（空间曲面、曲线、向量代数）"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D

# 注册中文字体
_cjk = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fm.fontManager.addfont(_cjk)
_fp = fm.FontProperties(fname=_cjk)
plt.rcParams['font.sans-serif'] = [_fp.get_name()] + plt.rcParams.get('font.sans-serif', [])
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams.update({'figure.dpi': 150, 'font.size': 9,
                     'axes.titlesize': 11, 'axes.labelsize': 9})


def save(fig, name):
    fig.savefig(name, bbox_inches='tight')
    plt.close(fig)
    print('saved', name)


def setup_ax(ax, title, lim=3):
    ax.set_box_aspect((1, 1, 1))
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    ax.xaxis.pane.set_alpha(0.0); ax.yaxis.pane.set_alpha(0.0); ax.zaxis.pane.set_alpha(0.0)


# ---------- 图1：空间直角坐标系 ----------
fig = plt.figure(figsize=(4.5, 4.2))
ax = fig.add_subplot(111, projection='3d')
for coords, col in [('x', 'C0'), ('y', 'C1'), ('z', 'C2')]:
    ax.quiver(0, 0, 0, *[(1 if c == coords else 0) for c in 'xyz'], color=col, arrow_length_ratio=0.1, lw=2)
ax.text(1.15, 0, 0, 'x', color='C0'); ax.text(0, 1.2, 0, 'y', color='C1'); ax.text(0, 0, 1.2, 'z', color='C2')
ax.scatter([1, 1, 1], [1, 1, 1], [1, 1, 1], color='C0')
ax.text(1.05, 1.05, 1.1, 'P(1,1,1)', color='k')
setup_ax(ax, '空间直角坐标系：三个互相垂直的轴', 1.5)
save(fig, 'geo-01-axis.svg')


# ---------- 图2：柱面（圆柱、椭圆、抛物柱） ----------
theta = np.linspace(0, 2*np.pi, 60)
# 圆柱面
fig = plt.figure(figsize=(8, 3.2))
ax = fig.add_subplot(131, projection='3d')
u = np.linspace(0, 2*np.pi, 60); v = np.linspace(-2, 2, 30)
X = np.outer(np.cos(u), np.ones_like(v)); Y = np.outer(np.sin(u), np.ones_like(v)); Z = np.outer(np.ones_like(u), v)
ax.plot_surface(X, Y, Z, alpha=0.6, color='C0', rstride=1, cstride=1)
setup_ax(ax, '圆柱面 $x^2+y^2=1$', 2.2)
# 椭圆柱面
ax = fig.add_subplot(132, projection='3d')
X = np.outer(1.5*np.cos(u), np.ones_like(v)); Y = np.outer(1.0*np.sin(u), np.ones_like(v)); Z = np.outer(np.ones_like(u), v)
ax.plot_surface(X, Y, Z, alpha=0.6, color='C1')
setup_ax(ax, '椭圆柱面 $x^2/1.5^2+y^2=1$', 2.2)
# 抛物柱面
ax = fig.add_subplot(133, projection='3d')
x = np.linspace(-2, 2, 40); z = np.linspace(-2, 2, 30)
X, Z = np.meshgrid(x, z); Y = X**2
ax.plot_surface(X, Y, Z, alpha=0.6, color='C2')
setup_ax(ax, '抛物柱面 $y=x^2$', 2.2)
save(fig, 'geo-02-cylinder.svg')


# ---------- 图3：椭球面 ----------
fig = plt.figure(figsize=(4.5, 4.2))
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, np.pi, 40); v = np.linspace(0, 2*np.pi, 60)
a, b, c = 2.0, 1.2, 0.8
X = a*np.outer(np.sin(u), np.cos(v)); Y = b*np.outer(np.sin(u), np.sin(v)); Z = c*np.outer(np.cos(u), np.ones_like(v))
ax.plot_surface(X, Y, Z, alpha=0.7, color='C3', rstride=1, cstride=1)
setup_ax(ax, '椭球面 $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}+\\frac{z^2}{c^2}=1$', 2.3)
save(fig, 'geo-03-ellipsoid.svg')


# ---------- 图4：单叶/双叶双曲面 ----------
fig = plt.figure(figsize=(8, 3.8))
# 单叶双曲面
ax = fig.add_subplot(121, projection='3d')
u = np.linspace(-1.5, 1.5, 40); v = np.linspace(0, 2*np.pi, 50)
U, V = np.meshgrid(u, v)
X = np.cosh(U)*np.cos(V); Y = np.cosh(U)*np.sin(V); Z = np.sinh(U)
ax.plot_surface(X, Y, Z, alpha=0.7, color='C4', rstride=1, cstride=1)
setup_ax(ax, '单叶双曲面 $x^2+y^2-z^2=1$', 2.3)
# 双叶双曲面
ax = fig.add_subplot(122, projection='3d')
u = np.linspace(0.4, 1.6, 30); v = np.linspace(0, 2*np.pi, 50)
U, V = np.meshgrid(u, v)
X = np.sinh(U)*np.cos(V); Y = np.sinh(U)*np.sin(V)
Zpos = np.cosh(U); Zneg = -np.cosh(U)
ax.plot_surface(X, Y, Zpos, alpha=0.7, color='C5', rstride=1, cstride=1)
ax.plot_surface(X, Y, Zneg, alpha=0.7, color='C5', rstride=1, cstride=1)
setup_ax(ax, '双叶双曲面 $x^2+y^2-z^2=-1$', 2.3)
save(fig, 'geo-04-hyperboloids.svg')


# ---------- 图5：抛物面（椭圆/双曲） ----------
fig = plt.figure(figsize=(8, 3.8))
x = np.linspace(-2, 2, 50); y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
# 椭圆抛物面
ax = fig.add_subplot(121, projection='3d')
Z = (X**2/4 + Y**2/1)
Z = np.clip(Z, -2, 2)
ax.plot_surface(X, Y, Z, alpha=0.7, color='C6')
setup_ax(ax, '椭圆抛物面 $z=x^2/4+y^2$', 2.3)
# 双曲抛物面（马鞍面）
ax = fig.add_subplot(122, projection='3d')
Z = (X**2/4 - Y**2/1)
Z = np.clip(Z, -2, 2)
ax.plot_surface(X, Y, Z, alpha=0.7, color='C7')
setup_ax(ax, '双曲抛物面 $z=x^2/4-y^2$（马鞍面）', 2.3)
save(fig, 'geo-05-paraboloids.svg')


# ---------- 图6：二次锥面 ----------
fig = plt.figure(figsize=(4.5, 4.2))
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(-1.5, 1.5, 40); v = np.linspace(0, 2*np.pi, 60)
U, V = np.meshgrid(u, v)
X = U*np.cos(V); Y = U*np.sin(V); Z = U
ax.plot_surface(X, Y, Z, alpha=0.7, color='C6', rstride=1, cstride=1)
ax.plot_surface(X, Y, -Z, alpha=0.7, color='C6', rstride=1, cstride=1)
setup_ax(ax, '二次锥面 $x^2+y^2=z^2$', 2.0)
save(fig, 'geo-06-cone.svg')


# ---------- 图7：二次曲面分类总览 ----------
fig = plt.figure(figsize=(12, 8))
u = np.linspace(0, np.pi, 30); v = np.linspace(0, 2*np.pi, 50)
U, V = np.meshgrid(u, v)
def ellipsoid(ax):
    X = 1.5*np.outer(np.sin(U), np.cos(V)); Y = 1.0*np.outer(np.sin(U), np.sin(V)); Z = 0.8*np.outer(np.cos(U), np.ones_like(V))
    ax.plot_surface(X, Y, Z, alpha=0.7, color='C0')
def hyper1(ax):
    u = np.linspace(-1.2, 1.2, 25); v = np.linspace(0, 2*np.pi, 40)
    U, V = np.meshgrid(u, v)
    ax.plot_surface(np.cosh(U)*np.cos(V), np.cosh(U)*np.sin(V), np.sinh(U), alpha=0.7, color='C1')
def hyper2(ax):
    u = np.linspace(0.4, 1.3, 22); v = np.linspace(0, 2*np.pi, 40)
    U, V = np.meshgrid(u, v)
    for s in (1, -1):
        ax.plot_surface(np.sinh(U)*np.cos(V), np.sinh(U)*np.sin(V), s*np.cosh(U), alpha=0.7, color='C2')
def el_par(ax):
    x = np.linspace(-1.6, 1.6, 35); y = np.linspace(-1.6, 1.6, 35)
    X, Y = np.meshgrid(x, y); Z = np.clip(X**2/2 + Y**2, 0, 1.8)
    ax.plot_surface(X, Y, Z, alpha=0.7, color='C3')
def hy_par(ax):
    x = np.linspace(-1.6, 1.6, 35); y = np.linspace(-1.6, 1.6, 35)
    X, Y = np.meshgrid(x, y); Z = np.clip((X**2 - Y**2)/2, -1.8, 1.8)
    ax.plot_surface(X, Y, Z, alpha=0.7, color='C4')
def cone(ax):
    u = np.linspace(-1.3, 1.3, 25); v = np.linspace(0, 2*np.pi, 40)
    U, V = np.meshgrid(u, v)
    for s in (1, -1):
        ax.plot_surface(U*np.cos(V), U*np.sin(V), s*U, alpha=0.7, color='C5')
titles = ['椭球面', '单叶双曲面', '双叶双曲面', '椭圆抛物面', '双曲抛物面', '二次锥面']
fns = [ellipsoid, hyper1, hyper2, el_par, hy_par, cone]
for i, (fn, t) in enumerate(zip(fns, titles)):
    ax = fig.add_subplot(2, 3, i+1, projection='3d')
    fn(ax); setup_ax(ax, t, 2.0)
fig.suptitle('六种标准二次曲面', fontsize=13)
save(fig, 'geo-07-quadrics-overview.svg')


# ---------- 图8：空间曲线（螺旋线 + 切线向量） ----------
fig = plt.figure(figsize=(4.8, 4.4))
ax = fig.add_subplot(111, projection='3d')
t = np.linspace(0, 4*np.pi, 300)
X = np.cos(t); Y = np.sin(t); Z = 0.4*t
ax.plot(X, Y, Z, lw=2, color='C6')
# 切线向量
t0 = 1.5
v = np.array([-np.sin(t0), np.cos(t0), 0.4])
ax.quiver(np.cos(t0), np.sin(t0), 0.4*t0, *v, color='C1', arrow_length_ratio=0.2, lw=2)
ax.text(np.cos(t0)+0.2, np.sin(t0), 0.4*t0+0.3, '切线向量 r\'(t)', color='C1')
setup_ax(ax, '螺旋线 $x=\\cos t, y=\\sin t, z=0.4t$ 及其切线', 3.0)
save(fig, 'geo-08-curve-tangent.svg')


# ---------- 图9：向量点积（投影） ----------
fig = plt.figure(figsize=(4.8, 4.4))
ax = fig.add_subplot(111, projection='3d')
a = np.array([1.6, 1.2, 0.8]); b = np.array([2.4, 0.4, 0.0])
ax.quiver(0, 0, 0, *a, color='C0', arrow_length_ratio=0.1, lw=2.5)
ax.quiver(0, 0, 0, *b, color='C1', arrow_length_ratio=0.1, lw=2.5)
# 投影
proj = (np.dot(a, b)/np.dot(b, b))*b
ax.quiver(0, 0, 0, *proj, color='C2', arrow_length_ratio=0.1, lw=2)
ax.plot([a[0], proj[0]], [a[1], proj[1]], [a[2], proj[2]], 'k--', lw=1)
ax.scatter(*a, color='C0'); ax.scatter(*b, color='C1')
ax.text(*a*1.1, 'a', color='C0'); ax.text(*b*1.1, 'b', color='C1'); ax.text(*proj*1.1+0.1, '投影', color='C2')
setup_ax(ax, '点积：a·b = |b|·(a在b上的投影长)', 3.0)
save(fig, 'geo-09-dot-product.svg')


# ---------- 图10：向量叉积（右手系 + 平行四边形面积） ----------
fig = plt.figure(figsize=(4.8, 4.4))
ax = fig.add_subplot(111, projection='3d')
a = np.array([1.8, 0.6, 0.2]); b = np.array([0.4, 1.6, 0.3])
cross = np.cross(a, b)
ax.quiver(0, 0, 0, *a, color='C0', arrow_length_ratio=0.1, lw=2.5)
ax.quiver(0, 0, 0, *b, color='C1', arrow_length_ratio=0.1, lw=2.5)
ax.quiver(0, 0, 0, *cross, color='C3', arrow_length_ratio=0.15, lw=2.5)
# 平行四边形
ax.plot([0, a[0], a[0]+b[0], b[0], 0], [0, a[1], a[1]+b[1], b[1], 0], [0, a[2], a[2]+b[2], b[2], 0], 'k-', lw=1)
ax.text(*(a*0.9), 'a', color='C0'); ax.text(*(b*0.9), 'b', color='C1'); ax.text(*(cross*1.1), 'a×b', color='C3')
setup_ax(ax, '叉积：|a×b| = 平行四边形面积，方向垂直', 3.0)
save(fig, 'geo-10-cross-product.svg')


# ---------- 图11：混合积（平行六面体体积） ----------
fig = plt.figure(figsize=(4.8, 4.4))
ax = fig.add_subplot(111, projection='3d')
a = np.array([1.8, 0.4, 0.2]); b = np.array([0.4, 1.6, 0.3]); c = np.array([0.3, 0.5, 1.6])
ax.quiver(0, 0, 0, *a, color='C0', arrow_length_ratio=0.1, lw=2.5)
ax.quiver(0, 0, 0, *b, color='C1', arrow_length_ratio=0.1, lw=2.5)
ax.quiver(0, 0, 0, *c, color='C2', arrow_length_ratio=0.1, lw=2.5)
# 平行六面体 8 个顶点
verts = [i*a + j*b + k*c for i in range(2) for j in range(2) for k in range(2)]
for i in range(2):
    for j in range(2):
        for k in range(2):
            p = i*a + j*b + k*c
            ax.scatter(*p, color='k', s=8)
# 边
edges = [(0,1),(0,2),(0,4),(3,1),(3,2),(3,7),(5,1),(5,4),(5,7),(6,2),(6,4),(6,7)]
for e in edges:
    ax.plot(*zip(verts[e[0]], verts[e[1]]), 'k-', lw=0.8)
ax.text(*(a*1.1), 'a', color='C0'); ax.text(*(b*1.1), 'b', color='C1'); ax.text(*(c*1.1), 'c', color='C2')
ax.text(0.2, 1.2, 1.3, 'V=|a·(b×c)|', color='k')
setup_ax(ax, '混合积：体积 = |a·(b×c)|', 2.6)
save(fig, 'geo-11-triple-product.svg')

print('ALL DONE')