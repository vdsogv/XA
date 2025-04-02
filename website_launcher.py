import webbrowser  
import threading  
import time  

URL = "https://pornhub.com"  
COUNT = 1000  

def open_and_chaos():  
    webbrowser.open(URL, new=0)  

if name == "__main__":  
    for _ in range(COUNT):  
        threading.Thread(target=open_and_chaos).start()  
        time.sleep(0.001)  # Псевдо-миллисекунды (на самом деле ~1 мс на Linux)
