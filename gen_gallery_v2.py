"""Generate gallery HTML and JS with new hierarchy from 个人作品集2."""
import os, sys, json

BASE = "D:/work buddy/2026-06-23-16-20-24/images"

# Define the new hierarchy: (gallery_key, section_title, tag_class, sub_sections)
# Each sub_section: (label, folder_path, thumb_type)
HIERARCHY = [
    ("promo", "品牌宣传视觉", "promo", [
        ("海报类", "brand-promo/1-海报类", "tall"),
        ("杂志类", "brand-promo/2-杂志类", "tall"),
        ("公众号类", "brand-promo/3-公众号类", "wide"),
        ("文创类", "brand-promo/4-文创类", "wide"),
    ]),
    ("events", "品牌活动视觉", "events", [
        ("品牌活动视觉", "brand-events", "sq"),
    ]),
    ("exhibit", "展会视觉", "exhibit", [
        ("2025年风能展 · 价值共生，可靠同行", "exhibition/1-2025风能展", "sq"),
        ("2024年风能展 · 全生命周期安全可靠", "exhibition/2-2024风能展", "sq"),
        ("2023年风能展 · 十五年 更可靠", "exhibition/3-2023风能展", "sq"),
        ("2022年德国汉堡展", "exhibition/4-2022汉堡展", "sq"),
    ]),
]

def get_files(folder_rel):
    folder = os.path.join(BASE, folder_rel)
    if not os.path.isdir(folder):
        return []
    files = sorted([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
    return [f"images/{folder_rel}/{f}" for f in files]

# Generate HTML gallery sections
html_lines = []
js_galleries = {}

gallery_index = 0  # global index per gallery

for gallery_key, section_title, tag_class, sub_sections in HIERARCHY:
    total_images = 0
    all_image_paths = []
    
    for sub_label, folder_rel, thumb_type in sub_sections:
        files = get_files(folder_rel)
        all_image_paths.extend(files)
    
    total_images = len(all_image_paths)
    
    # Section header
    html_lines.append(f'    <!-- ===== {section_title} ===== -->')
    html_lines.append(f'    <div class="gallery-section reveal reveal-delay-1">')
    html_lines.append(f'      <div class="gallery-section-title">')
    html_lines.append(f'        <span class="tag {tag_class}">{section_title}</span>')
    html_lines.append(f'        {total_images} 张作品')
    html_lines.append(f'      </div>')
    
    # Per sub-section
    running_idx = 0
    for sub_label, folder_rel, thumb_type in sub_sections:
        files = get_files(folder_rel)
        if not files:
            continue
        
        # Sub-category label
        if len(sub_sections) > 1:
            html_lines.append(f'      <div class="gallery-sub-label">{sub_label} · {len(files)} 张</div>')
        
        html_lines.append(f'      <div class="gallery-strip">')
        for f in files:
            fname = os.path.basename(f)
            # Clean caption
            caption = fname.rsplit('.', 1)[0]
            caption = caption.replace('_', ' ').strip()
            # Shorten long names
            if len(caption) > 30:
                caption = caption[:28] + '…'
            
            html_lines.append(f'        <div class="gallery-thumb {thumb_type}" data-gallery="{gallery_key}" data-index="{running_idx}"><img src="{f}" loading="lazy" alt="{caption}"><div class="thumb-caption">{sub_label if len(sub_sections) > 1 else section_title} · {caption}</div></div>')
            running_idx += 1
        
        html_lines.append(f'      </div>')
    
    html_lines.append(f'    </div>')
    html_lines.append('')
    
    # Store for JS
    js_galleries[gallery_key] = {
        "title": section_title,
        "images": all_image_paths
    }

# Output
print("=== HTML START ===")
print("\n".join(html_lines))
print("=== HTML END ===")
print("=== JS START ===")
print(f"const galleryData = {json.dumps(js_galleries, ensure_ascii=False, indent=2)};")
print("=== JS END ===")
