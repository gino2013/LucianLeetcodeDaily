# Claude Code Quick Start Guide

> 🎯 **Learn the most effective Claude Code usage in 5 minutes**

## 🚀 Quick Start (2-minute setup)

### Step 1: Copy files to your project
```bash
# Copy all guide files to your project root directory
cp ClaudeCodeOptimizationGuide.md /your-project-root/
cp CLAUDE.md /your-project-root/
cp PromptTemplates.md /your-project-root/
cp QuickStartGuide.md /your-project-root/
```

### Step 2: Fill in project information
Edit `CLAUDE.md` and fill in your project details:
```markdown
- **Project Name**: [Your project name]
- **Tech Stack**: [e.g., React + TypeScript + Node.js]
- **Development Command**: `npm run dev`
- **Test Command**: `npm test`
```

### Step 3: First optimized interaction
Copy this text to Claude Code:
```
Refer to ClaudeCodeOptimizationGuide.md and CLAUDE.md in the project, please follow token saving principles.

Test task: Create a simple Hello World component
Tech: [Your tech stack]
Output: Complete .tsx file, no explanation
```

---

## 📋 Complete Usage Process

### 🔧 Phase 1: Environment Setup (First-time setup)

#### 1.1 File Deployment Checklist
- [ ] `ClaudeCodeOptimizationGuide.md` - Main guide
- [ ] `CLAUDE.md` - Project memory file
- [ ] `PromptTemplates.md` - Template library
- [ ] `QuickStartGuide.md` - This guide

#### 1.2 Project Information Setup
Fill in `CLAUDE.md`:
- [ ] Basic project information
- [ ] Tech stack and development commands
- [ ] Code style preferences
- [ ] Project structure description

#### 1.3 Establish Template Habits
Bookmark 3-5 most commonly used templates:
- [ ] Basic interaction template
- [ ] Your main development template (React/Vue/API etc.)
- [ ] Error fixing template
- [ ] Code refactoring template

### 🎯 Phase 2: Daily Usage Process

#### 2.1 Standard Format for Every Interaction
```
[Step 1] Reference guide
Refer to ClaudeCodeOptimizationGuide.md and CLAUDE.md in the project

[Step 2] Use template
Select appropriate template from PromptTemplates.md

[Step 3] Fill in specific requirements
[Specific task description]

[Step 4] Specify output format
Output: [Code only/Need explanation]
```

#### 2.2 Best Practices for Common Tasks

**New Feature Development:**
```
Refer to CLAUDE.md settings, create [Feature Name]:
- Features: [Core feature list]
- Tech: [Tech stack used]
- Integration: [How to integrate with existing code]
- Output: Complete implementation code
```

**Bug Fixing:**
```
Based on project standards, fix [Specific Error]:
- Symptoms: [Error manifestation]
- Expected: [Correct behavior]
- Scope: [Impact scope]
- Output: Fixed code with explanation
```

**Code Refactoring:**
```
Refer to optimization guide, refactor [Target Code]:
- Issues: [Current problems]
- Goals: [Refactoring objectives]
- Preserve: [Must-retain functionality]
- Output: Refactored code
```

#### 2.3 Batch Task Processing
When you have multiple related tasks:
```
Refer to guide principles, batch process:
1. [Task one description]
2. [Task two description]
3. [Task three description]

Requirements: Complete all tasks in one conversation
```

---

## 💡 Advanced Usage Techniques

### 🔄 Context Reuse Strategy

#### Technique 1: Sequential Development
```
First: Create basic API endpoint
Second: Based on the previous API, add authentication middleware
Third: Create frontend calling functions for these APIs
Fourth: Add error handling and loading states
```

#### Technique 2: Progressive Enhancement
```
Phase 1: Implement core functionality
Phase 2: Based on previous code, add styling
Phase 3: On existing foundation, add advanced features
```

### 📊 Token Usage Monitoring with Advanced Tools

