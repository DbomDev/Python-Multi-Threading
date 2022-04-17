# Python-Multi-Threading
Ever wanted to know how to make your Programm have multiple Threads which run your Code. Here you go. An easy explanation how to integreate multi threading into your application.

## Tutorial
First import the Threading package.
```
import threading
```

Make a function out of your Program which the Threads gona run.
```python
def Google():
    requests.get("https://www.google.com/")
```

You can make the user choose how many threads he wants have to be run or set it in the Sript into the variable `threads`.
```python
threads = 5 or int(input("[?] How many threads? "))
```

Second we make that the Threads not gona start while the Programm runs, the threads should start at the beginning of the Programm start. The Thread Code is going to be always the last thing in your Script. Set the Target of the Thread to your main function which should be run by the Threads.
```python
if __name__ == "__main__":
    if threading.active_count() <= threads:
        threading.Thread(target=Google).start()
```

### Full Tutorial Code
```python
import threading

def Google():
    requests.get("https://www.google.com/")

threads = 5 or int(input("[-] How many threads: "))

if __name__ == "__main__":
    if threading.active_count() <= threads:
        threading.Thread(target=Google).start()
```


## Credits
You're not required to credit me in your Programm when you used this Tutorial to integreate multi threading in your Project.
```
Made by DbomDev
```
