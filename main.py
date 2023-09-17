import config
import stt
import tts
import commands
from fuzzywuzzy import fuzz
import datetime
import webbrowser
import random
from tkinter import *

def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_NAME):
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Извините, не могу вам ответить...")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_NAME:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 60}
    for c, v in config.VA_CMD_LIST.items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        commands.help()
    elif cmd == 'ctime':
        commands.dtme()
    elif cmd == 'joke':
        commands.jokes()
    elif cmd == 'mute_on' or cmd == 'mute_off':
        commands.mute()
    elif cmd == 'screen':
        commands.screen()
    elif cmd == 'open_browser':
        # ya_path = r"C:\Users\Iren\AppData\Local\Yandex\YandexBrowser\Application\browser.exe %s"
        webbrowser.open("https://ya.ru/")
    elif cmd == 'open_yt':
        webbrowser.open("https://www.youtube.com")

    elif cmd == 'open_music':
        webbrowser.open("https://music.yandex.ru/home")
        time.sleep(6)
        commands.music_on()
    elif cmd == 'music_off':
        commands.music_off()
    elif cmd == 'music_save':
        commands.music_like()
    elif cmd == 'music_next':
        commands.music_next()
    elif cmd == 'music_prev':
        commands.music_prev()


    elif cmd == 'thanks':
        thx = ['Благодарю', 'Так мило с вашей стороны', 'Большое спасибо',
               'Очень признательна', 'Правда? Теперь можно и не стараться', 'Вы такой искренний человек.']
        tts.va_speak(random.choice(thx))
    elif cmd == 'turn_off':
        bye = ['До свидания', 'До скорой встречи', 'Берегите себя',
               'С нетерпением буду ожидать нашей следующей встречи']
        tts.va_speak(random.choice(bye))
        exit()


def start():
    splash_root.destroy()
    commands.wish_me()
    stt.va_listen(va_respond)


print(f"{config.VA_NAME} начала свою работу")
splash_root = Tk()

splash_root.geometry("500x500")
splash_root.overrideredirect(True)
splash_root.eval('tk::PlaceWindow . center')

img = PhotoImage(file="images/friday.png")
Label(splash_root, image=img).pack()

splash_root.after(6000, start)
mainloop()
