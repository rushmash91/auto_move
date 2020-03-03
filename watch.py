
import sys 
from shutil import move
import time 
import logging 
from watchdog.observers import Observer 
from watchdog.events import LoggingEventHandler, FileSystemEventHandler, PatternMatchingEventHandler
  
class Handler(PatternMatchingEventHandler): 
    def __init__(self):  
        PatternMatchingEventHandler.__init__(self, patterns=['*.mp3'], ignore_directories=False, case_sensitive=True) 
    
    def on_created(self, event): 
        print("Watchdog received created event - % s." % event.src_path)
        name = "% s" % event.src_path[1:] 
        destination = '/home/arush/Desktop/Music'
        destination += name
        fr = '/home/arush/Desktop/watchdog'
        fr += name
        move(fr, destination)



if __name__ == "__main__": 
    path = sys.argv[1] if len(sys.argv) > 1 else '.'   

    observer = Observer() 
    observer.schedule(Handler(), path, recursive=True)  
    observer.start() 
    try: 
        while True: 
            time.sleep(1) 
    except KeyboardInterrupt: 
        observer.stop() 
    observer.join() 