> **📝 Attribution Note**: The following tool introduction content is partially referenced from online community sharing and developer community discussions, organized and supplemented for inclusion in this guide. Main sources include V2EX community discussions, GitHub project documentation, etc.

#### Discovering the Game-Changers
While browsing V2EX one evening, I discovered a post about "ccusage" - a tool specifically designed to analyze Claude Code token usage. This was exactly what I'd been looking for!

The reality is, every time I code with Claude Code, I enjoy the process but constantly worry about unknowingly exhausting my tokens. Especially when I'm in the flow state, I don't want to stop, but I'm always concerned about accidentally exceeding limits.

#### Tool 1: ccusage - Comprehensive Usage Analysis
**Installation:**
```bash
npm install -g ccusage
```

**Key Features:**
- `ccusage daily` - View today's usage
- `ccusage monthly` - Monthly usage trends  
- `ccusage session` - Detailed session breakdown
- `ccusage blocks` - 5-hour block statistics (matches Claude Code billing)
- `ccusage blocks --live` - Real-time monitoring (updates every 3 seconds)

**Why It's Amazing:**
Claude Code stores all usage records locally in JSONL files. ccusage analyzes these files to show token counts, cost estimates, usage times, and even calculates API cost comparisons to show how much Claude Code saves you.

#### Tool 2: Claude-Code-Usage-Monitor - Real-time Dashboard

**Installation:**
```bash
git clone https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor.git
cd Claude-Code-Usage-Monitor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Usage:**
```bash
# For Max plan (20 hours, 1M tokens)
./ccusage_monitor.py --plan max20

# For 5-hour plan (200K tokens)  
./ccusage_monitor.py --plan max5

# Auto-detect from history
./ccusage_monitor.py --plan custom_max
```

**Features:**
- Beautiful real-time monitoring dashboard
- Progress bars with usage predictions
- Timezone and reset hour customization
- Background monitoring with tmux support

#### Practical Workflow Integration

**Daily Routine:**
```bash
# Check morning usage
ccusage daily

# Start real-time monitoring
claude-monitor  # (set as alias)

# Background monitoring
tmux new-session -d -s claude-monitor './ccusage_monitor.py --plan max20'
```

**Pro Tips:**
```bash
# Create convenient alias
alias claude-monitor='cd ~/Claude-Code-Usage-Monitor && source venv/bin/activate && ./ccusage_monitor.py --plan max20'

# Timezone customization
./ccusage_monitor.py --plan max20 --reset-hour 8 --timezone America/New_York

