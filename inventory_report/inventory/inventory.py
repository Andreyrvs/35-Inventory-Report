from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, string_path, string_type):

        with open(string_path, encoding="utf-8") as file:
            csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
            array = list(csv_data)
            print(array)
            if string_type == "simples":
                SimpleReport.generate(array)
            else:
                CompleteReport.generate(array)
