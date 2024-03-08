import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
from datetime import date
import random
import smtplib
import pywhatkit
import pyautogui
import datetime
import subprocess

engine = pyttsx3.init("sapi5")  # ms voice api
voice = engine.getProperty("voices")
print(voice[2].id)
engine.setProperty("voice", voice[2].id)

myvoice_assistant_name = "bella"

"""Personal Variables"""
name = "Insiya"
fullname = "Insiya firoz haider rizvi"
hobby = "drawing"
course = "Bachelor of Information Technology"
prog_lang = ["python", "java", "c++"]
dob = "25 july 2003"
college_name = "SMT. JANAKIBAI RAMA SALVI COLLEGE"
place = "Thaane, Saaket"


# Python3 code to calculate age in years
def calculateAge(birthDate):
    today = date.today()
    age = (
        today.year
        - birthDate.year
        - ((today.month, today.day) < (birthDate.month, birthDate.day))
    )
    return age


"""Functions"""


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning mam")
    elif hour >= 12 and hour <= 17:
        speak("Good afternoon mam")
    elif hour >= 17 and hour <= 22:
        speak("Good evening mam")
    else:
        speak("Haven't you slept mam?")

    speak(f"my name is {myvoice_assistant_name}, please enter the valid password")


def takecommand():
    """To take microphone input from user and return it as a string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said {query}")
        # speak(query)
    except Exception as e:
        # print(e)
        x = "I cannot hear you proper, please speak louder"
        speak(x)
        return "None"
    return query


def sendEmail(to, email_content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("faizkhan.netpersonal.7@gmail.com", "fyjdawzgzkvajnna")
    server.sendmail("faizkhan.netpersonal.7@gmail.com", to, email_content)
    server.close()


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


"""All current emails contact"""
emails_dict = {
    "my main Gmail": "randygaming.net@gmail.com",
    "my other Gmail": "nurfarzanakhan7@gmail.com",
    "my father": "mk2223249@gmail.com",
    "my sister": "nurfarzanakhan@gmail.com",
}

"""All current whatsapp contacts"""
whatsapp_dic = {
    "MI redmi number": "+91 9167162878",
    "my father": "+968 9542 0072",
    "my mother": "+91 70393 50250",
}


if __name__ == "__main__":
    wishme()
    query = takecommand()
    if "2507" in query:
        speak(f"Hello {name} mam, Please tell me how may i help you")

        while True:
            query = takecommand().lower()

            """Logics for executing tasks"""

            def basiconvo():

                # Personal Datas

                if "my name" in query:
                    speak(f"mam, your name is {name}")
                elif "my full name" in query:
                    speak(f"your full name is {fullname}")
                elif "my age" in query:
                    speak(f"mam, you are {calculateAge(date(2003, 7, 25))} years old")
                elif "college name" in query:
                    speak(
                        f"Your college name is {college_name} and it is in Manisha nagar, kaalwaa"
                    )
                elif "about me" in query:
                    speak(
                        f"{fullname} is a student and has a hobby of {hobby}, she was born on {dob}, and is currently persuing {course} \
                         from {college_name}she has a knowledge of programming languages like {prog_lang}, but mainly work on {prog_lang[0]} \
                        .she stays in {place}"
                    )

                # ----------------------------------------------

                elif "how are you" in query:
                    speak("i'm fine mam, what about you")
                # elif "who created you" or "who made you" in query:
                #     speak(f"i was created by {name}")
                elif "what is your name" in query:
                    speak(f"my name is {myvoice_assistant_name}")
                elif "who are you" in query:
                    speak(f"I am {myvoice_assistant_name}, a virtual assistant")
                elif "i am fine" in query:  # W
                    speak("i'm glad you are fine")
                elif "ok" in query or "good" in query:
                    speak("is there anything else i can do for you, mam")
                elif "nope" in query:  # need work
                    speak("Okay mam")
                elif "can you sing" in query:  # W
                    speak("no, i am a bad singer")
                elif "how old are you" in query or "what is your age" in query:  # W
                    speak("i am 1 month old")
                elif "how many languages" in query:
                    speak("as of now i can only speak english")
                elif "humans" in query:
                    speak("yes i love humans")
                elif "are you a robot" in query:
                    speak("i am your virtual assistant")
                elif "correct" in query:
                    speak("see, i knew it")
                elif "not fine" in query:
                    speak("oh, i hope you feel better, is there anything i can do?")
                elif (
                    "can you be my girlfriend" in query
                    or "can you be my boyfriend" in query
                ):
                    speak("sorry, i am already taken")
                elif "love me" in query:
                    speak("ofcourse i do")
                elif "where are you from" in query:
                    speak("i am from your imagination")
                elif "is love" in query:
                    speak("it is the 7th sense that destroy all other senses")
                elif "favourite colour" in query:
                    speak("my favourite color is blue because i love the sky")
                elif f"{myvoice_assistant_name}" in query:
                    speak("yes mam, what can i do for you")
                elif "thank you" in query:
                    speak("my pleasure mam")
                elif "job" in query:
                    speak("thank you mam!")

            # calling the basic conversation
            basiconvo()

            if "wikipedia" in query:
                try:
                    speak("searching wikipedia...")
                    query = query.replace("wikipedia", "")
                    result = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(result)
                    speak(result)
                except:
                    speak("Sorry! i couldn't find it for some reason")

            elif "open youtube" in query:
                speak("opening youtube")
                # webbrowser.open("https://www.youtube.com/")
                urL = "https://www.youtube.com"
                chrome_path = (
                    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                )
                webbrowser.register(
                    "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
                )
                webbrowser.get("chrome").open_new_tab(urL)

            # elif "my website" in query:
            #     speak("opening your website code with faiz mam")
            #     urL = "https://www.codewithfaiz.com"
            #     chrome_path = (
            #         "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            #     )
            #     webbrowser.register(
            #         "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
            #     )
            #     webbrowser.get("chrome").open_new_tab(urL)

            elif "close chrome" in query:
                speak("closing chrome browser")
                os.system("taskkill /im firefox.exe /f")
                os.system("taskkill /im chrome.exe /f")

            elif "open google" in query:
                speak("opening google")
                # webbrowser.open("http://google.com")
                urL = "https://www.google.com"
                chrome_path = (
                    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                )
                webbrowser.register(
                    "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
                )
                webbrowser.get("chrome").open_new_tab(urL)

            elif "open github" in query:
                speak("opening github")
                urL = "https://github.com/"
                chrome_path = (
                    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                )
                webbrowser.register(
                    "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
                )
                webbrowser.get("chrome").open_new_tab(urL)

            elif "open vs code" in query:
                vs_path = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("opening vs code")
                os.startfile(vs_path)

            elif "make a note" in query:
                speak("what would you like me to write down?")
                notewrite = takecommand()
                note(notewrite)

                speak("I've made a note of that.")

            elif "play music" in query:
                try:
                    music_dir = "C:\\Users\\User\\OneDrive\\Documents\\Faiz Khan Program\\Insiya SEM 6 Project\\mymusic"
                    songs = os.listdir(music_dir)
                    print(songs)
                    random = os.startfile(os.path.join(music_dir, songs[0]))
                except Exception as e:
                    speak("Sorry mam, unable to play music")

            elif "test auto search" in query:
                """Need works"""
                import pyautogui
                import time

                speak("testing it")
                # print(pyautogui.position())

                pyautogui.click(498, 744, 1, 1, "left")
                pyautogui.click(497, 449, 1, 1, "left", duration=1)
                pyautogui.leftClick(601, 417, duration=1)

                speak("What do you wish to type mam?")
                input_query_insearchbar = takecommand()

                pyautogui.typewrite(input_query_insearchbar, interval=1)

                pyautogui.press("enter")

            elif "google search" in query:
                speak("what do you wish to search mam")
                ques = takecommand()
                speak(f"searching {ques} on google")
                pywhatkit.search(ques)

            elif "send an email" in query:
                try:
                    speak("who do you wish to send an email to, mam?")
                    mail_name = takecommand()
                    if mail_name in emails_dict.keys():
                        speak("okay, What should i say?")
                        email_content = takecommand()
                        to = emails_dict.get(mail_name)
                        sendEmail(to, email_content)
                        speak("email has been sent!")
                    else:
                        speak("sorry! This email is not available in my memory")
                except Exception as e:
                    print(e)
                    speak("sorry, i wasn't able to send the email")

            elif (
                "open whatsapp" in query or "open Whatsapp" in query
            ):  # need to change pyauto gui position
                speak("Roger that! mam")

                pyautogui.click(466, 752, 1, 1, "left")
                # pyautogui.click(697, 434, 1, 1, 'left', duration=1)

                # pyautogui.click(727, 631, 1, 1, 'left', duration=1)

            elif "whatsapp message" in query:  # need works
                try:
                    speak("who do you wish to message mam?")
                    whatsapp_name = takecommand()
                    if whatsapp_name in whatsapp_dic.keys():
                        test = whatsapp_dic.get(whatsapp_name)
                        from datetime import timedelta, time

                        # import time
                        speak("okay, what should i say?")
                        my_message = takecommand()
                        # time.sleep(3)
                        time1 = datetime.datetime.now()
                        minu = 2
                        t = time(time1.hour, time1.minute)
                        # result = datetime.datetime.combine(date.today(), t) + timedelta(minutes=minu)
                        x = time1.strftime("%I")
                        print("\n")
                        speak(
                            f"seonding message by {x} o'oclock and {time1.minute + minu} minutes"
                        )
                        print(
                            f"sending message by {x} o'oclock and {time1.minute + minu} minutes"
                        )

                        pywhatkit.sendwhatmsg(
                            test, my_message, time1.hour, time1.minute + minu
                        )
                        speak("Message has been sent!")
                except:
                    speak("Sorry mam, i was not able to send the message")

            elif "spam message" in query:
                """need works here"""
                import time

                try:
                    # speak('Who do you want to spam mam?')
                    # spamname = takecommand()
                    # if spamname in whatsapp_dic.keys():
                    speak("okay, and what will be the spam message?")
                    spammsg = takecommand()
                    # spammsg = input('enter: ')
                    speak("ok, how many times to you want to spam it?")
                    num_ofspam = takecommand()

                    # message = input("Enter the message: ")
                    # num_value = input("Enter num of times: ")
                    # speak('roger that!')
                    abc = int(num_ofspam)

                    # pyautogui.click(612, 745, 1, 1, 'left')
                    # pyautogui.click(697, 434, 1, 1, 'left', duration=1)

                    # pyautogui.click(727, 631, 1, 1, 'left', duration=1)

                    # pyautogui.click(289, 253, 1, 1, 'left', duration=7)

                    # pyautogui.click(610, 693, 1, 'left', duration=1)
                    speak(f"Sending spam messages")
                    time.sleep(15)

                    for i in range(abc):
                        pyautogui.typewrite(spammsg)
                        pyautogui.press("Enter")

                    speak("spam messages has been sent!")
                except Exception as e:
                    # print(e)
                    speak("sorry! unable to send spam messages")

            elif "search on youtube" in query:
                speak("what topic do you want to search for on youtube?")
                topic = takecommand()
                speak(f"okay, playing a random video on the topic {topic}")
                pywhatkit.playonyt(topic)

            elif "the time" in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strtime}")

            elif "the date" in query:
                date1 = date.today()
                print(date1)
                speak(date1)

            elif "sleep" in query:
                speak("Ok then, i am going to sleep, bye")
                quit()

            elif "joke" in query:
                import pyjokes

                speak(pyjokes.get_joke())

            elif "close current window" in query:
                speak("Closing the current window mam!")
                pyautogui.click(1332, 20, 1, 1, "left")

            elif "lock window" in query:
                speak("Locking the window mam")
                import ctypes

                # Define the Windows API function
                user32 = ctypes.windll.user32
                LockWorkStation = user32.LockWorkStation

                # Call the LockWorkStation function to lock the PC
                LockWorkStation()

            elif "shutdown" in query or "shut down" in query:
                speak("mam, are you sure you want to shut down ?")
                surety = takecommand()
                if surety == "yes" or "yeah" in query:
                    os.system("shutdown /s /t 1")
                else:
                    speak("shut down cancelled")

    else:
        speak("I'm sorry, You entered the wrong password")
        quit()
