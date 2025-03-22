class Person:
    """Reprezentuje osobę z imieniem i nazwiskiem"""

    def __init__(self, imie: str, nazwisko: str):
        self.name = imie
        self.surname = nazwisko

    def powitanie(self) -> str:
        return f"Witam, jestem {self.name}, {self.surname}"
