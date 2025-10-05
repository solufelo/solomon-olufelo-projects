#!/usr/bin/env node

/**
 * StudyOS Changelog Update Helper
 * 
 * This script helps maintain the AI_CHANGELOG.md file by:
 * - Adding new entries with proper formatting
 * - Updating issue status
 * - Generating changelog templates
 * 
 * Usage:
 *   node scripts/update-changelog.js add-issue "Issue title" "Description" "priority"
 *   node scripts/update-changelog.js update-status "issue-id" "new-status"
 *   node scripts/update-changelog.js new-session "version" "description"
 */

const fs = require('fs');
const path = require('path');

const CHANGELOG_PATH = path.join(__dirname, '..', 'AI_CHANGELOG.md');

// Helper functions
const getCurrentDate = () => new Date().toISOString().split('T')[0];

const priorityEmojis = {
  critical: '🔥',
  high: '⚠️',
  medium: '📝',
  low: '🔧'
};

const statusEmojis = {
  completed: '✅',
  'in-progress': '🔄',
  pending: '📋',
  blocked: '🚫'
};

// Command handlers
const commands = {
  'add-issue': (title, description, priority = 'medium') => {
    const emoji = priorityEmojis[priority] || '📝';
    const issueEntry = `
**${priority.charAt(0).toUpperCase() + priority.slice(1)} Priority:**
${priority === 'critical' ? '1' : priority === 'high' ? '2' : priority === 'medium' ? '3' : '4'}. **${title}**
   - **Issue**: ${description}
   - **Impact**: [To be assessed]
   - **Next Steps**: [To be defined]
   - **Files**: [To be identified]
`;
    
    console.log(`📝 Issue template generated:`);
    console.log(issueEntry);
    console.log(`\n💡 Add this to the "⚠️ Known Issues Requiring Attention" section in AI_CHANGELOG.md`);
  },

  'new-session': (version, description) => {
    const template = `
## 🚀 **Version ${version} - ${getCurrentDate()} (Current Session)**

### 🎯 **Session Goals**: ${description}

#### ✅ **Completed This Session**
[Add completed work here]

#### 🛠️ **Technical Changes**
[Add technical modifications here]

#### 🔍 **Issues Identified & Status**

##### ✅ **Fixed Issues**
[Add fixed issues here]

##### ⚠️ **New Issues Discovered**
[Add new issues here]

##### 🔄 **Work In Progress**
[Add current work status here]

#### 📊 **Session Metrics**
- **Files Modified**: [count]
- **New Components**: [count]  
- **Issues Fixed**: [count]
- **Issues Identified**: [count]

#### 🚀 **Next Session Priorities**
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

---
`;
    
    console.log(`🚀 New session template for version ${version}:`);
    console.log(template);
    console.log(`\n💡 Add this to the top of AI_CHANGELOG.md and update the previous session status`);
  },

  'generate-summary': () => {
    const summary = `
## 📋 **Current Status Summary**

### ✅ **What's Working**
- [List working features]

### ⚠️ **Critical Issues**
- [List blocking issues]

### 🔄 **In Progress**
- [List current work]

### 🚀 **Next Priorities**
1. [Top priority]
2. [Second priority]
3. [Third priority]

### 📊 **Health Metrics**
- **Build Status**: ✅ Passing
- **Tests**: [status]
- **Performance**: [status]
- **Accessibility**: [status]

---

*Generated on ${getCurrentDate()}*
`;
    
    console.log(`📊 Status summary template:`);
    console.log(summary);
  },

  'help': () => {
    console.log(`
📋 StudyOS Changelog Helper

Available commands:
  add-issue <title> <description> [priority]   Add new issue template
  new-session <version> <description>          Generate new session template  
  generate-summary                             Generate status summary
  help                                         Show this help

Examples:
  node scripts/update-changelog.js add-issue "Auth display broken" "Shows generic user instead of real name" "high"
  node scripts/update-changelog.js new-session "0.3.0" "Implement server operations"
  node scripts/update-changelog.js generate-summary

Priority levels: critical, high, medium, low
`);
  }
};

// Main execution
const [,, command, ...args] = process.argv;

if (!command || !commands[command]) {
  console.log('❌ Unknown command. Use "help" for available commands.');
  process.exit(1);
}

try {
  commands[command](...args);
} catch (error) {
  console.error('❌ Error executing command:', error.message);
  process.exit(1);
}
