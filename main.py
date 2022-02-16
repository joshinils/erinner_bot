#!/usr/bin/env python3

import datetime
import typing
from pprint import pformat, pprint

import telegram
from telegram.ext import CallbackContext, CommandHandler, Updater

import erinnerung


def my_pformat(obj: typing.Optional[typing.Any] = None, indent: int = 0) -> str:  # type: ignore
    indent_increment = 2
    if isinstance(obj, str):
        return obj

    if(isinstance(obj, int)
       or isinstance(obj, float)
       or obj is None
       ):
        return str(obj)

    if type(obj) is telegram.messageentity.MessageEntity:
        return my_pformat({"python_typename": "telegram.messageentity.MessageEntity",
                           "offset": obj.offset,
                           "length": obj.length,
                           "type": obj.type},
                          (indent + indent_increment))

    if type(obj) is telegram.message.Message:
        return my_pformat({"python_typename": "telegram.message.Message",
                           "text": obj.text,
                           "message_id": obj.message_id,
                           "new_chat_members": obj.new_chat_members,
                           "delete_chat_photo": obj.delete_chat_photo,
                           "date": obj.date,
                           "edit_date": obj.edit_date,
                           "group_chat_created": obj.group_chat_created,
                           "entities": obj.entities,
                           "chat": obj.chat,
                           "channel_chat_created": obj.channel_chat_created,
                           "photo": obj.photo,
                           "supergroup_chat_created": obj.supergroup_chat_created,
                           "caption_entities": obj.caption_entities,
                           "new_chat_photo": obj.new_chat_photo
                           },
                          (indent + indent_increment))

    if type(obj) is telegram.update.Update:
        return my_pformat(
            {"python_typename": "telegram.update.Update",
             "edited_message": obj.edited_message,
             "message": obj.message,
             "update_id": obj.update_id}, (indent + indent_increment))

    if type(obj) is telegram.ext.callbackcontext.CallbackContext:
        return my_pformat(str(obj), indent + indent_increment)

    if type(obj) is datetime.datetime:
        return str(obj)

    if type(obj) is telegram.chat.Chat:
        return my_pformat(
            {"python_typename": "telegram.chat.Chat",
             "type": obj.type,
             "id": obj.id,
             "first_name": obj.first_name,
             "last_name": obj.last_name,
             "username": obj.username
             },
            (indent + indent_increment))

    if isinstance(obj, list):
        if len(obj) == 0:
            return "[ ]"
        if len(obj) == 1:
            return "[ " + my_pformat(obj[0], (indent + indent_increment)) + " ]"

        if indent > 0:
            ret = "[\n"
        else:
            ret = " " * indent + "[\n"

        for v in obj:
            ret += " " * (indent + indent_increment) + \
                my_pformat(v, (indent + indent_increment)) + ",\n"
        ret += " " * indent + "]"
        return ret

    if isinstance(obj, dict):
        if indent > 0:
            ret = "{\n"
        else:
            ret = " " * indent + "{\n"

        max_len_key = 0
        for k, v in obj.items():
            max_len_key = max(max_len_key, len(k))

        for k, v in obj.items():
            ret += " " * (indent + indent_increment) + my_pformat(k, 0).ljust(max_len_key) + \
                ": " + \
                my_pformat(
                    v, (indent + indent_increment)) + ",\n"
        ret += " " * indent + "}"
        return ret

    print(type(obj), obj)
    return pformat(str(obj), width=80, indent=(indent + indent_increment))


def add(update: telegram.Update, context: CallbackContext) -> None:
    debug_data = {}
    debug_data["context"] = context
    debug_data["context.args"] = context.args
    debug_data["update"] = update

    message = update.message
    if message is None:
        message = update.edited_message
    debug_data["message.chat_id"] = message.chat_id
    debug_data["message.from_user.id"] = message.from_user.id

    out = "`add called from reply_to_message_id: " + \
        str(message.message_id) + "\n" + my_pformat(debug_data) + "`"

    e = erinnerung.Erinnerung(
        context.args,
        {
            "message_id": message.message_id,
            "user": {
                "chat_id": message.chat_id,
                "user_id": message.from_user.id,
                "username": message.from_user.username,
                "last_name": message.from_user.last_name,
                "first_name": message.from_user.first_name,
                "language_code": message.from_user.language_code,
                "is_bot": message.from_user.is_bot,
            },
            "debug_data": debug_data
        }
    )
    e.save_json()

    print(out)
    message.reply_text(out, parse_mode=telegram.ParseMode.MARKDOWN_V2,
                       reply_to_message_id=message.message_id)


def foo(update: telegram.Update, context: CallbackContext) -> None:
    pprint(["context", context], width=1)
    pprint(["context.args", context.args])
    pprint(["update", update])
    pprint(["update.message", update.message])
    pprint(["update.edited_message", update.edited_message])

    message = update.message
    if message is None:
        message = update.edited_message
    message.reply_text("bar " + str(message.message_id),
                       reply_to_message_id=message.message_id)
    print(message.chat_id)
    print(message.from_user.id)


def main() -> None:
    test = {"a": "b",  # noqa
            "b": 1,
            "asdasd": "asdasdassss",
            "c": {"foo": "42",
                  "b": [
                      1, 2, 3, 12987361827,
                      {
                          "b": 7
                      },
                      "u"
                  ]
                  },
            "g": "h"
            }

    # print(my_pformat(test))

    with open('TOKEN', 'r') as token_file:
        TOKEN = token_file.read().replace('\n', '')

    # bot = telegram.Bot(token=TOKEN)
    # me = bot.get_me()
    # pprint(me.to_dict())

    # updates = bot.get_updates()
    # print(len(updates), "updates:")
    # for update in updates:
    #     pprint(update.to_dict())

    # bot.send_message(text="bar", chat_id = updates[0].message.from_user.id)

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("foo", foo))
    dispatcher.add_handler(CommandHandler("add", add))

    print("updater.start_polling()")
    updater.start_polling()
    print("updater.idle()")
    updater.idle()

    # chat = bot.get_chat("593866396")
    # print(chat)
    # pprint(chat.to_dict())

    # #bot.delete_message(chat.id, 1)
    # bot.copy_message()


if __name__ == "__main__":
    main()
