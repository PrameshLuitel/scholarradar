import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const InFeedOverlay: React.FC<{
    status: 'scam' | 'official' | 'alert';
    text: string;
    startFrame: number;
}> = ({ status, text, startFrame }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const spr = spring({
        frame: frame - startFrame,
        fps,
        config: { damping: 10, stiffness: 100, mass: 0.8 },
    });

    const scale = interpolate(spr, [0, 1], [0.8, 1]);
    const opacity = interpolate(spr, [0, 1], [0, 1]);

    const getColors = () => {
        switch (status) {
            case 'scam': return { bg: '#ef4444', text: 'white', shadow: 'rgba(239, 68, 68, 0.5)' };
            case 'official': return { bg: '#22c55e', text: 'white', shadow: 'rgba(34, 197, 94, 0.5)' };
            case 'alert': return { bg: '#eab308', text: 'black', shadow: 'rgba(234, 179, 8, 0.5)' };
            default: return { bg: 'white', text: 'black', shadow: 'rgba(0,0,0,0.2)' };
        }
    };

    const colors = getColors();

    // Jiggle animation for "Scam" alerts
    const jiggle = status === 'scam' ? Math.sin(frame * 0.5) * 5 : 0;

    return (
        <div style={{
            position: 'absolute',
            top: 150,
            left: '50%',
            transform: `translateX(-50%) scale(${scale}) rotate(${jiggle}deg)`,
            opacity: opacity,
            backgroundColor: colors.bg,
            color: colors.text,
            padding: '20px 60px',
            borderRadius: 100,
            fontSize: 48,
            fontWeight: 900,
            textAlign: 'center',
            boxShadow: `0 20px 50px ${colors.shadow}, 0 0 40px ${colors.bg}`,
            zIndex: 1000,
            border: '4px solid white',
            whiteSpace: 'nowrap'
        }}>
            {text.toUpperCase()}
        </div>
    );
};

export const CommentBadge: React.FC<{
    user: string;
    text: string;
    delay: number;
}> = ({ user, text, delay }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const spr = spring({
        frame: frame - delay,
        fps,
        config: { damping: 12, stiffness: 120 },
    });

    const x = interpolate(spr, [0, 1], [-200, 40]);
    const opacity = interpolate(spr, [0, 1], [0, 1]);

    return (
        <div style={{
            position: 'absolute',
            bottom: 400 + (delay * 0.5),
            left: x,
            opacity: opacity,
            background: 'rgba(255, 255, 255, 0.1)',
            backdropFilter: 'blur(10px)',
            borderRadius: 20,
            padding: '15px 25px',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            display: 'flex',
            alignItems: 'center',
            gap: 15,
            width: 500
        }}>
            <div style={{ width: 40, height: 40, borderRadius: '50%', background: 'linear-gradient(45deg, #f093fb 0%, #f5576c 100%)' }} />
            <div>
                <div style={{ color: 'white', fontSize: 18, fontWeight: 700 }}>@{user}</div>
                <div style={{ color: '#d1d5db', fontSize: 20 }}>{text}</div>
            </div>
        </div>
    );
};
