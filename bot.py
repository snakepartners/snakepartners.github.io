from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    Update
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler
)

# Обработчик команды /start
async def start(update: Update, context):
    # Создаем кнопку, которая открывает MiniApp
    keyboard = [
        [InlineKeyboardButton(text="Open MiniApp", web_app=WebAppInfo(url="https://snakepartners.github.io/"))]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Press the button to open the MiniApp inside Telegram:", reply_markup=reply_markup)

if __name__ == '__main__':
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    app = ApplicationBuilder().token('7450715074:AAEyujx1s5edLjBRtppkT2QPTD1TTNGkKqQ').build()

    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler('start', start))

    # Запускаем бота
    app.run_polling()