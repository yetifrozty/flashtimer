def exthandleTime(extlist, module):
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                extlist.index("handleTime")
            except:
                return func(*args, **kwargs)
        
            module = __import__(module + '/extensions.py')
            return module.handleTime(func, *args, **kwargs)
        return wrapper
    return deco

def exthandleSplit(extlist, module):
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                extlist.index("handleSplit")
            except:
                return func(*args, **kwargs)
        
            module = __import__(module + '/extensions.py')
            return module.handleSplit(*args, **kwargs)
        return wrapper
    return deco
    
def exthandleRestart(extlist, module):
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                extlist.index("handleRestart")
            except:
                return func(*args, **kwargs)
        
            module = __import__(module + '/extensions.py')
            return module.handleRestart(*args, **kwargs)
        return wrapper
    return deco
    
def extSaveToFile(extlist, module):
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                extlist.index("SaveToFile")
            except:
                return func(*args, **kwargs)
            
            module = __import__(module + '/extensions.py')
            return module.SaveToFile(*args, **kwargs)
        return wrapper
    return deco
    
def extRender(extlist, module):
    def deco(func):
        def wrapper(*args, **kwargs):
            try:
                extlist.index("Render")
            except:
                return func(*args, **kwargs)
            
            module = __import__(module + '/extensions.py')
            return module.Render(*args, **kwargs)
        return wrapper
    return deco
    