# Accurate cost calculation
ccusage --mode calculate
```

#### Additional Ecosystem Tools
- **CCSeva**: Mac menu bar application for usage display
- **Raycast Extension**: Check usage directly in Raycast
- **ccusage Raycast Store**: Official extension by the developer

#### Impact on Development Workflow
These tools completely changed my approach to Claude Code:

**Before:** Constantly worried about token usage, conservative in experimentation
**After:** Clear usage awareness, confident exploration, data-driven work planning

**Usage Pattern Insights:**
- Complex refactoring tasks consume tokens quickly
- New feature development has stable consumption  
- Bug fixes are generally token-efficient
- Template usage significantly reduces consumption

**Monthly Analysis Benefits:**
- Identify high-consumption scenarios
- Optimize work scheduling around reset times
- Plan important coding sessions strategically
- Track improvement in token efficiency over time

#### 🔗 Tool Attribution
- **ccusage**: Developed by [ryoppippi](https://github.com/ryoppippi), Project: https://github.com/ryoppippi/ccusage
- **Claude-Code-Usage-Monitor**: Developed by [Maciek-roboblog](https://github.com/Maciek-roboblog), Project: https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor
- **CCSeva**: Mac menu bar application
- **Content Sources**: Partially referenced from V2EX community discussions and developer sharing

---

## 🎓 Learning Path

### 👶 Beginner Stage (Weeks 1-2)
**Goal**: Master basic usage process
- [ ] Complete environment setup
- [ ] Try all basic templates
- [ ] Record 3-5 common scenarios
- [ ] Establish personal usage habits

**Recommended Practice**:
- Use at least 1 template daily
- Compare token consumption before/after using templates
- Record which templates work best for your work

### 🧑‍💻 Advanced Stage (Weeks 3-4)
**Goal**: Optimize personal workflow
- [ ] Customize 3-5 specialized templates
- [ ] Establish batch processing workflow
- [ ] Optimize context reuse strategy
- [ ] Analyze usage data and adjust

**Recommended Practice**:
- Try completing complex tasks in one conversation
- Experiment with different prompt combinations
- Share usage insights with team

### 🚀 Expert Stage (Week 5+)
**Goal**: Establish team best practices
- [ ] Build team template library
- [ ] Establish team usage standards
- [ ] Automate common workflows
- [ ] Continuous optimization and innovation

**Recommended Practice**:
- Write team usage guides
- Establish template sharing mechanisms
- Regular workflow review and optimization

---

## 🛠️ Troubleshooting

### Common Issues and Solutions

#### Q1: Claude doesn't refer to my guide files
**Solution**:
```
Make sure to clearly mention at the beginning of every interaction:
"Refer to ClaudeCodeOptimizationGuide.md and CLAUDE.md in the project"
```

#### Q2: Generated code doesn't match project style
**Solution**:
1. Check code style settings in `CLAUDE.md`
2. Describe style requirements more specifically
3. Provide existing code examples for reference

#### Q3: Token consumption is still high
**Solution**:
1. Check if templates are being used
2. Avoid requesting too much explanation
3. Batch process related tasks
4. Clearly specify output format

#### Q4: Templates don't fit my needs
**Solution**:
1. Add custom templates in `PromptTemplates.md`
2. Record special requirements in `CLAUDE.md`
3. Gradually adjust and optimize templates

---

## 📈 Effect Evaluation

### Success Metrics
- **Token Savings Rate**: Target 40-60%
- **Development Efficiency**: Reduce repetitive description time
- **Code Quality**: More consistent code style
- **Learning Curve**: Team adoption speed

### Regular Checklist (Weekly)
- [ ] Check token usage trends
- [ ] Update commonly used templates
- [ ] Optimize CLAUDE.md settings
- [ ] Record new usage scenarios

### Continuous Improvement Suggestions
1. **Monthly Review**: Analyze usage data, adjust strategies
2. **Quarterly Optimization**: Update template library, share best practices
3. **Annual Assessment**: Calculate total savings, set next year's goals

---

## 🔗 Related Resources

### Core File Links
- [Complete Optimization Guide](./ClaudeCodeOptimizationGuide.md)
- [Project Memory File](./CLAUDE.md)
- [Template Library](./PromptTemplates.md)

### Extended Learning
- Claude Code Official Documentation
- Token Calculation Tools
- Prompt Engineering Best Practices

---

## 🎯 Action Plan

### Start Today (15 minutes)
- [ ] Copy files to project directory (2 minutes)
- [ ] Fill in CLAUDE.md basic information (5 minutes)
- [ ] Select 3-5 commonly used templates (3 minutes)
- [ ] Conduct first optimized interaction test (5 minutes)

### This Week Goals
- [ ] Complete all basic setup
- [ ] Try each template at least once
- [ ] Record usage effects and issues
- [ ] Establish personal usage habits

### This Month Goals
- [ ] Achieve 40%+ token savings
- [ ] Establish stable usage workflow
- [ ] Optimize personal template library
- [ ] Share usage insights

---

**🎉 Congratulations! You've mastered efficient Claude Code usage. Start now and make every token count!**

---

---

# Claude Code 快速上手指南

> 🎯 **5 分鐘學會最有效的 Claude Code 使用方法**

## 🚀 立即開始（2 分鐘設定）

### 步驟 1: 複製文件到專案
```bash
# 複製所有指南文件到你的專案根目錄
cp ClaudeCodeOptimizationGuide.md /your-project-root/
cp CLAUDE.md /your-project-root/
cp PromptTemplates.md /your-project-root/
cp QuickStartGuide.md /your-project-root/
```

### 步驟 2: 填寫專案信息
編輯 `CLAUDE.md`，填入你的專案資訊：
```markdown
- **專案名稱**: [你的專案名稱]
- **技術棧**: [例如: React + TypeScript + Node.js]
- **開發指令**: `npm run dev`
- **測試指令**: `npm test`
```

### 步驟 3: 第一次優化互動
複製這段文字到 Claude Code：
```
參考專案中的 ClaudeCodeOptimizationGuide.md 和 CLAUDE.md，請遵循 token 節省原則。

