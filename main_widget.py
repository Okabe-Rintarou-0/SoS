# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(747, 90)
        self.start_stop_btn = QtWidgets.QPushButton(Form)
        self.start_stop_btn.setGeometry(QtCore.QRect(630, 20, 101, 51))
        self.start_stop_btn.setObjectName("start_stop_btn")
        self.cur_dir_label = QtWidgets.QLabel(Form)
        self.cur_dir_label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.cur_dir_label.setObjectName("cur_dir_label")
        self.cur_dir_browser = QtWidgets.QTextBrowser(Form)
        self.cur_dir_browser.setGeometry(QtCore.QRect(100, 10, 411, 31))
        self.cur_dir_browser.setObjectName("cur_dir_browser")
        self.topic_label = QtWidgets.QLabel(Form)
        self.topic_label.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.topic_label.setObjectName("topic_label")
        self.browse_btn = QtWidgets.QPushButton(Form)
        self.browse_btn.setGeometry(QtCore.QRect(520, 10, 81, 31))
        self.browse_btn.setObjectName("browse_btn")
        self.topic_edit = QtWidgets.QLineEdit(Form)
        self.topic_edit.setGeometry(QtCore.QRect(110, 50, 271, 31))
        self.topic_edit.setObjectName("topic_edit")
        self.idx_spin_box = QtWidgets.QSpinBox(Form)
        self.idx_spin_box.setGeometry(QtCore.QRect(450, 50, 131, 31))
        self.idx_spin_box.setObjectName("idx_spin_box")
        self.idx_label = QtWidgets.QLabel(Form)
        self.idx_label.setGeometry(QtCore.QRect(410, 60, 41, 16))
        self.idx_label.setObjectName("idx_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "截图即保存"))
        self.start_stop_btn.setText(_translate("Form", "开始"))
        self.cur_dir_label.setText(_translate("Form", "当前文件夹"))
        self.topic_label.setText(_translate("Form", "当前 topic"))
        self.browse_btn.setText(_translate("Form", "浏览"))
        self.idx_label.setText(_translate("Form", "下标"))
