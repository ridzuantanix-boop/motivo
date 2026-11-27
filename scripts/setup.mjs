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
const envLines = readFileSync('.env','utf8').replace(/^\uFEFF/, '').split(/\r?\n/);
for (const [label, name] of [['Nexabot', 'NEXABOT_API_KEY'], ['Google API narration', 'GEMINI_API_KEY']]) {
  const line = envLines.find(x => x.trim().startsWith(`${name}=`));
  const key = (process.env[name] || line?.slice(line.indexOf('=') + 1) || '').trim().replace(/^["']|["']$/g, '');
  const configured = Boolean(key) && !/letak|gantikan|your_key|your_actual_key|xxxxxxxx|paste_here/i.test(key);
  console.log(`${label}: ${configured ? 'key present (not authenticated)' : 'optional; not connected'}`);
}
if (!existsSync('node_modules/remotion')) {console.log('Install dependencies with npm install (npm.cmd on Windows).'); failed = true;}
console.log(failed ? 'Resolve required prerequisites before production.' : 'Local graphics ready. Run npm run studio. Install missing media tools before media production. No API calls made.');
console.log('\nBaru mula? Cakap kepada agent: "Buka MOTIVO dan bimbing aku buat video pertama. Aku baru mula."');
console.log('Panduan: START_HERE.md | Provider dan suara: docs/PROVIDERS.md');
console.log('Google AI Studio manual tidak memerlukan API key dalam MOTIVO. Jangan tampal key dalam chat.');
process.exitCode = failed ? 1 : 0;
