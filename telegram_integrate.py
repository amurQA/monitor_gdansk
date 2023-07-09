from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

class TelegramIntegrate:
    def __init__(self, my_token):
        self.bot = Bot(token=my_token)
        self.chat_ids = []

    async def get_chats_ids(self):
        updates = await self.bot.get_updates()
        for update in updates:
            chat_id = update.message.chat.id
            self.chat_ids.append(chat_id)

    async def send_message(self, message):
        for chat_id in self.chat_ids:
            await self.bot.send_message(chat_id, text=message)
    
    async def start_polling(self):
        dp = Dispatcher(self.bot)
        await dp.start_polling(dp)
