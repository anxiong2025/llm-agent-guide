import gradio as gr
import sys
import os
from dotenv import load_dotenv
from typing import List, Tuple

# 加载环境变量
load_dotenv()

# 导入agent模块
try:
    from backend.agent_module import translate_text, chat_with_agent, clear_agent_memory
    agent_available = True
except ImportError as e:
    print(f"导入agent模块失败: {str(e)}")
    agent_available = False

# 全局变量存储聊天历史
chat_history = []

def translate_text_interface(input_lang: str, output_lang: str, text: str) -> str:
    """翻译文本的Gradio接口函数"""
    if not agent_available:
        return "错误：Agent模块未正确加载"
    
    if not text.strip():
        return "请输入要翻译的文本"
    
    try:
        result = translate_text(input_lang, output_lang, text)
        return result
    except Exception as e:
        return f"翻译出错: {str(e)}"

def translate_file_interface(input_file, input_lang: str, output_lang: str) -> str:
    """翻译文件的Gradio接口函数"""
    if not agent_available:
        return "错误：Agent模块未正确加载"
    
    if input_file is None:
        return "请上传要翻译的文件"
    
    try:
        # 读取文件内容
        with open(input_file.name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        translated = translate_text(input_lang, output_lang, content)
        
        # 保存翻译结果到临时文件
        output_filename = f"translated_{os.path.basename(input_file.name)}"
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(translated)
        
        return f"翻译完成！结果已保存到: {output_filename}"
    except Exception as e:
        return f"文件翻译出错: {str(e)}"

def agent_chat_interface(message: str, history: List[List[str]]) -> Tuple[str, List[List[str]]]:
    """Agent聊天的Gradio接口函数"""
    if not agent_available:
        return "错误：Agent模块未正确加载", history
    
    if not message.strip():
        return "请输入消息", history
    
    try:
        # 使用agent进行对话
        response = chat_with_agent(message)
        
        # 更新聊天历史
        history.append([message, response])
        return "", history
    except Exception as e:
        error_msg = f"处理消息时出错: {str(e)}"
        history.append([message, error_msg])
        return "", history

def clear_chat_history():
    """清空聊天历史"""
    global chat_history
    chat_history = []
    if agent_available:
        clear_agent_memory()
    return []

# 创建Gradio界面
def create_gradio_interface():
    """创建Gradio界面"""
    
    with gr.Blocks(title="LangChain Agent Demo", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 🤖 LangChain Agent Demo")
        gr.Markdown("这是一个集成了翻译功能和AI Agent的演示应用")
        
        # 状态指示器
        status_text = "🟢 Agent模块已加载" if agent_available else "🔴 Agent模块未加载"
        gr.Markdown(f"**状态**: {status_text}")
        
        with gr.Tabs():
            # 翻译标签页
            with gr.Tab("📝 文本翻译"):
                gr.Markdown("## 文本翻译工具")
                
                with gr.Row():
                    with gr.Column(scale=1):
                        input_lang = gr.Textbox(
                            label="输入语言", 
                            placeholder="例如: 中文", 
                            value="中文"
                        )
                        output_lang = gr.Textbox(
                            label="输出语言", 
                            placeholder="例如: English", 
                            value="English"
                        )
                        translate_btn = gr.Button("翻译", variant="primary")
                    
                    with gr.Column(scale=2):
                        input_text = gr.Textbox(
                            label="待翻译文本", 
                            placeholder="请输入要翻译的文本...",
                            lines=5
                        )
                        output_text = gr.Textbox(
                            label="翻译结果", 
                            lines=5,
                            interactive=False
                        )
                
                translate_btn.click(
                    fn=translate_text_interface,
                    inputs=[input_lang, output_lang, input_text],
                    outputs=output_text
                )
            
            # 文件翻译标签页
            with gr.Tab("📄 文件翻译"):
                gr.Markdown("## 文件翻译工具")
                
                with gr.Row():
                    with gr.Column(scale=1):
                        file_input_lang = gr.Textbox(
                            label="输入语言", 
                            placeholder="例如: 中文", 
                            value="中文"
                        )
                        file_output_lang = gr.Textbox(
                            label="输出语言", 
                            placeholder="例如: English", 
                            value="English"
                        )
                        file_translate_btn = gr.Button("翻译文件", variant="primary")
                    
                    with gr.Column(scale=2):
                        file_input = gr.File(
                            label="上传文件",
                            file_types=[".txt", ".md", ".py", ".js", ".html", ".css"]
                        )
                        file_output = gr.Textbox(
                            label="翻译结果", 
                            lines=10,
                            interactive=False
                        )
                
                file_translate_btn.click(
                    fn=translate_file_interface,
                    inputs=[file_input, file_input_lang, file_output_lang],
                    outputs=file_output
                )
            
            # Agent聊天标签页
            with gr.Tab("💬 AI Agent 聊天"):
                gr.Markdown("## AI Agent 对话")
                gr.Markdown("与AI Agent进行对话，它可以回答问题和执行任务")
                
                chatbot = gr.Chatbot(
                    label="对话历史",
                    height=400,
                    show_copy_button=True
                )
                
                with gr.Row():
                    msg_input = gr.Textbox(
                        label="输入消息",
                        placeholder="输入您的消息...",
                        scale=4
                    )
                    send_btn = gr.Button("发送", variant="primary", scale=1)
                    clear_btn = gr.Button("清空", scale=1)
                
                # 事件处理
                send_btn.click(
                    fn=agent_chat_interface,
                    inputs=[msg_input, chatbot],
                    outputs=[msg_input, chatbot]
                )
                
                msg_input.submit(
                    fn=agent_chat_interface,
                    inputs=[msg_input, chatbot],
                    outputs=[msg_input, chatbot]
                )
                
                clear_btn.click(
                    fn=clear_chat_history,
                    outputs=chatbot
                )
            
            # 关于标签页
            with gr.Tab("ℹ️ 关于"):
                gr.Markdown("""
                ## 关于这个应用
                
                这是一个基于LangChain的演示应用，包含以下功能：
                
                ### 🔧 功能特性
                - **文本翻译**: 支持多种语言的文本翻译
                - **文件翻译**: 支持多种格式文件的批量翻译
                - **AI Agent**: 智能对话助手，可以回答问题并执行任务
                
                ### 🛠️ 技术栈
                - **LangChain**: 用于构建LLM应用
                - **DeepSeek**: 作为底层大语言模型
                - **Gradio**: 用于创建Web界面
                - **Python**: 主要编程语言
                
                ### 📝 使用说明
                1. **文本翻译**: 选择输入和输出语言，输入文本即可获得翻译结果
                2. **文件翻译**: 上传文件，选择语言，系统会自动翻译并保存结果
                3. **AI聊天**: 与AI Agent进行自然对话，获取智能回答
                
                ### ⚠️ 注意事项
                - 请确保已正确配置环境变量
                - 需要有效的API密钥才能使用翻译和AI功能
                - 文件翻译功能支持常见的文本格式
                """)
    
    return demo

if __name__ == "__main__":
    # 创建并启动Gradio应用
    demo = create_gradio_interface()
    demo.launch(
        server_name="0.0.0.0",  # 允许外部访问
        server_port=7860,       # 端口号
        share=False,            # 是否创建公共链接
        debug=True              # 调试模式
    )
