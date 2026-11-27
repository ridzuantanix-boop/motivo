import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';
import {
  FacelessCaptions,
  InfoSideCard,
  IntroHookBadge,
  LocationLowerThird,
  TimelineProgressBar,
  TopChannelWatermark,
} from './components/MotionOverlays';
import { CaptionSegment, SceneConfig } from './subtitles';

const DEMO_SCENE: SceneConfig = {
  id: 1,
  startSec: 0,
  endSec: 15,
  location: 'Templat Video AI BM',
  subtitle: 'Sedia Dengan Nexabot & Remotion',
  yearTag: 'STARTER KIT',
  accentColor: '#2EC4B6',
};

const DEMO_CAPTIONS: CaptionSegment[] = [
  {
    id: 1,
    startSec: 0.2,
    endSec: 5.0,
    text: 'Isi NEXABOT_API_KEY dalam .env dan terus mula menjana video.',
    highlight: 'NEXABOT_API_KEY',
  },
];

export const StarterDemoVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const opacity = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{ backgroundColor: '#05070B', fontFamily: 'Inter, system-ui, sans-serif', opacity }}>
      <LocationLowerThird scene={DEMO_SCENE} sceneLocalFrame={frame} sceneDurationFrames={durationInFrames} />
      <InfoSideCard
        eyebrow="MOD VIDEO"
        heading="Dialog & Naratif BM"
        subtext="i2v Avatar • t2v • SuaraKita"
        accentColor="#FFD166"
        sceneLocalFrame={frame}
        sceneDurationFrames={durationInFrames}
      />
      <TopChannelWatermark label="NEXABOT STUDIO BM" />
      <IntroHookBadge eyebrow="STARTER KIT" title="VIDEO AI" subtitle="Siap Untuk Arahan Pertama Anda" />
      <FacelessCaptions captions={DEMO_CAPTIONS} />
      <TimelineProgressBar />
    </AbsoluteFill>
  );
};
