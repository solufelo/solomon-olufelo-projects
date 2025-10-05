# Development Rules

## Documentation Requirements

### 1. Changelog Management
- All changes must be documented in `ai/changelog.md`
- Follow the Keep a Changelog format
- Categories to use:
  - Added (for new features)
  - Changed (for changes in existing functionality)
  - Deprecated (for soon-to-be removed features)
  - Removed (for removed features)
  - Fixed (for bug fixes)
  - Security (for security fixes)
  - Pending (for planned next steps)

### 2. Project Planning
- Always refer to `ai/plan.md` for:
  - Current phase of development
  - Task priorities
  - Progress tracking
  - Testing requirements
- Update checkboxes as tasks are completed

### 3. Product Requirements
- Consult `ai/prd.md` for:
  - Feature specifications
  - User stories
  - Success criteria
  - Scope limitations

### 4. Code Documentation
- All new files must include docstrings
- Document all functions with Args/Returns
- Include usage examples for complex functions
- Add inline comments for non-obvious code

### 5. Version Control
- Create meaningful commit messages
- Reference related issues/tasks
- Keep commits focused and atomic

## Development Workflow

1. Check `plan.md` for next task
2. Implement the feature/fix
3. Update documentation:
   - Add changes to changelog.md
   - Update checkboxes in plan.md
   - Update other docs as needed
4. Test the changes
5. Commit with proper message

## Testing Requirements

- Write tests for new features
- Update existing tests when changing functionality
- Run full test suite before marking task complete
- Document test cases and expected results 