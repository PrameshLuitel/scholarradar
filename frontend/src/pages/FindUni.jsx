import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Upload, FileText, GraduationCap, Globe, DollarSign,
  Send, X, CheckCircle, AlertCircle, Loader2,
  ArrowRight, BookOpen, Target, Clock, Award,
  Info, ExternalLink, MapPin, Calendar, TrendingUp, ShieldCheck
} from 'lucide-react';

// ── Data ────────────────────────────────────────────────────────────────────

const COUNTRIES = [
  'Australia', 'United Kingdom', 'Canada', 'United States', 'Germany',
  'New Zealand', 'Ireland', 'Netherlands', 'Sweden', 'Denmark',
  'Finland', 'Norway', 'France', 'Japan', 'South Korea',
  'Singapore', 'Malaysia', 'Switzerland',
];

// State/Region data for countries that have it
const COUNTRY_STATES = {
  'australia': [
    'NSW (Sydney)', 'VIC (Melbourne)', 'QLD (Brisbane)', 'WA (Perth)',
    'SA (Adelaide)', 'TAS (Hobart)', 'ACT (Canberra)', 'NT (Darwin)'
  ],
  'united kingdom': [
    'England', 'Scotland', 'Wales', 'Northern Ireland',
    'London', 'Manchester', 'Birmingham', 'Edinburgh', 'Bristol'
  ],
  'canada': [
    'Ontario (Toronto)', 'British Columbia (Vancouver)', 'Quebec (Montreal)',
    'Alberta (Calgary)', 'Manitoba', 'Saskatchewan', 'Nova Scotia'
  ],
  'united states': [
    'California', 'New York', 'Texas', 'Massachusetts (Boston)',
    'Illinois (Chicago)', 'Washington (Seattle)', 'Florida'
  ],
  'germany': [
    'Bavaria (Munich)', 'Berlin', 'North Rhine-Westphalia',
    'Baden-Württemberg', 'Hamburg', 'Hesse (Frankfurt)'
  ],
  'new zealand': [
    'Auckland', 'Wellington', 'Canterbury (Christchurch)',
    'Otago (Dunedin)', 'Waikato (Hamilton)'
  ],
};

const NATIONALITIES = [
  'Nepalese', 'Indian', 'Bangladeshi', 'Pakistani', 'Sri Lankan',
  'Chinese', 'Vietnamese', 'Filipino', 'Indonesian', 'Nigerian',
  'Ghanaian', 'Kenyan', 'Ethiopian', 'Egyptian', 'Brazilian',
  'Colombian', 'Mexican', 'Turkish', 'Iranian', 'Thai',
  'Myanmar', 'Cambodian', 'Mongolian', 'Afghan', 'Other',
];

const QUALIFICATIONS = [
  { value: 'high_school', label: 'High School / +2 / A-Levels', level: 'Undergraduate' },
  { value: 'bachelors', label: "Bachelor's Degree", level: 'Postgraduate' },
  { value: 'masters', label: "Master's Degree", level: 'PhD / Doctorate' },
  { value: 'phd', label: 'PhD / Doctorate', level: 'Postdoc' },
];

const SUBJECT_SUGGESTIONS = [
  'Computer Science', 'Data Science', 'Software Engineering', 'Artificial Intelligence',
  'Cybersecurity', 'Information Technology', 'Engineering', 'Electrical Engineering',
  'Mechanical Engineering', 'Civil Engineering', 'Business Administration', 'MBA',
  'Finance', 'Accounting', 'Marketing', 'Economics', 'Medicine', 'Nursing',
  'Public Health', 'Pharmacy', 'Biotechnology', 'Environmental Science',
  'Law', 'Education', 'Psychology', 'Architecture', 'Graphic Design',
  'International Relations', 'Journalism', 'Agriculture', 'Hospitality Management',
];


// ── Course Card ─────────────────────────────────────────────────────────────

