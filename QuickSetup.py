import os
os.system("pip install colorama")
from colorama import Fore
import time
from tkinter import messagebox
from tkinter import Tk
print(Fore.LIGHTWHITE_EX)
print("Let's get you up and running with GateOne.")
print(Fore.RED)
print("THIS PROGRAM IS DESIGNED TO WORK ON WINDOWS.")
print("ALTHOUGH THIS PROGRAM MIGHT FUNCTION FOR LINUX AND MACOS,")
print("THIS WILL WORK OPTIMALLY ON WINDOWS.")
print(Fore.LIGHTWHITE_EX)
print("This program will install the necessary packages onto your computer.")
print("Please make sure pip works on your system before starting, and that ")
print("Your Python version is 3.9")
time.sleep(2)
print("Ready?")
print(Fore.CYAN)
sdk_installed = None
os.system("pip install scipy")
os.system("pip install numpy")
os.system("pip install tensorflow")
os.system("pip uninstall anki_vector")
os.system("pip install ikkez-vector")
os.system("pip install pyaudio")
os.system("pip install pygame")
os.system("pip install wolframalpha")
os.system("pip install json")
os.system("pip install keyboard")
os.system("pip install librosa")
os.system("pip install SpeechRecognition")
print(Fore.LIGHTWHITE_EX + "Get your Vector ready and place it on it's charger.")
import keyboard
print("Have you already installed the Vector SDK? [Y]es / [N]o")
while True:
    try:
        if keyboard.is_pressed("y"):
            sdk_installed = True
            break
        elif keyboard.is_pressed("n"):
            sdk_installed = False
            break
    except:
        pass
if sdk_installed == True:
    pass
else:
    os.system("py -m anki_vector.configure")

import anki_vector
from anki_vector.util import degrees
from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
try:
    with anki_vector.Robot() as robot:
        robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
        time.sleep(2)
        for x in range(5):
            robot.anim.play_animation("anim_pairing_icon_update")
        robot.anim.play_animation("anim_onboarding_wakeup_01")
        time.sleep(3)
        robot.behavior.say_text("Please launch the main.py file and start using Gate 1.")

except:
    print("Error. Please restart the program.")

