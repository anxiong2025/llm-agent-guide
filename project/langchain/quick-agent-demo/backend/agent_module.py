from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain.agents import tool, create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

load_dotenv()

# 初始化模型
model = ChatDeepSeek(
    model_name="deepseek-chat",
    temperature=0.5,
    max_tokens=1024
)

# 创建记忆对象
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# 定义工具
@tool
def get_weather(city: str):
    """获取指定城市的实时天气"""
    # 这里可以接入真实天气API
    return f"{city}当前天气：25℃，晴"

@tool
def calculate(expression: str):
    """计算数学表达式"""
    try:
        # 简单的数学计算，实际应用中需要更安全的计算方式
        result = eval(expression)
        return f"计算结果: {expression} = {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"

@tool
def get_current_time():
    """获取当前时间"""
    from datetime import datetime
    now = datetime.now()
    return f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}"

# 创建工具包
tools = [get_weather, calculate, get_current_time]

# 创建带工具的提示模板
agent_prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一个专业的技术顾问，具有以下特点：
    1. 回答简洁明确
    2. 会主动追问细节
    3. 使用Markdown格式
    4. 可以使用工具来获取信息
    5. 如果用户询问天气，使用get_weather工具
    6. 如果用户需要计算，使用calculate工具
    7. 如果用户询问时间，使用get_current_time工具"""),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# 构建带工具的Agent
agent = create_tool_calling_agent(
    model,
    tools,
    agent_prompt
)

# 创建Agent执行器
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    handle_parsing_errors=True
)

# 翻译相关的函数
def translate_text(input_language: str, output_language: str, text: str) -> str:
    """翻译文本"""
    try:
        # 创建翻译提示模板
        translation_prompt = PromptTemplate(
            input_variables=["input_language", "output_language", "text"],
            template="""
            请将以下{input_language}文本翻译成{output_language}：
            
            原文：{text}
            
            翻译：
            """
        )
        
        # 创建翻译链
        translation_chain = translation_prompt | model
        
        # 执行翻译
        response = translation_chain.invoke({
            "input_language": input_language,
            "output_language": output_language,
            "text": text
        })
        
        return response.content
    except Exception as e:
        return f"翻译出错: {str(e)}"

def create_translation_chain():
    """创建翻译链"""
    translation_prompt = PromptTemplate(
        input_variables=["input_language", "output_language", "input"],
        template="""
        请将以下{input_language}文本翻译成{output_language}：
        
        原文：{input}
        
        翻译：
        """
    )
    
    return translation_prompt | model

def chat_with_agent(user_input: str) -> str:
    """与Agent对话"""
    try:
        response = agent_executor.invoke({"input": user_input})
        return response['output']
    except Exception as e:
        return f"处理消息时出错: {str(e)}"

def clear_agent_memory():
    """清空Agent记忆"""
    global memory
    memory.clear()
    return "记忆已清空"

# 导出主要功能
__all__ = [
    'translate_text',
    'create_translation_chain', 
    'chat_with_agent',
    'clear_agent_memory',
    'agent_executor'
]
