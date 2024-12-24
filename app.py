import pyautogui
import time

mesaj = "merhaba"

mesaj_sayisi=25
for _ in range(mesaj_sayisi):
    pyautogui.typewrite(mesaj)
    pyautogui.press("enter")
    time.sleep(0.1)
