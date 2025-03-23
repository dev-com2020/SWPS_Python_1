class Termometr:
    def __init__(self):
        self._celsius = 0

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

    def to_fahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32

    def to_kelvin(self) -> float:
        return self._celsius + 273.15