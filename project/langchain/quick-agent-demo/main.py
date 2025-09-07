import importlib.util
import sys
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def import_translation_module():
    """动态导入翻译模块"""
    try:
        module_path = os.path.join("backend", "chat-prompt-template.py")
        spec = importlib.util.spec_from_file_location("chat_prompt_template", module_path)
        if spec is None:
            raise ImportError("无法创建模块规范")
        
        module = importlib.util.module_from_spec(spec)
        sys.modules["chat_prompt_template"] = module
        spec.loader.exec_module(module)
        return module
    except FileNotFoundError:
        print("错误：找不到翻译模块文件")
        sys.exit(1)
    except Exception as e:
        print(f"导入翻译模块时出错: {str(e)}")
        sys.exit(1)

# 导入模块
translation_module = import_translation_module()
from chat_prompt_template import translate_text, create_translation_chain

def translate_file(input_file, output_file, input_lang, output_lang):
    """翻译整个文件"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        translated = translate_text(input_lang, output_lang, content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated)
        print(f"文件已翻译并保存至: {output_file}")
    except Exception as e:
        print(f"文件翻译出错: {str(e)}")

def main():
    """主函数"""
    print("=== 高级翻译工具 ===")
    
    while True:
        print("\n请选择操作:")
        print("1. 单句翻译")
        print("2. 批量句子翻译")
        print("3. 文件翻译")
        print("4. 退出")
        
        choice = input("请输入选项: ")
        
        if choice == "1":
            input_lang = input("输入语言: ")
            output_lang = input("输出语言: ")
            text = input("待翻译文本: ")
            result = translate_text(input_lang, output_lang, text)
            print(f"\n翻译结果: {result}")
            
        elif choice == "2":
            chain = create_translation_chain()
            sentences = []
            print("请输入要翻译的句子（每行一句，空行结束）:")
            while True:
                line = input()
                if not line:
                    break
                sentences.append(line)
            
            input_lang = input("输入语言: ")
            output_lang = input("输出语言: ")
            
            print("\n翻译结果:")
            for text in sentences:
                result = chain.invoke({
                    "input_language": input_lang,
                    "output_language": output_lang,
                    "input": text,
                })
                print(f"- {text} -> {result}")
                
        elif choice == "3":
            input_file = input("输入文件路径: ")
            output_file = input("输出文件路径: ")
            input_lang = input("输入语言: ")
            output_lang = input("输出语言: ")
            translate_file(input_file, output_file, input_lang, output_lang)
            
        elif choice == "4":
            print("感谢使用，再见！")
            break
            
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    main()