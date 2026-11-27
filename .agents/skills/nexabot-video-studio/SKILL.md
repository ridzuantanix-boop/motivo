---
name: nexabot-video-studio
description: Aliran kerja lengkap menghasilkan video 60 saat (1080p) berbahasa Melayu menggunakan API Nexabot (`omni_flash`, `nano_banana_2`), audio SuaraKita/Nexabot, FFmpeg, dan Remotion. Gunakan apabila pengguna meminta video pelancongan, ulasan *tour guide*, video lagu negeri, atau video pendek berpandukan topik/lokasi/avatar.
---

# Nexabot + Remotion AI Video Studio (Bahasa Melayu)

Panduan langkah demi langkah untuk menghasilkan video sinematik `1920×1080`, `30 fps`, `60 saat` terus daripada arahan pengguna.

## 0. Semakan Awal (Pre-flight)

1. Semak fail `.env` dalam akar projek: pastikan `NEXABOT_API_KEY=nxb_...` wujud dan bukan nilai contoh.
   - Jika `.env` tiada atau kunci masih kosong, salin daripada `.env.example` dan minta pengguna tampal API key Nexabot mereka (jangan dedahkan kunci dalam kod/commit).
2. Pastikan kebergantungan tersedia:
   - `Test-Path node_modules` → jika tiada, jalankan `npm.cmd install`.
   - Sahkan `python`, `ffmpeg`, dan `ffprobe` boleh dipanggil dari terminal.
3. Semak baki kredit Nexabot dahulu:
   ```powershell
   python scripts/nexabot_client.py credit
   ```

## 1. Kajian Fakta & Pecahan 4 Babak (60 Saat)

1. Gunakan carian web untuk fakta sebenar lokasi, makanan ikonik, sejarah, atau keunikan destinasi supaya skrip 100% tepat.
2. Pecahkan video 60 saat kepada **4 babak × ~15 saat** (`1800` frame @ `30 fps`).
   - Jika menggunakan `TransitionSeries` dengan 3 transisi `15` frame (`fade` / `slide`), jumlah `durationInFrames` keempat-empat `TransitionSeries.Sequence` **mesti `1845`** (`1845 - 3*15 = 1800` frame).
   - Pastikan bagi setiap klip: `(clipDurationSec / playbackRate) >= (sequenceDurationFrames / 30)` supaya video tidak pegun di penghujung klip.
3. Video 15 saat boleh dipecahkan kepada 2–3 *sub-shot* dinamik dalam *prompt* (`Shot 1 (0-5s)... Shot 2 (5-10s)... Shot 3 (10-15s)...`), atau dibahagi mengikut segmen lagu.

## 2. Pilih Laluan Penghasilan Aset

### Laluan A: Video Berdialog / Host / Tour Guide (dengan atau tanpa Avatar)

1. **Jana Plat Latar Bersih (16:9) dahulu (`POST /api/v1/image`):**
   - Model disyorkan: `nano_banana_2`, `aspect: "16:9"`, `resolution: "1K"`.
   - Kosongkan bahagian kiri/hadapan untuk kedudukan host, dan nyatakan eksplisit pelawat latar berpakaian sopan menutup aurat.
   - Semak semua imej plat (`bg1.png..bg4.png`) secara visual sebelum jana video.
2. **Jana Klip Video Konsisten Wajah + Dialog BM Terus (`POST /api/v1/api`, `mode: "i2v"`):**
   - Jika ada gambar wajah rujukan pengguna, hantar `media: [avatar_data_uri, bg_data_uri]` (elak jana imej wajah baharu dengan `nano_banana` kerana wajah mudah berubah).
   - Nyatakan dalam *prompt* supaya host kekal menghadap kamera (`front-facing`, jangan pusing sisi keterlaluan), pakaian seragam/konsisten, dan **masukkan dialog Bahasa Melayu sebenar terus dalam prompt** supaya Nexabot menjana suara dan *lip-sync* Bahasa Melayu secara terus.
   - Gunakan `model: "omni_flash"`, `mode: "i2v"`, `ratio: 1`, `resolution: 1080`, `duration: 15`.
   - Kekalkan audio asal video (`muted={false}` / tiada prop `muted` pada `<OffthreadVideo>`) dan `playbackRate={1.0}` supaya kelajuan suara dan *lip-sync* kekal natural.

### Laluan B: Video Naratif Negeri / Lagu Khas (Tanpa Dialog On-Cam)

