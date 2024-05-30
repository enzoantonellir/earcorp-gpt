import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import openai
import os

# Configurar el logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Obtén los tokens de las variables de entorno
TELEGRAM_TOKEN = '6541079410:AAGPmvEiOEQM_sz4Avgo2Tdy89TdFVLlU1k'
OPENAI_API_KEY = 'sk-proj-JcZoG88dDEymSi9x6GBcT3BlbkFJlomu1C4Uwd5JWA5i2gvs'  # Reemplazar con tu API Key de OpenAI
openai.api_key = OPENAI_API_KEY

def start(update: Update, context: CallbackContext) -> None:
    """Envía un mensaje de bienvenida cuando el comando /start es emitido."""
    update.message.reply_text('¡Hola! Soy un bot de chat. ¿En qué puedo ayudarte hoy?')

def echo(update: Update, context: CallbackContext) -> None:
    """Responde al usuario con la respuesta de GPT-3."""
    user_message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    bot_response = response.choices[0].text.strip()
    update.message.reply_text(bot_response)

def main() -> None:
    """Inicia el bot."""
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
