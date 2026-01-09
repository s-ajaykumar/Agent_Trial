from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

# Tools
def get_weather(city: str) -> str:
    return f"It's sunny in {city}"

# Agent
model = init_chat_model(
    'google_genai:gemini-2.5-flash-lite',
    temperature = 0.7,
    max_tokens = 500
    )
agent = create_agent(
    model = model,
    tools = [get_weather],
    system_prompt = 'You are a helpful assistant.'
)

# Inference
agent.invoke(
    {'messages' : [{'role' : 'user', 'content' : 'whats the weather in Madurai'}]}
)