"""Optional one-off image pipeline (not needed to build or serve the site).

Crops the three source photographs into the art-directed variants used by
src/template.html and writes WebP + progressive JPEG files to assets/img/.
Requires Pillow and the `cwebp` binary. Usage:

    python3 tools/prepare_images.py <dir-with-originals>

Expected originals (3200 px wide, see assets/img/CREDITS.md):
    sea_clean.jpg      hero, Unsplash jOyBc3XkbP0 (roadside tape and sign retouched out)
    detail_clean.jpg   terms split, Unsplash jFgKMQbTA30 (engraved wordmark retouched out)
    night.jpg          closing call to action, Unsplash ad_d3szUkd0
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image

OUT = Path(__file__).resolve().parent.parent / "assets" / "img"

# name: (source, crop box (left, top, right, bottom), output widths)
VARIANTS = {
    "hero-wide": ("sea_clean.jpg", (0, 950, 3200, 2300), (1280, 1920, 2560, 3200)),
    "hero-band": ("sea_clean.jpg", (700, 1080, 2500, 2092), (640, 960, 1280, 1600)),
    "detail": ("detail_clean.jpg", (650, 0, 2350, 2125), (480, 800, 1200, 1600)),
    "night": ("night.jpg", (0, 300, 3200, 1600), (800, 1280, 1920, 2560)),
}


def main(src_dir: Path) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (source, box, widths) in VARIANTS.items():
        image = Image.open(src_dir / source).convert("RGB").crop(box)
        for width in widths:
            height = round(image.height * width / image.width)
            resized = image.resize((width, height), Image.LANCZOS)
            jpg = OUT / f"{name}-{width}.jpg"
            # The hero is the LCP image: cloud texture tolerates stronger compression.
            quality = 64 if name == "hero-wide" else 74
            resized.save(jpg, "JPEG", quality=quality, optimize=True, progressive=True)
            subprocess.run(
                ["cwebp", "-quiet", "-q", str(quality - 4), "-m", "6", str(jpg), "-o", str(jpg.with_suffix(".webp"))],
                check=True,
            )
            print(f"{jpg.name:28} {width}x{height}")
    og = Image.open(src_dir / "sea_clean.jpg").convert("RGB").crop((0, 640, 3200, 2320)).resize((1200, 630), Image.LANCZOS)
    og.save(OUT / "og-image.jpg", "JPEG", quality=82, optimize=True, progressive=True)
    print("og-image.jpg                 1200x630")


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "."))
