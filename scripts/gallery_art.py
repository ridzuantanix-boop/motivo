"""Original SVG art direction for the MOTIVO concept gallery. Stdlib, no API/assets."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTERS = []


def text(x, y, value, size=90, fill='#eee9dc', font='Arial, sans-serif', weight=800, spacing=-4, extra=''):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font}" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}" {extra}>{html.escape(value)}</text>'


def lines(x, y, values, size=90, leading=92, **kwargs):
    return ''.join(text(x, y+i*leading, value, size=size, **kwargs) for i, value in enumerate(values))


def poster(slug, label, title, direction, bg, ink, art):
    n = len(POSTERS)+1
    # Presentation metadata belongs outside the video-style artwork.
    art = re.sub(r'<text\b[^>]*font-size="(\d+(?:\.\d+)?)"[^>]*>.*?</text>',
                 lambda match: '' if float(match[1]) < 60 else match[0], art, flags=re.S)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(label)} — {html.escape(title)}</title><desc id="desc">Poster konsep grafik asli MOTIVO. {html.escape(direction)} Bukan frame video siap.</desc>
<rect width="1200" height="675" fill="{bg}"/>
{art}
</svg>'''
    POSTERS.append(dict(id=n, slug=slug, label=label, title=title, direction=direction, source=f'gallery/{n:02d}-{slug}.svg', preview=f'{n:02d}-{slug}.jpg', svg=svg))


def build():
    ink, lime = '#e9ecdf', '#d8fa58'
    city = ''.join(f'<rect x="{690+i*54}" y="{360-(i%3)*44}" width="40" height="{205+(i%3)*44}" fill="#25352f" stroke="#71917b" stroke-width="1"/>' for i in range(9))
    contour = ''.join(f'<ellipse cx="915" cy="330" rx="{140+i*38}" ry="{90+i*24}" fill="none" stroke="#b8d57d" opacity="{.34-i*.025}" stroke-width="1"/>' for i in range(7))
    poster('faceless','Faceless & fakta','Kota memerangkap haba','Ink gelap, cahaya asid, peta kontur dan hierarki dokumentari.', '#13251e',ink,
        f'<circle cx="965" cy="210" r="107" fill="{lime}"/>{contour}{city}'+lines(46,210,['KOTA','MEMERANGKAP','HABA.'],size=79,leading=87,fill=ink,spacing=-4)+text(48,548,'Soalan kecil. Penjelasan yang membuka mata.',21,ink,weight=400,spacing=0)+text(49,124,'SEBUAH CERITA TENTANG RUANG',13,lime,spacing=2,weight=600))

    bottle = '''<ellipse cx="344" cy="561" rx="197" ry="22" fill="#0b2532" opacity=".25"/>
<g transform="rotate(-12 335 340)"><rect x="272" y="140" width="120" height="54" rx="13" fill="#294d43"/><rect x="256" y="183" width="152" height="354" rx="56" fill="#91a88c" stroke="#d6deca"/>
<path d="M276 231V473" stroke="#f4f6df" opacity=".45" stroke-width="4"/><path d="M261 284H403M261 435H403" stroke="#5b7765" opacity=".3"/>
<text x="332" y="365" text-anchor="middle" fill="#2e4f43" font-family="Arial" font-size="20" letter-spacing="4">SORA</text></g>'''
    poster('affiliate','Affiliate produk','Butiran yang buat beza','Object-led, biru elektrik, ruang kosong dan close-up produk rekaan.', '#214ee1','#f2edda',
        '<circle cx="342" cy="344" r="232" fill="#e6e7cd"/>'+bottle+lines(642,225,['BUTIRAN','YANG BUAT','BEZA.'],size=76,leading=84,fill='#f2edda')+text(645,532,'Lihat dekat. Ceritakan dengan jujur.',21,'#f2edda',weight=400,spacing=0)+text(1154,586,'PRODUK & JENAMA REKAAN',12,'#f2edda',weight=400,spacing=1,extra='text-anchor="end"'))

    room = '''<path d="M0 675V80H1200V675" fill="#121c28"/><path d="M759 108H1000V620H759Z" fill="#e7b26b"/>
<path d="M759 108L842 146V620H759Z" fill="#352621"/><path d="M842 620L1136 619L1000 435L842 435Z" fill="#d89246" opacity=".23"/>
<path d="M0 536L759 458V620H0Z" fill="#202c38"/>
<circle cx="904" cy="300" r="29" fill="#34292a"/><path d="M861 351Q904 320 946 351L958 501H849Z" fill="#34292a"/><path d="M870 488L867 611M932 488L947 611" stroke="#34292a" stroke-width="22"/>
<circle cx="1080" cy="348" r="24" fill="#111c28"/><path d="M1048 386Q1080 365 1111 386L1127 520H1036Z" fill="#111c28"/><path d="M1057 512L1057 608M1100 512L1111 608" stroke="#111c28" stroke-width="18"/>'''
    poster('drama','Drama pendek & sketsa','Pesan terakhir','Ilustrasi sinematik: cahaya pintu, siluet, ruang sunyi dan tajuk serif.', '#121c28','#f3e8d6',room+text(48,145,'SEBUAH DRAMA PENDEK',14,'#d1a875',weight=500,spacing=4)+lines(42,308,['PESAN','TERAKHIR'],size=106,leading=108,font='Georgia, serif',weight=400,fill='#f3e8d6',spacing=-5)+text(49,565,'Ada perkara yang terlambat untuk diucap.',22,'#c4ced6',weight=400,spacing=0)+text(1155,586,'WATAK & ADEGAN ILUSTRASI',11,'#f3e8d6',weight=400,spacing=1,extra='text-anchor="end"'))

    buildings = ''.join(f'<g transform="translate({720+i*97},{210+(i%2)*45})"><path d="M0 50L43 10L86 50V320H0Z" fill="#c8beaa" stroke="#665c50"/><path d="M-7 50H93M13 82H74M13 286H74" stroke="#665c50"/>'+''.join(f'<rect x="{18+j*35}" y="{90+k*54}" width="15" height="29" fill="#706759"/>' for j in range(2) for k in range(3))+'</g>' for i in range(4))
    poster('documentary','Dokumentari & sejarah','Sebelum kota ini berubah','Editorial arkib: kertas, dakwat, lukisan bangunan dan cap vermilion.', '#e5decd','#28271f',
        '<path d="M690 100L1190 115L1170 590L674 570Z" fill="#d3c9b3"/>'+buildings+lines(44,218,['SEBELUM','KOTA INI','BERUBAH.'],size=80,leading=91,fill='#28271f',font='Georgia, serif',weight=400))

    host = '''<rect x="745" y="123" width="378" height="459" rx="170" fill="#d9b995"/>
<path d="M783 581V441Q785 401 845 389H1009Q1063 402 1075 450L1100 582Z" fill="#174943"/>
<path d="M909 373V413Q937 444 961 410V372Z" fill="#a46f4b"/>
<ellipse cx="936" cy="296" rx="68" ry="89" fill="#b78057"/>
<path d="M867 287Q851 185 934 187Q1012 182 1009 284L990 254Q915 267 889 235L879 296Z" fill="#282b29"/>
<path d="M936 488L981 431L1018 458L970 533Z" fill="#b78057"/>
<rect x="914" y="389" width="17" height="107" rx="8" fill="#282b29"/><ellipse cx="923" cy="384" rx="20" ry="28" fill="#282b29"/>
<path d="M913 521L865 494L851 468L882 453L932 478Z" fill="#b78057"/>'''
    poster('host','Host review & presenter','Cuba dulu, baru cerita','Presenter ilustrasi, terracotta, framing bersih dan suara terus ke kamera.', '#bc4a32','#fff0dc',host+lines(43,252,['CUBA','DULU.'],size=125,leading=122,fill='#fff0dc')+text(49,470,'Baru cerita.',46,'#f4c88d',font='Georgia, serif',weight=400,spacing=-1)+text(49,558,'Satu produk. Pandangan yang jelas.',21,'#fff0dc',weight=400,spacing=0)+text(1113,595,'HOST ILUSTRASI · BUKAN PELAKON SEBENAR',10,'#fff0dc',weight=400,spacing=.6,extra='text-anchor="end"'))

    gears = '<path d="M520 420H1010" stroke="#272e33" stroke-width="7"/>'
    for cx,r in [(670,130),(997,72)]:
        gears+=f'<circle cx="{cx}" cy="408" r="{r}" fill="none" stroke="#e66b36" stroke-width="17" stroke-dasharray="12 13"/><circle cx="{cx}" cy="408" r="{r-28}" fill="none" stroke="#343b3d" stroke-width="3"/><circle cx="{cx}" cy="408" r="16" fill="#343b3d"/>'
        gears+=''.join(f'<path d="M{cx} 408h{r-35}" stroke="#343b3d" stroke-width="3" transform="rotate({a} {cx} 408)"/>' for a in range(0,360,60))
    poster('tutorial','Pendidikan & tutorial','Satu putaran, dua kelajuan','Diagram mekanikal, anotasi tepat dan gerak yang menerangkan konsep.', '#e9e8dd','#27353a',
        lines(44,184,['SATU PUTARAN.','DUA KELAJUAN.'],size=66,leading=76,fill='#27353a')+gears+text(50,445,'FAHAMKAN',19,'#e66b36',weight=700,spacing=3)+text(50,480,'CARA IA BERFUNGSI.',19,'#27353a',weight=700,spacing=1)+text(51,559,'Bukan sekadar hafal istilah.',21,'#27353a',weight=400,spacing=0))

    headphones=''
    for cx,color in [(365,'#edb48c'),(837,'#9baab6')]:
        headphones+=f'<path d="M{cx-85} 490V415A85 85 0 0 1 {cx+85} 415V490" fill="none" stroke="{color}" stroke-width="20"/><rect x="{cx-112}" y="426" width="55" height="114" rx="21" fill="{color}"/><rect x="{cx+57}" y="426" width="55" height="114" rx="21" fill="{color}"/>'
    poster('comparison','Top 5 & perbandingan','Dua pilihan, satu keputusan','Komposisi berpasangan, warna kontras dan perbandingan yang adil.', '#1e2f43','#f5e8d5',
        '<path d="M600 306V584" stroke="#c0b9ac" opacity=".5"/>'+text(600,183,'DUA PILIHAN.',77,'#f5e8d5',extra='text-anchor="middle"')+text(600,264,'SATU KEPUTUSAN.',64,'#edb48c',extra='text-anchor="middle"')+headphones+text(365,579,'IKUT KEPERLUAN ANDA',13,'#edb48c',spacing=2,extra='text-anchor="middle"')+text(837,579,'BUKAN SEKADAR HYPE',13,'#b6c8d3',spacing=2,extra='text-anchor="middle"'))

    plate='''<ellipse cx="329" cy="372" rx="247" ry="185" fill="#081f20"/>
<circle cx="335" cy="341" r="205" fill="#dbc7a4"/><circle cx="335" cy="341" r="172" fill="none" stroke="#b3a181" stroke-width="2"/><circle cx="335" cy="341" r="135" fill="#e6d6b7"/>
<path d="M254 328Q294 230 374 279Q467 324 394 402Q298 456 254 328Z" fill="#ae5b35"/>
<path d="M269 315Q324 290 389 371M284 291Q338 277 412 346" fill="none" stroke="#e59e61" stroke-width="8"/>
<ellipse cx="281" cy="392" rx="31" ry="14" fill="#54794b" transform="rotate(-25 281 392)"/><ellipse cx="396" cy="292" rx="35" ry="13" fill="#54794b" transform="rotate(25 396 292)"/>
<path d="M82 240V530M102 240V303M122 240V303M82 303H122M574 241V533" stroke="#bda477" stroke-width="7"/>'''
    poster('promo','Promo kedai & servis','Malam di meja kita','Hospitaliti editorial: hijau gelap, ilustrasi hidangan dan tipografi hangat.', '#123b38','#f0dfbd',plate+lines(654,235,['MALAM','DI MEJA','KITA.'],size=81,leading=88,fill='#f0dfbd',font='Georgia, serif',weight=400)+text(659,555,'Ruang untuk rasa dan cerita.',20,'#c2cbb2',weight=400,spacing=0)+text(45,593,'KONSEP RESTORAN REKAAN',11,'#c2cbb2',weight=400,spacing=2))

    horizon=''.join(f'<path d="M0 {422+i*30}Q280 {360+i*29} 600 {444+i*20}T1200 {434+i*29}" fill="none" stroke="#a484aa" stroke-width="1" opacity="{.65-i*.08}"/>' for i in range(5))
    poster('lyrics','Lagu & video lirik','Pulang perlahan','Malam ungu, horizon berlapis, lirik asli dan ruang seperti sleeve album.', '#31233e','#f0e2dd',
        '<circle cx="932" cy="221" r="108" fill="#d4afc1"/>'+horizon+text(600,285,'PULANG',139,'#f0e2dd',font='Georgia, serif',weight=400,spacing=1,extra='text-anchor="middle"')+text(600,367,'perlahan.',70,'#bf9cb6',font='Georgia, serif',weight=400,spacing=-2,extra='text-anchor="middle" font-style="italic"')+text(600,548,'Di hujung hari, kita temui jalan sendiri.',23,'#f0e2dd',weight=400,spacing=.4,extra='text-anchor="middle"')+text(600,584,'LIRIK REKAAN · KONSEP ALBUM',11,'#bf9cb6',spacing=3,extra='text-anchor="middle"'))

    landscape='''<rect x="509" y="111" width="641" height="478" fill="#cdbb8d"/>
<rect x="526" y="127" width="607" height="444" fill="#b3d2c2"/><circle cx="966" cy="253" r="72" fill="#efc38e"/>
<path d="M526 364Q680 333 811 367T1133 353V571H526Z" fill="#5a9e97"/><path d="M526 432Q701 396 895 442T1133 422V571H526Z" fill="#2e7775"/>
<path d="M526 432L596 371L649 406L691 352L763 421L769 571H526Z" fill="#1e5152"/>
<path d="M1133 297L1099 303L1061 365L1033 438L991 469L975 571H1133Z" fill="#2e5552"/>
<path d="M831 567Q897 497 980 512L975 571H817Z" fill="#c7b88b"/>'''
    poster('travel','Travel & photo essay','Sehari di tepi laut','Travel journal: bingkai cetakan, ilustrasi pesisir dan serif yang lapang.', '#e8dfc9','#254b49',landscape+lines(44,244,['SEHARI','DI TEPI','LAUT.'],size=83,leading=94,fill='#254b49',font='Georgia, serif',weight=400)+text(49,559,'Pergi jauh. Lihat perlahan.',21,'#254b49',weight=400,spacing=0)+text(1130,596,'LOKASI ILUSTRASI',10,'#254b49',spacing=2,extra='text-anchor="end"'))

    mic='''<ellipse cx="940" cy="575" rx="137" ry="13" fill="#722e30" opacity=".25"/>
<rect x="886" y="175" width="107" height="217" rx="53" fill="#efdcc3"/>
<path d="M862 318V359Q862 440 941 440Q1019 440 1019 359V318M941 441V563M869 565H1010" fill="none" stroke="#efdcc3" stroke-width="13"/>
<path d="M909 221H970M909 240H970M909 259H970M909 278H970M909 297H970M909 316H970M909 335H970" stroke="#b4473a" stroke-width="3"/>'''
    wavebars=''.join(f'<path d="M{55+i*12} {540-(i%5)*5}v{15+(i%5)*10}" stroke="#edb0a2" stroke-width="3"/>' for i in range(43))
    poster('podcast','Podcast & petikan','Tak semua perlu cepat','Spoken-word editorial, mikrofon ilustrasi dan petikan asli yang dominan.', '#a43335','#f8e9d2',
        text(40,225,'“',180,'#c86860',font='Georgia, serif',weight=400)+lines(48,269,['TAK SEMUA','PERLU','CEPAT.'],size=82,leading=88,fill='#f8e9d2')+mic+wavebars+text(49,592,'PETIKAN REKAAN · RUANG UNTUK BERFIKIR',11,'#f8e9d2',spacing=1.7,weight=400))

    geometry=''.join(f'<ellipse cx="970" cy="336" rx="{44+i*22}" ry="204" fill="none" stroke="#d6fc55" stroke-width="2" transform="rotate({-28+i*6} 970 336)"/>' for i in range(9))
    poster('motion','Motion graphics & brand film','Bentuk ada bahasa','Brand specimen: dakwat, tipografi grotesk dan geometri berirama.', '#171b18','#f1eee5',
        geometry+lines(42,263,['BENTUK','ADA','BAHASA.'],size=114,leading=111,fill='#f1eee5',spacing=-6)+text(1149,587,'IDEA → ARAH → GERAK',13,'#d6fc55',spacing=3,extra='text-anchor="end"'))


def main():
    build()
    out = ROOT / 'public/gallery'
    out.mkdir(parents=True, exist_ok=True)
    for p in POSTERS:
        (out / Path(p['source']).name).write_text(p['svg'], encoding='utf-8')
    metadata = [{k: v for k, v in p.items() if k != 'svg'} for p in POSTERS]
    (ROOT / 'src/gallery-data.ts').write_text('// Generated by scripts/gallery_art.py. Original MOTIVO concept art.\nexport const gallery = '+json.dumps(metadata, ensure_ascii=False, indent=2)+' as const;\n', encoding='utf-8')
    write_docs(metadata)
    print(f'Created {len(POSTERS)} original SVG concept posters. No API or video generation.')


def write_docs(items):
    lines = [
        '# Pilih gaya melalui rupa', '',
        '12 poster konsep asli untuk membantu memilih arah visual. Klik poster untuk versi besar. Nombor sama dengan menu jenis video; palet, tipografi dan komposisi boleh disesuaikan dengan brief anda.', '',
        '**Ini poster konsep berilustrasi, bukan frame video siap atau bukti hasil rakaman AI.** Ia menunjukkan mood, susunan visual dan tipografi; gerakan, audio dan realisme dinilai dalam produksi sebenar.', '',
        'Gaya clean untuk semua kategori: tiada label penjuru, watermark atau metadata di dalam contoh. Nama kategori dan nota konsep berada di luar frame. Tajuk besar dalam poster menunjukkan satu momen bertajuk; dalam video sebenar ia muncul mengikut cue, kemudian hilang. Shot tanpa teks ialah default.', '',
        '![Semua 12 konsep MOTIVO](gallery/overview.jpg)', '',
        '| | |', '|---|---|',
    ]
    cells = [f'**{p["id"]:02d} · {p["label"]}**<br>[![{p["label"]} — {p["title"]}](gallery/{p["preview"]})](gallery/{p["preview"]})<br>{p["direction"]}' for p in items]
    lines.extend(f'| {cells[i]} | {cells[i+1]} |' for i in range(0,len(cells),2))
    lines.extend([
        '', '## Cara pilih', '',
        '> Aku pilih poster 3. Aku suka mood cahaya dan ruangnya, tetapi nak cerita komedi keluarga. Cadangkan skrip 45 saat dan sesuaikan gaya itu. Jangan jana aset berbayar dulu.', '',
        '> Gabungkan tipografi poster 4 dengan warna poster 10 untuk video faceless tentang kampung aku.', '',
        'Poster bukan sempadan kreativiti atau janji hasil serupa tanpa bahan yang sesuai. Agent boleh bina arah baharu. Untuk host/drama realistik, gunakan rakaman sendiri atau rancang penjanaan provider secara berasingan; figura dalam galeri ialah ilustrasi, bukan pelakon sebenar.', '',
        '## Sumber dan bina semula', '',
        'Semua lukisan, objek, figura, lokasi, lirik dan jenama contoh dalam poster ialah rekaan grafik asli. Tiada foto stok atau panggilan API digunakan. Sumber SVG berada dalam `public/gallery/`, dijana oleh `scripts/gallery_art.py`, dan dimasukkan ke komposisi `Gallery-*` di Studio. Ini komposisi poster satu frame, bukan templat video penuh.', '',
        'Untuk bina semula: `python scripts/gallery_art.py`, `npm run build`, kemudian `npm run gallery`. JPEG yang dirender berada dalam `docs/gallery/`. Helaian ringkasan boleh dibina semula dengan `python scripts/gallery_contact.py` (Pillow diperlukan untuk alat dokumentasi pilihan ini sahaja). Kod/grafik galeri menggunakan lesen MIT repo; fon sistem tidak dibundel.', '',
        'Alternatif memori rendah: `python scripts/gallery_raster.py` dengan PyMuPDF. Fon/rasterizer boleh memberi perbezaan kecil; semak hasil visual. PyMuPDF dan Pillow ialah alat dokumentasi pilihan dengan lesen masing-masing, bukan dependencies setup atau runtime video.', '',
        '[Katalog dan keperluan bahan](VIDEO_TYPES.md) · [Mula di sini](../START_HERE.md)',
    ])
    (ROOT / 'docs/STYLE_GALLERY.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')


if __name__ == '__main__':
    main()
