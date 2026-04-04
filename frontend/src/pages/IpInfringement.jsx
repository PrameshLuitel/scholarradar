import React from 'react';
import LegalLayout from '../components/LegalLayout';

export default function IpInfringement() {
  return (
    <LegalLayout title="IP Infringement Policy" lastUpdated="April 4, 2026">
      <div className="space-y-8 text-gray-600 font-light leading-relaxed">
        <p>Skolr respects the intellectual property rights of universities, governments, and educational content creators. Our platform strictly aggregates publicly accessible academic meta-data (e.g., tuition costs, program deadlines) designed for public distribution.</p>
        
        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">1. Copyright and Fair Use</h2>
          <p>The indexing of factual, numerical data (such as university tuition rates, location metadata, and application deadlines) generally falls under "Fair Use" principles or constitutes non-copyrightable facts. However, we do not index or reproduce proprietary university curricula, textbooks, licensed research papers, or gated media files.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">2. Takedown Requests (DMCA)</h2>
          <p>If you represent a university or educational institution and believe in good faith that your specific, copyrighted intellectual property has been improperly scraped into our database beyond factual limits, we will immediately honor valid takedown requests.</p>
          <p className="mt-4">Please submit a formal request identifying the specific institutional endpoint and the copyrighted material in question directly to <a href="mailto:legal@skolr.xyz" className="text-blue-600 hover:underline">legal@skolr.xyz</a>. We will process these requests immediately to ensure the fastest excision of any improperly indexed underlying data.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">3. Automated Opt-Out</h2>
          <p>If you simply wish for your institution's public endpoints to be ignored by our 24-hour update cycles, appending a standard `Disallow: /` block in your server's `robots.txt` for common web crawlers will automatically cascade up to our aggregator architecture during the next scrape.</p>
        </div>
      </div>
    </LegalLayout>
  );
}
