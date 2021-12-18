# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_formats.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_file_formats(object):
    def setupUi(self, file_formats):
        if not file_formats.objectName():
            file_formats.setObjectName("file_formats")
        file_formats.resize(190, 130)
        file_formats.setMinimumSize(QSize(190, 130))
        file_formats.setMaximumSize(QSize(190, 130))
        self.centralwidget = QWidget(file_formats)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 0, 190, 128))
        self.frame.setMinimumSize(QSize(190, 128))
        self.frame.setMaximumSize(QSize(190, 128))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(0)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(15, 94, 161, 27))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok_but = QPushButton(self.horizontalLayoutWidget)
        self.ok_but.setObjectName("ok_but")
        self.ok_but.setMinimumSize(QSize(0, 20))
        self.ok_but.setMaximumSize(QSize(16777215, 20))
        self.ok_but.setStyleSheet("QWidget {\n"
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
        self.cancel_but.setObjectName("cancel_but")
        self.cancel_but.setMinimumSize(QSize(0, 20))
        self.cancel_but.setMaximumSize(QSize(16777215, 20))
        self.cancel_but.setStyleSheet("QWidget {\n"
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

        self.gridLayoutWidget_2 = QWidget(self.frame)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 23, 150, 42))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tif_but = QCheckBox(self.gridLayoutWidget_2)
        self.file_formats_Grp = QButtonGroup(file_formats)
        self.file_formats_Grp.setObjectName("file_formats_Grp")
        self.file_formats_Grp.setExclusive(False)
        self.file_formats_Grp.addButton(self.tif_but)
        self.tif_but.setObjectName("tif_but")

        self.gridLayout.addWidget(self.tif_but, 0, 1, 1, 1)

        self.png_but = QCheckBox(self.gridLayoutWidget_2)
        self.file_formats_Grp.addButton(self.png_but)
        self.png_but.setObjectName("png_but")

        self.gridLayout.addWidget(self.png_but, 1, 0, 1, 1)

        self.exr_but = QCheckBox(self.gridLayoutWidget_2)
        self.file_formats_Grp.addButton(self.exr_but)
        self.exr_but.setObjectName("exr_but")
        self.exr_but.setChecked(False)

        self.gridLayout.addWidget(self.exr_but, 0, 0, 1, 1)

        self.jpg_but = QCheckBox(self.gridLayoutWidget_2)
        self.file_formats_Grp.addButton(self.jpg_but)
        self.jpg_but.setObjectName("jpg_but")

        self.gridLayout.addWidget(self.jpg_but, 1, 1, 1, 1)

        self.tga_but = QCheckBox(self.gridLayoutWidget_2)
        self.file_formats_Grp.addButton(self.tga_but)
        self.tga_but.setObjectName("tga_but")
        self.tga_but.setChecked(False)

        self.gridLayout.addWidget(self.tga_but, 0, 2, 1, 1)

        self.jpeg_but = QCheckBox(self.gridLayoutWidget_2)
        self.file_formats_Grp.addButton(self.jpeg_but)
        self.jpeg_but.setObjectName("jpeg_but")
        self.jpeg_but.setChecked(False)

        self.gridLayout.addWidget(self.jpeg_but, 1, 2, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(15, 2, 159, 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.use_tx = QCheckBox(self.frame)
        self.use_tx.setObjectName("use_tx")
        self.use_tx.setGeometry(QRect(21, 71, 148, 20))
        file_formats.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(file_formats)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 190, 21))
        file_formats.setMenuBar(self.menubar)

        self.retranslateUi(file_formats)

        QMetaObject.connectSlotsByName(file_formats)
    # setupUi

    def retranslateUi(self, file_formats):
        file_formats.setWindowTitle(QCoreApplication.translate("file_formats", "MainWindow", None))
        self.ok_but.setText(QCoreApplication.translate("file_formats", "OK", None))
        self.cancel_but.setText(QCoreApplication.translate("file_formats", "Cancel", None))
        self.tif_but.setText(QCoreApplication.translate("file_formats", "tif", None))
        self.png_but.setText(QCoreApplication.translate("file_formats", "png", None))
        self.exr_but.setText(QCoreApplication.translate("file_formats", "exr", None))
        self.jpg_but.setText(QCoreApplication.translate("file_formats", "jpg", None))
        self.tga_but.setText(QCoreApplication.translate("file_formats", "tga", None))
        self.jpeg_but.setText(QCoreApplication.translate("file_formats", "jpeg", None))
        self.label.setText(QCoreApplication.translate("file_formats", "File formats to search for:", None))
        self.use_tx.setText(QCoreApplication.translate("file_formats", "Use TX Textures", None))
    # retranslateUi

