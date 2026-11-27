import React from 'react';
import {AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';

export type StudyStyle = 'pressroom' | 'signal' | 'atelier';
export type StudyProps = {style: StudyStyle};
const clamp = {extrapolateLeft: 'clamp' as const, extrapolateRight: 'clamp' as const};
const colors = {pressroom: ['#ede9df','#24231f','#c63c29'], signal: ['#d5fb37','#181b16','#181b16'], atelier: ['#441e2a','#f0e6d6','#bd9e7c']} as const;

// Original geometric/type study. No API, external fonts, audio, or stock assets.
export const MotivoStudy: React.FC<StudyProps> = ({style}) => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const portrait = height > width;
  const sx = width / (portrait ? 1080 : 1920);
  const sy = height / (portrait ? 1920 : 1080);
  const [bg, ink, accent] = colors[style];
  const beat = frame < 100 ? 0 : frame < 220 ? 1 : 2;
  const local = frame - [0,100,220][beat];
  const reveal = interpolate(local,[0,24],[100,0],{...clamp,easing:Easing.bezier(.16,1,.3,1)});
  const move = interpolate(local,[0,90],[0,1],clamp);
  const base: React.CSSProperties = {background:bg,color:ink,fontFamily:style === 'signal' ? 'Arial, sans-serif' : 'Georgia, serif',overflow:'hidden'};
  const words = [['ADA','SEBAB.'],['SETIAP','GERAK.'],['BINA','MAKNA.']][beat];
  return <AbsoluteFill style={base}>
    <AbsoluteFill style={{transform:`scale(${sx}, ${sy})`,transformOrigin:'top left',width:portrait?1080:1920,height:portrait?1920:1080}}>
      <div style={{position:'absolute',left:72,right:72,top:56,display:'flex',justifyContent:'space-between',fontFamily:'Arial, sans-serif',fontSize:21,letterSpacing:3,borderTop:`1px solid ${ink}`,paddingTop:18}}><span>MOTIVO</span><span>KAJIAN GERAK / 0{beat+1}</span></div>
      {style === 'pressroom' && <div style={{position:'absolute',right:portrait?60:110,top:portrait?850:180,color:accent,fontSize:portrait?650:780,lineHeight:.9,fontStyle:'italic',opacity:.17,transform:`translateY(${-move*35}px)`}}>{beat+1}</div>}
      {style === 'signal' && <div style={{position:'absolute',right:portrait?-180:50,top:portrait?1100:200,width:600,height:600,transform:`rotate(${-25+move*12}deg)`,border:`100px solid ${ink}`,borderRadius:beat===1?'50%':'0'}} />}
      {style === 'atelier' && <div style={{position:'absolute',right:portrait?180:210,top:portrait?1000:210,width:portrait?600:420,height:portrait?600:620,border:`1px solid ${accent}`,borderRadius:'50% 50% 0 0',transform:`translateY(${-move*22}px)`}}><div style={{position:'absolute',inset:36,border:`1px solid ${accent}`,borderRadius:'50% 50% 0 0'}} /></div>}
      <div style={{position:'absolute',left:72,top:portrait?300:245,width:portrait?940:1300,clipPath:`inset(0 0 ${reveal}% 0)`}}>
        {words.map((word,i)=><div key={word} style={{fontSize:style==='signal'?(portrait?172:210):(portrait?160:200),fontWeight:style==='signal'?900:400,lineHeight:1.02,letterSpacing:style==='signal'?-12:-8,fontStyle:style==='atelier'&&i===1?'italic':'normal',color:i===1&&style==='pressroom'?accent:ink,transform:`translateX(${(reveal/100)*(i?65:30)}px)`}}>{word}</div>)}
      </div>
      <div style={{position:'absolute',left:76,bottom:portrait?230:170,maxWidth:portrait?750:630,fontFamily:'Arial, sans-serif',fontSize:portrait?32:26,lineHeight:1.45,opacity:interpolate(local,[20,40],[0,1],clamp)}}>{['Bukan sekadar bergerak. Ada cerita di sebalik setiap keputusan.','Potongan yang tepat. Ruang untuk bernafas. Satu idea yang jelas.','Daripada perbualan kepada bahasa visual anda sendiri.'][beat]}</div>
      <div style={{position:'absolute',bottom:58,left:72,right:72,display:'flex',justifyContent:'space-between',borderTop:`1px solid ${ink}`,paddingTop:20,fontFamily:'Arial, sans-serif',fontSize:21,letterSpacing:2}}><span>{style.toUpperCase()}</span><span>by Pawarna</span></div>
    </AbsoluteFill>
  </AbsoluteFill>;
};
