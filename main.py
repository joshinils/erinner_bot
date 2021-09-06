#!/usr/bin/env python3

import telegram

def main():
    with open('TOKEN', 'r') as token_file:
        TOKEN = token_file.read().replace('\n', '')

    bot = telegram.Bot(token=TOKEN)
    me = bot.get_me()
    print(me)

if __name__ == "__main__":
    main()
