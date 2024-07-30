from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent

def recommend_movie(genre:str):
    """takes movie genre and suggests movie"""
    return "Tere Naam"

movie_agent_tool = FunctionTool.from_defaults(fn=recommend_movie, name="movie_agent")