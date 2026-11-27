# MOTIVO · by Pawarna

**Jadikan AI agent anda sebuah studio video dengan pendekatan pengarah.**

**Baru mula?** Cakap: “Buka MOTIVO dan bimbing aku buat video pertama. Aku baru mula.” Agent akan bantu pilih video, bahan dan suara satu langkah pada satu masa. [Mula di sini](../START_HERE.md) · [Panduan key dan suara](PROVIDERS.md)

MOTIVO ialah skill dan kit produksi dalam repo. Beri arahan melalui chat; agent mengaudit bahan, menulis skrip, menetapkan arah visual, membina komposisi Remotion dan menyemak hasil. Ia menggunakan kebolehan coding agent anda, bukan dashboard berasingan.

**Default v0.4 ialah clean untuk semua 12 jenis:** visual penuh, tiada label penjuru atau overlay melekat. Tajuk bila perlu sahaja, besar dan ada masa tamat. Sarikata/lirik/diagram yang diperlukan kekal jelas dan mengikut timing. Demo lama telah diganti; [projek yang guna komponen overlay lama perlu dikemas kini](CLEAN_STYLE.md).

## Mula

Tak perlu download sendiri jika agent boleh clone GitHub. Beri link https://github.com/ridzuantanix-boop/motivo dan minta agent setup dalam folder baharu, baca `AGENTS.md`, kemudian bimbing anda tanpa menjana media atau menggunakan kredit dahulu.

Muat turun ZIP repo, ekstrak dan buka folder dalam agent. Pasang Node.js 22+, kemudian jalankan:

```sh
npm ci
npm run setup
npm run studio
```

Dalam Windows PowerShell, gunakan `npm.cmd` jika perlu. Python 3.10+ diperlukan untuk client Nexabot; FFmpeg/FFprobe untuk pemprosesan dan audit media.

Beritahu agent:

```text
Baca AGENTS.md dan .agents/skills/motivo/SKILL.md.
Gunakan MOTIVO untuk projek ini. Semak setup tanpa menjana video dahulu.
```

Kemudian:

```text
Buat video affiliate lampu meja 30 saat, 9:16, daripada gambar dalam
public/assets/lampu/. Gaya editorial moden. Guna rakaman suara aku.
Jangan reka harga, pengalaman penggunaan atau testimoni. Jangan publish.
```

## Apa yang tersedia

- Tujuh resipi cerita: faceless essay, senarai berpilih, butiran produk, perbandingan produk, visual explainer, lokasi/budaya dan drama pendek/sketsa.
- Tiga kajian arah visual: Pressroom, Signal dan Atelier, masing-masing dalam potret serta landskap.
- Panduan anti-slop, motion, tipografi, pacing, audio dan audit realisme.
- Setup, semakan TypeScript, bundle, pemeriksaan frame dan eksport MP4 tempatan.

Resipi ialah panduan agent, bukan tujuh generator satu klik. Kajian visual ialah contoh tipografi/geometri tanpa audio. Agent menyesuaikan cerita dan kod mengikut brief; kualiti memerlukan pertimbangan serta semakan hasil sebenar.

Onboarding kini menunjukkan [12 jenis video](VIDEO_TYPES.md), termasuk drama pendek. Drama boleh menggunakan rakaman sendiri, gambar dengan narasi/dialog atau klip AI pilihan. Suara TTS sahaja tidak menghasilkan lip-sync. Wajah, suara, pakaian dan kesinambungan babak perlu diperiksa; tiada jaminan watak AI sentiasa konsisten.

**Pilih melalui contoh adegan:** [galeri 12 jenis video](STYLE_GALLERY.md) menunjukkan rupa yang terus dikenali: watak drama, host review, demo produk dan studio podcast. Ada penerangan ringkas tentang apa yang dilihat/didengar dalam video. Gambar dijana AI, bukan klip siap. Contoh: “Aku nak drama komedi keluarga macam nombor 3.”

## API pilihan

Tanpa API, guna gambar, klip, suara dan muzik anda sendiri atau bina motion graphics. Nexabot hanya diperlukan jika memilih penjanaan aset melaluinya. Isi key sendiri dalam `.env`, semak dokumentasi provider terkini dan tetapkan bajet. Jangan upload `.env` atau media peribadi.

Kod diberi percuma dengan lesen MIT. Lesen aset, dependencies dan penggunaan provider berasingan. Tiada jaminan monetisasi, pendapatan atau rakaman AI yang sempurna realistik. Semakan agent tidak sama dengan semakan manusia.

Untuk suara, pilih rakaman sendiri, Google AI Studio manual (jana/download melalui browser tanpa key dalam MOTIVO), Google API automatik (`GEMINI_API_KEY`), Nexabot atau tanpa narasi. Dua provider memerlukan key berasingan; login Antigravity bukan key provider. Agent patut membimbing cara simpan secara tempatan, bukan meminta key dalam chat.

[Panduan lengkap](GETTING_STARTED.md) · [Contoh brief](EXAMPLES.md) · [README English](../README.md)
