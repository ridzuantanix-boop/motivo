"""Optional documentation contact sheet. Requires Pillow, not used by runtime/setup."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]


def font(size, bold=False):
    names = [f'C:/Windows/Fonts/arial{"bd" if bold else ""}.ttf', 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf']
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    source = (ROOT/'src/gallery-data.ts').read_text(encoding='utf-8')
    items = json.loads(source.split('export const gallery = ',1)[1].rsplit(' as const;',1)[0])
    image = Image.new('RGB',(1800,1720),'#eee9df')
    draw = ImageDraw.Draw(image)
    draw.text((48,28),'MOTIVO / PILIH ARAH VISUAL',font=font(22,True),fill='#284436')
    draw.text((44,66),'12 CARA BERCERITA.',font=font(76,True),fill='#202a23')
    draw.text((48,158),'Poster konsep asli. Klik galeri untuk lihat setiap poster dengan lebih dekat.',font=font(24),fill='#536052')
    for i,item in enumerate(items):
        x,y = 48+(i%3)*576, 225+(i//3)*354
        draw.text((x,y),f'{item["id"]:02d} / {item["label"]}',font=font(19,True),fill='#263c2e')
        with Image.open(ROOT/'docs/gallery'/item['preview']) as art:
            image.paste(art.resize((552,311),Image.Resampling.LANCZOS),(x,y+30))
    draw.line((48,1662,1752,1662),fill='#9eaa99',width=1)
    draw.text((48,1678),'KONSEP VISUAL / BUKAN FRAME VIDEO SIAP',font=font(17),fill='#536052')
    draw.text((1580,1678),'by Pawarna',font=font(20,True),fill='#263c2e')
    out=ROOT/'docs/gallery/overview.jpg'
    image.save(out,quality=92,optimize=True)
    print(out)


if __name__=='__main__':
    main()
