from app import create_app
from threading import Thread
from app.telegram_bot.bot import bot

app = create_app()

# Функция для запуска Flask-приложения
def run_flask():
    app.run(debug=True, use_reloader=False)  # Отключаем reloader

# Функция для запуска Telegram-бота
def run_telegram_bot():
    bot.polling()

if __name__ == '__main__':
    # Запуск Flask-приложения и Telegram-бота в отдельных потоках
    flask_thread = Thread(target=run_flask)
    telegram_thread = Thread(target=run_telegram_bot)

    flask_thread.start()
    telegram_thread.start()

    flask_thread.join()
    telegram_thread.join()
