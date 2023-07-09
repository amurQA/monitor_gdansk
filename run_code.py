import asyncio
from monitor import SlotChecker
from telegram_integrate import TelegramIntegrate
from date import DateGenerator

async def main():
    bot_token = '6016811546:AAFAHaTia6hIHnN20rJcXNR3t3QTG1L6_jk'
    interval = 100

    date_generator = DateGenerator()
    year_day_1 = date_generator.get_current_yyyy_mm()
    year_day_2 = '2023-11'

    telegram_bot = TelegramIntegrate(bot_token)
    await telegram_bot.get_chats_ids()
    slot_checker = SlotChecker(year_day_1, year_day_2, interval)
    slot_checker.send_message = telegram_bot.send_message  # Подменяем метод отправки сообщения

    # Запускаем слушателя Telegram
    # await telegram_bot.start_polling()

    # Запускаем мониторинг дат
    await slot_checker.monitor_dates_in_interval()


if __name__ == "__main__":
    bot_token = '6016811546:AAFAHaTia6hIHnN20rJcXNR3t3QTG1L6_jk'
    telegram_bot = TelegramIntegrate(bot_token)

    # Запускаем слушателя Telegram
    loop = asyncio.get_event_loop()
    loop.create_task(telegram_bot.start_polling())

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(telegram_bot.bot.session.close())
        loop.run_until_complete(telegram_bot.bot.session.close())
        loop.stop()
        loop.close()