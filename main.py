import keyboard
import clipboard
import pyautogui
import time

key_array = ['&','é','"','\'','(']
ram = ["","","","",""]
copy_key_prefix = "shift+ctrl+"
paste_key_prefix = "shift+alt+"
def _copy(ind):
    old = clipboard.paste()
    pyautogui.keyUp('shift')
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(.1)
    ram[int(ind)] = clipboard.paste()
    clipboard.copy(old)
def _paste(ind):
    old = clipboard.paste()
    clipboard.copy(ram[int(ind)])
    pyautogui.keyUp('shift')
    pyautogui.keyUp('alt')
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    time.sleep(.1)
    clipboard.copy(old)
index = 0
for key in key_array:
    keyboard.add_hotkey(copy_key_prefix + key, _copy, args=(str(index)))
    keyboard.add_hotkey(paste_key_prefix + key, _paste, args=(str(index)))
    index += 1
keyboard.wait()