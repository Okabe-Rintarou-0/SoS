import sys

from PyQt5.QtWidgets import QApplication

from capture import Capture
from gui import GUI

last_mean = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    capture = Capture()
    gui = GUI(capture, app)
    gui.run()
