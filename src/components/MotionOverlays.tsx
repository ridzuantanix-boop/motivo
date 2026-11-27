import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import { CaptionSegment, SceneConfig } from '../subtitles';

export const IntroHookBadge: React.FC<{
  title?: string;
  eyebrow?: string;
  subtitle?: string;
}> = ({
  title = 'MELAKA',
  eyebrow = 'MALAYSIA • TAPAK WARISAN DUNIA',
  subtitle = 'Bandaraya Bersejarah Dalam 30 Saat',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  if (frame > 135) return null;

  const enter = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120 },
  });
  const exit = interpolate(frame, [108, 135], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const opacity = Math.min(enter, exit);
  const translateY = interpolate(enter, [0, 1], [32, 0]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'center',
        alignItems: 'center',
        pointerEvents: 'none',
        opacity,
        transform: `translateY(${translateY}px)`,
      }}
    >
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: 12,
          padding: '26px 46px',
          borderRadius: 20,
          background: 'rgba(10, 14, 22, 0.72)',
          border: '1px solid rgba(255, 209, 102, 0.45)',
          boxShadow: '0 24px 60px rgba(0, 0, 0, 0.55)',
          backdropFilter: 'blur(12px)',
        }}
      >
        <div
          style={{
            fontSize: 20,
            fontWeight: 700,
            letterSpacing: 6,
            color: '#FFD166',
            textTransform: 'uppercase',
          }}
        >
          {eyebrow}
        </div>
        <div
          style={{
            fontSize: 74,
            fontWeight: 900,
            letterSpacing: 2,
            color: '#FFFFFF',
            lineHeight: 1.05,
            textShadow: '0 6px 24px rgba(0,0,0,0.6)',
          }}
        >
          {title}
        </div>
        <div
          style={{
            width: interpolate(enter, [0, 1], [0, 220]),
            height: 4,
            borderRadius: 999,
            background: 'linear-gradient(90deg, #E63946, #FFD166)',
          }}
        />
        <div
          style={{
            fontSize: 24,
            fontWeight: 500,
            color: '#E2E8F0',
            letterSpacing: 1.5,
          }}
        >
          {subtitle}
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const LocationLowerThird: React.FC<{
  scene: SceneConfig;
  sceneLocalFrame: number;
  sceneDurationFrames: number;
}> = ({ scene, sceneLocalFrame, sceneDurationFrames }) => {
  const { fps } = useVideoConfig();

  const enter = spring({
    frame: Math.max(0, sceneLocalFrame - 6),
    fps,
    config: { damping: 16, stiffness: 140 },
  });
  const exit = interpolate(
    sceneLocalFrame,
    [sceneDurationFrames - 18, sceneDurationFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  const opacity = Math.min(enter, exit);
  const slideX = interpolate(enter, [0, 1], [-40, 0]);

  return (
    <div
      style={{
        position: 'absolute',
        top: 52,
        left: 60,
        opacity,
        transform: `translateX(${slideX}px)`,
        display: 'flex',
        alignItems: 'stretch',
        gap: 14,
      }}
    >
      <div
        style={{
          width: 6,
          borderRadius: 6,
          background: scene.accentColor,
          boxShadow: `0 0 18px ${scene.accentColor}`,
        }}
      />
      <div
        style={{
          background: 'rgba(8, 12, 20, 0.72)',
          border: '1px solid rgba(255, 255, 255, 0.16)',
          borderRadius: 12,
          padding: '12px 22px',
          backdropFilter: 'blur(10px)',
        }}
      >
        <div
          style={{
            fontSize: 15,
            fontWeight: 800,
            letterSpacing: 3,
            color: scene.accentColor,
            marginBottom: 4,
          }}
        >
          {scene.yearTag}
        </div>
        <div
          style={{
            fontSize: 28,
            fontWeight: 800,
            color: '#FFFFFF',
            lineHeight: 1.15,
          }}
        >
          {scene.location}
        </div>
        <div
          style={{
            fontSize: 17,
            fontWeight: 500,
            color: '#CBD5E1',
            marginTop: 2,
          }}
        >
          {scene.subtitle}
        </div>
      </div>
    </div>
  );
};

export const ColonialTimelineCard: React.FC<{
  sceneLocalFrame: number;
  sceneDurationFrames: number;
}> = ({ sceneLocalFrame, sceneDurationFrames }) => {
  const { fps } = useVideoConfig();
  const milestones = [
    { year: '1511', label: 'Portugis', color: '#E63946' },
    { year: '1641', label: 'Belanda', color: '#F4A261' },
    { year: '1824', label: 'British', color: '#60A5FA' },
  ];

  const enter = spring({
    frame: Math.max(0, sceneLocalFrame - 18),
    fps,
    config: { damping: 16, stiffness: 120 },
  });
  const exit = interpolate(
    sceneLocalFrame,
    [sceneDurationFrames - 18, sceneDurationFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return (
    <div
      style={{
        position: 'absolute',
        top: 132,
        right: 60,
        opacity: Math.min(enter, exit),
        transform: `translateX(${interpolate(enter, [0, 1], [40, 0])}px)`,
        background: 'rgba(8, 12, 20, 0.74)',
        border: '1px solid rgba(255, 255, 255, 0.16)',
        borderRadius: 14,
        padding: '14px 20px',
        backdropFilter: 'blur(10px)',
        display: 'flex',
        flexDirection: 'column',
        gap: 10,
      }}
    >
      <div
        style={{
          fontSize: 13,
          fontWeight: 800,
          letterSpacing: 2.5,
          color: '#94A3B8',
        }}
      >
        GARIS MASA KOLONIAL
      </div>
      {milestones.map((m, i) => {
        const itemSpring = spring({
          frame: Math.max(0, sceneLocalFrame - (24 + i * 24)),
          fps,
          config: { damping: 14, stiffness: 140 },
        });
        return (
          <div
            key={m.year}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              opacity: itemSpring,
              transform: `translateY(${interpolate(itemSpring, [0, 1], [10, 0])}px)`,
            }}
          >
            <span
              style={{
                width: 10,
                height: 10,
                borderRadius: '50%',
                background: m.color,
                boxShadow: `0 0 10px ${m.color}`,
              }}
            />
            <span
              style={{
                fontSize: 18,
                fontWeight: 800,
                color: m.color,
                minWidth: 52,
              }}
            >
              {m.year}
            </span>
            <span style={{ fontSize: 18, fontWeight: 600, color: '#F8FAFC' }}>
              {m.label}
            </span>
          </div>
        );
      })}
    </div>
  );
};

export const UnescoBadgeCard: React.FC<{
  sceneLocalFrame: number;
  sceneDurationFrames: number;
}> = ({ sceneLocalFrame, sceneDurationFrames }) => {
  const { fps } = useVideoConfig();
  const enter = spring({
    frame: Math.max(0, sceneLocalFrame - 14),
    fps,
    config: { damping: 14, stiffness: 130 },
  });
  const exit = interpolate(
    sceneLocalFrame,
    [sceneDurationFrames - 18, sceneDurationFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return (
    <div
      style={{
        position: 'absolute',
        top: 132,
        right: 60,
        opacity: Math.min(enter, exit),
        transform: `scale(${interpolate(enter, [0, 1], [0.9, 1])})`,
        background: 'rgba(10, 22, 32, 0.78)',
        border: '1px solid rgba(46, 196, 182, 0.5)',
        borderRadius: 14,
        padding: '14px 22px',
        backdropFilter: 'blur(10px)',
      }}
    >
      <div
        style={{
          fontSize: 13,
          fontWeight: 800,
          letterSpacing: 2.5,
          color: '#2EC4B6',
        }}
      >
        PENGIKTIRAFAN DUNIA
      </div>
      <div style={{ fontSize: 24, fontWeight: 800, color: '#FFFFFF', marginTop: 4 }}>
        Tapak Warisan UNESCO
      </div>
      <div style={{ fontSize: 16, fontWeight: 500, color: '#CBD5E1', marginTop: 2 }}>
        Sejak 7 Julai 2008
      </div>
    </div>
  );
};

export const AmbientParticles: React.FC = () => {
  const frame = useCurrentFrame();
  const particles = [
    { x: 14, y: 24, size: 5, speed: 0.45, phase: 0 },
    { x: 28, y: 68, size: 7, speed: 0.35, phase: 1.2 },
    { x: 47, y: 42, size: 4, speed: 0.55, phase: 2.4 },
    { x: 64, y: 20, size: 6, speed: 0.4, phase: 0.8 },
    { x: 78, y: 58, size: 5, speed: 0.5, phase: 3.1 },
    { x: 88, y: 34, size: 6, speed: 0.38, phase: 1.9 },
  ];

  return (
    <AbsoluteFill style={{ pointerEvents: 'none', overflow: 'hidden' }}>
      {particles.map((p, idx) => {
        const yOffset = Math.sin(frame * 0.04 * p.speed + p.phase) * 18;
        const xOffset = Math.cos(frame * 0.03 * p.speed + p.phase) * 14;
        const opacity = 0.25 + 0.2 * Math.sin(frame * 0.05 + p.phase);
        return (
          <div
            key={idx}
            style={{
              position: 'absolute',
              left: `${p.x}%`,
              top: `${p.y}%`,
              width: p.size,
              height: p.size,
              borderRadius: '50%',
              background: '#FFD166',
              opacity,
              transform: `translate(${xOffset}px, ${yOffset}px)`,
              boxShadow: '0 0 14px rgba(255, 209, 102, 0.85)',
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

export const FacelessCaptions: React.FC<{ captions: CaptionSegment[] }> = ({
  captions,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentSec = frame / fps;

  const active = captions.find(
    (c) => currentSec >= c.startSec && currentSec < c.endSec
  );
  if (!active) return null;

  const localSec = currentSec - active.startSec;
  const pop = spring({
    frame: Math.round(localSec * fps),
    fps,
    config: { damping: 15, stiffness: 200 },
  });
  const scale = interpolate(pop, [0, 1], [0.92, 1]);

  const renderStyledText = (text: string, highlight?: string) => {
    if (!highlight || !text.includes(highlight)) {
      return <span>{text}</span>;
    }
    const idx = text.indexOf(highlight);
    const before = text.slice(0, idx);
    const after = text.slice(idx + highlight.length);
    return (
      <>
        <span>{before}</span>
        <span style={{ color: '#FFD166' }}>{highlight}</span>
        <span>{after}</span>
      </>
    );
  };

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 68,
        left: 120,
        right: 120,
        display: 'flex',
        justifyContent: 'center',
        pointerEvents: 'none',
        transform: `scale(${scale})`,
      }}
    >
      <div
        style={{
          background: 'rgba(9, 13, 22, 0.84)',
          border: '1px solid rgba(255, 255, 255, 0.16)',
          borderRadius: 16,
          padding: '16px 32px',
          boxShadow: '0 16px 40px rgba(0, 0, 0, 0.55)',
          textAlign: 'center',
          maxWidth: 1360,
        }}
      >
        <div
          style={{
            fontSize: 42,
            fontWeight: 800,
            lineHeight: 1.25,
            color: '#FFFFFF',
            textShadow: '0 3px 12px rgba(0, 0, 0, 0.85)',
          }}
        >
          {renderStyledText(active.text, active.highlight)}
        </div>
      </div>
    </div>
  );
};

export const TimelineProgressBar: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const progress = Math.min(1, Math.max(0, frame / durationInFrames));

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 0,
        left: 0,
        right: 0,
        height: 8,
        background: 'rgba(255, 255, 255, 0.14)',
      }}
    >
      <div
        style={{
          width: `${progress * 100}%`,
          height: '100%',
          background:
            'linear-gradient(90deg, #E63946 0%, #FFD166 55%, #2EC4B6 100%)',
          boxShadow: '0 0 16px rgba(255, 209, 102, 0.7)',
        }}
      />
    </div>
  );
};

export const InfoSideCard: React.FC<{
  eyebrow: string;
  heading: string;
  subtext: string;
  accentColor: string;
  sceneLocalFrame: number;
  sceneDurationFrames: number;
}> = ({
  eyebrow,
  heading,
  subtext,
  accentColor,
  sceneLocalFrame,
  sceneDurationFrames,
}) => {
  const { fps } = useVideoConfig();
  const enter = spring({
    frame: Math.max(0, sceneLocalFrame - 14),
    fps,
    config: { damping: 14, stiffness: 130 },
  });
  const exit = interpolate(
    sceneLocalFrame,
    [sceneDurationFrames - 18, sceneDurationFrames],
    [1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  return (
    <div
      style={{
        position: 'absolute',
        top: 132,
        right: 60,
        opacity: Math.min(enter, exit),
        transform: `scale(${interpolate(enter, [0, 1], [0.9, 1])})`,
        background: 'rgba(10, 20, 30, 0.78)',
        border: `1px solid ${accentColor}80`,
        borderRadius: 14,
        padding: '14px 22px',
        backdropFilter: 'blur(10px)',
      }}
    >
      <div
        style={{
          fontSize: 13,
          fontWeight: 800,
          letterSpacing: 2.5,
          color: accentColor,
        }}
      >
        {eyebrow}
      </div>
      <div style={{ fontSize: 24, fontWeight: 800, color: '#FFFFFF', marginTop: 4 }}>
        {heading}
      </div>
      <div style={{ fontSize: 16, fontWeight: 500, color: '#CBD5E1', marginTop: 2 }}>
        {subtext}
      </div>
    </div>
  );
};

export const TopChannelWatermark: React.FC<{ label?: string }> = ({
  label = 'SEJARAH & WARISAN',
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const totalSec = Math.round(durationInFrames / fps);
  const sec = Math.min(totalSec, Math.floor(frame / fps));
  const fmt = (s: number) =>
    `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;

  return (
    <div
      style={{
        position: 'absolute',
        top: 52,
        right: 60,
        display: 'flex',
        alignItems: 'center',
        gap: 12,
        background: 'rgba(8, 12, 20, 0.68)',
        border: '1px solid rgba(255, 255, 255, 0.14)',
        borderRadius: 999,
        padding: '8px 18px',
        color: '#F8FAFC',
        fontSize: 16,
        fontWeight: 700,
        letterSpacing: 1,
      }}
    >
      <span
        style={{
          width: 10,
          height: 10,
          borderRadius: '50%',
          background: '#E63946',
          boxShadow: '0 0 10px #E63946',
        }}
      />
      <span>{label}</span>
      <span style={{ color: '#94A3B8' }}>|</span>
      <span style={{ fontVariantNumeric: 'tabular-nums', color: '#FFD166' }}>
        {fmt(sec)} / {fmt(totalSec)}
      </span>
    </div>
  );
};
