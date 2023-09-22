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
        
        # Send GET-request to get the dates
        response = requests.get(self.date_url)
        data = response.json()

        # Get the list of dates
        dates = data["DATES"]

        # Join dates into one row
        print(', '.join(dates))

        # Join all the messages into one variable
        message = ''

        # Monitor the dates and check time spaces presence
        for date in dates:

           # Convert the date to the required year-month-day format
            formatted_date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")

            # Check if the date is in one month or another
            if formatted_date.startswith(self.year_day_1) or formatted_date.startswith(self.year_day_2):
                # Form the full URL for requesting time slots
                full_time_url = self.time_url + formatted_date

               # Send a GET request to get time slots
                response = requests.get(full_time_url)
                time_all_data = response.json()

                # Get a list of time slots
                times_raw = time_all_data.get("TIMES", [])
                times = ', '.join([i['time'] for i in times_raw])

                # Check the number of available slots
                if len(times_raw) == 1:
                    message += f"Доступна дата c 1 слотом: {formatted_date} Время: {times}\n"
                elif len(times_raw) >= 2:
                    message += f"Доступна дата с несколькими слотами: {formatted_date} Время: {times}\n"

        # Send the message
        if message != '':
          await self.send_message(message)

    async def monitor_dates_in_interval(self):

        # Start checking dates once every certain interval
        while True:
            print(datetime.now())
            await self.check_slots()
            time.sleep(self.interval)
    def send_message(self, message):

        # Send a message
        pass
