# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🚀 Claude Code Optimization Mode ACTIVATED

**Token Saving Principles Applied:**
- Reference ClaudeCodeOptimizationGuide.md and QuickStartGuide.md for efficient interactions
- Use PromptTemplates.md for standardized requests
- Follow bilingual documentation format (English first, Chinese second)
- Provide concise, code-focused responses
- Apply three core principles: Templating, Context Reuse, Precise Output

## Repository Overview

This is a daily LeetCode practice repository where the author solves one problem per day throughout 2025. The repository tracks progress and documents learning in algorithm and data structure practice with full bilingual automation support.

## File Structure and Organization

- **solutions/YYYY-MM-DD/**: Daily solution directories containing:
  - `XXXX.py`: Python implementation with bilingual comments (English first, Chinese second)
  - `XXXX.md`: Bilingual documentation (English section first, then Chinese section)
- **scripts/**: Python automation scripts
  - `leetcode_daily.py`: Interactive daily problem setup
  - `solve_latest.py`: Automatic solution generator
- **tools/**: Shell utilities (`copy_folder.sh`)
- **docs/**: Documentation including CCTCRG optimization guides
- **daily, sol**: Main command shortcuts

## Common Development Tasks

### Quick Commands (Use these for efficiency)
```bash
# Setup new daily problem (interactive)
./daily [optional_url]

# Generate solution for latest problem
./sol
```

### Optimization Commands
Reference PromptTemplates.md for these efficient requests:
- "Create daily problem setup" → Use daily command template
- "Generate solution code" → Use sol command template  
- "Update bilingual docs" → Use documentation template

## Code Standards & Token Optimization

### Bilingual Code Format
```python
# English comment first
# 中文註釋在後
def solution_method(self, param: List[int]) -> int:
    pass
```

### Bilingual Documentation Structure
```markdown
# English Title

## English sections...

---

# 中文標題  

## 中文章節...
```

### Efficient Request Patterns
1. **Template Usage**: "Reference PromptTemplates.md, create [component]"
2. **Context Reuse**: Handle related tasks in same conversation  
3. **Precise Output**: "Output: Complete code file, no explanation"

### Algorithm Categories
- Binary search, sliding window, dynamic programming patterns
- Greedy algorithms, graph traversal, tree manipulation
- String processing, array manipulation, mathematical computations

## Development Guidelines

### Adding New Solutions
1. Create daily folder using `copy_folder.sh` or manually create `solutions/YYYY-MM-DD/`
2. Add `XXXX.py` with the solution implementation
3. Add `XXXX.md` with detailed explanation
4. Update README.md progress section with new entry

### Code Style
- Maintain existing Chinese comment style in Python files
- Use clear variable names and consistent indentation
- Follow LeetCode's method signature requirements
- Include complexity analysis in markdown documentation

### Git Workflow
- Use descriptive commit messages referencing problem numbers
- Main branch is the default branch for all changes
- Tag commits with problem-specific information when possible

## Testing

No automated testing framework is currently set up. Solutions are validated against LeetCode's test cases on their platform.