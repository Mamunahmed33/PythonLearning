import threading

class test(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.currentThread().getName() + "  ")

mamun = test(name = "Mamun")
Rahim = test(name = "Rahim")
mamun.start()
Rahim.start()