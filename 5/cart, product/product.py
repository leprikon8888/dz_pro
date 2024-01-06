
class Product:
    def __init__(self, name: str, price: float | int):

        self.name = name
        self.price = price
    # остальной код

    def __str__(self):
        return f"{self.name} - {self.price}"