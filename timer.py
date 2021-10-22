import time

class Timer:
    def __init__(self):
        self.start_time = -1
        self.stop_time = -1
        self.reload_timer = False
    def start(self):
        self.start_time = time.perf_counter()
        
    def stop(self):
        self.stop_time = time.perf_counter()
    def getTime(self):
        if self.start_time == -1:
            return 0
        if self.stop_time == -1:
            return time.perf_counter()-self.start_time
        else:
            return self.stop_time-self.start_time
    