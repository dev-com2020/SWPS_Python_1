class Termometr:
    def __init__(self):
        self._celsius = 30

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("zero absolutne!!!")
        self._celsius = value

    def __repr__(self) -> str:
        return f"Klasa Termometr(temperatura={self._celsius})"
