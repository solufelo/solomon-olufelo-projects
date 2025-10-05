#!/usr/bin/env python3
"""
CP213 Markdown to HTML Converter

Converts CP213 lesson content from Markdown to HTML format using templates.
"""

import os
import re
import argparse
from pathlib import Path
from datetime import datetime

class MarkdownToHtmlConverter:
    def __init__(self, template_path, output_dir):
        self.template_path = template_path
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Student information (can be customized)
        self.student_info = {
            'STUDENT_NAME': 'Solomon Olufelo',
            'STUDENT_ID': '210729170',
            'STUDENT_EMAIL': 'oluf9170@mylaurier.ca'
        }
    
    def load_template(self):
        """Load the HTML template."""
        with open(self.template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def process_code_blocks(self, content):
        """Convert markdown code blocks to HTML pre/code blocks."""
        # Handle Java code blocks
        java_pattern = r'```java\n(.*?)\n```'
        java_replacement = r'<pre><code class="language-java">\1</code></pre>'
        content = re.sub(java_pattern, java_replacement, content, flags=re.DOTALL)
        
        # Handle generic code blocks
        code_pattern = r'```(\w+)?\n(.*?)\n```'
        def code_replacement(match):
            lang = match.group(1) or 'text'
            code = match.group(2)
            return f'<pre><code class="language-{lang}">{code}</code></pre>'
        
        content = re.sub(code_pattern, code_replacement, content, flags=re.DOTALL)
        
        return content
    
    def process_inline_code(self, content):
        """Convert inline code to HTML format."""
        content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
        return content
    
    def process_math(self, content):
        """Convert markdown math to HTML (basic implementation)."""
        # Inline math (simple conversion)
        content = re.sub(r'\$([^$]+)\$', r'<span class="math">$\1$</span>', content)
        
        # Display math
        content = re.sub(r'\$\$([^$]+)\$\$', r'<div class="math-display">$$\1$$</div>', content)
        
        return content
    
    def process_headings(self, content):
        """Convert markdown headings to HTML headings."""
        # H1
        content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
        
        # H2
        content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
        
        # H3
        content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
        
        # H4
        content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', content, flags=re.MULTILINE)
        
        return content
    
    def process_lists(self, content):
        """Convert markdown lists to HTML lists."""
        # Unordered lists
        content = re.sub(r'^- (.+)$', r'<li>\1</li>', content, flags=re.MULTILINE)
        
        # Wrap consecutive items in ul environment
        lines = content.split('\n')
        new_lines = []
        in_list = False
        
        for line in lines:
            if line.strip().startswith('<li>'):
                if not in_list:
                    new_lines.append('<ul>')
                    in_list = True
                new_lines.append(line)
            else:
                if in_list:
                    new_lines.append('</ul>')
                    in_list = False
                new_lines.append(line)
        
        if in_list:
            new_lines.append('</ul>')
        
        return '\n'.join(new_lines)
    
    def process_bold_italic(self, content):
        """Convert markdown bold and italic to HTML."""
        # Bold
        content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
        content = re.sub(r'__(.+?)__', r'<strong>\1</strong>', content)
        
        # Italic
        content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
        content = re.sub(r'_(.+?)_', r'<em>\1</em>', content)
        
        return content
    
    def process_tables(self, content):
        """Convert markdown tables to HTML tables."""
        # Simple table conversion (basic implementation)
        table_pattern = r'\|(.+?)\|\n\|[-:|\s]+\|\n((?:\|.+?\|\n?)+)'
        
        def table_replacement(match):
            header = match.group(1)
            rows = match.group(2)
            
            # Parse header
            header_cols = [col.strip() for col in header.split('|') if col.strip()]
            
            # Parse rows
            row_lines = [line.strip() for line in rows.split('\n') if line.strip()]
            row_data = []
            for line in row_lines:
                cols = [col.strip() for col in line.split('|') if col.strip()]
                if cols:
                    row_data.append(cols)
            
            # Generate HTML table
            html_table = '<table>\n<thead>\n<tr>\n'
            
            # Header row
            for col in header_cols:
                html_table += f'<th>{col}</th>\n'
            
            html_table += '</tr>\n</thead>\n<tbody>\n'
            
            # Data rows
            for row in row_data:
                html_table += '<tr>\n'
                for col in row:
                    html_table += f'<td>{col}</td>\n'
                html_table += '</tr>\n'
            
            html_table += '</tbody>\n</table>\n'
            
            return html_table
        
        content = re.sub(table_pattern, table_replacement, content, flags=re.DOTALL)
        return content
    
    def process_special_boxes(self, content):
        """Convert special markdown boxes to HTML divs."""
        # Concept boxes
        content = re.sub(r'### 🔹 (.+)', r'<div class="concept-box"><h4>\1</h4>', content)
        
        # Example boxes
        content = re.sub(r'### ✅ (.+)', r'<div class="example-box"><h4>\1</h4>', content)
        
        # Warning boxes
        content = re.sub(r'### ⚠️ (.+)', r'<div class="warning-box"><h4>\1</h4>', content)
        
        # Close boxes (simple implementation)
        content = re.sub(r'^---$', r'</div>', content, flags=re.MULTILINE)
        
        return content
    
    def extract_lesson_info(self, content):
        """Extract lesson title and number from content."""
        # Look for lesson title in first H1 or H2
        title_match = re.search(r'^#+\s*(?:Lesson\s*\d+)?[:\s]*(.+)$', content, re.MULTILINE)
        lesson_title = title_match.group(1).strip() if title_match else "CP213 Lesson"
        
        # Look for lesson number
        number_match = re.search(r'Lesson\s*(\d+)', content, re.IGNORECASE)
        lesson_number = number_match.group(1) if number_match else "1"
        
        return lesson_title, lesson_number
    
    def convert(self, markdown_content):
        """Convert markdown content to HTML."""
        # Extract lesson information
        lesson_title, lesson_number = self.extract_lesson_info(markdown_content)
        
        # Process content
        content = markdown_content
        
        # Apply transformations in order
        content = self.process_code_blocks(content)
        content = self.process_inline_code(content)
        content = self.process_math(content)
        content = self.process_headings(content)
        content = self.process_lists(content)
        content = self.process_bold_italic(content)
        content = self.process_tables(content)
        content = self.process_special_boxes(content)
        
        # Load template and substitute placeholders
        template = self.load_template()
        
        template = template.replace('LESSON_TITLE', lesson_title)
        template = template.replace('LESSON_NUMBER', f'Lesson {lesson_number}')
        template = template.replace('LESSON_CONTENT', content)
        
        # Replace student information
        for key, value in self.student_info.items():
            template = template.replace(key, value)
        
        return template
    
    def convert_file(self, input_file, output_file=None):
        """Convert a markdown file to HTML."""
        input_path = Path(input_file)
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        # Read markdown content
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert to HTML
        html_content = self.convert(markdown_content)
        
        # Determine output file
        if output_file is None:
            output_file = self.output_dir / f"{input_path.stem}.html"
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Converted {input_file} to {output_file}")
        return output_file

def main():
    parser = argparse.ArgumentParser(description='Convert CP213 markdown to HTML')
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output HTML file')
    parser.add_argument('-t', '--template', 
                       default='templates/html_lesson_template.html',
                       help='HTML template file')
    parser.add_argument('-d', '--output-dir', 
                       default='output',
                       help='Output directory')
    
    args = parser.parse_args()
    
    # Get script directory
    script_dir = Path(__file__).parent.parent
    template_path = script_dir / args.template
    
    if not template_path.exists():
        print(f"Template not found: {template_path}")
        return 1
    
    # Create converter
    converter = MarkdownToHtmlConverter(template_path, args.output_dir)
    
    try:
        output_file = converter.convert_file(args.input_file, args.output)
        print(f"Successfully converted to: {output_file}")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == '__main__':
    exit(main())



