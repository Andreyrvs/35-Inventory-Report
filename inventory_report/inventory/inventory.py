from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_data(cls, string_path, string_type):
        last_three_letters = string_path[-3:]

        if str(last_three_letters) == "csv":
            return cls.read_csv(cls, string_path, string_type)

        if str(last_three_letters) == "son":
            return cls.read_json(cls, string_path, string_type)

        if str(last_three_letters) == "xml":
            return cls.formatted_xml(cls, string_path, string_type)

    def read_csv(self, string_path, string_type):

        with open(string_path, encoding="utf-8") as file:
            csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
            csv_list = list(csv_data)

            if string_type == "simples":
                return SimpleReport.generate(csv_list)
            if string_type == "completo":
                return CompleteReport.generate(csv_list)

    def read_json(self, string_path, string_type):

        with open(string_path) as file:
            json_data = json.load(file)
            if string_type == "simples":
                return SimpleReport.generate(json_data)
            if string_type == "completo":
                return CompleteReport.generate(json_data)

    def read_xml(self, string_path):

        last_three_letters = string_path[-3:]
        print(f"🔥🔥🔥{last_three_letters}")

        tree = ET.parse(string_path)
        root = tree.getroot()

        xml_data = []
        tag = ""
        text = ""

        for element in root.iter('record'):
            xml_dict = {}
            for sub_elem in element:
                tag = sub_elem.tag
                text = sub_elem.text
                xml_dict[tag] = text
            xml_data.append(xml_dict)

        return xml_data

    def formatted_xml(self, string_path, string_type):

        if string_type == "simples":
            return SimpleReport.generate(self.read_xml(self, string_path))
        if string_type == "completo":
            return CompleteReport.generate(self.read_xml(self, string_path))
