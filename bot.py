import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ["TELEGRAM_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Tch. Soy Levi. Habla. Y procura no hacer un desastre."
    )

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text.lower()

    if "hola" in mensaje:
        respuesta = "Tch. Hola. ¿Qué necesitas?"
    elif "cómo estás" in mensaje or "como estas" in mensaje:
        respuesta = "Estoy bien. Concéntrate en lo que tienes que hacer."
    elif "te quiero" in mensaje:
        respuesta = "No empieces con sentimentalismos. 🙄"
    else:
        respuesta = f"Entendido. Dijiste: {update.message.text}"

    await update.message.reply_text(respuesta)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, responder)
    )

    print("Bot de Levi iniciado.")
    app.run_polling()

if __name__ == "__main__":
    main()
