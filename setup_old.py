#!/usr/bin/python3
import os


if __name__ == '__main__':
    python_dependencies = ['keyboard', 'colorama', 'pyfiglet']
    
    os.system('python3 -m venv ./venv') 

    for module in python_dependencies:
        os.system(f'./venv/bin/pip3 install {module}')
    
    os.mkdir('splits')

    try:
        with open('config.json', 'r'): pass
    except FileNotFoundError:
        with open('config.json', 'w') as f:
            f.write(
            """
                {
                    "Default_Split":"splits/splits",
                    "Keybinds":{
                        "start/stop":"page up",
                        "restart":"page down"
                    }
                }
            """
            )