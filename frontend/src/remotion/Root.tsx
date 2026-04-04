import { Composition, Still, registerRoot } from 'remotion';
import { InstagramReel } from './InstagramReel';
import { InstaGridLeft, InstaGridCenter, InstaGridRight } from './InstagramGrid';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="InstagramReel"
        component={InstagramReel}
        durationInFrames={160} // 160 frames gives a solid 2 seconds to absorb the final 'skolr.xyz' state
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
