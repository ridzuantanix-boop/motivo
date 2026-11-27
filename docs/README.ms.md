# MOTIVO · by Pawarna

**Jadikan AI agent anda sebuah studio video dengan pendekatan pengarah.**

MOTIVO ialah skill dan kit produksi dalam repo. Beri arahan melalui chat; agent mengaudit bahan, menulis skrip, menetapkan arah visual, membina komposisi Remotion dan menyemak hasil. Ia menggunakan kebolehan coding agent anda, bukan dashboard berasingan.

## Mula

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

- Enam resipi cerita: faceless essay, senarai berpilih, butiran produk, perbandingan produk, visual explainer, lokasi dan budaya.
- Tiga kajian arah visual: Pressroom, Signal dan Atelier, masing-masing dalam potret serta landskap.
- Panduan anti-slop, motion, tipografi, pacing, audio dan audit realisme.
- Setup, semakan TypeScript, bundle, pemeriksaan frame dan eksport MP4 tempatan.

Resipi ialah panduan agent, bukan enam generator satu klik. Kajian visual ialah contoh tipografi/geometri tanpa audio. Agent menyesuaikan cerita dan kod mengikut brief; kualiti memerlukan pertimbangan serta semakan hasil sebenar.

## API pilihan

Tanpa API, guna gambar, klip, suara dan muzik anda sendiri atau bina motion graphics. Nexabot hanya diperlukan jika memilih penjanaan aset melaluinya. Isi key sendiri dalam `.env`, semak dokumentasi provider terkini dan tetapkan bajet. Jangan upload `.env` atau media peribadi.

Kod diberi percuma dengan lesen MIT. Lesen aset, dependencies dan penggunaan provider berasingan. Tiada jaminan monetisasi, pendapatan atau rakaman AI yang sempurna realistik. Semakan agent tidak sama dengan semakan manusia.

[Panduan lengkap](GETTING_STARTED.md) · [Contoh brief](EXAMPLES.md) · [README English](../README.md)
