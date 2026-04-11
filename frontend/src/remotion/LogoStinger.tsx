import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate, Audio, Easing, Sequence, staticFile } from 'remotion';

export const LogoStinger: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Box appears
    const boxScale = spring({ frame, fps, config: { damping: 14 } });

    // Mathematical definition of the Bouncing airplane flight
    const getPhysics = (f: number) => {
        let x = -400, y = -600, sx = 1, sy = 1;
        if (f <= 20) return { x, y, sx, sy };
        
        if (f > 20 && f <= 30) {
            y = interpolate(f, [20, 30], [-600, 0], { easing: Easing.in(Easing.quad), extrapolateRight: 'clamp' });
            sx = interpolate(f, [20, 29, 30], [1, 0.6, 1.6], { extrapolateRight: 'clamp' });
            sy = interpolate(f, [20, 29, 30], [1, 1.8, 0.4], { extrapolateRight: 'clamp' });
        }
        else if (f > 30 && f <= 50) {
            const p = (f - 30) / 20; 
            y = -180 * (4 * p * (1 - p)); 
            x = interpolate(p, [0, 1], [-400, -200]);
            if (p < 0.2) { sy = interpolate(p, [0, 0.2], [0.4, 1.1]); sx = interpolate(p, [0, 0.2], [1.6, 0.9]); }
            else if (p > 0.8) { sy = interpolate(p, [0.8, 1], [1.1, 0.5]); sx = interpolate(p, [0.8, 1], [0.9, 1.5]); }
        }
        else if (f > 50 && f <= 70) {
            const p = (f - 50) / 20;
            y = -100 * (4 * p * (1 - p));
            x = interpolate(p, [0, 1], [-200, -60]);
            if (p < 0.2) { sy = interpolate(p, [0, 0.2], [0.5, 1.05]); sx = interpolate(p, [0, 0.2], [1.5, 0.95]); }
            else if (p > 0.8) { sy = interpolate(p, [0.8, 1], [1.05, 0.6]); sx = interpolate(p, [0.8, 1], [0.95, 1.4]); }
        }
        else if (f > 70 && f <= 85) {
            const p = (f - 70) / 15;
            y = -40 * (4 * p * (1 - p));
            x = interpolate(p, [0, 1], [-60, 0]); // Zero is the exact parking spot
            if (p < 0.3) { sy = interpolate(p, [0, 0.3], [0.6, 1.02]); sx = interpolate(p, [0, 0.3], [1.4, 0.98]); }
            else if (p > 0.8) { sy = interpolate(p, [0.8, 1], [1.02, 0.8]); sx = interpolate(p, [0.8, 1], [0.98, 1.2]); }
        }
        else {
            y = 0; x = 0;
            const p = Math.min((f - 85) / 15, 1);
            sy = interpolate(p, [0, 0.3, 0.7, 1], [0.8, 1.15, 0.95, 1]);
            sx = interpolate(p, [0, 0.3, 0.7, 1], [1.2, 0.85, 1.05, 1]);
        }
        return { x, y, sx, sy };
    }

    const currentPos = getPhysics(frame);

    // Function to generate radar rings
    const makeRadar = (delay: number) => {
        const p = spring({ frame: frame - delay, fps, config: { damping: 100, mass: 6 } });
        const opacity = interpolate(p, [0, 0.3, 1], [0, 0.6, 0]);
        const scale = interpolate(p, [0, 1], [0.1, 4]);
        return { opacity, scale, active: frame > delay };
    };
    const ripples = [makeRadar(30), makeRadar(50), makeRadar(70), makeRadar(85)];

    return (
        <AbsoluteFill style={{ background: '#f8fafc', justifyContent: 'center', alignItems: 'center' }}>
            {/* Elegant Ambient Mesh Gradient (Simple but not boring) */}
            <AbsoluteFill style={{ overflow: 'hidden' }}>
                {/* Slow ambient glow top-left */}
                <div style={{
                    position: 'absolute', width: '120%', height: '120%',
                    background: 'radial-gradient(circle, rgba(226,232,240,0.6) 0%, rgba(248,250,252,0) 60%)',
                    top: '-20%', left: '-20%',
                    transform: `translate(${Math.sin(frame * 0.01) * 80}px, ${Math.cos(frame * 0.015) * 80}px)`,
                }} />
                {/* Slow ambient glow bottom-right */}
                <div style={{
                    position: 'absolute', width: '140%', height: '140%',
                    background: 'radial-gradient(circle, rgba(241,245,249,0.8) 0%, rgba(248,250,252,0) 60%)',
                    bottom: '-30%', right: '-30%',
                    transform: `translate(${Math.cos(frame * 0.015) * 100}px, ${Math.sin(frame * 0.01) * 100}px)`,
                }} />

                {/* Constant Ambient Background Radar Rings representing 'Discovery / ScholarRadar' */}
                <div style={{ position: 'absolute', width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', opacity: 0.15 }}>
                    {[0, 1, 2, 3].map(i => {
                        const p = ((frame + i * 45) % 180) / 180;
                        return (
                            <div key={i} style={{
                                position: 'absolute',
                                width: 1200, height: 1200,
                                borderRadius: '50%',
                                border: '2px solid #64748b',
                                transform: `scale(${interpolate(p, [0, 1], [0.1, 1.5])})`,
                                opacity: interpolate(p, [0, 0.4, 0.8, 1], [0, 1, 0.5, 0])
                            }} />
                        );
                    })}
                </div>

                {/* Subtle Grid overlay */}
                <div style={{ position: 'absolute', width: '100%', height: '100%', backgroundImage: 'radial-gradient(#cbd5e1 1px, transparent 1px)', backgroundSize: '32px 32px', opacity: 0.2 }} />
            </AbsoluteFill>

            <div style={{ position: 'relative', transform: `scale(${boxScale})`, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                
                {/* Master White Container: Dynamically Expands at the End! */}
                <div style={{ 
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    backgroundColor: 'rgba(255,255,255,0.7)', backdropFilter: 'blur(12px)',
                    width: interpolate(spring({ frame: frame - 95, fps, config: { damping: 16 } }), [0, 1], [600, 850]), 
                    height: 240, 
                    borderRadius: 60, boxShadow: '0 20px 40px rgba(0,0,0,0.04)',
                    border: '1px solid rgba(255,255,255,1)'
                }}>
                    <style>
                        {`@import url('https://fonts.googleapis.com/css2?family=Inter:wght@800&display=swap');`}
                    </style>
                    
                    <div style={{ display: 'flex', alignItems: 'baseline', fontFamily: 'Inter', fontSize: 130, fontWeight: 800, letterSpacing: -8, color: '#111827' }}>
                        Skolr
                        <div style={{
                            position: 'relative', width: 40, height: 40,
                            marginLeft: interpolate(spring({ frame: frame - 95, fps, config: { damping: 14 } }), [0, 1], [2, 22]),
                            marginRight: 0
                        }}>

                            {/* Radar / Echo Rings on impact */}
                            {ripples.map((ripple, i) => ripple.active && (
                                <div key={'ripple'+i} style={{
                                    position: 'absolute', top: -5, left: -5, width: 50, height: 50,
                                    borderRadius: '50%', border: '4px solid #3b82f6',
                                    transform: `scale(${ripple.scale})`, opacity: ripple.opacity,
                                    transformOrigin: 'center center'
                                }} />
                            ))}

                            {/* The Main Bouncing Dot */}
                            {frame >= 20 && (
                            <div style={{
                                position: 'absolute', top: -5, left: -5, width: 50, height: 50, 
                                backgroundColor: '#2563eb', borderRadius: '50%',
                                transform: `translate(${currentPos.x}px, ${currentPos.y}px) scaleX(${currentPos.sx}) scaleY(${currentPos.sy})`,
                                boxShadow: currentPos.y < -10 ? '0 20px 40px rgba(37,99,235,0.4)' : '0 4px 20px rgba(37,99,235,0.6)',
                                transformOrigin: 'bottom center'
                            }} />
                            )}
                        </div>

                        {/* Staggered popping and sliding Reveal of 'xyz' */}
                        <div style={{
                            display: 'flex',
                            width: interpolate(spring({ frame: frame - 95, fps, config: { damping: 16 } }), [0, 1], [0, 260]),
                            color: '#9ca3af',
                            overflow: 'hidden',
                            marginLeft: interpolate(spring({ frame: frame - 95, fps, config: { damping: 14 } }), [0, 1], [40, 20]),
                            alignItems: 'baseline'
                        }}>
                            {"xyz".split("").map((char, index) => {
                                const charSpring = spring({ frame: frame - 100 - (index * 4), fps, config: { damping: 12, mass: 0.8 } });
                                return (
                                    <span key={index} style={{
                                        display: 'inline-block',
                                        opacity: interpolate(charSpring, [0, 1], [0, 1]),
                                        transform: `translateY(${interpolate(charSpring, [0, 1], [40, 0])}px) scale(${interpolate(charSpring, [0, 0.5, 1], [0.5, 1.2, 1])})`
                                    }}>
                                        {char}
                                    </span>
                                );
                            })}
                        </div>
                    </div>
                </div>

                {/* Subtitle explicitly defining MCP and Unbiasedness */}
                <div style={{
                    display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: 40,
                    opacity: interpolate(spring({ frame: frame - 110, fps, config: { damping: 14 } }), [0, 1], [0, 1]),
                    transform: `translateY(${interpolate(spring({ frame: frame - 110, fps, config: { damping: 14 } }), [0, 1], [30, 0])}px)`
                }}>
                    <h3 style={{
                        fontFamily: 'Inter', fontWeight: 600, fontSize: 32, letterSpacing: -1,
                        color: '#4b5563', margin: 0, padding: 0
                    }}>
                        The <span style={{ color: '#2563eb' }}>Unbiased MCP</span> for Global Education
                    </h3>
                </div>
            </div>
            
            {/* Audio Track Mapping using Remotion Best Practices (staticFile) and reliable Google Actions Sounds */}
            <Sequence from={2}> <Audio src={staticFile('sounds/whoosh.mp3')} volume={0.6} /> </Sequence>
            <Sequence from={29}> <Audio src={staticFile('sounds/ding.mp3')} volume={0.4} playbackRate={2.0} /> </Sequence>
            <Sequence from={49}> <Audio src={staticFile('sounds/ding.mp3')} volume={0.3} playbackRate={2.2} /> </Sequence>
            <Sequence from={69}> <Audio src={staticFile('sounds/ding.mp3')} volume={0.2} playbackRate={2.4} /> </Sequence>
            
            {/* Final Ding and typing pop sounds for 'xyz' Expansion (3 characters = 3 pops) */}
            <Sequence from={85}> <Audio src={staticFile('sounds/ding.mp3')} volume={1} /> </Sequence>
            <Sequence from={100}> <Audio src={staticFile('sounds/ding.mp3')} volume={0.5} playbackRate={3.0} /> </Sequence>
            <Sequence from={104}> <Audio src={staticFile('sounds/ding.mp3')} volume={0.4} playbackRate={3.2} /> </Sequence>
            <Sequence from={108}> <Audio src={staticFile('sounds/ding.mp3')} volume={0.3} playbackRate={3.4} /> </Sequence>
            
            {/* Subtitle gentle whoosh */}
            <Sequence from={110}> <Audio src={staticFile('sounds/whoosh.mp3')} volume={0.5} playbackRate={0.7} /> </Sequence>
        </AbsoluteFill>
    );
}
