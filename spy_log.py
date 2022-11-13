from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def log(update: Update, context: CallbackContext):
    with open('db.csv', 'a') as f:
        f.write(
            f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')

