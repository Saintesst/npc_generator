import random, json
from dataclasses import dataclass
from typing import List
from pathlib import Path

@dataclass
class NPC:
    race: str
    gender: str
    first_name: str
    last_name: str
    alignment: str
    age: int
    marital_status: str
    occupation: str
    traits: List[str]


class NPCGenerator:
    def __init__(self):
        self.data_dir = Path(__file__).parent / "data"  # Путь к папке data
        self.data = self._load_data()
        self.gender = ["Мужской", "Женский"]
        if self.gender == "Женский":
            self.first_names = self.data.get("first_names_female", [])    
        else:
            self.first_names = self.data.get("first_names_male", [])
        if self.gender == "Женский":
            self.last_names = self.data.get("last_names_female", [])
        else:
            self.last_names = self.data.get("last_names_male", [])
        self.race = self.data.get("humanoid_races", [])
        self.alignment = self.data.get("alignment", [])
        self.traits = self.data.get("traits", [])
        self.occupations = self.data.get("occupations", [])
        self.marital_status = ["Холост", "Женат", "Замужем"]

    def _load_data(self):
        try:
            data_path = self.data_dir / "data.json"
            with open(data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Файл data.json не найден!")
            return {}
        except json.JSONDecodeError:
            print("Ошибка в формате JSON!")
            return {}

        
    def generate_npc(self) -> NPC:
        return NPC(
            gender=random.choice(self.gender),
            first_name=random.choice(self.first_names),
            last_name=random.choice(self.last_names),
            race=random.choice(self.race),
            alignment=random.choice(self.alignment),
            age=random.randint(18, 80),
            marital_status=random.choice(self.marital_status),
            occupation=random.choice(self.occupations),
            traits=random.sample(self.traits, 2),
        )
    
