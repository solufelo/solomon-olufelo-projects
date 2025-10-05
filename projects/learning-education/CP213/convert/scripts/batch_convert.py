#!/usr/bin/env python3
"""
CP213 Batch Content Converter

Batch converts all CP213 lesson content from Markdown to multiple formats.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add scripts directory to path for imports
script_dir = Path(__file__).parent
sys.path.append(str(script_dir))

from markdown_to_latex import MarkdownToLatexConverter
from markdown_to_html import MarkdownToHtmlConverter

class BatchConverter:
    def __init__(self, input_dir, output_dir):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Create subdirectories for different formats
        self.latex_dir = self.output_dir / 'latex'
        self.html_dir = self.output_dir / 'html'
        self.pdf_dir = self.output_dir / 'pdf'
        
        for dir_path in [self.latex_dir, self.html_dir, self.pdf_dir]:
            dir_path.mkdir(exist_ok=True)
        
        # Initialize converters
        script_parent = script_dir.parent
        self.latex_converter = MarkdownToLatexConverter(
            script_parent / 'templates' / 'latex_lesson_template.tex',
            self.latex_dir
        )
        self.html_converter = MarkdownToHtmlConverter(
            script_parent / 'templates' / 'html_lesson_template.html',
            self.html_dir
        )
    
    def find_markdown_files(self):
        """Find all markdown files in the input directory."""
        md_files = list(self.input_dir.glob('*.md'))
        md_files.extend(list(self.input_dir.glob('**/*.md')))
        return sorted(md_files)
    
    def convert_to_latex(self, md_file):
        """Convert markdown file to LaTeX."""
        try:
            output_file = self.latex_converter.convert_file(md_file)
            return output_file
        except Exception as e:
            print(f"Error converting {md_file} to LaTeX: {e}")
            return None
    
    def convert_to_html(self, md_file):
        """Convert markdown file to HTML."""
        try:
            output_file = self.html_converter.convert_file(md_file)
            return output_file
        except Exception as e:
            print(f"Error converting {md_file} to HTML: {e}")
            return None
    
    def compile_latex_to_pdf(self, tex_file):
        """Compile LaTeX file to PDF using pdflatex."""
        try:
            import subprocess
            tex_path = Path(tex_file)
            pdf_path = self.pdf_dir / f"{tex_path.stem}.pdf"
            
            # Run pdflatex
            result = subprocess.run([
                'pdflatex', 
                '-output-directory', str(self.pdf_dir),
                '-interaction=nonstopmode',
                str(tex_path)
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"Successfully compiled {tex_file} to PDF")
                return pdf_path
            else:
                print(f"Error compiling {tex_file}: {result.stderr}")
                return None
                
        except FileNotFoundError:
            print("pdflatex not found. Please install LaTeX to generate PDFs.")
            return None
        except Exception as e:
            print(f"Error compiling LaTeX: {e}")
            return None
    
    def convert_all(self, generate_pdf=False):
        """Convert all markdown files to all formats."""
        md_files = self.find_markdown_files()
        
        if not md_files:
            print(f"No markdown files found in {self.input_dir}")
            return
        
        print(f"Found {len(md_files)} markdown files")
        print(f"Converting to LaTeX and HTML...")
        
        results = {
            'success': 0,
            'failed': 0,
            'files': []
        }
        
        for md_file in md_files:
            print(f"\nProcessing: {md_file.name}")
            
            file_result = {
                'input': md_file,
                'latex': None,
                'html': None,
                'pdf': None
            }
            
            # Convert to LaTeX
            latex_file = self.convert_to_latex(md_file)
            file_result['latex'] = latex_file
            
            # Convert to HTML
            html_file = self.convert_to_html(md_file)
            file_result['html'] = html_file
            
            # Compile to PDF if requested
            if generate_pdf and latex_file:
                pdf_file = self.compile_latex_to_pdf(latex_file)
                file_result['pdf'] = pdf_file
            
            # Check if at least one conversion succeeded
            if latex_file or html_file:
                results['success'] += 1
            else:
                results['failed'] += 1
            
            results['files'].append(file_result)
        
        # Print summary
        print(f"\n{'='*50}")
        print(f"Conversion Summary:")
        print(f"Successfully converted: {results['success']}")
        print(f"Failed conversions: {results['failed']}")
        print(f"Total files processed: {len(results['files'])}")
        
        if generate_pdf:
            pdf_count = sum(1 for f in results['files'] if f['pdf'])
            print(f"PDFs generated: {pdf_count}")
        
        print(f"\nOutput directories:")
        print(f"LaTeX files: {self.latex_dir}")
        print(f"HTML files: {self.html_dir}")
        if generate_pdf:
            print(f"PDF files: {self.pdf_dir}")
        
        return results
    
    def create_index(self, results):
        """Create an index file listing all converted files."""
        index_file = self.output_dir / 'index.html'
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CP213 Converted Content</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .file-item {{ margin: 10px 0; padding: 10px; border: 1px solid #ddd; }}
        .success {{ background-color: #d4edda; }}
        .failed {{ background-color: #f8d7da; }}
        .links {{ margin-top: 10px; }}
        .links a {{ margin-right: 15px; }}
    </style>
</head>
<body>
    <h1>CP213 Converted Content</h1>
    <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    
    <h2>Files ({len(results['files'])} total)</h2>
"""
        
        for file_result in results['files']:
            status = 'success' if (file_result['latex'] or file_result['html']) else 'failed'
            
            html_content += f"""
    <div class="file-item {status}">
        <h3>{file_result['input'].name}</h3>
        <div class="links">
"""
            
            if file_result['latex']:
                html_content += f'<a href="latex/{file_result["latex"].name}">LaTeX</a>'
            
            if file_result['html']:
                html_content += f'<a href="html/{file_result["html"].name}">HTML</a>'
            
            if file_result['pdf']:
                html_content += f'<a href="pdf/{file_result["pdf"].name}">PDF</a>'
            
            html_content += """
        </div>
    </div>
"""
        
        html_content += """
</body>
</html>
"""
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Index file created: {index_file}")

def main():
    parser = argparse.ArgumentParser(description='Batch convert CP213 markdown files')
    parser.add_argument('-i', '--input-dir', 
                       default='input',
                       help='Input directory containing markdown files')
    parser.add_argument('-o', '--output-dir', 
                       default='output',
                       help='Output directory for converted files')
    parser.add_argument('--pdf', action='store_true',
                       help='Also generate PDF files from LaTeX')
    parser.add_argument('--index', action='store_true',
                       help='Create an index HTML file')
    
    args = parser.parse_args()
    
    # Get script directory
    script_dir = Path(__file__).parent.parent
    input_dir = script_dir / args.input_dir
    
    if not input_dir.exists():
        print(f"Input directory not found: {input_dir}")
        print("Creating sample input directory...")
        input_dir.mkdir(exist_ok=True)
        
        # Create a sample file
        sample_file = input_dir / 'sample_lesson.md'
        with open(sample_file, 'w') as f:
            f.write("""# Sample CP213 Lesson

## Introduction
This is a sample lesson for testing the conversion system.

## Code Example

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

## Key Concepts
- Object-oriented programming
- Java syntax
- Basic structure
""")
        print(f"Created sample file: {sample_file}")
    
    # Create batch converter
    converter = BatchConverter(input_dir, args.output_dir)
    
    # Convert all files
    results = converter.convert_all(generate_pdf=args.pdf)
    
    # Create index if requested
    if args.index and results:
        converter.create_index(results)
    
    return 0

if __name__ == '__main__':
    exit(main())