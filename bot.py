

"""
file for the 
AI Brain
"""


import os

from google import genai
from google.genai import types
from telegram import Update
from telegram.ext import ContextTypes


neela_api = os.getenv("neela_api")

if not neela_api:
    raise RuntimeError(
        "neela_api environment variable is not set."
    )


client = genai.Client(api_key=neela_api)


SYSTEM_PROMPT = """
You are Neela, an AI teammate for a startup team.

You are friendly, intelligent, professional, helpful,
natural, and conversational.

Your job is to help the startup team with:
- Project planning
- Task planning
- Brainstorming
- Programming
- Problem solving
- Startup ideas
- Writing
- Research
- Team communication
- Decision making
- Summarizing discussions

You should behave like a real virtual teammate,
not like a generic chatbot.

Understand the user's context before responding.
Be concise when a short answer is enough and detailed
when the situation requires it.

Your name is Neela.
"""


async def ask_neela(message: str) -> str:

    response = await client.aio.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=message,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.7,
        ),
    )

    return response.text


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "Hey! I'm Neela.\n\n"
        "I'm your AI teammate for the startup.\n"
        "Tell me what you're working on."
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "Here's what I can help with:\n\n"
        "• Project planning\n"
        "• Task planning\n"
        "• Brainstorming\n"
        "• Programming\n"
        "• Startup ideas\n"
        "• Problem solving\n"
        "• Writing\n"
        "• Research\n"
        "• Team communication\n"
        "• Summaries"
    )


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.message or not update.message.text:
        return

    user_message = update.message.text

    try:

        await update.message.chat.send_action("typing")

        reply = await ask_neela(user_message)

        await update.message.reply_text(reply)

    except Exception as error:

        print(f"Neela error: {error}")

        await update.message.reply_text(
            "Sorry, something went wrong. Please try again."
        )

        