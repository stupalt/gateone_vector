import pandas as pandas
import speech_recognition as sr
import anki_vector
import time
from random import randint
import winsound
import datetime
from datetime import date
while True:
    try:
        Vinput = ("undefined")
        r = sr.Recognizer()
        mic = sr.Microphone()
        WAKE = ("vector")
        while True:
            Vinput = ("undefined")
            with mic as source:
                print("Listening...")
                audio = r.listen(source, 1.25)
            wake_listen = r.recognize_google(audio)
            print(wake_listen)
            if wake_listen.count(WAKE) > 0:
                with anki_vector.Robot() as robot:
                    robot.anim.play_animation("anim_wakeword_getin_01")
                    print("wake word heard")
                    with mic as source:
                        print("Listening for command")
                        winsound.PlaySound("C:\\Users\\georg\\Downloads\\wake.wem.wav",winsound.SND_FILENAME)
                        audio = r.listen(source, 3)
                        Vinput = r.recognize_google(audio)
                        print(Vinput)
            elif wake_listen == ("hey buddy"):
                with anki_vector.Robot() as robot:
                    robot.anim.play_animation_trigger("GreetAfterLongTime")
            else:
                print("Did not hear " + WAKE)
                print("Continue normal operation")
            if Vinput == ("hello"):
                with anki_vector.Robot() as robot:
                    robot.anim.play_animation_trigger("GreetAfterLongTime")

            elif Vinput == ("goodbye"):
                with anki_vector.Robot() as robot:
                    robot.anim.play_animation("anim_greeting_goodbye_01")

            elif Vinput == ("do you love your owner"):
                with anki_vector.Robot() as robot:
                    robot.behavior.say_text("Of course I do!")
                    time.sleep(0.25)
                    robot.anim.play_animation("anim_holiday_hyn_confetti_01")
                    robot.anim.play_animation("anim_feedback_iloveyou_02")

            elif Vinput == ("good morning"):
                with anki_vector.Robot() as robot:
                    robot.anim.play_animation("anim_greeting_goodmorning_02")

            elif Vinput == ("good robot"):
                with anki_vector.Robot() as robot:
                    robot.anim.play_animation("anim_feedback_goodrobot_01")

            elif Vinput == ("Bad Robot") :
                with anki_vector.Robot() as robot:
                    HateAnim = randint(0, 1)
                    if HateAnim == 0:
                        robot.anim.play_animation("anim_feedback_badrobot_01")
                    if HateAnim == 1:
                        robot.anim.play_animation("anim_feedback_badrobot_02")

            elif Vinput == ("I love you"):
                LoveAnim = randint(0, 1)
                print(LoveAnim)
                if LoveAnim == 0:
                    with anki_vector.Robot() as robot:
                        robot.anim.play_animation("anim_feedback_iloveyou_01")
                if LoveAnim == 1:
                    with anki_vector.Robot() as robot:
                        robot.anim.play_animation("anim_feedback_iloveyou_02")

            elif Vinput == ("battery level"):
                with anki_vector.Robot() as robot:
                    battery_state = robot.get_battery_state()
                    if battery_state:
                        if battery_state.battery_level == 1:
                            robot.behavior.say_text("Battery is low.")
                        if battery_state.battery_level == 2:
                            robot.behavior.say_text("My battery level is medium.")
                        if battery_state.battery_level == 3:
                            robot.behavior.say_text("I am on the charger.")
            elif Vinput == ("go home"):
                with anki_vector.Robot() as robot:
                    robot.behavior.drive_on_charger()

            elif Vinput == ("go to sleep"):
                with anki_vector.Robot(behavior_control_level=None) as robot:
                    robot.behavior.app_intent(intent="intent_system_sleep")

            elif Vinput == ("start exploring"):
                with anki_vector.Robot() as robot:
                    robot.behavior.drive_off_charger
            elif Vinput == ("pop a wheelie"):
                with anki_vector.Robot() as robot:
                    robot.world.connect_cube
                    robot.world.flash_cube_lights
                    robot.behavior.pop_a_wheelie

            elif Vinput == ("what is france's currency"):
                with anki_vector.Robot() as robot:
                    robot.behavior.say_text("France's natonal currency is baguette")
    except sr.UnknownValueError:
        print("oops error beep boop")
    except sr.WaitTimeoutError:
        print("other error oops beep boop")