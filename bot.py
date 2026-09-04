import socket
_old_getaddrinfo=socket.getaddrinfo
def _ipv4(*args, **kwargs):
    r=_old_getaddrinfo(*args, **kwargs)
    v=[x for x in r if x[0]==socket.AF_INET]
    return v or r
socket.getaddrinfo=_ipv4
import os
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]

ALLOWED_IDS = {7038195621, 5940426435}
CHANNEL = "@TROON"

WELCOME = """🌟 به کانال ارز دیجیتال TROON خوش آمدید! 🚀

📊 اخبار، تحلیل‌ها و مطالب جذاب دنیای کریپتو را اینجا دنبال کنید.

🔔 همراه ما باشید و فرصت‌ها را از دست ندهید!

@TROON"""

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    user_id = update.effective_user.id

    if user_id not in ALLOWED_IDS:
        await update.message.reply_text(WELCOME)
        return

    if update.message.text:
        await context.bot.send_message(
            chat_id=CHANNEL,
            text=f"{update.message.text}\n\n@TROON"
        )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT, handle_message)
)

print("ربات روشن است ✅")
app.run_polling()
