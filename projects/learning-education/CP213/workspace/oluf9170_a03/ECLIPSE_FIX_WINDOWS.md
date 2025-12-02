# Fixing Constructor Error in Eclipse (Windows)

## The Problem
Runtime error: `The constructor SingleNode<T>(T) is undefined`

This happens when Eclipse has stale compiled class files or incorrect build configuration.

## Solution for Eclipse on Windows

### Step 1: Clean the Project

1. **Right-click** on your project (`oluf9170_a03`) in the **Package Explorer**
2. Select **Clean...**
3. In the Clean dialog:
   - Select **Clean projects selected below**
   - Check your project: `oluf9170_a03`
   - Click **Clean**
4. Wait for Eclipse to finish cleaning

### Step 2: Refresh the Project

1. **Right-click** on your project
2. Select **Refresh** (or press **F5**)
3. This ensures Eclipse sees all file changes

### Step 3: Verify Build Path Configuration

1. **Right-click** on your project
2. Select **Properties**
3. In the Properties dialog:
   - Click **Java Build Path** in the left sidebar
   - Click the **Source** tab
   - Verify you see:
     - `oluf9170_a03/src` (as a source folder)
   - If `src` is not listed:
     - Click **Add Folder...**
     - Select the `src` folder
     - Click **OK**
   
4. Click the **Libraries** tab
   - Verify you see:
     - `oluf9170_a03/bin` in the classpath (usually shown as the project itself)
   - If missing, the project should automatically include its output folder

5. Click **Apply and Close**

### Step 4: Verify Output Folder

1. **Right-click** on your project → **Properties**
2. **Java Build Path** → **Source** tab
3. Expand `src` folder
4. Verify **Default output folder** shows: `oluf9170_a03/bin`
5. If it shows something else (like `oluf9170_a03/build` or `oluf9170_a03/classes`):
   - Click **Browse...**
   - Navigate to and select the `bin` folder
   - Click **OK**
6. Click **Apply and Close**

### Step 5: Delete Stale Class Files (Manual Clean)

1. In Eclipse, navigate to your project in **Package Explorer**
2. Expand `bin` folder
3. Expand `cp213` package
4. **Delete** all `.class` files you see:
   - `SingleNode.class`
   - `SingleLink.class`
   - `SingleList.class`
   - Any other `.class` files
5. **Right-click** project → **Refresh** (F5)

### Step 6: Rebuild the Project

1. **Project** → **Build All** (or **Build Project**)
2. Alternatively, let Eclipse auto-build (if enabled):
   - **Project** → **Build Automatically** should be checked
   - If not checked, check it and Eclipse will rebuild

### Step 7: Verify Compilation

1. Open `SingleNode.java`
2. Look for any red error markers (X icons) in the editor
3. Open `SingleList.java`
4. Look at line 48 (where `new SingleNode<T>(datum)` is called)
5. If you see a red underline:
   - Hover over it to see the error
   - If it says "constructor undefined", continue to Step 8

### Step 8: Force Rebuild of SingleNode

1. **Right-click** on `SingleNode.java` in Package Explorer
2. Select **Run As** → **Java Application** (this will fail, but forces compilation)
3. Or: **Project** → **Clean...** → Select your project → **Clean**
4. Check the **Console** view for compilation errors

### Step 9: Check for Multiple SingleNode Classes

1. In Eclipse, press **Ctrl+Shift+T** (Open Type)
2. Type: `SingleNode`
3. If you see multiple `SingleNode` classes:
   - Check which package each is in
   - Make sure you're using `cp213.SingleNode`
   - Delete any duplicate/old versions

### Step 10: Verify SingleNode Constructor Exists

1. Open `SingleNode.java` in Eclipse
2. Look for the constructor at line 32:
   ```java
   public SingleNode(final T datum) {
       this.datum = datum;
       this.next = null;
   }
   ```
3. If this constructor doesn't exist, you need to add it (but it should be there)

