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
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">2. Disclaimer of Warranties ("As-Is")</h2>
          <p>The data provided through Skolr is live-scraped from public universities, government endpoints, and third-party databases. While we refresh this data aggressively (every 24 hours), we make <strong>no warranties, expressed or implied</strong>, about the accuracy, reliability, or availability of the information.</p>
          <p className="mt-4">Skolr is a routing layer, not a registered educational agency or legal immigration advisor. Users and their respective AI agents are solely responsible for independently verifying all visas, deadlines, and tuition costs presented by the tool.</p>
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
          <p>In no event shall Skolr or its developers be liable for any direct, indirect, incidental, consequential, or punitive damages arising out of your access to or use of the Service, including but not limited to missed application deadlines, rejected visas, or inaccurate financial estimates.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">5. Contact Information</h2>
          <p>For generalized support, please contact <a href="mailto:support@skolr.xyz" className="text-blue-600 hover:underline">support@skolr.xyz</a>. For any formal legal inquiries regarding these terms, contact <a href="mailto:legal@skolr.xyz" className="text-blue-600 hover:underline">legal@skolr.xyz</a>.</p>
        </div>
      </div>
    </LegalLayout>
  );
}
