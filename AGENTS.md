# Agent Guidelines for Call Analyzer

## Project Structure
- Single-page React application in `index.html` using Babel standalone
- No build system - runs directly in browser with CDN dependencies
- React 18 + TailwindCSS + SheetJS (XLSX) + html2canvas

## Running the Application
```bash
start index.html  # Opens in default browser
```
No build, lint, or test commands - this is a standalone HTML file.

## Code Style

**Functions**: Use JSDoc comments for all utility functions (see lines 60-88 for examples)
**Naming**: camelCase for functions/variables, PascalCase for React components
**Organization**: Group related functions with section headers (e.g., `// ==================== UTILITY FUNCTIONS ====================`)
**Error Handling**: Use try-catch blocks; log errors to console; show user-friendly messages in UI
**Validation**: Three-phase approach - Phase 1/2 block with user errors, Phase 3 silently filters with console logs only
**State Management**: Use React hooks (useState, useEffect, useRef); store preferences in localStorage
**Data Flow**: Parse files → Validate structure → Process data → Calculate statistics → Display results
**Constants**: Define at top of functions; use descriptive names (e.g., `maxBytes`, `requiredColumns`)

## Key Patterns
- Validation errors display file name prefix (e.g., "New Leads: Missing required column")
- Required fields for joins: Quote #, Received at, Customer Phone (leads), Type/Direction/From/To/Date/Time (calls)
- Silent row filtering logs to console but never shows warnings to users
