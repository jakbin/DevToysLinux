from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json
import yaml
import sys
import os

base_dir = os.path.dirname(os.path.realpath(__file__))
ui_path = os.path.join(base_dir, 'main.ui')

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        uic.loadUi(ui_path, self)

        self.all_tools_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home_page))
        self.fsrmatters_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.farmatters_page))
        self.convertors_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.converters_page))

        self.jsonformate_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.json_formate_page))
        self.jsonformate_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.json_formate_page))

        self.json_format_button.clicked.connect(self.format_json)

    def format_json(self):
        text = self.json_input.toPlainText()
        dict_data = json.loads(text)
        rdata = json.dumps(dict_data, indent=4, sort_keys=True)
        self.json_output.setText(rdata)

    def json_to_yaml(self):
        text = self.textEdit.toPlainText()
        dict_data = json.loads(text)
        data = yaml.dump(dict_data)
        self.textEdit_2.setText(data)
