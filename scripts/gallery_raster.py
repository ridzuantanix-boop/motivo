"""Optional low-memory SVG-to-JPEG exporter. Requires PyMuPDF; no browser/API."""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]


def main():
    output=ROOT/'docs/gallery'
    output.mkdir(parents=True,exist_ok=True)
    posters=sorted((ROOT/'public/gallery').glob('*.svg'))
    if len(posters)!=12:
        raise RuntimeError('Generate the 12 SVG sources with scripts/gallery_art.py first.')
    for source in posters:
        with fitz.open(stream=source.read_bytes(),filetype='svg') as document:
            page=document[0]
            scale=fitz.Matrix(1200/page.rect.width,675/page.rect.height)
            pixels=page.get_pixmap(matrix=scale,alpha=False)
            target=output/(source.stem+'.jpg')
            pixels.save(str(target),jpg_quality=94)
            print(target.name)


if __name__=='__main__':
    main()
