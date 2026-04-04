import React from 'react';

export default function LegalLayout({ title, lastUpdated, children }) {
  return (
    <div className="pt-40 pb-24 px-6 min-h-screen bg-[#fafafa]">
      <div className="max-w-4xl mx-auto">
        <h1 className="font-serif text-5xl md:text-6xl font-medium text-gray-900 mb-6">{title}</h1>
        {lastUpdated && <p className="text-gray-400 text-sm mb-12 font-mono">Last Updated: {lastUpdated}</p>}
        <div className="bg-white p-8 md:p-16 rounded-[2.5rem] border border-gray-100 shadow-sm">
          {children}
        </div>
      </div>
    </div>
  );
}
