import os
from time import sleep

import numpy as np
from PIL import ImageGrab


class Capture:
    def __init__(self):
        self.started = False
        self.last_mean = 0
        self.topic = "unknown"
        self.save_path = "."
        self.idx = 0
        self.hook = None

    def set_idx(self, idx: int):
        self.idx = idx

    def set_topic(self, topic: str):
        self.topic = topic

    def set_save_path(self, save_path: str):
        self.save_path = save_path

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def bind_on_save_success_hook(self, hook):
        self.hook = hook

    def run(self):
        while True:
            sleep(0.5)
            if not self.started:
                continue
            img = ImageGrab.grabclipboard()
            if img is None:
                continue
            img_np = np.asarray(img)
            cur_mean = img_np.mean()

            if cur_mean != self.last_mean:
                self.last_mean = cur_mean
                img_name = '{}_{}.png'.format(self.topic, self.idx)
                path = os.path.join(self.save_path, img_name)
                print('saving screenshot as %s...' % path)
                img.save(path, 'PNG')
                self.idx += 1
                self.hook(self.idx)
