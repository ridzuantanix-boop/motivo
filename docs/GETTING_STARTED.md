# Your first MOTIVO session

**Beginner?** Start with [one sentence to your agent](../START_HERE.md). No need to memorize the commands below. To install from a link, ask your coding agent to clone https://github.com/ridzuantanix-boop/motivo into a new folder, read `AGENTS.md`, install dependencies, check setup and guide your first video without generating media yet.

## 1. Get the project

Download **Code → Download ZIP** from this repository, or clone it. Extract/open the resulting folder in your coding agent. The folder containing `package.json` is the project root.

Install Node.js 22 or newer. Python 3.10+ is needed for Nexabot; FFmpeg and FFprobe are needed for media inspection/preparation. Add installed tools to PATH and reopen the terminal.

```sh
npm ci
npm run setup
npm run typecheck
npm run studio
```

Windows PowerShell: replace `npm` with `npm.cmd` and `npx` with `npx.cmd` if script execution policy blocks them. Setup never installs system tools, overwrites `.env`, calls a paid API, or renders video. A missing optional Python/FFmpeg tool is reported without preventing local graphic studies.

## 2. Give the agent its entry point

```text
Read AGENTS.md, then .agents/skills/motivo/SKILL.md.
Use MOTIVO for this project. Run local checks, but do not generate a video yet.
```

Use this explicit instruction in Codex, Antigravity, Claude Code, or another agent with file editing and terminal access. This is a manual project-local workflow; automatic skill discovery and tool permissions vary. Only the local commands have been validated here, not every agent product.

After setup, say **“Buka MOTIVO dan bimbing aku buat video pertama. Aku baru mula.”** The agent should offer relevant visual and voice choices rather than stop at “installed”. Read [keys and voice routes](PROVIDERS.md) for Nexabot, manual Google AI Studio and optional Google API narration. You can begin without any provider key.

## 3. Supply a brief and assets

Put your own media under `public/assets/<project>/`. These files stay ignored by Git. Include the audience, platform/aspect, desired duration, message, factual sources and audio preference. If unspecified, the agent can propose a direction. You do not need to choose a style name.

```text
Use MOTIVO. Audience: Malaysian students. Make a 30-second vertical
product-detail video from public/assets/desk-lamp/. Use only the supplied
specifications. Modern editorial direction. My narration is voice.wav.
No AI generation, no publishing. Write the direction and shotlist, then build it.
```

Agent plans go under `projects/<slug>/`; rendered files go under `out/`. Both stay local. No Pawarna watermark is mandatory on customer videos.

## 4. Preview, inspect, export

Studio contains three silent design studies in two aspect ratios. To build and extract all study samples:

```sh
npm run build
npm run inspect
```

Inspection creates 18 PNGs, not a video. On first use Remotion may download a browser. Rendering requires a supported local environment and adequate disk/memory. For explicit export:

```sh
npx remotion render src/index.ts Motivo-pressroom-Landscape out/study.mp4
```

Customer compositions should use their own IDs. Check actual playback and listen to audio before calling a production finished. Still-frame checks cannot prove temporal realism or audio quality.

## 5. Optional providers

Read the [provider guide](PROVIDERS.md). For hidden local input use `npm run connect -- nexabot` or `npm run connect -- google` in your own interactive terminal (Python 3.10+). These commands store the selected key without printing it, preserve other `.env` settings, and make no API calls. Alternatively edit the appropriate line in `.env` locally. Do not paste a key into chat.

Google AI Studio manual uses the [speech playground](https://aistudio.google.com/generate-speech), then a downloaded audio file; no Google key is needed in MOTIVO. Automatic Google narration is a separate API route with your own key, account quota and explicit generation authorization. `npm run providers` reports key presence only; `npm run provider:check -- <provider>` performs an explicit read-only check.

### Nexabot

Leave `.env` empty for motion graphics and supplied media. To use Nexabot, put your own key in `.env`:

```env
NEXABOT_API_KEY=your_actual_key
```

The client also supports `NEXABOT_API_KEY` in the process environment. Verify current provider documentation and authorize a spending limit before generation. The inherited API notes are historical and generation is not exercised by setup/CI. A coding-agent subscription is separate from media-provider access. Never paste credentials into issues or commit them.
