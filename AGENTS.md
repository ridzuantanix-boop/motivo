# MOTIVO · by Pawarna

This repository gives a coding agent a video production workflow. It is not a hosted video generator. Read `.agents/skills/motivo/SKILL.md` before creating or editing a video. Read `.agents/rules/video-bm-guidelines.md` for Malay productions. The user's explicit brief takes precedence over defaults.

After install/setup or when a user is new, read `.agents/skills/motivo/references/onboarding.md` and guide them in chat. Do not stop at “installed”: explain visual/voice choices, offer the relevant provider steps, then help form their first brief. Onboarding itself never generates media. Keep API keys out of chat, logs and command arguments; use the local editor or the user's own hidden-input terminal. `START_HERE.md` is the beginner entry point.

Show the video-type menu from onboarding for new users or when asked what MOTIVO can make; use `docs/VIDEO_TYPES.md` for requirements. For an existing brief, skip unnecessary menu questions. Drama and sketches use `.agents/skills/motivo/references/drama.md`; do not confuse narration with on-camera lip-sync.

Make choices visual: offer `docs/STYLE_GALLERY.md` with the checked-in `docs/gallery/overview.jpg` alongside the menu. The 12 posters are illustrated concepts, not finished video frames. Let users choose, combine or change a poster's direction; do not regenerate images merely to show the existing gallery.

Use `npm run setup`, `npm run typecheck`, and `npm run studio`. On Windows use `npm.cmd` / `npx.cmd`. `npm run build` bundles the project; it does not render or spend API credits. Rendering is an explicit separate operation.

No API is needed for local motion graphics or user-supplied media. Never imply that a coding-agent subscription supplies media-generation API access. Nexabot is optional; its bundled integration is inherited and must be verified against current provider documentation before generation. Never commit `.env` or user media. Never publish, upload, or incur generation costs without authorization for that action.

Preserve the original components as legacy building blocks; do not use their glass panels, badges, particles, or progress bars as the default visual identity. New work should follow a project-specific direction and the quality gate in the skill. Do not claim photorealism, licensing clearance, or monetization eligibility without evidence.
