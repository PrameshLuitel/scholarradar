import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';

export const DataRain: React.FC = () => {
    const frame = useCurrentFrame();
    
    const characters = "0123456789ABCDEF!@#$%^&*()_+-=[]{}|;:,.<>?";
    const columns = 20;

    return (
        <AbsoluteFill style={{ overflow: 'hidden', opacity: 0.15 }}>
            {new Array(columns).fill(0).map((_, i) => {
                const columnX = (i * 100) / (columns - 1);
                const delay = i * 2;
                const speed = 10 + (i % 5) * 5;
                const dropY = ((frame - delay) * speed) % 1080;

                return (
                    <div key={i} style={{
                        position: 'absolute',
                        left: `${columnX}%`,
                        top: dropY,
                        color: '#4ade80',
                        fontSize: 24,
                        fontFamily: 'monospace',
                        writingMode: 'vertical-rl',
                        textShadow: '0 0 10px #4ade80'
                    }}>
                        {new Array(10).fill(0).map((_, j) => (
                            <div key={j} style={{ opacity: 1 - j * 0.1 }}>
                                {characters[Math.floor((frame + i + j) % characters.length)]}
                            </div>
                        ))}
                    </div>
                );
            })}
        </AbsoluteFill>
    );
};
