import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate, Easing } from 'remotion';
import { DataRain } from './DataRain';

export const ClaudeSimulation: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // Scene timing variables adjusted to fit the 585-frame sequence duration
    // Scene 1: Initial Prompt (0-120)
    // Scene 2: Masters Results (120-250)
    // Scene 3: Cost & Visa Prompt (260-350)
    // Scene 4: Analysis Results (360-585)

    const opacity = interpolate(frame, [0, 15], [0, 1]);
    const browserScale = spring({ frame, fps, config: { damping: 12, mass: 0.8, stiffness: 80 } });
    const browserTiltX = interpolate(browserScale, [0, 1], [40, 0]);
    const browserTiltY = interpolate(browserScale, [0, 1], [-25, 0]);

    // Scene 1 & 2 Text
    const text1 = "Find me a Masters in CS in Canada with full scholarships.";
    const typing1 = Math.floor(interpolate(frame, [40, 120], [0, text1.length], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
    
    // Scene 3 Text: New Prompt
    const text2 = "Compare living costs & Visa success rates.";
    const typing2 = Math.floor(interpolate(frame, [260, 350], [0, text2.length], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
    
    const isScene2 = frame < 255;
    const isScene3Onwards = frame >= 255;

    const currentText = isScene2 ? text1.slice(0, typing1) : text2.slice(0, typing2);
    const showCursor = (frame > 40 && frame < 140) || (frame > 255 && frame < 370);

    // Initial Cards Animation
    const renderCard = (university: string, deadline: string, index: number) => {
        const cardDelay = 140 + index * 12;
        const cardSpr = spring({ frame: frame - cardDelay, fps, config: { damping: 10, stiffness: 120, mass: 0.8 } });
        const cardFadeOut = spring({ frame: frame - 250 - (index * 5), fps, config: { damping: 12 } });
        
        const cardScale = interpolate(cardSpr, [0, 1], [0.6, 1]) * interpolate(cardFadeOut, [0, 1], [1, 0.8]);
        const cardY = interpolate(cardSpr, [0, 1], [80, 0]) - interpolate(cardFadeOut, [0, 1], [0, 100]);
        const cardOpacity = interpolate(cardSpr, [0, 1], [0, 1]) * interpolate(cardFadeOut, [0, 1], [1, 0]);

        return (
            <div key={index} style={{
                background: 'rgba(255, 255, 255, 0.08)', backdropFilter: 'blur(20px)', borderRadius: 24, padding: 30, marginBottom: 20,
                border: '1px solid rgba(255, 255, 255, 0.2)', opacity: cardOpacity,
                transform: `scale(${cardScale}) translateY(${cardY}px)`,
                boxShadow: `0 10px 30px rgba(0,0,0,0.3)`,
                display: 'flex', justifyContent: 'space-between', alignItems: 'center'
            }}>
                <div>
                    <h3 style={{ margin: 0, color: 'white', fontSize: 26, fontWeight: 600 }}>{university}</h3>
                    <div style={{ marginTop: 10, display: 'flex', gap: 15 }}>
                        <span style={{ backgroundColor: '#2563eb', color: 'white', padding: '4px 12px', borderRadius: 10, fontSize: 16, fontWeight: 700 }}>Full Scholarship</span>
                        <span style={{ color: '#9ca3af', fontSize: 16 }}>Deadline: {deadline}</span>
                    </div>
                </div>
                <div style={{ backgroundColor: 'white', color: 'black', fontWeight: 800, padding: '12px 24px', borderRadius: 50 }}>Apply</div>
            </div>
        );
    };

    // Scraper URL Stream Logic
    const urls = [
        "https://harvard.edu/financial-aid/prospective-students",
        "https://utoronto.ca/international/scholarships",
        "https://mcgill.ca/studentaid/scholarships-aid/international",
        "https://ox.ac.uk/admissions/graduate/fees-and-funding",
        "https://mit.edu/admissions/international/scholarships"
    ];

    const renderScraperLogic = () => {
        const isActive = frame > 60 && frame < 180;
        if (!isActive) return null;

        const urlIndex = Math.floor((frame % 15) / (15 / urls.length)); // Sped up
        const currentUrl = urls[urlIndex];

        return (
            <div style={{
                position: 'absolute', top: 520, left: 100, color: '#4ade80', fontSize: 18, fontFamily: 'monospace',
                opacity: 0.8, display: 'flex', flexDirection: 'column', gap: 5, pointerEvents: 'none'
            }}>
                <div style={{ fontWeight: 'bold' }}>📡 LIVE SCRAPER ACTIVE...</div>
                <div style={{ overflow: 'hidden', whiteSpace: 'nowrap', width: 400 }}>
                    {`> GET ${currentUrl}`}
                </div>
                <div style={{ color: '#22c55e' }}>{`[200 OK] DATA_PARSED: ${Math.random().toString(36).substring(7)}`}</div>
            </div>
        );
    };

    const renderAnalysisWidgets = () => {
        const animStart = 360;
        
        const barSpr = spring({ frame: frame - animStart, fps, config: { damping: 12, mass: 0.8 } });
        const visaSpr = spring({ frame: frame - (animStart + 40), fps, config: { damping: 10, stiffness: 100 } });
        
        return (
            <div style={{ display: 'flex', gap: 30, opacity: interpolate(barSpr, [0, 0.5], [0, 1]) }}>
                {/* Cost Analysis Card */}
                <div style={{
                    flex: 1, background: 'rgba(255, 255, 255, 0.05)', borderRadius: 30, padding: 40,
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    transform: `translateY(${interpolate(barSpr, [0, 1], [100, 0])}px)`
                }}>
                    <h3 style={{ color: 'white', margin: '0 0 20px 0', fontSize: 24, display: 'flex', alignItems: 'center', gap: 10 }}>
                        <span style={{ fontSize: 30 }}>📊</span> Annual Living Costs (CAD)
                    </h3>
                    
                    {/* Toronto Bar */}
                    <div style={{ marginBottom: 20 }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', color: '#cbd5e1', marginBottom: 8, fontSize: 18 }}>
                            <span>Toronto (UofT)</span><span>$24,500</span>
                        </div>
                        <div style={{ height: 20, background: 'rgba(255,255,255,0.1)', borderRadius: 10, overflow: 'hidden' }}>
                            <div style={{ height: '100%', width: `${interpolate(barSpr, [0, 1], [0, 85])}%`, background: 'linear-gradient(90deg, #ef4444, #f97316)', borderRadius: 10 }} />
                        </div>
                    </div>
                    
                    {/* McGill Bar */}
                    <div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', color: '#cbd5e1', marginBottom: 8, fontSize: 18 }}>
                            <span>Montreal (McGill)</span><span style={{color: '#4ade80', fontWeight: 'bold'}}>$16,200 (Lower!)</span>
                        </div>
                        <div style={{ height: 20, background: 'rgba(255,255,255,0.1)', borderRadius: 10, overflow: 'hidden' }}>
                            <div style={{ height: '100%', width: `${interpolate(barSpr, [0, 1], [0, 55])}%`, background: 'linear-gradient(90deg, #22c55e, #10b981)', borderRadius: 10 }} />
                        </div>
                    </div>
                </div>

                {/* Visa Success Rate Widget */}
                <div style={{
                    width: 300, background: 'linear-gradient(135deg, rgba(37,99,235,0.1), rgba(147,51,234,0.1))',
                    borderRadius: 30, padding: 40, border: '1px solid rgba(147,51,234,0.3)',
                    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
                    transform: `scale(${interpolate(visaSpr, [0, 1], [0.5, 1])})`,
                    boxShadow: `0 0 ${interpolate(Math.sin((frame - animStart)*0.1), [-1, 1], [20, 50])}px rgba(147,51,234,0.3)`
                }}>
                    <div style={{ color: '#e2e8f0', fontSize: 20, marginBottom: 15, fontWeight: 600, textAlign: 'center' }}>Study Permit<br/>Approval Rate</div>
                    <div style={{ position: 'relative', width: 140, height: 140 }}>
                        {/* Circular Progress Background */}
                        <svg width="140" height="140" viewBox="0 0 100 100">
                            <circle cx="50" cy="50" r="45" fill="none" stroke="rgba(255,255,255,0.1)" strokeWidth="10" />
                            {/* Circular Progress Foreground */}
                            <circle cx="50" cy="50" r="45" fill="none" stroke="#22c55e" strokeWidth="10" 
                                strokeDasharray="282.7" 
                                strokeDashoffset={interpolate(visaSpr, [0, 1], [282.7, 282.7 * (1 - 0.92)])} 
                                strokeLinecap="round" transform="rotate(-90 50 50)" 
                                style={{ filter: 'drop-shadow(0 0 8px #22c55e)' }} />
                        </svg>
                        <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white', fontSize: 32, fontWeight: 900 }}>
                            {Math.floor(interpolate(visaSpr, [0, 1], [0, 92]))}%
                        </div>
                    </div>
                </div>
            </div>
        );
    };

    return (
        <AbsoluteFill style={{ background: '#0a0a0a', justifyContent: 'center', alignItems: 'center', opacity }}>
            {/* Ambient Background Orbs */}
            <div style={{ position: 'absolute', width: '100%', height: '100%', pointerEvents: 'none' }}>
                <div style={{
                    position: 'absolute', top: '10%', left: '10%', width: 600, height: 600,
                    background: isScene3Onwards ? 'radial-gradient(circle, rgba(147,51,234,0.2) 0%, transparent 70%)' : 'radial-gradient(circle, rgba(37,99,235,0.2) 0%, transparent 70%)',
                    borderRadius: '50%', transformOrigin: 'center center',
                    transform: `translate(${Math.sin(frame * 0.02) * 80}px, ${Math.cos(frame * 0.02) * 80}px) scale(${interpolate(Math.sin(frame * 0.05), [-1, 1], [0.8, 1.2])})`,
                    transition: 'background 1s ease'
                }} />
                <div style={{
                    position: 'absolute', bottom: '10%', right: '10%', width: 800, height: 800,
                    background: isScene3Onwards ? 'radial-gradient(circle, rgba(236,72,153,0.15) 0%, transparent 70%)' : 'radial-gradient(circle, rgba(96,165,250,0.15) 0%, transparent 70%)',
                    borderRadius: '50%',
                    transform: `translate(${Math.cos(frame * 0.015) * 120}px, ${Math.sin(frame * 0.015) * 120}px) scale(${interpolate(Math.cos(frame * 0.04), [-1, 1], [0.9, 1.1])})`,
                    transition: 'background 1s ease'
                }} />
            </div>

            {/* Browser Hub */}
            <div style={{
                width: 900, height: 1400, background: 'rgba(15, 15, 15, 0.85)', backdropFilter: 'blur(40px)', borderRadius: 40,
                border: `1px solid rgba(255, 255, 255, ${interpolate(Math.sin(frame * 0.1), [-1, 1], [0.1, 0.3])})`,
                boxShadow: isScene3Onwards ? '0 50px 150px rgba(0,0,0,0.8), 0 0 60px rgba(147,51,234,0.3)' : '0 50px 150px rgba(0,0,0,0.8), 0 0 60px rgba(37,99,235,0.3)',
                transform: `scale(${browserScale}) perspective(1200px) rotateX(${browserTiltX}deg) rotateY(${browserTiltY}deg)`,
                overflow: 'hidden', display: 'flex', flexDirection: 'column',
                transition: 'box-shadow 1s ease'
            }}>
                {/* Browser Header */}
                <div style={{ height: 80, borderBottom: '1px solid rgba(255, 255, 255, 0.05)', display: 'flex', alignItems: 'center', padding: '0 30px', gap: 15 }}>
                    <div style={{ display: 'flex', gap: 10 }}>
                        <div style={{ width: 15, height: 15, borderRadius: '50%', backgroundColor: '#ff5f56' }} />
                        <div style={{ width: 15, height: 15, borderRadius: '50%', backgroundColor: '#ffbd2e' }} />
                        <div style={{ width: 15, height: 15, borderRadius: '50%', backgroundColor: '#27c93f' }} />
                    </div>
                    <div style={{
                        flex: 1, height: 40, background: 'rgba(255, 255, 255, 0.05)', borderRadius: 20, 
                        display: 'flex', alignItems: 'center', padding: '0 20px', color: '#6b7280', fontSize: 16
                    }}>claude.ai</div>
                </div>

                {/* Claude UI */}
                <div style={{ flex: 1, padding: 50, display: 'flex', flexDirection: 'column' }}>
                    <DataRain />
                    <div style={{ color: 'white', fontSize: 44, fontWeight: 700, marginBottom: 40, fontFamily: 'serif', zIndex: 1 }}>Claude 3.1</div>

                    <div style={{ position: 'relative', flex: 1 }}>
                        {/* Prompt Box */}
                        <div style={{
                            background: 'rgba(255, 255, 255, 0.05)', borderRadius: 24, padding: 25,
                            border: '1px solid rgba(255, 255, 255, 0.15)', boxShadow: '0 10px 30px rgba(0,0,0,0.5)',
                            fontSize: 32, color: 'white', minHeight: 120, lineHeight: 1.4, marginBottom: 40,
                            transform: `scale(${spring({ frame: isScene3Onwards ? frame - 280 : frame - 20, fps, config: { damping: 10, mass: 0.5 } })})`,
                        }}>
                            {currentText}
                            {showCursor && <span style={{ borderLeft: '4px solid #2563eb', marginLeft: 4, height: '1em', display: 'inline-block', verticalAlign: 'middle' }}>&nbsp;</span>}
                        </div>

                        {/* Content Area */}
                        <div style={{ position: 'relative', flex: 1 }}>
                            {renderScraperLogic()}
                            {/* Scene 1/2: Scholarship Results */}
                            <div style={{ position: 'absolute', width: '100%', top: 0, opacity: interpolate(spring({ frame: frame - 250, fps }), [0, 1], [1, 0]) }}>
                                <div style={{ 
                                    opacity: interpolate(frame, [130, 150], [0, 1]),
                                    color: '#2563eb', fontWeight: 800, fontSize: 20, marginBottom: 30, letterSpacing: 2, textTransform: 'uppercase',
                                    textShadow: '0 0 15px rgba(37,99,235,0.5)', transform: `translateY(${interpolate(spring({ frame: frame - 170, fps }), [0, 1], [30, 0])}px)`
                                }}>Data by Skolr ↓</div>
                                {renderCard("University of Toronto", "March 15, 2026", 0)}
                                {renderCard("McGill University", "January 30, 2026", 1)}
                                {renderCard("UBC Vancouver", "Feb 10, 2026", 2)}
                            </div>

                            {/* Scene 3/4: Visa & Costs Results */}
                            {isScene3Onwards && (
                                <div style={{ position: 'absolute', width: '100%', top: 0, opacity: interpolate(frame, [390, 400], [0, 1]) }}>
                                    <div style={{ 
                                        color: '#a855f7', fontWeight: 800, fontSize: 20, marginBottom: 30, letterSpacing: 2, textTransform: 'uppercase',
                                        textShadow: '0 0 15px rgba(168,85,247,0.5)', transform: `translateY(${interpolate(spring({ frame: frame - 390, fps }), [0, 1], [30, 0])}px)`
                                    }}>Skolr ROI & Visa Engine ↓</div>
                                    {renderAnalysisWidgets()}

                                    {/* Final CTA Button popping in at the end */}
                                    <div style={{
                                        marginTop: 40, background: 'white', color: 'black', fontSize: 24, fontWeight: 900,
                                        padding: '20px 40px', borderRadius: 40, textAlign: 'center', display: 'inline-block', cursor: 'pointer',
                                        transform: `scale(${spring({ frame: frame - 550, fps, config: { damping: 12 } })})`,
                                        boxShadow: `0 0 ${interpolate(Math.sin(frame * 0.2), [-1, 1], [10, 30])}px rgba(255,255,255,0.8)`
                                    }}>
                                        Add to Application Dashboard 🚀
                                    </div>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {/* Float Overlay Badge (Glassmorphism) */}
            <div style={{
                position: 'absolute', top: 400, right: 30, width: 340, padding: 30,
                background: 'rgba(255,255,255,0.1)', backdropFilter: 'blur(20px)', borderRadius: 30,
                border: '1px solid rgba(255,255,255,0.2)', boxShadow: '0 20px 50px rgba(0,0,0,0.3)',
                opacity: interpolate(spring({ frame: frame - 280, fps }), [0, 1], [spring({ frame: frame - 200, fps }), 0]),
                transform: `scale(${interpolate(spring({ frame: frame - 200, fps, config: { damping: 10 } }), [0, 1], [0.1, 1])}) rotateZ(${interpolate(spring({ frame: frame - 200, fps }), [0, 1], [15, 0])}deg)`,
                zIndex: 100
            }}>
                 <h4 style={{ margin: 0, color: 'white', fontSize: 24, fontWeight: 900, textShadow: '0 0 10px rgba(255,255,255,0.5)' }}>REAL DATA.</h4>
                 <p style={{ margin: '10px 0 0 0', color: '#9ca3af', fontSize: 18 }}>Updated 24h ago from official sources.</p>
            </div>
        </AbsoluteFill>
    );
};
