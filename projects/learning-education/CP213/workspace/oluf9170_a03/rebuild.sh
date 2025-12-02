#!/bin/bash
# Clean rebuild script for CP213 Assignment 3
# This ensures all classes are compiled with the latest SingleNode

echo "Cleaning old class files..."
rm -rf bin/cp213/*.class

echo "Compiling SingleNode..."
javac -d bin -sourcepath src src/cp213/SingleNode.java

echo "Compiling SingleLink..."
javac -d bin -sourcepath src -cp bin src/cp213/SingleLink.java

echo "Compiling SingleList..."
javac -d bin -sourcepath src -cp bin src/cp213/SingleList.java

echo "Verifying SingleNode constructor..."
javap -cp bin -public cp213.SingleNode | grep "public cp213.SingleNode"

echo ""
echo "If you see 'public cp213.SingleNode(T);' above, compilation was successful!"
echo ""
echo "To run your program, use:"
echo "  java -cp bin cp213.A03Main"
echo ""
echo "Or if using an IDE, make sure it's using the 'bin' directory as the output folder."

