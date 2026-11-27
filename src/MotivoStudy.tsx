import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {EditorialTitle} from './components/CleanTypography';

export type StudyStyle = 'pressroom' | 'signal' | 'atelier';
export type StudyProps = {style: StudyStyle};
const colors={pressroom:['#ede9df','#24231f','#c63c29'],signal:['#d5fb37','#181b16','#181b16'],atelier:['#441e2a','#f0e6d6','#bd9e7c']} as const;

export const MotivoStudy: React.FC<StudyProps> = ({style}) => {
  const frame=useCurrentFrame();
  const {width,height}=useVideoConfig();
  const portrait=height>width;
  const [bg,ink,accent]=colors[style];
  const beat=frame<100?0:frame<220?1:2;
  const start=[0,100,220][beat];
  const local=frame-start;
  const move=Math.min(1,Math.max(0,local/100));
  const words=['Ada\nsebab.','Setiap\ngerak.','Bina\nmakna.'][beat];
  return <AbsoluteFill style={{background:bg,overflow:'hidden'}}>
    {style==='pressroom' && <div style={{
      position:'absolute',width:portrait?700:650,height:portrait?950:1100,
      right:portrait?-150:-120,top:portrait?1000:-40,
      border:`2px solid ${accent}`,borderRadius:'50%',opacity:.3,
      transform:`rotate(${-20+move*6}deg)`,
    }} />}
    {style==='signal' && <div style={{
      position:'absolute',right:portrait?-180:50,top:portrait?1180:200,
      width:portrait?600:580,height:portrait?600:580,
      transform:`rotate(${-25+move*12}deg)`,border:`80px solid ${ink}`,borderRadius:beat===1?'50%':'0',
    }} />}
    {style==='atelier' && <div style={{
      position:'absolute',right:portrait?180:210,top:portrait?1090:210,
      width:portrait?600:420,height:portrait?600:620,border:`1px solid ${accent}`,
      borderRadius:'50% 50% 0 0',transform:`translateY(${-move*22}px)`,
    }}><div style={{position:'absolute',inset:36,border:`1px solid ${accent}`,borderRadius:'50% 50% 0 0'}} /></div>}
    <EditorialTitle text={words} from={start+24} durationInFrames={54}
      placement={portrait?'upper-middle':'center'} align="left" color={ink}
      fontFamily={style==='signal'?'Arial, sans-serif':'Georgia, serif'}
      fontWeight={style==='signal'?800:400} fontSize={portrait?128:160}
      maxWidth={portrait?900:1100} />
  </AbsoluteFill>;
};
