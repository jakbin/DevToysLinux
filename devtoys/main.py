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

        # json format
        self.jsonformate_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.json_formate_page)) # for home page
        self.jsonformate_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.json_formate_page)) # for formatters page
        self.json_format_button.clicked.connect(self.format_json)

        # json to yaml
        self.jsontoyaml_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.jsontoyaml_page)) # for home page
        self.jsontoyaml_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.jsontoyaml_page)) # for converts page
        self.jsontoyaml_convert_button.clicked.connect(self.json_to_yaml)

        # yaml to json
        self.yamltojson_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.yamltojson_page)) # for home page
        self.yamltojson_button_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.yamltojson_page)) # for converts page
        self.yamltojson_convert_button.clicked.connect(self.yaml_to_json)

    def format_json(self):
        text = self.json_input.toPlainText()
        dict_data = json.loads(text)
        rdata = json.dumps(dict_data, indent=4, sort_keys=True)
        self.json_output.setText(rdata)

    def json_to_yaml(self):
        text = self.json_input_2.toPlainText()
        dict_data = json.loads(text)
        data = yaml.dump(dict_data, indent=4)
        self.yaml_output_2.setText(data)

    def yaml_to_json(self):
        text = self.yaml_input_3.toPlainText()
        dict_data = yaml.safe_load(text)
        data = json.dumps(dict_data, indent=4)
        self.json_output_3.setText(data)
