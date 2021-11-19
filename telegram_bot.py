#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
from cv2 import cv2
import logging
import mss
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from index import clickBtn
import time
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

x_img = cv2.imread('targets/x.png')
coin_img = cv2.imread('targets/coins.png')


logger = logging.getLogger(__name__)


def print(update: Update, context: CallbackContext) -> None:
    with mss.mss() as sct:
        sct.shot(output='print.png')
    update.message.reply_photo(photo=open('print.png', 'rb'))


def coins(update: Update, context: CallbackContext) -> None:
    if clickBtn(coin_img):
        time.sleep(5)
        with mss.mss() as sct:
            sct.shot(output='coins.png')
            update.message.reply_photo(photo=open('coins.png', 'rb'))

    clickBtn(x_img)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2034245054:AAGn-i6I7fTPPFaIqsed1L8uzlWuB4-Ojfw")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("print", print))
    dispatcher.add_handler(CommandHandler("coins", coins))
    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
