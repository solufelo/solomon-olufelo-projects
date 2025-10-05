# CP213 Content Conversion System - Usage Guide

## Overview

This conversion system allows you to transform CP213 course content from Markdown format into multiple output formats including LaTeX, HTML, and PDF.

## Quick Start

### 1. Convert a Single File

```bash
# Convert to HTML
python3 scripts/markdown_to_html.py input/lesson01_variables.md

# Convert to LaTeX
python3 scripts/markdown_to_latex.py input/lesson01_variables.md
```

### 2. Batch Convert All Files

```bash
# Convert all markdown files to HTML and LaTeX
python3 scripts/batch_convert.py

# Also generate PDF files (requires LaTeX installation)
python3 scripts/batch_convert.py --pdf

# Create an index HTML file
python3 scripts/batch_convert.py --index
```

## File Structure

```
convert/
├── README.md                    # System overview
├── usage_guide.md              # This guide
├── input/                      # Source markdown files
│   ├── lesson01_variables.md
│   ├── lesson02_output_input.md
│   └── lesson03_control_flow.md
├── templates/                  # Output templates
│   ├── latex_lesson_template.tex
│   └── html_lesson_template.html
├── scripts/                    # Conversion scripts
│   ├── markdown_to_latex.py
│   ├── markdown_to_html.py
│   └── batch_convert.py
└── output/                     # Generated files
    ├── latex/                  # LaTeX files
    ├── html/                   # HTML files
    ├── pdf/                    # PDF files (if generated)
    └── index.html              # Index file (if created)
```

## Features

### Supported Markdown Elements

- **Headings** (H1-H6) → LaTeX sections/subsections
- **Code blocks** → Syntax-highlighted code listings
- **Inline code** → Monospace text
- **Bold/Italic** → LaTeX/HTML formatting
- **Lists** → Enumerated/itemized lists
- **Tables** → LaTeX/HTML tables
- **Math expressions** → LaTeX math mode
- **Special boxes** → Styled concept/example/warning boxes

### Output Formats

1. **LaTeX** - Professional academic formatting
2. **HTML** - Web-ready with syntax highlighting
3. **PDF** - Generated from LaTeX (requires pdflatex)

### Customization

#### Student Information

Edit the student information in the converter classes:

```python
self.student_info = {
    'STUDENT_NAME': 'Solomon Olufelo',
    'STUDENT_ID': '210729170',
    'STUDENT_EMAIL': 'oluf9170@mylaurier.ca'
}
```

#### Templates

- **LaTeX Template**: Modify `templates/latex_lesson_template.tex`
- **HTML Template**: Modify `templates/html_lesson_template.html`

## Advanced Usage

### Custom Output Directory

```bash
python3 scripts/batch_convert.py -o custom_output
```

### Custom Input Directory

```bash
python3 scripts/batch_convert.py -i custom_input
```

### Specific File Conversion

```bash
python3 scripts/markdown_to_latex.py input/lesson01_variables.md -o custom_output/my_file.tex
```

## Requirements

### Python Dependencies

- Python 3.6+
- Standard library only (no external dependencies)

### Optional Dependencies

- **LaTeX** (for PDF generation): Install `texlive-full` or similar
- **Web browser** (for viewing HTML output)

### Installation

```bash
# Ubuntu/Debian
sudo apt install python3 texlive-full

# macOS (with Homebrew)
brew install python3 mactex

# Windows
# Install Python 3 and MiKTeX
```

## Troubleshooting

### Common Issues

1. **Python not found**: Use `python3` instead of `python`
2. **LaTeX not found**: Install LaTeX distribution for PDF generation
3. **Permission denied**: Make scripts executable with `chmod +x scripts/*.py`
4. **Template not found**: Ensure templates are in the correct directory

### Error Messages

- `Template not found`: Check that template files exist in `templates/`
- `Input directory not found`: The system will create a sample directory
- `pdflatex not found`: Install LaTeX distribution for PDF generation

## Examples

### Example 1: Convert Single Lesson

```bash
cd /home/solom/Projects/CP213/convert
python3 scripts/markdown_to_html.py input/lesson01_variables.md
# Output: output/lesson01_variables.html
```

### Example 2: Batch Convert with Index

```bash
python3 scripts/batch_convert.py --index --pdf
# Creates: output/latex/, output/html/, output/pdf/, output/index.html
```

### Example 3: Custom Output

```bash
python3 scripts/markdown_to_latex.py input/lesson01_variables.md -o my_lesson.tex
# Output: my_lesson.tex
```

## Integration with CP213 Workflow

This conversion system integrates with your existing CP213 structure:

1. **Source Content**: Place markdown files in `input/`
2. **Conversion**: Run conversion scripts
3. **Output**: Use generated files for assignments, notes, or documentation
4. **Version Control**: Track both source markdown and generated outputs

## Tips and Best Practices

1. **Keep source clean**: Use consistent markdown formatting
2. **Regular conversion**: Convert after making changes
3. **Backup outputs**: Keep generated files for reference
4. **Test templates**: Verify output formatting before important submissions
5. **Use version control**: Track both source and generated files

## Support

For issues or questions:
1. Check this usage guide
2. Review error messages carefully
3. Ensure all dependencies are installed
4. Verify file paths and permissions



