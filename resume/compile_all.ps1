# compile_all.ps1
# Script to compile all tailored LaTeX resumes in the resumes folder structure

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "      Resumes LaTeX Compilation Script       " -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

# Verify pdflatex is installed
$hasPdfLatex = Get-Command pdflatex -ErrorAction SilentlyContinue
if (-not $hasPdfLatex) {
    Write-Error "pdflatex (TinyTeX / LaTeX compiler) was not found in your system PATH."
    Write-Host "Please ensure pdflatex is installed as specified in your Sigma Job Search Pipeline." -ForegroundColor Yellow
    exit 1
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Profiles = @("analyst", "journalist", "labourer", "volunteer", "web_designer", "csj", "prepr", "security", "it_support", "digital_media")

foreach ($Profile in $Profiles) {
    $TargetDir = Join-Path $ScriptDir $Profile
    $TexFile = Join-Path $TargetDir "resume_$Profile.tex"
    
    if (Test-Path $TexFile) {
        Write-Host "Compiling resume for profile: [$Profile]..." -ForegroundColor Green
        
        # Change directory to target directory to keep compilation context clean
        Push-Location $TargetDir
        
        # Run pdflatex (run twice to resolve any references/tabularx alignments if needed)
        pdflatex -interaction=nonstopmode "resume_$Profile.tex" | Out-Null
        
        # Clean up LaTeX aux files
        Remove-Item "resume_$Profile.aux" -ErrorAction SilentlyContinue
        Remove-Item "resume_$Profile.log" -ErrorAction SilentlyContinue
        Remove-Item "resume_$Profile.out" -ErrorAction SilentlyContinue
        
        Pop-Location
        
        $ExpectedPdf = Join-Path $TargetDir "resume_$Profile.pdf"
        if (Test-Path $ExpectedPdf) {
            Write-Host "Successfully generated: $ExpectedPdf" -ForegroundColor Cyan
        } else {
            Write-Host "Failed to generate PDF for $Profile." -ForegroundColor Red
        }
    } else {
        Write-Host "LaTeX file not found at: $TexFile" -ForegroundColor Red
    }
    Write-Host ""
}

# Compile root resumes
Write-Host "Compiling root resumes..." -ForegroundColor Green
Push-Location (Join-Path $ScriptDir "..")
pdflatex -interaction=nonstopmode "resume.tex" | Out-Null
Remove-Item "resume.aux" -ErrorAction SilentlyContinue
Remove-Item "resume.log" -ErrorAction SilentlyContinue
Remove-Item "resume.out" -ErrorAction SilentlyContinue

pdflatex -interaction=nonstopmode "resume_general.tex" | Out-Null
Remove-Item "resume_general.aux" -ErrorAction SilentlyContinue
Remove-Item "resume_general.log" -ErrorAction SilentlyContinue
Remove-Item "resume_general.out" -ErrorAction SilentlyContinue
Pop-Location
Write-Host "Successfully compiled root resumes (resume.pdf, resume_general.pdf)" -ForegroundColor Cyan
Write-Host ""

# Mirror PDFs into cover-letter hub and apply-pipeline paths
$CoverLetterResumes = Join-Path $ScriptDir "..\tools\cover-letter\resumes"
if (-not (Test-Path $CoverLetterResumes)) {
    New-Item -ItemType Directory -Force -Path $CoverLetterResumes | Out-Null
}

$RootDir = Join-Path $ScriptDir ".."
$MirrorMap = @{
    "resume.pdf" = "resume_developer.pdf"
    "resume_general.pdf" = "resume_general.pdf"
}
foreach ($Profile in $Profiles) {
    $MirrorMap["$Profile\resume_$Profile.pdf"] = "resume_$Profile.pdf"
}

foreach ($entry in $MirrorMap.GetEnumerator()) {
    $src = Join-Path $RootDir $entry.Key
    $dst = Join-Path $CoverLetterResumes $entry.Value
    if (Test-Path $src) {
        Copy-Item $src $dst -Force
        Write-Host "Mirrored: $($entry.Value)" -ForegroundColor DarkGray
    }
}

Write-Host "Compilation process finished." -ForegroundColor Green
