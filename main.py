import os
import asyncio
import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# Initialize Gemini-compatible client
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content=(
            " **Welcome to Ai-Chatbot!**\n\n"
            "Built with using [Chainlit](https://www.chainlit.io)\n"
            "Connect with me on [M-RaeesDev](https://github.com/M-RaeesDev)."
        ),
        author="System",
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    try:
        # Show typing indicator message
        thinking_msg = cl.Message(content="*Thinking...*")
        await thinking_msg.send()

        # Create empty message for streamed response
        msg = cl.Message(content="")
        await msg.send()

        buffer = ""
        last_update_time = 0
        update_interval = 0.08  # 80ms = smooth

        # Start Gemini response stream
        stream = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": message.content}],
            stream=True,
        )

        # Remove "thinking..." indicator before showing real response
        thinking_msg.content = ""
        await thinking_msg.update()

        # Stream tokens smoothly
        async for chunk in stream:
            delta = chunk.choices[0].delta.content if chunk.choices[0].delta else ""
            if delta:
                buffer += delta
                current_time = asyncio.get_event_loop().time()
                if current_time - last_update_time > update_interval:
                    await msg.stream_token(buffer)
                    buffer = ""
                    last_update_time = current_time

        # Flush remaining text
        if buffer:
            await msg.stream_token(buffer)

        # Finalize message with fade animation
        await msg.update()

    except Exception as e:
        await cl.Message(content=f" Error: {str(e)}").send()
