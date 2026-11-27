import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {CaptionSegment} from '../subtitles';
import {textOpacity} from '../textTiming';

type TitleProps = {
  text: string;
  from: number;
  durationInFrames: number;
  placement?: 'center' | 'lower' | 'upper-middle';
  align?: 'center' | 'left';
  color?: string;
  fontFamily?: string;
  fontSize?: number;
  fontWeight?: number;
  maxWidth?: number;
};

/** A deliberate title cue, never an always-on frame decoration. */
export const EditorialTitle: React.FC<TitleProps> = ({
  text, from, durationInFrames, placement='lower', align='center',
  color='#f4eee0', fontFamily='Georgia, serif', fontSize, fontWeight=400, maxWidth,
}) => {
  const frame=useCurrentFrame();
  const {width,height}=useVideoConfig();
  const opacity=textOpacity(frame,from,durationInFrames);
  if (!text.trim() || opacity===0) return null;
  const portrait=height>width;
  return <AbsoluteFill style={{
    justifyContent:placement==='lower'?'flex-end':placement==='upper-middle'?'flex-start':'center',
    alignItems:align==='left'?'flex-start':'center',
    paddingLeft:width*.09, paddingRight:width*.09,
    paddingTop:placement==='upper-middle'?height*.27:0,
    paddingBottom:placement==='lower'?height*(portrait ? 0.23 : 0.16):0,
    pointerEvents:'none', opacity,
  }}>
    <div style={{
      color,fontFamily,fontSize:fontSize??Math.round(Math.min(width,height)*.12),fontWeight,
      maxWidth:maxWidth??width*.82,lineHeight:1.08,letterSpacing:'-.035em',
      textAlign:align,whiteSpace:'pre-line',textWrap:'balance',
    }}>{text}</div>
  </AbsoluteFill>;
};

/** Opt-in speech captions; no badge, panel, word bounce or progress decoration. */
export const ReadableCaptions: React.FC<{
  segments: CaptionSegment[];
  enabled?: boolean;
  color?: string;
  fontSize?: number;
}> = ({segments,enabled=false,color='#fff',fontSize}) => {
  const frame=useCurrentFrame();
  const {fps,width,height}=useVideoConfig();
  if (!enabled) return null;
  const active=segments.find(s=>frame/fps>=s.startSec && frame/fps<s.endSec);
  if (!active) return null;
  return <div style={{
    position:'absolute',left:'10%',right:'10%',bottom:height*(height>width ? 0.12 : 0.08),
    textAlign:'center',color,fontFamily:'Arial, sans-serif',
    fontSize:fontSize??Math.round(Math.min(width,height)*.05),fontWeight:500,
    lineHeight:1.24,whiteSpace:'pre-line',textWrap:'balance',
    textShadow:'0 1px 4px rgba(0,0,0,.55)',pointerEvents:'none',
  }}>{active.text}</div>;
};
