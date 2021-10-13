#!/usr/bin/env python3

import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
from pprint import pprint


def foo(update: telegram.Update, context: CallbackContext) -> None:
    pprint(["context", context], width=1)
    pprint(["context.args", context.args])
    pprint(["update", update])
    pprint(["update.message", update.message])
    pprint(["update.edited_message", update.edited_message])

    message = update.message
    if message == None:
        message = update.edited_message
    message.reply_text("bar " + str(message.message_id),
                       reply_to_message_id=message.message_id)


def main():
    with open('TOKEN', 'r') as token_file:
        TOKEN = token_file.read().replace('\n', '')

    # bot = telegram.Bot(token=TOKEN)
    # me = bot.get_me()
    # pprint(me.to_dict())

    # updates = bot.get_updates()
    # print(len(updates), "updates:")
    # for update in updates:
    #     pprint(update.to_dict())

    #bot.send_message(text="bar", chat_id = updates[0].message.from_user.id)

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("foo", foo))

    updater.start_polling()
    updater.idle()

    # chat = bot.get_chat("593866396")
    # print(chat)
    # pprint(chat.to_dict())

    # #bot.delete_message(chat.id, 1)
    # bot.copy_message()


if __name__ == "__main__":
    main()
