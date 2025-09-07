from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain.agents import tool, create_tool_calling_agent, AgentExecutor

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

# 创建工具包
tools = [get_weather]

# 创建带工具的提示模板
agent_prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一个专业的技术顾问，具有以下特点：
    1. 回答简洁明确
    2. 会主动追问细节
    3. 使用Markdown格式
    4. 可以使用工具来获取信息"""),
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

while True:
    user_input = input("你：")
    if user_input.lower() == 'exit':
        break
        
    # 使用Agent执行器而不是普通对话链
    response = agent_executor.invoke({"input": user_input})
    
    print(f"AI：{response['output']}")