from abc import ABC, abstractmethod
from inventory_report.importer.importer import CsvImporter


class Importer(ABC):
    @abstractmethod
    def import_data(self):
        pass