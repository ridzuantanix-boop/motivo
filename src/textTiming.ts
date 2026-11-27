/** Finite text windows: outside the requested interval there is no visible text. */
export const textOpacity = (frame: number, from: number, duration: number, fade = 8): number => {
  if (![frame, from, duration, fade].every(Number.isFinite) || from < 0 || duration <= 0 || fade < 0) {
    throw new Error('Text needs a finite start, positive duration and nonnegative fade.');
  }
  const local = frame - from;
  if (local < 0 || local >= duration) return 0;
  const edge = Math.min(fade, duration / 2);
  return edge === 0 ? 1 : Math.min(1, local / edge, (duration - local) / edge);
};
