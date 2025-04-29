from rich import print as pprint
from SignToVoice import Sign2Voice
from VoiceToSign import Voice2Sign
from constants import *

import pyttsx3, time


engine = pyttsx3.init()
engine.setProperty('speed', 60)
voices = engine.getProperty('voices')


def printSay(fronttext='', text="",  endtext='', end='\n', printing=True):
    if printing:
        pprint(f'{fronttext}{text}{endtext}', end=end)
    time.sleep(0.25)
    engine.say(text)
    engine.runAndWait()

def run():
    while True:
        printSay("[cyan]","HELLO EVERYONE I am JANHVI ,I AM HERE TO HELP LANGUAGE PEOPLE IN DIFFERENT HAND PATTERNS....🖐️👈👉👆☝️👇🤘🫰👌✊👊🤙👍🤚👋✍️🙌👐🖖, PLEASE SELECT ONE ACTION TO PERFORM FROM BELOW :","[/cyan]")
        printSay("[yellow]","1. SIGN TO VOICE","[yellow]")
        printSay("[yellow]","2. VOICE TO SIGN","[yellow]")
        printSay("[yellow]","3. Exit","[yellow]")

        try:
            action = int(input('Your answer :- '))
            print()

            # try:
            if action == 1:
                Sign2Voice(model_path=MODEL, video_src=VIDEO)

            elif action == 2:
                Voice2Sign(img_path=IMAGE, audio_src=AUDIO)

            elif action == 3:
                break

            else:
                raise ValueError('invalid value...')

        except Exception as e:
            printSay('[red]','WRONG ATTEMPT! TRY AGAIN!','[/red]')

    printSay("[yellow]","Thanks for using ! Have a nice day...","[/yellow]")


if __name__== '__main__':
    run()