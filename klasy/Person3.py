class Osoba:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self._birth_year = birth_year

    @property
    def age(self) -> int:
        from datetime import date
        return date.today().year - self._birth_year

    @age.setter
    def age(self, value: int):
        from datetime import date
        self._birth_year = date.today().year - value

    @age.deleter
    def age(self):
        del self._birth_year
