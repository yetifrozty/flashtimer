import os
from re import split
import timer
import time
import keyboard
import json
from colorama import Fore, Style

def handleSplit(timer):
    
    if timer.start_time == -1:
        timer.start()

    else:
        if timer.stop_time == -1:
            timer.stop()

def handleRestart(timer, file, splits):
    if splits["Time"] <= 0:
        SaveToFile(file, timer, splits)
    elif timer.stop_time == -1 or splits["Time"] <= timer.getTime():
        timer.start_time = -1
        timer.stop_time = -1
    
    elif splits["Time"] >= timer.getTime():
        SaveToFile(file, timer, splits)
    
    
    
def SaveToFile(file, timer, splits):
    
    with open(file, 'w') as f:
        splits["Time"] = timer.getTime()
        json.dump(splits, f)
        
    
    timer.reload_timer = False


def render(splits, time):
    os.system('clear')

    TextToPrint = splits.get("Title") + '\n'
    TextToPrint += 'PB: ' + str(splits.get("Time")) + '\n'

    if splits["Time"] >= time or splits["Time"] <= 0:
        color = Fore.GREEN
    else:
        color = Fore.RED

    TextToPrint += color + f'Time: {time:0.3f}' + Style.RESET_ALL + '\n'

    print(TextToPrint)

def main():
    DEFAULTSPLIT = {
        "Title":"Game",
        "Time":0,
        "Splits":[]
    }

    with open('config.json', 'r') as f:
        config = json.load(f)

    with open(config.get('Default_Split'), 'r') as f:
        data = f.read()
    
    with open(config.get('Default_Split'), 'w') as f:
        if not data:
            f.write(json.dumps(DEFAULTSPLIT))
            data = json.dumps(DEFAULTSPLIT)
            
        
    splits = json.loads(data)

    t = timer.Timer()
    
    



    
    #keyboard.add_hotkey('del', lambda file, timer: SaveToFile(config.get('Default_Split'),t))
    keyboard.add_hotkey('5', lambda: handleSplit(t))
    keyboard.add_hotkey('6', lambda: handleRestart(t, config.get('Default_Split'), splits))

    while True:

        if t.reload_timer:
            with open(config.get('Default_Split'), 'r') as f:
                data = f.read()
                
                
                splits = json.loads(data)
            t.reload_timer = False

        time.sleep(0.05)
        render(splits, t.getTime())


    




if __name__ == '__main__':
    main()