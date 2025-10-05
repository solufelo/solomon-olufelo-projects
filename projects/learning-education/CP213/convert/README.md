# CP213 Content Conversion System

This directory contains tools and templates for converting CP213 course content into various formats.

## Structure

- `templates/` - LaTeX, HTML, and other format templates
- `scripts/` - Python conversion scripts
- `output/` - Generated output files
- `input/` - Source content to be converted

## Usage

### Quick Start

```bash
# Convert lesson content to LaTeX
python scripts/markdown_to_latex.py input/lesson01.md

# Convert to HTML
python scripts/markdown_to_html.py input/lesson01.md

# Batch convert all lessons
python scripts/batch_convert.py
```

### Available Formats

1. **LaTeX** - For academic papers and assignments
2. **HTML** - For web display
3. **PDF** - Via LaTeX compilation
4. **Word** - Via pandoc (if installed)

## Templates

Each template supports:
- Code syntax highlighting
- Math equations
- Tables and diagrams
- Academic formatting
- Student information integration

## Features

- Automatic code block formatting
- Syntax highlighting for Java
- Math equation rendering
- Table generation
- Bibliography support
- Custom styling options



