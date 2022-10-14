import os
INPUT_MAP = [0, 0.25, 0.27, 0.31, 0.35, 0.39, 0.43, 0.5, 0.6, 0.65, 0.69, 0.73, 0.76, 0.78, 1]

class Pad: #for writing controller inputs
    def __init__(self, path): #creates fifo, but does not open
        self.pipe = None
        self.path = path
        try:
            os.mkfifo(self.path)
        except OSError:
            pass

    def __enter__(self): #opens fifo
        self.pipe = open(self.path, 'w', buffering=1)
        return self

    def __exit__(self, *args): #closes fifo
        if self.pipe:
            self.pipe.close()

    def press_button(self, button): #presses a button
        self.pipe.write('PRESS {}\n'.format(button))

    def release_button(self, button): #releases a button
        self.pipe.write('RELEASE {}\n'.format(button))

    def set_stick(self, x, y): #sets gcn stick to corresponding MKW input
        self.pipe.write('SET MAIN {} {}\n'.format(INPUT_MAP[x], INPUT_MAP[y]))