# Local validation and provider limitations

## v0.4 clean direction

- Four finite-text timing tests plus 16 existing offline provider tests pass locally. New clean compositions typecheck. The old overlay implementations/exports are removed; all 12 categories now follow the same clean-frame rules.
- All 12 gallery SVG/JPEGs were regenerated without corner metadata, footer branding, tiny supporting text or border UI, and the updated contact sheet was visually inspected. Category labels and concept notices are outside the artwork.
- The new scene uses an AI-generated illustrative still from built-in imagegen, stored in `public/demo/coast-clean.jpg` with its prompt/source note. No Nexabot/Google generation or video export was performed for this change.
- Linux CI runs `inspect:clean`: 36 stills, exact clean-before/after equality and a different title-on frame in landscape/portrait. Review artifacts are available on the associated workflow run. This is static inspection, not playback/audio validation. See the live workflow link below for the current result.

## Historical v0.1–v0.3 checks

Validated on Windows, Node 22.18.0, Python 3.13.6, FFmpeg/FFprobe 9.0.1.

- Skill frontmatter validator: passed.
- Local setup: passed; created an empty optional credential file without contacting Nexabot.
- TypeScript: passed after dependency installation completed.
- Remotion browser bundle: passed.
- All six MOTIVO compositions: rendered frames 60, 160 and 280 (18 PNGs total). Contact sheet visually inspected for text overflow, missing elements and layout issues. No obvious overlap observed at these sampled frames.
- No video rendered. Motion playback and audio have not been reviewed. Demo studies are intentionally silent.
- No Nexabot generation or credit use. Provider endpoints and generation quality not validated in this release.
- Cross-agent installation remains unverified. Hosted CI checks Windows and Linux; see the [live workflow results](https://github.com/ridzuantanix-boop/motivo/actions/workflows/check.yml).
- Public-release pass: four offline credential-handling tests passed; staged source credential-pattern scan and relative Markdown link checks passed. `.env` and local media are excluded. Remotion package versions are aligned and pinned; CI targets Windows and Linux.
- Clean-install pass: `npm ci --no-audit --no-fund`, followed by TypeScript, browser bundle and setup checks, completed successfully. The public repository is available at [ridzuantanix-boop/motivo](https://github.com/ridzuantanix-boop/motivo).

The original v0.1 preview was assembled from rendered study frames. That old preview and overlay system were replaced in v0.4; the older records below describe their historical validation, not the current clean-frame output.

## v0.2 onboarding

- Sixteen offline Python tests pass, covering the inherited client, local credential updates, placeholder/multiline rejection, environment precedence, hidden-input noninteractive refusal, redacted status, Google TTS no-network preflight, output protection, request credential placement and WAV/PCM handling.
- Skill validation passes. Provider status and setup do not make network requests. The Google client uses the official single-speaker REST Interactions contract checked on 2026-11-27.
- Google and Nexabot live generation have not been tested in this release. No real provider key, credit or generated customer audio is used by the tests. Browser-based AI Studio account availability and first-run behavior across all agents remain unverified.
- Narration payloads and audio responses use mocked fixtures in tests; successful offline tests are not proof of provider entitlement or live output quality.

## v0.2.1 catalog and drama direction

Documentation and skill update only: numbered use cases, a seventh narrative recipe and conditional drama guidance. Relative links and skill metadata are checked. No drama video, actor-consistency run or multi-speaker generation was produced or tested. Existing composition code and provider behavior are unchanged.

## v0.3 visual gallery

- Twelve original SVG posters parsed as valid XML and exported sequentially as JPEGs, plus a contact-sheet overview. Static visual inspection checks typography, borders, crop and image loading; these are concept illustrations, not finished video frames.
- New single-frame Studio compositions typechecked locally. The local full browser bundle hit an out-of-memory error while the computer was under memory pressure; documentation JPEGs were exported with the optional low-memory PyMuPDF 1.26.7 path instead. Hosted CI validates the browser bundle separately; see live results above.
- SVGs use solid vector fills for consistent low-memory export. Font/rasterizer differences can remain; no fonts, stock photos, real actor likenesses or third-party artwork are bundled with this gallery.
- No video, audio, provider credit or API-generated imagery used for the gallery. Poster artwork and descriptions demonstrate direction, not temporal motion, lip-sync or photorealism.
