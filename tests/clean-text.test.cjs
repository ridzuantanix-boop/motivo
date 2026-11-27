const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const Module=require('node:module');
const ts=require('typescript');

const filename=path.resolve(__dirname,'../src/textTiming.ts');
const compiled=ts.transpileModule(fs.readFileSync(filename,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}});
const loaded=new Module(filename,module);
loaded._compile(compiled.outputText,filename);
const {textOpacity}=loaded.exports;

test('title appears only inside its scheduled cue; no text before or after',()=>{
  assert.equal(textOpacity(60,90,90),0);
  assert.equal(textOpacity(135,90,90),1);
  assert.equal(textOpacity(180,90,90),0);
  assert.equal(textOpacity(400,90,90),0);
});
test('long fades remain bounded for short cues and never leave stuck text',()=>{
  for(let f=-10;f<80;f++) {
    const opacity=textOpacity(f,12,3,100);
    assert.ok(opacity>=0&&opacity<=1);
    if(f<12||f>=15) assert.equal(opacity,0);
  }
});
test('a zero-fade cue has exact start and end boundaries',()=>{
  assert.equal(textOpacity(9,10,20,0),0);
  assert.equal(textOpacity(10,10,20,0),1);
  assert.equal(textOpacity(29,10,20,0),1);
  assert.equal(textOpacity(30,10,20,0),0);
});
test('unbounded or invalid text schedules are rejected',()=>{
  for(const args of [[0,0,Infinity],[0,0,0],[0,-1,10],[0,0,10,-1],[NaN,0,10]]) {
    assert.throws(()=>textOpacity(...args));
  }
});