1. **Klip Sinematik (`mode: "t2v"`) & Muzik (`mode: "music"`):**
   - Guna `model: "omni_flash"`, `mode: "t2v"`, `ratio: 1`, `resolution: 1080`, `duration: 15`.
   - Jika tema berkaitan lagu ceria (cth: lagu negeri), hantar *prompt* genre muzik + lirik Bahasa Melayu penuh ke `mode: "music"`, kemudian potong tepat 60.0s dengan `ffmpeg` (jika ada bahagian instrumental terlalu panjang, buat *radio edit* `acrossfade` supaya verse + chorus muat kemas dalam 60s).
2. **Suara Latar Naratif (Terbina Nexabot / SuaraKita):**
   - Untuk video dokumentari/penerangan negeri tanpa dialog *on-cam*, jangan guna `edge-tts`. Pilih salah satu suara natural ini:
     - **Nexabot TTS (`POST /api/v1/api`, `mode: "tts"`, `voice: "Charon"` / `"Kore"` / `"Puck"`):** Menghasilkan WAV suara Gemini yang sama dengan SuaraKita (~5–15s, guna satu bahasa sahaja iaitu Bahasa Melayu dalam `prompt`).
     - **Nexabot Voice ElevenLabs (`POST /api/v1/voice`):** Guna `voice_id` daripada `GET /api/v1/voices` (`0.02` kredit) — respons memulangkan `url` audio dan array `timestamps` (`{ text, start }`) yang memudahkan penyelarasan sarikata. *(Boleh juga klon suara sendiri secara percuma via `POST /api/v1/voice/clone`.)*
     - **SuaraKita (Google AI Studio):** Jika pengguna memberikan pautan/sesi SuaraKita, boleh jana `.wav` di situ.
   - Normalisasikan audio akhir dengan FFmpeg:
     ```powershell
     ffmpeg -y -i raw.wav -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 44100 -ac 2 -b:a 192k public/assets/<projek>/voiceover.mp3
     ```

## 3. Audit Visual, Aurat & Penyelarasan Masa (Wajib Sebelum Render)

1. **Audit Visual (`ffmpeg`):** Ekstrak *contact sheet* `2x2` atau `3x2` bagi setiap klip MP4:
   ```powershell
   ffmpeg -y -i public/assets/<projek>/clip1.mp4 -vf "fps=1/2.5,scale=640:-1,tile=3x2" -frames:v 1 audit_clip1.jpg -loglevel error
   ```
   - Semak jika ada objek bertukar pelik (*morphing*) atau individu berpakaian mendedahkan aurat.
   - Jika hanya satu sub-shot bermasalah, jana klip single-shot pendek (`duration: 6`) untuk sub-shot itu sahaja dan cantum dengan `ffmpeg` (`trim`, `setpts=PTS-STARTPTS`, `fps=24`, `scale=1920:1080`, `concat`).
2. **Kesan Masa Sebenar Audio:**
   - Jalankan `silencedetect` dan dengar audio sebenar sebelum menetapkan `startSec` / `endSec` sarikata dan sempadan `PENANG_SUBSHOTS` / babak (`select='gt(scene,0.28)',showinfo`).
   - Pastikan teks sarikata ringkas (1–2 baris) dan bertukar tepat mengikut jeda suara atau lirik lagu.

## 4. Komposisi Remotion & Pengesahan Akhir

1. Bina komposisi baharu dalam `src/<Projek>Video.tsx` dan `src/<projek>Data.ts` dengan menggunakan komponen sedia ada dalam `src/components/MotionOverlays.tsx` (`TopChannelWatermark`, `IntroHookBadge`, `LocationLowerThird`, `InfoSideCard`, `FacelessCaptions`, `TimelineProgressBar`), lalu daftarkan dalam `src/Root.tsx`.
2. Semak TypeScript & render:
   ```powershell
   npx.cmd tsc --noEmit; if ($LASTEXITCODE -ne 0) { throw "TSC gagal" }
   npx.cmd remotion render src/index.ts <CompositionId> out/<output>.mp4 --codec=h264 --crf=18 --overwrite
   ```
3. **Pengesahan Output:** Semak dengan `ffprobe` (`1920×1080`, `30/1`, `duration ~60s`, kedua-dua aliran `video` + `audio` wujud) dan ekstrak 3–4 frame daripada MP4 siap untuk pastikan tiada pertindihan UI atau kecacatan visual sebelum menyerahkan hasil kepada pengguna.
