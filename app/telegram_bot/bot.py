import telebot
from app.config import TELEGRAM_BOT_TOKEN, WHITE_LIST
from app.imei.imei_service import check_imei
from app.telegram_bot.handlers import setup_handlers

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

setup_handlers(bot, WHITE_LIST, check_imei)

