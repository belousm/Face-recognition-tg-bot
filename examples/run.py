# -*- coding: utf-8 -*-
from my_bot.bot import dp, WEBAPP_PORT, on_startup, on_shutdown, WEBAPP_HOST, WEBHOOK_PATH
from aiogram.utils.executor import start_webhook

if __name__ == "__main__":
    '''Starting bot'''
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )