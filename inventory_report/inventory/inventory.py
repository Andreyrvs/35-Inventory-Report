from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, string_path, string_type):

        print(f"🔥🔥🔥🔥{string_path} -- {string_type}\n")

        with open(string_path, encoding="utf-8") as file:
            csv_data = csv.DictReader(file, delimiter=",", quotechar='"')
            csv_list = list(csv_data)

            print(f"💵💵💵{csv_list}\n")

            if string_type == "simples":
                SimpleReport.generate(csv_list)
            if string_type == "completo":
                CompleteReport.generate(csv_list)
