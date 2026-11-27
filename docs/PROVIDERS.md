# Sambungan dan suara, langkah demi langkah

Mula dengan [START_HERE](../START_HERE.md) dan minta agent membimbing anda. Anda tak perlu sambungkan semua provider.

| Laluan | Key dalam MOTIVO | Apa yang pengguna buat |
|---|---|---|
| Gambar/klip + suara sendiri | Tiada | Beri fail kepada agent |
| Google AI Studio manual | Tiada | Jana/download audio dalam browser, beri lokasinya |
| Google API automatik | `GEMINI_API_KEY` | Simpan key sendiri secara tempatan |
| Nexabot | `NEXABOT_API_KEY` | Simpan key sendiri; pastikan akses/kredit API |
| Tanpa suara | Tiada | Nyatakan video sengaja tanpa narasi |

## Nexabot

1. Buka [API keys Nexabot](https://nexabot.id/api-keys) dan login sendiri. Salin key daripada akaun anda. Halaman mungkin perlu login sebelum kawalan key muncul.
2. Beritahu agent “Buka `.env` dan tunjuk baris Nexabot tanpa memaparkan key.” Tampal selepas `NEXABOT_API_KEY=` dan save. Alternatif: `npm run connect -- nexabot` dalam terminal anda sendiri untuk input tersembunyi.
3. Minta “semak sambungan sahaja”. Agent menggunakan `npm run provider:check -- nexabot`, bukan submit video.
4. Jika 401/403, semak key/akses akaun; jika 429, semak had. Jangan beli pelan hanya berdasarkan nama atau harga dalam starter lama. [Dokumentasi API terkini](https://nexabot.id/api-docs).

## Google AI Studio manual — tiada key dalam MOTIVO

1. Minta agent sediakan skrip dan arahan sebutan berasingan.
2. Buka [Generate speech](https://aistudio.google.com/generate-speech), login, pilih model TTS dan suara yang tersedia. Label UI mungkin berubah.
3. Letakkan skrip dalam ruang teks dan gaya suara dalam kawalan/arahan yang sesuai. Untuk BM: “Bahasa Melayu Malaysia, natural, jelas dan tenang.” Dengar hasil dahulu.
4. Gunakan kawalan download/export yang tersedia. Simpan ke folder `public/assets/<projek>/`, kemudian beritahu agent lokasi fail sebenar. Jangan tukar extension jika format asal berbeza.
5. Agent semak audio, durasi dan sarikata sebelum menyunting video. Cara ini memerlukan langkah browser daripada anda setiap kali; ia tidak menyambungkan API secara automatik.

## Google API automatik

1. Buka [AI Studio API keys](https://aistudio.google.com/apikey). Cipta/pilih key pada projek yang sesuai mengikut UI Google. Semak syarat akses, kuota dan billing akaun; MOTIVO tidak mengaktifkan billing.
2. Isi `GEMINI_API_KEY=` dalam `.env`, atau jalankan `npm run connect -- google` dalam terminal interaktif sendiri. Jangan tampal key dalam chat/command.
3. `npm run provider:check -- google` menyemak akses senarai model sahaja; kejayaan itu tidak menjamin kuota TTS.
4. Agent menulis skrip dalam fail dan menjalankan semakan tempatan `scripts/google_tts.py` dahulu. Audio hanya dijana jika `--generate` digunakan selepas anda memberi izin menghantar skrip dan menggunakan API.

Model dan suara boleh diubah dalam `.env` melalui `GEMINI_TTS_MODEL` dan `GEMINI_TTS_VOICE`. Default ialah `gemini-3.8-flash-tts` / `Kore` berdasarkan dokumen rasmi yang disemak pada 2026-11-27. Model, harga dan akses boleh berubah; ini bukan janji penjanaan percuma. [Google TTS](https://ai.google.dev/gemini-api/docs/speech-generation) · [Google API keys](https://ai.google.dev/gemini-api/docs/api-key)

## Semakan status

`npm run providers` hanya membaca konfigurasi tempatan. Ia tidak memaparkan key dan tidak menghubungi provider. Key “tersedia” belum bermaksud “sudah disahkan”.

Jika terminal tidak menemui `python`, minta agent semak Python 3.10+ dan gunakan `python3` mengikut persekitaran, atau terus gunakan laluan editor/manual. Masalah setup tidak patut memaksa anda membeli API.
