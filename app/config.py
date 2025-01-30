from dotenv import load_dotenv
import os

load_dotenv()

WHITE_LIST = os.getenv('WHITE_LIST').split(',')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
IMEI_API_TOKEN = os.getenv('IMEI_API_TOKEN')
