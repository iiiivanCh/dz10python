from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


with open('C:\kod.txt', 'r', encoding="UTF-8") as f:
    kod = f.readline()


updater = Updater(str(kod))

updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('a', addition_command))
updater.dispatcher.add_handler(CommandHandler('s', subtraction_command))
updater.dispatcher.add_handler(CommandHandler('m', multiplication_command))
updater.dispatcher.add_handler(CommandHandler('d', division_command))

print('server start')

updater.start_polling()
updater.idle()
