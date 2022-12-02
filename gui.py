import sys
from threading import Thread

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from capture import Capture
from main_widget import Ui_Form


class GUI(QMainWindow, Ui_Form):
    def __init__(self, capture: Capture, app: QApplication):
        super().__init__()
        self.app = app
        self.start_capture = False
        self.capture = capture
        self.setupUi(self)

        self.start_stop_btn.clicked.connect(self.toggle)
        self.browse_btn.clicked.connect(self.browse)
        self.topic_edit.textChanged.connect(self.change_topic)
        self.idx_spin_box.valueChanged.connect(self.change_idx)

        self.capture.bind_on_save_success_hook(lambda idx: self.idx_spin_box.setValue(idx))

    def toggle(self):
        self.start_capture = not self.start_capture
        if self.start_capture:
            self.capture.start()
            self.start_stop_btn.setText("停止")
        else:
            self.capture.stop()
            self.start_stop_btn.setText("开始")

    def browse(self):
        dir = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.cur_dir_browser.setText(dir)
        self.capture.set_save_path(dir)

    def change_topic(self, new: str):
        self.capture.set_topic(new)

    def change_idx(self, idx: int):
        self.capture.set_idx(idx)

    def run(self):
        daemon = Thread(target=self.capture.run, daemon=True)
        daemon.start()
        self.show()
        sys.exit(self.app.exec())
