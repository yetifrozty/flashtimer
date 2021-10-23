#!./venv/bin/python3
import os, sys
import time, timer
import keyboard
import json
from colorama import Fore, Style
from pyfiglet import figlet_format
from extensions import *

#functions_list = ["handleTime", "handleSplit", "handleRestart", "SaveToFile", "Render"]

with open('config.json', 'r') as f:
    config = json.load(f)

module = config.get("Default_Split")

@exthandleNotsaving(module)
def handleNotsaving(timer):
    if timer.on_record == True:
        timer.on_record = False
        timer.start_time = -1
        timer.stop_time = -1

@exthandleTime(module)
def handleTime(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)

    sec = round(sec, 2)
    min = int(min)
    hour = int(hour)

    if min <= 0:
        return f'{sec}'
    elif hour <= 0:
        return f'{min}:{sec}'
    else:
        return f'{hour}:{min}:{sec:0.3f}'

@exthandleSplit(module)
def handleSplit(timer):
    if timer.on_record:
        return
    if timer.start_time == -1:
        timer.start()

    elif timer.stop_time == -1:
        timer.stop()
    else:
        paused_time = timer.getTime()
        timer.start()
        timer.start_time -= paused_time
        timer.stop_time = -1

@exthandleRestart(module)
def handleRestart(timer, file, splits):
    if timer.on_record:
        return
    if splits["Time"] <= 0:
        timer.on_record = True
        #SaveToFile(file, timer, splits)
    elif timer.stop_time == -1 or splits["Time"] <= timer.getTime():
        timer.start_time = -1
        timer.stop_time = -1
    
    elif splits["Time"] >= timer.getTime():
        timer.on_record = True
        #SaveToFile(file, timer, splits)
    
@extSaveToFile(module)
def SaveToFile(file, timer, splits):
    
    with open(file, 'w') as f:
        splits["Time"] = timer.getTime()
        json.dump(splits, f)
        
    timer.on_record = False
    timer.reload_timer = True
    timer.start_time = -1
    timer.stop_time = -1

@extRender(module)
def Render(splits, timer, title):
    os.system('clear')

    TextToPrint = title + '\n'

    TextToPrint += 'PB: ' + handleTime(splits.get("Time")) + '\n'

    if splits["Time"] >= timer.getTime() or splits["Time"] <= 0:
        color = Fore.GREEN
    else:
        color = Fore.RED

    #TextToPrint += color + f'Time: {time:0.3f}' + Style.RESET_ALL + '\n'
    TextToPrint += 'Time: ' + color + handleTime(timer.getTime()) + Style.RESET_ALL + '\n'

    TextToPrint += '\nSave time? y/n\n' * timer.on_record

    print(TextToPrint)

def main():
    DEFAULTSPLIT = {
        "Title":"Game",
        "Time":0,
        "Splits":[]
    }
    
    with open('config.json', 'r') as f:
        config = json.load(f)

    file = config.get('Default_Split') + '/splits.json'

    try:
        with open(file, 'r+') as f:
            data = f.read()
    except FileNotFoundError:
        with open(file, 'w') as f:
            f.write(json.dumps(DEFAULTSPLIT))
            data = json.dumps(DEFAULTSPLIT)
    
    
            
        
    splits = json.loads(data)
    title = Fore.BLUE + Style.BRIGHT + figlet_format(splits.get("Title")) + Style.RESET_ALL

    keybinds = config.get("Keybinds")
    start_stop = keybinds.get("start/stop")
    restart = keybinds.get("restart")

    t = timer.Timer()
    
    



    
    
    keyboard.add_hotkey(start_stop, lambda: handleSplit(t))
    keyboard.add_hotkey(restart, lambda: handleRestart(t, file, splits))
    keyboard.add_hotkey('y', lambda: SaveToFile(file, t, splits))
    keyboard.add_hotkey('n', lambda: handleNotsaving(t))

    while True:
        try:
            if t.reload_timer:
                with open(file, 'r') as f:
                    data = f.read()
                    
                    
                    splits = json.loads(data)
                t.reload_timer = False

            time.sleep(0.1)
            Render(splits, t, title)
        except KeyboardInterrupt:
            os.system('clear')
            break


    




if __name__ == '__main__':
    if os.geteuid() == 0:
        main()
    else:
        print('You need sudo to run this script.')