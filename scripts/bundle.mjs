import {bundle} from '@remotion/bundler';
import path from 'node:path';
const result = await bundle({entryPoint: path.resolve('src/index.ts'), outDir: path.resolve('dist')});
console.log(`MOTIVO bundle ready: ${result}. No video rendered.`);