測試任務: 創建一個簡單的 Hello World 組件
技術: [你的技術棧]
輸出: 完整 .tsx 文件，無解釋
```

---

## 📋 完整使用流程

### 🔧 Phase 1: 環境準備（首次設定）

#### 1.1 文件部署檢查清單
- [ ] `ClaudeCodeOptimizationGuide.md` - 主要指南
- [ ] `CLAUDE.md` - 專案記憶文件  
- [ ] `PromptTemplates.md` - 模板庫
- [ ] `QuickStartGuide.md` - 本指南

#### 1.2 專案資訊設定
在 `CLAUDE.md` 中填寫：
- [ ] 專案基本信息
- [ ] 技術棧和開發指令
- [ ] 代碼風格偏好
- [ ] 專案結構說明

#### 1.3 建立模板習慣
選擇 3-5 個最常用的模板加入書籤：
- [ ] 基礎互動模板
- [ ] 你的主要開發模板（React/Vue/API等）
- [ ] 錯誤修復模板
- [ ] 代碼重構模板

### 🎯 Phase 2: 日常使用流程

#### 2.1 每次互動的標準格式
```
[步驟 1] 引用指南
參考專案中的 ClaudeCodeOptimizationGuide.md 和 CLAUDE.md

[步驟 2] 使用模板
從 PromptTemplates.md 選擇合適模板

[步驟 3] 填入具體需求
[具體任務描述]

[步驟 4] 指定輸出格式
輸出: [只要代碼/需要解釋]
```

#### 2.2 常見任務的最佳實踐

**開發新功能：**
```
參考 CLAUDE.md 設定，創建 [功能名稱]：
- 功能: [核心功能列表]
- 技術: [使用的技術棧]
- 整合: [與現有代碼的整合方式]  
- 輸出: 完整實現代碼
```

**修復 Bug：**
```
基於專案規範，修復 [具體錯誤]：
- 現象: [錯誤表現]
- 期望: [正確行為]
- 範圍: [影響範圍]
- 輸出: 修復代碼及說明
```

**代碼重構：**
```
參考優化指南，重構 [目標代碼]：
- 問題點: [當前問題]
- 目標: [重構目標]
- 保持: [必須保留的功能]
- 輸出: 重構後代碼
```

#### 2.3 批量任務處理
當有多個相關任務時：
```
參考指南原則，批量處理：
1. [任務一描述]
2. [任務二描述]
3. [任務三描述]

