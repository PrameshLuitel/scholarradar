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
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="w-full bg-black text-white py-2 px-6 text-center text-[10px] md:text-xs font-medium tracking-tight relative z-[60]"
        >
          <span className="opacity-70 uppercase mr-2 tracking-widest border border-white/20 px-1.5 py-0.5 rounded text-[9px]">Important Notice</span>
          Skolr is an AI data proxy, not a migration agent or legal advisor. Always verify critical data on official university or government websites.
        </motion.div>
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
