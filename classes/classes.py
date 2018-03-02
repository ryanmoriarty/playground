class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

man = Celsius()
man.temperature = 37
man.temperature

man.to_fahrenheit()


man.__dict__
