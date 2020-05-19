from pynput.keyboard import Key, Listener


class TypewriterLogic():


    @staticmethod
    def on_press(key):
        print("bip-bop")


    @staticmethod
    def turn_on():
        try:
            Listener(on_press=TypewriterLogic.on_press).start()
        except:
            pass
        

    @staticmethod
    def turn_off():
        Listener.stop

