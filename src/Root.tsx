import React from 'react';
import { Composition } from 'remotion';
import { StarterDemoVideo } from './StarterDemoVideo';
import {MotivoStudy, StudyStyle} from './MotivoStudy';
import {GalleryPoster} from './GalleryPoster';
import {gallery} from './gallery-data';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {gallery.map(poster => <Composition
        key={poster.slug}
        id={`Gallery-${poster.slug}`}
        component={GalleryPoster}
        defaultProps={{source:poster.source}}
        durationInFrames={1}
        fps={30}
        width={1200}
        height={675}
      />)}
      {(['pressroom', 'signal', 'atelier'] as StudyStyle[]).flatMap((style) =>
        [false, true].map((portrait) => <Composition
          key={`${style}-${portrait}`}
          id={`Motivo-${style}-${portrait ? 'Portrait' : 'Landscape'}`}
          component={MotivoStudy}
          defaultProps={{style}}
          durationInFrames={360}
          fps={30}
          width={portrait ? 1080 : 1920}
          height={portrait ? 1920 : 1080}
        />)
      )}
      <Composition
        id="StarterDemoVideo"
        component={StarterDemoVideo}
        durationInFrames={450}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
