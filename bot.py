from llama_index.llms.groq import Groq
from dotenv import load_dotenv
import os

# agents
from llama_index.agent.openai import OpenAIAgent
from agents import movie_agent_tool

load_dotenv()

llm = Groq(model="llama3-8b-8192", api_key=os.environ.get("GROP_API_KEY"))

with open(os.path.abspath('prompts\system.txt'),'r') as f:
    system_prompt = f.read()
agent = OpenAIAgent.from_tools([movie_agent_tool], llm=llm, system_prompt=system_prompt)

def chat(message, history):
    return str(agent.chat(message))