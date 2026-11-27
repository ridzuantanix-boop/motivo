export interface CaptionSegment {
  id: number;
  startSec: number;
  endSec: number;
  text: string;
  highlight?: string;
}

export interface SceneConfig {
  id: number;
  startSec: number;
  endSec: number;
  location: string;
  subtitle: string;
  yearTag: string;
  accentColor: string;
}
