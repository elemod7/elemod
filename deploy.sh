#!/bin/bash

# Обновление кода
git pull origin main

# Активация виртуального окружения
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Перезапуск бота (если используется systemd)
systemctl restart bot.service
