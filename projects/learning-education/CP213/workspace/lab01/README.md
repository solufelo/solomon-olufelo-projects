# Lab 01: Documentation and I/O

Steps
- Create package `cp213`.
- Add `ScannerTest` and Javadoc comments.
- Generate Javadoc (use script below or Eclipse).
- Run program and test input cases.

Generate Javadoc (CLI)
```bash
../../scripts/gen_javadoc.sh lab01
```
Run program (CLI)
```bash
mkdir -p bin
javac -d bin src/cp213/ScannerTest.java
java -cp bin cp213.ScannerTest
```
