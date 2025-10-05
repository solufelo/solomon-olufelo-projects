"""
Salary parsing and filtering utilities
Handles various salary formats and provides filtering capabilities
"""

import re
import logging
from typing import Optional, Tuple, Dict, List

logger = logging.getLogger(__name__)

class SalaryParser:
    """Parse and normalize salary information from job postings"""
    
    def __init__(self):
        # Salary patterns for different formats
        self.salary_patterns = [
            # Hourly rates
            r'\$(\d+(?:\.\d{2})?)\s*(?:to|-)?\s*\$?(\d+(?:\.\d{2})?)\s*(?:per\s*)?(?:hour|hr|hourly)',
            r'\$(\d+(?:\.\d{2})?)\s*(?:per\s*)?(?:hour|hr|hourly)',
            
            # Annual salaries
            r'\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:to|-)?\s*\$?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:per\s*)?(?:year|annual|annually)',
            r'\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:per\s*)?(?:year|annual|annually)',
            
            # K format (e.g., $50K, $40K-60K)
            r'\$(\d+)k?\s*(?:to|-)?\s*\$?(\d+)k\s*(?:per\s*)?(?:year|annual|annually)?',
            r'\$(\d+)k\s*(?:per\s*)?(?:year|annual|annually)?',
            
            # Range without specific period
            r'\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:to|-)?\s*\$?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)',
            
            # Monthly
            r'\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:to|-)?\s*\$?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:per\s*)?(?:month|monthly)',
            r'\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:per\s*)?(?:month|monthly)',
        ]
        
        # Words that indicate negotiable/flexible salary
        self.negotiable_keywords = [
            'negotiable', 'competitive', 'commensurate', 'dependent on experience',
            'doe', 'tbd', 'to be determined', 'flexible', 'open'
        ]
    
    def parse_salary(self, salary_text: str) -> Dict:
        """
        Parse salary text and return normalized information
        
        Returns:
            Dict with keys: min_amount, max_amount, period, currency, is_range, is_negotiable, raw_text
        """
        if not salary_text:
            return {}
        
        salary_text = salary_text.lower().strip()
        
        # Check if salary is negotiable
        is_negotiable = any(keyword in salary_text for keyword in self.negotiable_keywords)
        
        result = {
            'raw_text': salary_text,
            'is_negotiable': is_negotiable,
            'currency': 'CAD',  # Assume CAD for Canadian job sites
            'min_amount': None,
            'max_amount': None,
            'period': None,
            'is_range': False
        }
        
        # Try to extract salary amounts
        for pattern in self.salary_patterns:
            match = re.search(pattern, salary_text, re.IGNORECASE)
            if match:
                try:
                    groups = match.groups()
                    
                    # Determine period from pattern
                    if 'hour' in pattern or 'hr' in pattern:
                        result['period'] = 'hourly'
                    elif 'year' in pattern or 'annual' in pattern:
                        result['period'] = 'annually'
                    elif 'month' in pattern:
                        result['period'] = 'monthly'
                    else:
                        # Try to infer from the text context
                        if any(word in salary_text for word in ['hour', 'hr', 'hourly']):
                            result['period'] = 'hourly'
                        elif any(word in salary_text for word in ['year', 'annual', 'annually']):
                            result['period'] = 'annually'
                        elif any(word in salary_text for word in ['month', 'monthly']):
                            result['period'] = 'monthly'
                        else:
                            # Default assumption based on amount
                            amount1 = self._parse_amount(groups[0])
                            if amount1 and amount1 < 100:
                                result['period'] = 'hourly'
                            elif amount1 and amount1 > 1000:
                                result['period'] = 'annually'
                            else:
                                result['period'] = 'hourly'  # Default
                    
                    # Parse amounts
                    if len(groups) >= 1 and groups[0]:
                        result['min_amount'] = self._parse_amount(groups[0])
                        
                        if len(groups) >= 2 and groups[1]:
                            result['max_amount'] = self._parse_amount(groups[1])
                            result['is_range'] = True
                        else:
                            result['max_amount'] = result['min_amount']
                    
                    # Handle K format
                    if 'k' in pattern.lower():
                        if result['min_amount']:
                            result['min_amount'] *= 1000
                        if result['max_amount']:
                            result['max_amount'] *= 1000
                    
                    break
                    
                except (ValueError, AttributeError) as e:
                    logger.debug(f"Error parsing salary pattern: {e}")
                    continue
        
        return result
    
    def _parse_amount(self, amount_str: str) -> Optional[float]:
        """Parse amount string to float"""
        if not amount_str:
            return None
        
        try:
            # Remove commas and currency symbols
            cleaned = re.sub(r'[,$]', '', amount_str.strip())
            return float(cleaned)
        except ValueError:
            return None
    
    def normalize_to_annual(self, salary_data: Dict) -> Dict:
        """Convert salary to annual equivalent for comparison"""
        if not salary_data or not salary_data.get('min_amount'):
            return salary_data
        
        result = salary_data.copy()
        period = salary_data.get('period', 'annually')
        
        if period == 'hourly':
            # Assume 40 hours/week, 52 weeks/year
            multiplier = 40 * 52
            if result['min_amount']:
                result['min_annual'] = result['min_amount'] * multiplier
            if result['max_amount']:
                result['max_annual'] = result['max_amount'] * multiplier
        elif period == 'monthly':
            multiplier = 12
            if result['min_amount']:
                result['min_annual'] = result['min_amount'] * multiplier
            if result['max_amount']:
                result['max_annual'] = result['max_amount'] * multiplier
        else:  # annually
            result['min_annual'] = result['min_amount']
            result['max_annual'] = result['max_amount']
        
        return result
    
    def filter_jobs_by_salary(self, jobs: List[Dict], min_salary: Optional[float] = None, 
                             max_salary: Optional[float] = None, salary_period: str = 'annually') -> List[Dict]:
        """
        Filter jobs based on salary criteria
        
        Args:
            jobs: List of job dictionaries
            min_salary: Minimum salary requirement
            max_salary: Maximum salary limit
            salary_period: Period for comparison ('hourly', 'annually', 'monthly')
        
        Returns:
            Filtered list of jobs
        """
        if not min_salary and not max_salary:
            return jobs
        
        filtered_jobs = []
        
        for job in jobs:
            salary_text = job.get('salary', '')
            if not salary_text or salary_text.lower() in ['not specified', 'n/a', '']:
                # Include jobs without salary info if no strict filtering
                if not min_salary or not max_salary:
                    filtered_jobs.append(job)
                continue
            
            # Parse job salary
            salary_data = self.parse_salary(salary_text)
            if not salary_data or not salary_data.get('min_amount'):
                continue
            
            # Normalize to comparison period
            if salary_period == 'annually':
                normalized = self.normalize_to_annual(salary_data)
                job_min = normalized.get('min_annual')
                job_max = normalized.get('max_annual')
            else:
                # Convert user criteria to job's period for comparison
                job_period = salary_data.get('period', 'annually')
                if job_period == salary_period:
                    job_min = salary_data.get('min_amount')
                    job_max = salary_data.get('max_amount')
                else:
                    # Different periods, normalize both to annual
                    normalized = self.normalize_to_annual(salary_data)
                    job_min = normalized.get('min_annual')
                    job_max = normalized.get('max_annual')
                    
                    # Convert user criteria to annual
                    if salary_period == 'hourly':
                        user_min = min_salary * 40 * 52 if min_salary else None
                        user_max = max_salary * 40 * 52 if max_salary else None
                    elif salary_period == 'monthly':
                        user_min = min_salary * 12 if min_salary else None
                        user_max = max_salary * 12 if max_salary else None
                    else:
                        user_min = min_salary
                        user_max = max_salary
                    
                    min_salary = user_min
                    max_salary = user_max
            
            if not job_min:
                continue
            
            # Check if job salary meets criteria
            meets_criteria = True
            
            if min_salary and job_max and job_max < min_salary:
                meets_criteria = False
            
            if max_salary and job_min and job_min > max_salary:
                meets_criteria = False
            
            if meets_criteria:
                # Add parsed salary info to job for display
                job['parsed_salary'] = salary_data
                filtered_jobs.append(job)
        
        logger.info(f"Salary filtering: {len(jobs)} -> {len(filtered_jobs)} jobs")
        return filtered_jobs

# Singleton instance
salary_parser = SalaryParser() 