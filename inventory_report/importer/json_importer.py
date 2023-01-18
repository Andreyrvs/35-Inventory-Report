from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    @classmethod
    def import_data(cls, path_name):
        last_three_letters = path_name[-5:]

        if last_three_letters != '.json':
            raise ValueError("Arquivo inválido")

        with open(path_name) as file:
            json_data = json.load(file)
            return json_data
