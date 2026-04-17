import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { motion } from 'framer-motion';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import FindUni from './pages/FindUni';
import PrivacyPolicy from './pages/PrivacyPolicy';
import TermsOfUse from './pages/TermsOfUse';
import Compliance from './pages/Compliance';
import IpInfringement from './pages/IpInfringement';

export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-[#fafafa] text-gray-900 font-sans selection:bg-blue-200">
        <Header />
        
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/finduni" element={<FindUni />} />
          <Route path="/privacypolicy" element={<PrivacyPolicy />} />
          <Route path="/terms" element={<TermsOfUse />} />
          <Route path="/compliance" element={<Compliance />} />
          <Route path="/ip-infringement" element={<IpInfringement />} />
        </Routes>
        
        <Footer />
      </div>
    </BrowserRouter>
  );
}
