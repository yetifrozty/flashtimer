#!./venv/bin/python3
import os
import time, timer
import keyboard
import json
from colorama import Fore, Style
from pyfiglet import figlet_format
from datetime import timedelta
from extensions import *

functions_list = ["handleTime", "handleSplit", "handleRestart", "SaveToFile", "Render"]

with open('config.json', 'r') as f:
    config = json.load(f)

extensions_file = config.get('Default_Split') + '/extensions.json'

with open(extensions_file, 'r') as f:
    extensions_list = json.load(f)
    


@exthandleTime(extlist=extensions_list, module=config.get('Default_Split'))
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

@exthandleSplit(extensions_list, config.get('Default_Split'))
def handleSplit(timer):
    
    if timer.start_time == -1:
        timer.start()

    else:
        if timer.stop_time == -1:
            timer.stop()

@exthandleRestart(extensions_list, config.get('Default_Split'))
def handleRestart(timer, file, splits):
    if splits["Time"] <= 0:
        SaveToFile(file, timer, splits)
    elif timer.stop_time == -1 or splits["Time"] <= timer.getTime():
        timer.start_time = -1
        timer.stop_time = -1
    
    elif splits["Time"] >= timer.getTime():
        SaveToFile(file, timer, splits)
    
@extSaveToFile(extensions_list, config.get('Default_Split'))
def SaveToFile(file, timer, splits):
    
    with open(file, 'w') as f:
        splits["Time"] = timer.getTime()
        json.dump(splits, f)
        
    
    timer.reload_timer = False

@extRender(extensions_list, config.get('Default_Split'))
def Render(splits, time, title):
    os.system('clear')

    TextToPrint = title + '\n'

    TextToPrint += 'PB: ' + handleTime(splits.get("Time")) + '\n'

    if splits["Time"] >= time or splits["Time"] <= 0:
        color = Fore.GREEN
    else:
        color = Fore.RED

    #TextToPrint += color + f'Time: {time:0.3f}' + Style.RESET_ALL + '\n'
    TextToPrint += 'Time: ' + color + handleTime(time) + Style.RESET_ALL + '\n'

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

    while True:
        try:
            if t.reload_timer:
                with open(file, 'r') as f:
                    data = f.read()
                    
                    
                    splits = json.loads(data)
                t.reload_timer = False

            time.sleep(0.1)
            Render(splits, t.getTime(), title)
        except KeyboardInterrupt:
            os.system('clear')
            break


    




if __name__ == '__main__':
    if os.geteuid() == 0:
        main()
    else:
        print('You need sudo to run this script.')