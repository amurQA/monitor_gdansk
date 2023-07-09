import requests
from datetime import datetime
import time

class SlotChecker:
    def __init__(self, year_day_1, year_day_2, interval):
        self.date_url = "https://kolejkagdansk.ajhmedia.pl/admin/API/date/5/304/pl"
        self.time_url = "https://kolejkagdansk.ajhmedia.pl/admin/API/time/5/3/"
        self.year_day_1 = year_day_1
        self.year_day_2 = year_day_2
        self.interval = interval

    async def check_slots(self):
        # Отправляем GET-запрос для получения дат
        response = requests.get(self.date_url)
        data = response.json()
        # Получаем список дат
        dates = data["DATES"]
        print(', '.join(dates)) # Объединяем даты в одну строку
        # Мониторим даты и проверяем доступность временных слотов
        for date in dates:
            # Преобразуем дату в требуемый формат "год-месяц-день"
            formatted_date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")

            # Проверяем, является ли дата в одной месяце или в другом
            if formatted_date.startswith(self.year_day_1) or formatted_date.startswith(self.year_day_2):
                # Формируем полный URL для запроса временных слотов
                full_time_url = self.time_url + formatted_date

                # Отправляем GET-запрос для получения временных слотов
                response = requests.get(full_time_url)
                time_all_data = response.json()

                # Получаем список временных слотов
                times_raw = time_all_data.get("TIMES", [])
                times = ', '.join([i['time'] for i in times_raw])

                # Проверяем количество доступных слотов
                if len(times_raw) == 1:
                    await self.send_message(f"Доступна дата c 1 слотом: {formatted_date} Время: {times}")
                elif len(times_raw) >= 2:
                    await self.send_message(f"Доступна дата с несколькими слотами: {formatted_date} Время: {times}")

    async def monitor_dates_in_interval(self):
        # Запускаем проверку дат раз в определенный интервал
        while True:
            await self.check_slots()
            time.sleep(self.interval)
    def send_message(self, message):
        # Отправляем сообщение любым способом
        pass
