import { Composition, Still, registerRoot } from 'remotion';
import { InstagramReel } from './InstagramReel';
import { InstaGridLeft, InstaGridCenter, InstaGridRight } from './InstagramGrid';
import { ScholarPromo } from './ScholarPromo';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="InstagramReel"
        component={InstagramReel}
        durationInFrames={160} // Original short reel
        fps={30}
        width={1080}
        height={1920}
      />

      <Composition
        id="ScholarPromo"
        component={ScholarPromo}
        durationInFrames={1230} // ~41 seconds (Recalibrated for full Audio)
        fps={30}
        width={1080}
        height={1920}
      />
      
      {/* The 3 Pinned Instagram portrait format Grids (1080x1350) */}
      <Still id="InstaGridLeft" component={InstaGridLeft} width={1080} height={1350} />
      <Still id="InstaGridCenter" component={InstaGridCenter} width={1080} height={1350} />
      <Still id="InstaGridRight" component={InstaGridRight} width={1080} height={1350} />
    </>
  );
};

registerRoot(RemotionRoot);
