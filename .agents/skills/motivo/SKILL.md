---
name: motivo
description: Guide first-time MOTIVO users through setup, provider and voice choices, then direct, compose, inspect and render videos in this Remotion repository using supplied media or optional providers.
---

# MOTIVO — by Pawarna

Turn a brief into an intentional edit. A recipe supplies narrative scaffolding, not a compulsory layout. Default to Bahasa Melayu unless the user requests another language. Adapt length, aspect ratio, tone, and delivery to the actual brief.

For a new user, setup request, or provider/voice question, read [onboarding.md](references/onboarding.md). Guide them through the relevant choices instead of leaving a command list. Read [providers.md](references/providers.md) only for a selected provider route. Google AI Studio manual needs no local API key; Google API narration is an optional separate connection with a real client. No provider is mandatory for supplied media.

## Work from evidence

1. Inspect available images, clips, audio, and project code. Run setup checks. Identify missing assets and factual claims. Ask only for decisions that cannot reasonably be inferred; progress on independent work. Do not invent product tests, testimonials, prices, or results.
2. Write a short `projects/<slug>/direction.md`: audience, central idea, hook, intended feeling, selected recipe, visual reference/provenance, typography, palette, motion rules, audio plan, and an avoid list specific to this brief. Describe references when no image tool is available; do not pretend to have seen them.
3. Read [recipes.md](references/recipes.md) for narrative construction and [art-direction.md](references/art-direction.md) for motion design. Plan shots in `projects/<slug>/shotlist.md` with duration, story purpose, source asset, crop/focal point, sound, and caption. A different beat should have a different visual job. If the user already authorized production, a reviewable direction need not become an extra approval round.
4. For generated live action only, read [realism.md](references/realism.md), plus the inherited `.agents/skills/nexabot-video-studio/SKILL.md` for provider-specific historical settings. Verify current API details before use. Work within the authorized budget; stop on repeated defects or exhausted budget, and propose a simpler shot or real asset. Never loop generation indefinitely.
5. Implement a new composition in `src/`, register it in `Root.tsx`, and keep content separate from layout. The demo's three art directions are examples, not a style ceiling. Match target aspect ratio deliberately; do not crop a landscape design into portrait. Use local fonts/assets for reproducible exports. Use frame-based animation, seeded randomness, and frame-derived audio timing; avoid CSS transitions, timers, remote runtime dependencies, and arbitrary overlapping overlays.
6. Typecheck, bundle, and inspect stills at opening, each cut, mid-move, and ending. Then review a draft in motion and listen to audio when rendering is authorized. If tools cannot play video/audio, say which checks were visual/static only. Use [quality-gate.md](references/quality-gate.md); fix failures before final export or explicitly label unresolved limitations.
7. Deliver the output path, dimensions, duration, audio status, source/licensing notes, and actual checks performed. Agent review is not human review. Never promise virality, income, platform approval, or perfect realism.

## Commands

`npm run setup` checks prerequisites and creates `.env` without overwriting it. `npm run studio` opens the composition picker. `npm run typecheck` and `npm run build` validate without producing video. For explicit output use `npx remotion render src/index.ts <CompositionId> out/<name>.mp4 --codec=h264 --crf=18`; for frame inspection use `npx remotion still src/index.ts <CompositionId> out/<name>.png --frame=<frame>`.

API keys stay local. Preserve host audio at playbackRate 1 for lip-sync. For narration use a supplied recording or an explicitly configured natural-voice provider; do not silently substitute synthetic narration. Do not generate a video merely to test setup.
