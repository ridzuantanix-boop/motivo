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
    image = Image.new('RGB',(1800,1900),'#eee9df')
    draw = ImageDraw.Draw(image)
    draw.text((48,28),'MOTIVO / CONTOH JENIS VIDEO',font=font(22,True),fill='#284436')
    draw.text((44,66),'TENGOK. TERUS FAHAM.',font=font(70,True),fill='#202a23')
    draw.text((48,158),'12 contoh adegan. Pilih nombor atau ceritakan idea anda.',font=font(26),fill='#536052')
    for i,item in enumerate(items):
        x,y = 48+(i%3)*576, 225+(i//3)*395
        draw.text((x,y),f'{item["id"]:02d} / {item["label"]}',font=font(19,True),fill='#263c2e')
        with Image.open(ROOT/'docs/gallery'/item['preview']) as art:
            image.paste(art.resize((552,311),Image.Resampling.LANCZOS),(x,y+30))
        words=item['summary'].split()
        row=''
        rows=[]
        for word in words:
            candidate=(row+' '+word).strip()
            if draw.textbbox((0,0),candidate,font=font(19))[2]>548 and row:
                rows.append(row)
                row=word
            else:
                row=candidate
        rows.append(row)
        draw.multiline_text((x,y+349),'\n'.join(rows),font=font(19),fill='#435141',spacing=3)
    draw.line((48,1832,1752,1832),fill='#9eaa99',width=1)
    draw.text((48,1852),'GAMBAR CONTOH DIJANA AI / BUKAN KLIP VIDEO SIAP',font=font(18),fill='#536052')
    draw.text((1580,1852),'by Pawarna',font=font(20,True),fill='#263c2e')
    out=ROOT/'docs/gallery/overview.jpg'
    image.save(out,quality=92,optimize=True)
    print(out)


if __name__=='__main__':
    main()
