"""
Author: Efthymis B.
Last Modified: 11/12/2021

Python 3.7 (Maya 2022+)
Shading-Kit for Maya
"""

from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from ShadingKit_python3.UIs import mainUI, shader_list, file_formats
from PySide2 import QtCore, QtGui, QtWidgets
from functools import partial
from maya import OpenMaya
import maya.OpenMayaUI as omui
import mtoa.utils as mutils
import maya.cmds as cmds
import mtoa.aovs as aovs
import maya.mel as mel
import shiboken2
import importlib
import json
import os

if os.name == 'nt':
    import winsound

try:
    importlib.reload(file_formats)
except NameError:
    pass

try:
    importlib.reload(mainUI)
except NameError:
    pass

try:
    importlib.reload(shader_list)
except NameError:
    pass


# GET SCRIPT'S PATH
script_folder = os.path.dirname(os.path.abspath(__file__))
user_settings_path = os.path.join(script_folder, 'user_Settings.json')

def get_main_window():
    pointer = omui.MQtUtil.mainWindow()
    if pointer is not None:
        return shiboken2.wrapInstance(int(pointer), QtWidgets.QWidget)

class ShaderList(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ShaderList, self).__init__(parent)

        self.ui_sh_list = shader_list.Ui_shader_list_win()
        self.ui_sh_list.setupUi(self)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        self.ui_sh_list.cancel_but.clicked.connect(self.close_win)
        self.ui_sh_list.ok_but.clicked.connect(self.selected_item)

        shaders = cmds.ls(et='aiStandardSurface')

        if shaders:
            for shader in shaders:
                item = QtWidgets.QListWidgetItem(shader)
                self.ui_sh_list.listWidget.addItem(item)
        else:
            item = QtWidgets.QListWidgetItem("No aiSS Shaders found!")
            self.ui_sh_list.listWidget.addItem(item)
            self.ui_sh_list.listWidget.setDisabled(True)
            self.ui_sh_list.ok_but.setDisabled(True)

    def selected_item(self):
        sel_items = self.ui_sh_list.listWidget.selectedItems()
        for item in sel_items:
            if cmds.hyperShade(lun=item.text() + 'SG') is not None:
                node_list = cmds.hyperShade(lun=item.text() + 'SG')
                node_list.append(item.text() + 'SG')
            elif cmds.hyperShade(lun=item.text()) is not None:
                node_list = cmds.hyperShade(lun=item.text())
                node_list.append(item.text())

            for node in node_list:
                if cmds.nodeType(node) == 'colorManagementGlobals' or cmds.nodeType(node) == 'mesh':
                    pass
                else:
                    cmds.delete(node)
        self.close()

    def close_win(self):
        self.close()


class Second(QtWidgets.QMainWindow):
    def __init__(self, parent=None):

        with open(user_settings_path, 'r') as file1:
            old_settings = json.load(file1)

        super(Second, self).__init__(parent)
        self.ui_file_formats = file_formats.Ui_file_formats()
        self.ui_file_formats.setupUi(self)

        for but in self.ui_file_formats.file_formats_Grp.buttons():
            if old_settings["start_up_settings"]["file_formats"][but.objectName()[:-4]]:
                but.setChecked(True)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)

        self.ui_file_formats.cancel_but.clicked.connect(self.close_window)
        self.ui_file_formats.ok_but.clicked.connect(self.save_and_close)

    def close_window(self):
        self.close()

    def save_and_close(self):

        with open(user_settings_path, 'r') as file1:
            old_settings = json.load(file1)

        for but in self.ui_file_formats.file_formats_Grp.buttons():
            if but.isChecked():
                old_settings["start_up_settings"]["file_formats"][but.objectName()[:-4]] = True
            else:
                old_settings["start_up_settings"]["file_formats"][but.objectName()[:-4]] = False

        # Save and close user_Settings.json
        with open(user_settings_path, 'w') as file1:
            json.dump(old_settings, file1, indent=4, sort_keys=True)
        file1.close()

        self.close()


