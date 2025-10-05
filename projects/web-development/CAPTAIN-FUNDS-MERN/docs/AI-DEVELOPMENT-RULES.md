# AI Development Rules & Guidelines

## 🤖 AI Assistant Guidelines for CAPTAIN-FUNDS Project

### 🎯 Core Principles

1. **Always Follow the Project Structure**
   - Maintain consistent file organization
   - Use established naming conventions
   - Follow the existing architecture patterns

2. **Security First**
   - Never expose sensitive information (API keys, passwords)
   - Always implement proper authentication checks
   - Validate all user inputs
   - Use environment variables for configuration

3. **Code Quality Standards**
   - Write TypeScript with proper type definitions
   - Follow ESLint rules and best practices
   - Maintain consistent code formatting
   - Add meaningful comments for complex logic

## ✅ DO's - What We Should Always Do

### Development Process
- ✅ **Use TODO lists** for complex tasks to track progress
- ✅ **Update TODO status** as tasks are completed
- ✅ **Read existing code** before making changes
- ✅ **Test changes** after implementation
- ✅ **Use parallel tool calls** for efficiency
- ✅ **Clear caches** when needed (Vite, TypeScript)
- ✅ **Check for errors** after each significant change

### Code Implementation
- ✅ **Use established patterns** from existing codebase
- ✅ **Import from the store** for state management
- ✅ **Use Ant Design components** consistently
- ✅ **Implement proper error handling**
- ✅ **Add loading states** for async operations
- ✅ **Use TypeScript interfaces** for type safety
- ✅ **Follow React hooks rules** (call at top level)

### File Management
- ✅ **Create files in correct directories**
- ✅ **Use consistent naming** (kebab-case for files)
- ✅ **Export default** from component files
- ✅ **Import with proper paths** (relative/absolute)
- ✅ **Update routes** when adding new pages

### Database & API
- ✅ **Use environment variables** for connection strings
- ✅ **Implement proper error responses**
- ✅ **Add input validation** on server routes
- ✅ **Use JWT tokens** for authentication
- ✅ **Hash passwords** before storing

## ❌ DON'Ts - What We Should Never Do

### Development Process
- ❌ **Never skip TODO tracking** for complex features
- ❌ **Don't make assumptions** about existing code
- ❌ **Never ignore errors** or warnings
- ❌ **Don't use sequential calls** when parallel is possible
- ❌ **Never leave broken code** uncommitted
- ❌ **Don't create files** without updating imports/routes

### Code Implementation
- ❌ **Never use any type** in TypeScript
- ❌ **Don't call hooks** conditionally or in loops
- ❌ **Never hardcode** sensitive data
- ❌ **Don't ignore React warnings**
- ❌ **Never use inline styles** (use Tailwind classes)
- ❌ **Don't create duplicate components**

### Security & Data
- ❌ **Never expose JWT secrets** in client code
- ❌ **Don't store passwords** in plain text
- ❌ **Never skip input validation**
- ❌ **Don't trust client-side data** on server
- ❌ **Never commit .env files**
- ❌ **Don't use HTTP** for sensitive data

### File & Structure
- ❌ **Never break** existing file structure
- ❌ **Don't create** unnecessary nested directories
- ❌ **Never use** absolute imports for relative files
- ❌ **Don't modify** package.json without discussion
- ❌ **Never delete** files without checking dependencies

## 🔄 Development Workflow

### 1. Planning Phase
```markdown
1. Understand the requirement
2. Check existing codebase for similar patterns
3. Create TODO list for complex features
4. Plan file structure and components needed
```

### 2. Implementation Phase
```markdown
1. Start with TODO marked as 'in_progress'
2. Create/modify files following established patterns
3. Test changes incrementally
4. Update TODO status as completed
5. Check for any lint errors or warnings
```

### 3. Validation Phase
```markdown
1. Test the feature in browser
2. Check console for errors
3. Verify authentication works
4. Test role-based access if applicable
5. Ensure responsive design
```

## 📋 Common Task Patterns

### Adding a New Page
1. Create page component in appropriate directory
2. Add route to App.tsx
3. Update navigation if needed
4. Test routing and access control
5. Add to TODO list if complex

### Database Operations
1. Check existing models and routes
2. Add validation and error handling
3. Test with sample data
4. Verify authentication requirements
5. Update API documentation

### UI Components
1. Use Ant Design components when possible
2. Follow existing styling patterns
3. Ensure responsive design
4. Add proper TypeScript types
5. Test accessibility

## 🚨 Error Handling Patterns

### Frontend Errors
```typescript
try {
  // API call or operation
} catch (error: any) {
  message.error(error?.response?.data?.message || 'Operation failed')
  console.error('Error:', error)
}
```

### Backend Errors
```javascript
try {
  // Database operation
} catch (error) {
  res.status(500).json({ 
    message: 'Operation failed', 
    error: process.env.NODE_ENV === 'development' ? error : {} 
  })
}
```

## 🔧 Common Commands

### Development
```bash
# Start servers
cd server && npm start
cd client && npm run dev

# Clear caches
cd client && rm -rf node_modules/.vite

# Build for production
cd client && npm run build
```

### Debugging
```bash
# Check processes
ps aux | grep node

# Kill processes
pkill -f vite
pkill -f "node.*index.js"

# Test API endpoints
curl -X GET http://localhost:5000/api/users/
```

## 📊 Progress Tracking

### Use TODO Lists For:
- Multi-step features (3+ steps)
- Complex integrations
- New page creation with multiple components
- Database schema changes
- Authentication flow modifications

### Don't Use TODO Lists For:
- Simple text changes
- Single component updates
- Bug fixes
- Style adjustments
- Configuration changes

## 🎯 Quality Checkpoints

### Before Completing Any Feature:
- [ ] Code follows TypeScript best practices
- [ ] Error handling is implemented
- [ ] Authentication is properly checked
- [ ] UI is responsive and accessible
- [ ] No console errors or warnings
- [ ] TODO list is updated
- [ ] Changes are tested in browser

### Before Major Releases:
- [ ] All TODO items completed
- [ ] Full authentication flow tested
- [ ] All routes accessible
- [ ] Database operations working
- [ ] No breaking changes
- [ ] Documentation updated

---

## 📞 When in Doubt:

1. **Check existing patterns** in the codebase
2. **Ask for clarification** if requirements are unclear
3. **Test incrementally** rather than big changes
4. **Use TODO lists** to track complex work
5. **Follow the established architecture**

**Remember**: Consistency and quality over speed. Better to do it right the first time than to refactor later.

---

**Last Updated**: September 2024  
**Version**: 1.0.0
