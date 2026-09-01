

"""
file for the telegram bot
"""


from telegram.ext import Application

telegram_token = "8317586678:AAFWAcbvHV8mYlFUD10BvONL5E4YiE0MXMQ"


def create_bot():
    application = Application.builder().token(telegram_token).build()

    return application

