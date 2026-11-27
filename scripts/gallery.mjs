import {openBrowser, getCompositions, renderStill} from '@remotion/renderer';
import {mkdir} from 'node:fs/promises';
import path from 'node:path';

// After npm run build. Static art-direction concepts, not finished video samples.
const serveUrl=path.resolve('dist');
const browser=await openBrowser('chrome');
try {
  await mkdir('docs/gallery',{recursive:true});
  const compositions=await getCompositions(serveUrl,{puppeteerInstance:browser});
  const posters=compositions.filter(c=>c.id.startsWith('Gallery-'));
  for (let i=0;i<posters.length;i++) {
    const composition=posters[i];
    const slug=composition.id.slice('Gallery-'.length);
    const output=`docs/gallery/${String(i+1).padStart(2,'0')}-${slug}.jpg`;
    await renderStill({serveUrl,composition,frame:0,output,imageFormat:'jpeg',jpegQuality:94,puppeteerInstance:browser});
    console.log(output);
  }
  if(posters.length!==12) throw new Error(`Expected 12 concept posters, got ${posters.length}`);
} finally {await browser.close({silent:true});}
