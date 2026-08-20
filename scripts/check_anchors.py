#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查「数学公理体系与定理依赖关系」下所有 md 文件是否都包含
认知锚点：> **一句话大白话**：... 与 > **小例子**：...

用法:
    python3 check_anchors.py [根目录路径]
    若不传路径, 默认检查本文件上级目录下的 src/数学公理体系与定理依赖关系

输出:
    - 每个缺失锚点的文件列表（按大目录分组）
    - 总结统计: 总数 / 含大白话数 / 含小例子数 / 缺失数
退出码:
    0 = 全部通过; 1 = 存在缺失
"""

import os
import sys

BLOCK_DAHU = "一句话大白话"
BLOCK_EXAMPLE = "小例子"
MISSING_DAHU_LINE = "> **一句话大白话**："
MISSING_EXAMPLE_LINE = "> **小例子**："


def default_root():
    """定位脚本仓库里的数学公理体系根目录。"""
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(here, "src", "数学公理体系与定理依赖关系")
    if os.path.isdir(candidate):
        return candidate
    # 兜底: 向上找 src
    for parent in [here, os.path.dirname(here)]:
        c = os.path.join(parent, "src", "数学公理体系与定理依赖关系")
        if os.path.isdir(c):
            return c
    return None


def iter_md_files(root):
    """递归产出所有 .md 文件(绝对路径), 跳过 README.md。"""
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in sorted(filenames):
            if fn.lower() == "readme.md":
                continue
            if fn.lower().endswith(".md"):
                yield os.path.join(dirpath, fn)


def check_file(path):
    """返回 (行号阴, 只报 bool 缺失情况): (missing_dahu: bool, missing_example: bool)"""
    # 用索引 0 高亮。
    try:
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
    except (OSError, UnicodeDecodeError) as exc:
        return ("ERROR", str(exc))
    has_dahu = BLOCK_DAHU in text
    has_example = BLOCK_EXAMPLE in text
    return (not has_dahu, not has_example)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else default_root()
    if not root or not os.path.isdir(root):
        print(f"找不到根目录: {root}")
        return 2

    total = 0
    dahu_ok = 0
    example_ok = 0
    missing = []

    for path in iter_md_files(root):
        total += 1
        res = check_file(path)
        if isinstance(res, str):
            rel = os.path.relpath(path, root)
            missing.append((rel, res, ""))
            continue
        miss_dahu, miss_example = res
        if not miss_dahu:
            dahu_ok += 1
        if not miss_example:
            example_ok += 1
        # 归类
        rel = os.path.relpath(path, root)
        top = os.path.dirname(rel)
        if miss_dahu or miss_example:
            # 记录缺失详情
            reasons = []
            if miss_dahu:
                reasons.append("缺『一句话大白话』")
            if miss_example:
                reasons.append("缺『小例子』")
            missing.append((top, rel, "; ".join(reasons)))

    # 输出
    missing_sorted = sorted(missing, key=lambda x: (x[0], x[1]))
    if missing_sorted:
        print("=" * 60)
        print("缺少认知锚点的文件 (共 %d 个)" % len(missing_sorted))
        print("=" * 60)
        cur = None
        for top, rel, reason in missing_sorted:
            if top != cur:
                cur = top
                print(f"\n[{cur}]")
            print(f"  - {os.path.basename(rel)}  ->  {reason}")

    print("\n" + "=" * 60)
    print("汇总统计")
    print("=" * 60)
    print(f"检查总数(非README .md) : {total}")
    print(f"含『一句话大白话』     : {dahu_ok}")
    print(f"含『小例子』           : {example_ok}")
    print(f"缺失件数               : {len(missing)}")

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())