import React from 'react';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header className="absolute top-0 w-full z-50 bg-transparent">
      <div className="max-w-7xl mx-auto px-6 h-24 flex items-center justify-between">
        <Link to="/" className="flex items-center font-bold text-2xl tracking-tighter">
          Skolr<span className="text-blue-600 -ml-0.5 tracking-tighter">.</span>
        </Link>
        <nav className="hidden md:flex gap-10 text-sm font-medium tracking-wide text-gray-600">
          <a href="/#features" className="hover:text-black transition-colors">Platform</a>
          <a href="/dashboard" className="hover:text-black transition-colors flex items-center gap-1.5 group">
            Dashboard
            <span className="flex h-1.5 w-1.5 rounded-full bg-emerald-500 animate-pulse ring-2 ring-emerald-500/20"></span>
          </a>
          <a href="/#connect" className="hover:text-black transition-colors">Connect</a>

          <a href="/#pricing" className="hover:text-black transition-colors text-blue-600 relative">
            Pricing
            <span className="absolute -top-3 -right-6 text-[10px] bg-blue-100 text-blue-700 font-bold px-1.5 py-0.5 rounded-full">FREE</span>
          </a>
        </nav>
        <div className="flex items-center gap-6">
          <a href="/#connect" className="relative group overflow-hidden px-6 py-2.5 text-sm font-semibold text-white bg-black/90 backdrop-blur-md rounded-full shadow-[0_4px_14px_0_rgba(0,0,0,0.39)] hover:shadow-[0_6px_20px_rgba(0,0,0,0.23)] hover:bg-black transition-all hover:-translate-y-[1px] active:translate-y-0 active:scale-95 border border-white/10 ring-1 ring-inset ring-white/20">
            <span className="relative z-10">Add to AI</span>
            <div className="absolute inset-0 h-full w-full bg-gradient-to-tr from-transparent via-white/10 to-transparent -translate-x-[100%] group-hover:animate-[shimmer_1.5s_infinite]"></div>
          </a>
        </div>
      </div>
    </header>
  );
}
