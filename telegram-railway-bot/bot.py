from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚆 Bot running on Railway!")

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
