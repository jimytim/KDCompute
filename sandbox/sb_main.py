import os
import sys
import logging 
import PySide2

if sys.platform == "win32":
    pyside2_dirpath = os.path.dirname(PySide2.__file__)
    pyside2_plugin_path = os.path.join(pyside2_dirpath, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = pyside2_plugin_path
    
from PySide2.QtCore import QDateTime, QTimeZone
from PySide2.QtWidgets import QApplication

from sb_main_window import MainWindow
from sb_tab import Tab

if __name__ == "__main__":

    # Qt Application
    app = QApplication(sys.argv)

    table_tab = Tab()
    # QMainWindow using QWidget as central widget
    window = MainWindow([table_tab])

    window.show()
    sys.exit(app.exec_())
