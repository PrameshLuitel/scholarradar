import React from 'react';
import LegalLayout from '../components/LegalLayout';

export default function Compliance() {
  return (
    <LegalLayout title="Data & Compliance" lastUpdated="April 4, 2026">
      <div className="space-y-8 text-gray-600 font-light leading-relaxed">
        <p>Skolr adheres to global data privacy and scraping compliance standards. This declaration explicitly outlines our alignment with the General Data Protection Regulation (GDPR), the California Consumer Privacy Act (CCPA), and general web scraping ethics.</p>
        
        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">1. GDPR & CCPA Statement</h2>
          <p>As a non-tracking, stateless protocol proxy, Skolr does not request, log, or maintain records of end-user Personally Identifiable Information (PII). Because we do not persistently store data linking directly to data subjects, we operate outside the scope of many primary GDPR and CCPA enforcement vectors concerning user profiling.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">2. Ethical Scraping Doctrine</h2>
          <p>The core of Skolr is our 24-hour live-update scraping jobs. To remain compliant and entirely respectful of higher-education and government systems, our engines abide by the following technical strictures:</p>
          <ul className="list-disc pl-6 space-y-2 mt-4">
            <li><strong>Robots.txt Adherence:</strong> Our scrapers fundamentally respect paths disallowed by standard `robots.txt` architectures.</li>
            <li><strong>Rate Limiting:</strong> We strictly limit concurrent requests to ensure we impart zero strain on university infrastructure.</li>
            <li><strong>Public Data Only:</strong> We exclusively index non-gated, unauthenticated public web pages (e.g., standard tuition tables, public scholarship PDFs). We do not attempt to bypass paywalls or scrape internal student portals.</li>
          </ul>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">3. Scope of Hosted Data</h2>
          <p>Any data temporarily cached or saved locally within the Skolr infrastructure is purely related to institutional metadata (e.g., University Names, Program Deadlines, Global Cost of Living aggregates). We expressly forbid our platform from persisting, caching, or distributing individual student data.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">4. Compliance Inquiries</h2>
          <p>For any formal declarations or inquiries regarding GDPR Data Subject Access Requests (DSARs), CCPA compliance, or Data Protection Officer (DPO) communications, please contact <a href="mailto:legal@skolr.xyz" className="text-blue-600 hover:underline">legal@skolr.xyz</a>.</p>
        </div>
      </div>
    </LegalLayout>
  );
}
