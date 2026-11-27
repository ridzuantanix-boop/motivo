import {spawnSync} from 'node:child_process';
import {existsSync, copyFileSync, readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
process.chdir(fileURLToPath(new URL('..', import.meta.url)));
const checks = [['Node.js', process.execPath, ['--version'], true], ['Python (optional Nexabot client)', 'python', ['--version'], false], ['FFmpeg (media preparation)', 'ffmpeg', ['-version'], false], ['FFprobe (media inspection)', 'ffprobe', ['-version'], false]];
let failed = Number(process.versions.node.split('.')[0]) < 22;
if (failed) console.log('Node.js 22+ is required.');
for (const [label, command, args, required] of checks) {
  const r = spawnSync(command, args, {encoding: 'utf8'});
  console.log(`${r.status === 0 ? 'OK' : 'MISSING'} ${label}: ${(r.stdout || r.stderr || r.error?.message || '').split(/\r?\n/)[0]}`);
  if (r.status !== 0 && required) failed = true;
  if (command === 'python' && r.status === 0) {
    const version = (r.stdout || r.stderr).match(/Python (\d+)\.(\d+)/);
    if (version && (Number(version[1]) < 3 || (Number(version[1]) === 3 && Number(version[2]) < 10))) console.log('Upgrade Python to 3.10+ before using Nexabot.');
  }
}
if (!existsSync('.env')) {copyFileSync('.env.example', '.env'); console.log('Created .env. No credentials required for local compositions.');}
const configured = /^NEXABOT_API_KEY=nxb_.+/m.test(readFileSync('.env','utf8')) && !/LETAK|gantikan|YOUR_KEY|xxxxxxxx/.test(readFileSync('.env','utf8'));
console.log(`Nexabot: ${configured ? 'key present (not authenticated)' : 'optional; no usable key configured'}`);
if (!existsSync('node_modules/remotion')) {console.log('Install dependencies with npm install (npm.cmd on Windows).'); failed = true;}
console.log(failed ? 'Resolve required prerequisites before production.' : 'Local graphics ready. Run npm run studio. Install missing media tools before media production. No API calls made.');
process.exitCode = failed ? 1 : 0;
