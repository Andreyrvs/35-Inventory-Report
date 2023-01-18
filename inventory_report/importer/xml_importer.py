from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):

    @classmethod
    def import_data(cls, path_name):
        last_three_letters = path_name[-4:]

        if last_three_letters != '.xml':
            raise ValueError("Arquivo inválido")

        tree = ET.parse(path_name)
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