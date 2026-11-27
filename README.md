![MOTIVO by Pawarna — Turn your agent into a director-led video studio](docs/hero.svg)

<p align="center">
  <a href="https://github.com/ridzuantanix-boop/motivo/actions/workflows/check.yml"><img alt="CI validation" src="https://github.com/ridzuantanix-boop/motivo/actions/workflows/check.yml/badge.svg"/></a>
  <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/license-MIT-d5fb37?style=flat-square&amp;labelColor=171b18"/></a>
  <img alt="Node 22+" src="https://img.shields.io/badge/node-22%2B-d5fb37?style=flat-square&amp;labelColor=171b18"/>
  <img alt="Release 0.1.0" src="https://img.shields.io/badge/starter-v0.1.0-d5fb37?style=flat-square&amp;labelColor=171b18"/>
</p>

<p align="center"><a href="#local-setup">Quick start</a> · <a href="docs/GETTING_STARTED.md">Full guide</a> · <a href="docs/EXAMPLES.md">Prompt library</a> · <a href="docs/README.ms.md">Bahasa Melayu</a> · <a href="CONTRIBUTING.md">Contribute</a></p>

# Your agent has an idea. Give it a director's toolkit.

Give your coding agent a brief. Build faceless stories, product videos, and deliberate motion graphics through conversation, using Remotion and FFmpeg locally.

**Agent-first · Local rendering · Open source · Optional Nexabot**

![Pressroom, Signal and Atelier: original MOTIVO composition studies](docs/style-studies.jpg)

MOTIVO is a repository-based skill and production kit, not a dashboard. Your agent supplies reasoning and code execution. Supplied media and motion graphics need no media-generation API. Generating new AI footage or voices requires a separately configured provider and may cost money.

## Start with a conversation

```text
Read AGENTS.md and use the MOTIVO skill. Check setup without making a video.
```

Then try:

```text
Buat video affiliate 30 saat daripada gambar dalam public/assets/botol/.
Gaya editorial premium, 9:16. Jangan reka testimoni atau harga.
```

```text
Turn my script and photos into a faceless essay. Propose an art direction,
build a shotlist, then compose the edit. Use my recorded narration.
```

```text
Create an original motion explainer. Avoid dashboard cards and stock
animation patterns. Explain the mechanism visually, with room to read.
```

## Local setup

Use Node.js 22+, Python 3.10+, FFmpeg and FFprobe on PATH. Python is used by the optional Nexabot client; FFmpeg supports media preparation and inspection.

```sh
git clone https://github.com/ridzuantanix-boop/motivo.git
cd motivo
npm ci
npm run setup
npm run typecheck
npm run studio
```

On Windows PowerShell use `npm.cmd` and `npx.cmd`. Setup creates `.env` only when absent, checks tools, and never contacts Nexabot. Leave the API key empty for local work. Never commit credentials.

Open a `Motivo-*` composition: **Pressroom**, **Signal**, or **Atelier**, independently laid out for portrait and landscape. These are silent, original typography/geometry studies, not finished customer videos. `StarterDemoVideo` remains a legacy reference.

| Direction | Visual language | Starting use |
|---|---|---|
| Pressroom | Paper, ink, monumental serif, editorial asymmetry | Essays and culture |
| Signal | Acid green, bold type, directional geometry | Explainers and launches |
| Atelier | Oxblood, parchment, restrained type, architectural curves | Product narratives |

Six **narrative recipes**, separate from styles: faceless essay, ranked discovery, product detail, product comparison, visual explainer, place & culture. These are agent instructions, not six one-click video generators. The agent adapts code and real assets to each brief.

## Connect your agent

- **Codex:** open the repo as a workspace and explicitly ask it to read `AGENTS.md` and `.agents/skills/motivo/SKILL.md`. A global install is unnecessary for this project-local workflow.
- **Antigravity or another coding agent:** open the folder and ask it to read those same files. Import through the agent's supported skill mechanism if available. Automatic discovery varies and is not assumed.
- **Other agents:** an agent that can read files, edit TSX and execute Node commands can follow the manual entry point. Cross-agent integrations have not all been independently tested.

An agent subscription does not automatically supply programmatic voice, image, or video generation.

## Production workflow

Brief → asset audit → art direction → shotlist → composition → inspected draft → final export.

Keep direction, sources, shot timing, and review evidence in `projects/<slug>/`. MOTIVO discourages generic glass panels, automatic particles, endless springs and uniform layouts. It calls for subject-specific decisions and records what was actually inspected. No preset guarantees artistic quality, photorealism, virality, monetization eligibility, or income.

The live-action guide covers continuity, anatomy, physics, product fidelity, speech, modest wardrobe for Malay productions, and temporal inspection. Repair or replace defective footage. Verify the inherited Nexabot endpoint/model guidance against current official documentation before paid generation.

## Commands

| Command | Result |
|---|---|
| `npm run setup` | Local prerequisite check; creates optional `.env` |
| `npm run studio` | Interactive composition preview |
| `npm run typecheck` | TypeScript validation |
| `npm run build` | Browser bundle in `dist/`; no video or API calls |
| `npm run inspect` | After build: 18 static frames across three styles and two ratios in `out/inspection/`; not a motion/audio review |
| `npx remotion still src/index.ts Motivo-pressroom-Landscape out/frame.png --frame=60` | Inspection frame |
| `npx remotion render src/index.ts Motivo-pressroom-Landscape out/study.mp4` | Explicit MP4 export |

Frame rendering may download Remotion's browser on first use. The studies contain no audio; customer productions use supplied recordings, licensed tracks, or explicitly configured voice generation.

## Repository map

```text
AGENTS.md                          Project entry point
.agents/skills/motivo/              Director workflow and review references
.agents/skills/nexabot-video-studio/ Preserved starter provider guidance
src/MotivoStudy.tsx                 Three direction studies
src/components/                    Optional legacy starter components
scripts/setup.mjs                  Non-destructive local check
scripts/nexabot_client.py           Optional inherited provider client
```

## Troubleshooting and sharing

Missing tool: install it, add it to PATH, and reopen the terminal. API `401`: replace the optional key; local compositions still work. Missing media: supply assets and correct paths. A bundle passing does not prove motion/audio quality; inspect output.

Code is MIT licensed, **by Pawarna**. Dependencies retain their licenses; check Remotion's current licensing terms for your use. User assets, music, fonts, provider usage, and generated outputs are not licensed by this repo's MIT license. MOTIVO requires no export watermark. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Release status

**v0.1.0 is a starter release.** Local checks and six composition studies have been validated; universal agent installation and provider generation have not. See the [validation record](docs/VALIDATION.md) and [changelog](CHANGELOG.md). Follow [SECURITY.md](SECURITY.md) when reporting sensitive issues.
