import random
from dataclasses import dataclass
from typing import List

@dataclass
class NPC:
    first_name: str
    last_name: str
    age: int
    marital_status: str
    occupation: str
    traits: List[str]
    appearance: str

class NPCGenerator:
    def __init__(self):
        with open("data/names.json", "r") as f:
            names_data = json.load(f)
            self.first_names = names_data["first_names"]
            self.last_names = names_data["last_names"]
        
        self.marital_statuses = ["Холост", "Женат", "Разведен", "Вдовец"]
        self.occupations = [...]  # загрузите из файла
        self.traits = [...]       # загрузите из файла
        
    def generate_npc(self) -> NPC:
        return NPC(
            first_name=random.choice(self.first_names),
            last_name=random.choice(self.last_names),
            age=random.randint(18, 80),
            marital_status=random.choice(self.marital_statuses),
            occupation=random.choice(self.occupations),
            traits=random.sample(self.traits, 3),
            appearance=self._generate_appearance()
        )
    
    def _generate_appearance(self) -> str:
        descriptions = [...]
        return random.choice(descriptions)