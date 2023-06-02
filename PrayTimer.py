import json
import os
from datetime import datetime
import requests
import sys

today = datetime.now().strftime("%d-%m-%Y")
month = today.split('-')[1]
year = today.split('-')[2]

city = "Cairo"
country = "Egypt"

api = f"https://api.aladhan.com/v1/calendarByCity/{year}/{month}?city={city}&country={country}&method=3"

def download(url, file):
    res = requests.get(url)
    with open(file, 'w') as file:
        json_data = json.loads(res.content)
        file.write(json.dumps(json_data))

def formate(filename, output):
    with open(filename, 'r') as filename:
        data_file = json.load(filename)

        result = { }

        for data in data_file.get("data"):
            result[data["date"]["gregorian"]["date"]] = data["timings"]

        with open(output, "w") as res:
            res.write(json.dumps(result))

def check_files():
    try:
        if os.path.exists("data.json"):
            with open("data.json", "r") as file:
                data_file = json.load(file)
                end_date = list(data_file.keys())[-1]

                if today not in data_file:
                    # data file exists but the data has expired
                    download(api, "data.json")
                    formate("data.json", "data.json")
        else:
            # data file is not exist, so download it
            download(api, "data.json")
            formate("data.json", "data.json")

        # the file has been verified correctly
        return True
    except:
        # some error has occured, like no internet connection
        return False

def get_times_now():
    if check_files():
        with open("data.json", 'r') as file:
            today_times = json.load(file)[today]

        return today_times
    else:
        print("No internet Connections")
        sys.exit()
