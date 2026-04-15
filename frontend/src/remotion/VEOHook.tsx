import React from 'react';
import { AbsoluteFill, Video, staticFile, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const VEOHook: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Aggressive bouncy zoom for the video hook to simulate camera movement
    const zoomSpr = spring({ frame, fps, config: { damping: 12, mass: 2, stiffness: 60 } });
    // Make the zoom go in and out slightly for a breathing effect after the initial pop
    const zoomBreathing = Math.sin(frame * 0.05) * 0.05;
    const zoom = interpolate(zoomSpr, [0, 1], [1, 1.3]) + zoomBreathing;

    // Scanline effect
    const scanlineY = (frame * 15) % 1080;

    // Words for the kinetic hook
    const words = ["Stop.", "Paying.", "Study-Abroad", "Agencies.", "🛑"];
    
    // Staggered reveal for each word with 3D tilt
    const renderWord = (word: string, index: number) => {
        const delay = index * 8; // Slight increase in delay for suspense
        const spr = spring({
            frame: frame - delay,
            fps,
            config: { damping: 8, mass: 0.6, stiffness: 150 } // More snappy
        });

        // Add a slight continuous float after it pops in
        const floatY = Math.sin((frame - delay) * 0.1) * 15;
        const tiltX = Math.cos((frame - delay) * 0.1) * 20;
        const rotateZ = interpolate(spr, [0, 1], [(index % 2 === 0 ? 10 : -10), 0]);

        const opacity = interpolate(spr, [0, 1], [0, 1]);
        const scale = interpolate(spr, [0, 0.5, 1], [0.1, 1.2, 1]); // Extra bouncy pop
        const y = interpolate(spr, [0, 1], [150, 0]);

        return (
            <span key={index} style={{
                display: 'inline-block',
                margin: '0 15px',
                opacity,
                transform: `scale(${scale}) translateY(${y + floatY}px) perspective(500px) rotateX(${tiltX}deg) rotateZ(${rotateZ}deg)`,
                textShadow: '0 15px 40px rgba(0,0,0,0.8), 0 0 20px rgba(239,68,68,0.5)',
                color: index === 4 ? 'white' : index === 0 ? '#ef4444' : 'white',
                filter: `drop-shadow(0 0 ${interpolate(spr, [0, 1], [0, 25])}px rgba(255,255,255,0.4))`
            }}>
                {word}
            </span>
        );
    };

    return (
        <AbsoluteFill style={{ backgroundColor: 'black', overflow: 'hidden' }}>
            <Video 
                src={staticFile('media/veo_hook.mp4')} 
                muted={true}
                style={{ 
                    width: '100%', 
                    height: '100%', 
                    objectFit: 'cover',
                    transform: `scale(${zoom})`,
                    filter: `brightness(${interpolate(frame, [0, 20], [0.3, 1.2])}) contrast(1.1) saturate(1.2)`
                }} 
            />
            
            {/* Cinematic color glitch shifts based on frame modulo */}
            {frame % 40 > 36 && (
                <AbsoluteFill style={{ mixBlendMode: 'color-dodge', backgroundColor: 'rgba(255, 0, 0, 0.2)', opacity: 0.5 }} />
            )}
            {frame % 40 > 38 && (
                <AbsoluteFill style={{ mixBlendMode: 'color-burn', backgroundColor: 'rgba(0, 0, 255, 0.2)', opacity: 0.5 }} />
            )}
            
            {/* Pulsing Vignette Overlay */}
            <AbsoluteFill style={{ 
                background: `radial-gradient(circle, transparent 30%, rgba(0,0,0,${interpolate(Math.sin(frame * 0.2), [-1, 1], [0.5, 0.9])}))`,
                zIndex: 1
            }} />

            {/* Simulated UI: Live Recording Indicator */}
            <div style={{
                position: 'absolute', top: 80, left: 60, zIndex: 10,
                display: 'flex', alignItems: 'center', gap: 15,
                background: 'rgba(0,0,0,0.6)', padding: '10px 25px', borderRadius: 30,
                backdropFilter: 'blur(10px)',
                opacity: spring({frame, fps}),
                transform: `scale(${interpolate(Math.sin(frame * 0.1), [-1, 1], [0.95, 1.05])})`
            }}>
                <div style={{ 
                    width: 24, height: 24, borderRadius: '50%', backgroundColor: '#ef4444',
                    opacity: Math.sin(frame * 0.2) > 0 ? 1 : 0.3,
                    boxShadow: Math.sin(frame * 0.2) > 0 ? '0 0 15px #ef4444' : 'none'
                }} />
                <span style={{ color: 'white', fontSize: 24, fontWeight: 800, fontFamily: 'monospace', letterSpacing: 2 }}>REC 4K</span>
            </div>
            
            {/* Scanning Line overlay */}
            <div style={{
                position: 'absolute', top: scanlineY, left: 0, width: '100%', height: 4,
                backgroundColor: 'rgba(255,255,255,0.2)',
                boxShadow: '0 0 20px rgba(255,255,255,0.5)',
                zIndex: 2,
                opacity: 0.4
            }} />

            {/* Kinetic Typography Container */}
            <div style={{
                position: 'absolute',
                bottom: 250,
                width: '100%',
                textAlign: 'center',
                fontFamily: 'Inter, sans-serif',
                fontSize: 120,
                fontWeight: 900,
                letterSpacing: -5,
                display: 'flex',
                alignItems: 'center',
                flexWrap: 'wrap',
                justifyContent: 'center',
                zIndex: 5,
                padding: '0 40px'
            }}>
                {words.map((word, i) => renderWord(word, i))}
            </div>
            
            {/* Flash/Strobe effect at the end of the scene before transition */}
            {frame > 210 && (
                 <AbsoluteFill style={{ 
                     backgroundColor: 'white', 
                     opacity: interpolate(frame, [210, 240], [0, 1], { extrapolateRight: 'clamp' }),
                     zIndex: 10
                 }} />
            )}
        </AbsoluteFill>
    );
};
