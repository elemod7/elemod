from aiogram import Bot, Dispatcher, executor
import logging
from config import BOT_TOKEN
from handlers import (
    start_handler,
    services_handler,
    ask_question_handler,
    send_request_handler,
    main_menu_handler,
)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрация обработчиков
dp.register_message_handler(start_handler, commands=["start"])
dp.register_message_handler(services_handler, lambda message: message.text == "Услуги")
dp.register_message_handler(ask_question_handler, lambda message: message.text == "Задать вопрос")
dp.register_message_handler(send_request_handler, lambda message: message.text == "Отправить заявку")
dp.register_message_handler(main_menu_handler, lambda message: message.text == "На главную")

# Добавление отладочных сообщений при запуске и остановке
async def on_startup(dp):
    logger.info("Бот запущен")

async def on_shutdown(dp):
    logger.info("Бот остановлен")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
