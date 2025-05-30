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
        self.first_name_male = self.data.get("first_names_male", [])
        self.first_name_female = self.data.get("first_names_female", [])
        self.last_name_male = self.data.get("last_names_male", [])
        self.last_name_female = self.data.get("last_names_female", [])
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
        
        gender = random.choice(self.gender)  
    
        first_names = (
            self.data.get("first_names_female", []) 
            if gender == "Женский" 
            else self.data.get("first_names_male", [])
        )
        last_names = (
            self.data.get("last_names_female", []) 
            if gender == "Женский" 
            else self.data.get("last_names_male", [])
        )
    
        return NPC(
            race=random.choice(self.race),
            gender=gender, 
            first_name=random.choice(first_names),
            last_name=random.choice(last_names),
            alignment=random.choice(self.alignment),
            age=random.randint(18, 80),
            marital_status=random.choice(self.marital_status),
            occupation=random.choice(self.occupations),
            traits=random.sample(self.traits, 2),
        )
    
