class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} wydaje dźwięk"


class Chomik(Animal):

    def __init__(self, name: str, kolor: str):
        super().__init__(name)
        self.kolor = kolor

    def speak(self) -> str:
        return f"{self.name} w kolorze {self.kolor} sobie skrobię..."

    def biega(self) -> str:
        return f"{self.name} biega w karuzeli"
