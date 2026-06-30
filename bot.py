import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)

KEYWORDS = [
    "recharge",
    "রিচার্জ",
    "balance",
    "ব্যালেন্স",
]

REPLY = """⏳ কিছুক্ষণ অপেক্ষা করুন।

✅ আমাদের টিম থেকে আপনাকে খুব দ্রুতই রিচার্জ দেওয়া হবে।"""

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    text = update.message.text.lower()

    if any(keyword.lower() in text for keyword in KEYWORDS):
        await update.message.reply_text(REPLY)

def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN environment variable not found!")

    app = Application.builder().token(token).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
    )

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
