#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
from cv2 import cv2
import logging
import mss
import pyautogui
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from index import clickBtn
import time
import sys
from pathlib import Path

#read token from file
TOKEN = open("./telegram_key.txt", "r").read()
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

x_img = cv2.imread('targets/x.png')
coin_img = cv2.imread('targets/coins.png')


logger = logging.getLogger(__name__)


def ps(update: Update, context: CallbackContext):
    print("PS")
    with mss.mss() as sct:
        sct.shot(output='print.png')
        text = sct.grab(sct.monitors[1])
    update.message.reply_photo(photo=Path('print.png').read_bytes())
    update.message.reply_text("Resolução da imagem" + str(text.size))
    sys.stdout.flush()

def f5(update: Update, context: CallbackContext):
    print("F5")
    update.message.reply_text("F5 enviado")
    pyautogui.press('f5')
    sys.stdout.flush()

def get_c(update: Update, context: CallbackContext):
    print("Coins")
    if clickBtn(coin_img):
        time.sleep(5)
        with mss.mss() as sct:
            sct.shot(output='coins.png')
            update.message.reply_photo(photo=Path('coins.png').read_bytes())

    clickBtn(x_img)
    sys.stdout.flush()


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("print", ps))
    dispatcher.add_handler(CommandHandler("coins", get_c))
    dispatcher.add_handler(CommandHandler("f5", f5))
    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