class MainWindow(MayaQWidgetDockableMixin, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        with open(user_settings_path, 'r') as file:
            settings = json.load(file)
        self.user_settings = settings["start_up_settings"]
        self.texture_pass_list = settings["texture_aliases"]
        self.default_but_color = self.user_settings["but_color"]

        self.ui = mainUI.Ui_MainWindow()
        self.ui.setupUi(self)

        # CREATE CALLBACK AFTER SAVE/LOAD/NEW SCENE
        self.save_scene_callBack = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterOpen, self.reset_save)
        self.save_scene_callBack = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterNew, self.reset_save)
        self.save_scene_callBack = OpenMaya.MSceneMessage.addCallback(OpenMaya.MSceneMessage.kAfterSave, self.reset_save)
        self.current_time = 0

        # CREATE TEXTURE-UTILS DICT
        self.util_grps = {
            self.ui.baseColorButton: self.ui.Utils_BC.buttons(),
            self.ui.specularButton: self.ui.Utils_Spec.buttons(),
            self.ui.metalnessButton: self.ui.Utils_Metal.buttons(),
            self.ui.displacementButton: self.ui.Utils_Disp.buttons(),
            self.ui.normalButton: self.ui.Utils_Normal.buttons(),
            self.ui.coatButton: self.ui.Utils_Coat.buttons(),
            self.ui.sssButton: self.ui.Utils_SSS.buttons(),
            self.ui.transmissionButton: self.ui.Utils_Trans.buttons(),
            self.ui.opacityButton: self.ui.Utils_Opacity.buttons()
        }
        # CREATE LIST WITH ALL THE UTILS CHECKBOXES
        self.all_util = self.ui.Utils_BC.buttons() + self.ui.Utils_Spec.buttons() + self.ui.Utils_Metal.buttons()\
                        + self.ui.Utils_Disp.buttons() + self.ui.Utils_Normal.buttons() + self.ui.Utils_Coat.buttons()\
                        + self.ui.Utils_SSS.buttons() + self.ui.Utils_Trans.buttons() + self.ui.Utils_Opacity.buttons()

        # CONNECT COMMAND ON BUTTONS (SHADING TAB)
        for but in self.ui.buttonGroup.buttons():
            but.clicked.connect(partial(self.change_but_color, but))
            but.installEventFilter(self)
            but.setChecked(self.user_settings[but.objectName()])
            self.change_but_color(but)
        for but_def in self.ui.buttonGroup_def.buttons():
            but_def.clicked.connect(partial(self.change_but_color, but_def))
            but_def.setChecked(self.user_settings[but_def.objectName()[:-4]])
            self.change_but_color(but_def)
        for but_dir in self.ui.udim_selected_dir_Grp.buttons():
            but_dir.clicked.connect(partial(self.change_but_color, but_dir))
            but_dir.setChecked(self.user_settings[but_dir.objectName()])
            self.change_but_color(but_dir)
        for but_aov in self.ui.AOV_buts.buttons():
            but_aov.clicked.connect(partial(self.change_but_color, but_aov))

        self.ui.udim_default.clicked.connect(partial(self.change_but_color, self.ui.udim_default))
        self.ui.udim_default.setChecked(self.user_settings['udim'])
        self.change_but_color(self.ui.udim_default)

        self.ui.assign_to_selected_default.clicked.connect(partial(self.change_but_color, self.ui.assign_to_selected_default))
        self.ui.assign_to_selected_default.setChecked(self.user_settings['assign_to_viewport'])
        self.change_but_color(self.ui.assign_to_selected_default)

        # COLOR BUTTONS (SETTINGS TAB)
        for color_but in self.ui.buttonColorGroup.buttons():
            color_but.clicked.connect(partial(self.changeDefaultColor, color_but))

        for tree_but in self.ui.tree_Buttons.buttons():
            tree_but.setIcon(QtGui.QIcon(os.path.join(script_folder, "icons", "util_tree.png")))
            tree_but.setIconSize(QtCore.QSize(10, 52))
            #tree_but.setVisible(False)

        # SET SAVE REMINDER
        save_values = self.user_settings['save_reminder'].split('.')
        self.ui.comboBox_hours.setCurrentText(save_values[0])
        self.ui.comboBox_mins.setCurrentText(save_values[1])
        self.ui.comboBox_secs.setCurrentText(save_values[2])
        self.ui.comboBox_hours.activated.connect(self.change_save_reminder)
        self.ui.comboBox_mins.activated.connect(self.change_save_reminder)
        self.ui.comboBox_secs.activated.connect(self.change_save_reminder)
        self.save_reminder = (int(save_values[0]) * 3600) + (int(save_values[1]) * 60) + int(save_values[2])

        self.ui.save_reminder_sound.setChecked(self.user_settings["save_sound"])

        # SET ICONS FOR SELECT/DESELECT ALL
        self.ui.selectAll.clicked.connect(self.select_all)
        self.ui.selectAll.setIcon(QtGui.QIcon(os.path.join(script_folder, "icons", "all.png")))
        self.ui.selectAll.setIconSize(QtCore.QSize(20, 20))
        self.ui.selectAll.installEventFilter(self)

        self.ui.deselectAll.clicked.connect(self.deselectAll)
        self.ui.deselectAll.setIcon(QtGui.QIcon(os.path.join(script_folder, "icons", "none.png")))
        self.ui.deselectAll.setIconSize(QtCore.QSize(20, 20))
        self.ui.deselectAll.installEventFilter(self)

        # CONNECT FUNCTION TO ADVANCED/SIMPLE BUTTON (SHADING TAB)
        self.ui.expand_Utils.clicked.connect(self.checkOnOff)
        self.ui.expand_Utils.setIcon(QtGui.QIcon(os.path.join(script_folder, "icons", "shrink.png")))
        self.ui.expand_Utils.setIconSize(QtCore.QSize(20, 20))

        # CONNECT FUNCTION TO SELECT DIRECTORY BUTTON & ASSIGN ICON (SHADING TAB)
        self.ui.selectDirectory.installEventFilter(self)
        self.ui.selectDirectory.clicked.connect(self.select_dir)
        self.ui.selectDirectory.setStyleSheet(u"QPushButton{"
                                                "qproperty-icon: url();"
                                                "border-style:none;"
                                                "qproperty-iconSize: 20px 20px;"
                                                "background-image: url(" + script_folder.replace("\\", "/") + "/icons/folder.png);"
                                                "background-repeat: no-repeat;}"
                                        
                                                "QPushButton:hover{"
                                                "border-style:none;"
                                                "background-image: url(" + script_folder.replace("\\", "/") + "/icons/folder_light.png);"
                                                "background-repeat: no-repeat;}"

                                                "QPushButton:pressed{"
                                                "border-style:none;"
                                                "background-image: url(" + script_folder.replace("\\", "/") + "/icons/folder_dark.png);"
                                                "background-repeat: no-repeat;}")

        # CREATE/DELETE SHADER BUTTONS
        self.ui.deleteShader.clicked.connect(self.delete_shader)
        self.ui.createShader.clicked.connect(self.create_shader)

        layout = self.ui.gridLayoutWidget_2
        layout.setGeometry(layout.x(), layout.y(), layout.width(), 220)

        # CHECK IF TEXTURE IS SELECTED AND ENABLE/DISABLE UTILS ACCORDINGLY
        for key in self.util_grps:
            for util in self.util_grps[key]:
                if key.isChecked():
                    util.setEnabled(True)
                    #util.setVisible(False)
                else:
                    util.setDisabled(True)
                    #util.setVisible(False)

        # CHANGE COLOR PREVIEW BUTTON STYLESHEET
        self.ui.previewButOn.setStyleSheet(u"QWidget {"
                                            "color: white;"
                                            "background-color: rgba(70, 70, 70);"
                                            "border-style:solid;"
                                            "border-width:1px;"
                                            "border-radius:5px;"
                                            "border-color: rgb(140, 140, 140);}"
                                            
                                            "QWidget:hover{    "
                                            "background-color: rgb(100, 100, 100);}"
                                            
                                            "QWidget:checked{"
                                            "border-width:1px;"
                                            "border-color: " + self.default_but_color + ";}")

        # CREATE TIMER FOR COUNTERS
        self.timer = QtCore.QTimer(self.ui.tabWidget)
        self.timer.timeout.connect(self.show_time)
        self.timer.start()
        self.timer.setInterval(1000)

        # CONNECT FUNCTIONS TO SAVE/RESET BUTTONS
        self.ui.save_settings.clicked.connect(self.save_settings)
        self.ui.reset_settings.clicked.connect(self.reset_settings)

        # CONNCET FUNCTIONS TO ALL/NONE/MATCH BUTTONS (AOVS)
        self.ui.sel_all_aovs.clicked.connect(self.sel_all_aovs)
        self.ui.desel_all_aovs.clicked.connect(self.desel_all_aovs)
        self.ui.match_sel_aovs.clicked.connect(self.match_aovs_sel)

        self.ui.create_AOVs.clicked.connect(partial(self.create_delete_aovs, True))
        self.ui.delete_AOVs.clicked.connect(partial(self.create_delete_aovs, False))

        # CREATE PROPERTY ANIMATION FOR SHADER_WIDGET
        self.animation = QtCore.QPropertyAnimation(self.ui.gridLayoutWidget_2, b'geometry')
        self.bot_layout_anim = QtCore.QPropertyAnimation(self.ui.createShaderWidget, b'geometry')

        self.aovFrameAnim = QtCore.QPropertyAnimation(self.ui.aov_frame, b'geometry')

        self.animation.setDuration(400)
        self.bot_layout_anim.setDuration(400)
        self.aovFrameAnim.setDuration(400)

        # HIDE shaderCount and textureFileCount
        self.ui.textureFileCount.setVisible(False)
        self.ui.textureFileCountColon.setVisible(False)
        self.ui.textureFileCountLabel.setVisible(False)
        self.ui.shaderCount.setVisible(False)
        self.ui.shaderCountColon.setVisible(False)
        self.ui.shaderCountLabel.setVisible(False)

    def test(self, *args):
        print('It works!')

    def helper_function(self, widget, color):
        widget.setStyleSheet(f"background-color: rgba({color.red()}, {color.green()}, {color.blue()}, {color.alpha()});"
                             f"border-style:none;")

    def select_dir(self):
        texture_path = cmds.fileDialog2(ds=2, fm=3, okc='Select', dir=cmds.workspace(q=True, rd=True) + 'sourceimages')
        '''options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        options |= QtWidgets.QFileDialog.ShowDirsOnly
        path = QtWidgets.QFileDialog.getExistingDirectory(options=options, dir=texture_path)'''
        self.ui.directoryPath.setText(texture_path[0])

    def delete_shader(self):
        shader_name = self.ui.shader_text.text()
        if shader_name.isspace() or not shader_name:
            sh_list = ShaderList(self)
            sh_list.show()
        else:
            if cmds.hyperShade(lun=shader_name + 'SG') is not None:
                node_list = cmds.hyperShade(lun=shader_name + 'SG')
                node_list.append(shader_name + 'SG')
            elif cmds.hyperShade(lun=shader_name) is not None:
                node_list = cmds.hyperShade(lun=shader_name)
                node_list.append(shader_name)

            for node in node_list:
                if cmds.nodeType(node) == 'colorManagementGlobals':
                    pass
                else:
                    cmds.delete(node)

            self.ui.shader_text.setText('')

    def save_settings(self):
        # Open user_Settings.json
        with open(user_settings_path, 'r') as file1:
            old_settings = json.load(file1)

        # Check if any color is selected and get its value
        selected = self.ui.buttonColorGroup.checkedButton()
        if selected is not None:
            new_color = selected.styleSheet().split('QWidget:hover')[0].split(';')[1].split(':')[1]
            old_settings["start_up_settings"]['but_color'] = new_color

        # Get h,m,s
        hours = self.ui.comboBox_hours.currentText()
        minutes = self.ui.comboBox_mins.currentText()
        seconds = self.ui.comboBox_secs.currentText()
        old_settings["start_up_settings"]['save_reminder'] = hours + "." + minutes + "." + seconds

        # Iterate through default texture buttons and check if selected
        for but in self.ui.buttonGroup_def.buttons():
            if but.isChecked():
                old_settings["start_up_settings"][but.objectName()[:-4]] = True
            else:
                old_settings["start_up_settings"][but.objectName()[:-4]] = False

        if self.ui.udim_default.isChecked():
            old_settings["start_up_settings"]['udim'] = True
        else:
            old_settings["start_up_settings"]['udim'] = False

        if self.ui.assign_to_selected_default.isChecked():
            old_settings["start_up_settings"]['assign_to_viewport'] = True
        else:
            old_settings["start_up_settings"]['assign_to_viewport'] = False

        if self.ui.save_reminder_sound.isChecked():
            old_settings["start_up_settings"]['save_sound'] = True
        else:
            old_settings["start_up_settings"]['save_sound'] = False

        # Save and close user_Settings.json
        with open(user_settings_path, 'w') as file1:
            json.dump(old_settings, file1, indent=4, sort_keys=True)
        file1.close()

        self.user_settings = old_settings["start_up_settings"]
        return self.user_settings

    def reset_settings(self):

        new_settings = {"start_up_settings": {
                            "assign_to_viewport": False,
                            "baseColorButton": False,
                            "but_color": " rgb(85, 255, 255)",
                            "coatButton": False,
                            "displacementButton": False,
                            "file_formats": {
                                "exr": True,
                                "jpeg": True,
                                "jpg": True,
                                "png": True,
                                "tga": True,
                                "tif": True
                            },
                            "metalnessButton": False,
                            "normalButton": False,
                            "opacityButton": False,
                            "save_reminder": "00.15.00",
                            "save_sound": False,
                            "specularButton": False,
                            "sssButton": False,
                            "transmissionButton": False,
                            "udim": False,
                            "use_dir": False
                        },
                        "texture_aliases": {
                            "Base Color": ["base_color", [ "basecolor", "diffuse", "albedo", "base_color", "base color"], ".outColor", ".baseColor"],
                            "Coat R.": [ "coat_roughness", [ "coat" ], ".outColorR", ".coatRoughness" ],
                            "Displace": [ "displacement", [ "height", "displace" ], ".outColorR", ".displacement" ],
                            "Metalness": [ "metalness", [ "metal", "metalness", "metallic" ], ".outColorR", ".metalness" ],
                            "Normal": [ "normal", [ "normal", "bump" ], ".outColorR", ".bumpValue" ],
                            "Opacity": [ "opacity", [ "opacity" ], ".outColor", ".opacity" ],
                            "SSS": [ "subsurface", [ "sss", "subsurface" ], ".outColor", ".subsurfaceColor" ],
                            "Specular R.": [ "spec_roughness", [ "spec", "roughness" ], ".outColorR", ".specularRoughness" ],
                            "Transmis.": [ "transmission", [ "transmission", "transmissionweight", "transmission_weight", "transmission weight" ], ".outColorR", ".transmission" ]
                        }
                    }

        # Save and close user_Settings.json
        with open(user_settings_path, 'w') as file1:
            json.dump(new_settings, file1, indent=4, sort_keys=True)
        file1.close()
        self.close()

    def change_save_reminder(self):
        hours = int(self.ui.comboBox_hours.currentText())
        minutes = int(self.ui.comboBox_mins.currentText())
        seconds = int(self.ui.comboBox_secs.currentText())

        self.save_reminder = (hours * 3600) + (minutes * 60) + seconds
        self.ui.lastSave.setStyleSheet(u"color: rgba(200, 200, 200);")
        return self.save_reminder

    def reset_save(self, arg):
        self.current_time = 0
        return self.current_time

    def show_time(self):
        shaders = cmds.ls(et='aiStandardSurface')
        txt_files = cmds.ls(et='file')

        self.current_time += 1
        hours, remainder = divmod(self.current_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        final_time = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        self.ui.shaderCount.setText(str(len(shaders)))
        self.ui.textureFileCount.setText(str(len(txt_files)))
        if hours == 0:
            self.ui.lastSave.setText(final_time[3:])
        else:
            self.ui.lastSave.setText(final_time)
        if self.current_time >= self.save_reminder:
            if (int(seconds) % 2) == 0:
                self.ui.lastSave.setStyleSheet(u"color: rgba(200, 0, 0);")
                if self.user_settings["save_sound"] and "winsound" in sys.modules:
                    duration = 50
                    freq = 4000
                    winsound.Beep(freq, duration)
                    winsound.Beep(freq, duration)
            else:
                self.ui.lastSave.setStyleSheet(u"color: rgba(200, 200, 200);")
        return self.current_time

    def dockCloseEventTriggered(self):
        print('Shading-Kit successfully closed.')
        self.timer.stop()
        OpenMaya.MSceneMessage.removeCallback(self.save_scene_callBack)

    def eventFilter(self, obj, event):

        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                pass
            elif event.button() == QtCore.Qt.RightButton:
                if obj in self.ui.buttonGroup.buttons():
                    if self.util_grps[obj][0].isChecked():
                        for util in self.util_grps[obj]:
                            util.setChecked(False)
                    else:
                        for util in self.util_grps[obj]:
                            util.setChecked(True)
                elif obj in self.ui.rounded_buttons.buttons():
                    if obj.objectName() == 'selectAll':
                        for util in self.all_util:
                            util.setChecked(True)
                    elif obj.objectName() == 'deselectAll':
                        for util in self.all_util:
                            util.setChecked(False)
                elif obj == self.ui.selectDirectory:
                    dialog = Second(self)
                    dialog.show()
            elif event.button() == QtCore.Qt.MiddleButton:
                pass
        elif event.type() == QtCore.QEvent.Close:
            self.close()
        return QtCore.QObject.event(obj, event)

    def select_all(self):
        for but in self.ui.buttonGroup.buttons():
            but.setChecked(True)
            self.change_but_color(but)

    def deselectAll(self):
        for but in self.ui.buttonGroup.buttons():
            but.setChecked(False)
            self.change_but_color(but)

    def checkOnOff(self):
        top_layout = self.ui.gridLayoutWidget_2
        bot_layout = self.ui.createShaderWidget
        aovLayout = self.ui.aov_frame

        if self.ui.expand_Utils.isChecked():
            self.animation.setStartValue(QtCore.QRect(top_layout.x(), top_layout.y(), top_layout.width(), 90))
            self.animation.setEndValue(QtCore.QRect(top_layout.x(), top_layout.y(), top_layout.width(), 220))

            self.aovFrameAnim.setStartValue(QtCore.QRect(aovLayout.x(), 235, aovLayout.width(), aovLayout.height()))
            self.aovFrameAnim.setEndValue(QtCore.QRect(aovLayout.x(), 390, aovLayout.width(), aovLayout.height()))

            for checkBut in self.all_util:
                checkBut.setVisible(True)
            for tree_but in self.ui.tree_Buttons.buttons():
                tree_but.setVisible(True)
            self.ui.expand_Utils.setIcon(QtGui.QIcon(os.path.join(script_folder, "icons", "shrink.png")))
            self.ui.expand_Utils.setIconSize(QtCore.QSize(20, 20))
            self.ui.expand_Utils.setStatusTip("Simple mode")
            self.bot_layout_anim.setEasingCurve(QtCore.QEasingCurve.InCurve)
            self.bot_layout_anim.setStartValue(QtCore.QRect(bot_layout.x(), 145, bot_layout.width(), bot_layout.height()))
            self.bot_layout_anim.setEndValue(QtCore.QRect(bot_layout.x(), 280, bot_layout.width(), bot_layout.height()))

            self.animation.start()
            self.bot_layout_anim.start()
            self.aovFrameAnim.start()

        else:
            self.animation.setStartValue(QtCore.QRect(top_layout.x(), top_layout.y(), top_layout.width(), 220))
            self.animation.setEndValue(QtCore.QRect(top_layout.x(), top_layout.y(), top_layout.width(), 90))

            self.aovFrameAnim.setStartValue(QtCore.QRect(aovLayout.x(), 390, aovLayout.width(), aovLayout.height()))
            self.aovFrameAnim.setEndValue(QtCore.QRect(aovLayout.x(), 235, aovLayout.width(), aovLayout.height()))

            for checkBut in self.all_util:
                checkBut.setVisible(False)
            for tree_but in self.ui.tree_Buttons.buttons():
                tree_but.setVisible(False)
            self.ui.expand_Utils.setIcon(QtGui.QIcon(os.path.join(script_folder, "icons", "expand.png")))
            self.ui.expand_Utils.setIconSize(QtCore.QSize(20, 20))
            self.ui.expand_Utils.setStatusTip("Advanced mode")
            self.bot_layout_anim.setEasingCurve(QtCore.QEasingCurve.InCurve)
            self.bot_layout_anim.setStartValue(QtCore.QRect(bot_layout.x(), 280, bot_layout.width(), bot_layout.height()))
            self.bot_layout_anim.setEndValue(QtCore.QRect(bot_layout.x(), 145, bot_layout.width(), bot_layout.height()))

            self.animation.start()
            self.bot_layout_anim.start()
            self.aovFrameAnim.start()

    def changeDefaultColor(self, color_but):
        new_color = color_but.styleSheet().split('QWidget:hover')[0].split(';')[1].split(':')[1]
        if new_color != self.default_but_color:
            self.ui.previewButOn.setStyleSheet(u"QWidget {"
                                                "color: white;"
                                                "background-color: rgba(70, 70, 70);"
                                                "border-style:solid;"
                                                "border-width:1px;"
                                                "border-radius:5px;"
                                                "border-color: rgb(140, 140, 140);}"
                                                
                                                "QWidget:hover{    "
                                                "background-color: rgb(100, 100, 100);}"
                                                
                                                "QWidget:checked{"
                                                "border-width:1px;"
                                                "border-color: " + new_color + ";}")
            self.default_but_color = new_color

            for but in (self.ui.buttonGroup.buttons() + self.ui.buttonGroup_def.buttons()):
                self.change_but_color(but)
            return self.default_but_color
        else:
            pass

    def change_but_color(self, but):
        if but.isChecked():
            but.setStyleSheet(u"QWidget {\n"
                                             "	color: white;\n"
                                             "	background-color: rgba(70, 70, 70);\n"
                                             "	border-style:solid;\n"
                                             "	border-width:1px;\n"
                                             "	border-radius:5px;\n"
                                             "	border-color: " + self.default_but_color + ";}\n"
                                             "\n"
                                             "QWidget:hover{    \n"
                                             "background-color: rgb(100, 100, 100);}\n"
                                             "\n"
                                             "QWidget:pressed{\n"
                                             "background-color: rgba(50, 50, 50);}")
            if but in self.util_grps:
                for item in self.util_grps[but]:
                    item.setEnabled(True)
        else:
            but.setStyleSheet(u"QWidget {\n"
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
                                             "background-color: rgba(50, 50, 50);}")
            if but in self.util_grps:
                for item in self.util_grps[but]:
                    item.setDisabled(True)

    def utility_nodes(self, file_node, new_shader, txt, connection, node_output, *args):

        sel_nod = []

        for ob in self.util_grps[txt]:
            if ob.isChecked():
                sel_nod.append(ob.objectName())

        if sel_nod:
            ut_node1 = cmds.shadingNode(sel_nod[0].split('_')[1], name=sel_nod[0], asUtility=True)
            cmds.connectAttr(file_node + '.outColor', ut_node1 + '.input')
            if len(sel_nod) == 1:
                cmds.connectAttr(ut_node1 + node_output, new_shader + connection)
            elif len(sel_nod) == 2:
                ut_node2 = cmds.shadingNode(sel_nod[1].split('_')[1], name=sel_nod[1], asUtility=True)
                cmds.connectAttr(ut_node1 + '.outColor', ut_node2 + '.input')
                cmds.connectAttr(ut_node2 + node_output, new_shader + connection)
            elif len(sel_nod) == 3:
                ut_node2 = cmds.shadingNode(sel_nod[1].split('_')[1], name=sel_nod[1], asUtility=True)
                ut_node3 = cmds.shadingNode(sel_nod[2].split('_')[1], name=sel_nod[2], asUtility=True)

                cmds.connectAttr(ut_node1 + '.outColor', ut_node2 + '.input')
                cmds.connectAttr(ut_node2 + '.outColor', ut_node3 + '.input')
                cmds.connectAttr(ut_node3 + node_output, new_shader + connection)
        else:
            cmds.connectAttr(file_node + node_output, new_shader + connection)

    def check_dir(self, file_node, abbreviations, *args):

        # with open(user_settings_path, 'r') as file:
        #     self.user_settings = json.load(file)

        directory_path = self.ui.directoryPath.text()

        txt_dir_list = []
        for key in self.user_settings['file_formats'].keys():
            if self.user_settings['file_formats'][key]:
                txt_dir_list.extend(cmds.getFileList(folder=directory_path, fs='*.' + str(key)))

        if txt_dir_list:
            for txt_file in txt_dir_list:
                if any(word.lower() in txt_file.lower() for word in abbreviations):
                    cmds.setAttr(file_node + '.fileTextureName', str(directory_path) + '\\' + str(txt_file),
                                 type='string')
                    break

    def create_shader(self):

        selected_objects = cmds.ls(sl=True, long=True)

        use_dir = False
        if self.ui.use_dir.isChecked():
            use_dir = True

        shader_name = self.ui.shader_text.text()
        if shader_name.isspace() or not shader_name:
            new_shader = cmds.shadingNode('aiStandardSurface', asShader=True, ss=True)
        else:
            new_shader = cmds.shadingNode('aiStandardSurface', asShader=True, name=shader_name, ss=True)

        if self.ui.assign_to_viewport.isChecked():
            cmds.select(clear=True)
            for sel_object in selected_objects:
                cmds.select(sel_object, add=True)
        cmds.hyperShade(assign=new_shader)

        cmds.setAttr(new_shader + '.base', 1)

        tiling = 0
        if self.ui.udim.isChecked():
            tiling = 3

        txt_found = []

        for txt in self.ui.buttonGroup.buttons():
            if txt.isChecked():
                button_info = self.texture_pass_list[txt.text()]

                file_node = cmds.shadingNode('file', asTexture=True, name=button_info[0], skipSelect=True)
                cmds.setAttr(file_node + '.uvTilingMode', tiling)

                if txt.text() == 'Displace':
                    disp_shader = cmds.shadingNode('displacementShader', name=shader_name + '_disp', asShader=True)
                    cmds.connectAttr(disp_shader + '.displacement', new_shader + 'SG.displacementShader')
                    txt_found.append([file_node, button_info[1]])
                    self.utility_nodes(file_node, disp_shader, txt, button_info[3], button_info[2])

                    cmds.setAttr(shader_name + '_disp.aiDisplacementZeroValue', 0.5)

                elif txt.text() == 'Normal':
                    normal_node = cmds.shadingNode('bump2d', asUtility=True, ss=True)
                    cmds.connectAttr(normal_node + '.outNormal', new_shader + '.normalCamera')
                    txt_found.append([file_node, button_info[1]])
                    self.utility_nodes(file_node, normal_node, txt, button_info[3], button_info[2])

                else:
                    txt_found.append([file_node, button_info[1]])
                    self.utility_nodes(file_node, new_shader, txt, button_info[3], button_info[2])

        if txt_found:
            plc2dtxtr = cmds.shadingNode('place2dTexture', asUtility=True, skipSelect=True)
            for node in txt_found:
                cmds.defaultNavigation(connectToExisting=True, source=plc2dtxtr, destination=node[0])
                if use_dir:
                    self.check_dir(node[0], node[1])

    def sel_all_aovs(self):
        for but in self.ui.AOV_buts.buttons():
            but.setChecked(True)
            self.change_but_color(but)

    def desel_all_aovs(self):
        for but in self.ui.AOV_buts.buttons():
            but.setChecked(False)
            self.change_but_color(but)

    def match_aovs_sel(self):
        for but in self.ui.buttonGroup.buttons():
            for but2 in self.ui.AOV_buts.buttons():
                if but.text() == but2.text():
                    if but.isChecked():
                        but2.setChecked(True)
                        self.change_but_color(but2)
                    else:
                        but2.setChecked(False)
                        self.change_but_color(but2)

    def create_delete_aovs(self, value, *args):

        selection = []
        for aov_but in self.ui.AOV_buts.buttons():
            if aov_but.isChecked():
                selection.append((self.texture_pass_list[aov_but.text()][0], self.texture_pass_list[aov_but.text()][1], self.texture_pass_list[aov_but.text()][3]))
        if selection:

            if value:
                existed_aovs = aovs.AOVInterface().getAOVs()
                existed_aovs_names = []
                for existed_AOV in existed_aovs:
                    existed_aovs_names.append(existed_AOV.name)
                already_exist = []

                for aov_name in selection:
                    if aov_name[0] not in existed_aovs_names:
                        aovs.AOVInterface().addAOV(aov_name[0])

                        selected_shaders = cmds.ls(sl=True, type='aiStandardSurface')
                        shading_groups = []
                        for shader in selected_shaders:
                            new_groups = cmds.listConnections(shader, type="shadingEngine")
                            for group in new_groups:
                                shading_groups.append((shader, group))

                        for pair in shading_groups:
                            numOfCustomAOVs = cmds.getAttr(pair[1] + '.aiCustomAOVs', size=True)
                            for customAOV in range(0, numOfCustomAOVs):
                                if cmds.getAttr(pair[1] + f'.aiCustomAOVs[{customAOV}].aovName') == aov_name[0]:
                                    ut_name = pair[0] + '_' + aov_name[0] + '_' + 'AOV'
                                    shader_att = aov_name[2]

                                    if shader_att == '.displacement':
                                        if cmds.listConnections(pair[1] + '.displacementShader', plugs=True):
                                            cmds.shadingNode('aiUserDataFloat', name = ut_name, asUtility=True, skipSelect=True)
                                            cmds.connectAttr(cmds.listConnections(pair[1] + '.displacementShader', plugs=True)[0], ut_name + '.default')
                                            cmds.connectAttr(ut_name + '.outValue', pair[1] + f'.aiCustomAOVs[{customAOV}].aovInput')
                                        else:
                                            aovs.AOVInterface().removeAOV(aov_name[0])
                                    else:
                                        if shader_att == '.bumpValue':
                                            shader_att = '.normalCamera'

                                        if cmds.getAttr(pair[0] + shader_att, type=True) == 'float3':
                                            cmds.shadingNode('aiUserDataColor', name=ut_name, asUtility=True, skipSelect=True)
                                            cmds.connectAttr(pair[0] + shader_att, ut_name + '.default')
                                            cmds.connectAttr(ut_name + '.outColor', pair[1] + f'.aiCustomAOVs[{customAOV}].aovInput')
                                        elif cmds.getAttr(pair[0] + shader_att, type=True) == 'float':
                                            cmds.shadingNode('aiUserDataFloat', name=ut_name, asUtility=True, skipSelect=True)
                                            cmds.connectAttr(pair[0] + shader_att, ut_name + '.default')
                                            cmds.connectAttr(ut_name + '.outValue', pair[1] + f'.aiCustomAOVs[{customAOV}].aovInput')
                    else:
                        already_exist.append(aov_name[0])
                if already_exist:
                    cmds.confirmDialog(t='Warning', m=f'AOVs {already_exist} already exist', icn='information')
            else:
                custom_aovs = aovs.AOVInterface().getAOVs()
                if len(custom_aovs) > 0:

                    custom_aov_names = []
                    for customAOV in custom_aovs:
                        custom_aov_names.append(customAOV.name)
                    not_found_aovs = []

                    for aov_name in selection:
                        if aov_name[0] in custom_aov_names:
                            aovs.AOVInterface().removeAOV(aov_name[0])
                            user_data_list = cmds.ls(type=('aiUserDataColor', 'aiUserDataFloat'))
                            for node in user_data_list:
                                if aov_name[0] + '_AOV' in node:
                                    cmds.delete(node)
                        else:
                            not_found_aovs.append(aov_name[0])
                    if len(not_found_aovs) != 0:
                        cmds.confirmDialog(t='Warning', m=f'AOVs {not_found_aovs} not found',
                                           icn='information')
                else:
                    cmds.confirmDialog(t='Warning', m='No active AOVs found.', icn='information')
        else:
            cmds.confirmDialog(t='Warning', m='No active selection!', icn='information')


try:
    if main_window.isVisible():
        pass
    else:
        main_window = MainWindow(parent=get_main_window())
        main_window.show(dockable=True, floating=True)
except:
    main_window = MainWindow(parent=get_main_window())
    main_window.show(dockable=True, floating=True)
