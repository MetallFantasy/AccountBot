from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

button_help = "Help"

def message_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help),
            ],
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text="Ага", reply_markup=reply_markup)

def main ():
    print("Start")
    updater = Updater(token='1370079143:AAH0QfrEpnT_w1syJD-MxVUOAaFbFIW15Z4', use_context=True)
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()