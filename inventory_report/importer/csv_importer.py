from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, path_name):
        last_three_letters = path_name[-4:]

        if last_three_letters != '.csv':
            raise ValueError("Arquivo inválido")

        with open(path_name, encoding="utf-8") as file:
            csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
            csv_list = list(csv_data)

            return csv_list
