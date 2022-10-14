import pad
import time
import os

with pad.Pad(os.path.expanduser('~/.local/share/dolphin-emu/Pipes/pad')) as p:
    for button in ['A', 'B', 'D_UP', 'D_DOWN', 'D_LEFT', 'D_RIGHT', 'L']:
        p.press_button(button)
        time.sleep(1)
        p.release_button(button)
    
    for i in range(15):
        p.set_stick(i, i)
        time.sleep(0.5)
    p.set_stick(7, 7)