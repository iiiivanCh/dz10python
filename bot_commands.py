from telegram import Update
from telegram.ext import CallbackContext
import random

from spy_log import *


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Пример ввода одного комплесного числа: 3+4j\n'
                              'комплексные числа вводим через пробел\n'
                              '/a - сложение комплексных чисел, например: 3+4j 4+3j \n'
                              '/s - вычитание комплексных чисел\n'
                              '/m - умножение комплексных чисел\n'
                              '/d - деление комплексных чисел')



def addition_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split()  # /a 123 534543
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x + y}')  # ~print


def subtraction_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x - y}')

def multiplication_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x * y}')


def division_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x / y}')
