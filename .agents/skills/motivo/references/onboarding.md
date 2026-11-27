# First-run conversation — guide the user, do not leave them at “installed”

Read this after a setup/install request, “how do I start?”, “guide me”, provider/key questions, or a first video brief without an established workflow. Continue in the user's language (default BM). If the brief already supplies a decision, do not ask it again. No setup step generates media or spends credits.

## Welcome with a useful next step

After local checks, show a short capability summary: local visuals ready/missing; Nexabot key present/not connected; Google API key present/not connected. Read key presence without printing `.env`, keys, prefixes or suffixes. Present configuration as unverified until an explicit read-only check succeeds. Do not equate install success with authentication, model access or production readiness.

Suggested opening:

> MOTIVO dah dipasang. Aku boleh bantu dari idea sampai video. Ini jenis yang boleh kita buat:
> 1. Faceless & fakta
> 2. Affiliate produk
> 3. Drama pendek & sketsa
> 4. Dokumentari & sejarah
> 5. Host review & presenter
> 6. Pendidikan & tutorial
> 7. Top 5 & perbandingan
> 8. Promo kedai & servis
> 9. Lagu & video lirik
> 10. Travel & photo essay
> 11. Podcast & petikan
> 12. Motion graphics & brand film
>
> Pilih nombor atau terus ceritakan idea. Kalau tak pasti, beritahu topik/produk sahaja.

Read `docs/VIDEO_TYPES.md` from the project root for current use cases and asset requirements. Show the compact numbered menu on first-run onboarding and whenever asked for available video types, not only a faceless/affiliate/“other” choice. If the user already has a brief, go straight to the relevant route and do not force a menu. These are supported planning/editing use cases, not 12 ready-made templates or automatic generation guarantees. For drama/sketch requests, read [drama.md](drama.md) before planning shots or audio. Clarify illustrated narration versus speaking live-action characters.

Offer the visual gallery with the menu: `docs/STYLE_GALLERY.md` and the checked-in `docs/gallery/overview.jpg`. Show the overview image if the chat supports local/repository images; otherwise give a clickable gallery link for the current repository. Use the existing posters, not a new generation request. Ask “Nak ikut rupa poster nombor berapa, atau ubah/gabungkan gaya?” Users may select by mood, color, type or layout rather than category. Posters are illustrated art-direction concepts, not finished video frames or live-action examples; say this briefly. Do not dump all 12 full-size images into chat. For a user with an established brief, offer only relevant references when useful.

After the user chooses, offer only relevant choices:

> Bahan visual nak guna **gambar/klip sendiri** (tanpa API penjanaan) atau **jana melalui Nexabot** (key dan kredit sendiri)?

> Suara nak guna **rakaman sendiri**, **Google AI Studio manual**, **Google API automatik**, **Nexabot**, atau **tanpa suara**? Kalau baru mula dan tiada key, Google AI Studio manual boleh jadi laluan pertama, tertakluk akses akaun.

Ask one small stage at a time, not a long questionnaire. Infer audience/aspect/duration when sensible and state proposed defaults (e.g. 30 seconds, 9:16 for short-form affiliate). A provider choice does not authorize a paid test. Do not force Nexabot/Google on a project using supplied media. Do not require returning users to repeat onboarding; use existing project notes or `.motivo/preferences.json` (ignored) for nonsecret choices only.

## Provider guidance

Read [providers.md](providers.md) only for the chosen route. Explain that API key means a private access key for a provider, separate from Antigravity/Codex login. Give the correct provider link and a simple next action. The user creates the key/signs in themselves. Never ask them to paste a key into chat. Offer a local `.env` editor path or a hidden terminal prompt they run themselves. Do not put secrets into command arguments, logs, examples or project notes. If the user voluntarily provides a key, save it only to local `.env` without echoing it.

After a connection is selected, run `npm run providers` to show redacted status. With authorization for read-only validation, run `npm run provider:check -- <provider>`. Explain actual failure (401/403 access, 429 quota, network) and offer the manual/local route without repeatedly retrying. A Google model-list response does not establish TTS generation entitlement. Client existence and offline tests do not mean the live provider was exercised.

## Finish onboarding with a first brief

If no brief exists, offer three short examples relevant to their chosen category. If a brief exists, show a compact recap: video idea, duration/aspect, available assets, voice route, missing items and any cost-dependent next step. End with an actual next action: write the script, put images into an exact folder, or have the user download AI Studio audio. Do not end with only a terminal command list or “setup complete”.

Example first brief:

> Buat video affiliate lampu meja, 30 saat, 9:16. Guna gambar aku. Tolong tulis skrip, kemudian bimbing aku buat suara di Google AI Studio. Jangan jana aset berbayar dahulu.

For manual Google audio: prepare a `projects/<slug>/narration.txt` and speaking-style note, give the speech playground link, wait for the saved audio path, inspect it using ffprobe, listen if tools allow, then align captions to the actual file. Do not invent word timestamps or claim lip-sync from a narration WAV. Keep original Nexabot host speech unmodified for lip-sync.
