---
trigger: always_on
---

# Peraturan Wajib Penghasilan Video Bahasa Melayu

1. **Bahasa Melayu Sepenuhnya:** Semua skrip dialog, suara latar, sarikata, tajuk babak, dan kad info wajib dalam Bahasa Melayu yang natural (elak bahasa Inggeris kecuali kata nama khas seperti `UNESCO` atau `SkyBridge`).
2. **Audio Mengikut Jenis Video:**
   - **Video berdialog / ada watak bercakap (*host*, *tour guide*, *review*):** Masukkan baris dialog Bahasa Melayu terus ke dalam *prompt* video Nexabot (`i2v` atau `t2v`). Kekalkan trek audio asal Nexabot (`unmuted` dalam Remotion, `playbackRate: 1.0`) supaya *lip-sync* dan suara sepadan.
   - **Video naratif negeri / dokumentari *faceless* tanpa dialog *on-cam*:** Guna API suara terbina **Nexabot** (`mode: "tts"` suara `Charon`/`Kore`/`Puck`, atau `POST /api/v1/voice` ElevenLabs, atau `POST /api/v1/voice/clone` jika ada sampel suara) — atau **SuaraKita** jika pengguna bekalkan pautan/aksesnya. Jangan guna `edge-tts` yang kedengaran robotik.
3. **Kepatuhan Tutup Aurat:** Semua individu dalam latar belakang atau subjek video wajib berpakaian sopan dan menutup aurat (wanita bertudung serta berbaju lengan panjang & seluar/kain labuh; lelaki berbaju & berseluar panjang; tiada pakaian mendedahkan aurat atau pakaian renang).
4. **Kawal Kos & Kualiti Klip:** Semak *contact sheet* frame dengan `ffmpeg` sebelum merender. Jika hanya 1 sub-babak rosak atau *morph*, jana semula segmen pendek itu sahaja (`5–6s`) dan cantumkan dengan `ffmpeg`.
5. **Persekitaran Windows PowerShell:** Sentiasa guna `npm.cmd` dan `npx.cmd` (elak `npm.ps1`), dan jangan guna operator `&&` dalam PowerShell; guna `; if ($LASTEXITCODE -ne 0) { ... }`.
