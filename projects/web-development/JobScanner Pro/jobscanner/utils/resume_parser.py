"""
Advanced Resume Parser with NLP capabilities
Extracts skills, experience, and keywords from resumes in various formats
"""

import os
import re
import logging
from pathlib import Path
from typing import List, Dict, Set, Optional, Tuple
import json

# Document processing
try:
    import docx
    from PyPDF2 import PdfReader
    import textract
except ImportError:
    docx = None
    PdfReader = None
    textract = None

# NLP libraries
try:
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.corpus import stopwords
    from nltk.tag import pos_tag
    from nltk.chunk import ne_chunk
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False

try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False

logger = logging.getLogger(__name__)

class ResumeParser:
    """Advanced resume parser with NLP-powered keyword extraction"""
    
    def __init__(self):
        """Initialize the resume parser with NLP models"""
        self.nlp_model = None
        self.setup_nlp()
        
        # Skills database for creative/tech roles
        self.skills_database = self._load_skills_database()
        
        # Experience patterns
        self.experience_patterns = [
            r'(\d+)[\+\-\s]*(?:years?|yrs?)\s*(?:of\s*)?(?:experience|exp)',
            r'(\d+)[\+\-\s]*(?:to|-)[\+\-\s]*(\d+)\s*(?:years?|yrs?)',
            r'(?:over|more than|above)\s*(\d+)\s*(?:years?|yrs?)',
            r'(\d+)[\+\-\s]*(?:year|yr)\s*(?:experience|exp)',
        ]
        
    def setup_nlp(self):
        """Setup NLP libraries and models"""
        try:
            # Try to load spaCy model
            if SPACY_AVAILABLE:
                try:
                    self.nlp_model = spacy.load("en_core_web_sm")
                    logger.info("Loaded spaCy model successfully")
                except OSError:
                    logger.warning("spaCy English model not found. Install with: python -m spacy download en_core_web_sm")
                    self.nlp_model = None
            
            # Setup NLTK
            if NLTK_AVAILABLE:
                self._download_nltk_data()
                
        except Exception as e:
            logger.error(f"Error setting up NLP: {e}")
    
    def _download_nltk_data(self):
        """Download required NLTK data"""
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
            
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
            
        try:
            nltk.data.find('taggers/averaged_perceptron_tagger')
        except LookupError:
            nltk.download('averaged_perceptron_tagger')
            
        try:
            nltk.data.find('chunkers/maxent_ne_chunker')
        except LookupError:
            nltk.download('maxent_ne_chunker')
            
        try:
            nltk.data.find('corpora/words')
        except LookupError:
            nltk.download('words')
    
    def _load_skills_database(self) -> Dict[str, Set[str]]:
        """Load comprehensive skills database for different categories"""
        return {
            "design_software": {
                "adobe photoshop", "photoshop", "adobe illustrator", "illustrator", 
                "adobe indesign", "indesign", "figma", "sketch", "canva", "adobe xd", 
                "framer", "principle", "invision", "zeplin", "adobe after effects", 
                "after effects", "adobe premiere", "premiere pro", "cinema 4d", 
                "blender", "maya", "3ds max", "autocad", "solidworks"
            },
            "design_skills": {
                "ui design", "ux design", "user interface", "user experience", 
                "graphic design", "web design", "logo design", "branding", 
                "typography", "color theory", "layout design", "print design", 
                "digital design", "visual design", "brand identity", "packaging design",
                "motion graphics", "animation", "illustration", "photo editing",
                "image retouching", "digital art", "concept art", "storyboarding"
            },
            "web_technologies": {
                "html", "html5", "css", "css3", "javascript", "jquery", "react", 
                "angular", "vue", "node.js", "php", "python", "wordpress", "drupal",
                "shopify", "woocommerce", "bootstrap", "sass", "less", "responsive design",
                "mobile design", "cross-browser compatibility", "seo", "accessibility"
            },
            "marketing_skills": {
                "digital marketing", "social media marketing", "content marketing",
                "email marketing", "seo", "sem", "google ads", "facebook ads",
                "instagram marketing", "linkedin marketing", "content creation",
                "copywriting", "brand management", "campaign management",
                "marketing analytics", "google analytics", "conversion optimization"
            },
            "soft_skills": {
                "creative thinking", "problem solving", "attention to detail",
                "time management", "project management", "team collaboration",
                "communication", "presentation skills", "client relations",
                "multitasking", "deadline management", "adaptability", "leadership"
            },
            "industry_knowledge": {
                "print production", "prepress", "color management", "file preparation",
                "production workflow", "quality assurance", "client presentation",
                "design consultation", "brand guidelines", "style guides",
                "design systems", "user research", "usability testing", "wireframing",
                "prototyping", "information architecture"
            }
        }
    
    def extract_text_from_file(self, file_path: str) -> str:
        """Extract text from various file formats"""
        file_path = Path(file_path)
        
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            return ""
        
        try:
            file_extension = file_path.suffix.lower()
            
            if file_extension == '.pdf':
                return self._extract_from_pdf(str(file_path))
            elif file_extension in ['.docx', '.doc']:
                return self._extract_from_docx(str(file_path))
            elif file_extension == '.txt':
                return self._extract_from_txt(str(file_path))
            else:
                # Try textract for other formats
                if textract:
                    try:
                        return textract.process(str(file_path)).decode('utf-8')
                    except Exception as e:
                        logger.error(f"Textract failed for {file_path}: {e}")
                        return ""
                else:
                    logger.warning(f"Unsupported file format: {file_extension}")
                    return ""
                    
        except Exception as e:
            logger.error(f"Error extracting text from {file_path}: {e}")
            return ""
    
    def _extract_from_pdf(self, file_path: str) -> str:
        """Extract text from PDF file"""
        if not PdfReader:
            logger.error("PyPDF2 not available for PDF processing")
            return ""
        
        try:
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text
        except Exception as e:
            logger.error(f"Error reading PDF {file_path}: {e}")
            return ""
    
    def _extract_from_docx(self, file_path: str) -> str:
        """Extract text from DOCX file"""
        if not docx:
            logger.error("python-docx not available for DOCX processing")
            return ""
        
        try:
            doc = docx.Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            logger.error(f"Error reading DOCX {file_path}: {e}")
            return ""
    
    def _extract_from_txt(self, file_path: str) -> str:
        """Extract text from TXT file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='latin-1') as file:
                    return file.read()
            except Exception as e:
                logger.error(f"Error reading TXT {file_path}: {e}")
                return ""
        except Exception as e:
            logger.error(f"Error reading TXT {file_path}: {e}")
            return ""
    
    def extract_skills(self, text: str) -> Dict[str, List[str]]:
        """Extract categorized skills from resume text"""
        text_lower = text.lower()
        found_skills = {}
        
        for category, skills_set in self.skills_database.items():
            found_in_category = []
            for skill in skills_set:
                # Use regex for better matching
                pattern = r'\b' + re.escape(skill.lower()) + r'\b'
                if re.search(pattern, text_lower):
                    found_in_category.append(skill)
            
            if found_in_category:
                found_skills[category] = found_in_category
        
        return found_skills
    
    def extract_experience_years(self, text: str) -> Optional[int]:
        """Extract years of experience from resume text"""
        for pattern in self.experience_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                try:
                    if len(match.groups()) == 1:
                        return int(match.group(1))
                    elif len(match.groups()) == 2:
                        # Range like "3-5 years"
                        return int(match.group(2))  # Take the higher number
                except ValueError:
                    continue
        
        return None
    
    def extract_keywords_nlp(self, text: str) -> List[str]:
        """Extract keywords using NLP techniques"""
        keywords = set()
        
        # Method 1: spaCy-based extraction
        if self.nlp_model:
            keywords.update(self._extract_with_spacy(text))
        
        # Method 2: NLTK-based extraction
        if NLTK_AVAILABLE:
            keywords.update(self._extract_with_nltk(text))
        
        # Method 3: Custom pattern-based extraction
        keywords.update(self._extract_with_patterns(text))
        
        return list(keywords)
    
    def _extract_with_spacy(self, text: str) -> Set[str]:
        """Extract keywords using spaCy"""
        keywords = set()
        
        try:
            doc = self.nlp_model(text)
            
            # Extract named entities
            for ent in doc.ents:
                if ent.label_ in ['ORG', 'PRODUCT', 'LANGUAGE']:  # Organizations, products, languages
                    keywords.add(ent.text.lower())
            
            # Extract noun phrases and important terms
            for chunk in doc.noun_chunks:
                if len(chunk.text.split()) <= 3:  # Limit to 3-word phrases
                    keywords.add(chunk.text.lower())
            
            # Extract verbs and skills-related terms
            for token in doc:
                if (token.pos_ in ['NOUN', 'PROPN'] and 
                    len(token.text) > 2 and 
                    token.is_alpha and 
                    not token.is_stop):
                    keywords.add(token.lemma_.lower())
        
        except Exception as e:
            logger.error(f"Error with spaCy extraction: {e}")
        
        return keywords
    
    def _extract_with_nltk(self, text: str) -> Set[str]:
        """Extract keywords using NLTK"""
        keywords = set()
        
        try:
            # Tokenize and POS tag
            tokens = word_tokenize(text)
            pos_tags = pos_tag(tokens)
            
            # Extract nouns, proper nouns, and adjectives
            for word, pos in pos_tags:
                if (pos in ['NN', 'NNS', 'NNP', 'NNPS', 'JJ'] and 
                    len(word) > 2 and 
                    word.isalpha() and
                    word.lower() not in stopwords.words('english')):
                    keywords.add(word.lower())
        
        except Exception as e:
            logger.error(f"Error with NLTK extraction: {e}")
        
        return keywords
    
    def _extract_with_patterns(self, text: str) -> Set[str]:
        """Extract keywords using custom patterns"""
        keywords = set()
        
        # Pattern for skills sections
        skills_patterns = [
            r'(?:skills?|competencies|proficiencies?|technologies|tools?|software)[:,]?\s*([^\n]+)',
            r'(?:experience with|proficient in|skilled in|knowledge of)[:,]?\s*([^\n]+)',
        ]
        
        for pattern in skills_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                skills_text = match.group(1)
                # Split by common delimiters
                skills = re.split(r'[,;|•\-\n]', skills_text)
                for skill in skills:
                    skill = skill.strip()
                    if len(skill) > 2 and len(skill) < 50:
                        keywords.add(skill.lower())
        
        return keywords
    
    def parse_resume(self, file_path: str) -> Dict:
        """Complete resume parsing with all extracted information"""
        logger.info(f"Parsing resume: {file_path}")
        
        # Extract text
        text = self.extract_text_from_file(file_path)
        if not text:
            logger.error("No text extracted from resume")
            return {}
        
        # Parse information
        result = {
            'file_path': file_path,
            'text_length': len(text),
            'skills_by_category': self.extract_skills(text),
            'experience_years': self.extract_experience_years(text),
            'nlp_keywords': self.extract_keywords_nlp(text),
            'all_skills': [],
            'top_keywords': []
        }
        
        # Flatten all skills
        for category_skills in result['skills_by_category'].values():
            result['all_skills'].extend(category_skills)
        
        # Remove duplicates and get top keywords
        all_keywords = set(result['all_skills'] + result['nlp_keywords'])
        
        # Score keywords by frequency and relevance
        keyword_scores = {}
        text_lower = text.lower()
        
        for keyword in all_keywords:
            score = 0
            # Frequency score
            score += text_lower.count(keyword.lower())
            # Length bonus (prefer longer, more specific terms)
            if len(keyword.split()) > 1:
                score += 2
            # Skills database bonus
            for category_skills in self.skills_database.values():
                if keyword.lower() in category_skills:
                    score += 5
                    break
            
            keyword_scores[keyword] = score
        
        # Get top 15 keywords
        result['top_keywords'] = sorted(keyword_scores.keys(), 
                                      key=lambda x: keyword_scores[x], 
                                      reverse=True)[:15]
        
        logger.info(f"Extracted {len(result['all_skills'])} skills and {len(result['top_keywords'])} top keywords")
        return result
    
    def get_job_search_terms(self, resume_data: Dict, primary_role: str = "") -> List[str]:
        """Generate intelligent job search terms based on resume analysis"""
        search_terms = []
        
        if primary_role:
            search_terms.append(primary_role)
        
        # Add top skills as search terms
        if 'top_keywords' in resume_data:
            search_terms.extend(resume_data['top_keywords'][:8])
        
        # Add category-specific terms
        if 'skills_by_category' in resume_data:
            skills_by_cat = resume_data['skills_by_category']
            
            # Prioritize design and web skills for creative roles
            priority_categories = ['design_skills', 'design_software', 'web_technologies']
            for category in priority_categories:
                if category in skills_by_cat:
                    search_terms.extend(skills_by_cat[category][:3])
        
        # Remove duplicates while preserving order
        seen = set()
        unique_terms = []
        for term in search_terms:
            if term.lower() not in seen:
                seen.add(term.lower())
                unique_terms.append(term)
        
        return unique_terms[:12]  # Limit to 12 terms for performance

# Singleton instance
resume_parser = ResumeParser() 