# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(216, 446)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(216, 446))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 216, 415))
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.shader_text = QLineEdit(self.tab)
        self.shader_text.setObjectName("shader_text")
        self.shader_text.setGeometry(QRect(25, 20, 161, 20))
        self.label = QLabel(self.tab)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(25, 1, 161, 17))
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 42, 211, 22))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.selectAll = QPushButton(self.horizontalLayoutWidget)
        self.rounded_buttons = QButtonGroup(MainWindow)
        self.rounded_buttons.setObjectName("rounded_buttons")
        self.rounded_buttons.setExclusive(False)
        self.rounded_buttons.addButton(self.selectAll)
        self.selectAll.setObjectName("selectAll")
        self.selectAll.setMinimumSize(QSize(20, 20))
        self.selectAll.setMaximumSize(QSize(20, 20))
        self.selectAll.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectAll.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgba(70, 70, 70);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:10px;\n"
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
        self.selectAll.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.selectAll)

        self.expand_Utils = QPushButton(self.horizontalLayoutWidget)
        self.rounded_buttons.addButton(self.expand_Utils)
        self.expand_Utils.setObjectName("expand_Utils")
        self.expand_Utils.setMinimumSize(QSize(20, 20))
        self.expand_Utils.setMaximumSize(QSize(20, 20))
        self.expand_Utils.setCursor(QCursor(Qt.PointingHandCursor))
        self.expand_Utils.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgba(70, 70, 70);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:10px;\n"
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
        self.expand_Utils.setCheckable(True)
        self.expand_Utils.setChecked(True)

        self.horizontalLayout_10.addWidget(self.expand_Utils)

        self.deselectAll = QPushButton(self.horizontalLayoutWidget)
        self.rounded_buttons.addButton(self.deselectAll)
        self.deselectAll.setObjectName("deselectAll")
        self.deselectAll.setMinimumSize(QSize(20, 20))
        self.deselectAll.setMaximumSize(QSize(20, 20))
        self.deselectAll.setCursor(QCursor(Qt.PointingHandCursor))
        self.deselectAll.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgba(70, 70, 70);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:10px;\n"
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
        self.deselectAll.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.deselectAll)

        self.createShaderWidget = QWidget(self.tab)
        self.createShaderWidget.setObjectName("createShaderWidget")
        self.createShaderWidget.setGeometry(QRect(0, 280, 211, 91))
        self.selectDirectory = QPushButton(self.createShaderWidget)
        self.selectDirectory.setObjectName("selectDirectory")
        self.selectDirectory.setGeometry(QRect(178, 35, 20, 20))
        self.selectDirectory.setMinimumSize(QSize(0, 0))
        self.selectDirectory.setMaximumSize(QSize(20, 20))
        self.selectDirectory.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectDirectory.setStyleSheet("")
        self.use_dir = QPushButton(self.createShaderWidget)
        self.udim_selected_dir_Grp = QButtonGroup(MainWindow)
        self.udim_selected_dir_Grp.setObjectName("udim_selected_dir_Grp")
        self.udim_selected_dir_Grp.setExclusive(False)
        self.udim_selected_dir_Grp.addButton(self.use_dir)
        self.use_dir.setObjectName("use_dir")
        self.use_dir.setGeometry(QRect(8, 10, 83, 20))
        self.use_dir.setMinimumSize(QSize(0, 0))
        self.use_dir.setMaximumSize(QSize(90, 20))
        self.use_dir.setCursor(QCursor(Qt.PointingHandCursor))
        self.use_dir.setStyleSheet("QWidget {\n"
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
        self.use_dir.setCheckable(True)
        self.directoryPath = QLineEdit(self.createShaderWidget)
        self.directoryPath.setObjectName("directoryPath")
        self.directoryPath.setGeometry(QRect(8, 35, 166, 20))
        self.directoryPath.setMinimumSize(QSize(0, 0))
        self.directoryPath.setMaximumSize(QSize(16777215, 20))
        self.udim = QPushButton(self.createShaderWidget)
        self.udim_selected_dir_Grp.addButton(self.udim)
        self.udim.setObjectName("udim")
        self.udim.setGeometry(QRect(157, 10, 41, 20))
        self.udim.setMinimumSize(QSize(0, 0))
        self.udim.setMaximumSize(QSize(41, 20))
        self.udim.setCursor(QCursor(Qt.PointingHandCursor))
        self.udim.setStyleSheet("QWidget {\n"
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
        self.udim.setCheckable(True)
        self.assign_to_viewport = QPushButton(self.createShaderWidget)
        self.udim_selected_dir_Grp.addButton(self.assign_to_viewport)
        self.assign_to_viewport.setObjectName("assign_to_viewport")
        self.assign_to_viewport.setGeometry(QRect(93, 10, 62, 20))
        self.assign_to_viewport.setMinimumSize(QSize(0, 0))
        self.assign_to_viewport.setMaximumSize(QSize(62, 20))
        self.assign_to_viewport.setCursor(QCursor(Qt.PointingHandCursor))
        self.assign_to_viewport.setStyleSheet("QWidget {\n"
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
        self.assign_to_viewport.setCheckable(True)
        self.createShader = QPushButton(self.createShaderWidget)
        self.createShader.setObjectName("createShader")
        self.createShader.setGeometry(QRect(8, 60, 94, 20))
        self.createShader.setMinimumSize(QSize(0, 0))
        self.createShader.setMaximumSize(QSize(94, 20))
        self.createShader.setCursor(QCursor(Qt.PointingHandCursor))
        self.createShader.setStyleSheet("QWidget {\n"
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
        self.deleteShader = QPushButton(self.createShaderWidget)
        self.deleteShader.setObjectName("deleteShader")
        self.deleteShader.setGeometry(QRect(104, 60, 94, 20))
        self.deleteShader.setMinimumSize(QSize(0, 0))
        self.deleteShader.setMaximumSize(QSize(94, 20))
        self.deleteShader.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteShader.setStyleSheet("QWidget {\n"
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
        self.gridLayoutWidget_2 = QWidget(self.tab)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 66, 217, 283))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 2, 5, 2)
        self.bumpButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.setExclusive(False)
        self.buttonGroup.addButton(self.bumpButton)
        self.bumpButton.setObjectName("bumpButton")
        self.bumpButton.setMinimumSize(QSize(60, 20))
        self.bumpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.bumpButton.setStyleSheet("QWidget {\n"
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
        self.bumpButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.bumpButton, 7, 3, 1, 1)

        self.baseColorButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup.addButton(self.baseColorButton)
        self.baseColorButton.setObjectName("baseColorButton")
        self.baseColorButton.setMinimumSize(QSize(60, 20))
        self.baseColorButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.baseColorButton.setStyleSheet("QWidget {\n"
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
        self.baseColorButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.baseColorButton, 0, 1, 1, 1)

        self.specularButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup.addButton(self.specularButton)
        self.specularButton.setObjectName("specularButton")
        self.specularButton.setMinimumSize(QSize(60, 20))
        self.specularButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.specularButton.setStyleSheet("QWidget {\n"
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
        self.specularButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.specularButton, 0, 2, 1, 1)

        self.coatButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup.addButton(self.coatButton)
        self.coatButton.setObjectName("coatButton")
        self.coatButton.setMinimumSize(QSize(60, 20))
        self.coatButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.coatButton.setStyleSheet("QWidget {\n"
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
        self.coatButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.coatButton, 3, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 6, 1, 1, 2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 2, 1, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 8, 1, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.tree_but_2 = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons = QButtonGroup(MainWindow)
        self.tree_Buttons.setObjectName("tree_Buttons")
        self.tree_Buttons.setExclusive(False)
        self.tree_Buttons.addButton(self.tree_but_2)
        self.tree_but_2.setObjectName("tree_but_2")
        self.tree_but_2.setMinimumSize(QSize(0, 0))
        self.tree_but_2.setMaximumSize(QSize(30, 70))
        self.tree_but_2.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_3.addWidget(self.tree_but_2)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.baseColor_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_BC = QButtonGroup(MainWindow)
        self.Utils_BC.setObjectName("Utils_BC")
        self.Utils_BC.setExclusive(False)
        self.Utils_BC.addButton(self.baseColor_aiColorCorrect)
        self.baseColor_aiColorCorrect.setObjectName("baseColor_aiColorCorrect")
        self.baseColor_aiColorCorrect.setEnabled(True)

        self.gridLayout_6.addWidget(self.baseColor_aiColorCorrect, 2, 0, 1, 1)

        self.baseColor_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_BC.addButton(self.baseColor_aiRange)
        self.baseColor_aiRange.setObjectName("baseColor_aiRange")

        self.gridLayout_6.addWidget(self.baseColor_aiRange, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.baseColor_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_BC.addButton(self.baseColor_aiClamp)
        self.baseColor_aiClamp.setObjectName("baseColor_aiClamp")

        self.gridLayout_6.addWidget(self.baseColor_aiClamp, 3, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_6)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.tree_but_5 = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons.addButton(self.tree_but_5)
        self.tree_but_5.setObjectName("tree_but_5")
        self.tree_but_5.setMinimumSize(QSize(0, 0))
        self.tree_but_5.setMaximumSize(QSize(30, 70))
        self.tree_but_5.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_6.addWidget(self.tree_but_5)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_17, 0, 0, 1, 1)

        self.coat_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Coat = QButtonGroup(MainWindow)
        self.Utils_Coat.setObjectName("Utils_Coat")
        self.Utils_Coat.setExclusive(False)
        self.Utils_Coat.addButton(self.coat_aiRange)
        self.coat_aiRange.setObjectName("coat_aiRange")

        self.gridLayout_9.addWidget(self.coat_aiRange, 1, 0, 1, 1)

        self.coat_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Coat.addButton(self.coat_aiColorCorrect)
        self.coat_aiColorCorrect.setObjectName("coat_aiColorCorrect")
        self.coat_aiColorCorrect.setEnabled(True)

        self.gridLayout_9.addWidget(self.coat_aiColorCorrect, 2, 0, 1, 1)

        self.coat_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Coat.addButton(self.coat_aiClamp)
        self.coat_aiClamp.setObjectName("coat_aiClamp")

        self.gridLayout_9.addWidget(self.coat_aiClamp, 3, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_9)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 4, 2, 1, 1)

        self.displacementButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup.addButton(self.displacementButton)
        self.displacementButton.setObjectName("displacementButton")
        self.displacementButton.setMinimumSize(QSize(60, 20))
        self.displacementButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.displacementButton.setStyleSheet("QWidget {\n"
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
        self.displacementButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.displacementButton, 3, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.tree_but_7 = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons.addButton(self.tree_but_7)
        self.tree_but_7.setObjectName("tree_but_7")
        self.tree_but_7.setMinimumSize(QSize(0, 0))
        self.tree_but_7.setMaximumSize(QSize(30, 70))
        self.tree_but_7.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_8.addWidget(self.tree_but_7)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.sss_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_SSS = QButtonGroup(MainWindow)
        self.Utils_SSS.setObjectName("Utils_SSS")
        self.Utils_SSS.setExclusive(False)
        self.Utils_SSS.addButton(self.sss_aiRange)
        self.sss_aiRange.setObjectName("sss_aiRange")

        self.gridLayout_11.addWidget(self.sss_aiRange, 1, 0, 1, 1)

        self.sss_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_SSS.addButton(self.sss_aiColorCorrect)
        self.sss_aiColorCorrect.setObjectName("sss_aiColorCorrect")
        self.sss_aiColorCorrect.setEnabled(True)

        self.gridLayout_11.addWidget(self.sss_aiColorCorrect, 2, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_19, 0, 0, 1, 1)

        self.sss_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_SSS.addButton(self.sss_aiClamp)
        self.sss_aiClamp.setObjectName("sss_aiClamp")

        self.gridLayout_11.addWidget(self.sss_aiClamp, 3, 0, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_11)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 9, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.tree_but_4 = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons.addButton(self.tree_but_4)
        self.tree_but_4.setObjectName("tree_but_4")
        self.tree_but_4.setMinimumSize(QSize(0, 0))
        self.tree_but_4.setMaximumSize(QSize(30, 70))
        self.tree_but_4.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_5.addWidget(self.tree_but_4)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.disp_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Disp = QButtonGroup(MainWindow)
        self.Utils_Disp.setObjectName("Utils_Disp")
        self.Utils_Disp.setExclusive(False)
        self.Utils_Disp.addButton(self.disp_aiRange)
        self.disp_aiRange.setObjectName("disp_aiRange")

        self.gridLayout_8.addWidget(self.disp_aiRange, 1, 0, 1, 1)

        self.disp_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Disp.addButton(self.disp_aiColorCorrect)
        self.disp_aiColorCorrect.setObjectName("disp_aiColorCorrect")
        self.disp_aiColorCorrect.setEnabled(True)

        self.gridLayout_8.addWidget(self.disp_aiColorCorrect, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.disp_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Disp.addButton(self.disp_aiClamp)
        self.disp_aiClamp.setObjectName("disp_aiClamp")

        self.gridLayout_8.addWidget(self.disp_aiClamp, 3, 0, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_8)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.tree_but_8 = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons.addButton(self.tree_but_8)
        self.tree_but_8.setObjectName("tree_but_8")
        self.tree_but_8.setMinimumSize(QSize(0, 0))
        self.tree_but_8.setMaximumSize(QSize(30, 70))
        self.tree_but_8.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_9.addWidget(self.tree_but_8)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.bump_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Bump = QButtonGroup(MainWindow)
        self.Utils_Bump.setObjectName("Utils_Bump")
        self.Utils_Bump.setExclusive(False)
        self.Utils_Bump.addButton(self.bump_aiColorCorrect)
        self.bump_aiColorCorrect.setObjectName("bump_aiColorCorrect")
        self.bump_aiColorCorrect.setEnabled(True)

        self.gridLayout_12.addWidget(self.bump_aiColorCorrect, 2, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_20, 0, 0, 1, 1)

        self.bump_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Bump.addButton(self.bump_aiRange)
        self.bump_aiRange.setObjectName("bump_aiRange")

        self.gridLayout_12.addWidget(self.bump_aiRange, 1, 0, 1, 1)

        self.bump_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Bump.addButton(self.bump_aiClamp)
        self.bump_aiClamp.setObjectName("bump_aiClamp")

        self.gridLayout_12.addWidget(self.bump_aiClamp, 3, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout_12)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 9, 3, 1, 1)

        self.sssButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup.addButton(self.sssButton)
        self.sssButton.setObjectName("sssButton")
        self.sssButton.setMinimumSize(QSize(60, 20))
        self.sssButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sssButton.setStyleSheet("QWidget {\n"
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
        self.sssButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.sssButton, 7, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.tree_but_6 = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons.addButton(self.tree_but_6)
        self.tree_but_6.setObjectName("tree_but_6")
        self.tree_but_6.setMinimumSize(QSize(0, 0))
        self.tree_but_6.setMaximumSize(QSize(30, 70))
        self.tree_but_6.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_7.addWidget(self.tree_but_6)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_18, 0, 0, 1, 1)

        self.normal_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Normal = QButtonGroup(MainWindow)
        self.Utils_Normal.setObjectName("Utils_Normal")
        self.Utils_Normal.setExclusive(False)
        self.Utils_Normal.addButton(self.normal_aiRange)
        self.normal_aiRange.setObjectName("normal_aiRange")

        self.gridLayout_10.addWidget(self.normal_aiRange, 1, 0, 1, 1)

        self.normal_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Normal.addButton(self.normal_aiColorCorrect)
        self.normal_aiColorCorrect.setObjectName("normal_aiColorCorrect")
        self.normal_aiColorCorrect.setEnabled(True)

        self.gridLayout_10.addWidget(self.normal_aiColorCorrect, 2, 0, 1, 1)

        self.normal_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Normal.addButton(self.normal_aiClamp)
        self.normal_aiClamp.setObjectName("normal_aiClamp")

        self.gridLayout_10.addWidget(self.normal_aiClamp, 3, 0, 1, 1)


        self.horizontalLayout_7.addLayout(self.gridLayout_10)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 4, 3, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.tree_but_3 = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons.addButton(self.tree_but_3)
        self.tree_but_3.setObjectName("tree_but_3")
        self.tree_but_3.setMinimumSize(QSize(0, 0))
        self.tree_but_3.setMaximumSize(QSize(30, 70))
        self.tree_but_3.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_4.addWidget(self.tree_but_3)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.metal_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Metal = QButtonGroup(MainWindow)
        self.Utils_Metal.setObjectName("Utils_Metal")
        self.Utils_Metal.setExclusive(False)
        self.Utils_Metal.addButton(self.metal_aiClamp)
        self.metal_aiClamp.setObjectName("metal_aiClamp")

        self.gridLayout_7.addWidget(self.metal_aiClamp, 3, 0, 1, 1)

        self.metal_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Metal.addButton(self.metal_aiColorCorrect)
        self.metal_aiColorCorrect.setObjectName("metal_aiColorCorrect")
        self.metal_aiColorCorrect.setEnabled(True)

        self.gridLayout_7.addWidget(self.metal_aiColorCorrect, 2, 0, 1, 1)

        self.metal_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Metal.addButton(self.metal_aiRange)
        self.metal_aiRange.setObjectName("metal_aiRange")

        self.gridLayout_7.addWidget(self.metal_aiRange, 1, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_7)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 3, 1, 1)

        self.normalButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup.addButton(self.normalButton)
        self.normalButton.setObjectName("normalButton")
        self.normalButton.setMinimumSize(QSize(60, 20))
        self.normalButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.normalButton.setStyleSheet("QWidget {\n"
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
        self.normalButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.normalButton, 3, 3, 1, 1)

        self.metalnessButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup.addButton(self.metalnessButton)
        self.metalnessButton.setObjectName("metalnessButton")
        self.metalnessButton.setMinimumSize(QSize(60, 20))
        self.metalnessButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.metalnessButton.setStyleSheet("QWidget {\n"
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
        self.metalnessButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.metalnessButton, 0, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.tree_but = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons.addButton(self.tree_but)
        self.tree_but.setObjectName("tree_but")
        self.tree_but.setMinimumSize(QSize(0, 0))
        self.tree_but.setMaximumSize(QSize(30, 70))
        self.tree_but.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.tree_but)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.spec_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Spec = QButtonGroup(MainWindow)
        self.Utils_Spec.setObjectName("Utils_Spec")
        self.Utils_Spec.setExclusive(False)
        self.Utils_Spec.addButton(self.spec_aiColorCorrect)
        self.spec_aiColorCorrect.setObjectName("spec_aiColorCorrect")
        self.spec_aiColorCorrect.setEnabled(True)

        self.gridLayout_4.addWidget(self.spec_aiColorCorrect, 2, 0, 1, 1)

        self.spec_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Spec.addButton(self.spec_aiRange)
        self.spec_aiRange.setObjectName("spec_aiRange")

        self.gridLayout_4.addWidget(self.spec_aiRange, 1, 0, 1, 1)

        self.spec_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Spec.addButton(self.spec_aiClamp)
        self.spec_aiClamp.setObjectName("spec_aiClamp")

        self.gridLayout_4.addWidget(self.spec_aiClamp, 3, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_4)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 2, 1, 1)

        self.opacityButton = QPushButton(self.gridLayoutWidget_2)
        self.buttonGroup.addButton(self.opacityButton)
        self.opacityButton.setObjectName("opacityButton")
        self.opacityButton.setMinimumSize(QSize(60, 20))
        self.opacityButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.opacityButton.setStyleSheet("QWidget {\n"
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
        self.opacityButton.setCheckable(True)

        self.gridLayout_2.addWidget(self.opacityButton, 7, 2, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.tree_but_9 = QPushButton(self.gridLayoutWidget_2)
        self.tree_Buttons.addButton(self.tree_but_9)
        self.tree_but_9.setObjectName("tree_but_9")
        self.tree_but_9.setMinimumSize(QSize(0, 0))
        self.tree_but_9.setMaximumSize(QSize(30, 70))
        self.tree_but_9.setStyleSheet("border:none;\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_11.addWidget(self.tree_but_9)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.opacity_aiRange = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Opacity = QButtonGroup(MainWindow)
        self.Utils_Opacity.setObjectName("Utils_Opacity")
        self.Utils_Opacity.setExclusive(False)
        self.Utils_Opacity.addButton(self.opacity_aiRange)
        self.opacity_aiRange.setObjectName("opacity_aiRange")

        self.gridLayout_14.addWidget(self.opacity_aiRange, 1, 0, 1, 1)

        self.opacity_aiColorCorrect = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Opacity.addButton(self.opacity_aiColorCorrect)
        self.opacity_aiColorCorrect.setObjectName("opacity_aiColorCorrect")
        self.opacity_aiColorCorrect.setEnabled(True)

        self.gridLayout_14.addWidget(self.opacity_aiColorCorrect, 2, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_21, 0, 0, 1, 1)

        self.opacity_aiClamp = QCheckBox(self.gridLayoutWidget_2)
        self.Utils_Opacity.addButton(self.opacity_aiClamp)
        self.opacity_aiClamp.setObjectName("opacity_aiClamp")

        self.gridLayout_14.addWidget(self.opacity_aiClamp, 3, 0, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout_14)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 9, 2, 1, 1)

        self.aov_frame = QFrame(self.tab)
        self.aov_frame.setObjectName("aov_frame")
        self.aov_frame.setGeometry(QRect(0, 390, 211, 165))
        self.aov_frame.setFrameShape(QFrame.NoFrame)
        self.aov_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_4 = QWidget(self.aov_frame)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 130, 209, 24))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.create_AOVs = QPushButton(self.horizontalLayoutWidget_4)
        self.create_AOVs.setObjectName("create_AOVs")
        self.create_AOVs.setMinimumSize(QSize(60, 20))
        self.create_AOVs.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_AOVs.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgba(50, 50, 50);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"\n"
"QWidget:hover{    \n"
"background-color: rgb(100, 100, 100);}\n"
"\n"
"QWidget:pressed{\n"
"background-color: rgba(30, 30, 30);}\n"
"\n"
"\n"
"")
        self.create_AOVs.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.create_AOVs)

        self.delete_AOVs = QPushButton(self.horizontalLayoutWidget_4)
        self.delete_AOVs.setObjectName("delete_AOVs")
        self.delete_AOVs.setMinimumSize(QSize(60, 20))
        self.delete_AOVs.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_AOVs.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgba(50, 50, 50);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"\n"
