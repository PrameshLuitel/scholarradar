import React from 'react';
import { AbsoluteFill, Audio, staticFile, Sequence, useCurrentFrame, interpolate } from 'remotion';
import { ClaudeSimulation } from './ClaudeSimulation';
import { LogoStinger } from './LogoStinger';
import { InFeedOverlay, CommentBadge } from './InFeedOverlay';
import { GlitchEffect, SpeedRampVideo } from './GlitchEffect';

export const ScholarPromo: React.FC = () => {
    // Timing constants (frames at 30fps) - Recalibrated for full Audio length
    const hookEnd = 240;       // 8.00s
    const pivotEnd = 485;      // 8.08s + Hook
    const mechanismEnd = 810;  // 10.64s + Pivot
    const proofEnd = 1070;     // 8.40s + Mechanism
    const duration = 1230;     // 5.04s + Proof (Final: 41s)

    return (
        <AbsoluteFill style={{ backgroundColor: 'black' }}>
            {/* --- AUDIO ENGINE: PHONK & SYNC --- */}
            {/* Background Phonk Beat with Dynamic Ducking */}
            <Audio 
                src={staticFile('sounds/trendy_bg.mp3')} 
                volume={interpolate(
                    useCurrentFrame(),
                    [0, 10, hookEnd - 10, hookEnd, pivotEnd - 10, pivotEnd, mechanismEnd - 10, mechanismEnd, proofEnd - 10, proofEnd], // Duck points
                    [0.4, 0.15, 0.15, 0.4, 0.4, 0.15, 0.15, 0.4, 0.4, 0.15], // Volume levels
                    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
                )} 
                loop 
            />
            
            {/* Groq Orpheus-v1 VO Segments */}
            <Sequence from={0} durationInFrames={hookEnd}>
                <Audio src={staticFile('social-videos/vo_hook.wav')} volume={1.2} />
            </Sequence>
            <Sequence from={hookEnd} durationInFrames={pivotEnd - hookEnd}>
                <Audio src={staticFile('social-videos/vo_pivot.wav')} volume={1.2} />
            </Sequence>
            <Sequence from={pivotEnd} durationInFrames={mechanismEnd - pivotEnd}>
                <Audio src={staticFile('social-videos/vo_tool_reveal.wav')} volume={1.2} />
            </Sequence>
            <Sequence from={mechanismEnd} durationInFrames={proofEnd - mechanismEnd}>
                <Audio src={staticFile('social-videos/vo_result.wav')} volume={1.4} />
            </Sequence>
            <Sequence from={proofEnd}>
                <Audio src={staticFile('social-videos/vo_cta.wav')} volume={1.2} />
            </Sequence>

            {/* --- VISUAL ENGINE: BRAIN ORGASM AESTHETICS --- */}
            
            {/* Scene 1: Speed Ramped VEO A + Glitch */}
            <Sequence from={0} durationInFrames={hookEnd}>
                <GlitchEffect intensity={useCurrentFrame() < 45 ? 2 : 0.5}>
                    <SpeedRampVideo 
                        src={staticFile('social-videos/veo_a.mp4')} 
                        startFrame={0} 
                        durationInFrames={hookEnd} 
                        videoDurationInFrames={240} // 8s clip
                    />
                </GlitchEffect>
                <InFeedOverlay status="scam" text="Stop Paying Agencies" startFrame={15} />
            </Sequence>

            {/* Scene 2: Speed Ramped VEO B + Flash Pivot */}
            <Sequence from={hookEnd} durationInFrames={pivotEnd - hookEnd}>
                <GlitchEffect intensity={useCurrentFrame() > hookEnd + 150 ? 3 : 1}>
                    <SpeedRampVideo 
                        src={staticFile('social-videos/veo_b.mp4')} 
                        startFrame={hookEnd} 
                        durationInFrames={pivotEnd - hookEnd} 
                        videoDurationInFrames={240} 
                    />
                </GlitchEffect>
                <InFeedOverlay status="alert" text="THEY ARE LYING" startFrame={hookEnd + 10} />
            </Sequence>

            {/* Scene 3: Deep-Scraper Claude Mode (Mechanism Focus) */}
            <Sequence from={pivotEnd} durationInFrames={mechanismEnd - pivotEnd}>
                <ClaudeSimulation />
                <CommentBadge user="scholar_hacker" text="Agency gatekeeping is over." delay={pivotEnd + 30} />
            </Sequence>

            {/* Scene 4: Speed Ramped VEO C (Human Proof) */}
            <Sequence from={mechanismEnd} durationInFrames={proofEnd - mechanismEnd}>
                <GlitchEffect intensity={1.5}>
                    <SpeedRampVideo 
                        src={staticFile('social-videos/veo_c.mp4')} 
                        startFrame={mechanismEnd} 
                        durationInFrames={proofEnd - mechanismEnd} 
                        videoDurationInFrames={240} 
                    />
                </GlitchEffect>
                <CommentBadge user="visa_expert" text="Just found a $40k link! 🚀" delay={mechanismEnd + 20} />
                <InFeedOverlay status="official" text="Direct Results" startFrame={mechanismEnd + 15} />
            </Sequence>

            {/* Scene 5: Simple Logo Outro */}
            <Sequence from={proofEnd}>
                <AbsoluteFill style={{ background: 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%)' }} />
                <LogoStinger />
                <InFeedOverlay status="official" text="skolr.xyz" startFrame={proofEnd + 20} />
            </Sequence>

            {/* --- SFX ENGINE: HIGH DENSITY IMPACTS --- */}
            {/* Impact on scene cuts */}
            {[hookEnd, pivotEnd, mechanismEnd, proofEnd, duration].map((f, i) => (
                <Sequence key={i} from={f - 5}>
                    <Audio src={staticFile('sounds/whoosh.mp3')} volume={1.0} playbackRate={1.5} />
                    <Audio src={staticFile('sounds/ding.mp3')} volume={0.8} />
                </Sequence>
            ))}
            
            {/* Scholarship Data SFX (Repeating 'ding' during reveal) */}
            {[700, 750, 800, 850, 900, 950, 1000].map((f, i) => (
                <Sequence key={i} from={f}>
                    <Audio src={staticFile('sounds/ding.mp3')} volume={0.5} playbackRate={2.5} />
                </Sequence>
            ))}
        </AbsoluteFill>
    );
};
