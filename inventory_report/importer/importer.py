from abc import ABC, abstractmethod
# from inventory_report.importer.importer import CsvImporter


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls, strategy):
        raise NotImplementedError