import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8674997924:AAHT7w5uf8P5tCMMz0ptqFjOSaLaKJBTYTE")

if not TOKEN:
    print("ERROR: BOT_TOKEN variable is empty!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working!Nigga")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()