要求: 一次對話完成所有任務
```

---

## 💡 進階使用技巧

### 🔄 上下文復用策略

#### 技巧 1: 連續開發
```
第一次: 創建基礎 API 端點
第二次: 基於剛才的 API，添加認證中間件
第三次: 為這些 API 創建前端調用函數
第四次: 添加錯誤處理和 loading 狀態
```

#### 技巧 2: 漸進式完善
```
第一階段: 實現核心功能
第二階段: 基於剛才的代碼，添加樣式
第三階段: 在現有基礎上，加入進階功能
```

### 📊 進階工具實現 Token 使用監控

> **📝 引用說明**: 以下工具介紹內容部分引用自網路社群分享和開發者社群討論，經過整理和補充後納入本指南。主要來源包括 V2EX 社群討論、GitHub 項目文檔等。

#### 意外的發現
那天晚上在V2EX上閒逛，看到有人發了一個帖子說「發現了一個神器：ccusage，專門用來分析Claude Code的token使用情況」。我當時就想，這不就是我一直在找的東西嗎？

說實話，自從開始用Claude Code，我就一直有個心病。你懂的，每次寫代碼的時候都很爽，但總是擔心會不會不知不覺就把token用完了。特別是進入狀態的時候，根本不想停下來，可是又怕一不小心就超額了。

#### 工具一：ccusage - 全面使用分析

**安裝方式：**
```bash
npm install -g ccusage
```

**核心功能：**
- `ccusage daily` - 查看當天使用情況
- `ccusage monthly` - 每月使用趨勢
- `ccusage session` - 詳細會話記錄
- `ccusage blocks` - 5小時區塊統計（符合Claude Code計費方式）
- `ccusage blocks --live` - 實時監控（每3秒更新）

**為什麼這麼神奇：**
原來Claude Code會把所有的使用記錄都保存在本地的JSONL文件中。ccusage就是分析這些文件，顯示token數量、成本估算、使用時間，還能計算出如果用API的話要花多少錢，讓你知道Claude Code到底幫你省了多少。

#### 工具二：Claude-Code-Usage-Monitor - 實時監控儀表板

**安裝過程：**
```bash
git clone https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor.git
cd Claude-Code-Usage-Monitor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**使用方式：**
```bash
# Max計劃（20小時，100萬token）
./ccusage_monitor.py --plan max20

# 5小時計劃（20萬token）
./ccusage_monitor.py --plan max5

# 自動從歷史記錄中偵測
./ccusage_monitor.py --plan custom_max
```

**強大功能：**
- 美觀的實時監控儀表板
- 帶使用預測的進度條
- 時區和重置時間自定義
- 支援tmux後台監控

#### 實際工作流程整合

**每日例行公事：**
```bash
# 檢查早上使用情況
ccusage daily

# 啟動實時監控
claude-monitor  # （設定為別名）

# 後台監控
tmux new-session -d -s claude-monitor './ccusage_monitor.py --plan max20'
```

**進階技巧：**
```bash
# 設定方便的別名
alias claude-monitor='cd ~/Claude-Code-Usage-Monitor && source venv/bin/activate && ./ccusage_monitor.py --plan max20'

# 時區自定義
./ccusage_monitor.py --plan max20 --reset-hour 8 --timezone America/New_York

# 精確成本計算
ccusage --mode calculate
```

#### 生態系統中的其他工具
- **CCSeva**：Mac選單列應用程式顯示使用情況
- **Raycast擴展**：直接在Raycast中查看使用情況
- **ccusage Raycast Store**：開發者官方擴展

#### 對開發工作流程的影響
這些工具完全改變了我使用Claude Code的方式：

**以前：** 總是提心吊膽，不敢大膽實驗
**現在：** 使用狀況一清二楚，可以放心探索，根據數據規劃工作

**使用模式洞察：**
- 複雜重構任務token消耗特別快
- 新功能開發相對穩定
- Bug修復通常比較節省token
- 使用模板能顯著減少消耗

**月度分析的好處：**
- 識別高耗用場景
- 根據重置時間優化工作安排
- 策略性規劃重要編碼工作
- 追蹤token效率的改善情況

