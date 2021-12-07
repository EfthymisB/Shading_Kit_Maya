# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shader_list.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_shader_list_win(object):
    def setupUi(self, shader_list_win):
        if not shader_list_win.objectName():
            shader_list_win.setObjectName(u"shader_list_win")
        shader_list_win.resize(185, 158)
        shader_list_win.setMinimumSize(QSize(185, 158))
        shader_list_win.setMaximumSize(QSize(185, 158))
        self.centralwidget = QWidget(shader_list_win)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 185, 156))
        self.frame_2.setMinimumSize(QSize(185, 156))
        self.frame_2.setMaximumSize(QSize(186, 156))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setMidLineWidth(0)
        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(7, 7, 171, 106))
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(7, 117, 171, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok_but = QPushButton(self.horizontalLayoutWidget)
        self.ok_but.setObjectName(u"ok_but")
        self.ok_but.setMinimumSize(QSize(0, 20))
        self.ok_but.setMaximumSize(QSize(16777215, 20))
        self.ok_but.setStyleSheet(u"QWidget {\n"
"color: white;\n"
"background-color: rgba(70, 70, 70);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"\n"
"QWidget:hover{    \n"
"background-color: rgb(100, 100, 100);}\n"
"\n"
"QWidget:pressed{\n"
"background-color: rgba(50, 50, 50);}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.ok_but)

        self.cancel_but = QPushButton(self.horizontalLayoutWidget)
        self.cancel_but.setObjectName(u"cancel_but")
        self.cancel_but.setMinimumSize(QSize(0, 20))
        self.cancel_but.setMaximumSize(QSize(16777215, 20))
        self.cancel_but.setStyleSheet(u"QWidget {\n"
"color: white;\n"
"background-color: rgba(70, 70, 70);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"\n"
"QWidget:hover{    \n"
"background-color: rgb(100, 100, 100);}\n"
"\n"
"QWidget:pressed{\n"
"background-color: rgba(50, 50, 50);}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.cancel_but)

        shader_list_win.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(shader_list_win)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 185, 21))
        shader_list_win.setMenuBar(self.menubar)

        self.retranslateUi(shader_list_win)

        QMetaObject.connectSlotsByName(shader_list_win)
    # setupUi

    def retranslateUi(self, shader_list_win):
        shader_list_win.setWindowTitle(QCoreApplication.translate("shader_list_win", u"MainWindow", None))
        self.ok_but.setText(QCoreApplication.translate("shader_list_win", u"Delete", None))
        self.cancel_but.setText(QCoreApplication.translate("shader_list_win", u"Cancel", None))
    # retranslateUi

