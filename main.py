import gradio as gr
from bot import chat

gr.ChatInterface(
    chat,
    title="Gaamfoi"
).launch()