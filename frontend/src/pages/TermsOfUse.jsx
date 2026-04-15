import React from 'react';
import LegalLayout from '../components/LegalLayout';

export default function TermsOfUse() {
  return (
    <LegalLayout title="Terms of Use" lastUpdated="April 4, 2026">
      <div className="space-y-8 text-gray-600 font-light leading-relaxed">
        <p>By accessing or using the Skolr API or Model Context Protocol endpoint, you agree to be bound by these Terms of Use. If you disagree with any part of these terms, you may not access the service.</p>
        
        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">1. Service Description</h2>
          <p>Skolr provides an unbiased data layer ("the Service") acting as a proxy to publicly available educational information, scholarships, and visa guidelines. The Service is provided 100% free of charge and does not require API keys or registration.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">2. No Professional Advice & Disclaimer of Warranties</h2>
          <p>Skolr is a data aggregation tool powered by Artificial Intelligence. <strong>We are NOT registered migration agents, legal advisors, certified financial planners, or authorized educational consultants.</strong></p>
          <ul className="list-disc pl-6 space-y-2 mt-4">
            <li><strong>AI-Generated Content:</strong> Information is served by AI models which may occasionally hallucinate or provide outdated data.</li>
            <li><strong>"As-Is" Basis:</strong> We provide data exactly as found on public sources, with no warranty of accuracy, completeness, or timeliness.</li>
            <li><strong>Mandatory Verification:</strong> You must independently verify all admissions requirements, tuition fees, and visa regulations on official university or government portals.</li>
          </ul>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">3. Acceptable Use</h2>
          <p>You agree to use Skolr only for lawful purposes. You agree not to:</p>
          <ul className="list-disc pl-6 space-y-2 mt-4">
            <li>Engage in abusive volumetric querying designed to overwhelm our infrastructure.</li>
            <li>Use the data to perpetrate fraud or deceive international students.</li>
            <li>Resell access to the raw proxy endpoints.</li>
          </ul>
          <p className="mt-4">We reserve the right to temporarily or permanently block IP addresses demonstrating abusive, malicious, or irresponsibly un-throttled behavior.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">4. Limitation of Liability</h2>
          <p><strong>To the maximum extent permitted by law, Skolr and its developers shall NOT be held liable</strong> for any direct, indirect, incidental, or consequential damages resulting from your use of this tool. This includes, but is not limited to: missed application deadlines, rejected visa applications, incorrect financial planning based on our estimates, or any other academic or legal setbacks.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">5. Contact Information</h2>
          <p>For generalized support, please contact <a href="mailto:support@skolr.xyz" className="text-blue-600 hover:underline">support@skolr.xyz</a>. For any formal legal inquiries regarding these terms, contact <a href="mailto:legal@skolr.xyz" className="text-blue-600 hover:underline">legal@skolr.xyz</a>.</p>
        </div>
      </div>
    </LegalLayout>
  );
}
