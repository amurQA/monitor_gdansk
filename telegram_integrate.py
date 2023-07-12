from aiogram import Bot

class TelegramIntegrate:
    def __init__(self, my_token, channel_id):
        self.bot = Bot(token=my_token)
        self.channel_id = channel_id

    async def send_message(self, message):
        await self.bot.send_message(self.channel_id, text=message)
