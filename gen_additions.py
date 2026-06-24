#!/usr/bin/env python3
"""Scan 文创类 and 2023风能展 directories, generate HTML + JS snippets for index.html additions."""

import os
import re

# Respect CJK + digit natural sort
def natural_key(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]

# ==================== 文创类 ====================
wenchuang_dir = r"D:\work buddy\2026-06-23-16-20-24\images\brand-promo\4-文创类"
wenchuang_files = sorted(os.listdir(wenchuang_dir), key=natural_key)
print(f"文创类 files ({len(wenchuang_files)}):")
for f in wenchuang_files:
    print(f"  {f}")

print("\n--- HTML snippet (data-index starts at 40) ---")
base_idx = 40
for i, f in enumerate(wenchuang_files):
    idx = base_idx + i
    name_no_ext = os.path.splitext(f)[0]
    # Decide class: wide for 产品手册/画册/包装, normal for others
    is_wide = any(k in f for k in ['手册', '画册', '包装', '扑克牌', '衣服'])
    cls = 'gallery-thumb wide' if is_wide else 'gallery-thumb'
    print(f'        <div class="{cls}" data-gallery="promo" data-index="{idx}"><img src="images/brand-promo/4-文创类/{f}" loading="lazy" alt="{name_no_ext}"><div class="thumb-caption">文创类 · {name_no_ext}</div></div>')

print("\n--- JS paths ---")
for f in wenchuang_files:
    print(f'      "images/brand-promo/4-文创类/{f}",')

# ==================== 2023风能展 ====================
print("\n\n===========================================")
expo2023_dir = r"D:\work buddy\2026-06-23-16-20-24\images\exhibition\3-2023风能展"
expo2023_files = sorted(os.listdir(expo2023_dir), key=natural_key)
print(f"2023风能展 files ({len(expo2023_files)}):")
for f in expo2023_files:
    print(f"  {f}")

print("\n--- HTML snippet (data-index starts at 19) ---")
base_idx_expo = 19
for i, f in enumerate(expo2023_files):
    idx = base_idx_expo + i
    name_no_ext = os.path.splitext(f)[0]
    print(f'        <div class="gallery-thumb" data-gallery="exhibit" data-index="{idx}"><img src="images/exhibition/3-2023风能展/{f}" loading="lazy" alt="{name_no_ext}"><div class="thumb-caption">2023年风能展 · 十五年 更可靠 · {name_no_ext}</div></div>')

print("\n--- JS paths ---")
for f in expo2023_files:
    print(f'      "images/exhibition/3-2023风能展/{f}",')
