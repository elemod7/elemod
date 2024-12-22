from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Токен вашего бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
