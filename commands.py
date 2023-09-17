import datetime
import tts
import pyautogui
import webbrowser
from num2words import num2words
import random


def mute():
    pyautogui.press('volumemute')


def screen():
    screen = pyautogui.screenshot('screenshot.png')


def jokes():
    jokes = ['Программы без ошибок можно писать двумя способами, но работает только третий...',
             'девяносто девять ошибок в коде, девяносто девять ошибок в коде. Возьми-ка одну и пофикси её. сто двадцать семь ошибок в коде...',
             'Чтобы понять рекурсию, нужно сперва понять рекурсию...']
    tts.va_speak(random.choice(jokes))


def music_off():
    if (pyautogui.locateCenterOnScreen('images/stop.png')):
        x, y = pyautogui.locateCenterOnScreen('images/stop.png')
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.leftClick()
    else:
        tts.va_speak('Музыка уже выключена')


def music_on():
    if (pyautogui.locateCenterOnScreen('images/start.png')):
        x, y = pyautogui.locateCenterOnScreen('images/start.png')
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.leftClick()
    else:
        tts.va_speak('Музыка уже включена')


def music_next():
    x, y = pyautogui.locateCenterOnScreen('images/next.png')
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.leftClick()


def music_prev():
    x, y = pyautogui.locateCenterOnScreen('images/prev.png')
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.leftClick()


def music_like():
    if (pyautogui.locateCenterOnScreen('images/like.png')):
        x, y = pyautogui.locateCenterOnScreen('images/like.png')
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.leftClick()
    else:
        tts.va_speak("Трек уже был сохранен !")


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        tts.va_speak("Доброе утро !")

    elif hour >= 12 and hour < 18:
        tts.va_speak("Добрый день !")
    elif hour >= 18 and hour < 23:
        tts.va_speak("Добрый вечер !")
    else:
        tts.va_speak("Доброй ночи !")
    tts.va_speak("Я - Пятница. Слушаю вас.")


def dtme():
    now = datetime.datetime.now()
    text = "Сейч+ас " + num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
    tts.va_speak(text)


def help():
    text = "Я умею:..."
    text += "подсказывать время..."
    text += "рассказывать анекдоты..."
    text += "включать и выключать звук компьютера..."
    text += "и открывать браузер, ютуб и яндекс музыку..."
    tts.va_speak(text)