## Quick Fix: Full Project Reset

If the above steps don't work:

### Option A: Delete and Re-import

1. **Close Eclipse**
2. In Windows Explorer, navigate to your workspace
3. Delete the `.metadata` folder in your workspace (this resets Eclipse settings)
   - **Warning**: This will reset all Eclipse preferences for this workspace
4. **Reopen Eclipse**
5. **File** → **Import** → **Existing Projects into Workspace**
6. Select your project folder
7. Click **Finish**

### Option B: Fresh Build from Command Line (Recommended)

1. **Close Eclipse** (important!)
2. Open **Command Prompt** or **PowerShell**
3. Navigate to your project:
   ```cmd
   cd C:\path\to\your\workspace\oluf9170_a03
   ```
4. Delete all class files:
   ```cmd
   del /s /q bin\cp213\*.class
   ```
5. Compile from command line:
   ```cmd
   javac -d bin -sourcepath src src\cp213\*.java
   ```
6. **Reopen Eclipse**
7. **Right-click** project → **Refresh** (F5)
8. Eclipse should recognize the newly compiled classes

## Verify the Fix

1. Open `SingleList.java`
2. Go to line 48: `SingleNode<T> newNode = new SingleNode<T>(datum);`
3. There should be **no red underline**
4. If you hover over `SingleNode`, you should see the constructor in the tooltip
5. Try running your program:
   - **Right-click** `A03Main.java`
   - **Run As** → **Java Application**

## Common Eclipse Issues

### Issue 1: Eclipse Not Picking Up Changes

**Solution:**
- **Project** → **Clean...** → Clean your project
- **Right-click** project → **Refresh** (F5)
- Turn off and on **Build Automatically**: **Project** → **Build Automatically**

### Issue 2: Wrong Java Version

**Check:**
1. **Right-click** project → **Properties**
2. **Java Build Path** → **Libraries** tab
3. Verify Java version matches your JDK
4. **Java Compiler** → Verify compiler compliance level

### Issue 3: Build Path Issues

**Fix:**
1. **Right-click** project → **Properties**
2. **Java Build Path** → **Source** tab
3. Remove any incorrect source folders
4. Add `src` folder if missing
5. Verify output folder is `bin`

### Issue 4: Workspace vs Project Settings

**Check:**
1. **Window** → **Preferences** → **Java** → **Build Path**
2. Verify settings are correct
3. **Window** → **Preferences** → **Java** → **Compiler**
4. Verify compiler settings

## After Fixing: Prevention

1. **Enable Build Automatically**: **Project** → **Build Automatically** ✓
2. **Regular Clean**: Periodically do **Project** → **Clean...**
3. **Refresh After External Changes**: If you edit files outside Eclipse, always **Refresh** (F5)

## Quick Checklist

- [ ] Project cleaned (Project → Clean...)
- [ ] Project refreshed (F5)
- [ ] Build path configured correctly (src folder, bin output)
- [ ] Stale .class files deleted from bin folder
- [ ] Project rebuilt (Build All)
- [ ] No red errors in SingleNode.java
- [ ] No red errors in SingleList.java at line 48
- [ ] Program runs without constructor error

## Still Not Working?

If you've tried everything:

1. **Close Eclipse completely**
2. Delete `bin` folder contents: `del /s /q bin\cp213\*.class`
3. Compile from command line: `javac -d bin -sourcepath src src\cp213\*.java`
4. **Reopen Eclipse**
5. **Refresh** project (F5)
6. Try running again

The constructor **does exist** in your source code. The issue is Eclipse using stale compiled classes. Once you clean and rebuild, it should work!

---

## Windows-Specific Notes

- Use backslashes (`\`) in Windows paths: `bin\cp213\*.class`
- Command Prompt commands use `del` instead of `rm`
- PowerShell can use either `del` or `Remove-Item`
- Eclipse on Windows might have different default paths - always verify in Properties