"QWidget:hover{    \n"
"background-color: rgb(100, 100, 100);}\n"
"\n"
"QWidget:pressed{\n"
"background-color: rgba(30, 30, 30);}\n"
"\n"
"\n"
"")
        self.delete_AOVs.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.delete_AOVs)

        self.gridLayoutWidget_7 = QWidget(self.aov_frame)
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 25, 212, 104))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(4)
        self.gridLayout_16.setVerticalSpacing(6)
        self.gridLayout_16.setContentsMargins(5, 2, 5, 2)
        self.metalnessButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts = QButtonGroup(MainWindow)
        self.AOV_buts.setObjectName("AOV_buts")
        self.AOV_buts.setExclusive(False)
        self.AOV_buts.addButton(self.metalnessButton_AOV)
        self.metalnessButton_AOV.setObjectName("metalnessButton_AOV")
        self.metalnessButton_AOV.setMinimumSize(QSize(60, 20))
        self.metalnessButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.metalnessButton_AOV.setStyleSheet("QWidget {\n"
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
        self.metalnessButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.metalnessButton_AOV, 1, 2, 1, 1)

        self.normalButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts.addButton(self.normalButton_AOV)
        self.normalButton_AOV.setObjectName("normalButton_AOV")
        self.normalButton_AOV.setMinimumSize(QSize(60, 20))
        self.normalButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.normalButton_AOV.setStyleSheet("QWidget {\n"
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
        self.normalButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.normalButton_AOV, 2, 2, 1, 1)

        self.coatButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts.addButton(self.coatButton_AOV)
        self.coatButton_AOV.setObjectName("coatButton_AOV")
        self.coatButton_AOV.setMinimumSize(QSize(60, 20))
        self.coatButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.coatButton_AOV.setStyleSheet("QWidget {\n"
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
        self.coatButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.coatButton_AOV, 2, 1, 1, 1)

        self.bumpButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts.addButton(self.bumpButton_AOV)
        self.bumpButton_AOV.setObjectName("bumpButton_AOV")
        self.bumpButton_AOV.setMinimumSize(QSize(60, 20))
        self.bumpButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.bumpButton_AOV.setStyleSheet("QWidget {\n"
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
        self.bumpButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.bumpButton_AOV, 3, 2, 1, 1)

        self.sssButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts.addButton(self.sssButton_AOV)
        self.sssButton_AOV.setObjectName("sssButton_AOV")
        self.sssButton_AOV.setMinimumSize(QSize(60, 20))
        self.sssButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.sssButton_AOV.setStyleSheet("QWidget {\n"
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
        self.sssButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.sssButton_AOV, 3, 0, 1, 1)

        self.displacementButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts.addButton(self.displacementButton_AOV)
        self.displacementButton_AOV.setObjectName("displacementButton_AOV")
        self.displacementButton_AOV.setMinimumSize(QSize(60, 20))
        self.displacementButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.displacementButton_AOV.setStyleSheet("QWidget {\n"
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
        self.displacementButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.displacementButton_AOV, 2, 0, 1, 1)

        self.opacityButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts.addButton(self.opacityButton_AOV)
        self.opacityButton_AOV.setObjectName("opacityButton_AOV")
        self.opacityButton_AOV.setMinimumSize(QSize(60, 20))
        self.opacityButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.opacityButton_AOV.setStyleSheet("QWidget {\n"
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
        self.opacityButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.opacityButton_AOV, 3, 1, 1, 1)

        self.specularButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts.addButton(self.specularButton_AOV)
        self.specularButton_AOV.setObjectName("specularButton_AOV")
        self.specularButton_AOV.setMinimumSize(QSize(60, 20))
        self.specularButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.specularButton_AOV.setStyleSheet("QWidget {\n"
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
        self.specularButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.specularButton_AOV, 1, 1, 1, 1)

        self.baseColorButton_AOV = QPushButton(self.gridLayoutWidget_7)
        self.AOV_buts.addButton(self.baseColorButton_AOV)
        self.baseColorButton_AOV.setObjectName("baseColorButton_AOV")
        self.baseColorButton_AOV.setMinimumSize(QSize(60, 20))
        self.baseColorButton_AOV.setCursor(QCursor(Qt.PointingHandCursor))
        self.baseColorButton_AOV.setStyleSheet("QWidget {\n"
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
        self.baseColorButton_AOV.setCheckable(True)

        self.gridLayout_16.addWidget(self.baseColorButton_AOV, 1, 0, 1, 1)

        self.sel_all_aovs = QPushButton(self.gridLayoutWidget_7)
        self.sel_all_aovs.setObjectName("sel_all_aovs")
        self.sel_all_aovs.setMinimumSize(QSize(60, 20))
        self.sel_all_aovs.setCursor(QCursor(Qt.PointingHandCursor))
        self.sel_all_aovs.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgba(50, 50, 50);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"\n"
"QWidget:hover{    \n"
"background-color: rgb(100, 100, 100);}\n"
"\n"
"QWidget:pressed{\n"
"background-color: rgba(30, 30, 30);}\n"
"\n"
"\n"
"")
        self.sel_all_aovs.setCheckable(True)

        self.gridLayout_16.addWidget(self.sel_all_aovs, 0, 0, 1, 1)

        self.desel_all_aovs = QPushButton(self.gridLayoutWidget_7)
        self.desel_all_aovs.setObjectName("desel_all_aovs")
        self.desel_all_aovs.setMinimumSize(QSize(60, 20))
        self.desel_all_aovs.setCursor(QCursor(Qt.PointingHandCursor))
        self.desel_all_aovs.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgba(50, 50, 50);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"\n"
