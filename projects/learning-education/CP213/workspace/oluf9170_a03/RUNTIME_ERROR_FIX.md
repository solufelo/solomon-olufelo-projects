# Fixing Runtime Error: "Constructor SingleNode<T>(T) is undefined"

## The Problem

You're getting this error at runtime:
```
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
	The constructor SingleNode<T>(T) is undefined
	at cp213.SingleList.append(SingleList.java:47)
```

## Root Cause

This happens when:
1. **Stale class files**: Your `SingleList.class` was compiled against an old version of `SingleNode.class` that didn't have the constructor
2. **IDE caching**: Your IDE is using cached/old compiled classes
3. **Classpath issues**: The runtime classpath points to old class files

## Solution: Clean Rebuild

### Step 1: Clean All Class Files

**From command line:**
```bash
cd /home/solom/Projects/CP213/workspace/oluf9170_a03
rm -rf bin/cp213/*.class
```

**Or use the rebuild script:**
```bash
./rebuild.sh
```

### Step 2: Recompile Everything

**Compile in order (dependencies first):**
```bash
# 1. Compile SingleNode (no dependencies)
javac -d bin -sourcepath src src/cp213/SingleNode.java

# 2. Compile SingleLink (depends on SingleNode)
javac -d bin -sourcepath src -cp bin src/cp213/SingleLink.java

# 3. Compile SingleList (depends on SingleNode and SingleLink)
javac -d bin -sourcepath src -cp bin src/cp213/SingleList.java

# 4. Compile A03Main (depends on everything)
javac -d bin -sourcepath src -cp bin src/cp213/A03Main.java
```

**Or compile all at once:**
```bash
javac -d bin -sourcepath src -cp bin src/cp213/*.java
```

### Step 3: Verify Constructor Exists

```bash
javap -cp bin -public cp213.SingleNode
```

You should see:
```
public class cp213.SingleNode<T> {
  public cp213.SingleNode(T);    ← This must exist!
  public T getDatum();
  public cp213.SingleNode<T> getNext();
  public void setNext(cp213.SingleNode<T>);
}
```

### Step 4: Run with Correct Classpath

```bash
java -cp bin cp213.A03Main
```

## IDE-Specific Fixes

### Eclipse

1. **Clean Project:**
   - Right-click project → Clean...
   - Select your project → Clean

2. **Refresh:**
   - Right-click project → Refresh (F5)

3. **Rebuild:**
   - Project → Build All

4. **Check Build Path:**
   - Right-click project → Properties
   - Java Build Path → Source
   - Verify: `oluf9170_a03/src` is listed
   - Java Build Path → Libraries
   - Verify: `oluf9170_a03/bin` is in classpath

### IntelliJ IDEA

1. **Invalidate Caches:**
   - File → Invalidate Caches / Restart
   - Select "Invalidate and Restart"

2. **Rebuild Project:**
   - Build → Rebuild Project

3. **Check Project Structure:**
   - File → Project Structure (Ctrl+Alt+Shift+S)
   - Modules → Your module → Sources
   - Verify `src` is marked as Sources
   - Modules → Your module → Paths
   - Verify Output path is `bin`

### VS Code

1. **Clean Java Workspace:**
   - Command Palette (Ctrl+Shift+P)
   - Type: "Java: Clean Java Language Server Workspace"
   - Restart

2. **Rebuild Projects:**
   - Command Palette → "Java: Rebuild Projects"

## Quick Fix Script

I've created a `rebuild.sh` script for you. Run:

```bash
cd /home/solom/Projects/CP213/workspace/oluf9170_a03
./rebuild.sh
```

This will:
1. Clean all old class files
2. Compile everything in the correct order
3. Verify the constructor exists

## Verification

After rebuilding, verify the fix:

```bash
# Check that constructor exists in bytecode
javap -cp bin -public cp213.SingleNode | grep "SingleNode(T)"

# Should output: public cp213.SingleNode(T);

# Try running your program
java -cp bin cp213.A03Main
```

## Why This Happens

1. **Compilation Order**: If `SingleList.java` was compiled before `SingleNode.java` had the constructor, it creates class files that reference a non-existent constructor.

2. **Partial Compilation**: If you only recompiled `SingleList.java` but not `SingleNode.java`, you get a mismatch.

3. **IDE Auto-Compile**: IDEs sometimes compile files individually, creating inconsistent states.

## Prevention

Always compile all related files together:

```bash
# Good: Compile all at once
javac -d bin -sourcepath src src/cp213/*.java

# Or use a build tool like ant, maven, or gradle
```

## Current Status

✅ **SingleNode.java** has the constructor: `public SingleNode(final T datum)`
✅ **Source code compiles** successfully
✅ **Bytecode contains** the constructor

The issue is **stale class files** that need to be cleaned and recompiled.

## Next Steps

1. Run `./rebuild.sh` to clean and rebuild
2. Verify with `javap` command
3. Run your program: `java -cp bin cp213.A03Main`
4. If using an IDE, clean and rebuild the project

---

**The constructor exists and works correctly. The error is from stale class files that need to be cleaned and recompiled.**

