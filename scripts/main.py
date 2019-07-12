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

from main_window import MainWindow
from stats import StatTab

def create_logger(loglevel="INFO"):
    """Create a logger with the provided log level

    Args:
        loglevel (str): loglevel string for the console -> 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    """
    try:
        numeric_console_loglevel = getattr(logging, loglevel.upper())
    except AttributeError as e:
        print("LoggingError: Invalid logLevel -> {}".format(e))
        sys.exit(1)


    logger = logging.getLogger('root')
    # logger.setLevel(logging.DEBUG)

    consoleLogger = logging.StreamHandler(stream=sys.stdout)
    # consoleFormatter = logging.Formatter("{name:<5} - {levelname} - {message}", style='{')
    consoleFormatter = logging.Formatter("{asctime}|{name:<5}|{levelname:^9} - {message}", datefmt='%H:%M:%S', style='{')
    consoleLogger.setLevel(numeric_console_loglevel)
    consoleLogger.setFormatter(consoleFormatter)
    logger.addHandler(consoleLogger)
         
    # Silence the matplotlib logger
    mpl_logger = logging.getLogger("matplotlib")
    mpl_logger.setLevel(logging.WARNING)

    return logger

if __name__ == "__main__":

    # Qt Application
    app = QApplication(sys.argv)

    initials_stats = [5000000000,260]
    # Tab creation
    stat_widget = StatTab(initials_stats)
    # QMainWindow using QWidget as central widget
    window = MainWindow([stat_widget])

    window.show()
    sys.exit(app.exec_())
