import React from 'react';
import { Network, Search, FileText, Zap, ArrowRight, Box } from 'lucide-react';

export default function Home() {
  return (
    <>
      <section className="relative pt-24 pb-16 md:pt-32 md:pb-20 lg:pt-44 lg:pb-32 overflow-hidden">
        <div 
          className="absolute inset-0 z-0 opacity-[0.05] pointer-events-none" 
          style={{ backgroundImage: `url('/images/data_texture.png')`, backgroundSize: 'cover', backgroundPosition: 'center' }}
        ></div>
        
        <div className="max-w-7xl mx-auto px-5 relative z-10 flex flex-col lg:flex-row items-center gap-10 lg:gap-16">
          <div className="flex-1 text-center lg:text-left">
            <h1 className="font-serif text-5xl sm:text-6xl md:text-8xl font-medium tracking-normal text-gray-900 mb-6 md:mb-8 leading-[1.05]">
              The moment your AI<br />
              <span className="italic text-gray-500">stops guessing.</span>
            </h1>
            
            <p className="text-lg md:text-xl lg:text-2xl text-gray-500 mb-8 md:mb-10 max-w-xl font-light leading-relaxed mx-auto lg:mx-0">
              Skolr connects any AI to live university data from 30+ countries. Programs, scholarships, deadlines, visa rules. Scraped daily from official sources. Free. One URL to start.
            </p>

            <div className="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4 md:gap-5">
              <a href="#connect" className="w-full sm:w-auto relative group overflow-hidden px-8 py-4 text-base font-medium text-white bg-blue-600 rounded-full shadow-[0_8px_30px_rgb(37,99,235,0.4)] hover:shadow-[0_8px_30px_rgb(37,99,235,0.6)] transition-all hover:-translate-y-1 active:translate-y-0 border border-blue-400/30 ring-1 ring-inset ring-white/20 flex items-center justify-center gap-2">
                <span className="relative z-10 flex items-center gap-2 drop-shadow-sm">Connect Now <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform"/></span>
                <div className="absolute inset-0 bg-gradient-to-b from-white/20 to-transparent opacity-50 rounded-full pointer-events-none"></div>
              </a>
              <a href="#features" className="text-base font-medium text-gray-500 hover:text-black transition-colors border-b border-transparent hover:border-black pb-1">
                See what it can do
              </a>
            </div>
            
            <p className="mt-6 text-[10px] text-gray-400 font-light max-w-md mx-auto lg:mx-0">
              *Skolr is an AI data proxy. Not professional advice. Verify all data on official university or government sites.
            </p>
          </div>
          
          <div className="flex-1 relative w-full max-w-sm sm:max-w-md md:max-w-lg lg:max-w-none mt-4 lg:mt-0">
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[120%] h-[120%] bg-blue-400/10 blur-[120px] rounded-full pointer-events-none"></div>
            <img 
              src="/images/skolr_hero_art_2.png" 
              alt="Skolr University Architecture" 
              className="relative z-10 w-full h-auto drop-shadow-2xl rounded-[2rem] md:rounded-[3rem] object-cover aspect-square md:aspect-[4/3] border border-white/50 shadow-[0_20px_50px_rgba(0,0,0,0.1)]"
            />
          </div>
        </div>
      </section>

      <section className="py-16 md:py-32 bg-black text-white relative overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img 
            src="/images/students_editorial.png" 
            alt="Students Collaborating"
            className="w-full h-full object-cover opacity-20 select-none grayscale"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black via-black/90 to-transparent"></div>
        </div>

        <div className="max-w-5xl mx-auto px-5 relative z-10 text-center">
          <h2 className="font-serif text-3xl sm:text-4xl md:text-6xl mb-6 md:mb-8 font-medium">No agency fees. No gatekeepers.</h2>
          <p className="text-lg md:text-xl lg:text-2xl text-gray-400 font-light max-w-3xl mx-auto leading-relaxed">
            International students lose thousands of dollars to recruitment agencies that hide the best options and push commissions. Skolr scrapes university and scholarship data daily from primary sources and serves it directly to your AI. Every link goes to the official page. Every result is unfiltered. Free forever.
          </p>
        </div>
      </section>

      <section id="features" className="py-16 md:py-32 px-5">
        <div className="max-w-7xl mx-auto">
          <div className="mb-12 md:mb-20">
             <h2 className="font-serif text-3xl sm:text-4xl md:text-5xl font-medium mb-3 md:mb-4 text-gray-900">What your AI gets access to</h2>
             <p className="text-gray-500 text-lg md:text-xl font-light">Four tools. Real data. Updated every 24 hours from primary university sources.</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-5 md:gap-8">
            <div className="md:col-span-2 bg-white p-6 md:p-12 rounded-3xl md:rounded-[2.5rem] border border-gray-100 shadow-sm relative overflow-hidden group">
              <div className="absolute -right-20 -top-20 w-64 h-64 bg-blue-50 rounded-full blur-3xl group-hover:bg-blue-100 transition-colors"></div>
              <div className="relative z-10">
                <Search className="w-7 h-7 md:w-8 md:h-8 text-blue-600 mb-5 md:mb-8" />
                <h3 className="text-2xl md:text-3xl font-serif font-medium mb-3 md:mb-4">Course Search</h3>
                <p className="text-gray-500 text-base md:text-lg max-w-md font-light leading-relaxed">Search across 5,000+ programs from universities in the US, UK, Canada, Australia, and beyond. Get tuition fees, deadlines, entry requirements, and direct application links. Data refreshed daily from official university pages.</p>
              </div>
            </div>
            
            <div className="bg-gray-900 text-white p-6 md:p-12 rounded-3xl md:rounded-[2.5rem] shadow-xl relative overflow-hidden group">
              <div className="absolute inset-0 opacity-20 transition-opacity group-hover:opacity-40" style={{ backgroundImage: `url('/images/data_texture.png')`, backgroundSize: 'cover' }}></div>
              <div className="relative z-10 h-full flex flex-col">
                <Zap className="w-7 h-7 md:w-8 md:h-8 text-blue-400 mb-5 md:mb-8" />
                <h3 className="text-2xl md:text-3xl font-serif font-medium mb-3 md:mb-4">Scholarship Finder</h3>
                <p className="text-gray-300 text-base md:text-lg font-light leading-relaxed mb-auto">Surface scholarships that never show up on Google. Government grants, university-specific funding, and regional awards matched to your profile, nationality, and field of study.</p>
              </div>
            </div>

            <div className="bg-white p-6 md:p-10 rounded-3xl md:rounded-[2.5rem] border border-gray-100 shadow-sm hover:border-gray-200 transition-colors">
              <FileText className="w-6 h-6 md:w-7 md:h-7 text-gray-900 mb-5 md:mb-6" />
              <h3 className="text-xl md:text-2xl font-serif font-medium mb-2 md:mb-3">Visa Intelligence</h3>
              <p className="text-gray-500 text-sm md:text-base font-light leading-relaxed">Student visa requirements, post-study work rights, and processing timelines pulled from official immigration sources. No agency spin.</p>
            </div>

            <div className="md:col-span-2 bg-gradient-to-br from-[#f0f4ff] to-white p-6 md:p-10 rounded-3xl md:rounded-[2.5rem] border border-blue-50 flex flex-col justify-center">
              <Network className="w-6 h-6 md:w-7 md:h-7 text-blue-600 mb-5 md:mb-6" />
              <h3 className="text-xl md:text-2xl font-serif font-medium mb-2 md:mb-3 text-gray-900">Works with any AI</h3>
              <p className="text-gray-500 text-sm md:text-base font-light max-w-xl leading-relaxed">Built on the open Model Context Protocol. Connects natively to Claude, ChatGPT, Gemini, Cursor, and any MCP-compatible tool. No API keys. No authentication. Just paste the URL and go.</p>
            </div>
          </div>
        </div>
      </section>

      <section id="connect" className="py-16 md:py-32 px-5 bg-white border-y border-gray-100">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-12 md:mb-24">
            <h2 className="font-serif text-3xl sm:text-4xl md:text-6xl font-medium text-gray-900 mb-4 md:mb-6">
              Connect in seconds.
            </h2>
            <p className="text-base md:text-xl text-gray-500 font-light">
              No API keys required. Skolr is completely open and free.<br className="hidden sm:block" /> Use our direct proxy URL: <strong className="text-gray-900 font-mono bg-gray-50 px-2 py-1 rounded-md text-sm md:text-base border border-gray-200 break-all">https://skolr.xyz/mcp</strong>
            </p>
          </div>
          
          <div className="space-y-10 md:space-y-16">
            <div className="flex flex-col md:flex-row gap-5 md:gap-10 items-start">
              <div className="flex-shrink-0 text-5xl md:text-7xl font-sans font-black text-gray-100 uppercase">01</div>
              <div className="w-full">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 md:gap-4 mb-4 md:mb-6">
                  <h3 className="text-2xl md:text-3xl font-serif font-medium">Claude Web</h3>
                  <a href="https://claude.ai/settings/connectors" target="_blank" rel="noreferrer" className="inline-flex items-center justify-center relative shadow-[0_4px_14px_0_rgba(0,0,0,0.1)] hover:shadow-[0_6px_20px_rgba(0,0,0,0.15)] bg-white border border-gray-200 text-gray-900 px-5 py-2 rounded-full font-medium text-sm transition-all hover:bg-gray-50 hover:-translate-y-0.5 active:translate-y-0 whitespace-nowrap">
                    Open Claude Connectors <ArrowRight className="w-4 h-4 ml-2"/>
                  </a>
                </div>
                <div className="bg-[#fafafa] p-5 md:p-8 rounded-2xl md:rounded-3xl border border-gray-100 shadow-inner">
                  <p className="text-gray-500 text-base md:text-lg mb-5 md:mb-6 leading-relaxed">Connect Skolr to Claude in your browser. Once connected, just ask Claude about any program, scholarship, or visa and it will pull live data for you.</p>
                  <ol className="list-none space-y-3 md:space-y-4 text-gray-900 font-medium">
                    <li className="flex gap-3 items-start bg-white p-3 md:p-4 rounded-xl md:rounded-2xl border border-gray-200 shadow-sm text-sm md:text-base"><span className="w-6 h-6 rounded-full bg-black text-white font-bold flex items-center justify-center text-xs shrink-0 mt-0.5">1</span> Click 'Open Claude Connectors' above.</li>
                    <li className="flex gap-3 items-start bg-white p-3 md:p-4 rounded-xl md:rounded-2xl border border-gray-200 shadow-sm text-sm md:text-base"><span className="w-6 h-6 rounded-full bg-black text-white font-bold flex items-center justify-center text-xs shrink-0 mt-0.5">2</span> Click into <strong>Custom Connectors</strong>.</li>
                    <li className="flex gap-3 items-start bg-white p-3 md:p-4 rounded-xl md:rounded-2xl border border-gray-200 shadow-sm text-sm md:text-base"><span className="w-6 h-6 rounded-full bg-black text-white font-bold flex items-center justify-center text-xs shrink-0 mt-0.5">3</span> <span>Add a name and paste <code className="bg-gray-100 px-1.5 py-0.5 rounded text-black font-mono text-xs border border-gray-200 break-all">https://skolr.xyz/mcp</code> — done.</span></li>
                  </ol>
                </div>
              </div>
            </div>

            <div className="flex flex-col md:flex-row gap-5 md:gap-10 items-start">
              <div className="flex-shrink-0 text-5xl md:text-7xl font-sans font-black text-gray-100 uppercase">02</div>
              <div className="w-full">
                <h3 className="text-2xl md:text-3xl font-serif font-medium mb-4 md:mb-6">ChatGPT &amp; Gemini</h3>
                <div className="bg-[#fafafa] p-5 md:p-8 rounded-2xl md:rounded-3xl border border-gray-200 shadow-sm">
                  <p className="text-gray-500 text-base md:text-lg mb-5 md:mb-6 leading-relaxed">Building a Custom GPT or a Gemini tool? Point it at our endpoint and your agent can answer any question about studying abroad with real, sourced data.</p>
                  <div className="bg-white p-4 md:p-6 rounded-xl md:rounded-2xl border border-gray-200 shadow-sm">
                    <p className="text-gray-900 mb-3 md:mb-4 font-medium text-sm md:text-base">How to connect:</p>
                    <ol className="list-none space-y-3 md:space-y-4 text-gray-600">
                      <li className="flex gap-3 items-start text-sm md:text-base">
                        <span className="w-2 h-2 rounded-full bg-blue-600 shrink-0 mt-2"></span>
                        <span><strong>OpenAI Custom Actions:</strong> Use our endpoint <code className="bg-gray-100 px-1.5 py-0.5 rounded border border-gray-200 font-mono text-black text-xs break-all">https://skolr.xyz/mcp</code> as your server URL. No auth required.</span>
                      </li>
                      <li className="flex gap-3 items-start text-sm md:text-base">
                        <span className="w-2 h-2 rounded-full bg-blue-600 shrink-0 mt-2"></span>
                        <span><strong>Gemini / Vertex:</strong> Provide the same direct URL into your tool function calling definitions.</span>
                      </li>
                    </ol>
                  </div>
                </div>
              </div>
            </div>

            <div className="flex flex-col md:flex-row gap-5 md:gap-10 items-start">
              <div className="flex-shrink-0 text-5xl md:text-7xl font-sans font-black text-gray-100 uppercase">03</div>
              <div className="w-full">
                <h3 className="text-2xl md:text-3xl font-serif font-medium mb-4 md:mb-6">Coding Agents (Cursor)</h3>
                <div className="bg-[#fafafa] p-5 md:p-8 rounded-2xl md:rounded-3xl border border-gray-200 shadow-sm">
                  <p className="text-gray-500 text-base md:text-lg mb-5 md:mb-6 leading-relaxed">Building an EdTech product? Give Cursor's agent live access to global education data while you code. Search programs, match scholarships, and pull visa info right from your editor.</p>
                  <div className="bg-white p-4 md:p-6 rounded-xl md:rounded-2xl border border-gray-200 shadow-sm">
                    <p className="text-gray-900 mb-3 font-medium flex items-center gap-2 text-sm md:text-base"><Box className="w-4 h-4 shrink-0"/> Navigate to Settings {'>'} Features {'>'} MCP</p>
                    <p className="text-gray-600 text-sm md:text-base">Add a new MCP server: <code className="bg-gray-100 px-1.5 py-0.5 rounded border border-gray-200 font-mono text-black text-xs break-all">https://skolr.xyz/mcp</code></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="pricing" className="py-16 md:py-24 bg-gradient-to-b from-white to-blue-50/30 text-center px-5">
        <h2 className="font-serif text-3xl sm:text-4xl md:text-5xl font-medium text-gray-900 mb-4 md:mb-6">
          Free. No catch.
        </h2>
        <p className="text-lg md:text-xl text-gray-500 font-light max-w-xl mx-auto leading-relaxed mb-8 md:mb-10">
          Skolr exists because students deserve direct access to opportunity without paying someone to Google for them. No rate limits. No subscriptions.
        </p>
        <a href="#connect" className="inline-flex items-center justify-center relative shadow-[0_4px_20px_0_rgba(37,99,235,0.3)] hover:shadow-[0_6px_30px_rgba(37,99,235,0.5)] bg-blue-600 border border-blue-500 text-white px-8 md:px-10 py-3.5 md:py-4 rounded-full font-semibold text-base md:text-lg transition-all hover:bg-blue-700 hover:-translate-y-1 active:translate-y-0 ring-1 ring-inset ring-white/20">
          Start using Skolr Now
        </a>
        
        <div className="mt-12 md:mt-16 pt-8 md:pt-10 border-t border-gray-200/60 max-w-lg mx-auto">
          <p className="text-gray-500 font-light mb-2">Building something bigger? Let's talk.</p>
          <a href="mailto:contact@skolr.xyz" className="font-medium text-gray-900 border-b border-gray-900 pb-0.5 hover:text-blue-600 hover:border-blue-600 transition-colors">
            contact@skolr.xyz
          </a>
        </div>
      </section>
    </>
  );
}
