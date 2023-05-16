import requests
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil import parser



class PrayTimer:
    def __init__(self):
        self.today_date = datetime.today().date().strftime("%y/%m/%d")
        self.names_ar = ["الفجر", "الظهر", "العصر", "المغرب", "العشاء"]
        self.names_en = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

    def get_all_paryer_times_today(self):
        data = {}

        response = requests.get("https://prayertimes.me/Cairo.html")
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")

        prayer_times = soup.find_all(class_="badge badge-clockdif")

        for i, prayer_time in enumerate(prayer_times[1:]):
            # convert to english datetime formate
            data[self.names_en[i]] = parser.parse(prayer_time.text.replace('م', 'PM').replace('ص', 'AM')).time().strftime("%H:%M")

        return data       
        