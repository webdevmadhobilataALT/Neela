

"""
file for the telegram bot
"""


from telegram.ext import Application
import os

telegram_token = os.getenv("telegram_token")


def create_bot():
    application = Application.builder().token(telegram_token).build()

    return application

