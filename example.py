import threading

def Hello():
    print("Hello")

threads = int(input("[-] How many threads: "))

if __name__ == "__main__":
    if threading.active_count() <= threads:
        threading.Thread(target=Hello).start()
