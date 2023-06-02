@echo [off]
pip install -r requirement.txt
mkdir c:\azan
copy .\azan.wav c:\azan
pyinstaller --onefile --noconsole PrayRemainder.py
move ".\dist\PrayRemainder.exe" "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"