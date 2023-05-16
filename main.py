from PrayTimer import PrayTimer
from win10toast import ToastNotifier
from datetime import datetime
import threading
import winsound

pray = PrayTimer()
times = pray.get_all_paryer_times_today()
toaster = ToastNotifier()

def notify(name):
    time = times[name]

    now = datetime.now().strftime("%H:%M")
    
    if time == now:
        winsound.PlaySound("C:\\azan.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        title = f"It is the time for {name}"
        toaster.show_toast(
            f"حي علي الصلاه",
            f"{title}",
            duration=1,
        )    
        return

    threading.Timer(1.0, notify, args=[name, ]).start()

threads = []

for time in times:
    now = datetime.now().strftime("%H:%M")
    if now <= times[time]:
        thread = threading.Thread(target=notify, args=[time, ])
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()