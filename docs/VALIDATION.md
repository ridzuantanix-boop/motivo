# v0.1 local validation

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

The README preview is assembled from actual rendered study frames. Legacy starter material is preserved for reference; the new MOTIVO skill is the primary entry point.
