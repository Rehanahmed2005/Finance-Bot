import logging
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [[InlineKeyboardButton(text="💸 Expense", callback_data="expense"),
                InlineKeyboardButton(text="💰 Income", callback_data="income")]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
    chat_id=update.effective_chat.id, 
    text="V.A.U.L.T. initialized. Your financial system is now active, Mr. Ahmed.",
    reply_markup = reply_markup
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()