import sys
from PyQt5 import QtWidgets
from devtoys.main import Ui_MainWindow

__version__= '0.0.2'

def run_devtoys():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())