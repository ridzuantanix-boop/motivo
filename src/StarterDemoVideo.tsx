import React from 'react';
import {AbsoluteFill, Img, staticFile, useVideoConfig} from 'remotion';
import {EditorialTitle} from './components/CleanTypography';

/** Still-based design demo: clean image, one timed title, then clean image again. */
export const StarterDemoVideo: React.FC = () => {
  const {width,height}=useVideoConfig();
  const portrait=height>width;
  return <AbsoluteFill style={{background:'#13251e'}}>
    <Img src={staticFile('demo/coast-clean.jpg')} style={{
      width:'100%',height:'100%',objectFit:'cover',objectPosition:portrait?'68% center':'center',
    }} />
    <EditorialTitle text={portrait?'Lihat\nperlahan.':'Lihat perlahan.'} from={90} durationInFrames={90} fontSize={portrait?130:150} />
  </AbsoluteFill>;
};
