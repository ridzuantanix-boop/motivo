import {openBrowser, getCompositions, renderStill} from '@remotion/renderer';
import {mkdir} from 'node:fs/promises';
import path from 'node:path';

// Run npm run build first. Static inspection only; this does not review motion/audio.
const serveUrl = path.resolve('dist');
const browser = await openBrowser('chrome');
try {
  await mkdir('out/inspection', {recursive:true});
  const compositions = await getCompositions(serveUrl, {puppeteerInstance:browser});
  for (const composition of compositions.filter(c=>c.id.startsWith('Motivo-'))) {
    for (const frame of [12,60,90]) {
      const output = `out/inspection/${composition.id}-${frame}.png`;
      await renderStill({serveUrl, composition, frame, output, imageFormat:'png', puppeteerInstance:browser, scale:0.5});
      console.log(output);
    }
  }
} finally {await browser.close({silent:true});}
