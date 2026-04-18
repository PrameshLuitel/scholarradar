import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, ChevronDown, ChevronUp, ExternalLink, MapPin, DollarSign, Clock, Building2, BookOpen, Phone, Mail, Globe, Filter } from 'lucide-react';

export default function Cricos() {
  const [data, setData] = useState([]);
  const [totalCount, setTotalCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [expandedCourse, setExpandedCourse] = useState(null);
  const [universities, setUniversities] = useState([]);
  
  // Filter States
  const [query, setQuery] = useState('');
  const [searchInput, setSearchInput] = useState('');
  const [selectedLevel, setSelectedLevel] = useState('All');
  const [selectedState, setSelectedState] = useState('All');
  const [selectedUniversity, setSelectedUniversity] = useState('All');
  const [maxFee, setMaxFee] = useState(null);
  const [minDuration, setMinDuration] = useState(null);
  const [maxDuration, setMaxDuration] = useState(null);
  
  // Pagination
  const [page, setPage] = useState(1);
  const pageSize = 50;

  const levels = ['All', 'Bachelor', 'Master', 'Doctorate', 'Diploma', 'Certificate', 'Vocational'];
  const states = ['All', 'NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT'];

  // Fetch universities for filter
  useEffect(() => {
    const fetchUniversities = async () => {
      try {
        const response = await fetch('/api/cricos/universities');
        const result = await response.json();
        if (result.data) {
          setUniversities(result.data);
        }
      } catch (error) {
        console.error('Failed to fetch universities', error);
      }
    };
    fetchUniversities();
  }, []);

  const fetchCricosData = async (currentPage, searchQuery) => {
    setLoading(true);
    try {
      const response = await fetch('/api/cricos/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: searchQuery || undefined,
          state: selectedState === 'All' ? null : selectedState,
          level: selectedLevel === 'All' ? null : selectedLevel,
          university: selectedUniversity === 'All' ? null : selectedUniversity,
          max_fee: maxFee || undefined,
          min_duration: minDuration || undefined,
          max_duration: maxDuration || undefined,
          page: currentPage,
          page_size: pageSize
        })
      });
      
      const result = await response.json();
      if (result.data) {
        setData(result.data);
        setTotalCount(result.total_count);
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
  }, [page, selectedLevel, selectedState, selectedUniversity, maxFee, minDuration, maxDuration, query]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    setPage(1);
    setQuery(searchInput);
  };

  const totalPages = Math.ceil(totalCount / pageSize);

  const toggleExpand = (courseId) => {
    setExpandedCourse(expandedCourse === courseId ? null : courseId);
  };

  const formatCurrency = (amount) => {
    if (!amount) return '-';
    return `$${amount.toLocaleString()}`;
  };

  const formatDuration = (months) => {
    if (!months) return '-';
    if (months < 12) return `${months}mo`;
    const years = Math.floor(months / 12);
    const remainingMonths = months % 12;
    return remainingMonths > 0 ? `${years}y ${remainingMonths}mo` : `${years}y`;
  };

  return (
    <div className="min-h-screen bg-[#fafafa] pt-24 pb-16">
      <div className="max-w-7xl mx-auto px-6">
        
        {/* Header */}
        <motion.div 
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
          className="mb-10"
        >
          <h1 className="font-serif text-5xl font-medium text-gray-900 mb-3">
            CRICOS Register
          </h1>
          <p className="text-lg text-gray-500 font-light">
            Official Australian Government courses for international students
          </p>
          {totalCount > 0 && (
            <p className="text-sm text-gray-400 mt-2">
              {totalCount.toLocaleString()} courses available
            </p>
          )}
        </motion.div>

        {/* Search & Filters */}
        <motion.div 
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
          className="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 mb-8"
        >
          {/* AI Search Bar */}
          <form onSubmit={handleSearchSubmit} className="mb-4">
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input
                type="text"
                value={searchInput}
                onChange={(e) => setSearchInput(e.target.value)}
                placeholder="Search naturally... 'MBA in Sydney under $50k' or 'Engineering at UNSW'"
                className="w-full pl-12 pr-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-gray-900 placeholder:text-gray-400"
              />
            </div>
          </form>
          
          {/* Filter Grid */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-3">
            {/* State Filter */}
            <div className="relative">
              <MapPin className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
              <select
                value={selectedState}
                onChange={(e) => { setSelectedState(e.target.value); setPage(1); }}
                className="w-full pl-10 pr-8 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 text-sm text-gray-700 cursor-pointer appearance-none"
              >
                {states.map(s => <option key={s} value={s}>{s === 'All' ? 'All States' : s}</option>)}
              </select>
              <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 pointer-events-none" />
            </div>
            
            {/* Level Filter */}
            <div className="relative">
              <BookOpen className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
              <select
                value={selectedLevel}
                onChange={(e) => { setSelectedLevel(e.target.value); setPage(1); }}
                className="w-full pl-10 pr-8 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 text-sm text-gray-700 cursor-pointer appearance-none"
              >
                {levels.map(l => <option key={l} value={l}>{l === 'All' ? 'All Levels' : l}</option>)}
              </select>
              <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 pointer-events-none" />
            </div>

            {/* University Filter */}
            <div className="relative col-span-2">
              <Building2 className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
              <select
                value={selectedUniversity}
                onChange={(e) => { setSelectedUniversity(e.target.value); setPage(1); }}
                className="w-full pl-10 pr-8 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 text-sm text-gray-700 cursor-pointer appearance-none"
              >
                <option value="All">All Universities</option>
                {universities.map(uni => (
                  <option key={uni.name} value={uni.name}>{uni.name}</option>
                ))}
              </select>
              <ChevronDown className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400 pointer-events-none" />
            </div>
          </div>

          {/* Advanced Filters */}
          <div className="grid grid-cols-3 gap-3 pt-3 border-t border-gray-100">
            <div>
              <label className="block text-xs text-gray-500 mb-1.5 font-medium">Max Tuition (AUD)</label>
              <input
                type="number"
                value={maxFee || ''}
                onChange={(e) => { setMaxFee(e.target.value ? Number(e.target.value) : null); setPage(1); }}
                placeholder="e.g. 50000"
                className="w-full px-3 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 text-sm text-gray-700 placeholder:text-gray-400"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-500 mb-1.5 font-medium">Min Duration (months)</label>
              <input
                type="number"
                value={minDuration || ''}
                onChange={(e) => { setMinDuration(e.target.value ? Number(e.target.value) : null); setPage(1); }}
                placeholder="e.g. 12"
                className="w-full px-3 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 text-sm text-gray-700 placeholder:text-gray-400"
              />
            </div>
            <div>
              <label className="block text-xs text-gray-500 mb-1.5 font-medium">Max Duration (months)</label>
              <input
                type="number"
                value={maxDuration || ''}
                onChange={(e) => { setMaxDuration(e.target.value ? Number(e.target.value) : null); setPage(1); }}
                placeholder="e.g. 36"
                className="w-full px-3 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 text-sm text-gray-700 placeholder:text-gray-400"
              />
            </div>
          </div>
        </motion.div>

        {/* CRICOS Table */}
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.4, delay: 0.2 }}
          className="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden"
        >
          {loading ? (
            <div className="p-16 text-center">
              <div className="inline-block w-6 h-6 border-2 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
              <p className="mt-3 text-sm text-gray-500">Loading courses...</p>
            </div>
          ) : data.length === 0 ? (
            <div className="p-16 text-center">
              <p className="text-gray-500">No courses found</p>
              <p className="text-sm text-gray-400 mt-2">Try adjusting your search or filters</p>
            </div>
          ) : (
            <>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-gray-50/80 border-b border-gray-100">
                    <tr>
                      <th className="w-12 px-6 py-4"></th>
                      <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Course</th>
                      <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Institution</th>
                      <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Location</th>
                      <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Level</th>
                      <th className="px-6 py-4 text-right text-xs font-semibold text-gray-600 uppercase tracking-wider">Fee</th>
                      <th className="px-6 py-4 text-right text-xs font-semibold text-gray-600 uppercase tracking-wider">Duration</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-50">
                    {data.map((course, idx) => (
                      <React.Fragment key={course.id}>
                        <motion.tr 
                          initial={{ opacity: 0, y: 5 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: idx * 0.02, duration: 0.3 }}
                          className="hover:bg-blue-50/30 cursor-pointer transition-colors"
                          onClick={() => toggleExpand(course.id)}
                        >
                          <td className="px-6 py-4">
                            {expandedCourse === course.id ? (
                              <ChevronUp className="w-4 h-4 text-gray-400" />
                            ) : (
                              <ChevronDown className="w-4 h-4 text-gray-400" />
                            )}
                          </td>
                          <td className="px-6 py-4">
                            <div className="font-medium text-gray-900">{course.name}</div>
                            {course.cricos_code && (
                              <div className="text-xs text-gray-400 font-mono mt-0.5">{course.cricos_code}</div>
                            )}
                          </td>
                          <td className="px-6 py-4 text-sm text-gray-700">{course.university}</td>
                          <td className="px-6 py-4">
                            <div className="flex items-center gap-1.5 text-sm text-gray-700">
                              <MapPin className="w-3.5 h-3.5 text-gray-400" />
                              {course.city && course.state ? `${course.city}, ${course.state}` : course.city || course.state || '-'}
                            </div>
                          </td>
                          <td className="px-6 py-4">
                            <span className="inline-flex px-2.5 py-1 rounded-lg bg-blue-50 border border-blue-100 text-xs font-medium text-blue-700">
                              {course.level || '-'}
                            </span>
                          </td>
                          <td className="px-6 py-4 text-right">
                            <div className="font-semibold text-gray-900">{formatCurrency(course.tuition_fee)}</div>
                            {course.currency && course.currency !== 'AUD' && (
                              <div className="text-xs text-gray-400 mt-0.5">{course.currency}</div>
                            )}
                          </td>
                          <td className="px-6 py-4 text-right text-sm text-gray-700">
                            {formatDuration(course.duration_months)}
                          </td>
                        </motion.tr>
                        
                        {/* Expanded Details */}
                        {expandedCourse === course.id && (
                          <motion.tr
                            initial={{ opacity: 0, height: 0 }}
                            animate={{ opacity: 1, height: 'auto' }}
                            exit={{ opacity: 0, height: 0 }}
                            transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
                          >
                            <td colSpan="7" className="px-6 pb-6 bg-gradient-to-b from-blue-50/50 to-white">
                              <div className="pt-4 grid grid-cols-1 md:grid-cols-3 gap-6">
                                {/* Course Details */}
                                <div className="bg-white rounded-xl border border-gray-100 p-5 shadow-sm">
                                  <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-4 flex items-center gap-2">
                                    <BookOpen className="w-4 h-4" />
                                    Course Details
                                  </h4>
                                  <div className="space-y-3 text-sm">
                                    <div>
                                      <div className="text-xs text-gray-400 mb-0.5">Course Name</div>
                                      <div className="font-medium text-gray-900">{course.name || '-'}</div>
                                    </div>
                                    <div>
                                      <div className="text-xs text-gray-400 mb-0.5">CRICOS Code</div>
                                      <div className="font-mono text-gray-900">{course.cricos_code || '-'}</div>
                                    </div>
                                    <div>
                                      <div className="text-xs text-gray-400 mb-0.5">Level</div>
                                      <div className="text-gray-900">{course.level || '-'}</div>
                                    </div>
                                    <div>
                                      <div className="text-xs text-gray-400 mb-0.5">Duration</div>
                                      <div className="text-gray-900">{course.duration_months ? formatDuration(course.duration_months) : '-'}</div>
                                    </div>
                                    <div>
                                      <div className="text-xs text-gray-400 mb-0.5">Tuition Fee</div>
                                      <div className="font-semibold text-gray-900">{formatCurrency(course.tuition_fee)} {course.currency || 'AUD'}</div>
                                    </div>
                                    {course.subject && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Subject</div>
                                        <div className="text-gray-900">{course.subject}</div>
                                      </div>
                                    )}
                                    {course.subject_category && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Category</div>
                                        <div className="text-gray-900">{course.subject_category}</div>
                                      </div>
                                    )}
                                  </div>
                                </div>

                                {/* Institution Details */}
                                <div className="bg-white rounded-xl border border-gray-100 p-5 shadow-sm">
                                  <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-4 flex items-center gap-2">
                                    <Building2 className="w-4 h-4" />
                                    Institution
                                  </h4>
                                  <div className="space-y-3 text-sm">
                                    <div>
                                      <div className="text-xs text-gray-400 mb-0.5">Institution</div>
                                      <div className="font-medium text-gray-900">{course.university || '-'}</div>
                                    </div>
                                    {course.provider_code && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Provider Code</div>
                                        <div className="font-mono text-gray-900">{course.provider_code}</div>
                                      </div>
                                    )}
                                    {course.institution_type && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Type</div>
                                        <div className="text-gray-900">{course.institution_type}</div>
                                      </div>
                                    )}
                                    <div>
                                      <div className="text-xs text-gray-400 mb-0.5">Location</div>
                                      <div className="text-gray-900">{course.city && course.state ? `${course.city}, ${course.state}` : course.city || course.state || '-'}</div>
                                    </div>
                                    {course.postal_address && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Address</div>
                                        <div className="text-gray-900 text-xs leading-relaxed">{course.postal_address}</div>
                                      </div>
                                    )}
                                    {course.total_students && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Students</div>
                                        <div className="text-gray-900">{course.total_students.toLocaleString()}</div>
                                      </div>
                                    )}
                                  </div>
                                </div>

                                {/* Contact & Additional Info */}
                                <div className="bg-white rounded-xl border border-gray-100 p-5 shadow-sm">
                                  <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-4 flex items-center gap-2">
                                    <Globe className="w-4 h-4" />
                                    Contact & Info
                                  </h4>
                                  <div className="space-y-3 text-sm">
                                    {course.website && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Website</div>
                                        <a href={course.website} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:text-blue-700 flex items-center gap-1.5 group">
                                          <span className="truncate">{course.website}</span>
                                          <ExternalLink className="w-3 h-3 flex-shrink-0 opacity-0 group-hover:opacity-100 transition-opacity" />
                                        </a>
                                      </div>
                                    )}
                                    {course.contact_phone && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Phone</div>
                                        <a href={`tel:${course.contact_phone}`} className="text-blue-600 hover:text-blue-700 flex items-center gap-1.5">
                                          <Phone className="w-3 h-3" />
                                          {course.contact_phone}
                                        </a>
                                      </div>
                                    )}
                                    {course.contact_email && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Email</div>
                                        <a href={`mailto:${course.contact_email}`} className="text-blue-600 hover:text-blue-700 flex items-center gap-1.5">
                                          <Mail className="w-3 h-3" />
                                          {course.contact_email}
                                        </a>
                                      </div>
                                    )}
                                    {course.is_active !== undefined && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Status</div>
                                        <div className={`inline-flex px-2 py-0.5 rounded-full text-xs font-medium ${course.is_active ? 'bg-green-50 text-green-700 border border-green-200' : 'bg-red-50 text-red-700 border border-red-200'}`}>
                                          {course.is_active ? 'Active' : 'Inactive'}
                                        </div>
                                      </div>
                                    )}
                                    {course.last_verified && (
                                      <div>
                                        <div className="text-xs text-gray-400 mb-0.5">Last Verified</div>
                                        <div className="text-gray-900">{new Date(course.last_verified).toLocaleDateString('en-AU', { year: 'numeric', month: 'short', day: 'numeric' })}</div>
                                      </div>
                                    )}
                                  </div>
                                </div>
                              </div>
                            </td>
                          </motion.tr>
                        )}
                      </React.Fragment>
                    ))}
                  </tbody>
                </table>
              </div>
              
              {/* Pagination */}
              {totalPages > 1 && (
                <div className="px-6 py-4 border-t border-gray-100 bg-gray-50/50 flex items-center justify-between">
                  <div className="text-sm text-gray-600">
                    Showing <span className="font-medium text-gray-900">{((page - 1) * pageSize) + 1}</span> to <span className="font-medium text-gray-900">{Math.min(page * pageSize, totalCount)}</span> of <span className="font-medium text-gray-900">{totalCount.toLocaleString()}</span>
                  </div>
                  
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => setPage(p => Math.max(1, p - 1))}
                      disabled={page === 1}
                      className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    >
                      Previous
                    </button>
                    <span className="px-3 py-2 text-sm text-gray-600">
                      Page {page} of {totalPages}
                    </span>
                    <button
                      onClick={() => setPage(p => Math.min(totalPages, p + 1))}
                      disabled={page >= totalPages}
                      className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-200 rounded-lg hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    >
                      Next
                    </button>
                  </div>
                </div>
              )}
            </>
          )}
        </motion.div>

        {/* Footer */}
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="mt-8 text-center text-xs text-gray-400"
        >
          <p>Source: Australian Government - CRICOS (data.gov.au) • Updated daily</p>
        </motion.div>
      </div>
    </div>
  );
}
// rebuild trigger Sat Apr 18 20:35:49 +0545 2026
