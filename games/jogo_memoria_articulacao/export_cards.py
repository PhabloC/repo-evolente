"""Crop articulation memory cards from the reference print and export webp assets."""

from __future__ import annotations

import os
from pathlib import Path

from PIL import Image

SRC = Path(
    r"C:\Users\phabl\.cursor\projects\c-Users-phabl-Desktop-projects-evolente\assets"
    r"\c__Users_phabl_AppData_Roaming_Cursor_User_workspaceStorage_50db123f289c7b34ea3f56694f02c4a8"
    r"_images_WhatsApp_Image_2026-08-04_at_21.22.22-7698d0f3-6ccc-4508-86bf-80f6455f57b9.png"
)
ROOT = Path(__file__).resolve().parent
MEDIO_DIR = ROOT / "medio"
DEBUG_DIR = ROOT / "_debug"

# Tuned for 1024x1024 collage: header + 4x4 cards with colored frames
HEADER = 198
MARGIN_L = 22
MARGIN_R = 22
MARGIN_B = 22
GAP_X = 8
GAP_Y = 8

CARDS = [
    ("lingua_para_cima", "Língua para cima", False),
    ("lingua_para_baixo", "Língua para baixo", False),
    ("lingua_para_direita", "Língua para a direita", False),
    ("lingua_para_esquerda", "Língua para a esquerda", False),
    ("empurrar_as_bochechas", "Empurrar as bochechas", False),
    ("segurar_canudo_labios", "Segurar um canudo com os lábios", True),
    ("assoprar_bolinha_algodao", "Assoprar bolinha de algodão até o alvo", True),
    ("estalos_com_a_lingua", "Estalos com a língua (toc-toc)", False),
    ("lingua_em_circulos", "Língua em círculos ao redor dos lábios", False),
    ("alternar_sorriso_biquinho", "Alternar sorriso e biquinho", False),
    ("assoprar_5_segundos", "Assoprar mantendo o ar por 5 segundos", False),
    ("lingua_nos_cantos", "Língua nos cantos da boca", False),
    ("lamber_os_labios", "Lamber os lábios", False),
    ("abrir_bem_a_boca", "Abrir bem a boca", False),
    ("repetir_silabas_pa_ta_ka", "Repetir sílabas PA - TA - KA", False),
    ("repetir_palavras_pato_bola_gato", "Repetir palavras (pato, bola, gato)", False),
]


def cell_box(im: Image.Image, row: int, col: int) -> tuple[int, int, int, int]:
    grid_top = HEADER
    grid_bottom = im.height - MARGIN_B
    grid_left = MARGIN_L
    grid_right = im.width - MARGIN_R
    cell_w = (grid_right - grid_left - 3 * GAP_X) / 4
    cell_h = (grid_bottom - grid_top - 3 * GAP_Y) / 4
    x0 = int(round(grid_left + col * (cell_w + GAP_X)))
    y0 = int(round(grid_top + row * (cell_h + GAP_Y)))
    x1 = int(round(x0 + cell_w))
    y1 = int(round(y0 + cell_h))
    return x0, y0, x1, y1


def main() -> None:
    im = Image.open(SRC).convert("RGB")
    MEDIO_DIR.mkdir(parents=True, exist_ok=True)
    DEBUG_DIR.mkdir(parents=True, exist_ok=True)

    # Full print as cover/reference
    im.save(ROOT / "capa_jogo_memoria_articulacao.webp", "WEBP", quality=90)
    im.crop((0, 0, im.width, HEADER + 20)).save(
        ROOT / "capa-modal-jogo-memoria-articulacao.webp", "WEBP", quality=90
    )

    for index, (card_id, _label, _material) in enumerate(CARDS):
        row, col = divmod(index, 4)
        box = cell_box(im, row, col)
        card = im.crop(box)
        # Normalize to square-ish card for game board
        side = max(card.size)
        canvas = Image.new("RGB", (side, side), (255, 255, 255))
        ox = (side - card.size[0]) // 2
        oy = (side - card.size[1]) // 2
        canvas.paste(card, (ox, oy))
        out = MEDIO_DIR / f"{card_id}.webp"
        canvas.save(out, "WEBP", quality=92)
        card.save(DEBUG_DIR / f"{index + 1:02d}_{card_id}.png")
        print(f"saved {out.name} from {box}")

    print("done", len(CARDS), "cards")


if __name__ == "__main__":
    main()
