import pynput, threading

from datetime import datetime
from pynput.keyboard import Key, Listener

word = ""
word_dict = {}

def on_press(key):
    global word
    global word_dict

    if ((key == Key.space) | (key == Key.alt) | (key == Key.cmd) | (key == Key.ctrl) | (key == Key.cmd) | (key == Key.delete) | (key == Key.down) | (key == Key.enter) | (key == Key.tab) | (key == Key.shift) | (key == Key.shift_r) | (key == Key.shift_l) | (key == Key.up)):
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
        word = ""
        return
    elif key == Key.backspace:
        if word != "":
            word = word[0:len(word)-1]
        else:
            word = ""
        return

    word += str(key).replace("'", "")

def on_release(key):
    if key == Key.f1:
        f = open(str(datetime.now())+".txt", "w+")
        for word in word_dict:
            f.write(word + ": " + str(word_dict[word]) + "\n")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    # print(threading.Thread.getName())
    listener.join()
