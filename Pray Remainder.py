from PrayTimer import get_times_now
from win10toast import ToastNotifier
from datetime import datetime
import threading
import winsound


times = get_times_now()
print(times)
#def check_times():
#    now = datetime.now().strftime("%H:%M")
#    if now == "23:59":
#        print(times)
#        times = get_times_now()
#        print(times)
#    threading.Timer(1, check_times).start()


def notify(name):
    time = times[name].split(" (EEST)")[0]

    now = datetime.now().strftime("%H:%M")
    
    if time == now:
        winsound.PlaySound("C:\\azan.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        message = f"It is the time for {name}"
        toaster = ToastNotifier()
        toaster.show_toast(
            title=f"حي علي الصلاه",
            msg=f"{message}",
            duration=1,
            threaded=True
        )    
        return
        

    threading.Timer(30, notify, args=[name, ]).start()

threads = []



#threading.Thread(target=check_times).start()

for time in times:
    now = datetime.now().strftime("%H:%M")
    #thread = threading.Thread(target=notify, args=[time, ]).start()
    if now <= times[time].split(" (EEST)")[0]:
        thread = threading.Thread(target=notify, args=[time, ])
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()