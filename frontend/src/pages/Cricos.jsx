import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, Sparkles, Filter, ChevronLeft, ChevronRight, GraduationCap, MapPin, DollarSign, Clock, Building2, BookOpen, Calendar, Phone, Globe, ExternalLink, ChevronDown, ChevronUp, Mail, User, Building, PhoneCall } from 'lucide-react';

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
  const [selectedState, setSelectedState] = useState('All');
  const [sortBy, setSortBy] = useState('name');
  const [sortOrder, setSortOrder] = useState('asc');
  
  // Pagination
  const [page, setPage] = useState(1);
  const pageSize = 50;

  const levels = ['All', 'Undergraduate', 'Postgraduate', 'Bachelor', 'Master', 'Doctorate', 'Vocational', 'Diploma', 'Certificate'];
  const states = ['All', 'NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT'];

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
  }, [page, selectedLevel, selectedState, query]);

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
            Search and filter thousands of Australian courses for international students using AI.
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
              
              <select
                value={selectedState}
                onChange={(e) => { setSelectedState(e.target.value); setPage(1); }}
                className="bg-white border border-gray-200 text-gray-700 rounded-lg px-4 py-2 text-sm focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 cursor-pointer shadow-sm appearance-none min-w-[150px]"
                style={{ backgroundImage: "url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%239CA3AF%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E')", backgroundRepeat: 'no-repeat', backgroundPosition: 'right 1rem top 50%', backgroundSize: '0.65em auto' }}
              >
                {states.map(s => <option key={s} value={s}>{s === 'All' ? 'All States' : s}</option>)}
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
        <div className="bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden">
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

          {!loading && data.length > 0 && (
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead className="bg-gray-50 border-b border-gray-200">
                  <tr>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Course Name</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Institution</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">CRICOS Code</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Provider Code</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Level</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Location</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">State</th>
                    <th className="px-4 py-3 text-right text-xs font-semibold text-gray-700 uppercase tracking-wider">Tuition Fee</th>
                    <th className="px-4 py-3 text-right text-xs font-semibold text-gray-700 uppercase tracking-wider">Duration</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Website</th>
                    <th className="px-4 py-3 text-left text-xs font-semibold text-gray-700 uppercase tracking-wider">Contact</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-100">
                  {data.map((course, idx) => (
                    <React.Fragment key={course.id || idx}>
                      <tr 
                        onClick={() => toggleExpand(course.id)} 
                        className="hover:bg-blue-50/50 transition-colors cursor-pointer"
                      >
                        <td className="px-4 py-3">
                          <div className="font-medium text-gray-900 max-w-xs">{course.name}</div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="text-gray-700 max-w-xs">{course.university}</div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="font-mono text-xs bg-blue-50 px-2 py-1 rounded inline-block">{course.cricos_code || 'N/A'}</div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="font-mono text-xs bg-gray-50 px-2 py-1 rounded inline-block">{course.provider_code || 'N/A'}</div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="text-gray-700">{course.level || 'N/A'}</div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="text-gray-700">{course.city || 'N/A'}</div>
                        </td>
                        <td className="px-4 py-3">
                          <div className="text-gray-700">{course.state || 'N/A'}</div>
                        </td>
                        <td className="px-4 py-3 text-right">
                          <div className="font-semibold text-blue-600">
                            {course.tuition_fee ? `${course.currency || 'AUD'} ${course.tuition_fee.toLocaleString()}` : 'N/A'}
                          </div>
                        </td>
                        <td className="px-4 py-3 text-right">
                          <div className="text-gray-700">{course.duration_months ? `${course.duration_months} months` : 'N/A'}</div>
                        </td>
                        <td className="px-4 py-3">
                          {course.website ? (
                            <a href={course.website} target="_blank" rel="noopener noreferrer" onClick={(e) => e.stopPropagation()} className="text-blue-600 hover:text-blue-800 flex items-center gap-1">
                              <Globe className="w-3.5 h-3.5" />
                              <span className="text-xs">Visit</span>
                            </a>
                          ) : (
                            <span className="text-gray-400">N/A</span>
                          )}
                        </td>
                        <td className="px-4 py-3">
                          {expandedCourse === course.id ? (
                            <ChevronUp className="w-5 h-5 text-gray-400" />
                          ) : (
                            <ChevronDown className="w-5 h-5 text-gray-400" />
                          )}
                        </td>
                      </tr>
                      
                      {/* Expanded Details - ALL DATA */}
                      <AnimatePresence>
                        {expandedCourse === course.id && (
                          <motion.tr
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: 'auto', opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}
                            transition={{ duration: 0.3 }}
                          >
                            <td colSpan="12" className="p-0">
                              <div className="bg-gradient-to-br from-blue-50 to-indigo-50 border-l-4 border-blue-500">
                                <div className="p-6 space-y-6">
                                  
                                  {/* Course Details Section */}
                                  <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                                    <h4 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                                      <BookOpen className="w-5 h-5 text-blue-600" />
                                      Course Details
                                    </h4>
                                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">Course Name:</span>
                                        <span className="font-semibold text-gray-900">{course.name}</span>
                                      </div>
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">CRICOS Course Code:</span>
                                        <span className="font-mono font-semibold text-blue-600">{course.cricos_code || 'N/A'}</span>
                                      </div>
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">Course Level:</span>
                                        <span className="font-semibold text-gray-900">{course.level || 'N/A'}</span>
                                      </div>
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">Duration:</span>
                                        <span className="font-semibold text-gray-900">{course.duration_months ? `${course.duration_months} months (${course.duration_months * 4.345} weeks)` : 'N/A'}</span>
                                      </div>
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">Tuition Fee:</span>
                                        <span className="font-semibold text-blue-600">{course.tuition_fee ? `AUD ${course.tuition_fee.toLocaleString()}` : 'N/A'}</span>
                                      </div>
                                      {course.subject_category && (
                                        <div>
                                          <span className="text-sm text-gray-600 block mb-1">Field of Education (Broad):</span>
                                          <span className="font-semibold text-gray-900">{course.subject_category}</span>
                                        </div>
                                      )}
                                      {course.subject && (
                                        <div>
                                          <span className="text-sm text-gray-600 block mb-1">Field of Education (Narrow):</span>
                                          <span className="font-semibold text-gray-900">{course.subject}</span>
                                        </div>
                                      )}
                                    </div>
                                  </div>

                                  {/* Institution Details Section */}
                                  <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                                    <h4 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                                      <Building className="w-5 h-5 text-indigo-600" />
                                      Institution Details
                                    </h4>
                                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">Institution Name:</span>
                                        <span className="font-semibold text-gray-900">{course.university}</span>
                                      </div>
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">CRICOS Provider Code:</span>
                                        <span className="font-mono font-semibold text-indigo-600">{course.provider_code || 'N/A'}</span>
                                      </div>
                                      {course.institution_type && (
                                        <div>
                                          <span className="text-sm text-gray-600 block mb-1">Institution Type:</span>
                                          <span className="font-semibold text-gray-900">{course.institution_type}</span>
                                        </div>
                                      )}
                                      {course.total_students && (
                                        <div>
                                          <span className="text-sm text-gray-600 block mb-1">Total Capacity:</span>
                                          <span className="font-semibold text-gray-900">{course.total_students.toLocaleString()} students</span>
                                        </div>
                                      )}
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">Location:</span>
                                        <span className="font-semibold text-gray-900">{course.city || 'N/A'}, {course.state || 'N/A'}</span>
                                      </div>
                                      {course.postal_address && (
                                        <div className="md:col-span-2 lg:col-span-3">
                                          <span className="text-sm text-gray-600 block mb-1">Postal Address:</span>
                                          <span className="font-semibold text-gray-900">{course.postal_address}</span>
                                        </div>
                                      )}
                                    </div>
                                  </div>

                                  {/* Contact Information Section */}
                                  {(course.website || course.contact_phone || course.contact_email) && (
                                    <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                                      <h4 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                                        <PhoneCall className="w-5 h-5 text-green-600" />
                                        Contact Information
                                      </h4>
                                      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                                        {course.website && (
                                          <div>
                                            <span className="text-sm text-gray-600 block mb-1">Website:</span>
                                            <a href={course.website} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:text-blue-800 font-semibold flex items-center gap-1">
                                              <Globe className="w-4 h-4" />
                                              {course.website}
                                            </a>
                                          </div>
                                        )}
                                        {course.contact_phone && (
                                          <div>
                                            <span className="text-sm text-gray-600 block mb-1">Phone Number:</span>
                                            <a href={`tel:${course.contact_phone}`} className="text-blue-600 hover:text-blue-800 font-semibold flex items-center gap-1">
                                              <Phone className="w-4 h-4" />
                                              {course.contact_phone}
                                            </a>
                                          </div>
                                        )}
                                        {course.contact_email && (
                                          <div>
                                            <span className="text-sm text-gray-600 block mb-1">Email Address:</span>
                                            <a href={`mailto:${course.contact_email}`} className="text-blue-600 hover:text-blue-800 font-semibold flex items-center gap-1">
                                              <Mail className="w-4 h-4" />
                                              {course.contact_email}
                                            </a>
                                          </div>
                                        )}
                                      </div>
                                    </div>
                                  )}

                                  {/* Additional Information */}
                                  <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-200">
                                    <h4 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                                      <Calendar className="w-5 h-5 text-gray-600" />
                                      Additional Information
                                    </h4>
                                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">Data Freshness:</span>
                                        <span className="font-semibold text-gray-900">{course.updated_at ? new Date(course.updated_at).toLocaleDateString('en-AU') : 'N/A'}</span>
                                      </div>
                                      <div>
                                        <span className="text-sm text-gray-600 block mb-1">Status:</span>
                                        <span className={`font-semibold ${course.is_active ? 'text-green-600' : 'text-red-600'}`}>
                                          {course.is_active ? 'Active' : 'Inactive'}
                                        </span>
                                      </div>
                                      {course.last_verified && (
                                        <div>
                                          <span className="text-sm text-gray-600 block mb-1">Last Verified:</span>
                                          <span className="font-semibold text-gray-900">{new Date(course.last_verified).toLocaleDateString('en-AU')}</span>
                                        </div>
                                      )}
                                    </div>
                                  </div>

                                </div>
                              </div>
                            </td>
                          </motion.tr>
                        )}
                      </AnimatePresence>
                    </React.Fragment>
                  ))}
                </tbody>
              </table>
            </div>
          )}
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
