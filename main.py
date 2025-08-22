import os 
import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("Key is not set in env")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="👋 **Welcome to Ai-Chatbot!**\n\nBuilt with ❤️ using [Chainlit](https://www.chainlit.io) | Connect with me on [M-Raeesdev](https://github.com/M-RaeesDev)."
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    try:
        response = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": message.content}],
        )
        await cl.Message(content=response.choices[0].message.content).send()
    except Exception as e:
        await cl.Message(content=f"Error:{str(e)}").send()
