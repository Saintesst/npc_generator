import json
from pathlib import Path

class DataLoader:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.traits = self._load_file("traits.json")
        self.occupations = self._load_file("occupations.json")
        self.first_names = self._load_file("first_names.json")
        self.last_names = self._load_file("last_names.json")

    def _load_file(self, filename):
        try:
            file_path = self.data_dir / filename
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Файл {filename} не найден!")
            return []
        except json.JSONDecodeError:
            print(f"Ошибка в формате файла {filename}!")
            return []

    def reload_all(self):
        """Перезагрузить все данные"""
        self.__init__(self.data_dir)