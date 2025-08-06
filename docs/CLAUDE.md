# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a daily LeetCode practice repository where the author solves one problem per day throughout 2025. The repository tracks progress and documents learning in algorithm and data structure practice.

## File Structure and Organization

- **solutions/YYYY-MM-DD/**: Daily solution directories containing:
  - `XXXX.py`: Python implementation for LeetCode problem XXXX
  - `XXXX.md`: Detailed explanation with approach, complexity analysis, and notes
- **copy_folder.sh**: Utility script to create new daily folders based on template
- **README.md**: Progress tracking and project documentation

## Common Development Tasks

### Creating New Daily Solutions
Use the provided shell script to create a new daily folder:
```bash
./copy_folder.sh
```
This creates a new folder with today's date and copies template files from the reference folder.

### Solution File Format
Each solution follows this structure:
- Python file with class-based solution implementing the required method
- Markdown file with detailed explanation including:
  - Problem approach and algorithm explanation
  - Time and space complexity analysis
  - Step-by-step code breakdown
  - Key insights and optimization notes

## Code Architecture

### Solution Structure
All Python solutions follow LeetCode's expected format:
- Class named `Solution`
- Method signature matching LeetCode requirements
- Type hints where applicable (e.g., `List[int]`)
- Chinese comments explaining the logic (preserve this commenting style)

### Problem Documentation
The markdown files provide comprehensive explanations:
- Algorithm approach description
- Binary search, sliding window, dynamic programming patterns
- Complexity analysis with Big O notation
- Code walkthrough with line-by-line explanations

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