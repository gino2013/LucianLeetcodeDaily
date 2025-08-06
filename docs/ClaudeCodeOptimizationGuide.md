# Claude Code Interactive Optimization Complete Guide

> 🚀 **Complete tutorial to maximize your $20 plan value**

## 📖 Table of Contents
1. [Quick Start](#quick-start)
2. [Project Integration Setup](#project-integration-setup)
3. [Efficient Interaction Techniques](#efficient-interaction-techniques)
4. [Token Saving Strategies](#token-saving-strategies)
5. [Practical Template Library](#practical-template-library)
6. [Frequently Asked Questions](#frequently-asked-questions)

---

## 🚀 Quick Start

### Step 1: Add this guide to your project
```bash
# Place this file in your project root directory
cp ClaudeCodeOptimizationGuide.md /your-project-root/
```

### Step 2: Opening statement for every interaction
```
Refer to ClaudeCodeOptimizationGuide.md in the project, please follow the token saving principles in your response.
```

### Step 3: Use structured prompts
```
Task: [Specific description]
Tech: [React/Node.js/Python etc.]
Output: [Code only/Need explanation]
Reference: ClaudeCodeOptimizationGuide.md
```

---

## 📁 Project Integration Setup

### Method 1: CLAUDE.md Memory System
Create `CLAUDE.md` in your project root directory:

```markdown
# Project Claude Code Usage Guide

## Project Overview
- Tech Stack: [Your tech stack]
- Architecture: [Project architecture description]
- Code Style: [ESLint/Prettier settings]

## Common Commands
- Development: `npm run dev`
- Testing: `npm test`
- Build: `npm run build`
- Lint: `npm run lint`

## Interaction Principles
Please refer to all suggestions in ClaudeCodeOptimizationGuide.md, especially:
- Use concise prompts
- Phased development
- Clear output format
```

### Method 2: Project Configuration File
Add to `package.json` or project documentation:

```json
{
  "claude-code": {
    "guidelines": "./ClaudeCodeOptimizationGuide.md",
    "memory": "./CLAUDE.md",
    "preferences": {
      "verbose": false,
      "format": "code-only",
      "structure": "modular"
    }
  }
}
```

---

## 💡 Efficient Interaction Techniques

### 1. Concise Prompt Formula
```
[Action] + [Object] + [Technology] + [Output Format]

Example:
Create + Login Form + React+TypeScript + Complete Component File
```

### 2. Layered Requirement Expression
```
Core Features: [Must-have]
Advanced Features: [Nice-to-have]  
Style Requirements: [UI/UX requirements]
Technical Constraints: [Must comply with]
```

### 3. Clear Success Criteria
```
Completion Standards:
✅ Function works properly
✅ Passes TypeScript check
✅ Follows project code style
✅ Includes error handling
```

---

## 🎯 Token Saving Core Strategies

### Strategy 1: Context Reuse
**Handle related tasks in one conversation**
```
First: Create user registration API
Second: Based on the previous API, add login functionality
Third: Add tests for these two APIs
```

### Strategy 2: Template-based Requests
**Establish common templates**
```
# React Component Template
Create [Component Name] component:
- Props: [Type definitions]
- Features: [Core feature list]
- Styling: Tailwind CSS
- Output: Complete .tsx file, no explanation

# API Endpoint Template
Implement [Endpoint Path] API:
- Method: [HTTP method]
- Parameters: [Request parameters]
- Response: [Return format]
- Output: Complete code with error handling
```

### Strategy 3: Precise Output Control
```
Output code only, no explanation
Output only modified parts
Output file content only, no preamble or postamble
```

---

## 📋 Practical Template Library

### Frontend Development Templates

#### React Component Development
```
Refer to ClaudeCodeOptimizationGuide.md, create [Component Name]:
- Features: [Core functionality points]
- Props: [TypeScript interface]
- State: [useState requirements]
- Styling: [Tailwind/CSS Modules]
- Output: Complete .tsx file
```

#### Page Development
```
Based on ClaudeCodeOptimizationGuide.md principles, create [Page Name] page:
- Route: [Path]
- Components: [Used components]
- Data: [API calls]
- SEO: [meta tags]
- Output: Complete page file
```

### Backend Development Templates

#### API Development
```
Following ClaudeCodeOptimizationGuide.md, implement [Feature] API:
- Endpoint: [HTTP method] /api/[path]
- Parameters: [Request body/query parameters]
- Validation: [Authentication/parameter validation]
- Response: [Success/error format]
- Output: Complete route file
```

#### Database Operations
```
Refer to guide principles, create [Entity] data operations:
- Model: [Data structure]
- CRUD: [Required operations]
- Relations: [Relationships with other tables]
- Output: Complete model/service file
```

---

## 📊 Token Usage Tracking

### Usage Monitoring Tools
Create a simple tracking table:

| Date | Task Type | Token Consumption | Saving Techniques | Effect |
|------|-----------|-------------------|-------------------|--------|
| 2024-01-01 | React Component | ~2000 | Use template | -30% |
| 2024-01-02 | API Development | ~1500 | Concise prompt | -25% |

### Cost Control Recommendations
```
Daily Budget Control:
- Important tasks: Priority processing
- Medium tasks: Use templates
- Simple tasks: Handle yourself when possible

Weekly Review:
- Analyze high-consumption tasks
- Optimize common templates
- Adjust usage strategy
```

---

## 🔧 Advanced Optimization Techniques

### 1. Code Library Creation
Create `claude-templates/` folder in your project:

```
claude-templates/
├── components/           # React component templates
├── api/                 # API endpoint templates
├── styles/              # Style templates
└── configs/             # Configuration file templates
```

### 2. Automated Prompts
Use shell script to automatically add prefix:

```bash
#!/bin/bash
# claude-prompt.sh
echo "Refer to ClaudeCodeOptimizationGuide.md, $1"
```

Usage:
```bash
./claude-prompt.sh "Create user management component"
```

### 3. Project-Specific Configuration
```markdown
# Record project-specific information in CLAUDE.md

## My Preference Settings
- Code Style: [Specific specifications]
- Common Libraries: [Frequently used packages]
- Naming Conventions: [Variable/function naming rules]
- File Structure: [Project directory structure]

## Things to Avoid
- Don't use [certain libraries]
- Don't create [certain file types]
- Don't add [unnecessary features]
```

---

## ❓ Frequently Asked Questions

### Q: How to make Claude Code remember my project settings?
A: Create a `CLAUDE.md` file in your project root directory and remind Claude to refer to it in every interaction.

### Q: When should I not use Claude Code?
A: 
- Simple one-line code changes
- Basic CSS adjustments
- Copy-paste repetitive work
- Pure refactoring/renaming

### Q: How to maximize token savings?
A:
1. Use templates from this guide
2. Handle related tasks in one conversation
3. Clearly specify output format
4. Avoid unnecessary explanations

### Q: How can project teams share these best practices?
A:
1. Add this guide to version control
2. Reference in team documentation
3. Build team-specific template library
4. Regularly share usage insights

---

## 🎯 Practical Examples

### Example 1: Complete Feature Development
```
Refer to ClaudeCodeOptimizationGuide.md, implement user authentication system:

Task: Complete user login/registration functionality
Tech: React + Node.js + JWT
Include: 
- Frontend login/registration forms (with validation)
- Backend API endpoints
- JWT token handling
- Error handling
Output: Provide separate complete files for frontend and backend
```

### Example 2: Extending Existing Code Base
```
Based on ClaudeCodeOptimizationGuide.md principles, extend existing shopping cart functionality:

Existing: Basic product addition functionality
New additions: 
- Quantity adjustment
- Product removal
- Total price calculation
- Coupon application
Output: Only modified functions, maintain existing structure
```

---

## 🚀 Getting Started

### Immediate Action Checklist
- [ ] Place this guide in project root directory
- [ ] Create `CLAUDE.md` to record project information
- [ ] Select 3-5 common templates
- [ ] Conduct first optimized interaction test
- [ ] Record token usage comparison

### Continuous Improvement
- Weekly review of usage effectiveness
- Adjust templates based on project needs
- Share best practices with team
- Continuously optimize prompt structure

---

**💰 Expected Results: Using this guide can save 40-60% of token consumption, making your Claude Code usage more efficient!**

> Remember: Always remind Claude to refer to this guide in every interaction!

---

---

# Claude Code 互動最佳化完整指南

> 🚀 **讓你的 $20 方案發揮最大價值的完整教學**

## 📖 目錄
1. [快速開始](#快速開始)
2. [專案整合設定](#專案整合設定)
3. [高效互動技巧](#高效互動技巧)
4. [Token 節省策略](#token-節省策略)
5. [實用模板庫](#實用模板庫)
6. [常見問題解答](#常見問題解答)

---

## 🚀 快速開始

### 第一步：將本指南加入你的專案
```bash
# 將此文件放在專案根目錄
cp ClaudeCodeOptimizationGuide.md /your-project-root/
```

### 第二步：每次互動時的開場白
```
參考專案中的 ClaudeCodeOptimizationGuide.md，請遵循其中的 token 節省原則來回應。
```

### 第三步：使用結構化 prompt
```
任務: [具體描述]
技術: [React/Node.js/Python等]
輸出: [只要代碼/需要解釋]
參考: ClaudeCodeOptimizationGuide.md
```

---

## 📁 專案整合設定

### 方法一：CLAUDE.md 記憶系統
在專案根目錄創建 `CLAUDE.md`：

```markdown
# 專案 Claude Code 使用指南

## 專案概況
- 技術棧: [你的技術棧]
- 架構: [專案架構說明]
- 代碼風格: [ESLint/Prettier設定]

## 常用指令
- 開發: `npm run dev`
- 測試: `npm test`
- 構建: `npm run build`
- 檢查: `npm run lint`

## 互動原則
請參考 ClaudeCodeOptimizationGuide.md 的所有建議，特別是：
- 使用精簡 prompt
- 分階段開發
- 明確輸出格式
```

### 方法二：專案配置文件
在 `package.json` 或專案說明中加入：

```json
{
  "claude-code": {
    "guidelines": "./ClaudeCodeOptimizationGuide.md",
    "memory": "./CLAUDE.md",
    "preferences": {
      "verbose": false,
      "format": "code-only",
      "structure": "modular"
    }
  }
}
```

---

## 💡 高效互動技巧

### 1. 精簡 Prompt 公式
```
[動作] + [對象] + [技術] + [輸出格式]

範例：
創建 + 登入表單 + React+TypeScript + 完整組件文件
```

### 2. 分層次需求表達
```
核心功能: [必須有的]
進階功能: [好有更好的]
樣式需求: [UI/UX要求]
技術限制: [必須遵守的]
```

### 3. 明確成功標準
```
完成標準:
✅ 功能正常運作
✅ 通過 TypeScript 檢查
✅ 符合專案代碼風格
✅ 包含錯誤處理
```

---

## 🎯 Token 節省核心策略

### 策略 1: 上下文復用
**一次對話處理相關任務**
```
第一次：創建用戶註冊 API
第二次：基於剛才的 API，添加登入功能
第三次：為這兩個 API 添加測試
```

### 策略 2: 模板化請求
**建立常用模板**
```
# React 組件模板
創建 [組件名] 組件：
- Props: [類型定義]
- 功能: [核心功能列表]  
- 樣式: Tailwind CSS
- 輸出: 完整 .tsx 文件，無解釋

# API 端點模板
實現 [端點路徑] API：
- 方法: [HTTP方法]
- 參數: [請求參數]
- 響應: [返回格式]
- 輸出: 完整代碼，含錯誤處理
```

### 策略 3: 精準輸出控制
```
只輸出代碼，不要解釋
只輸出修改的部分
只輸出文件內容，不要前言後語
```

---

## 📋 實用模板庫

### 前端開發模板

#### React 組件開發
```
參考 ClaudeCodeOptimizationGuide.md，創建 [組件名稱]：
- 功能: [核心功能點]
- Props: [TypeScript 介面]
- 狀態: [useState 需求]
- 樣式: [Tailwind/CSS Modules]
- 輸出: 完整 .tsx 文件
```

#### 頁面開發
```
基於 ClaudeCodeOptimizationGuide.md 原則，創建 [頁面名稱] 頁面：
- 路由: [路徑]
- 組件: [使用的組件]
- 數據: [API 調用]
- SEO: [meta 標籤]
- 輸出: 完整頁面文件
```

### 後端開發模板

#### API 開發
```
遵循 ClaudeCodeOptimizationGuide.md，實現 [功能] API：
- 端點: [HTTP方法] /api/[路徑]
- 參數: [請求體/查詢參數]
- 驗證: [身份驗證/參數驗證]  
- 響應: [成功/錯誤格式]
- 輸出: 完整路由文件
```

#### 數據庫操作
```
參考指南原則，創建 [實體] 數據操作：
- 模型: [數據結構]
- CRUD: [需要的操作]
- 關聯: [與其他表的關係]
- 輸出: 完整 model/service 文件
```

---

## 📊 Token 使用追蹤

### 使用量監控工具
建立簡單的追蹤表格：

| 日期 | 任務類型 | Token 消耗 | 節省技巧 | 效果 |
|------|----------|------------|----------|------|
| 2024-01-01 | React 組件 | ~2000 | 使用模板 | -30% |
| 2024-01-02 | API 開發 | ~1500 | 精簡 prompt | -25% |

### 成本控制建議
```
每日預算控制:
- 重要任務: 優先處理
- 中等任務: 使用模板
- 簡單任務: 盡量自己處理

每週回顧:
- 分析高耗用任務
- 優化常用模板
- 調整使用策略
```

---

## 🔧 進階優化技巧

### 1. 代碼庫建立
在專案中創建 `claude-templates/` 資料夾：

```
claude-templates/
├── components/           # React 組件模板
├── api/                 # API 端點模板  
├── styles/              # 樣式模板
└── configs/             # 配置文件模板
```

### 2. 自動化 Prompt
使用 shell script 自動添加前綴：

```bash
#!/bin/bash
# claude-prompt.sh
echo "參考 ClaudeCodeOptimizationGuide.md，$1"
```

使用方式：
```bash
./claude-prompt.sh "創建用戶管理組件"
```

### 3. 專案特定配置
```markdown
# 在 CLAUDE.md 中記錄專案特定信息

## 我的偏好設定
- 代碼風格: [具體規範]
- 常用庫: [經常使用的套件]
- 命名規範: [變數/函數命名規則]
- 文件結構: [專案目錄結構]

## 避免的做法
- 不要使用 [某些庫]
- 不要創建 [某類文件]
- 不要添加 [不必要的功能]
```

---

## ❓ 常見問題解答

### Q: 如何讓 Claude Code 記住我的專案設定？
A: 創建 `CLAUDE.md` 文件在專案根目錄，每次互動時提醒 Claude 參考該文件。

### Q: 什麼情況下不應該使用 Claude Code？
A: 
- 簡單的一行代碼修改
- 基本的 CSS 調整
- 複製貼上的重複工作
- 純粹的重構命名

### Q: 如何最大化節省 token？
A:
1. 使用本指南的模板
2. 一次對話處理相關任務
3. 明確指定輸出格式
4. 避免不必要的解釋

### Q: 專案團隊如何共享這些最佳實踐？
A:
1. 將本指南加入版本控制
2. 在團隊文檔中引用
3. 建立團隊專用的模板庫
4. 定期分享使用心得

---

## 🎯 實戰範例

### 範例 1: 完整功能開發
```
參考 ClaudeCodeOptimizationGuide.md，實現用戶認證系統：

任務: 完整的用戶登入/註冊功能
技術: React + Node.js + JWT
包含: 
- 前端登入/註冊表單 (含驗證)
- 後端 API 端點
- JWT token 處理
- 錯誤處理
輸出: 分別提供前後端完整文件
```

### 範例 2: 基於現有代碼的擴展
```
基於 ClaudeCodeOptimizationGuide.md 原則，擴展現有購物車功能：

現有: 基本的商品添加功能
新增: 
- 數量調整
- 商品移除  
- 總價計算
- 優惠券應用
輸出: 只需修改的函數，保持現有結構
```

---

## 🚀 開始使用

### 立即行動清單
- [ ] 將本指南放入專案根目錄
- [ ] 創建 `CLAUDE.md` 記錄專案信息  
- [ ] 選擇 3-5 個常用模板
- [ ] 進行第一次優化互動測試
- [ ] 記錄 token 使用量對比

### 持續改進
- 每週檢視使用效果
- 根據項目需求調整模板
- 與團隊分享最佳實踐
- 持續優化 prompt 結構

---

**💰 預期效果：使用本指南可節省 40-60% 的 token 消耗，讓你的 Claude Code 使用更高效！**

> 記住：每次與 Claude Code 互動時，都要提醒它參考這份指南！