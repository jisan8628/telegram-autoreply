from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

KEYWORDS = [
    "recharge",
    "রিচার্জ",
    "balance",
    "ব্যালেন্স"
]

REPLY = """⏳ কিছুক্ষণ অপেক্ষা করুন।

✅ আমাদের টিম থেকে আপনাকে খুব দ্রুতই রিচার্জ দেওয়া হবে।"""

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if any(word.lower() in text for word in KEYWORDS):
        await update.message.reply_text(REPLY)

def main():
    app = Application.builder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
    )

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
