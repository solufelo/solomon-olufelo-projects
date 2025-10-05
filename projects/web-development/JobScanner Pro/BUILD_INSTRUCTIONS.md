# Building JobScanner Pro Executables

This guide explains how to create standalone executable files for JobScanner Pro that can run on systems without Python installed.

## Quick Start (Recommended)

### Option 1: Automated Build Script
```bash
python build_exe.py
```

This will create both CLI and GUI executables with all dependencies included.

### Option 2: Simple GUI Only
```bash
python build_simple.py
```

Creates a basic GUI executable with minimal configuration.

## Manual Build Commands

### Prerequisites
```bash
pip install pyinstaller
python -m spacy download en_core_web_sm
```

### GUI Executable (Recommended for most users)
```bash
pyinstaller --onefile --windowed --name=JobScannerPro-GUI \
    --add-data="jobscanner/config.yml;jobscanner/" \
    --add-data="config.yml;." \
    --hidden-import=nltk \
    --hidden-import=spacy \
    --hidden-import=selenium \
    --hidden-import=playwright \
    --collect-all=spacy \
    --collect-all=nltk \
    jobscanner/gui/app_tkinter.py
```

### CLI Executable
```bash
pyinstaller --onefile --console --name=JobScannerPro-CLI \
    --add-data="jobscanner/config.yml;jobscanner/" \
    --add-data="config.yml;." \
    --hidden-import=nltk \
    --hidden-import=spacy \
    --hidden-import=selenium \
    --hidden-import=playwright \
    --hidden-import=rich \
    --collect-all=spacy \
    --collect-all=nltk \
    jobscanner/main.py
```

## Build Output

After successful build:
- **Executables**: `dist/` folder
- **GUI**: `JobScannerPro-GUI.exe` (Windows) or `JobScannerPro-GUI` (Linux/Mac)
- **CLI**: `JobScannerPro-CLI.exe` (Windows) or `JobScannerPro-CLI` (Linux/Mac)

## Platform-Specific Notes

### Windows (WSL2)
- Executables will have `.exe` extension
- Build creates Windows-compatible binaries
- Test on actual Windows system for compatibility

### Linux
- No file extension for executables
- May need to set execute permissions: `chmod +x dist/JobScannerPro-GUI`

### macOS
- Similar to Linux
- May need to bypass Gatekeeper for unsigned applications

## Troubleshooting

### Common Issues

#### 1. Large File Size
**Problem**: Executable is very large (200MB+)
**Solution**: This is normal due to:
- spaCy language models (~50MB)
- NLTK data (~20MB)
- Selenium/Playwright browsers
- Python runtime (~50MB)

#### 2. Missing Dependencies
**Problem**: "Module not found" errors
**Solution**: Add missing imports:
```bash
pyinstaller --hidden-import=missing_module_name ...
```

#### 3. spaCy Model Not Found
**Problem**: "Can't find model en_core_web_sm"
**Solutions**:
```bash
# Download model
python -m spacy download en_core_web_sm

# Or use alternative model
python -m spacy download en_core_web_md
```

#### 4. NLTK Data Missing
**Problem**: NLTK data errors
**Solution**:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

#### 5. Slow Startup
**Problem**: Executable takes long to start
**Explanation**: Normal behavior due to:
- Extracting embedded files
- Loading ML models
- First-run initialization

#### 6. Antivirus False Positives
**Problem**: Antivirus flags executable
**Solution**: 
- Add to antivirus exceptions
- This is common with PyInstaller executables

### Advanced Options

#### Reduce File Size
```bash
# Exclude unnecessary modules
pyinstaller --exclude-module=matplotlib \
    --exclude-module=scipy \
    --exclude-module=pandas.plotting \
    ...
```

#### Debug Build
```bash
# Add console window to GUI for debugging
pyinstaller --onefile --console --debug=all \
    jobscanner/gui/app_tkinter.py
```

#### Spec File Customization
Generate a `.spec` file for advanced configuration:
```bash
pyinstaller --onefile jobscanner/gui/app_tkinter.py
# Edit JobScannerPro-GUI.spec as needed
pyinstaller JobScannerPro-GUI.spec
```

## Alternative Tools

If PyInstaller doesn't work for your use case:

### cx_Freeze
```bash
pip install cx_freeze
python setup.py build
```

### Nuitka
```bash
pip install nuitka
python -m nuitka --onefile --windows-disable-console jobscanner/gui/app_tkinter.py
```

### auto-py-to-exe (GUI for PyInstaller)
```bash
pip install auto-py-to-exe
auto-py-to-exe
```

## Testing Your Executable

### Basic Test
1. Copy executable to a clean system (or VM)
2. Run without Python installed
3. Test core functionality:
   - Search for jobs
   - Apply filters
   - Export results

### Performance Test
- Test with various search terms
- Check memory usage
- Verify all scrapers work
- Test file operations

## Distribution

### Single File Distribution
The `--onefile` option creates a single executable that:
- Contains all dependencies
- Self-extracts at runtime
- Requires no installation
- Can be distributed via USB, email, etc.

### Security Considerations
- Executables are unsigned
- May trigger antivirus warnings
- Consider code signing for production

## Build Size Expectations

| Component | Approximate Size |
|-----------|------------------|
| Python Runtime | ~50MB |
| spaCy + Model | ~60MB |
| NLTK Data | ~20MB |
| Other Dependencies | ~30MB |
| Your Code | ~5MB |
| **Total** | **~165MB** |

This is normal for ML-powered applications with NLP capabilities.

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Try the simple build script first
3. Verify all dependencies are installed
4. Test on the same platform where you'll run the executable

The automated build script (`build_exe.py`) handles most edge cases and provides detailed error messages to help diagnose issues. 