# Your first MOTIVO session

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

## 5. Optional Nexabot

Leave `.env` empty for motion graphics and supplied media. To use Nexabot, put your own key in `.env`:

```env
NEXABOT_API_KEY=your_actual_key
```

The client also supports `NEXABOT_API_KEY` in the process environment. Verify current provider documentation and authorize a spending limit before generation. The inherited API notes are historical and generation is not exercised by setup/CI. A coding-agent subscription is separate from media-provider access. Never paste credentials into issues or commit them.
