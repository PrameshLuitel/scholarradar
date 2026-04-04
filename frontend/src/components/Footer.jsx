import React from 'react';
import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <footer className="bg-white py-12 md:py-16 px-5 border-t border-gray-100">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-baseline justify-between gap-10">
        <div>
          <Link to="/" className="flex items-center font-bold text-2xl tracking-tighter mb-3 md:mb-4">
            Skolr<span className="text-blue-600 -ml-0.5">.</span>
          </Link>
          <p className="text-gray-400 font-light text-sm max-w-xs leading-relaxed">
            Live university, scholarship, and visa data for AI agents. Scraped daily from official sources. Free and open.
          </p>
        </div>
        
        <div className="flex flex-wrap gap-8 md:gap-20">
          <div className="flex flex-col gap-3">
            <span className="font-medium text-xs tracking-widest uppercase text-gray-300 mb-2">Connect</span>
            <a href="mailto:contact@skolr.xyz" className="text-gray-500 hover:text-black font-light transition-colors text-sm">Contact</a>
            <a href="mailto:support@skolr.xyz" className="text-gray-500 hover:text-black font-light transition-colors text-sm">Get Support</a>
            <a href="mailto:investors@skolr.xyz" className="text-gray-500 hover:text-black font-light transition-colors text-sm">Investors</a>
          </div>
          <div className="flex flex-col gap-3">
            <span className="font-medium text-xs tracking-widest uppercase text-gray-300 mb-2">Platform</span>
            <a href="/#features" className="text-gray-500 hover:text-black font-light transition-colors text-sm">Documentation</a>
            <a href="/#connect" className="text-gray-500 hover:text-black font-light transition-colors text-sm">Status</a>
            <a href="/#features" className="text-gray-500 hover:text-black font-light transition-colors text-sm">API Reference</a>
          </div>
          <div className="flex flex-col gap-3">
            <span className="font-medium text-xs tracking-widest uppercase text-gray-300 mb-2">Legal</span>
            <Link to="/privacypolicy" className="text-gray-500 hover:text-black font-light transition-colors text-sm">Privacy Policy</Link>
            <Link to="/terms" className="text-gray-500 hover:text-black font-light transition-colors text-sm">Terms of Use</Link>
            <Link to="/compliance" className="text-gray-500 hover:text-black font-light transition-colors text-sm">Data &amp; Compliance</Link>
            <Link to="/ip-infringement" className="text-gray-500 hover:text-black font-light transition-colors text-sm">IP Infringement</Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
