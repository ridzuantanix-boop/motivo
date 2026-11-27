"""Optional Pillow documentation board from actual inspect:clean PNGs, not a mockup."""
from pathlib import Path
from PIL import Image, ImageDraw
from gallery_contact import font

ROOT=Path(__file__).resolve().parents[1]


def main():
    source=ROOT/'out/clean-ci'
    image=Image.new('RGB',(1080,1500),'#eee9df')
    draw=ImageDraw.Draw(image)
    draw.text((48,28),'MOTIVO / FRAME DEMO',font=font(22,True),fill='#304337')
    draw.text((44,72),'VISUAL DAHULU.',font=font(62,True),fill='#202a23')
    for name,label,label_y,image_y in [
        ('StarterDemoVideo-60.png','01 / VISUAL BERSIH',163,204),
        ('StarterDemoVideo-135.png','02 / TAJUK SEMENTARA (3–6 SAAT)',815,858),
    ]:
        draw.text((48,label_y),label,font=font(24,True),fill='#304337')
        with Image.open(source/name) as frame:
            image.paste(frame.convert('RGB').resize((984,554),Image.Resampling.LANCZOS),(48,image_y))
    draw.text((48,1450),'Visual kembali bersih selepas tajuk. Tiada overlay kekal.',font=font(23),fill='#304337')
    target=ROOT/'docs/clean-style-preview.jpg'
    image.save(target,quality=92,optimize=True)
    print(target)


if __name__=='__main__':
    main()
