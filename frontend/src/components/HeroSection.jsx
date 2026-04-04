import React from 'react';
import './HeroSection.css';

const HeroSection = () => {
  const codeSnippet = `// Request
{
  "jsonrpc": "2.0",
  "method": "call_tool",
  "params": {
    "name": "get_scholarships",
    "arguments": {
      "level": "phd",
      "country": "canada"
    }
  },
  "id": "1"
}`;

  return (
    <section className="hero">
      <div className="hero-container">
        
        <div className="hero-content">
          <div className="hero-badge">Model Context Protocol Server</div>
          <h1 className="hero-title">
            The data layer for<br/>
            global education.
          </h1>
          <p className="hero-subtitle">
            ScholarRadar provides native MCP tools for AI agents to query 5,000+ university programs, direct scholarships, and visa requirements in real-time.
          </p>
          
          <div className="hero-actions">
            <button className="btn btn-primary">Read the Docs</button>
            <button className="btn btn-secondary">View on GitHub</button>
          </div>
        </div>

        <div className="hero-visual">
          <div className="code-window">
            <div className="code-header">
              <span className="dot dot-red"></span>
              <span className="dot dot-yellow"></span>
              <span className="dot dot-green"></span>
              <span className="code-title">mcp-server-request.json</span>
            </div>
            <pre className="code-block">
              <code>{codeSnippet}</code>
            </pre>
          </div>
        </div>

      </div>
    </section>
  );
};

export default HeroSection;
