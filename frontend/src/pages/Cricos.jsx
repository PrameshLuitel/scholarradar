import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, Sparkles, Filter, ChevronLeft, ChevronRight, GraduationCap, MapPin, DollarSign, Clock, Building2, Globe2 } from 'lucide-react';

export default function Cricos() {
  const [data, setData] = useState([]);
  const [totalCount, setTotalCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [aiFiltersApplied, setAiFiltersApplied] = useState(null);
  
  // Filter States
  const [query, setQuery] = useState('');
  const [searchInput, setSearchInput] = useState('');
  const [selectedState, setSelectedState] = useState('All');
  const [selectedLevel, setSelectedLevel] = useState('All');
  
  // Pagination
  const [page, setPage] = useState(1);
  const pageSize = 50;

  const states = ['All', 'NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT'];
  const levels = ['All', 'Undergraduate', 'Postgraduate', 'Vocational', 'Doctorate'];

  const fetchCricosData = async (currentPage, searchQuery) => {
    setLoading(true);
    setAiFiltersApplied(null);
    try {
      const response = await fetch('/api/cricos/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: searchQuery,
          state: selectedState === 'All' ? null : selectedState,
          level: selectedLevel === 'All' ? null : selectedLevel,
          page: currentPage,
          page_size: pageSize
        })
      });
      
      const result = await response.json();
      if (result.data) {
        setData(result.data);
        setTotalCount(result.total_count);
        // If query was non-empty, we highlight what the AI extracted
        if (searchQuery && Object.keys(result.ai_filters_applied || {}).length > 0) {
          setAiFiltersApplied(result.ai_filters_applied);
        }
      } else {
        setData([]);
      }
    } catch (error) {
      console.error("Failed to fetch CRICOS data", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCricosData(page, query);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [page, selectedState, selectedLevel, query]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    setPage(1);
    setQuery(searchInput);
  };

  const totalPages = Math.ceil(totalCount / pageSize);

  return (
    <div className="min-h-screen bg-[#fafafa] pt-24 pb-16 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto space-y-8">
        
        {/* Header Section */}
        <div className="text-center max-w-3xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-blue-50 text-blue-700 font-medium text-sm mb-6"
          >
            <Globe2 className="w-4 h-4" />
            Official CRICOS Register
          </motion.div>
          <motion.h1 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight mb-4"
          >
            Discover Your Future in <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">Australia</span>
          </motion.h1>
          <motion.p 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.1 }}
            className="text-lg text-gray-600"
          >
            Search through thousands of officially registered courses for international students. Use our AI to filter precisely.
          </motion.p>
        </div>

        {/* Search & Filters Card */}
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="bg-white rounded-3xl shadow-xl shadow-gray-200/50 border border-gray-100 overflow-hidden"
        >
          <div className="p-2">
            {/* AI Search Bar */}
            <form onSubmit={handleSearchSubmit} className="relative flex items-center">
              <div className="absolute left-4 sm:left-6 flex items-center justify-center pointer-events-none text-blue-500">
                <Sparkles className="w-6 h-6 animate-pulse" />
              </div>
              <input
                type="text"
                value={searchInput}
                onChange={(e) => setSearchInput(e.target.value)}
                placeholder="Type to filter with AI... e.g. 'MBA programs in Sydney under $40k'"
                className="w-full pl-14 sm:pl-16 pr-4 sm:pr-32 py-5 sm:py-6 text-gray-900 text-lg rounded-2xl border-none focus:ring-0 focus:outline-none placeholder:text-gray-400 bg-transparent transition-all"
              />
              <div className="absolute right-2 sm:right-3 flex items-center">
                <button 
                  type="submit"
                  className="bg-gray-900 hover:bg-gray-800 text-white p-3 sm:px-6 sm:py-3 rounded-xl sm:rounded-2xl font-medium transition-all shadow-md active:scale-95 flex items-center gap-2"
                >
                  <span className="hidden sm:inline">Search</span>
                  <Search className="w-5 h-5" />
                </button>
              </div>
            </form>
          </div>
          
          {/* Traditional Filters */}
          <div className="bg-gray-50/80 px-6 py-4 border-t border-gray-100 flex flex-wrap gap-4 items-center justify-between">
            <div className="flex flex-wrap gap-4 items-center">
              <div className="flex items-center gap-2 text-sm">
                <Filter className="w-4 h-4 text-gray-500" />
                <span className="text-gray-700 font-medium whitespace-nowrap">Filters:</span>
              </div>
              
              <select
                value={selectedState}
                onChange={(e) => { setSelectedState(e.target.value); setPage(1); }}
                className="bg-white border border-gray-200 text-gray-700 rounded-lg px-4 py-2 text-sm focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 cursor-pointer shadow-sm appearance-none min-w-[120px]"
                style={{ backgroundImage: "url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%239CA3AF%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')", backgroundRepeat: 'no-repeat', backgroundPosition: 'right 1rem top 50%', backgroundSize: '0.65em auto' }}
              >
                {states.map(s => <option key={s} value={s}>{s === 'All' ? 'All States' : s}</option>)}
              </select>

              <select
                value={selectedLevel}
                onChange={(e) => { setSelectedLevel(e.target.value); setPage(1); }}
                className="bg-white border border-gray-200 text-gray-700 rounded-lg px-4 py-2 text-sm focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 cursor-pointer shadow-sm appearance-none min-w-[150px]"
                style={{ backgroundImage: "url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%239CA3AF%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')", backgroundRepeat: 'no-repeat', backgroundPosition: 'right 1rem top 50%', backgroundSize: '0.65em auto' }}
              >
                {levels.map(l => <option key={l} value={l}>{l === 'All' ? 'All Study Levels' : l}</option>)}
              </select>
            </div>
            
            {aiFiltersApplied && (
              <div className="flex items-center gap-2 text-sm text-blue-600 bg-blue-50 px-3 py-1.5 rounded-full mt-4 sm:mt-0 shadow-sm border border-blue-100">
                <Sparkles className="w-3.5 h-3.5" />
                AI applied: {Object.keys(aiFiltersApplied).join(', ')}
              </div>
            )}
          </div>
        </motion.div>

        {/* Database Table */}
        <div className="bg-white rounded-3xl shadow-lg border border-gray-100 overflow-hidden relative min-h-[500px]">
          {loading && (
            <div className="absolute inset-0 z-10 bg-white/70 backdrop-blur-sm flex items-center justify-center">
              <div className="flex flex-col items-center">
                <div className="w-12 h-12 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>
                <p className="mt-4 text-blue-900 font-medium">Fetching database records...</p>
              </div>
            </div>
          )}
          
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-gray-50 border-b border-gray-200 text-gray-500 text-xs uppercase tracking-wider font-semibold">
                  <th className="px-6 py-4 w-1/3">Course Name</th>
                  <th className="px-6 py-4">University / Provider</th>
                  <th className="px-6 py-4">Location</th>
                  <th className="px-6 py-4">Level</th>
                  <th className="px-6 py-4 text-right">Tuition Fee</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-100 text-gray-700">
                <AnimatePresence mode="popLayout">
                  {!loading && data.length === 0 ? (
                    <motion.tr 
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                    >
                      <td colSpan="5" className="px-6 py-24 text-center text-gray-500">
                        <Search className="w-12 h-12 text-gray-300 mx-auto mb-4" />
                        <p className="text-lg font-medium text-gray-900">No courses found</p>
                        <p>Try adjusting your search query or filters.</p>
                      </td>
                    </motion.tr>
                  ) : (
                    data.map((course, idx) => (
                      <motion.tr 
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: Math.min(idx * 0.03, 0.5) }}
                        key={`${course.cricos_code || idx}-${course.id}`}
                        className="hover:bg-blue-50/50 transition-colors group"
                      >
                        <td className="px-6 py-4">
                          <div className="font-semibold text-gray-900 group-hover:text-blue-700 transition-colors line-clamp-2">
                            {course.name}
                          </div>
                          <div className="text-xs text-gray-500 mt-1 flex items-center gap-1.5 opacity-80 group-hover:opacity-100">
                            CRICOS: <code className="bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">{course.cricos_code || 'N/A'}</code>
                            {course.duration_months && (
                              <span className="flex items-center gap-1 ml-2"><Clock className="w-3 h-3"/> {course.duration_months} mo</span>
                            )}
                          </div>
                        </td>
                        <td className="px-6 py-4">
                          <div className="flex items-center gap-2">
                            <Building2 className="w-4 h-4 text-gray-400 shrink-0" />
                            <span className="font-medium text-gray-800 line-clamp-1">{course.university}</span>
                          </div>
                          <div className="text-xs text-gray-500 mt-1">Provider: {course.provider_code || 'N/A'}</div>
                        </td>
                        <td className="px-6 py-4">
                          <div className="flex items-center gap-1.5 text-sm">
                            <MapPin className="w-4 h-4 text-rose-400 shrink-0" />
                            {course.city && course.state ? `${course.city}, ${course.state}` : (course.state || course.city || "Australia")}
                          </div>
                        </td>
                        <td className="px-6 py-4">
                          <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-100 text-gray-700 text-xs font-medium border border-gray-200">
                            <GraduationCap className="w-3.5 h-3.5" />
                            {course.level || 'Unknown'}
                          </span>
                        </td>
                        <td className="px-6 py-4 text-right">
                          {course.tuition_fee ? (
                            <div className="flex flex-col items-end">
                              <span className="font-semibold text-gray-900 flex items-center gap-1">
                                {course.currency || 'AUD'} <DollarSign className="w-3 h-3 text-emerald-500 -mr-1" />
                                {course.tuition_fee.toLocaleString()}
                              </span>
                              <span className="text-xs text-gray-500">per year</span>
                            </div>
                          ) : (
                            <span className="text-gray-400 text-sm italic">N/A</span>
                          )}
                        </td>
                      </motion.tr>
                    ))
                  )}
                </AnimatePresence>
              </tbody>
            </table>
          </div>

          {/* Pagination Footer */}
          {!loading && data.length > 0 && (
            <div className="bg-gray-50 px-6 py-4 border-t border-gray-200 flex items-center justify-between">
              <div className="text-sm text-gray-600">
                Showing <span className="font-medium text-gray-900">{((page - 1) * pageSize) + 1}</span> to <span className="font-medium text-gray-900">{Math.min(page * pageSize, totalCount)}</span> of <span className="font-medium text-gray-900">{totalCount.toLocaleString()}</span> entries
              </div>
              
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setPage(p => Math.max(1, p - 1))}
                  disabled={page === 1}
                  className="p-2 rounded-lg border border-gray-200 bg-white text-gray-600 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  <ChevronLeft className="w-5 h-5" />
                </button>
                <div className="px-4 py-2 rounded-lg bg-white border border-gray-200 text-sm font-medium text-gray-900">
                  Page {page} of {totalPages}
                </div>
                <button
                  onClick={() => setPage(p => Math.min(totalPages, p + 1))}
                  disabled={page >= totalPages}
                  className="p-2 rounded-lg border border-gray-200 bg-white text-gray-600 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  <ChevronRight className="w-5 h-5" />
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
