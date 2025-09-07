# 🤖 LangChain Agent Demo

一个基于LangChain和DeepSeek的智能Agent演示项目，集成了文本翻译、文件翻译和AI对话功能，提供命令行和Web界面两种使用方式。

![image.png](https://fisherai-1312281807.cos.ap-guangzhou.myqcloud.com/20250907155652.png)


## ✨ 功能特性

### 🔧 核心功能
- **智能Agent对话**: 基于LangChain构建的AI助手，支持工具调用
- **多语言翻译**: 支持文本和文件的批量翻译
- **工具集成**: 内置天气查询、数学计算、时间查询等实用工具
- **记忆管理**: 支持对话上下文的保持和清空

### 🎨 界面支持
- **命令行界面**: 交互式终端操作
- **Web界面**: 基于Gradio的现代化Web应用
- **响应式设计**: 适配不同设备和屏幕尺寸

### 🛠️ 技术特性
- **模块化架构**: 清晰的代码结构，易于扩展
- **错误处理**: 完善的异常处理和用户提示
- **环境配置**: 灵活的环境变量配置
- **依赖管理**: 使用现代Python包管理工具

## 🚀 快速开始

### 环境要求
- Python >= 3.13
- 有效的DeepSeek API密钥

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd quick-agent-demo
   ```

2. **安装依赖**
   ```bash
   # 使用pip
   pip install -e .
   
   # 或使用uv（推荐）
   uv sync
   ```

3. **配置环境变量**
   ```bash
   # 复制环境变量模板
   cp env.example .env
   
   # 编辑.env文件，添加你的API密钥
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   ```

### 使用方式

#### 🌐 Web界面（推荐）

启动Web应用：
```bash
python run_gradio.py
```

访问地址：http://localhost:7860

**Web界面功能**：
- 📝 **文本翻译**: 实时多语言翻译
- 📄 **文件翻译**: 支持多种格式文件的批量翻译
- 💬 **AI聊天**: 智能对话助手，支持工具调用
- ℹ️ **关于页面**: 详细的功能说明

#### 💻 命令行界面

启动命令行应用：
```bash
python main.py
```

**命令行功能**：
- 单句翻译
- 批量句子翻译
- 文件翻译
- 交互式菜单操作

## 📁 项目结构

```
quick-agent-demo/
├── 📄 README.md                    # 项目说明文档
├── 📄 GRADIO_README.md            # Gradio界面使用指南
├── 📄 pyproject.toml              # 项目配置和依赖
├── 📄 env.example                 # 环境变量模板
├── 🚀 run_gradio.py               # Web界面启动脚本
├── 🖥️ main.py                     # 命令行主程序
├── 🌐 gradio_app.py               # Gradio Web应用
└── 📁 backend/                    # 后端模块
    ├── 📄 __init__.py
    ├── 🤖 agent_module.py         # Agent功能模块
    └── 💬 chat-prompt-template.py # 原始聊天模板
```

## 🔧 核心模块说明

### `backend/agent_module.py`
- **Agent核心**: 基于LangChain的智能Agent实现
- **工具定义**: 天气查询、数学计算、时间查询等工具
- **翻译功能**: 集成文本翻译能力
- **记忆管理**: 对话上下文的维护

### `gradio_app.py`
- **Web界面**: 基于Gradio的现代化Web应用
- **多标签页**: 翻译、聊天、文件处理等功能模块
- **状态管理**: 实时显示系统状态和错误信息
- **文件处理**: 支持文件上传和下载

### `main.py`
- **命令行界面**: 交互式终端应用
- **菜单系统**: 清晰的功能选择界面
- **文件操作**: 支持文件翻译和保存

## 🎯 使用示例

### Web界面使用

1. **文本翻译**
   ```
   输入语言: 中文
   输出语言: English
   待翻译文本: 你好，世界！
   结果: Hello, world!
   ```

2. **AI对话**
   ```
   用户: 今天北京的天气怎么样？
   Agent: 我来为您查询北京今天的天气...
   [调用天气工具]
   结果: 北京当前天气：25℃，晴
   ```

3. **文件翻译**
   - 上传文件（支持.txt, .md, .py等格式）
   - 选择源语言和目标语言
   - 自动翻译并下载结果文件

### 命令行使用

```bash
=== 高级翻译工具 ===

请选择操作:
1. 单句翻译
2. 批量句子翻译
3. 文件翻译
4. 退出

请输入选项: 1
输入语言: 中文
输出语言: English
待翻译文本: 这是一个测试
翻译结果: This is a test
```

## 🛠️ 开发指南

### 添加新工具

1. 在`backend/agent_module.py`中定义新工具：
   ```python
   @tool
   def new_tool(param: str):
       """工具描述"""
       return "工具结果"
   ```

2. 将工具添加到工具列表：
   ```python
   tools = [get_weather, calculate, get_current_time, new_tool]
   ```

3. 更新Agent提示模板以包含新工具的使用说明

### 自定义界面

1. **修改Web界面**: 编辑`gradio_app.py`中的界面布局
2. **添加新标签页**: 在`create_gradio_interface()`函数中添加新的Tab
3. **自定义主题**: 修改Gradio主题配置

### 环境配置

支持的环境变量：
```bash
# DeepSeek API配置
DEEPSEEK_API_KEY=your_api_key

# 智谱AI API配置（可选）
ZHIPUAI_API_KEY=your_api_key

# 其他配置
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_api_key
```

## 🐛 故障排除

### 常见问题

1. **Agent模块未加载**
   - 检查`.env`文件是否存在且配置正确
   - 确认API密钥有效且有足够配额
   - 查看控制台错误信息

2. **翻译功能异常**
   - 确认网络连接正常
   - 检查API服务状态
   - 验证输入语言格式

3. **Web界面无法访问**
   - 确认端口7860未被占用
   - 检查防火墙设置
   - 尝试使用不同端口

### 调试模式

启用详细日志：
```python
# 在gradio_app.py中
demo.launch(debug=True, show_error=True)
```

## 📊 技术栈

- **核心框架**: LangChain 0.3.7
- **大语言模型**: DeepSeek Chat
- **Web界面**: Gradio 4.0+
- **依赖管理**: Python 3.13+
- **环境管理**: python-dotenv

## 🤝 贡献指南

1. Fork项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [LangChain](https://github.com/langchain-ai/langchain) - 强大的LLM应用开发框架
- [DeepSeek](https://www.deepseek.com/) - 提供优秀的AI模型服务
- [Gradio](https://github.com/gradio-app/gradio) - 便捷的机器学习Web界面框架

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- 提交Issue
- 发送邮件
- 参与讨论

---

⭐ 如果这个项目对你有帮助，请给它一个星标！