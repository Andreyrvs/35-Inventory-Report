from inventory_report.importer.importer import Importer


class JsonImporter(Importer):

    @classmethod
    def import_data(cls, path_name):
        last_three_letters = path_name[-5:]

        if last_three_letters != '.json':
            raise ValueError("Arquivo inválido")
