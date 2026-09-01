

from telegram.ext import CommandHandler, MessageHandler, filters

from telegram_bot import create_bot
from bot import start, help_command, message_handler


def main():

    application = create_bot()

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler
        )
    )

    print("Neela is online...")

    application.run_polling()


if __name__ == "__main__":
    main()
    