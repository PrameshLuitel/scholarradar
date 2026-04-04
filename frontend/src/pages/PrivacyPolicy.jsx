import React from 'react';
import LegalLayout from '../components/LegalLayout';

export default function PrivacyPolicy() {
  return (
    <LegalLayout title="Privacy Policy" lastUpdated="April 4, 2026">
      <div className="space-y-8 text-gray-600 font-light leading-relaxed">
        <p>Skolr ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how we handle data when you use the Skolr Model Context Protocol (MCP) server.</p>
        
        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">1. Scope of Data Collection</h2>
          <p>Skolr is designed as a data proxy layer. We do not require account creation, and we do not profile your personal identity. However, to maintain and optimize the system, we do collect specific operational telemetry:</p>
          <ul className="list-disc pl-6 space-y-2 mt-4">
            <li><strong>Tool Call Telemetry:</strong> We log the specific parameters and arguments that your AI agent sends to our endpoints (e.g., searching for "Computer Science in Canada" or "Visa deadlines for Australia").</li>
            <li><strong>Rate Limiting & Abuse:</strong> We may temporarily log request origins to prevent DDoS attacks or abusive volumetric querying.</li>
          </ul>
          <p className="mt-4"><strong>What we do NOT collect:</strong> We do not have access to the conversational context, raw user interface prompts, or sensitive personal data that you share privately with your AI assistant (such as Claude or Cursor) prior to it executing a tool call.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">2. Global Analytics</h2>
          <p>The tool call data we collect is aggregated into secured, internal operational dashboards. This helps our administrative team understand macroeconomic trends—such as the most popular study destinations or broken program links—so that we can manually fix gaps in the data layer. We do not sell this telemetry to external marketing agencies.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">3. Third-Party Agents</h2>
          <p>Please note that when you use Skolr through third-party platforms (like Anthropic's Claude or OpenAI's ChatGPT), your data is subject to the respective privacy policies of those operators. Skolr is only responsible for the data while it is in transit through our endpoint proxy.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">4. Changes to This Policy</h2>
          <p>We may update this Privacy Policy from time to time to reflect changes in our protocol proxy infrastructure. We will indicate at the top of the policy when it was most recently updated.</p>
        </div>

        <div>
          <h2 className="text-gray-900 font-medium text-2xl mb-4 font-serif">5. Contact Us</h2>
          <p>If you have any questions about this Privacy Policy, your rights, or how we handle telemetry data, please contact our legal team at <a href="mailto:legal@skolr.xyz" className="text-blue-600 hover:underline">legal@skolr.xyz</a>.</p>
        </div>
      </div>
    </LegalLayout>
  );
}
