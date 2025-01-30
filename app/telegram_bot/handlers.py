def setup_handlers(bot, white_list, check_imei):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Привет! Отправь мне IMEI для проверки.")

    @bot.message_handler(func=lambda message: True)
    def handle_imei(message):
        user_id = str(message.from_user.id)
        if user_id not in white_list:
            bot.reply_to(message, "У вас нет доступа к этому боту.")
            return

        imei = message.text
        if not(imei.replace(' ', '').isdigit()) or len(imei.replace(' ', '')) != 15:
            bot.reply_to(message, "Неверный формат IMEI.")
            return

        imei_info = check_imei(imei)
        bot.reply_to(message, f"Информация о IMEI: {imei_info}")
