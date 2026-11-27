# Provider routes and beginner guidance

## No API

Use supplied images, video, recordings and licensed music, or original code-based motion graphics. The agent handles script, layout, animation and local export. No media-generation key is required. Silent video is a valid choice if the brief asks for it.

## Nexabot — visuals, host audio or narration

1. Open [Nexabot API keys](https://nexabot.id/api-keys), sign in, and create/copy the account's key. Account/key creation remains with the user. Credits/plans and API access differ from the web product; consult the current dashboard, not old price examples.
2. Offer the user `npm run connect -- nexabot` in their own interactive terminal (hidden input), or open local `.env` in their editor and identify the `NEXABOT_API_KEY=` line without showing its contents. If Python is unavailable, use the editor route.
3. With read-only checking authorized, `npm run provider:check -- nexabot` calls the credit endpoint without generating media. Never print the provider's full response or any key.
4. Verify [current API docs](https://nexabot.id/api-docs) before generation. The older starter note is preserved as a reference, not an authoritative current contract. Show a concrete plan, credit budget if verifiable, and get generation authorization if not already supplied. No real generation is part of onboarding.

If the API pages require login, tell the user exactly that. Do not invent where a hidden dashboard control is located. A key saved locally is not an authenticated account. Follow the realism gate for generated video; preserve original host speech.

## Google AI Studio — manual audio, no API key in MOTIVO

Best for a user who prefers a browser step over managing an API key. Subject to Google's account, region, model availability and usage limits; do not promise unlimited or universally free generation.

1. Agent writes the final narration text and a speaking direction, keeping direction separate from words to be spoken.
2. User opens [Generate speech in Google AI Studio](https://aistudio.google.com/generate-speech) and signs in. Choose a single speaker and an available TTS model/voice. UI labels may vary; guide from the screen the user actually sees if browser tools are available.
3. Put the spoken script in the text field. Suggested direction: “Bahasa Melayu Malaysia, sebutan natural, tenang dan jelas, jangan baca arahan gaya.” Listen to a preview, adjust pronunciation/pace, then use the available download/export control.
4. Save the resulting audio under `public/assets/<slug>/voiceover.wav` (or preserve the actual extension if different) and give the agent its path. Do not tell the user to rename MP3 bytes to WAV. Agent verifies the format and timing before editing.

Signing into AI Studio does not connect a Gemini API key to MOTIVO. No API key is needed in `.env` for this manual route. Do not automate sign-in or create credentials on the user's behalf.

## Google API — optional automatic narration

1. User opens [Google AI Studio API keys](https://aistudio.google.com/apikey), selects/creates the appropriate project/key using Google's UI, and checks quota/billing. Key management is separate from the speech playground. Do not enable billing or change project permissions for them.
2. User runs `npm run connect -- google` locally, or fills `GEMINI_API_KEY=` in `.env`. No new npm/Python dependency is required by this client beyond Python 3.10+.
3. `npm run provider:check -- google` is a read-only model-list check. It does not prove quota, billing or TTS entitlement. `GEMINI_TTS_MODEL` and `GEMINI_TTS_VOICE` are optional configuration; defaults were verified against the official docs on 2026-11-27 and may change.
4. Agent prepares `projects/<slug>/narration.txt`. A local-only preflight (no key, network or audio) is:

```sh
python scripts/google_tts.py --text-file projects/<slug>/narration.txt --out public/assets/<slug>/voiceover.wav
```

After the user authorizes sending this script to Google and any applicable API usage, add `--generate`. The client sends a single request with no automatic retries, saves a new WAV (does not overwrite), and never logs the key. A dry run succeeding is not a live generation test. On provider changes, check the official docs before editing the payload or model; do not guess endpoints.

```sh
python scripts/google_tts.py --text-file projects/<slug>/narration.txt --out public/assets/<slug>/voiceover.wav --generate
```

Errors: 400/404 → check current model/voice and request contract; 401/403 → key/project/access; 429 → quota/rate limit. Explain and offer manual AI Studio or the user's recording. Never silently buy credits, rotate accounts or try paid alternatives.

Official references: [speech generation](https://ai.google.dev/gemini-api/docs/speech-generation), [API key guide](https://ai.google.dev/gemini-api/docs/api-key). The REST Interactions single-speaker contract is used by `scripts/google_tts.py`; offline tests cover payload/audio handling, not real account entitlement.
