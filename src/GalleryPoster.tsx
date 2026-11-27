import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

export const GalleryPoster: React.FC<{source: string}> = ({source}) => (
  <AbsoluteFill style={{background: '#171b18'}}>
    <Img src={staticFile(source)} style={{width:'100%',height:'100%',objectFit:'cover'}} />
  </AbsoluteFill>
);
