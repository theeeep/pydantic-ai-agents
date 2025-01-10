from pydantic_ai import Agent

from dotenv import load_dotenv

load_dotenv()

agent = Agent("openai:gpt-3.5-turbo", system_prompt="You are a helpful assistant.")

result = agent.run_sync("What is the capital of France?")

print(result.data)
