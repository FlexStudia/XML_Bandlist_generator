# coding: utf-8

"""
    Forge:
        * main branch: https://gricad-gitlab.univ-grenoble-alpes.fr/SSHADE/sshade/-/issues/1148
        * branch for implementation SSDM v0.92a: https://gricad-gitlab.univ-grenoble-alpes.fr/SSHADE/sshade/-/issues/1282

    About:
        This tool converts xlsx file to xml.
        It is a part of SSHADE project (https://www.sshade.eu/)

    Useful tools:
        * Notepad++ plugin XML Tools (to install go to Plugins -> Plugins Admin -> XML Tools -> Install)
"""

# 1 IMPORTS
# 1.1 PyQt pack
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QAction, QProgressDialog
from PyQt5.QtCore import Qt, QSettings
import sys
import os
from os import path as os_path
# 1.2 templates
from templates.mw import Ui_MainWindow as Ui_MainWindow
# 1.3 core code
from XMLGenerator_Bandlist_core import XML_filler as XML_filler
from XMLGenerator_Bandlist_core import verification_F as verification_F

"""
    TODO:
        One day:
        * to finish verification tests
    
"""


# 2 GLOBALS
# variables
__version__ = 0.693
__copyright__ = "<a href='https://www.gnu.org/licenses/gpl-3.0.html'>The GNU General Public License v3.0</a>"
__GitHub_repos__ = "https://github.com/FlexStudia/XML_Bandlist_generator"
__author_mail__ = "<a href='mailto: flex.studia.dev@gmail.com'>flex.studia.dev@gmail.com</a>"
__bug_support_mail__ = "<a href='mailto: flex.studia.help@gmail.com'>flex.studia.help@gmail.com</a>"
__app_name__ = "XMLGenerator Bandlists"
__org_name__ = "Flex Studia Dev"
# styles
settings = QSettings(__org_name__, __app_name__)
button_pudding = 5
red_color = "FFE4E6"
red_color_hover = "FFF9F9"
green_color = "EDFFF4"
green_color_hover = "F9FFFB"
blue_color = "E7F2FF"
blue_color_hover = "F3F9FF"


