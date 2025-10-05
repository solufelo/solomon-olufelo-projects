# StudyOS Cursor Rules Documentation

This directory contains rule files that guide development of the StudyOS application. These rules provide context, conventions, and best practices for AI-assisted development.

## Rule Categories

### Core Framework Rules (Always Applied)
These rules are automatically applied to all development work:

- **`wasp-overview.mdc`** - Wasp framework fundamentals and core concepts
- **`project-conventions.mdc`** - Project structure, import rules, and coding conventions  
- **`database-operations.mdc`** - Database schema, entities, and Wasp operations
- **`authentication.mdc`** - Authentication setup and user management
- **`studyos-features.mdc`** - StudyOS-specific features and architecture
- **`development-workflow.mdc`** - Development workflow and coding standards

### Feature-Specific Rules (Applied on Request)
These rules provide detailed guidance for specific features:

- **`ui-components.mdc`** - ShadCN UI components and styling guidelines
- **`spaced-repetition.mdc`** - Spaced repetition algorithm and learning science
- **`deployment.mdc`** - Deployment processes and production setup
- **`advanced-troubleshooting.mdc`** - Advanced Wasp features and debugging

### UX Design & Research Rules (Applied on Request) 🎨
Professional UX design documentation and research:

- **`competitive-analysis.mdc`** - Market research and competitive positioning analysis
- **`ux-research.mdc`** - User personas, journey maps, and behavioral insights
- **`design-system-comprehensive.mdc`** - Complete design system with PatternCraft integration
- **`usability-guidelines.mdc`** - Usability heuristics and interaction design patterns
- **`accessibility-standards.mdc`** - WCAG 2.1 AA compliance and accessibility implementation

### Development Methodology (Applied on Request)
- **`possible-solutions-thinking.mdc`** - Problem-solving framework and solution evaluation

## Rule Usage

### Always Applied Rules
These rules are automatically considered for all development tasks and provide the foundation for consistent development practices.

### Requestable Rules
Use the `fetch_rules` tool to load specific rules when working on related features:

```typescript
// Example: When working on UI components
fetch_rules(['ui-components'])

// Example: When implementing flashcard features
fetch_rules(['spaced-repetition'])
```

## File Organization

```
.cursor/rules/
├── README.md                          # This documentation
├── wasp-overview.mdc                  # Wasp framework basics
├── project-conventions.mdc            # Project structure & conventions
├── database-operations.mdc            # Database & operations
├── authentication.mdc                 # Auth setup & management
├── studyos-features.mdc              # StudyOS specific features
├── development-workflow.mdc           # Dev workflow & standards
├── ui-components.mdc                 # UI components & styling
├── spaced-repetition.mdc             # Learning algorithm details
├── deployment.mdc                    # Deployment processes
├── advanced-troubleshooting.mdc      # Advanced features & debugging
├── possible-solutions-thinking.mdc   # Problem-solving methodology
├── competitive-analysis.mdc          # 🎨 Market research & positioning
├── ux-research.mdc                   # 🎨 User personas & behavioral insights
├── design-system-comprehensive.mdc   # 🎨 Complete design system
├── usability-guidelines.mdc          # 🎨 Usability & interaction patterns
└── accessibility-standards.mdc       # 🎨 WCAG compliance & accessibility
```

## Best Practices

### When to Use Rules
- **Starting new features**: Review relevant feature-specific rules
- **Debugging issues**: Check troubleshooting and framework rules
- **Code review**: Ensure adherence to conventions and workflow rules
- **Architecture decisions**: Use problem-solving methodology

### Keeping Rules Updated
- Update rules when patterns change
- Add new rules for recurring issues
- Remove outdated information
- Keep examples current with codebase

### Rule Maintenance
- Regular review of rule effectiveness
- Update examples to match current codebase
- Consolidate overlapping information
- Ensure consistency across rule files

## Quick Reference

### Common Development Tasks
- **New page component**: `project-conventions.mdc`, `development-workflow.mdc`
- **Database changes**: `database-operations.mdc`, `wasp-overview.mdc`
- **Authentication issues**: `authentication.mdc`, `advanced-troubleshooting.mdc`
- **UI styling**: `ui-components.mdc`, `development-workflow.mdc`
- **Deployment**: `deployment.mdc`
- **Performance issues**: `possible-solutions-thinking.mdc`, `advanced-troubleshooting.mdc`

### Emergency Debugging
1. Check `advanced-troubleshooting.mdc` for common issues
2. Review `project-conventions.mdc` for import/structure problems
3. Use `possible-solutions-thinking.mdc` for systematic problem-solving
4. Consult `wasp-overview.mdc` for framework-specific issues
