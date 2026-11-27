# Pilih gaya melalui rupa

12 poster konsep asli untuk membantu memilih arah visual. Klik poster untuk versi besar. Nombor sama dengan menu jenis video; palet, tipografi dan komposisi boleh disesuaikan dengan brief anda.

**Ini poster konsep berilustrasi, bukan frame video siap atau bukti hasil rakaman AI.** Ia menunjukkan mood, susunan visual dan tipografi; gerakan, audio dan realisme dinilai dalam produksi sebenar.

![Semua 12 konsep MOTIVO](gallery/overview.jpg)

| | |
|---|---|
| **01 · Faceless & fakta**<br>[![Faceless & fakta — Kota memerangkap haba](gallery/01-faceless.jpg)](gallery/01-faceless.jpg)<br>Ink gelap, cahaya asid, peta kontur dan hierarki dokumentari. | **02 · Affiliate produk**<br>[![Affiliate produk — Butiran yang buat beza](gallery/02-affiliate.jpg)](gallery/02-affiliate.jpg)<br>Object-led, biru elektrik, ruang kosong dan close-up produk rekaan. |
| **03 · Drama pendek & sketsa**<br>[![Drama pendek & sketsa — Pesan terakhir](gallery/03-drama.jpg)](gallery/03-drama.jpg)<br>Ilustrasi sinematik: cahaya pintu, siluet, ruang sunyi dan tajuk serif. | **04 · Dokumentari & sejarah**<br>[![Dokumentari & sejarah — Sebelum kota ini berubah](gallery/04-documentary.jpg)](gallery/04-documentary.jpg)<br>Editorial arkib: kertas, dakwat, lukisan bangunan dan cap vermilion. |
| **05 · Host review & presenter**<br>[![Host review & presenter — Cuba dulu, baru cerita](gallery/05-host.jpg)](gallery/05-host.jpg)<br>Presenter ilustrasi, terracotta, framing bersih dan suara terus ke kamera. | **06 · Pendidikan & tutorial**<br>[![Pendidikan & tutorial — Satu putaran, dua kelajuan](gallery/06-tutorial.jpg)](gallery/06-tutorial.jpg)<br>Diagram mekanikal, anotasi tepat dan gerak yang menerangkan konsep. |
| **07 · Top 5 & perbandingan**<br>[![Top 5 & perbandingan — Dua pilihan, satu keputusan](gallery/07-comparison.jpg)](gallery/07-comparison.jpg)<br>Komposisi berpasangan, warna kontras dan perbandingan yang adil. | **08 · Promo kedai & servis**<br>[![Promo kedai & servis — Malam di meja kita](gallery/08-promo.jpg)](gallery/08-promo.jpg)<br>Hospitaliti editorial: hijau gelap, ilustrasi hidangan dan tipografi hangat. |
| **09 · Lagu & video lirik**<br>[![Lagu & video lirik — Pulang perlahan](gallery/09-lyrics.jpg)](gallery/09-lyrics.jpg)<br>Malam ungu, horizon berlapis, lirik asli dan ruang seperti sleeve album. | **10 · Travel & photo essay**<br>[![Travel & photo essay — Sehari di tepi laut](gallery/10-travel.jpg)](gallery/10-travel.jpg)<br>Travel journal: bingkai cetakan, ilustrasi pesisir dan serif yang lapang. |
| **11 · Podcast & petikan**<br>[![Podcast & petikan — Tak semua perlu cepat](gallery/11-podcast.jpg)](gallery/11-podcast.jpg)<br>Spoken-word editorial, mikrofon ilustrasi dan petikan asli yang dominan. | **12 · Motion graphics & brand film**<br>[![Motion graphics & brand film — Bentuk ada bahasa](gallery/12-motion.jpg)](gallery/12-motion.jpg)<br>Brand specimen: dakwat, tipografi grotesk dan geometri berirama. |

## Cara pilih

> Aku pilih poster 3. Aku suka mood cahaya dan ruangnya, tetapi nak cerita komedi keluarga. Cadangkan skrip 45 saat dan sesuaikan gaya itu. Jangan jana aset berbayar dulu.

> Gabungkan tipografi poster 4 dengan warna poster 10 untuk video faceless tentang kampung aku.

Poster bukan sempadan kreativiti atau janji hasil serupa tanpa bahan yang sesuai. Agent boleh bina arah baharu. Untuk host/drama realistik, gunakan rakaman sendiri atau rancang penjanaan provider secara berasingan; figura dalam galeri ialah ilustrasi, bukan pelakon sebenar.

## Sumber dan bina semula

Semua lukisan, objek, figura, lokasi, lirik dan jenama contoh dalam poster ialah rekaan grafik asli. Tiada foto stok atau panggilan API digunakan. Sumber SVG berada dalam `public/gallery/`, dijana oleh `scripts/gallery_art.py`, dan dimasukkan ke komposisi `Gallery-*` di Studio. Ini komposisi poster satu frame, bukan templat video penuh.

Untuk bina semula: `python scripts/gallery_art.py`, `npm run build`, kemudian `npm run gallery`. JPEG yang dirender berada dalam `docs/gallery/`. Helaian ringkasan boleh dibina semula dengan `python scripts/gallery_contact.py` (Pillow diperlukan untuk alat dokumentasi pilihan ini sahaja). Kod/grafik galeri menggunakan lesen MIT repo; fon sistem tidak dibundel.

Alternatif memori rendah: `python scripts/gallery_raster.py` dengan PyMuPDF. Fon/rasterizer boleh memberi perbezaan kecil; semak hasil visual. PyMuPDF dan Pillow ialah alat dokumentasi pilihan dengan lesen masing-masing, bukan dependencies setup atau runtime video.

[Katalog dan keperluan bahan](VIDEO_TYPES.md) · [Mula di sini](../START_HERE.md)
