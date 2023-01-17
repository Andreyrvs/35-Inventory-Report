from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET
# from xml.dom import minidom


class Inventory:
    @classmethod
    def import_data(cls, string_path, string_type):
        last_three_letters = string_path[-3:]

        if str(last_three_letters) == "csv":
            with open(string_path, encoding="utf-8") as file:
                csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
                csv_list = list(csv_data)

                if string_type == "simples":
                    return SimpleReport.generate(csv_list)
                if string_type == "completo":
                    return CompleteReport.generate(csv_list)

        if str(last_three_letters) == "son":
            with open(string_path) as file:
                json_data = json.load(file)
                if string_type == "simples":
                    return SimpleReport.generate(json_data)
                if string_type == "completo":
                    return CompleteReport.generate(json_data)

        if str(last_three_letters) == "xml":
            tree = ET.parse(string_path)
            root = tree.getroot()
            print(root[0][2].text)

            xml_data = []
            xml_dict = {}
            tag = ""
            text = ""
            for element in root.iter('record'):
                for sub_elem in element:
                    # print(f"🔥🔥🔥{sub_elem}")
                    tag = sub_elem.tag
                    text = sub_elem.text
                    xml_dict[tag] = text
                    xml_data.append(xml_dict)

            print(f"🔥🔥🔥{xml_dict}")
            # print(ET.tostring(root, encoding='utf8').decode('utf8'))

            if string_type == "simples":
                return SimpleReport.generate(xml_data)
            if string_type == "completo":
                return CompleteReport.generate(xml_data)
