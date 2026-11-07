import os
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context):
    await update.message.reply_text(
        "🤖 Kick Quick\n\n"
        "▶️ تشغيل المشاهدة\n"
        "🔥 تشغيل الكرة العائمة\n"
        "⏹ إيقاف المهمتين\n\n"
        "التطبيق المساعد للهاتف مطلوب للتحكم في Kick."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
