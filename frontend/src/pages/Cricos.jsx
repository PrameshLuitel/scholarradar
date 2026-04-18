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
        
        {/* Header */}
        <div className="mb-6">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">CRICOS Course Register</h1>
          <p className="text-gray-600">Official Australian Government courses for international students ({totalCount.toLocaleString()} courses)</p>
        </div>

        {/* Search & Filters */}
        <div className="bg-white p-4 rounded-lg border border-gray-200 mb-6">
          <form onSubmit={handleSearchSubmit} className="mb-4">
            <input
              type="text"
              value={searchInput}
              onChange={(e) => setSearchInput(e.target.value)}
              placeholder="Search courses... e.g. 'MBA', 'Engineering', 'Nursing'"
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            />
          </form>
          
          <div className="flex gap-4">
            <select
              value={selectedState}
              onChange={(e) => { setSelectedState(e.target.value); setPage(1); }}
              className="px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            >
              {states.map(s => <option key={s} value={s}>{s === 'All' ? 'All States' : s}</option>)}
            </select>
            
            <select
              value={selectedLevel}
              onChange={(e) => { setSelectedLevel(e.target.value); setPage(1); }}
              className="px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            >
              {levels.map(l => <option key={l} value={l}>{l === 'All' ? 'All Levels' : l}</option>)}
            </select>
          </div>
        </div>

        {/* CRICOS Table */}
        <div className="bg-white border border-gray-200 rounded-lg overflow-hidden">
          {loading ? (
            <div className="p-8 text-center">Loading...</div>
          ) : data.length === 0 ? (
            <div className="p-8 text-center text-gray-600">No courses found</div>
          ) : (
            <>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead className="bg-gray-50 border-b border-gray-200">
                    <tr>
                      <th className="px-4 py-3 text-left font-semibold text-gray-700">Course</th>
                      <th className="px-4 py-3 text-left font-semibold text-gray-700">Institution</th>
                      <th className="px-4 py-3 text-left font-semibold text-gray-700">CRICOS Code</th>
                      <th className="px-4 py-3 text-left font-semibold text-gray-700">Level</th>
                      <th className="px-4 py-3 text-left font-semibold text-gray-700">Location</th>
                      <th className="px-4 py-3 text-right font-semibold text-gray-700">Fee (AUD)</th>
                      <th className="px-4 py-3 text-right font-semibold text-gray-700">Duration</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-100">
                    {data.map((course) => (
                      <tr key={course.id} className="hover:bg-gray-50">
                        <td className="px-4 py-3 font-medium text-gray-900">{course.name}</td>
                        <td className="px-4 py-3 text-gray-700">{course.university}</td>
                        <td className="px-4 py-3 font-mono text-xs">{course.cricos_code}</td>
                        <td className="px-4 py-3 text-gray-700">{course.level}</td>
                        <td className="px-4 py-3 text-gray-700">{course.city}, {course.state}</td>
                        <td className="px-4 py-3 text-right font-semibold">{course.tuition_fee ? `$${course.tuition_fee.toLocaleString()}` : '-'}</td>
                        <td className="px-4 py-3 text-right">{course.duration_months ? `${course.duration_months} mo` : '-'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              
              {/* Pagination */}
              <div className="px-4 py-3 border-t border-gray-200 flex items-center justify-between">
                <div className="text-sm text-gray-600">
                  Showing {((page - 1) * pageSize) + 1}-{Math.min(page * pageSize, totalCount)} of {totalCount.toLocaleString()}
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={() => setPage(p => Math.max(1, p - 1))}
                    disabled={page === 1}
                    className="px-3 py-1 border border-gray-300 rounded disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
                  >
                    Previous
                  </button>
                  <span className="px-3 py-1">Page {page} of {totalPages}</span>
                  <button
                    onClick={() => setPage(p => Math.min(totalPages, p + 1))}
                    disabled={page >= totalPages}
                    className="px-3 py-1 border border-gray-300 rounded disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
                  >
                    Next
                  </button>
                </div>
              </div>
            </>
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
      
      {/* Footer */}
      <div className="mt-6 text-center text-sm text-gray-600">
        <p>Source: Australian Government - CRICOS (data.gov.au) | Updated: {new Date().toLocaleDateString('en-AU')}</p>
      </div>
    </div>
  );
}
