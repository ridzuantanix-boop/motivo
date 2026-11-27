# Changelog

## 0.4.1 — 2026-11-27

- Replaced abstract SVG posters with 12 generated example scenes that make each video genre recognizable: drama actors, product use, a presenter, podcast speakers and more.
- Added plain-language explanations of what viewers see/hear in each format, with source prompts and AI provenance outside the images.
- Retired the old SVG generator/export path; gallery metadata/docs now come from a JSON manifest. Clean styling and finite title behavior remain unchanged.

## 0.4.0 — 2026-11-27

- Clean visual-first direction for all 12 types: no default corner labels, watermark, persistent cards, progress or branded footer.
- Replaced legacy overlay exports with required-duration `EditorialTitle` and opt-in `ReadableCaptions`; existing imports need migration.
- New landscape/portrait still-based clean → title → clean demo using an AI-generated illustrative coastal image; stripped metadata and small supporting text from motion studies/gallery art.
- Finite-text timing tests and Linux CI static inspection of 36 frames, including exact before/after checks. No video or paid provider media generation is part of validation.

## 0.3.0 — 2026-11-27

- Twelve original SVG art-direction posters with checked-in JPEG previews and a numbered overview.
- Visual gallery linked from README, beginner entry, video catalog and conversational onboarding.
- Single-frame `Gallery-*` Studio compositions and optional documentation exporters; no video or paid assets generated.
- Poster concepts are clearly distinguished from finished video or generated live-action samples.

## 0.2.1 — 2026-11-27

- First-run numbered catalog of 12 video use cases, with asset/provider requirements.
- Short drama/sketch recipe and direction guide: script, character bible, coverage, voice continuity and episodic notes.
- Distinct routes for supplied footage, illustrated drama and optional generated clips; narration is not claimed as lip-sync. No finished drama or live generated sample tested in this update.

## 0.2.0 — 2026-11-27

- Guided first-run agent conversation: video idea, visual sources, voice route, then a first brief.
- Beginner entry point, provider guide, manual AI Studio handoff and API key guidance.
- Hidden local key entry, redacted status and explicit read-only provider checks.
- Optional Google TTS REST client with no-network default preflight and opt-in generation.
- Offline tests for secret preservation, no-network onboarding, payload and audio handling. No live paid generation tested or performed.

## 0.1.0 — 2026-11-27

First public-ready MOTIVO starter, by Pawarna.

- Agent director workflow, six narrative recipes and evidence-based delivery gate.
- Pressroom, Signal and Atelier studies in portrait and landscape.
- Optional inherited Nexabot integration and live-action realism guidance.
- Local setup, bundle, static inspection, contribution guidance and CI.

This release is a starter kit. It does not include a hosted service, universal agent installer, automatic footage generation, or guaranteed monetization/photorealism.
