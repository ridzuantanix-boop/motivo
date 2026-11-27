import {openBrowser,getCompositions,renderStill} from '@remotion/renderer';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';

const serveUrl=path.resolve('dist');
const output='out/clean-review';
await mkdir(output,{recursive:true});
const browser=await openBrowser('chrome');
try {
  const compositions=await getCompositions(serveUrl,{puppeteerInstance:browser});
  const rendered=[];
  for (const id of ['StarterDemoVideo','CleanScene-Portrait']) {
    const composition=compositions.find(c=>c.id===id);
    assert.ok(composition,`Missing ${id}`);
    const files=[];
    for (const frame of [60,135,240]) {
      const file=`${output}/${id}-${frame}.png`;
      await renderStill({serveUrl,composition,frame,output:file,imageFormat:'png',scale:.5,puppeteerInstance:browser});
      files.push(await readFile(file));
      rendered.push(file);
    }
    assert.ok(files[0].equals(files[2]),`${id}: clean frames before and after title must match`);
    assert.ok(!files[0].equals(files[1]),`${id}: the scheduled title must actually appear`);
  }
  for (const composition of compositions.filter(c=>c.id.startsWith('Motivo-'))) {
    for (const frame of [12,60,90]) {
      const file=`${output}/${composition.id}-${frame}.png`;
      await renderStill({serveUrl,composition,frame,output:file,imageFormat:'png',scale:.5,puppeteerInstance:browser});
      rendered.push(file);
    }
  }
  for (const composition of compositions.filter(c=>c.id.startsWith('Gallery-'))) {
    const file=`${output}/${composition.id}.png`;
    await renderStill({serveUrl,composition,frame:0,output:file,imageFormat:'png',scale:.5,puppeteerInstance:browser});
    rendered.push(file);
  }
  await writeFile(`${output}/review.json`,JSON.stringify({checks:{cleanBeforeAfter:'pass',titleAppears:'pass'},frames:rendered,motionPlayback:'not reviewed',audio:'silent demos',note:'Static output checks, not a human review or live-action realism guarantee.'},null,2));
  console.log(`Clean review: ${rendered.length} stills. Before/on/after checks passed. No video rendered.`);
} finally {await browser.close({silent:true});}
