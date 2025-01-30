# IMEI Check Backend System

Этот проект представляет собой бэкенд-систему для проверки IMEI устройств, интегрированную с Telegram-ботом и предоставляющую API для внешних запросов.

## Установка
1. Склонируйте репозиторий:
    ```bash
    https://github.com/Albert-Sadykov/hatiko.git
    cd hatiko
    ```

2. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Создайте файл `.env` с следующими переменными:
    ```env
    WHITE_LIST=ваш_telegram_user_id
    TELEGRAM_BOT_TOKEN=ваш_токен_бота
    IMEI_API_TOKEN=ваш_токен_imei_api
    ```

## Запуск
Запустите проект командой:
```bash
python run.py
```