function CourseCard({ course, index, allCourses, allScholarships }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const relevance = Math.round((course.relevance || 0) * 100);
  const showCodes = course.country?.toLowerCase() === 'australia' && (course.cricos_code || course.provider_code);

  // Find related scholarships for this university
  const relatedScholarships = allScholarships.filter(s => 
    s.university?.toLowerCase() === course.university?.toLowerCase()
  ).slice(0, 3);

  // Find alternative courses at same university
  const alternativeCourses = allCourses.filter(c => 
    c.university?.toLowerCase() === course.university?.toLowerCase() && 
    c.name !== course.name
  ).slice(0, 3);

  // Calculate total course cost
  const totalCost = course.tuition_fee && course.duration_months 
    ? course.tuition_fee * (course.duration_months / 12)
    : null;
  
  // Calculate potential scholarship savings
  const topScholarship = relatedScholarships[0];
  const scholarshipAmount = topScholarship?.amount ? 
    (typeof topScholarship.amount === 'string' ? 
      parseFloat(topScholarship.amount.replace(/[^0-9.]/g, '')) : 
      topScholarship.amount) : 0;
  const costAfterScholarship = totalCost && scholarshipAmount > 0 ? 
    totalCost - scholarshipAmount : null;

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.05, duration: 0.3 }}
      className="bg-white rounded-2xl border border-gray-100 hover:shadow-md transition-shadow group relative overflow-hidden"
    >
      {/* Clickable Card Header */}
      <div 
        onClick={() => setIsExpanded(!isExpanded)}
        className="p-5 cursor-pointer"
      >
        {/* Reasoning Badge */}
        <div className="flex items-center gap-1.5 mb-3">
          <div className="px-2 py-0.5 rounded-full bg-blue-50 border border-blue-100 text-[10px] font-bold text-blue-600 uppercase tracking-tight">
            {course.is_cricos ? 'CRICOS Verified' : 'Verified'}
          </div>
          <span className="text-[11px] font-medium text-gray-500 italic">{course.match_reason}</span>
          <span className="ml-auto text-[10px] text-gray-400 font-medium">
            {isExpanded ? 'Click to collapse ▲' : 'Click for details ▼'}
          </span>
        </div>

        <div className="flex items-start justify-between gap-3 mb-4">
          <div className="flex-1 min-w-0">
            <h4 className="font-semibold text-gray-900 text-sm leading-snug mb-1 line-clamp-2">{course.name}</h4>
            <p className="text-xs text-gray-500 font-medium flex items-center gap-1">
              {course.university}
            </p>
            <div className="flex flex-col gap-0.5 mt-1">
                <p className="text-[10px] text-gray-400 flex items-center gap-1 uppercase tracking-wider">
                  <MapPin className="w-2.5 h-2.5" />
                  {course.city}{course.state && `, ${course.state}`}
                  {course.locations?.length > 1 && (
                    <span className="text-blue-500 font-bold ml-1">
                      + {course.locations.length - 1} more locations
                    </span>
                  )}
                </p>
                {showCodes && (
                  <div className="flex items-center gap-1.5 mt-1">
                    {course.cricos_code && <span className="text-[9px] bg-gray-50 text-gray-400 px-1.5 py-0.5 rounded border border-gray-100 font-mono">CRICOS: {course.cricos_code}</span>}
                    {course.provider_code && <span className="text-[9px] bg-gray-50 text-gray-400 px-1.5 py-0.5 rounded border border-gray-100 font-mono">PROV: {course.provider_code}</span>}
                  </div>
                )}
              </div>
          </div>
          <div className="flex-shrink-0">
            <div className={`w-10 h-10 rounded-xl flex items-center justify-center text-xs font-bold ${
              relevance >= 80 ? 'bg-green-50 text-green-700' :
              relevance >= 50 ? 'bg-blue-50 text-blue-700' :
              'bg-gray-50 text-gray-600'
            }`}>
              {relevance}%
            </div>
          </div>
        </div>

        <div className="flex items-center flex-wrap gap-2 mb-4">
          {course.country && (
            <span className="px-2 py-0.5 rounded-md bg-gray-50 text-gray-600 text-[10px] font-bold uppercase tracking-wider">{course.country}</span>
          )}
          {course.level && (
            <span className="px-2 py-0.5 rounded-md bg-blue-50 text-blue-700 text-[10px] font-bold uppercase tracking-wider">{course.level}</span>
          )}
          {course.duration_months && (
            <span className="px-2 py-0.5 rounded-md bg-gray-50 text-gray-600 text-[10px] font-bold uppercase tracking-wider">{course.duration_months} months</span>
          )}
          {course.ielts_met === true && course.ielts_required && (
            <span className="px-2 py-0.5 rounded-md bg-green-50 text-green-700 text-[10px] font-bold uppercase tracking-wider">IELTS ✓ ({course.ielts_required})</span>
          )}
        </div>

        <div className="flex items-center justify-between pt-3 border-t border-gray-50">
          <div>
            <span className="text-sm font-bold text-gray-900">{course.tuition_display || 'Contact university'}</span>
            {totalCost && (
              <span className="block text-[10px] text-gray-500 mt-0.5">Total: {course.currency || 'AUD'} {totalCost.toLocaleString()}</span>
            )}
            {costAfterScholarship && costAfterScholarship > 0 && (
              <div className="mt-2 pt-2 border-t border-gray-100">
                <span className="text-[10px] text-green-600 font-medium">After {topScholarship.title}: </span>
                <span className="text-sm font-bold text-green-700">{course.currency || 'AUD'} {costAfterScholarship.toLocaleString(undefined, {maximumFractionDigits: 0})}</span>
              </div>
            )}
          </div>
          {(course.apply_url || course.source_url) && (
            <a
              href={course.apply_url || course.source_url}
              target="_blank"
              rel="noopener noreferrer"
              onClick={(e) => e.stopPropagation()}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-gray-900 text-white text-[11px] font-bold hover:bg-black transition-colors"
            >
              Apply <ExternalLink className="w-3 h-3" />
            </a>
          )}
        </div>
      </div>

      {/* Expanded Details */}
      {isExpanded && (
        <motion.div
          initial={{ height: 0, opacity: 0 }}
          animate={{ height: 'auto', opacity: 1 }}
          exit={{ height: 0, opacity: 0 }}
          className="border-t border-gray-100"
        >
          <div className="p-5 space-y-5 bg-gray-50/50">
            {/* IELTS Details */}
            {course.ielts_breakdown && (
              <div>
                <h5 className="text-xs font-bold text-gray-900 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <BookOpen className="w-3.5 h-3.5" />
                  IELTS Requirements
                </h5>
                <div className="grid grid-cols-2 gap-2">
                  <div className="bg-white rounded-lg p-2 border border-gray-100">
                    <p className="text-[10px] text-gray-500">Overall</p>
                    <p className="text-sm font-bold text-gray-900">{course.ielts_breakdown.overall || 'N/A'}</p>
                  </div>
                  <div className="bg-white rounded-lg p-2 border border-gray-100">
                    <p className="text-[10px] text-gray-500">Reading</p>
                    <p className="text-sm font-bold text-gray-900">{course.ielts_breakdown.reading || 'N/A'}</p>
                  </div>
                  <div className="bg-white rounded-lg p-2 border border-gray-100">
                    <p className="text-[10px] text-gray-500">Writing</p>
                    <p className="text-sm font-bold text-gray-900">{course.ielts_breakdown.writing || 'N/A'}</p>
                  </div>
                  <div className="bg-white rounded-lg p-2 border border-gray-100">
                    <p className="text-[10px] text-gray-500">Speaking</p>
                    <p className="text-sm font-bold text-gray-900">{course.ielts_breakdown.speaking || 'N/A'}</p>
                  </div>
                </div>
              </div>
            )}

            {/* Start Dates */}
            {course.start_dates && course.start_dates.length > 0 && (
              <div>
                <h5 className="text-xs font-bold text-gray-900 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <Calendar className="w-3.5 h-3.5" />
                  Available Intakes
                </h5>
                <div className="flex flex-wrap gap-2">
                  {course.start_dates.map((date, idx) => (
                    <span key={idx} className="px-2 py-1 rounded-md bg-blue-50 text-blue-700 text-xs font-medium">
                      {date}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Entry Requirements */}
            {(course.entry_qualification || course.gpa_requirement) && (
              <div>
                <h5 className="text-xs font-bold text-gray-900 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <FileText className="w-3.5 h-3.5" />
                  Entry Requirements
                </h5>
                <div className="bg-white rounded-lg p-3 border border-gray-100 space-y-1">
                  {course.entry_qualification && (
                    <p className="text-xs text-gray-700"><span className="font-medium">Qualification:</span> {course.entry_qualification}</p>
                  )}
                  {course.gpa_requirement && (
                    <p className="text-xs text-gray-700"><span className="font-medium">GPA:</span> {course.gpa_requirement}</p>
                  )}
                </div>
              </div>
            )}

            {/* Related Scholarships */}
            {relatedScholarships.length > 0 && (
              <div>
                <h5 className="text-xs font-bold text-gray-900 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <Award className="w-3.5 h-3.5" />
                  Available Scholarships ({relatedScholarships.length})
                </h5>
                <div className="space-y-2">
                  {relatedScholarships.map((sch, idx) => (
                    <div key={idx} className="bg-white rounded-lg p-3 border border-amber-100">
                      <div className="flex items-start justify-between gap-2 mb-1">
                        <p className="text-xs font-semibold text-gray-900 line-clamp-1">{sch.title}</p>
                        <span className="text-xs font-bold text-amber-600 whitespace-nowrap">{sch.value}</span>
                      </div>
                      {sch.deadline && (
                        <p className="text-[10px] text-red-600 font-medium">Deadline: {new Date(sch.deadline).toLocaleDateString()}</p>
                      )}
                      {sch.apply_url && (
                        <a
                          href={sch.apply_url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-[10px] text-blue-600 hover:underline mt-1 inline-block"
                        >
                          Apply for scholarship →
                        </a>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Alternative Courses */}
            {alternativeCourses.length > 0 && (
              <div>
                <h5 className="text-xs font-bold text-gray-900 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                  <GraduationCap className="w-3.5 h-3.5" />
                  Other Courses at {course.university}
                </h5>
                <div className="space-y-2">
                  {alternativeCourses.map((alt, idx) => (
                    <div key={idx} className="bg-white rounded-lg p-3 border border-gray-100">
                      <div className="flex items-start justify-between gap-2 mb-1">
                        <p className="text-xs font-semibold text-gray-900 line-clamp-1">{alt.name}</p>
                        <span className="text-xs font-bold text-gray-900 whitespace-nowrap">{alt.tuition_display}</span>
                      </div>
                      <div className="flex items-center gap-2 text-[10px] text-gray-500">
                        <span>{alt.duration_months} months</span>
                        {alt.ielts_required && <span>• IELTS {alt.ielts_required}</span>}
                        {alt.level && <span>• {alt.level}</span>}
                      </div>
                      {alt.apply_url && (
                        <a
                          href={alt.apply_url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-[10px] text-blue-600 hover:underline mt-1 inline-block"
                        >
                          View details →
                        </a>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Source & Verification */}
            <div className="pt-3 border-t border-gray-200">
              <p className="text-[10px] text-gray-500">
                Data sourced from {course.source || 'official databases'} • 
                Last verified: {course.last_verified ? new Date(course.last_verified).toLocaleDateString() : 'Check official website'}
              </p>
            </div>
          </div>
        </motion.div>
      )}
    </motion.div>
  );
}


// ── Scholarship Card ────────────────────────────────────────────────────────

function ScholarshipCard({ scholarship, index }) {
  const score = Math.round((scholarship.match_score || 0) * 100);
  const isUrgent = scholarship.deadline && (() => {
    try {
      const days = Math.ceil((new Date(scholarship.deadline) - new Date()) / 86400000);
      return days > 0 && days < 30;
    } catch { return false; }
  })();

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.06, duration: 0.3 }}
      className="bg-white rounded-2xl border border-gray-100 p-5 hover:shadow-md transition-shadow group"
    >
      <div className="flex items-start justify-between gap-3 mb-2">
        <div className="flex-1 min-w-0">
          <h4 className="font-semibold text-gray-900 text-sm leading-snug mb-1 line-clamp-2">{scholarship.title}</h4>
          <p className="text-xs text-gray-500">{scholarship.university} • {scholarship.country}</p>
        </div>
        {isUrgent && (
          <span className="flex-shrink-0 px-2 py-0.5 rounded-md bg-red-50 text-red-600 text-[10px] font-bold uppercase animate-pulse">Urgent</span>
        )}
      </div>

      <div className="flex items-center flex-wrap gap-2 mb-3">
        {scholarship.funding_type && (
          <span className={`px-2 py-0.5 rounded-md text-[11px] font-medium ${
            scholarship.funding_type === 'full' ? 'bg-green-50 text-green-700' : 'bg-amber-50 text-amber-700'
          }`}>
            {scholarship.funding_type === 'full' ? 'Fully Funded' : 'Partial'}
          </span>
        )}
        {scholarship.deadline && (
          <span className="px-2 py-0.5 rounded-md bg-gray-50 text-gray-600 text-[11px] font-medium flex items-center gap-1">
            <Calendar className="w-3 h-3" />
            {new Date(scholarship.deadline).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}
          </span>
        )}
        {scholarship.why_matched?.slice(0, 2).map((r, i) => (
          <span key={i} className="px-2 py-0.5 rounded-md bg-blue-50 text-blue-700 text-[11px] font-medium">{r}</span>
        ))}
      </div>

      <div className="flex items-center justify-between">
        <span className="text-sm font-bold text-gray-900">{scholarship.value}</span>
        {(scholarship.apply_url || scholarship.source_url) && (
          <a
            href={scholarship.apply_url || scholarship.source_url}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center gap-1 text-xs text-blue-600 font-medium hover:underline opacity-0 group-hover:opacity-100 transition-opacity"
          >
            Apply <ExternalLink className="w-3 h-3" />
          </a>
        )}
      </div>
    </motion.div>
  );
}


// ── Markdown Renderer ───────────────────────────────────────────────────────

// Section header config for styled rendering
const SECTION_CONFIG = {
  '🎯': { color: 'blue', icon: Target, label: 'Profile Analysis' },
  '🎓': { color: 'indigo', icon: GraduationCap, label: 'Universities & Courses' },
  '💰': { color: 'amber', icon: Award, label: 'Scholarships' },
  '💵': { color: 'green', icon: DollarSign, label: 'Financial Reality' },
  '🛂': { color: 'purple', icon: Globe, label: 'Visa Pathway' },
  '📝': { color: 'blue', icon: BookOpen, label: 'Test Scores' },
  '📅': { color: 'teal', icon: Calendar, label: 'Action Plan' },
  '🚀': { color: 'rose', icon: TrendingUp, label: 'Career Pathway' },
  '⚠️': { color: 'gray', icon: Info, label: 'Disclaimers' },
};

function MarkdownResponse({ text }) {
  if (!text) return null;

  // Split into sections by h3 headers (### emoji Section Name)
  const sections = [];
  let currentSection = { title: '', emoji: '', lines: [] };

  for (const line of text.split('\n')) {
    const h3Match = line.match(/^###\s+([\p{Emoji}\u200d]+)\s*(.*)$/u);
    if (h3Match) {
      if (currentSection.title || currentSection.lines.length > 0) {
        sections.push({ ...currentSection });
      }
      currentSection = { title: h3Match[2].trim(), emoji: h3Match[1], lines: [] };
    } else {
      currentSection.lines.push(line);
    }
  }
  if (currentSection.title || currentSection.lines.length > 0) {
    sections.push(currentSection);
  }

  return (
    <div className="space-y-4">
      {sections.map((section, idx) => {
        const config = SECTION_CONFIG[section.emoji];
        const content = section.lines.join('\n').trim();
        if (!content && !section.title) return null;

        // If no matching config, render as plain section
        if (!section.title) {
          return (
            <div key={idx} className="text-sm text-gray-600 leading-relaxed">
              <RenderLines text={content} />
            </div>
          );
        }

        const colorMap = {
          blue: 'bg-blue-50 border-blue-100 text-blue-700',
          indigo: 'bg-indigo-50 border-indigo-100 text-indigo-700',
          amber: 'bg-amber-50 border-amber-100 text-amber-700',
          green: 'bg-green-50 border-green-100 text-green-700',
          purple: 'bg-purple-50 border-purple-100 text-purple-700',
          teal: 'bg-teal-50 border-teal-100 text-teal-700',
          rose: 'bg-rose-50 border-rose-100 text-rose-700',
          orange: 'bg-orange-50 border-orange-100 text-orange-700',
          gray: 'bg-gray-50 border-gray-200 text-gray-600',
        };

        const headerColor = config ? colorMap[config.color] || colorMap.blue : colorMap.blue;
        const IconComp = config?.icon || Info;

        return (
          <motion.div
            key={idx}
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1, duration: 0.3 }}
            className="bg-white rounded-2xl border border-gray-100 overflow-hidden"
          >
            {/* Section header */}
            <div className={`px-5 py-3 border-b flex items-center gap-2.5 ${headerColor}`}>
              <IconComp className="w-4 h-4 flex-shrink-0" />
              <span className="text-sm font-semibold">{section.emoji} {section.title}</span>
            </div>
            {/* Section content */}
            <div className="px-5 py-4 text-sm text-gray-700 leading-relaxed">
              <RenderLines text={content} />
            </div>
          </motion.div>
        );
      })}
    </div>
  );
}

function RenderLines({ text }) {
  if (!text) return null;
  return text.split('\n').map((line, i) => {
    if (!line.trim()) return <div key={i} className="h-2" />;

    // Sub-headers
    if (line.startsWith('#### ')) {
      return <h4 key={i} className="font-semibold text-gray-900 mt-4 mb-1.5 text-sm">{line.replace(/^#### /, '')}</h4>;
    }

    // Numbered items
    if (/^\d+\.\s/.test(line)) {
      return (
        <div key={i} className="flex gap-2.5 mb-2 pl-0.5">
          <span className="text-blue-600 font-bold flex-shrink-0 w-5 text-right">{line.match(/^\d+/)[0]}.</span>
          <span><InlineText text={line.replace(/^\d+\.\s/, '')} /></span>
        </div>
      );
    }

    // Bullets
    if (line.startsWith('- ') || line.startsWith('* ')) {
      return (
        <div key={i} className="flex gap-2.5 mb-1.5 pl-1">
          <span className="w-1.5 h-1.5 rounded-full bg-blue-400 flex-shrink-0 mt-2"></span>
          <span><InlineText text={line.replace(/^[-*]\s/, '')} /></span>
        </div>
      );
    }

    // Horizontal rule
    if (line.match(/^---+$/)) return <hr key={i} className="border-gray-100 my-4" />;

    // Regular paragraph
    return <p key={i} className="mb-2"><InlineText text={line} /></p>;
  });
}

function InlineText({ text }) {
  const html = text
    .replace(/\*\*(.*?)\*\*/g, '<strong class="text-gray-900 font-semibold">$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/`(.*?)`/g, '<code class="bg-gray-100 px-1 py-0.5 rounded text-xs font-mono text-gray-800">$1</code>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer" class="text-blue-600 underline underline-offset-2 hover:text-blue-800">$1</a>');
  return <span dangerouslySetInnerHTML={{ __html: html }} />;
}


// ── Main Component ──────────────────────────────────────────────────────────

export default function FindUni() {
  const [cvFile, setCvFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [profile, setProfile] = useState({
    nationality: '',
    current_qualification: '',
    gpa: '',
    ielts_overall: '',
    ielts_reading: '',
    ielts_writing: '',
    ielts_speaking: '',
    ielts_listening: '',
    target_subject: '',
    target_level: '',
    preferred_countries: [],
    preferred_states: [],  // NEW: State/region filtering
    budget_usd: 30000,
    timeline_months: 12,
    career_goal: '',
    work_experience_years: 0,
    extra_info: '',
  });
  const [showIeltsDetail, setShowIeltsDetail] = useState(false);
  const [suggestions, setSuggestions] = useState([]);

  // Results state
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [loadingStep, setLoadingStep] = useState(0);
  const [responseText, setResponseText] = useState('');
  const [metadata, setMetadata] = useState(null);
  const [modelInfo, setModelInfo] = useState(null);
  const [doneInfo, setDoneInfo] = useState(null);
  const [courses, setCourses] = useState([]);
  const [scholarships, setScholarships] = useState([]);
  const [locationFilter, setLocationFilter] = useState('');
  const [error, setError] = useState(null);

  const fileRef = useRef(null);
  const responseEndRef = useRef(null);

  const filteredCourses = courses.filter(c => {
    if (!locationFilter) return true;
    const search = locationFilter.toLowerCase();
    return (c.city?.toLowerCase() || '').includes(search) || 
           (c.state?.toLowerCase() || '').includes(search);
  });

  const availableLocations = Array.from(new Set(
    courses.flatMap(c => {
      const locs = [c.state, c.city];
      if (c.locations) {
        c.locations.forEach(l => {
          locs.push(l.state);
          locs.push(l.city);
        });
      }
      return locs;
    }).filter(Boolean)
  )).sort();

  const update = (k, v) => setProfile(p => ({ ...p, [k]: v }));
  const toggleCountry = (c) => {
    setProfile(p => ({
      ...p,
      preferred_countries: p.preferred_countries.includes(c)
        ? p.preferred_countries.filter(x => x !== c)
        : [...p.preferred_countries, c],
      // Clear states when country is deselected
      preferred_states: p.preferred_countries.includes(c)
        ? p.preferred_states
        : [],
    }));
  };

  const toggleState = (state) => {
    setProfile(p => ({
      ...p,
      preferred_states: p.preferred_states.includes(state)
        ? p.preferred_states.filter(x => x !== state)
        : [...p.preferred_states, state],
    }));
  };

  const toggleAllStates = (country, states, allSelected) => {
    setProfile(p => {
      const currentStates = [...p.preferred_states];
      if (allSelected) {
        // Deselect all states for this country
        return {
          ...p,
          preferred_states: currentStates.filter(s => !states.includes(s)),
        };
      } else {
        // Select all states for this country
        const newStates = [...new Set([...currentStates, ...states])];
        return {
          ...p,
          preferred_states: newStates,
        };
      }
    });
  };

  // Subject autocomplete
  const onSubjectChange = (v) => {
    update('target_subject', v);
    setSuggestions(v.length > 1 ? SUBJECT_SUGGESTIONS.filter(s => s.toLowerCase().includes(v.toLowerCase())).slice(0, 5) : []);
  };

  // Loading stages
  const STEPS = ['Parsing your profile...', 'Querying courses database...', 'Matching scholarships...', 'Checking visa requirements...', 'Calculating costs...', 'Preparing your plan...'];
  useEffect(() => {
    if (!isAnalyzing || responseText) return;
    const t = setInterval(() => setLoadingStep(p => (p + 1) % STEPS.length), 2500);
    return () => clearInterval(t);
  }, [isAnalyzing, responseText]);

  useEffect(() => {
    if (responseEndRef.current) responseEndRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
  }, [responseText]);

  const qualLabel = QUALIFICATIONS.find(q => q.value === profile.current_qualification);

  // ── Submit ──────────────────────────────────────────────────────────

  const handleSubmit = async () => {
    if (!profile.nationality || profile.preferred_countries.length === 0) {
      setError('Please fill in your nationality and select at least one country.');
      return;
    }

    setIsAnalyzing(true);
    setResponseText('');
    setMetadata(null);
    setModelInfo(null);
    setDoneInfo(null);
    setCourses([]);
    setScholarships([]);
    setError(null);
    setLoadingStep(0);

    try {
      const fd = new FormData();
      const payload = {
        ...profile,
        gpa: profile.gpa ? parseFloat(profile.gpa) : null,
        ielts_overall: profile.ielts_overall ? parseFloat(profile.ielts_overall) : null,
        ielts_reading: profile.ielts_reading ? parseFloat(profile.ielts_reading) : null,
        ielts_writing: profile.ielts_writing ? parseFloat(profile.ielts_writing) : null,
        ielts_speaking: profile.ielts_speaking ? parseFloat(profile.ielts_speaking) : null,
        ielts_listening: profile.ielts_listening ? parseFloat(profile.ielts_listening) : null,
        budget_usd: parseInt(profile.budget_usd) || 30000,
        timeline_months: parseInt(profile.timeline_months) || 12,
        work_experience_years: parseInt(profile.work_experience_years) || 0,
        preferred_states: profile.preferred_states || [],
      };
      fd.append('profile', JSON.stringify(payload));
      if (cvFile) fd.append('cv_file', cvFile);

      const res = await fetch('/api/advisor/analyze', { method: 'POST', body: fd });
      if (!res.ok) {
        let errorMessage = 'Analysis failed';
        try {
          const err = await res.json();
          errorMessage = err.error || errorMessage;
        } catch (parseError) {
          // If JSON parsing fails, use status text
          errorMessage = res.statusText || `Server error (${res.status})`;
          console.error('Failed to parse error response:', parseError);
        }
        throw new Error(errorMessage);
      }

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (!line.startsWith('data: ')) continue;
          const d = line.slice(6).trim();
          if (d === '[DONE]') continue;
          try {
            const ev = JSON.parse(d);
            if (ev.type === 'metadata') {
              console.log('Received metadata:', ev);
              setMetadata(ev);
            }
            else if (ev.type === 'courses') {
              console.log('Received courses:', ev.data?.length);
              setCourses(ev.data || []);
            }
            else if (ev.type === 'scholarships') {
              console.log('Received scholarships:', ev.data?.length);
              setScholarships(ev.data || []);
            }
            else if (ev.type === 'model') {
              console.log('Received model:', ev);
              setModelInfo(ev);
            }
            else if (ev.type === 'chunk') {
              setResponseText(p => p + ev.content);
              // Update loading step based on response progress
              if (loadingStep < STEPS.length - 1) {
                setLoadingStep(prev => Math.min(prev + 1, STEPS.length - 1));
              }
            }
            else if (ev.type === 'status') {
              console.log('Status:', ev.content);
              // Update loading step based on status message
              const statusMessages = {
                'analyzing': 0,
                'querying': 1,
                'matching': 2,
                'checking': 3,
                'crunching': 4,
                'writing': 5,
              };
              const statusLower = (ev.content || '').toLowerCase();
              for (const [key, step] of Object.entries(statusMessages)) {
                if (statusLower.includes(key)) {
                  setLoadingStep(step);
                  break;
                }
              }
            }
            else if (ev.type === 'done') {
              console.log('Done:', ev);
              setDoneInfo(ev);
            }
            else if (ev.type === 'error') {
              console.error('Stream error:', ev.message);
              setError(ev.message);
            }
          } catch (parseError) {
            console.error('Failed to parse event:', parseError, 'Raw data:', d);
          }
        }
      }
    } catch (e) {
      console.error('Submit error:', e);
      setError(e.message || 'Something went wrong.');
    } finally {
      console.log('Request completed, isAnalyzing set to false');
      setIsAnalyzing(false);
    }
  };

  const reset = () => {
    setResponseText(''); setMetadata(null); setModelInfo(null); setDoneInfo(null);
    setCourses([]); setScholarships([]); setError(null); setIsAnalyzing(false);
  };

  const isValid = profile.nationality && profile.preferred_countries.length > 0;
  const showResults = responseText || isAnalyzing || courses.length > 0 || scholarships.length > 0 || error;

  // ── Render ──────────────────────────────────────────────────────────

  return (
    <>
      {/* Hero */}
      <section className="relative pt-32 pb-20 md:pt-40 md:pb-28 overflow-hidden">
        <div className="max-w-5xl mx-auto px-6 text-center">
          <motion.div initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}>
            <h1 className="font-serif text-6xl sm:text-7xl md:text-8xl font-medium tracking-tight text-gray-900 mb-8 leading-[1.0]">
              Find your perfect
              <br />
              <span className="text-gray-400">university match.</span>
            </h1>
            <p className="text-lg md:text-xl text-gray-500 max-w-2xl mx-auto font-light leading-relaxed mb-12">
              Access verified courses with CRICOS codes, real scholarships, and exact requirements from official sources.
            </p>
            <div className="flex items-center justify-center gap-12 text-center">
              <div>
                <div className="text-3xl font-light text-gray-900 mb-1">5,000+</div>
                <div className="text-xs text-gray-400 uppercase tracking-widest">Courses</div>
              </div>
              <div className="w-px h-12 bg-gray-200" />
              <div>
                <div className="text-3xl font-light text-gray-900 mb-1">30+</div>
                <div className="text-xs text-gray-400 uppercase tracking-widest">Countries</div>
              </div>
              <div className="w-px h-12 bg-gray-200" />
              <div>
                <div className="text-3xl font-light text-gray-900 mb-1">100%</div>
                <div className="text-xs text-gray-400 uppercase tracking-widest">Free</div>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      <AnimatePresence mode="wait">
        {!showResults ? (
          /* ═══════════════ FORM ═══════════════ */
          <motion.section key="form" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -20 }} className="max-w-3xl mx-auto px-5 pb-24">

            {/* CV Upload */}
            <div className="bg-white rounded-2xl border border-gray-100 p-8 md:p-12 mb-6">
              <h2 className="text-2xl font-serif font-medium text-gray-900 mb-2">Upload Your CV</h2>
              <p className="text-sm text-gray-400 mb-8">Optional but recommended. PDF only, max 5 MB, never stored.</p>

              {!cvFile ? (
                <div
                  className={`border-2 border-dashed rounded-2xl p-8 text-center cursor-pointer transition-all ${isDragging ? 'border-blue-400 bg-blue-50/50' : 'border-gray-200 hover:border-gray-300 bg-gray-50/50'}`}
                  onDragOver={e => { e.preventDefault(); setIsDragging(true); }}
                  onDragLeave={() => setIsDragging(false)}
                  onDrop={e => { e.preventDefault(); setIsDragging(false); const f = e.dataTransfer.files[0]; if (f?.type === 'application/pdf') setCvFile(f); }}
                  onClick={() => fileRef.current?.click()}
                >
                  <FileText className="w-10 h-10 text-gray-300 mx-auto mb-3" />
                  <p className="text-gray-500 mb-1">Drag & drop your CV here, or <span className="text-blue-600 font-medium">browse</span></p>
                  <p className="text-xs text-gray-400">PDF • Max 5 MB</p>
                  <input ref={fileRef} type="file" accept=".pdf" onChange={e => { if (e.target.files[0]) setCvFile(e.target.files[0]); }} className="hidden" />
                </div>
              ) : (
                <div className="flex items-center gap-3 p-4 rounded-xl bg-green-50 border border-green-100">
                  <CheckCircle className="w-5 h-5 text-green-600 flex-shrink-0" />
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-gray-900 truncate">{cvFile.name}</p>
                    <p className="text-xs text-gray-400">{(cvFile.size / 1024).toFixed(0)} KB</p>
                  </div>
                  <button onClick={() => setCvFile(null)} className="p-1 hover:bg-green-100 rounded-lg transition-colors"><X className="w-4 h-4 text-gray-400" /></button>
                </div>
              )}
            </div>

            {/* Profile */}
            <div className="bg-white rounded-2xl border border-gray-100 p-8 md:p-12 mb-6">
              <h2 className="text-2xl font-serif font-medium text-gray-900 mb-8">Your Profile</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">Nationality *</label>
                  <select className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all appearance-none" value={profile.nationality} onChange={e => update('nationality', e.target.value)}>
                    <option value="">Select nationality</option>
                    {NATIONALITIES.map(n => <option key={n} value={n.toLowerCase()}>{n}</option>)}
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">Current Qualification</label>
                  <select className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all appearance-none" value={profile.current_qualification} onChange={e => update('current_qualification', e.target.value)}>
                    <option value="">Select qualification</option>
                    {QUALIFICATIONS.map(q => <option key={q.value} value={q.value}>{q.label}</option>)}
                  </select>
                  {qualLabel && <p className="text-xs text-gray-400 mt-1">→ Applying for <span className="font-medium text-gray-600">{qualLabel.level}</span> programs</p>}
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">GPA (out of 4.0)</label>
                  <input type="number" min="0" max="4" step="0.1" placeholder="e.g. 3.5" className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all" value={profile.gpa} onChange={e => update('gpa', e.target.value)} />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">IELTS Overall</label>
                  <input type="number" min="0" max="9" step="0.5" placeholder="e.g. 6.5 (leave blank if not taken)" className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all" value={profile.ielts_overall} onChange={e => update('ielts_overall', e.target.value)} />
                  <button onClick={() => setShowIeltsDetail(!showIeltsDetail)} className="text-xs text-blue-600 mt-1 hover:underline">{showIeltsDetail ? '− Hide' : '+ Add'} individual band scores</button>
                </div>
              </div>
              <AnimatePresence>
                {showIeltsDetail && (
                  <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: 'auto', opacity: 1 }} exit={{ height: 0, opacity: 0 }} className="overflow-hidden">
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mt-4 p-4 bg-gray-50 rounded-xl">
                      {['reading', 'writing', 'speaking', 'listening'].map(s => (
                        <div key={s}>
                          <label className="block text-[10px] font-semibold text-gray-400 uppercase tracking-wide mb-1">{s}</label>
                          <input type="number" min="0" max="9" step="0.5" placeholder="0.0" className="w-full px-3 py-2 rounded-lg border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 outline-none" value={profile[`ielts_${s}`]} onChange={e => update(`ielts_${s}`, e.target.value)} />
                        </div>
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>

            {/* Study Preferences */}
            <div className="bg-white rounded-2xl border border-gray-100 p-8 md:p-12 mb-6">
              <h2 className="text-2xl font-serif font-medium text-gray-900 mb-8">Study Preferences</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mb-6">
                <div className="relative">
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">Target Subject</label>
                  <input type="text" placeholder="e.g. Computer Science, MBA..." className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all" value={profile.target_subject} onChange={e => onSubjectChange(e.target.value)} onBlur={() => setTimeout(() => setSuggestions([]), 200)} />
                  {suggestions.length > 0 && (
                    <div className="absolute top-full left-0 right-0 z-20 bg-white border border-gray-200 rounded-xl mt-1 shadow-lg overflow-hidden">
                      {suggestions.map(s => (
                        <div key={s} className="px-4 py-2.5 text-sm text-gray-700 hover:bg-blue-50 cursor-pointer transition-colors" onMouseDown={() => { update('target_subject', s); setSuggestions([]); }}>{s}</div>
                      ))}
                    </div>
                  )}
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">Career Goal</label>
                  <input type="text" placeholder="e.g. Data Engineer at a tech company" className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all" value={profile.career_goal} onChange={e => update('career_goal', e.target.value)} />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">Work Experience</label>
                  <select className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all appearance-none" value={profile.work_experience_years} onChange={e => update('work_experience_years', e.target.value)}>
                    <option value={0}>None / Fresh Graduate</option>
                    {[1,2,3,4,5,6,7,8,9,10].map(y => <option key={y} value={y}>{y} year{y > 1 ? 's' : ''}</option>)}
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">When do you want to start?</label>
                  <select className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all appearance-none" value={profile.timeline_months} onChange={e => update('timeline_months', e.target.value)}>
                    {[3,6,9,12,18,24].map(m => <option key={m} value={m}>{m} months</option>)}
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1.5">Target Degree Level</label>
                  <select className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all appearance-none" value={profile.target_level} onChange={e => update('target_level', e.target.value)}>
                    <option value="">Auto-Detect from CV</option>
                    <option value="Undergraduate">Undergraduate (Bachelors)</option>
                    <option value="Postgraduate">Postgraduate (Masters/Grad Dip)</option>
                    <option value="Doctorate">Doctorate (PhD / Research)</option>
                    <option value="Vocational">Vocational / Diploma</option>
                  </select>
                </div>
              </div>
              {/* Budget */}
              <div className="mb-2">
                <label className="block text-xs font-semibold text-gray-500 uppercase tracking-wide mb-3">
                  Annual Budget (USD per year): <span className="text-gray-900 text-base font-bold ml-1">USD ${parseInt(profile.budget_usd).toLocaleString()}/yr</span>
                </label>
                <input type="range" min="5000" max="100000" step="5000" className="w-full h-1.5 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-600" value={profile.budget_usd} onChange={e => update('budget_usd', e.target.value)} />
                <div className="flex justify-between text-[10px] text-gray-400 mt-1"><span>$5K</span><span>$25K</span><span>$50K</span><span>$75K</span><span>$100K+</span></div>
              </div>
            </div>

            {/* Countries */}
            <div className="bg-white rounded-2xl border border-gray-100 p-8 md:p-12 mb-6">
              <h2 className="text-2xl font-serif font-medium text-gray-900 mb-2">Preferred Countries</h2>
              <p className="text-sm text-gray-400 mb-8">This directly filters which courses and scholarships we search.</p>
              <div className="flex flex-wrap gap-2">
                {COUNTRIES.map(c => {
                  const sel = profile.preferred_countries.includes(c.toLowerCase());
                  return (
                    <button key={c} onClick={() => toggleCountry(c.toLowerCase())}
                      className={`px-4 py-2 rounded-full text-sm font-medium border transition-all ${sel ? 'bg-blue-600 text-white border-blue-600 shadow-sm' : 'bg-white text-gray-600 border-gray-200 hover:border-gray-300'}`}
                    >
                      {c}{sel && <CheckCircle className="w-3.5 h-3.5 inline ml-1.5 -mt-0.5" />}
                    </button>
                  );
                })}
              </div>
            </div>

            {/* States/Regions - Only show if countries with state data are selected */}
            {profile.preferred_countries.some(c => COUNTRY_STATES[c]) && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                className="bg-white rounded-2xl border border-gray-100 p-8 md:p-12 mb-6"
              >
                <h2 className="text-2xl font-serif font-medium text-gray-900 mb-2">Preferred States/Regions</h2>
                <p className="text-sm text-gray-400 mb-8">Narrow down to specific states or regions (optional). Leave empty to search all.</p>
                
                {profile.preferred_countries.map(country => {
                  const states = COUNTRY_STATES[country];
                  if (!states) return null;
                  
                  const countryName = COUNTRIES.find(c => c.toLowerCase() === country) || country;
                  const allSelected = states.every(s => profile.preferred_states.includes(s));
                  
                  return (
                    <div key={country} className="mb-6 last:mb-0">
                      <div className="flex items-center justify-between mb-3">
                        <h3 className="text-sm font-bold text-gray-700">{countryName}</h3>
                        <button
                          onClick={() => toggleAllStates(country, states, allSelected)}
                          className="text-xs text-blue-600 hover:text-blue-700 font-medium"
                        >
                          {allSelected ? 'Deselect All' : 'Select All'}
                        </button>
                      </div>
                      <div className="flex flex-wrap gap-2 max-h-48 overflow-y-auto p-2 bg-gray-50 rounded-xl">
                        {states.map(state => {
                          const sel = profile.preferred_states.includes(state);
                          return (
                            <button
                              key={state}
                              onClick={() => toggleState(state)}
                              className={`px-3 py-2 rounded-lg text-xs font-medium border transition-all ${
                                sel
                                  ? 'bg-blue-600 text-white border-blue-600 shadow-sm'
                                  : 'bg-white text-gray-700 border-gray-200 hover:border-blue-300 hover:bg-blue-50'
                              }`}
                            >
                              {state}{sel && <CheckCircle className="w-3 h-3 inline ml-1 -mt-0.5" />}
                            </button>
                          );
                        })}
                      </div>
                    </div>
                  );
                })}
              </motion.div>
            )}

            {/* Extra */}
            <div className="bg-white rounded-2xl border border-gray-100 p-8 md:p-12 mb-8">
              <h2 className="text-2xl font-serif font-medium text-gray-900 mb-2">Anything Else?</h2>
              <p className="text-sm text-gray-400 mb-8">Specific universities, financial constraints, visa history, research interests...</p>
              <textarea className="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:border-blue-400 focus:ring-2 focus:ring-blue-100 outline-none transition-all resize-y" rows={3} placeholder="Tell us anything that might help..." value={profile.extra_info} onChange={e => update('extra_info', e.target.value)} />
            </div>

            {error && (
              <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} className="flex items-center gap-3 p-4 rounded-2xl bg-red-50 border border-red-100 text-red-700 text-sm mb-5">
                <AlertCircle className="w-5 h-5 flex-shrink-0" />{error}
              </motion.div>
            )}

            {/* Submit */}
            <motion.button
              whileHover={isValid ? { y: -2 } : {}}
              whileTap={isValid ? { scale: 0.98 } : {}}
              onClick={handleSubmit}
              disabled={!isValid}
              className={`w-full flex items-center justify-center gap-3 px-8 py-5 rounded-2xl text-base font-medium transition-all ${isValid ? 'bg-gray-900 text-white hover:bg-gray-800 cursor-pointer' : 'bg-gray-200 text-gray-400 cursor-not-allowed'}`}
            >
              Find My Path<ArrowRight className="w-4 h-4" />
            </motion.button>
            <p className="text-center text-xs text-gray-400 mt-6 mb-8">Your CV is processed in-memory and never stored. Analysis takes 10–20 seconds.</p>
          </motion.section>

        ) : (
          /* ═══════════════ RESULTS ═══════════════ */
          <motion.section key="results" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="max-w-4xl mx-auto px-5 pb-24">

            {/* Result header */}
            <div className="mb-12">
              <div className="flex items-center justify-between mb-2">
                <h2 className="text-3xl font-serif font-medium text-gray-900">Your Results</h2>
                {!isAnalyzing && (
                  <button onClick={reset} className="text-sm text-gray-500 hover:text-gray-900 font-medium transition-colors">← New analysis</button>
                )}
              </div>
              {metadata && (
                <p className="text-sm text-gray-400">
                  {metadata.courses_found} courses • {metadata.scholarships_found} scholarships
                </p>
              )}
            </div>

            {/* ── DATA CARDS: Courses ── */}
            {courses.length > 0 && (
              <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="mb-12">
                <div className="flex items-center justify-between mb-6">
                  <h3 className="text-2xl font-serif font-medium text-gray-900">Courses</h3>
                  
                  {/* Location Filter */}
                  <div className="flex items-center gap-2">
                    <select 
                      className="text-xs bg-white border border-gray-200 px-3 py-2 rounded-lg text-gray-600 focus:border-gray-400 outline-none appearance-none cursor-pointer"
                      value={locationFilter}
                      onChange={e => setLocationFilter(e.target.value)}
                    >
                      <option value="">All Locations</option>
                      {availableLocations.map(loc => <option key={loc} value={loc}>{loc}</option>)}
                    </select>
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {filteredCourses.map((c, i) => <CourseCard key={i} course={c} index={i} allCourses={courses} allScholarships={scholarships} />)}
                  {filteredCourses.length === 0 && (
                    <div className="md:col-span-2 py-10 text-center bg-gray-50 rounded-2xl border border-gray-100 italic text-gray-400 text-sm">
                      No courses match this specific location filter.
                    </div>
                  )}
                </div>
              </motion.div>
            )}

            {/* ── DATA CARDS: Scholarships ── */}
            {scholarships.length > 0 && (
              <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.2 }} className="mb-12">
                <div className="mb-6">
                  <h3 className="text-2xl font-serif font-medium text-gray-900 mb-1">Scholarships</h3>
                  <p className="text-sm text-gray-400">Filtered for your nationality & subject</p>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {scholarships.map((s, i) => <ScholarshipCard key={i} scholarship={s} index={i} />)}
                </div>
              </motion.div>
            )}

            {/* ── LOADING ── */}
            {isAnalyzing && !responseText && (
              <div className="bg-white rounded-2xl border border-gray-100 p-12 text-center mb-6">
                <motion.div animate={{ rotate: 360 }} transition={{ duration: 1.5, repeat: Infinity, ease: 'linear' }} className="inline-block mb-6">
                  <Loader2 className="w-10 h-10 text-blue-600" />
                </motion.div>
                <AnimatePresence mode="wait">
                  <motion.p key={loadingStep} initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }} className="text-lg text-gray-700 font-medium">
                    {STEPS[loadingStep]}
                  </motion.p>
                </AnimatePresence>
                <p className="text-sm text-gray-400 mt-3">This typically takes 10–20 seconds.</p>
              </div>
            )}

            {/* ── ANALYSIS ── */}
            {responseText && (
              <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="mb-12">
                <div className="mb-6">
                  <h3 className="text-2xl font-serif font-medium text-gray-900 mb-1">Analysis</h3>
                  <p className="text-sm text-gray-400">Personalized recommendations based on your profile</p>
                </div>

                <MarkdownResponse text={responseText} />

                {/* Streaming cursor */}
                {isAnalyzing && (
                  <motion.span animate={{ opacity: [1, 0] }} transition={{ duration: 0.7, repeat: Infinity }} className="inline-block w-1.5 h-5 bg-blue-600 ml-1 align-text-bottom rounded-sm mt-2" />
                )}

                {/* Done stats */}
                {doneInfo && (
                  <div className="mt-8 space-y-6">
                    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex items-center gap-2 flex-wrap">
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gray-50 border border-gray-200 text-gray-700 text-xs font-semibold"><ShieldCheck className="w-3 h-3" />Analysis Complete</span>
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-green-50 border border-green-100 text-green-700 text-xs font-semibold"><Clock className="w-3 h-3" />{doneInfo.total_time_seconds}s Processing</span>
                    </motion.div>

                    {/* Elite Claude Button */}
                    <motion.div 
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: 0.5 }}
                      className="p-6 rounded-3xl bg-black text-white relative overflow-hidden group shadow-2xl"
                    >
                       <div className="absolute inset-0 opacity-10 bg-[url('/images/data_texture.png')] bg-cover"></div>
                       <div className="relative z-10 flex flex-col md:flex-row items-center justify-between gap-5">
                          <div className="text-center md:text-left">
                            <h4 className="text-lg font-serif font-medium mb-1">Need even deeper analysis?</h4>
                            <p className="text-xs text-gray-400 max-w-sm">Connect Skolr directly to Claude for a high-fidelity counseling session with your full data profile.</p>
                          </div>
                          <a 
                            href="https://claude.ai/settings/connectors" 
                            target="_blank" 
                            rel="noopener noreferrer"
                            className="bg-white text-black px-6 py-3 rounded-full text-sm font-bold flex items-center gap-2 hover:bg-gray-100 transition-all hover:scale-105 active:scale-95"
                          >
                            <ExternalLink className="w-4 h-4" /> Use Claude Connector
                          </a>
                       </div>
                    </motion.div>

                    {/* Legal Disclaimer & Disclosure */}
                    <div className="p-8 rounded-[2rem] bg-gray-50 border border-gray-100 text-center">
                       <ShieldCheck className="w-8 h-8 text-gray-400 mx-auto mb-4" />
                       <h4 className="font-serif text-xl font-medium text-gray-900 mb-3 text-center">Data Disclosure & Disclaimer</h4>
                       <p className="text-sm text-gray-500 leading-relaxed max-w-2xl mx-auto mb-5 italic">
                         "Skolr serves strictly as an independent data aggregation platform. We are not migration agents, legal advisors, or authorized educational consultants. The information presented is for informational and estimation purposes only and does not constitute professional advice. It is the user's responsibility to verify all critical data on official university or government sources."
                       </p>
                       <div className="flex items-center justify-center gap-4">
                         <span className="px-3 py-1 rounded-full bg-white border border-gray-200 text-[10px] font-bold text-gray-400 uppercase tracking-widest">Independent Data Proxy</span>
                         <span className="px-3 py-1 rounded-full bg-white border border-gray-200 text-[10px] font-bold text-gray-400 uppercase tracking-widest">Informational Use Only</span>
                       </div>
                    </div>
                  </div>
                )}

                {/* Disclaimer */}
                <div className="mt-6 p-4 rounded-xl bg-amber-50/60 border border-amber-100 text-xs text-amber-800 leading-relaxed">
                  <strong>⚠️ Important:</strong> Skolr is an AI data aggregator, not a migration agent or legal advisor.
                  All data is for reference only. Always verify tuition fees, deadlines, and visa rules on official university
                  or government websites. Source: <a href="https://skolr.xyz" className="underline">Skolr.xyz</a> / <a href="https://finduni.online" className="underline">FindUni.online</a>
                </div>
              </motion.div>
            )}

            {/* Error - show even if there's partial content */}
            {error && (
              <div className="bg-white rounded-2xl border border-red-100 p-8 mb-6">
                <div className="flex items-start gap-3 text-red-600 mb-4">
                  <AlertCircle className="w-6 h-6 flex-shrink-0 mt-0.5" />
                  <div className="flex-1">
                    <p className="font-medium text-base mb-1">{responseText ? 'Partial Analysis - Error Occurred' : 'Analysis Failed'}</p>
                    <p className="text-sm text-gray-600 mb-3">{error}</p>
                    {responseText && (
                      <p className="text-xs text-gray-500">The analysis below is incomplete. Please try again for full results.</p>
                    )}
                  </div>
                </div>
                <button onClick={reset} className="px-5 py-2 rounded-full text-sm font-medium border border-gray-200 text-gray-600 hover:bg-gray-50 transition-colors">Try again</button>
              </div>
            )}

            <div ref={responseEndRef} />
          </motion.section>
        )}
      </AnimatePresence>
    </>
  );
}