# 3 MAIN WINDOW class
class XMLGeneratorMainW(QtWidgets.QMainWindow):
    def __init__(self):
        super(XMLGeneratorMainW, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 3.0 class constants
        self.data_source = ""
        self.str_to_upload = ""
        self.xml_file_name = ""
        self.open_dir = ""
        self.save_dir = ""
        # 3.1 GUI beauties
        self.setWindowTitle(f'SSHADE Bandlist XLSX to XML v{__version__}')
        values_array = ["absorption", "Raman scattering", "reflectance", "thermal emission", "fluorescence emission"]
        for index in range(0, len(values_array)):
            self.ui.cb_bl_type.insertItem(index, values_array[index])
        self.ui.cb_bl_type.setCurrentIndex(0)
        self.ui.cb_bl_type.setStyleSheet(f'QComboBox(padding: {button_pudding}px;)'.replace("(", "{").replace(")", "}"))
        self.ui.btn_chose.setStyleSheet(f'QPushButton(padding: {button_pudding}px; background-color: #{red_color}) QPushButton:hover(padding: {button_pudding}px; background-color: #{red_color_hover})'.replace("(", "{").replace(")", "}"))
        self.ui.btn_read.setStyleSheet(f'QPushButton(padding: {button_pudding}px; background-color: #{green_color}) QPushButton:hover(padding: {button_pudding}px; background-color: #{green_color_hover})'.replace("(", "{").replace(")", "}"))
        self.ui.btn_generate.setStyleSheet(f'QPushButton(padding: {button_pudding}px; background-color: #{blue_color}) QPushButton:hover(padding: {button_pudding}px; background-color: #{blue_color_hover})'.replace("(", "{").replace(")", "}"))
        # Menu
        extractAction = QAction("&About", self)
        extractAction.setStatusTip('About The App')
        extractAction.triggered.connect(self.show_about)
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Help')
        fileMenu.addAction(extractAction)
        # 3.2 SLOT functions connect
        self.ui.btn_chose.clicked.connect(self.choose_file_function)
        self.ui.btn_read.clicked.connect(self.read_and_analyse)
        self.ui.btn_generate.clicked.connect(self.fill_and_save)

    # 3.3 SLOT functions
    def dialog_ok(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Info')
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Information)
        dlg.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Error!')
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def show_about(self):
        self.dialog_ok(f"<b>XML generator: instrument</b> v{__version__}"
                       f"<p>Copyright: {__copyright__}</p>"
                       f"<p><a href='{__GitHub_repos__}'>GitHub repository</a> (program code and more information)</p>"
                       f"<p>Created by Gorbacheva Maria ({__author_mail__})</p>"
                       "<p>Scientific base by Bernard Schmitt, IPAG (bernard.schmitt@univ-grenoble-alpes.fr)</p>"
                       f"<p>For any questions and bug reports, please, mail at {__bug_support_mail__}</p>"
                       "<p>In case of a bug, please report it and specify your operating system, "
                       "provide a detailed description of the problem with screenshots "
                       "and the files used and produced, if possible. Your contribution matters to make it better!</p>")

    def choose_file_function(self):
        if self.open_dir and os_path.exists(self.open_dir):
            path, _ = QFileDialog.getOpenFileName(self, "Choose file", self.open_dir, "MS Excel Spreadsheet (*.xlsx *.xlsm *.xltx *.xltm)")
        elif settings.value("open_dir") and os_path.exists(settings.value("open_dir")):
            path, _ = QFileDialog.getOpenFileName(self, "Choose file", settings.value("open_dir"), "MS Excel Spreadsheet (*.xlsx *.xlsm *.xltx *.xltm)")
        else:
            path, _ = QFileDialog.getOpenFileName(self, "Choose file", os.getcwd(), "MS Excel Spreadsheet (*.xlsx *.xlsm *.xltx *.xltm)")
        if path:
            try:
                self.data_source = path
                if path.rfind("/") != -1:
                    data_file_name = path[path.rfind("/") + 1:]
                    self.open_dir = path[:path.rfind("/") + 1]
                else:
                    data_file_name = path[path.rfind("\\") + 1:]
                    self.open_dir = path[:path.rfind("\\") + 1]
                settings.setValue("open_dir", self.open_dir)
                self.ui.lbl_file_name.setText(data_file_name)
            except Exception as e:
                self.dialog_critical(f'Critical error while opening file: {str(e)}.'
                                     f'\nThis file may be corrupted.')

    def read_and_analyse(self):
        if self.data_source:
            self.dialog_analyse("Working...", "Abort", 0, 100)
        else:
            self.dialog_critical(f'Please, chose an XLSX file before generate an XML.')
    
    def dialog_analyse(self, text1, text2, lim1, lim2):
        dlg = QProgressDialog(text1, text2, lim1, lim2)
        dlg.setWindowModality(Qt.WindowModal)
        dlg.setStyleSheet("QLabel{min-width: 300px;}")
        dlg.setMinimumDuration(0)
        dlg.setWindowTitle('Working...')
        max_step = 2
        for i in range(1, max_step):
            dlg.setValue(int(i * 100 / max_step))
            if dlg.wasCanceled():
                break
            if i == 1:
                dlg.setWindowTitle('Analysing XLSX...')
                try:
                    verification_result = verification_F(self.data_source, self.from_cb_to_str_type())
                    self.ui.error_log.setPlainText(verification_result)
                except Exception as e:
                    self.dialog_critical(f'Critical error during verification: {str(e)}.')
        dlg.setValue(100)
        dlg.show()

    def fill_and_save(self):
        if self.data_source:
            try:
                self.dialog_fill("Working...", "Abort", 0, 100)
                options = QFileDialog.Options()
                xml_file_name = self.xml_file_name
                if self.save_dir and os_path.exists(self.save_dir):
                    file_name, _ = QFileDialog.getSaveFileName(self, "Save File", self.save_dir + xml_file_name, "XML Files (*.xml)", options=options)
                elif settings.value("save_dir") and os_path.exists(settings.value("save_dir")):
                    file_name, _ = QFileDialog.getSaveFileName(self, "Save File", settings.value("save_dir") + xml_file_name, "XML Files (*.xml)", options=options)
                else:
                    file_name, _ = QFileDialog.getSaveFileName(self, "Save File", xml_file_name, "XML Files (*.xml)", options=options)
                if file_name.rfind("/") != -1:
                    self.save_dir = file_name[:file_name.rfind("/") + 1]
                    settings.setValue("save_dir", self.save_dir)
                else:
                    self.save_dir = file_name[:file_name.rfind("\\") + 1]
                    settings.setValue("save_dir", self.save_dir)
                if file_name:
                    with open(file_name, 'w+', encoding="utf-8") as file_output:
                        file_output.write(self.str_to_upload.decode("utf-8"))
            except Exception as e:
                self.dialog_critical(f'Critical error during XML creation: {str(e)}.')
        else:
            self.dialog_critical(f'Please, chose an XLSX file before generate an XML.')

    def dialog_fill(self, text1, text2, lim1, lim2):
        dlg = QProgressDialog(text1, text2, lim1, lim2)
        dlg.setWindowModality(Qt.WindowModal)
        dlg.setStyleSheet("QLabel{min-width: 300px;}")
        dlg.setMinimumDuration(0)
        dlg.setWindowTitle('Working...')
        max_step = 2
        for i in range(1, max_step):
            dlg.setValue(int(i * 100 / max_step))
            if dlg.wasCanceled():
                break
            if i == 1:
                dlg.setWindowTitle('Reading XLSX...')
                result = XML_filler(self.data_source, self.from_cb_to_str_type())
                self.str_to_upload = result[0]
                self.xml_file_name = result[1]
        dlg.setValue(100)
        dlg.show()

    def from_cb_to_str_type(self):
        if self.ui.cb_bl_type.currentIndex() == 0:
            return "ABS"
        if self.ui.cb_bl_type.currentIndex() == 1:
            return "RAMAN"
        return ""


# 4 MAIN WINDOW class emulation
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setApplicationName(__app_name__)
    app.setOrganizationName(__org_name__)
    win = XMLGeneratorMainW()
    win.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
    win.show()
    sys.exit(app.exec())
