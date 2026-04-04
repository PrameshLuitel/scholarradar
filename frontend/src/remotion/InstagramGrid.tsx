import { AbsoluteFill, Img, staticFile } from 'remotion';

export const InstaGridMaster: React.FC<{ offsetX: number }> = ({ offsetX }) => {
    return (
        <AbsoluteFill style={{ overflow: 'hidden', backgroundColor: '#f8fafc' }}>
            <div style={{ position: 'absolute', left: -offsetX, width: 3240, height: 1350, display: 'flex' }}>
                
                {/* --- 1. CORE THEME BACKGROUND (Skolr / Cluely Aesthetic) --- */}
                {/* Extremely soft, premium off-white ambient light */}
                <div style={{
                    position: 'absolute', width: '100%', height: '100%',
                    background: 'radial-gradient(circle at 50% 0%, #ffffff 0%, #f8fafc 100%)'
                }} />
                
                {/* 2. ELEGANT STATIC SVG WAVES (Framing the bottom like a premium landing page) */}
                <div style={{ position: 'absolute', bottom: -50, left: 0, width: '100%', height: 400, display: 'flex', opacity: 0.7 }}>
                    <svg viewBox="0 0 3240 400" preserveAspectRatio="none" style={{ position: 'absolute', bottom: 0, width: '100%', height: '100%' }}>
                        <path fill="#e2e8f0" d="M0,200 C800,100 1600,300 3240,200 L3240,400 L0,400 Z" />
                    </svg>
                    <svg viewBox="0 0 3240 400" preserveAspectRatio="none" style={{ position: 'absolute', bottom: 0, width: '100%', height: '80%' }}>
                        <path fill="#f1f5f9" d="M0,150 C1000,50 2000,250 3240,150 L3240,400 L0,400 Z" />
                    </svg>
                    <svg viewBox="0 0 3240 400" preserveAspectRatio="none" style={{ position: 'absolute', bottom: 0, width: '100%', height: '60%' }}>
                        <path fill="#ffffff" d="M0,100 C1200,0 2400,200 3240,100 L3240,400 L0,400 Z" />
                    </svg>
                </div>

                {/* 3. SUBTLE RADAR RINGS (Thematic consistency with ScholarRadar) */}
                <div style={{ position: 'absolute', width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', opacity: 0.15 }}>
                    {[0, 1, 2, 3].map(i => (
                        <div key={i} style={{
                            position: 'absolute',
                            width: 1000 + i * 500, height: 1000 + i * 500,
                            borderRadius: '50%',
                            border: '2px solid #64748b',
                        }} />
                    ))}
                </div>

                {/* Grid Overlay for technical texture */}
                <div style={{ position: 'absolute', width: '100%', height: '100%', backgroundImage: 'radial-gradient(#cbd5e1 2px, transparent 2px)', backgroundSize: '48px 48px', opacity: 0.2 }} />


                {/* --- JAW-DROPPING BACKGROUND TILTED GLASS SCREENS --- */}
                
                {/* SCREEN 1: LLM Chat Interface (Tilted towards center, placed bridging Panel 1 and Panel 2) */}
                <div style={{
                    position: 'absolute', left: 450, top: 160, width: 900, height: 600,
                    backgroundColor: 'rgba(255, 255, 255, 0.75)', backdropFilter: 'blur(24px)',
                    border: '1px solid #ffffff', borderRadius: 24, padding: 40,
                    boxShadow: '0 40px 80px rgba(0,0,0,0.06)',
                    transform: 'perspective(2000px) rotateY(22deg) rotateX(12deg) rotateZ(-2deg)',
                    zIndex: 0, opacity: 0.95
                }}>
                    {/* Header Dots */}
                    <div style={{ display: 'flex', gap: 10, marginBottom: 50 }}>
                        <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#ef4444' }} />
                        <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#eab308' }} />
                        <div style={{ width: 14, height: 14, borderRadius: '50%', backgroundColor: '#22c55e' }} />
                    </div>
                    
                    {/* User Prompt */}
                    <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: 40 }}>
                        <div style={{ backgroundColor: '#2563eb', color: 'white', padding: '24px 32px', borderRadius: '24px 24px 6px 24px', fontFamily: 'Inter', fontSize: 28, maxWidth: '85%', boxShadow: '0 10px 25px rgba(37,99,235,0.25)', lineHeight: 1.4 }}>
                            Find fully funded Master's programs in Australia for AI.
                        </div>
                    </div>
                    
                    {/* AI Loading/Processing */}
                    <div style={{ display: 'flex', justifyContent: 'flex-start' }}>
                        <div style={{ backgroundColor: '#ffffff', border: '1px solid #e2e8f0', color: '#334155', padding: '24px 32px', borderRadius: '6px 24px 24px 24px', fontFamily: 'Inter', fontSize: 26, maxWidth: '75%', display: 'flex', alignItems: 'center', gap: 20, boxShadow: '0 10px 30px rgba(0,0,0,0.05)', fontWeight: 500 }}>
                            <div style={{ width: 28, height: 28, border: '4px solid #e2e8f0', borderTopColor: '#2563eb', borderRadius: '50%' }} />
                            Calling ScholarRadar MCP...
                        </div>
                    </div>
                </div>

                {/* SCREEN 2: Light Mode Code Window / JSON (Tilted away, bridging Panel 2 and Panel 3) */}
                <div style={{
                    position: 'absolute', left: 1680, top: 580, width: 750, height: 600,
                    backgroundColor: 'rgba(255, 255, 255, 0.85)', backdropFilter: 'blur(24px)',
                    border: '1px solid #ffffff', borderRadius: 24, padding: 32,
                    boxShadow: '0 40px 80px rgba(0,0,0,0.06)',
                    transform: 'perspective(2000px) rotateY(-24deg) rotateX(10deg) rotateZ(3deg)',
                    zIndex: 0, opacity: 0.95, color: '#334155', fontFamily: 'monospace', fontSize: 20, lineHeight: 1.7
                }}>
                    <div style={{ display: 'flex', gap: 10, marginBottom: 20, borderBottom: '1px solid #e2e8f0', paddingBottom: 16 }}>
                        <span style={{ color: '#64748b', fontSize: 18, fontFamily: 'Inter', fontWeight: 500 }}>mcp-tool-call.json</span>
                    </div>
                    <div style={{ whiteSpace: 'pre-wrap' }}>
                        {'{'}<br/>
                        {'  '}<span style={{ color: '#0369a1', fontWeight: 600 }}>"method"</span>: <span style={{ color: '#2563eb' }}>"call_tool"</span>,<br/>
                        {'  '}<span style={{ color: '#0369a1', fontWeight: 600 }}>"params"</span>: {'{'}<br/>
                        {'    '}<span style={{ color: '#0369a1', fontWeight: 600 }}>"name"</span>: <span style={{ color: '#2563eb' }}>"get_scholarships"</span>,<br/>
                        {'    '}<span style={{ color: '#0369a1', fontWeight: 600 }}>"arguments"</span>: {'{'}<br/>
                        {'      '}<span style={{ color: '#0f766e', fontWeight: 600 }}>"level"</span>: <span style={{ color: '#16a34a' }}>"masters"</span>,<br/>
                        {'      '}<span style={{ color: '#0f766e', fontWeight: 600 }}>"country"</span>: <span style={{ color: '#16a34a' }}>"Australia"</span>,<br/>
                        {'      '}<span style={{ color: '#0f766e', fontWeight: 600 }}>"funding"</span>: <span style={{ color: '#16a34a' }}>"fully_funded"</span>,<br/>
                        {'      '}<span style={{ color: '#0f766e', fontWeight: 600 }}>"major"</span>: <span style={{ color: '#16a34a' }}>"Artificial Intelligence"</span><br/>
                        {'    }'}<br/>
                        {'  }'}<br/>
                        {'}'}
                    </div>
                </div>


                {/* --- CONTENT PANELS --- */}

                {/* 1. LEFT PANEL CONTENT (0 to 1080px) */}
                <div style={{ position: 'absolute', left: 0, width: 1080, height: 1350, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'flex-start', paddingLeft: 120 }}>
                    {/* Clean flat badge from the Hero */}
                    <div style={{ 
                        padding: '12px 24px', border: '1px solid #e2e8f0', borderRadius: 8, 
                        backgroundColor: '#ffffff', color: '#334155', 
                        fontWeight: 500, fontSize: 24, marginBottom: 40,
                        boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)'
                    }}>
                        Model Context Protocol Server
                    </div>
                    
                    <h1 style={{ fontFamily: 'Inter', fontSize: 130, fontWeight: 800, letterSpacing: -5, color: '#0f172a', margin: 0, lineHeight: 1.05 }}>
                        Unbiased
                    </h1>
                    <h1 style={{ fontFamily: 'Inter', fontSize: 130, fontWeight: 800, letterSpacing: -5, color: '#0f172a', margin: 0, lineHeight: 1.05 }}>
                        MCP Engine.
                    </h1>
                </div>

                {/* 2. CENTER PANEL CONTENT (1080px to 2160px) */}
                <div style={{ position: 'absolute', left: 1080, width: 1080, height: 1350, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                    
                    {/* The Official Skolr Social Logo Image directly embedded */}
                    <Img 
                        src={staticFile('skolr-social-logo.svg')} 
                        style={{ width: 850, height: 'auto', zIndex: 10, filter: 'drop-shadow(0 30px 60px rgba(15,23,42,0.1))' }} 
                    />

                </div>

                {/* 3. RIGHT PANEL CONTENT (2160px to 3240px) */}
                <div style={{ position: 'absolute', left: 2160, width: 1080, height: 1350, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'flex-start', paddingLeft: 240 }}>
                    <h1 style={{ fontFamily: 'Inter', fontSize: 110, fontWeight: 800, letterSpacing: -4, color: '#0f172a', margin: 0, lineHeight: 1.1 }}>
                        Global
                    </h1>
                    <h1 style={{ fontFamily: 'Inter', fontSize: 110, fontWeight: 800, letterSpacing: -4, color: '#0f172a', margin: 0, lineHeight: 1.1 }}>
                        Education
                    </h1>
                    <h1 style={{ fontFamily: 'Inter', fontSize: 110, fontWeight: 800, letterSpacing: -4, color: '#94a3b8', margin: 0, lineHeight: 1.1 }}>
                        Unlocked.
                    </h1>
                    
                    {/* Hero-matched Button */}
                    <div style={{ 
                        marginTop: 80, padding: '24px 50px', 
                        backgroundColor: '#2563eb', color: 'white', 
                        borderRadius: 12, fontFamily: 'Inter', fontSize: 32, fontWeight: 500,
                        border: '1px solid #2563eb',
                        display: 'flex', alignItems: 'center', gap: 16,
                        boxShadow: '0 4px 6px -1px rgba(37,99,235,0.2)'
                    }}>
                        Start Discovering 
                        <span style={{ fontSize: 34 }}>→</span>
                    </div>
                </div>

            </div>
        </AbsoluteFill>
    );
};

export const InstaGridLeft: React.FC = () => <InstaGridMaster offsetX={0} />
export const InstaGridCenter: React.FC = () => <InstaGridMaster offsetX={1080} />
export const InstaGridRight: React.FC = () => <InstaGridMaster offsetX={1080 * 2} />
