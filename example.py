import threading, requests

def Google():
    requests.get("https://www.google.com/")

threads = 5 or int(input("[-] How many threads: "))

if __name__ == "__main__":
    if threading.active_count() <= threads:
        threading.Thread(target=Google).start()
