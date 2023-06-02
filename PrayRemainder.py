from PrayTimer import get_times_now
from win10toast import ToastNotifier
from datetime import datetime
import threading
import winsound
import time

primary = {"Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"}
times = get_times_now()
print(times)
#def check_times():
#    now = datetime.now().strftime("%H:%M")
#    if now == "23:59":
#        print(times)
#        times = get_times_now()
#        print(times)
#    threading.Timer(1, check_times).start()

# print hello

def notify(name):
    prayTime = times[name].split(" (EEST)")[0]

    now = datetime.now().strftime("%H:%M")
    
    if time == now and name in primary:
        winsound.PlaySound(r"C:\azan\azan.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        message = f"It is the time for {name}"
        toaster = ToastNotifier()
        toaster.show_toast(
            title=f"حي علي الصلاه",
            msg=f"{message}",
            duration=1,
            threaded=True
        )    
        time.sleep(61)
       # return
        

    threading.Timer(1, notify, args=[name, ]).start()

threads = []

#threading.Thread(target=check_times).start()

for prayTime in times:
    now = datetime.now().strftime("%H:%M")
    #thread = threading.Thread(target=notify, args=[time, ]).start()
    #if now <= times[prayTime].split(" (EEST)")[0]:
    thread = threading.Thread(target=notify, args=[prayTime, ])
    thread.start()
    threads.append(thread)

#for thread in threads:
#    thread.join()