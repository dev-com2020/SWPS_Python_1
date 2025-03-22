from dataclasses import dataclass


@dataclass
class Persona:
    name: str
    surname: str

    def powitanie(self) -> str:
        return f"Witam, jestem {self.name}, {self.surname}"