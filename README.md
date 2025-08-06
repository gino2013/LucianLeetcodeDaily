# LucianLeetCodeDaily

## Description
This repository serves as a comprehensive log of my daily LeetCode practice challenges throughout 2025. My goal is to systematically enhance my proficiency in algorithms, data structures, and problem-solving techniques by tackling one problem each day. All solutions are implemented in Python, accompanied by detailed explanations of the approach, time complexity, and space complexity. This project is designed to track my progress, document my learning journey, and prepare for technical interviews or competitive programming. I warmly invite fellow developers, learners, and enthusiasts to join me on this endeavor, share insights, and grow together!

## Project Background
Initiated on March 4, 2025, this repository reflects my commitment to continuous learning and skill development in computer science. Inspired by the need to strengthen my foundation for software engineering roles, I aim to cover a wide range of LeetCode problems, spanning Easy, Medium, and Hard difficulties. The solutions are version-controlled using Git, hosted on GitHub, and organized by date for easy reference. This project also serves as a portfolio piece to demonstrate my coding consistency and problem-solving capabilities.

## Progress
- **2025-03-04**: [Powers of Three](solutions/2025-03-04/1780.py)  
  - Problem ID: [LeetCode #1780](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)  
  - Approach: Greedy algorithm with \( O(\log_3 n) \) time complexity and \( O(1) \) space complexity.  
  - Notes: Utilized the property of ternary representation to ensure distinct powers of three.  
- **2025-03-05**: [Count Total Number of Colored Cells](solutions/2025-03-05/2579.py)  
  - Problem ID: [LeetCode #2579](https://leetcode.com/problems/count-total-number-of-colored-cells/)   
  - Approach: Mathematical formula with \( O(1) \) time complexity and \( O(1) \) space complexity.  
  - Notes: Derived a quadratic formula \( f(n) = 2n^2 - 2n + 1 \) from pattern observation and solved using algebraic equations.
- **2025-03-06**: [Find Missing and Repeated Values](solutions/2025-03-06/2965.py)  
  - Problem ID: [LeetCode #2965](https://leetcode.com/problems/find-missing-and-repeated-values/)  
  - Approach: Counting and Comparison with O(n²) time complexity and O(n²) space complexity.
  - Notes: The algorithm efficiently finds the repeated and missing values by first counting the    occurrences of each element in the grid using a hash table (dictionary). Then, it iterates through the expected value range [1, n*n] to identify the repeated and missing numbers.
- **2025-03-08**: [Minimum Recolors to Get k Consecutive Black Blocks](solutions/2025-03-08/2379.py)
  - Problem ID: [LeetCode #2379](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/)
  - Approach: Sliding Window with ( O(n) ) time complexity and ( O(1) ) space complexity.
  - Notes: Utilized a sliding window of size ( k ) to efficiently calculate the minimum number of recoloring operations needed.
- **2025-03-09**: [Count of Substrings Containing Every Vowel and K Consonants II](solutions/2025-03-09/3141.py)
  - Problem ID: [LeetCode #3141](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/)
  - Approach: Sliding Window with Precomputation, \( O(n) \) time complexity and \( O(1) \) space complexity.
  - Notes: This solution counts the number of substrings with exactly \( k \) consonants and all five vowels. It uses a sliding window, precomputes the next consonant index for optimization, and maintains vowel counts to efficiently identify valid substrings.
- **...** (More entries will be added daily)

## Goals
- **Daily Commitment**: Solve and document at least one LeetCode problem each day in 2025, targeting a minimum of 365 problems.
- **Skill Enhancement**: Master core computer science concepts, including dynamic programming, graph traversal, binary search, and more.
- **Interview Preparation**: Build a robust problem-solving toolkit to excel in technical interviews for software engineering positions.
- **Community Engagement**: Foster a collaborative environment by sharing knowledge and receiving feedback.

## Quick Start Commands

### **Daily Problem Setup**
Create and set up today's LeetCode problem template:
```bash
./daily [optional_leetcode_url]
```

**Interactive Setup Process:**
1. Input problem number (e.g., `3479`)
2. Input English title (e.g., `Fruits Into Baskets III`)
3. Input Chinese title (e.g., `水果成籃 III`)  
4. Input difficulty (`Easy`/`Medium`/`Hard`)
5. Paste problem description (end with `Ctrl+D` or double enter)

**Generated Files:**
- `solutions/YYYY-MM-DD/XXXX.py` - Python template with bilingual comments
- `solutions/YYYY-MM-DD/XXXX.md` - Bilingual markdown documentation (English first, Chinese second)

### **Auto Solution Generator**
Generate solution for the most recent problem:
```bash
./sol
```

**What it does:**
- Automatically finds the latest date folder
- Analyzes the problem files  
- Generates complete solution code with bilingual comments
- Updates both Python and Markdown files
- For problem 3479: Generates full Greedy Algorithm implementation
- For other problems: Generates template structure

### **Example Workflow**
```bash
# 1. Set up today's problem
./daily "https://leetcode.com/problems/fruits-into-baskets-iii/"

# 2. Generate solution automatically  
./sol

# 3. Your files are ready with complete bilingual documentation!
```

## Technical Details
- **Programming Language**: Python 3.x (preferred for its readability and extensive libraries).
- **Version Control**: Managed with Git, using the `main` branch as the default.
- **File Structure**:
  - `solutions/YYYY-MM-DD/`: Daily solution files (e.g., `.py` for code, `.md` for explanations).
  - `daily` & `leetcode_daily.py`: Problem setup automation scripts
  - `sol` & `solve_latest.py`: Solution generation automation scripts
  - `copy_folder.sh`: Utility for creating daily folders
- **Documentation Format**: 
  - **Bilingual Support**: All files contain both English and Chinese
  - **Python Files**: Bilingual inline comments (English first, Chinese second)
  - **Markdown Files**: English version first, then Chinese version separated by `---`
  - **Auto-Generated**: Complete problem analysis, complexity analysis, and examples

## How to Contribute
I welcome contributions and discussions from the community! Here's how you can get involved:
- **Suggest Solutions**: Propose alternative approaches or optimizations for existing problems.
- **Discuss Approaches**: Open an issue or pull request to share your insights or ask questions.
- **Report Issues**: If you find errors in my code or documentation, please submit an issue with details.
- **Fork and Collaborate**: Fork this repository, add your solutions, and submit a pull request for review.

### Contribution Guidelines
1. Fork the repository and create a branch for your changes (e.g., `feature/new-solution`).
2. Add your solution under the appropriate date folder (e.g., `solutions/2025-03-05/`).
3. Include a Markdown file with your approach and analysis.
4. Submit a pull request with a clear description of your contribution.
5. I will review and provide feedback or merge your changes.

## Contact
- **GitHub**: [@gino2013](https://github.com/gino2013) 
- **Email**: [csluling@hotmail.com](mailto:csluling@hotmail.com) 
- **Feedback**: Feel free to reach out via GitHub Issues for questions, collaborations, or suggestions.

## License
This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by the LeetCode community and resources like NeetCode, LeetCode Discuss, and various online tutorials.
- Thanks to my peers and mentors for their continuous support and encouragement.