#### 🔗 工具引用資訊
- **ccusage**: 由 [ryoppippi](https://github.com/ryoppippi) 開發，項目地址：https://github.com/ryoppippi/ccusage
- **Claude-Code-Usage-Monitor**: 由 [Maciek-roboblog](https://github.com/Maciek-roboblog) 開發，項目地址：https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor
- **CCSeva**: Mac 選單列應用程式
- **內容來源**: 部分內容參考 V2EX 社群討論和開發者分享

---

## 🎓 學習路徑

### 👶 新手階段（第 1-2 週）
**目標**: 熟悉基本使用流程
- [ ] 完成環境設定
- [ ] 嘗試所有基礎模板
- [ ] 記錄 3-5 個常用場景
- [ ] 建立個人使用習慣

**推薦練習**:
- 每天至少使用 1 個模板
- 對比使用模板前後的 token 消耗
- 記錄哪些模板最適合你的工作

### 🧑‍💻 進階階段（第 3-4 週）  
**目標**: 優化個人工作流程
- [ ] 自定義 3-5 個專用模板
- [ ] 建立批量處理流程
- [ ] 優化上下文復用策略
- [ ] 分析使用數據並調整

**推薦練習**:
- 嘗試一次對話完成複雜任務
- 實驗不同的 prompt 組合
- 分享使用心得給團隊

### 🚀 專家階段（第 5+ 週）
**目標**: 建立團隊最佳實踐
- [ ] 建立團隊模板庫
- [ ] 制定團隊使用規範
- [ ] 自動化常用流程
- [ ] 持續優化和創新

**推薦實踐**:
- 編寫團隊使用指南
- 建立模板分享機制
- 定期檢討和優化流程

---

## 🛠️ 故障排除

### 常見問題及解決方案

#### Q1: Claude 沒有參考我的指南文件
**解決方案**:
```
請確保在每次互動開頭明確提及：
"參考專案中的 ClaudeCodeOptimizationGuide.md 和 CLAUDE.md"
```

#### Q2: 生成的代碼不符合專案風格
**解決方案**:
1. 檢查 `CLAUDE.md` 中的代碼風格設定
2. 更具體地描述風格要求
3. 提供現有代碼範例供參考

#### Q3: Token 消耗仍然很高
**解決方案**:
1. 檢查是否使用了模板
2. 避免要求過多解釋
3. 批量處理相關任務
4. 明確指定輸出格式

#### Q4: 模板不符合我的需求
**解決方案**:
1. 在 `PromptTemplates.md` 中添加自定義模板
2. 在 `CLAUDE.md` 中記錄特殊需求
3. 逐漸調整和優化模板

---

## 📈 效果評估

### 成功指標
- **Token 節省率**: 目標 40-60%
- **開發效率**: 減少重複性描述時間
- **代碼品質**: 更一致的代碼風格
- **學習曲線**: 團隊採用速度

### 定期檢查清單（每週）
- [ ] 檢查 token 使用趨勢
- [ ] 更新常用模板
- [ ] 優化 CLAUDE.md 設定
- [ ] 記錄新的使用場景

### 持續改進建議
1. **月度回顧**: 分析使用數據，調整策略
2. **季度優化**: 更新模板庫，分享最佳實踐  
3. **年度評估**: 計算總體節省效果，制定來年目標

---

## 🔗 相關資源

### 核心文件連結
- [完整優化指南](./ClaudeCodeOptimizationGuide.md)
- [專案記憶文件](./CLAUDE.md)
- [模板庫](./PromptTemplates.md)

### 延伸學習
- Claude Code 官方文檔
- Token 計算工具
- 提示工程最佳實踐

---

## 🎯 行動計劃

### 今天就開始（15 分鐘）
- [ ] 複製文件到專案 (2 分鐘)
- [ ] 填寫 CLAUDE.md 基本信息 (5 分鐘)  
- [ ] 選擇 3 個常用模板 (3 分鐘)
- [ ] 進行第一次優化互動測試 (5 分鐘)

### 本週目標
- [ ] 完成所有基礎設定
- [ ] 嘗試每種模板至少一次
- [ ] 記錄使用效果和問題
- [ ] 建立個人使用習慣

### 本月目標  
- [ ] 實現 40% 以上 token 節省
- [ ] 建立穩定的使用流程
- [ ] 優化個人模板庫
- [ ] 分享使用心得

---

**🎉 恭喜！你已經掌握了 Claude Code 的高效使用方法。立即開始，讓每一個 token 都發揮最大價值！**