# Visual dahulu. Teks bila perlu.

MOTIVO v0.4 uses the clean direction across all 12 video types. A scene can remain completely free of text. If a title helps, it is large, composed in the image's negative space, and scheduled to enter and leave. There is no automatic top-left label, top-right watermark, progress rail, information card or branded footer in exported video.

## What you will see in Studio

- `StarterDemoVideo`: a landscape still-based design demo. Clean image at the start, “Lihat perlahan.” from 3–6 seconds with a restrained fade, then clean image again.
- `CleanScene-Portrait`: the same principle with a deliberate portrait crop and line breaks.
- `Motivo-*`: Pressroom, Signal and Atelier motion studies with visual-only intervals and one finite title cue per beat; no small header/footer metadata.
- `Gallery-*`: single-frame illustrated posters. Category names, branding and concept notices are outside the artwork in gallery documentation, not corner labels inside the sample.

The coastline is an AI-generated illustrative still, not filmed footage or proof of a real location. Source and generation prompt: [asset note](../public/demo/ASSET.md). The gallery remains illustrated concept art. None of these examples establishes motion realism or replaces a review of a finished film.

## Text that belongs to the content

Clean does not mean hiding useful information. Requested speech captions, timed lyrics, a diagram's labels, essential context or a supplied CTA can appear when needed. Make them clear and properly timed. Do not add a second permanent header explaining what the caption already says. Avoid placing captions and a headline in the same reading space.

For an infographic or typography-led scene, the words may be the primary content. For a drama, host shot or landscape, let the image and sound lead. The [agent direction guide](../.agents/skills/motivo/references/clean-style.md) describes how this applies to every category.

## Example cue

```tsx
import {EditorialTitle, ReadableCaptions} from './components/CleanTypography';

// At 30fps: one title from seconds 3 to 6, not a label for the whole film.
<EditorialTitle text="Lihat perlahan." from={90} durationInFrames={90} />

// Add only when speech captions are wanted; segments use actual audio timing.
<ReadableCaptions enabled={true} segments={captions} />
```

`from` is relative to the enclosing Remotion Sequence. Default title size is about 130px and caption size about 54px for 1080-minimum-dimension output; the landscape photo demo uses 150px. Inspect actual size and a phone-sized preview; adjust to the composition. No universal font size or placement guarantees readability on every shot.

## Updating an existing MOTIVO project

Ask your agent:

> Update MOTIVO without overwriting my .env or media. Read AGENTS.md and apply the clean style to my existing compositions. Remove automatic corner labels, watermark, cards and progress. Keep necessary captions, lyrics and diagram labels readable and timed. Show before/on/after frames before a final render.

Legacy named exports such as `TopChannelWatermark`, `IntroHookBadge`, `LocationLowerThird`, `InfoSideCard`, `TimelineProgressBar`, `FacelessCaptions` and decorative particle/cards were removed in v0.4. `MotionOverlays.tsx` only re-exports the new clean helpers. Existing generated compositions importing old names need migration; remove decoration, replace useful title cues with `EditorialTitle`, and replace requested captions with opt-in `ReadableCaptions`. Do not delete personal scripts or media to make the update compile.

## Verification

`npm run test:clean` checks finite title timing. After `npm run build`, `npm run inspect:clean` produces 36 static review frames: landscape/portrait clean → title → clean, six motion studies at three moments and 12 posters. The still-based scene's before/after images must match exactly and the title frame must differ. The Linux CI job also runs this check and uploads review images as an artifact. These checks do not watch motion or listen to audio.
