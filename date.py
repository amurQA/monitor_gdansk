from datetime import datetime
from dateutil.relativedelta import relativedelta

class DateGenerator:
    def __init__(self):
        self.current_datetime = datetime.now()

    def get_current_yyyy_mm(self):
        current_yyyy_mm = self.current_datetime.strftime("%Y-%m")
        return current_yyyy_mm

    def get_next_month_yyyy_mm(self):
        next_month_datetime = self.current_datetime + relativedelta(months=1)
        next_month_yyyy_mm = next_month_datetime.strftime("%Y-%m")
        return next_month_yyyy_mm

date_generator = DateGenerator()
print (date_generator.get_current_yyyy_mm())
print (date_generator.get_next_month_yyyy_mm())