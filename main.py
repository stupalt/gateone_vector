######## IMPORTS ##########
modelTrained = None
import gatesdk
print("ALPHA BETA :)")
from tkinter import messagebox
print("Starting up.")
f = open(gatesdk.GetFilePath("config.txt"), 'r+')
if "hasBeenBoot = false" in f.read():
    print("Config file has been found ")
    f.truncate(0)
    f.write("hasBeenBoot = true")
import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
from tensorflow.keras.models import load_model
import anki_vector
import speech_recognition as sr
import pygame
import time
from random import randint
import sys
import os
import pygame
import wolframalpha
import json
while modelTrained == None:
    modelTrained = input("Have you run all the required setup files? [Y]es / [N]o").lower()
    if modelTrained == "yes" or "y":
        pass
    elif modelTrained == "no" or "n":
        print("Please run all the required files to ensure correct functionality.")
        print("For more info on these files, visit the GitHub repo and take a look at the README file.")

r = sr.Recognizer()
mic = sr.Microphone()
####### ALL CONSTANTS #####
fs = 44100
seconds = 2
filename = "prediction.wav"
class_names = ["Wake Word NOT Detected", "Wake Word Detected"]

##### LOADING OUR SAVED MODEL and PREDICTING ###
model = load_model("saved_model/WWD2.h5")

print("Prediction Started: ")
i = 0
while True:
    print("Say Now: ")
    Vinput = ("undefined")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(filename, fs, myrecording)

    audio, sample_rate = librosa.load(filename)
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfcc_processed = np.mean(mfcc.T, axis=0)

    prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))
    if prediction[:, 1] > 0.99:
        print(f"Wake Word Detected for ({i})")
        print("Confidence:", prediction[:, 1])
        i += 1
        try:
            with anki_vector.Robot() as robot:
                robot.anim.play_animation("anim_wakeword_getin_01")
                with mic as source:
                    print("Listening...")
                    audio = r.listen(source, 1.25)
                Vinput = r.recognize_google(audio)
                if Vinput == ("hello"):
                    robot.anim.play_animation_trigger("GreetAfterLongTime")

                elif Vinput == ("goodbye"):
                    robot.anim.play_animation("anim_greeting_goodbye_01")

                elif Vinput == ("do you love your owner"):
                    robot.behavior.say_text("Of course I do!")
                    time.sleep(0.25)
                    robot.anim.play_animation("anim_holiday_hyn_confetti_01")
                    robot.anim.play_animation("anim_feedback_iloveyou_02")

                elif Vinput == ("good morning"):
                    robot.anim.play_animation("anim_greeting_goodmorning_02")

                elif Vinput == ("good robot"):
                    robot.anim.play_animation("anim_feedback_goodrobot_01")

                elif Vinput == ("Bad Robot"):
                    HateAnim = randint(0, 1)
                    if HateAnim == 0:
                        robot.anim.play_animation("anim_feedback_badrobot_01")
                    if HateAnim == 1:
                        robot.anim.play_animation("anim_feedback_badrobot_02")

                elif Vinput == ("I love you"):
                    LoveAnim = randint(0, 1)
                    print(LoveAnim)
                    if LoveAnim == 0:
                        robot.anim.play_animation("anim_feedback_iloveyou_01")
                    if LoveAnim == 1:
                        robot.anim.play_animation("anim_feedback_iloveyou_02")

                elif Vinput == ("battery level"):
                    battery_state = robot.get_battery_state()
                    if battery_state:
                        if battery_state.battery_level == 1:
                            robot.behavior.say_text("Battery is low.")
                        if battery_state.battery_level == 2:
                            robot.behavior.say_text("My battery level is medium.")
                        if battery_state.battery_level == 3:
                            robot.behavior.say_text("I am on the charger.")

                elif Vinput == ("go home"):
                    robot.behavior.drive_on_charger()

                elif Vinput == ("go to sleep"):
                    with anki_vector.Robot(behavior_control_level=None) as robot:
                        robot.behavior.app_intent(intent="intent_system_sleep")

                elif Vinput == ("start exploring"):
                    robot.behavior.drive_off_charger

                elif Vinput == ("pop a wheelie"):
                    robot.world.connect_cube
                    robot.world.flash_cube_lights
                    robot.behavior.pop_a_wheelie

                elif Vinput == ("happy halloween"):
                    robot.behavior.set_eye_color(0, 100)
                    robot.anim.play_animation("anim_rt_pickup_putdown_03")

                elif Vinput == ("set a timer"):
                    print("oh well")

                elif Vinput == ("I have a question"):
                    question = ("undefined")
                    robot.anim.play_animation("anim_knowledgegraph_getin_01")
                    robot.anim.play_animation("anim_knowledgegraph_listening_01")
                    with mic as source:
                        robot.behavior.say_text("")
                        print("Listening...")
                        audio = r.listen(source, 2.25)
                    question = r.recognize_google(audio)
                    print(question)
                    client = wolframalpha.Client("YH9J8R-7Y9QXTX47U")
                    res = client.query(question)
                    answer = next(res.results).text
                    print(answer)
                    robot.anim.play_animation("anim_knowledgegraph_searching_01")
                    robot.anim.play_animation("anim_knowledgegraph_searching_getout_01")
                    robot.behavior.say_text(answer)

                else:
                    print("Unkown command :)")
        except:
            print("An error occured.")
    else:
        print(f"Wake Word NOT Detected")
        print("Confidence:", prediction[:, 0])
