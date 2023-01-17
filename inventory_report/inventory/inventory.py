from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


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
