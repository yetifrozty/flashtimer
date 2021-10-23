#!/usr/bin/python3
import os
from venv import create

if __name__ == '__main__':
    python_dependencies = ['keyboard', 'colorama']
    
    os.system('python3 -m venv ./venv')
    os.chdir('venv/bin')
    

    for module in python_dependencies:
        os.system(f'./pip3 install {module}')
    
    os.mkdir('splits')

    try:
        with open('config.json', 'r'): pass
    except FileNotFoundError:
        with open('config.json', 'w') as f:
            f.write(
            """
                {
                    "Default_Split":"splits/splits.json",
                    "Keybinds":{
                        "start/stop":"page up",
                        "restart":"page down"
                    }
                }
            """
            )