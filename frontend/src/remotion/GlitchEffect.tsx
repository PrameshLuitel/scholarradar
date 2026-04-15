import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame } from 'remotion';

export const GlitchEffect: React.FC<{ children: React.ReactNode; intensity?: number }> = ({ children, intensity = 1 }) => {
    const frame = useCurrentFrame();
    
    // Random jitter logic
    const jitter = (frame % 3 === 0) ? (Math.random() - 0.5) * 15 * intensity : 0;
    const scale = (frame % 5 === 0) ? 1 + (Math.random() - 0.5) * 0.05 * intensity : 1;
    
    // RGB Split logic
    const offset = (frame % 2 === 0) ? Math.sin(frame) * 5 * intensity : 0;

    return (
        <AbsoluteFill style={{ overflow: 'hidden' }}>
            {/* Red Channel */}
            <AbsoluteFill style={{ 
                transform: `translate(${jitter + offset}px, ${jitter}px) scale(${scale})`,
                opacity: 0.5,
                mixBlendMode: 'screen',
                filter: 'brightness(1.5) contrast(1.2)'
            }}>
                <div style={{ filter: 'drop-shadow(0 0 10px red)' }}>{children}</div>
            </AbsoluteFill>

            {/* Blue Channel */}
            <AbsoluteFill style={{ 
                transform: `translate(${jitter - offset}px, ${jitter}px) scale(${scale})`,
                opacity: 0.5,
                mixBlendMode: 'screen',
                filter: 'brightness(1.5) contrast(1.2)'
            }}>
                <div style={{ filter: 'drop-shadow(0 0 10px blue)' }}>{children}</div>
            </AbsoluteFill>

            {/* Main Layer */}
            <AbsoluteFill style={{ transform: `scale(${scale})` }}>
                {children}
            </AbsoluteFill>
        </AbsoluteFill>
    );
};

import { Video, Sequence } from 'remotion';

export const SpeedRampVideo: React.FC<{ 
    src: string; 
    startFrame: number; 
    durationInFrames: number;
    videoDurationInFrames?: number; 
}> = ({ src, startFrame, durationInFrames, videoDurationInFrames = 240 }) => {
    // Stable 3-Stage Ramp Logic:
    // Stage 1: Fast (Intro)
    // Stage 2: Slow (Dramatic Focus)
    // Stage 3: Fast (Impact / Out)
    
    const stage1Dur = Math.floor(durationInFrames * 0.15);
    const stage2Dur = Math.floor(durationInFrames * 0.7);
    const stage3Dur = durationInFrames - stage1Dur - stage2Dur;

    const vStage1Dur = Math.floor(videoDurationInFrames * 0.4);
    const vStage2Dur = Math.floor(videoDurationInFrames * 0.4);
    const vStage3Dur = videoDurationInFrames - vStage1Dur - vStage2Dur;

    return (
        <AbsoluteFill style={{ backgroundColor: 'black' }}>
            {/* Stage 1: Fast */}
            <Sequence from={0} durationInFrames={stage1Dur}>
                <Video 
                    src={src} 
                    startFrom={0} 
                    endAt={vStage1Dur}
                    playbackRate={vStage1Dur / stage1Dur} 
                    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                    volume={0}
                />
            </Sequence>
            {/* Stage 2: Slow */}
            <Sequence from={stage1Dur} durationInFrames={stage2Dur}>
                <Video 
                    src={src} 
                    startFrom={vStage1Dur} 
                    endAt={vStage1Dur + vStage2Dur}
                    playbackRate={vStage2Dur / stage2Dur} 
                    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                    volume={0}
                />
            </Sequence>
            {/* Stage 3: Fast */}
            <Sequence from={stage1Dur + stage2Dur} durationInFrames={stage3Dur}>
                <Video 
                    src={src} 
                    startFrom={vStage1Dur + vStage2Dur} 
                    endAt={videoDurationInFrames}
                    playbackRate={vStage3Dur / stage3Dur} 
                    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                    volume={0}
                />
            </Sequence>
        </AbsoluteFill>
    );
};
