from inventory_report.importer.importer import Importer


class CsvImporter(Importer):

    @classmethod
    def import_data(cls, path_name):
        last_three_letters = path_name[-4:]

        if last_three_letters != '.csv':
            raise ValueError("Arquivo inválido")

