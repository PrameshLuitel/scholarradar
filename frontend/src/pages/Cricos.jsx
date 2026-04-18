import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, Sparkles, Filter, ChevronLeft, ChevronRight, GraduationCap, MapPin, DollarSign, Clock, Building2, BookOpen, Calendar, Phone, Globe, ChevronDown, ChevronUp, ExternalLink } from 'lucide-react';

export default function Cricos() {
  const [data, setData] = useState([]);
  const [totalCount, setTotalCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [aiFiltersApplied, setAiFiltersApplied] = useState(null);
  const [expandedCourse, setExpandedCourse] = useState(null);
  
  // Filter States
  const [query, setQuery] = useState('');
  const [searchInput, setSearchInput] = useState('');
  const [selectedLevel, setSelectedLevel] = useState('All');
  const [sortBy, setSortBy] = useState('name');
  const [sortOrder, setSortOrder] = useState('asc');
  
  // Pagination
  const [page, setPage] = useState(1);
  const pageSize = 20;

  const levels = ['All', 'Undergraduate', 'Postgraduate', 'Bachelor', 'Master', 'Doctorate', 'Vocational', 'Diploma', 'Certificate'];

  const fetchCricosData = async (currentPage, searchQuery) => {
    setLoading(true);
    setAiFiltersApplied(null);
    try {
      const response = await fetch('/api/cricos/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: searchQuery,
          state: null,
          level: selectedLevel === 'All' ? null : selectedLevel,
          page: currentPage,
          page_size: pageSize
        })
      });
      
      const result = await response.json();
      if (result.data) {
        setData(result.data);
        setTotalCount(result.total_count);
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
  }, [page, selectedLevel, query]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    setPage(1);
    setQuery(searchInput);
  };

  const totalPages = Math.ceil(totalCount / pageSize);

  const toggleExpand = (courseId) => {
    setExpandedCourse(expandedCourse === courseId ? null : courseId);
  };

  const formatCurrency = (amount, currency) => {
    if (!amount) return 'Not specified';
    return `${currency || 'AUD'} ${amount.toLocaleString()}`;
  };

  const formatDate = (dateString) => {
    if (!dateString) return 'Not specified';
    try {
      return new Date(dateString).toLocaleDateString('en-AU', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    } catch {
      return dateString;
    }
  };

  return (
    <div className="min-h-screen bg-[#fafafa] pt-24 pb-16 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto space-y-8">
        
        {/* Header Section */}
        <div className="text-center max-w-3xl mx-auto">
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
                value={selectedLevel}
                onChange={(e) => { setSelectedLevel(e.target.value); setPage(1); }}
                className="bg-white border border-gray-200 text-gray-700 rounded-lg px-4 py-2 text-sm focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 cursor-pointer shadow-sm appearance-none min-w-[180px]"
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

        {/* Database Cards */}
        <div className="space-y-4">
          {loading && (
            <div className="flex items-center justify-center py-24">
              <div className="flex flex-col items-center">
                <div className="w-12 h-12 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>
                <p className="mt-4 text-blue-900 font-medium">Loading courses...</p>
              </div>
            </div>
          )}
          
          {!loading && data.length === 0 && (
            <div className="bg-white rounded-2xl shadow-lg border border-gray-100 p-24 text-center">
              <Search className="w-16 h-16 text-gray-300 mx-auto mb-4" />
              <p className="text-xl font-medium text-gray-900 mb-2">No courses found</p>
              <p className="text-gray-500">Try adjusting your search query or filters.</p>
            </div>
          )}

          <AnimatePresence mode="popLayout">
            {!loading && data.map((course, idx) => (
              <motion.div
                key={course.id || idx}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: Math.min(idx * 0.05, 0.5) }}
                className="bg-white rounded-2xl shadow-md border border-gray-100 overflow-hidden hover:shadow-lg transition-shadow"
              >
                {/* Course Header */}
                <div className="p-6 cursor-pointer" onClick={() => toggleExpand(course.id)}>
                  <div className="flex items-start justify-between gap-4">
                    <div className="flex-1">
                      <h3 className="text-xl font-bold text-gray-900 mb-2 hover:text-blue-700 transition-colors">
                        {course.name}
                      </h3>
                      <div className="flex flex-wrap items-center gap-4 text-sm text-gray-600">
                        <div className="flex items-center gap-1.5">
                          <Building2 className="w-4 h-4 text-gray-400" />
                          <span className="font-medium">{course.university}</span>
                        </div>
                        {course.city && (
                          <div className="flex items-center gap-1.5">
                            <MapPin className="w-4 h-4 text-gray-400" />
                            <span>{course.city}, {course.country}</span>
                          </div>
                        )}
                      </div>
                    </div>
                    <div className="flex items-center gap-3">
                      {course.tuition_fee && (
                        <div className="text-right">
                          <div className="text-2xl font-bold text-blue-600">
                            {formatCurrency(course.tuition_fee, course.currency)}
                          </div>
                          <div className="text-xs text-gray-500">per year</div>
                        </div>
                      )}
                      {expandedCourse === course.id ? (
                        <ChevronUp className="w-5 h-5 text-gray-400" />
                      ) : (
                        <ChevronDown className="w-5 h-5 text-gray-400" />
                      )}
                    </div>
                  </div>

                  {/* Quick Info Badges */}
                  <div className="flex flex-wrap gap-2 mt-4">
                    {course.level && (
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-semibold border border-blue-200">
                        <GraduationCap className="w-3.5 h-3.5" />
                        {course.level}
                      </span>
                    )}
                    {course.duration_months && (
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-green-50 text-green-700 text-xs font-semibold border border-green-200">
                        <Clock className="w-3.5 h-3.5" />
                        {course.duration_months} months
                      </span>
                    )}
                    {course.ielts_overall && (
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-50 text-purple-700 text-xs font-semibold border border-purple-200">
                        <BookOpen className="w-3.5 h-3.5" />
                        IELTS: {course.ielts_overall}
                      </span>
                    )}
                    {course.subject_category && (
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-orange-50 text-orange-700 text-xs font-semibold border border-orange-200">
                        {course.subject_category}
                      </span>
                    )}
                  </div>
                </div>

                {/* Expanded Details */}
                <AnimatePresence>
                  {expandedCourse === course.id && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: 'auto', opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.3 }}
                      className="border-t border-gray-100"
                    >
                      <div className="p-6 bg-gray-50/50">
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                          {/* IELTS Requirements */}
                          {(course.ielts_overall || course.ielts_reading || course.ielts_writing || course.ielts_speaking || course.ielts_listening) && (
                            <div className="bg-white p-4 rounded-xl border border-gray-200">
                              <h4 className="text-sm font-bold text-gray-900 mb-3 flex items-center gap-2">
                                <BookOpen className="w-4 h-4 text-purple-600" />
                                IELTS Requirements
                              </h4>
                              <div className="space-y-2 text-sm">
                                {course.ielts_overall && (
                                  <div className="flex justify-between">
                                    <span className="text-gray-600">Overall:</span>
                                    <span className="font-semibold text-gray-900">{course.ielts_overall}</span>
                                  </div>
                                )}
                                {course.ielts_reading && (
                                  <div className="flex justify-between">
                                    <span className="text-gray-600">Reading:</span>
                                    <span className="font-semibold text-gray-900">{course.ielts_reading}</span>
                                  </div>
                                )}
                                {course.ielts_writing && (
                                  <div className="flex justify-between">
                                    <span className="text-gray-600">Writing:</span>
                                    <span className="font-semibold text-gray-900">{course.ielts_writing}</span>
                                  </div>
                                )}
                                {course.ielts_speaking && (
                                  <div className="flex justify-between">
                                    <span className="text-gray-600">Speaking:</span>
                                    <span className="font-semibold text-gray-900">{course.ielts_speaking}</span>
                                  </div>
                                )}
                                {course.ielts_listening && (
                                  <div className="flex justify-between">
                                    <span className="text-gray-600">Listening:</span>
                                    <span className="font-semibold text-gray-900">{course.ielts_listening}</span>
                                  </div>
                                )}
                              </div>
                            </div>
                          )}

                          {/* Duration & Dates */}
                          <div className="bg-white p-4 rounded-xl border border-gray-200">
                            <h4 className="text-sm font-bold text-gray-900 mb-3 flex items-center gap-2">
                              <Calendar className="w-4 h-4 text-green-600" />
                              Duration & Dates
                            </h4>
                            <div className="space-y-2 text-sm">
                              {course.duration_months && (
                                <div className="flex justify-between">
                                  <span className="text-gray-600">Duration:</span>
                                  <span className="font-semibold text-gray-900">{course.duration_months} months</span>
                                </div>
                              )}
                              {course.start_dates && course.start_dates.length > 0 && (
                                <div>
                                  <span className="text-gray-600 block mb-1">Start Dates:</span>
                                  <div className="space-y-1">
                                    {Array.isArray(course.start_dates) ? (
                                      course.start_dates.map((date, i) => (
                                        <div key={i} className="font-semibold text-gray-900">
                                          {formatDate(date)}
                                        </div>
                                      ))
                                    ) : (
                                      <div className="font-semibold text-gray-900">
                                        {formatDate(course.start_dates)}
                                      </div>
                                    )}
                                  </div>
                                </div>
                              )}
                            </div>
                          </div>

                          {/* Additional Requirements */}
                          {(course.gpa_requirement || course.entry_qualification) && (
                            <div className="bg-white p-4 rounded-xl border border-gray-200">
                              <h4 className="text-sm font-bold text-gray-900 mb-3 flex items-center gap-2">
                                <GraduationCap className="w-4 h-4 text-blue-600" />
                                Entry Requirements
                              </h4>
                              <div className="space-y-2 text-sm">
                                {course.gpa_requirement && (
                                  <div>
                                    <span className="text-gray-600 block mb-1">GPA:</span>
                                    <span className="font-semibold text-gray-900">{course.gpa_requirement}</span>
                                  </div>
                                )}
                                {course.entry_qualification && (
                                  <div>
                                    <span className="text-gray-600 block mb-1">Qualification:</span>
                                    <span className="font-semibold text-gray-900">{course.entry_qualification}</span>
                                  </div>
                                )}
                              </div>
                            </div>
                          )}

                          {/* Subject Information */}
                          {(course.subject || course.subject_category) && (
                            <div className="bg-white p-4 rounded-xl border border-gray-200">
                              <h4 className="text-sm font-bold text-gray-900 mb-3 flex items-center gap-2">
                                <BookOpen className="w-4 h-4 text-orange-600" />
                                Subject Area
                              </h4>
                              <div className="space-y-2 text-sm">
                                {course.subject_category && (
                                  <div>
                                    <span className="text-gray-600 block mb-1">Category:</span>
                                    <span className="font-semibold text-gray-900">{course.subject_category}</span>
                                  </div>
                                )}
                                {course.subject && (
                                  <div>
                                    <span className="text-gray-600 block mb-1">Subject:</span>
                                    <span className="font-semibold text-gray-900">{course.subject}</span>
                                  </div>
                                )}
                              </div>
                            </div>
                          )}

                          {/* Links */}
                          {(course.apply_url || course.source_url) && (
                            <div className="bg-white p-4 rounded-xl border border-gray-200">
                              <h4 className="text-sm font-bold text-gray-900 mb-3 flex items-center gap-2">
                                <ExternalLink className="w-4 h-4 text-indigo-600" />
                                Useful Links
                              </h4>
                              <div className="space-y-2 text-sm">
                                {course.apply_url && (
                                  <a
                                    href={course.apply_url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="flex items-center gap-2 text-blue-600 hover:text-blue-800 transition-colors"
                                  >
                                    <Globe className="w-3.5 h-3.5" />
                                    <span className="font-medium">Apply Now</span>
                                  </a>
                                )}
                                {course.source_url && course.source_url !== course.apply_url && (
                                  <a
                                    href={course.source_url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="flex items-center gap-2 text-blue-600 hover:text-blue-800 transition-colors"
                                  >
                                    <Globe className="w-3.5 h-3.5" />
                                    <span className="font-medium">Course Details</span>
                                  </a>
                                )}
                              </div>
                            </div>
                          )}

                          {/* Data Information */}
                          <div className="bg-white p-4 rounded-xl border border-gray-200">
                            <h4 className="text-sm font-bold text-gray-900 mb-3 flex items-center gap-2">
                              <Calendar className="w-4 h-4 text-gray-600" />
                              Data Information
                            </h4>
                            <div className="space-y-2 text-sm">
                              <div className="flex justify-between">
                                <span className="text-gray-600">Last Verified:</span>
                                <span className="font-semibold text-gray-900">
                                  {course.last_verified ? formatDate(course.last_verified) : 'Not verified'}
                                </span>
                              </div>
                              <div className="flex justify-between">
                                <span className="text-gray-600">Status:</span>
                                <span className={`font-semibold ${course.is_active ? 'text-green-600' : 'text-red-600'}`}>
                                  {course.is_active ? 'Active' : 'Inactive'}
                                </span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>

        {/* Pagination Footer */}
        {!loading && data.length > 0 && (
          <div className="bg-white rounded-2xl shadow-lg border border-gray-100 px-6 py-4 flex items-center justify-between">
            <div className="text-sm text-gray-600">
              Showing <span className="font-medium text-gray-900">{((page - 1) * pageSize) + 1}</span> to <span className="font-medium text-gray-900">{Math.min(page * pageSize, totalCount)}</span> of <span className="font-medium text-gray-900">{totalCount.toLocaleString()}</span> courses
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
  );
}
