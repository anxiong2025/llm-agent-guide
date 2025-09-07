#!/usr/bin/env python3
"""
启动Gradio Web界面的脚本
"""

import os
import sys
from pathlib import Path

# 确保当前目录在Python路径中
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    """主函数"""
    print("🚀 启动LangChain Agent Demo Web界面...")
    print("=" * 50)
    
    # 检查环境变量文件
    env_file = current_dir / ".env"
    if not env_file.exists():
        print("⚠️  警告: 未找到.env文件")
        print("请确保已配置必要的环境变量（如API密钥）")
        print("=" * 50)
    
    try:
        # 导入并启动Gradio应用
        from gradio_app import create_gradio_interface
        
        print("✅ 正在启动Web服务器...")
        print("📱 界面将在浏览器中自动打开")
        print("🌐 本地访问地址: http://localhost:7860")
        print("🛑 按 Ctrl+C 停止服务器")
        print("=" * 50)
        
        # 创建并启动应用
        demo = create_gradio_interface()
        demo.launch(
            server_name="0.0.0.0",  # 允许外部访问
            server_port=7860,       # 端口号
            share=False,            # 是否创建公共链接
            debug=True,             # 调试模式
            show_error=True         # 显示错误信息
        )
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请确保已安装所有依赖包:")
        print("  pip install -e .")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
