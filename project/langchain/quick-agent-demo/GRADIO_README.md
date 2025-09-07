# Gradio Web界面使用指南

## 🚀 快速开始

### 1. 安装依赖
```bash
# 安装项目依赖
pip install -e .

# 或者使用uv（推荐）
uv sync
```

### 2. 配置环境变量
创建 `.env` 文件并配置必要的API密钥：
```bash
# DeepSeek API配置
DEEPSEEK_API_KEY=your_api_key_here
```

### 3. 启动Web界面
```bash
# 使用启动脚本（推荐）
python run_gradio.py

# 或者直接运行
python gradio_app.py
```

## 🌐 访问界面

启动后，在浏览器中访问：
- **本地访问**: http://localhost:7860
- **网络访问**: http://0.0.0.0:7860

## 📱 功能说明

### 1. 文本翻译
- 支持多种语言的文本翻译
- 输入源语言和目标语言
- 实时翻译结果

### 2. 文件翻译
- 支持多种文件格式：`.txt`, `.md`, `.py`, `.js`, `.html`, `.css`
- 批量翻译文件内容
- 自动保存翻译结果

### 3. AI Agent聊天
- 智能对话助手
- 支持工具调用（天气查询、数学计算、时间查询）
- 保持对话上下文

## 🛠️ 技术特性

- **响应式设计**: 适配不同屏幕尺寸
- **实时状态**: 显示Agent模块加载状态
- **错误处理**: 友好的错误提示
- **文件上传**: 支持拖拽上传文件
- **聊天历史**: 保持对话记录

## 🔧 自定义配置

### 修改端口
在 `gradio_app.py` 中修改：
```python
demo.launch(
    server_port=8080,  # 修改端口号
    # ... 其他配置
)
```

### 启用公共链接
```python
demo.launch(
    share=True,  # 创建公共链接
    # ... 其他配置
)
```

## 🐛 故障排除

### 常见问题

1. **Agent模块未加载**
   - 检查 `.env` 文件是否存在
   - 确认API密钥配置正确
   - 查看控制台错误信息

2. **翻译功能不工作**
   - 确认网络连接正常
   - 检查API配额是否充足
   - 验证输入语言格式

3. **文件上传失败**
   - 检查文件格式是否支持
   - 确认文件大小限制
   - 查看文件编码格式

### 调试模式
启动时添加调试信息：
```python
demo.launch(debug=True, show_error=True)
```

## 📝 开发说明

### 项目结构
```
├── gradio_app.py          # Gradio主应用
├── run_gradio.py          # 启动脚本
├── backend/
│   ├── agent_module.py    # Agent功能模块
│   └── chat-prompt-template.py  # 原始模块
└── pyproject.toml         # 项目配置
```

### 添加新功能
1. 在 `backend/agent_module.py` 中添加新工具
2. 在 `gradio_app.py` 中创建对应的界面函数
3. 更新界面布局和事件绑定

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

本项目采用MIT许可证。
