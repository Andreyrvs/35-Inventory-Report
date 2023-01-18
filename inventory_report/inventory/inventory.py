from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET
# from xml.dom import minidom


class Inventory:

    def __init__(self) -> None:
        pass

    def read_csv(self, string_path, string_type):
        self.string_path = string_path
        self.string_type = string_type

        last_three_letters = string_path[-3:]

        if str(last_three_letters) == "csv":
            with open(self.string_path, encoding="utf-8") as file:
                csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
                csv_list = list(csv_data)

                if self.string_type == "simples":
                    return SimpleReport.generate(csv_list)
                if self.string_type == "completo":
                    return CompleteReport.generate(csv_list)

    def read_json(self, string_path, string_type):
        self.string_path = string_path
        self.string_type = string_type
        last_three_letters = string_path[-3:]

        if str(last_three_letters) == "son":
            with open(self.string_path) as file:
                json_data = json.load(file)
                if self.string_type == "simples":
                    return SimpleReport.generate(json_data)
                if self.string_type == "completo":
                    return CompleteReport.generate(json_data)

    def formatedd_xml(self, string_path):
        last_three_letters = string_path[-3:]
        if str(last_three_letters) == "xml":
            tree = ET.parse(self.string_path)
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

    def read_xml(self, string_path, string_type):
        self.string_path = string_path
        self.string_type = string_type

        if string_type == "simples":
            return SimpleReport.generate(self.formatedd_xml(string_path))
        if string_type == "completo":
            return CompleteReport.generate(self.formatedd_xml(string_path))

    @classmethod
    def import_data(cls, string_path, string_type):
        cls.read_csv(string_path, string_type)
        cls.read_json(string_path, string_type)
        cls.read_xml(string_path, string_type)






        # ----------------
        # if str(last_three_letters) == "csv":
        #     with open(string_path, encoding="utf-8") as file:
        #         csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
        #         csv_list = list(csv_data)

        #         if string_type == "simples":
        #             return SimpleReport.generate(csv_list)
        #         if string_type == "completo":
        #             return CompleteReport.generate(csv_list)
        # ----------------
        # if str(last_three_letters) == "son":
        #     with open(string_path) as file:
        #         json_data = json.load(file)
        #         if string_type == "simples":
        #             return SimpleReport.generate(json_data)
        #         if string_type == "completo":
        #             return CompleteReport.generate(json_data)

        # ---------------------
        # if str(last_three_letters) == "xml":
        #     tree = ET.parse(string_path)
        #     root = tree.getroot()

        #     xml_data = []
        #     tag = ""
        #     text = ""

        #     for element in root.iter('record'):
        #         xml_dict = {}
        #         for sub_elem in element:
        #             tag = sub_elem.tag
        #             text = sub_elem.text
        #             xml_dict[tag] = text
        #         xml_data.append(xml_dict)

        #     print(f"🔥🔥🔥{xml_data}")

        #     if string_type == "simples":
        #         return SimpleReport.generate(xml_data)
        #     if string_type == "completo":
        #         return CompleteReport.generate(xml_data)