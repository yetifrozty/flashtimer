module1 = ''

def import_module(module):
    import importlib.util
    spec=importlib.util.spec_from_file_location("Extension",module + '/extensions.py')
    Extension = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(Extension)
    return Extension

def exthandleNotsaving(module):
    module1 = module
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                module = import_module(module1)
                return module.handleNotsaving(func, *args, **kwargs)
            except:
                return func(*args, **kwargs)
        return wrapper
    return deco

def exthandleTime(module):
    module1 = module
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                module = import_module(module1)
                return module.handleTime(func, *args, **kwargs)
            except:
                return func(*args, **kwargs)
        return wrapper
    return deco

def exthandleSplit(module):
    module1 = module
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                module = import_module(module1)
                return module.handleSplit(func, *args, **kwargs)
            except:
                return func(*args, **kwargs)
        return wrapper
    return deco
    
def exthandleRestart(module):
    module1 = module
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                module = import_module(module1)
                return module.handleRestart(func, *args, **kwargs)
            except:
                return func(*args, **kwargs)
        return wrapper
    return deco
    
def extSaveToFile(module):
    module1 = module
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                module = import_module(module1)
                return module.SaveToFile(func, *args, **kwargs)
            except:
                return func(*args, **kwargs)
        return wrapper
    return deco
    
def extRender(module):
    module1 = module
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                module = import_module(module1)
                return module.Render(func, *args, **kwargs)
            except:
                return func(*args, **kwargs)
        return wrapper
    return deco
    
