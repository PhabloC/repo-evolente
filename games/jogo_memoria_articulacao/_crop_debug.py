from PIL import Image, ImageDraw
import os

src = r"C:\Users\phabl\.cursor\projects\c-Users-phabl-Desktop-projects-evolente\assets\c__Users_phabl_AppData_Roaming_Cursor_User_workspaceStorage_50db123f289c7b34ea3f56694f02c4a8_images_WhatsApp_Image_2026-08-04_at_21.22.22-7698d0f3-6ccc-4508-86bf-80f6455f57b9.png"
im = Image.open(src)
out_dir = os.path.dirname(__file__)
debug_dir = os.path.join(out_dir, "_debug")
os.makedirs(debug_dir, exist_ok=True)

# Heuristic for 1024x1024 collage with header
header = 210
margin_l, margin_r, margin_b = 28, 28, 28
gap = 10
grid_top = header
grid_bottom = im.height - margin_b
grid_left = margin_l
grid_right = im.width - margin_r
cell_w = (grid_right - grid_left - 3 * gap) / 4
cell_h = (grid_bottom - grid_top - 3 * gap) / 4
print("cell", cell_w, cell_h)

ann = im.copy()
d = ImageDraw.Draw(ann)
for r in range(4):
    for c in range(4):
        x0 = grid_left + c * (cell_w + gap)
        y0 = grid_top + r * (cell_h + gap)
        x1 = x0 + cell_w
        y1 = y0 + cell_h
        d.rectangle([x0, y0, x1, y1], outline=(255, 0, 0), width=2)
        d.text((x0 + 4, y0 + 4), str(r * 4 + c + 1), fill=(255, 0, 0))
ann.save(os.path.join(debug_dir, "grid_guess.png"))
print("saved", os.path.join(debug_dir, "grid_guess.png"))
