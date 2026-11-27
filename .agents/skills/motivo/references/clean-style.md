# Clean visual-first direction — all 12 video types

The approved direction is a full-frame visual, followed only when useful by one clearly designed title, then a clean frame again. No corner-label scaffold. The same rule applies to live action, photos and graphics; it is not a single travel preset or one font for every project.

## Default picture

Do not place channel names, MOTIVO/by Pawarna branding, category labels, recipe names, shot numbers, timecodes, counters, location cards, progress bars, side cards or ambient particles across the film by default. No permanent top-left/top-right/bottom-corner text. Repo branding and gallery labels stay outside the sample frame. A brief may explicitly request a logo/disclosure, but that decision is separate from the default, and the result must remain readable and unobtrusive.

Compose the image before adding type. Let subject, crop, light, action, cuts, pauses and sound carry the film. Leave intentional visual-only beats. Do not make ordinary footage look like a dashboard, cover every quiet moment with information, or add text just to fill empty space. A typography-led sequence can make type the main visual; it still does not need corner metadata.

## Purposeful text

For every text cue specify: exact words, why it is needed, in/out times, hierarchy, size and placement. If there is no reason, write `none`. Prefer one dominant text cluster at a time. Use negative space and real contrast, deliberate line breaks and generous margins. Titles should read at phone viewing size; in 1080-minimum-dimension output, the helper defaults to about 130px for titles and 54px for captions, with composition-specific adjustment after inspection. These are starting sizes, not guarantees or fixed universal metrics.

Use short readable copy and a finite entrance/hold/exit. Never hold a title to the end of every shot by accident. No automatic bounce, pill, outline panel, glass card, gradient strip or multicolored word pop. Contrast should usually come from the image/placement; change placement/color or use a deliberate title shot if necessary rather than covering the scene with decorative panels. Use restrained speech-caption shadow only when it aids legibility.

Captions are not automatic. Use them when requested or when the chosen format/accessibility needs them. Time them to the actual speech, keep them concise, generally one or two readable lines, avoid faces/product details and do not run a title over the same reading area. Never hide meaningful words just to obey an arbitrary line count; split/retime them. Lyrics and instructional labels are content, not a reason for permanent branding.

## Applying it to every type

| Type | Needed text, if any | Keep clean |
|---|---|---|
| Faceless & facts | A key term, short question or chapter title at its moment | No constant topic/channel labels or repeated narration above captions |
| Affiliate product | One supported benefit/detail at a time; a clear bounded CTA/price if supplied | No permanent price stack, fake discounts or feature cards across footage |
| Drama/sketch | Requested speech captions, a purposeful opening/ending title | No character-name/location badges over the whole scene |
| Documentary/history | An essential date/source/context cue sized to read; source ledger in notes | No tiny corner fact boxes or archive/channel framing by default |
| Host review | Brief identification only when needed; selected product detail cues | Let the host/objects occupy the picture, no persistent lower third |
| Education/tutorial | Readable labels attached to the actual diagram/step while explained | Multiple essential diagram labels can coexist; no unrelated HUD |
| Lists/comparisons | The current item/criterion, sized and timed to the comparison | No always-on index, counter or dashboard frame |
| Business promo | Needed offer/CTA in a designed finite moment | No repeated logos/price badges/contact clutter on every shot |
| Song/lyrics | One timed phrase/line group, if a lyric video is requested | No permanent song/channel headers; omit lyrics for a visual-only music film |
| Travel/photo essay | Occasional place/title cue if context needs it | Let the landscape breathe; no location card on every image |
| Podcast/excerpt | Requested speech captions or a clearly timed key quote | No fake waveform, speaker labels and progress rail as automatic decoration |
| Motion/brand | Type and geometry may be the main content, with clear hierarchy | No obligatory miniature metadata, footer or decorative counters |

## Implementation and migration

Use `EditorialTitle` from `src/components/CleanTypography.tsx` with required `from` and `durationInFrames`. Without an active cue it renders nothing. `ReadableCaptions` defaults to disabled and needs explicit `enabled` plus timed segments. Cue frames are relative to the enclosing Remotion Sequence; keep that time origin in the shotlist.

The v0.4 `MotionOverlays.tsx` file only re-exports the new typography helpers. Old badges/watermark/progress/side-card/particle exports are removed. In existing projects, remove their imports/usages; replace an actually useful hook/location cue with a timed `EditorialTitle`. Replace requested `FacelessCaptions` with opt-in `ReadableCaptions`. Build a needed factual diagram for its own shot instead of restoring the old generic cards. Do not overwrite personal media or credentials while updating projects.

Before delivery inspect clean-before, title-on and clean-after frames, plus transitions, at phone size and at actual output size. Check all four corners and the lower edge. Watch the draft when authorized: a neat screenshot does not prove that text exits or that motion works. Record unverified checks honestly.