"QWidget:hover{    \n"
"background-color: rgb(100, 100, 100);}\n"
"\n"
"QWidget:pressed{\n"
"background-color: rgba(30, 30, 30);}\n"
"\n"
"\n"
"")
        self.desel_all_aovs.setCheckable(True)

        self.gridLayout_16.addWidget(self.desel_all_aovs, 0, 1, 1, 1)

        self.match_sel_aovs = QPushButton(self.gridLayoutWidget_7)
        self.match_sel_aovs.setObjectName("match_sel_aovs")
        self.match_sel_aovs.setMinimumSize(QSize(60, 20))
        self.match_sel_aovs.setCursor(QCursor(Qt.PointingHandCursor))
        self.match_sel_aovs.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgba(50, 50, 50);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"\n"
"QWidget:hover{    \n"
"background-color: rgb(100, 100, 100);}\n"
"\n"
"QWidget:pressed{\n"
"background-color: rgba(30, 30, 30);}\n"
"\n"
"\n"
"")
        self.match_sel_aovs.setCheckable(True)

        self.gridLayout_16.addWidget(self.match_sel_aovs, 0, 2, 1, 1)

        self.label_12 = QLabel(self.aov_frame)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QRect(0, 0, 211, 20))
        self.label_12.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.createShaderWidget.raise_()
        self.shader_text.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.aov_frame.raise_()
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget = QWidget(self.tab_3)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(10, 3, 181, 271))
        self.default_textures_groupBox = QGroupBox(self.widget)
        self.default_textures_groupBox.setObjectName("default_textures_groupBox")
        self.default_textures_groupBox.setGeometry(QRect(0, 107, 181, 164))
        self.default_textures_groupBox.setStyleSheet("")
        self.default_textures_groupBox.setAlignment(Qt.AlignCenter)
        self.default_textures_groupBox.setFlat(False)
        self.default_textures_groupBox.setCheckable(False)
        self.gridLayoutWidget_3 = QWidget(self.default_textures_groupBox)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 19, 161, 140))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.coatButton_def = QPushButton(self.gridLayoutWidget_3)
        self.buttonGroup_def = QButtonGroup(MainWindow)
        self.buttonGroup_def.setObjectName("buttonGroup_def")
        self.buttonGroup_def.setExclusive(False)
        self.buttonGroup_def.addButton(self.coatButton_def)
        self.coatButton_def.setObjectName("coatButton_def")
        self.coatButton_def.setMinimumSize(QSize(71, 20))
        self.coatButton_def.setCursor(QCursor(Qt.PointingHandCursor))
        self.coatButton_def.setStyleSheet("QWidget {\n"
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
        self.coatButton_def.setCheckable(True)

        self.gridLayout_3.addWidget(self.coatButton_def, 2, 1, 1, 1)

        self.normalButton_def = QPushButton(self.gridLayoutWidget_3)
        self.buttonGroup_def.addButton(self.normalButton_def)
        self.normalButton_def.setObjectName("normalButton_def")
        self.normalButton_def.setMinimumSize(QSize(71, 20))
        self.normalButton_def.setCursor(QCursor(Qt.PointingHandCursor))
        self.normalButton_def.setStyleSheet("QWidget {\n"
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
        self.normalButton_def.setCheckable(True)

        self.gridLayout_3.addWidget(self.normalButton_def, 2, 0, 1, 1)

        self.specularButton_def = QPushButton(self.gridLayoutWidget_3)
        self.buttonGroup_def.addButton(self.specularButton_def)
        self.specularButton_def.setObjectName("specularButton_def")
        self.specularButton_def.setMinimumSize(QSize(71, 20))
        self.specularButton_def.setCursor(QCursor(Qt.PointingHandCursor))
        self.specularButton_def.setStyleSheet("QWidget {\n"
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
        self.specularButton_def.setCheckable(True)

        self.gridLayout_3.addWidget(self.specularButton_def, 0, 1, 1, 1)

        self.baseColorButton_def = QPushButton(self.gridLayoutWidget_3)
        self.buttonGroup_def.addButton(self.baseColorButton_def)
        self.baseColorButton_def.setObjectName("baseColorButton_def")
        self.baseColorButton_def.setMinimumSize(QSize(71, 20))
        self.baseColorButton_def.setCursor(QCursor(Qt.PointingHandCursor))
        self.baseColorButton_def.setStyleSheet("QWidget {\n"
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
        self.baseColorButton_def.setCheckable(True)

        self.gridLayout_3.addWidget(self.baseColorButton_def, 0, 0, 1, 1)

        self.metalnessButton_def = QPushButton(self.gridLayoutWidget_3)
        self.buttonGroup_def.addButton(self.metalnessButton_def)
        self.metalnessButton_def.setObjectName("metalnessButton_def")
        self.metalnessButton_def.setMinimumSize(QSize(71, 20))
        self.metalnessButton_def.setCursor(QCursor(Qt.PointingHandCursor))
        self.metalnessButton_def.setStyleSheet("QWidget {\n"
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
        self.metalnessButton_def.setCheckable(True)

        self.gridLayout_3.addWidget(self.metalnessButton_def, 1, 0, 1, 1)

        self.sssButton_def = QPushButton(self.gridLayoutWidget_3)
        self.buttonGroup_def.addButton(self.sssButton_def)
        self.sssButton_def.setObjectName("sssButton_def")
        self.sssButton_def.setMinimumSize(QSize(71, 20))
        self.sssButton_def.setCursor(QCursor(Qt.PointingHandCursor))
        self.sssButton_def.setStyleSheet("QWidget {\n"
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
        self.sssButton_def.setCheckable(True)

        self.gridLayout_3.addWidget(self.sssButton_def, 3, 0, 1, 1)

        self.displacementButton_def = QPushButton(self.gridLayoutWidget_3)
        self.buttonGroup_def.addButton(self.displacementButton_def)
        self.displacementButton_def.setObjectName("displacementButton_def")
        self.displacementButton_def.setMinimumSize(QSize(71, 20))
        self.displacementButton_def.setCursor(QCursor(Qt.PointingHandCursor))
        self.displacementButton_def.setStyleSheet("QWidget {\n"
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
        self.displacementButton_def.setCheckable(True)

        self.gridLayout_3.addWidget(self.displacementButton_def, 1, 1, 1, 1)

        self.bumpButton_def = QPushButton(self.gridLayoutWidget_3)
        self.buttonGroup_def.addButton(self.bumpButton_def)
        self.bumpButton_def.setObjectName("bumpButton_def")
        self.bumpButton_def.setMinimumSize(QSize(71, 20))
        self.bumpButton_def.setCursor(QCursor(Qt.PointingHandCursor))
        self.bumpButton_def.setStyleSheet("QWidget {\n"
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
        self.bumpButton_def.setCheckable(True)

        self.gridLayout_3.addWidget(self.bumpButton_def, 3, 1, 1, 1)

        self.assign_to_selected_default = QPushButton(self.gridLayoutWidget_3)
        self.assign_to_selected_default.setObjectName("assign_to_selected_default")
        self.assign_to_selected_default.setMinimumSize(QSize(0, 20))
        self.assign_to_selected_default.setStyleSheet("QWidget {\n"
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
        self.assign_to_selected_default.setCheckable(True)

        self.gridLayout_3.addWidget(self.assign_to_selected_default, 4, 0, 1, 1)

        self.udim_default = QPushButton(self.gridLayoutWidget_3)
        self.udim_default.setObjectName("udim_default")
        self.udim_default.setMinimumSize(QSize(0, 20))
        self.udim_default.setStyleSheet("QWidget {\n"
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
        self.udim_default.setCheckable(True)

        self.gridLayout_3.addWidget(self.udim_default, 4, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 0, 181, 106))
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 20, 161, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.previewButOff = QPushButton(self.horizontalLayoutWidget_3)
        self.previewButOff.setObjectName("previewButOff")
        self.previewButOff.setEnabled(False)
        self.previewButOff.setMinimumSize(QSize(25, 20))
        self.previewButOff.setMaximumSize(QSize(75, 20))
        self.previewButOff.setStyleSheet("QWidget {\n"
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

        self.horizontalLayout_2.addWidget(self.previewButOff)

        self.previewButOn = QPushButton(self.horizontalLayoutWidget_3)
        self.previewButOn.setObjectName("previewButOn")
        self.previewButOn.setEnabled(False)
        self.previewButOn.setMinimumSize(QSize(25, 20))
        self.previewButOn.setMaximumSize(QSize(75, 20))
        self.previewButOn.setStyleSheet("QWidget {\n"
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
"QWidget:checked{\n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.previewButOn.setCheckable(True)
        self.previewButOn.setChecked(True)

        self.horizontalLayout_2.addWidget(self.previewButOn)

        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 48, 161, 52))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.colorBut2 = QPushButton(self.gridLayoutWidget)
        self.buttonColorGroup = QButtonGroup(MainWindow)
        self.buttonColorGroup.setObjectName("buttonColorGroup")
        self.buttonColorGroup.setExclusive(True)
        self.buttonColorGroup.addButton(self.colorBut2)
        self.colorBut2.setObjectName("colorBut2")
        self.colorBut2.setEnabled(True)
        self.colorBut2.setMinimumSize(QSize(21, 21))
        self.colorBut2.setMaximumSize(QSize(21, 21))
        self.colorBut2.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorBut2.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgb(255, 150, 0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"                                          \n"
"QWidget:hover{    \n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"QWidget:checked{\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"\n"
"\n"
"")
        self.colorBut2.setCheckable(True)

        self.gridLayout.addWidget(self.colorBut2, 0, 2, 1, 1)

        self.colorBut4 = QPushButton(self.gridLayoutWidget)
        self.buttonColorGroup.addButton(self.colorBut4)
        self.colorBut4.setObjectName("colorBut4")
        self.colorBut4.setEnabled(True)
        self.colorBut4.setMinimumSize(QSize(21, 21))
        self.colorBut4.setMaximumSize(QSize(21, 21))
        self.colorBut4.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorBut4.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgb(85, 255, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"                                          \n"
"QWidget:hover{    \n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"QWidget:checked{\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.colorBut4.setCheckable(True)

        self.gridLayout.addWidget(self.colorBut4, 1, 1, 1, 1)

        self.colorBut1_2 = QPushButton(self.gridLayoutWidget)
        self.buttonColorGroup.addButton(self.colorBut1_2)
        self.colorBut1_2.setObjectName("colorBut1_2")
        self.colorBut1_2.setEnabled(True)
        self.colorBut1_2.setMinimumSize(QSize(21, 21))
        self.colorBut1_2.setMaximumSize(QSize(21, 21))
        self.colorBut1_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorBut1_2.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"                                          \n"
"QWidget:hover{    \n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"QWidget:checked{\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.colorBut1_2.setCheckable(True)

        self.gridLayout.addWidget(self.colorBut1_2, 0, 0, 1, 1)

        self.colorBut1_3 = QPushButton(self.gridLayoutWidget)
        self.buttonColorGroup.addButton(self.colorBut1_3)
        self.colorBut1_3.setObjectName("colorBut1_3")
        self.colorBut1_3.setEnabled(True)
        self.colorBut1_3.setMinimumSize(QSize(21, 21))
        self.colorBut1_3.setMaximumSize(QSize(21, 21))
        self.colorBut1_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorBut1_3.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"                                          \n"
"QWidget:hover{    \n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"QWidget:checked{\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.colorBut1_3.setCheckable(True)

        self.gridLayout.addWidget(self.colorBut1_3, 1, 0, 1, 1)

        self.colorBut3 = QPushButton(self.gridLayoutWidget)
        self.buttonColorGroup.addButton(self.colorBut3)
        self.colorBut3.setObjectName("colorBut3")
        self.colorBut3.setEnabled(True)
        self.colorBut3.setMinimumSize(QSize(21, 21))
        self.colorBut3.setMaximumSize(QSize(21, 21))
        self.colorBut3.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorBut3.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgb(135, 225, 0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"                                          \n"
"QWidget:hover{    \n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"QWidget:checked{\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);}\n"
"")
        self.colorBut3.setCheckable(True)

        self.gridLayout.addWidget(self.colorBut3, 0, 3, 1, 1)

        self.colorBut1 = QPushButton(self.gridLayoutWidget)
        self.buttonColorGroup.addButton(self.colorBut1)
        self.colorBut1.setObjectName("colorBut1")
        self.colorBut1.setEnabled(True)
        self.colorBut1.setMinimumSize(QSize(21, 21))
        self.colorBut1.setMaximumSize(QSize(21, 21))
        self.colorBut1.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorBut1.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgb(255, 80, 0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"                                          \n"
"QWidget:hover{    \n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"QWidget:checked{\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.colorBut1.setCheckable(True)

        self.gridLayout.addWidget(self.colorBut1, 0, 1, 1, 1)

        self.colorBut5 = QPushButton(self.gridLayoutWidget)
        self.buttonColorGroup.addButton(self.colorBut5)
        self.colorBut5.setObjectName("colorBut5")
        self.colorBut5.setEnabled(True)
        self.colorBut5.setMinimumSize(QSize(21, 21))
        self.colorBut5.setMaximumSize(QSize(21, 21))
        self.colorBut5.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorBut5.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgb(140, 100, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"                                          \n"
"QWidget:hover{    \n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"QWidget:checked{\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.colorBut5.setCheckable(True)

        self.gridLayout.addWidget(self.colorBut5, 1, 2, 1, 1)

        self.colorBut6 = QPushButton(self.gridLayoutWidget)
        self.buttonColorGroup.addButton(self.colorBut6)
        self.colorBut6.setObjectName("colorBut6")
        self.colorBut6.setEnabled(True)
        self.colorBut6.setMinimumSize(QSize(21, 21))
        self.colorBut6.setMaximumSize(QSize(21, 21))
        self.colorBut6.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorBut6.setStyleSheet("QWidget {\n"
"color: white;\n"
"background-color: rgb(255, 0, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:5px;\n"
"border-color: rgb(140, 140, 140);}\n"
"\n"
"QWidget:hover{\n"
"border-width:1px;\n"
"border-color: rgb(255, 255, 255);}\n"
"\n"
"QWidget:checked{\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);}\n"
"")
        self.colorBut6.setCheckable(True)

        self.gridLayout.addWidget(self.colorBut6, 1, 3, 1, 1)

        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setGeometry(QRect(10, 272, 181, 67))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget_5 = QWidget(self.groupBox)
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 20, 160, 41))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.comboBox_secs = QComboBox(self.gridLayoutWidget_5)
        self.comboBox_secs.addItem("")
        self.comboBox_secs.addItem("")
        self.comboBox_secs.addItem("")
        self.comboBox_secs.addItem("")
        self.comboBox_secs.addItem("")
        self.comboBox_secs.setObjectName("comboBox_secs")
        self.comboBox_secs.setMinimumSize(QSize(40, 20))
        self.comboBox_secs.setMaximumSize(QSize(40, 20))
        self.comboBox_secs.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_secs.setStyleSheet("")
        self.comboBox_secs.setEditable(False)
        self.comboBox_secs.setMaxVisibleItems(5)
        self.comboBox_secs.setMaxCount(5)
        self.comboBox_secs.setFrame(True)

        self.gridLayout_13.addWidget(self.comboBox_secs, 1, 2, 1, 1)

        self.comboBox_hours = QComboBox(self.gridLayoutWidget_5)
        self.comboBox_hours.addItem("")
        self.comboBox_hours.addItem("")
        self.comboBox_hours.addItem("")
        self.comboBox_hours.addItem("")
        self.comboBox_hours.addItem("")
        self.comboBox_hours.addItem("")
        self.comboBox_hours.setObjectName("comboBox_hours")
        self.comboBox_hours.setMinimumSize(QSize(40, 20))
        self.comboBox_hours.setMaximumSize(QSize(40, 20))
        self.comboBox_hours.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_hours.setStyleSheet("")
        self.comboBox_hours.setEditable(False)
        self.comboBox_hours.setMaxVisibleItems(6)
        self.comboBox_hours.setMaxCount(6)
        self.comboBox_hours.setFrame(True)

        self.gridLayout_13.addWidget(self.comboBox_hours, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_5)
        self.label_9.setObjectName("label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_9, 0, 1, 1, 1)

        self.comboBox_mins = QComboBox(self.gridLayoutWidget_5)
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.addItem("")
        self.comboBox_mins.setObjectName("comboBox_mins")
        self.comboBox_mins.setMinimumSize(QSize(40, 20))
        self.comboBox_mins.setMaximumSize(QSize(40, 20))
        self.comboBox_mins.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_mins.setStyleSheet("")
        self.comboBox_mins.setEditable(False)
        self.comboBox_mins.setMaxVisibleItems(5)
        self.comboBox_mins.setMaxCount(61)
        self.comboBox_mins.setFrame(True)

        self.gridLayout_13.addWidget(self.comboBox_mins, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_5)
        self.label_8.setObjectName("label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_5)
        self.label_10.setObjectName("label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_10, 0, 2, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 361, 180, 26))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.save_settings = QPushButton(self.horizontalLayoutWidget_2)
        self.save_settings.setObjectName("save_settings")
        self.save_settings.setMinimumSize(QSize(0, 20))
        self.save_settings.setMaximumSize(QSize(16777215, 20))
        self.save_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_settings.setStyleSheet("QWidget {\n"
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

        self.horizontalLayout_19.addWidget(self.save_settings)

        self.reset_settings = QPushButton(self.horizontalLayoutWidget_2)
        self.reset_settings.setObjectName("reset_settings")
        self.reset_settings.setMinimumSize(QSize(0, 20))
        self.reset_settings.setMaximumSize(QSize(16777215, 20))
        self.reset_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_settings.setStyleSheet("QWidget {\n"
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

        self.horizontalLayout_19.addWidget(self.reset_settings)

        self.save_reminder_sound = QCheckBox(self.tab_3)
        self.save_reminder_sound.setObjectName("save_reminder_sound")
        self.save_reminder_sound.setGeometry(QRect(20, 342, 161, 17))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.version_label = QLabel(self.tab_2)
        self.version_label.setObjectName("version_label")
        self.version_label.setGeometry(QRect(10, 287, 191, 81))
        self.version_label.setStyleSheet("")
        self.version_label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(10, 258, 191, 21))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.widget1 = QWidget(self.tab_2)
        self.widget1.setObjectName("widget1")
        self.widget1.setGeometry(QRect(20, 19, 171, 221))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.readme_but = QPushButton(self.widget1)
        self.readme_but.setObjectName("readme_but")
        self.readme_but.setMinimumSize(QSize(71, 30))
        self.readme_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.readme_but.setStyleSheet("QWidget {\n"
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
        self.readme_but.setCheckable(True)

        self.verticalLayout.addWidget(self.readme_but)

        self.manual_but = QPushButton(self.widget1)
        self.manual_but.setObjectName("manual_but")
        self.manual_but.setMinimumSize(QSize(71, 30))
        self.manual_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.manual_but.setStyleSheet("QWidget {\n"
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
        self.manual_but.setCheckable(True)

        self.verticalLayout.addWidget(self.manual_but)

        self.github_but = QPushButton(self.widget1)
        self.github_but.setObjectName("github_but")
        self.github_but.setMinimumSize(QSize(71, 30))
        self.github_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.github_but.setStyleSheet("QWidget {\n"
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
        self.github_but.setCheckable(True)

        self.verticalLayout.addWidget(self.github_but)

        self.gumroad_but = QPushButton(self.widget1)
        self.gumroad_but.setObjectName("gumroad_but")
        self.gumroad_but.setMinimumSize(QSize(71, 30))
        self.gumroad_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.gumroad_but.setStyleSheet("QWidget {\n"
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
        self.gumroad_but.setCheckable(True)

        self.verticalLayout.addWidget(self.gumroad_but)

        self.contactme_but = QPushButton(self.widget1)
        self.contactme_but.setObjectName("contactme_but")
        self.contactme_but.setMinimumSize(QSize(71, 30))
        self.contactme_but.setCursor(QCursor(Qt.PointingHandCursor))
        self.contactme_but.setStyleSheet("QWidget {\n"
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
        self.contactme_but.setCheckable(True)

        self.verticalLayout.addWidget(self.contactme_but)

        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(6, 403, 131, 53))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lastSave = QLabel(self.gridLayoutWidget_4)
        self.lastSave.setObjectName("lastSave")
        self.lastSave.setScaledContents(False)
        self.lastSave.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.lastSave, 2, 3, 1, 1)

        self.textureFileCountLabel = QLabel(self.gridLayoutWidget_4)
        self.textureFileCountLabel.setObjectName("textureFileCountLabel")
        self.textureFileCountLabel.setEnabled(True)

        self.gridLayout_5.addWidget(self.textureFileCountLabel, 1, 1, 1, 1)

        self.shaderCountLabel = QLabel(self.gridLayoutWidget_4)
        self.shaderCountLabel.setObjectName("shaderCountLabel")
        self.shaderCountLabel.setEnabled(True)

        self.gridLayout_5.addWidget(self.shaderCountLabel, 0, 1, 1, 1)

        self.shaderCount = QLabel(self.gridLayoutWidget_4)
        self.shaderCount.setObjectName("shaderCount")
        self.shaderCount.setEnabled(True)
        self.shaderCount.setScaledContents(False)
        self.shaderCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.shaderCount, 0, 3, 1, 1)

        self.lastSaveLabel = QLabel(self.gridLayoutWidget_4)
        self.lastSaveLabel.setObjectName("lastSaveLabel")

        self.gridLayout_5.addWidget(self.lastSaveLabel, 2, 1, 1, 1)

        self.textureFileCount = QLabel(self.gridLayoutWidget_4)
        self.textureFileCount.setObjectName("textureFileCount")
        self.textureFileCount.setEnabled(True)
        self.textureFileCount.setScaledContents(False)
        self.textureFileCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.textureFileCount, 1, 3, 1, 1)

        self.textureFileCountColon = QLabel(self.gridLayoutWidget_4)
        self.textureFileCountColon.setObjectName("textureFileCountColon")
        self.textureFileCountColon.setEnabled(True)
        self.textureFileCountColon.setMinimumSize(QSize(2, 0))
        self.textureFileCountColon.setMaximumSize(QSize(2, 16777215))

        self.gridLayout_5.addWidget(self.textureFileCountColon, 1, 2, 1, 1)

        self.lastSaveColon = QLabel(self.gridLayoutWidget_4)
        self.lastSaveColon.setObjectName("lastSaveColon")
        self.lastSaveColon.setMinimumSize(QSize(2, 0))
        self.lastSaveColon.setMaximumSize(QSize(2, 16777215))

        self.gridLayout_5.addWidget(self.lastSaveColon, 2, 2, 1, 1)

        self.shaderCountColon = QLabel(self.gridLayoutWidget_4)
        self.shaderCountColon.setObjectName("shaderCountColon")
        self.shaderCountColon.setEnabled(True)
        self.shaderCountColon.setMinimumSize(QSize(2, 0))
        self.shaderCountColon.setMaximumSize(QSize(2, 16777215))

        self.gridLayout_5.addWidget(self.shaderCountColon, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 216, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox_secs.setCurrentIndex(0)
        self.comboBox_hours.setCurrentIndex(0)
        self.comboBox_mins.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Shading Kit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Shader Name", None))
#if QT_CONFIG(tooltip)
        self.selectAll.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.selectAll.setStatusTip(QCoreApplication.translate("MainWindow", "LeftClick : Select All Textures   |   RightClick: Select All Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.selectAll.setText("")
#if QT_CONFIG(statustip)
        self.expand_Utils.setStatusTip(QCoreApplication.translate("MainWindow", "Advanced mode", None))
#endif // QT_CONFIG(statustip)
        self.expand_Utils.setText("")
#if QT_CONFIG(statustip)
        self.deselectAll.setStatusTip(QCoreApplication.translate("MainWindow", "LeftClick : Deselect All Textures   |   RightClick: Deselect All Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.deselectAll.setText("")
        self.selectDirectory.setText("")
        self.use_dir.setText(QCoreApplication.translate("MainWindow", "Use Directory", None))
        self.udim.setText(QCoreApplication.translate("MainWindow", "UDIM", None))
        self.assign_to_viewport.setText(QCoreApplication.translate("MainWindow", "Assign Sel.", None))
        self.createShader.setText(QCoreApplication.translate("MainWindow", "Create", None))
        self.deleteShader.setText(QCoreApplication.translate("MainWindow", "Delete", None))
#if QT_CONFIG(statustip)
        self.bumpButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.bumpButton.setText(QCoreApplication.translate("MainWindow", "Bump", None))
#if QT_CONFIG(statustip)
        self.baseColorButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.baseColorButton.setText(QCoreApplication.translate("MainWindow", "Base Color", None))
#if QT_CONFIG(statustip)
        self.specularButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.specularButton.setText(QCoreApplication.translate("MainWindow", "Specular R.", None))
#if QT_CONFIG(statustip)
        self.coatButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.coatButton.setText(QCoreApplication.translate("MainWindow", "Coat R.", None))
        self.tree_but_2.setText("")
        self.baseColor_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.baseColor_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
        self.baseColor_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
        self.tree_but_5.setText("")
        self.coat_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
        self.coat_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.coat_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
#if QT_CONFIG(statustip)
        self.displacementButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.displacementButton.setText(QCoreApplication.translate("MainWindow", "Displace", None))
        self.tree_but_7.setText("")
        self.sss_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
        self.sss_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.sss_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
        self.tree_but_4.setText("")
        self.disp_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
        self.disp_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.disp_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
        self.tree_but_8.setText("")
        self.bump_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.bump_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
        self.bump_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
#if QT_CONFIG(statustip)
        self.sssButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.sssButton.setText(QCoreApplication.translate("MainWindow", "SSS", None))
        self.tree_but_6.setText("")
        self.normal_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
        self.normal_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.normal_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
        self.tree_but_3.setText("")
        self.metal_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
        self.metal_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.metal_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
#if QT_CONFIG(statustip)
        self.normalButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.normalButton.setText(QCoreApplication.translate("MainWindow", "Normal", None))
#if QT_CONFIG(statustip)
        self.metalnessButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.metalnessButton.setText(QCoreApplication.translate("MainWindow", "Metalness", None))
        self.tree_but.setText("")
        self.spec_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.spec_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
        self.spec_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
#if QT_CONFIG(statustip)
        self.opacityButton.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.opacityButton.setText(QCoreApplication.translate("MainWindow", "Opacity", None))
        self.tree_but_9.setText("")
        self.opacity_aiRange.setText(QCoreApplication.translate("MainWindow", "RG", None))
        self.opacity_aiColorCorrect.setText(QCoreApplication.translate("MainWindow", "CC", None))
        self.opacity_aiClamp.setText(QCoreApplication.translate("MainWindow", "CL", None))
#if QT_CONFIG(statustip)
        self.create_AOVs.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.create_AOVs.setText(QCoreApplication.translate("MainWindow", "Create", None))
#if QT_CONFIG(statustip)
        self.delete_AOVs.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.delete_AOVs.setText(QCoreApplication.translate("MainWindow", "Delete", None))
#if QT_CONFIG(statustip)
        self.metalnessButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.metalnessButton_AOV.setText(QCoreApplication.translate("MainWindow", "Metalness", None))
#if QT_CONFIG(statustip)
        self.normalButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.normalButton_AOV.setText(QCoreApplication.translate("MainWindow", "Normal", None))
#if QT_CONFIG(statustip)
        self.coatButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.coatButton_AOV.setText(QCoreApplication.translate("MainWindow", "Coat R.", None))
#if QT_CONFIG(statustip)
        self.bumpButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.bumpButton_AOV.setText(QCoreApplication.translate("MainWindow", "Bump", None))
#if QT_CONFIG(statustip)
        self.sssButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.sssButton_AOV.setText(QCoreApplication.translate("MainWindow", "SSS", None))
#if QT_CONFIG(statustip)
        self.displacementButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.displacementButton_AOV.setText(QCoreApplication.translate("MainWindow", "Displace", None))
#if QT_CONFIG(statustip)
        self.opacityButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.opacityButton_AOV.setText(QCoreApplication.translate("MainWindow", "Opacity", None))
#if QT_CONFIG(statustip)
        self.specularButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.specularButton_AOV.setText(QCoreApplication.translate("MainWindow", "Specular R.", None))
#if QT_CONFIG(statustip)
        self.baseColorButton_AOV.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.baseColorButton_AOV.setText(QCoreApplication.translate("MainWindow", "Base Color", None))
#if QT_CONFIG(statustip)
        self.sel_all_aovs.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.sel_all_aovs.setText(QCoreApplication.translate("MainWindow", "All", None))
#if QT_CONFIG(statustip)
        self.desel_all_aovs.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.desel_all_aovs.setText(QCoreApplication.translate("MainWindow", "None", None))
#if QT_CONFIG(statustip)
        self.match_sel_aovs.setStatusTip(QCoreApplication.translate("MainWindow", "RightClick: Select Utility nodes", None))
#endif // QT_CONFIG(statustip)
        self.match_sel_aovs.setText(QCoreApplication.translate("MainWindow", "Match", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", "Texture AOVs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", "Shading", None))
        self.default_textures_groupBox.setTitle(QCoreApplication.translate("MainWindow", "Default Values", None))
        self.coatButton_def.setText(QCoreApplication.translate("MainWindow", "Coat R.", None))
        self.normalButton_def.setText(QCoreApplication.translate("MainWindow", "Normal", None))
        self.specularButton_def.setText(QCoreApplication.translate("MainWindow", "Specular R.", None))
        self.baseColorButton_def.setText(QCoreApplication.translate("MainWindow", "Base Color", None))
        self.metalnessButton_def.setText(QCoreApplication.translate("MainWindow", "Metalness", None))
        self.sssButton_def.setText(QCoreApplication.translate("MainWindow", "SSS", None))
        self.displacementButton_def.setText(QCoreApplication.translate("MainWindow", "Displace", None))
        self.bumpButton_def.setText(QCoreApplication.translate("MainWindow", "Bump", None))
        self.assign_to_selected_default.setText(QCoreApplication.translate("MainWindow", "Assign sel.", None))
        self.udim_default.setText(QCoreApplication.translate("MainWindow", "UDIM", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", "Button Outline Color", None))
        self.previewButOff.setText(QCoreApplication.translate("MainWindow", "Off", None))
        self.previewButOn.setText(QCoreApplication.translate("MainWindow", "On", None))
        self.colorBut2.setText("")
        self.colorBut4.setText("")
        self.colorBut1_2.setText("")
        self.colorBut1_3.setText("")
        self.colorBut3.setText("")
        self.colorBut1.setText("")
        self.colorBut5.setText("")
        self.colorBut6.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", "Save Reminder", None))
        self.comboBox_secs.setItemText(0, QCoreApplication.translate("MainWindow", "00", None))
        self.comboBox_secs.setItemText(1, QCoreApplication.translate("MainWindow", "15", None))
        self.comboBox_secs.setItemText(2, QCoreApplication.translate("MainWindow", "30", None))
        self.comboBox_secs.setItemText(3, QCoreApplication.translate("MainWindow", "45", None))
        self.comboBox_secs.setItemText(4, QCoreApplication.translate("MainWindow", "60", None))

        self.comboBox_hours.setItemText(0, QCoreApplication.translate("MainWindow", "00", None))
        self.comboBox_hours.setItemText(1, QCoreApplication.translate("MainWindow", "01", None))
        self.comboBox_hours.setItemText(2, QCoreApplication.translate("MainWindow", "02", None))
        self.comboBox_hours.setItemText(3, QCoreApplication.translate("MainWindow", "03", None))
        self.comboBox_hours.setItemText(4, QCoreApplication.translate("MainWindow", "04", None))
        self.comboBox_hours.setItemText(5, QCoreApplication.translate("MainWindow", "05", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", "Minutes", None))
        self.comboBox_mins.setItemText(0, QCoreApplication.translate("MainWindow", "00", None))
        self.comboBox_mins.setItemText(1, QCoreApplication.translate("MainWindow", "01", None))
        self.comboBox_mins.setItemText(2, QCoreApplication.translate("MainWindow", "02", None))
        self.comboBox_mins.setItemText(3, QCoreApplication.translate("MainWindow", "03", None))
        self.comboBox_mins.setItemText(4, QCoreApplication.translate("MainWindow", "04", None))
        self.comboBox_mins.setItemText(5, QCoreApplication.translate("MainWindow", "05", None))
        self.comboBox_mins.setItemText(6, QCoreApplication.translate("MainWindow", "06", None))
        self.comboBox_mins.setItemText(7, QCoreApplication.translate("MainWindow", "07", None))
        self.comboBox_mins.setItemText(8, QCoreApplication.translate("MainWindow", "08", None))
        self.comboBox_mins.setItemText(9, QCoreApplication.translate("MainWindow", "09", None))
        self.comboBox_mins.setItemText(10, QCoreApplication.translate("MainWindow", "10", None))
        self.comboBox_mins.setItemText(11, QCoreApplication.translate("MainWindow", "11", None))
        self.comboBox_mins.setItemText(12, QCoreApplication.translate("MainWindow", "12", None))
        self.comboBox_mins.setItemText(13, QCoreApplication.translate("MainWindow", "13", None))
        self.comboBox_mins.setItemText(14, QCoreApplication.translate("MainWindow", "14", None))
        self.comboBox_mins.setItemText(15, QCoreApplication.translate("MainWindow", "15", None))
        self.comboBox_mins.setItemText(16, QCoreApplication.translate("MainWindow", "16", None))
        self.comboBox_mins.setItemText(17, QCoreApplication.translate("MainWindow", "17", None))
        self.comboBox_mins.setItemText(18, QCoreApplication.translate("MainWindow", "18", None))
        self.comboBox_mins.setItemText(19, QCoreApplication.translate("MainWindow", "19", None))
        self.comboBox_mins.setItemText(20, QCoreApplication.translate("MainWindow", "20", None))
        self.comboBox_mins.setItemText(21, QCoreApplication.translate("MainWindow", "21", None))
        self.comboBox_mins.setItemText(22, QCoreApplication.translate("MainWindow", "22", None))
        self.comboBox_mins.setItemText(23, QCoreApplication.translate("MainWindow", "23", None))
        self.comboBox_mins.setItemText(24, QCoreApplication.translate("MainWindow", "24", None))
        self.comboBox_mins.setItemText(25, QCoreApplication.translate("MainWindow", "25", None))
        self.comboBox_mins.setItemText(26, QCoreApplication.translate("MainWindow", "26", None))
        self.comboBox_mins.setItemText(27, QCoreApplication.translate("MainWindow", "27", None))
        self.comboBox_mins.setItemText(28, QCoreApplication.translate("MainWindow", "28", None))
        self.comboBox_mins.setItemText(29, QCoreApplication.translate("MainWindow", "29", None))
        self.comboBox_mins.setItemText(30, QCoreApplication.translate("MainWindow", "30", None))
        self.comboBox_mins.setItemText(31, QCoreApplication.translate("MainWindow", "31", None))
        self.comboBox_mins.setItemText(32, QCoreApplication.translate("MainWindow", "32", None))
        self.comboBox_mins.setItemText(33, QCoreApplication.translate("MainWindow", "33", None))
        self.comboBox_mins.setItemText(34, QCoreApplication.translate("MainWindow", "34", None))
        self.comboBox_mins.setItemText(35, QCoreApplication.translate("MainWindow", "35", None))
        self.comboBox_mins.setItemText(36, QCoreApplication.translate("MainWindow", "36", None))
        self.comboBox_mins.setItemText(37, QCoreApplication.translate("MainWindow", "37", None))
        self.comboBox_mins.setItemText(38, QCoreApplication.translate("MainWindow", "38", None))
        self.comboBox_mins.setItemText(39, QCoreApplication.translate("MainWindow", "39", None))
        self.comboBox_mins.setItemText(40, QCoreApplication.translate("MainWindow", "40", None))
        self.comboBox_mins.setItemText(41, QCoreApplication.translate("MainWindow", "41", None))
        self.comboBox_mins.setItemText(42, QCoreApplication.translate("MainWindow", "42", None))
        self.comboBox_mins.setItemText(43, QCoreApplication.translate("MainWindow", "43", None))
        self.comboBox_mins.setItemText(44, QCoreApplication.translate("MainWindow", "44", None))
        self.comboBox_mins.setItemText(45, QCoreApplication.translate("MainWindow", "45", None))
        self.comboBox_mins.setItemText(46, QCoreApplication.translate("MainWindow", "46", None))
        self.comboBox_mins.setItemText(47, QCoreApplication.translate("MainWindow", "47", None))
        self.comboBox_mins.setItemText(48, QCoreApplication.translate("MainWindow", "48", None))
        self.comboBox_mins.setItemText(49, QCoreApplication.translate("MainWindow", "49", None))
        self.comboBox_mins.setItemText(50, QCoreApplication.translate("MainWindow", "50", None))
        self.comboBox_mins.setItemText(51, QCoreApplication.translate("MainWindow", "51", None))
        self.comboBox_mins.setItemText(52, QCoreApplication.translate("MainWindow", "52", None))
        self.comboBox_mins.setItemText(53, QCoreApplication.translate("MainWindow", "53", None))
        self.comboBox_mins.setItemText(54, QCoreApplication.translate("MainWindow", "54", None))
        self.comboBox_mins.setItemText(55, QCoreApplication.translate("MainWindow", "55", None))
        self.comboBox_mins.setItemText(56, QCoreApplication.translate("MainWindow", "56", None))
        self.comboBox_mins.setItemText(57, QCoreApplication.translate("MainWindow", "57", None))
        self.comboBox_mins.setItemText(58, QCoreApplication.translate("MainWindow", "58", None))
        self.comboBox_mins.setItemText(59, QCoreApplication.translate("MainWindow", "59", None))
        self.comboBox_mins.setItemText(60, QCoreApplication.translate("MainWindow", "60", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", "Hours", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", "Seconds", None))
        self.save_settings.setText(QCoreApplication.translate("MainWindow", "Save settings", None))
        self.reset_settings.setText(QCoreApplication.translate("MainWindow", "Reset settings", None))
        self.save_reminder_sound.setText(QCoreApplication.translate("MainWindow", "Save Reminder Sound", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", "Settings", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", "TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Current version", None))
        self.readme_but.setText(QCoreApplication.translate("MainWindow", "README", None))
        self.manual_but.setText(QCoreApplication.translate("MainWindow", "MANUAL", None))
        self.github_but.setText(QCoreApplication.translate("MainWindow", "GitHub", None))
        self.gumroad_but.setText(QCoreApplication.translate("MainWindow", "Gumroad", None))
#if QT_CONFIG(tooltip)
        self.contactme_but.setToolTip(QCoreApplication.translate("MainWindow", "efthymisb.vfx@gmail.com", None))
#endif // QT_CONFIG(tooltip)
        self.contactme_but.setText(QCoreApplication.translate("MainWindow", "Contact me", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", "About", None))
        self.lastSave.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.textureFileCountLabel.setText(QCoreApplication.translate("MainWindow", "File Textures", None))
        self.shaderCountLabel.setText(QCoreApplication.translate("MainWindow", "aiSS Shaders", None))
        self.shaderCount.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.lastSaveLabel.setText(QCoreApplication.translate("MainWindow", "Since Last Save", None))
        self.textureFileCount.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.textureFileCountColon.setText(QCoreApplication.translate("MainWindow", ":", None))
        self.lastSaveColon.setText(QCoreApplication.translate("MainWindow", ":", None))
        self.shaderCountColon.setText(QCoreApplication.translate("MainWindow", ":", None))
    # retranslateUi

