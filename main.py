import asyncio
from monitor import SlotChecker
from telegram_integrate import TelegramIntegrate
from date import DateGenerator

async def main():
    bot_token = '6016811546:AAFAHaTia6hIHnN20rJcXNR3t3QTG1L6_jk'
    interval = 100
    channel_id = -1001922911449

    date_generator = DateGenerator()
    year_day_1 = date_generator.get_current_yyyy_mm()
    year_day_2 = date_generator.get_next_month_yyyy_mm()

    telegram_bot = TelegramIntegrate(bot_token, channel_id)
    slot_checker = SlotChecker(year_day_1, year_day_2, interval)

    # Change the send message method at telegram_bot instance
    slot_checker.send_message = telegram_bot.send_message  

    # Run monitoring of dates
    await slot_checker.monitor_dates_in_interval()


if __name__ == "__main__":
    
    # Create a new event loop and set it as the current event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Run the main function within the event loop
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
   