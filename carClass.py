class Car(object):
    def __init__(self, brand, model, color, carNumber = None):
        self.brand = brand
        self.model = model
        self.color = color
        self.carNumber = carNumber
    def getCar(self):
        print("Your car brand is " + self.brand + " and your model number is " + self.model)
    def getColor(self):
        print("Your car color is " + self.color)
    def getcarNumber(self):
        print("The numberplate on your car is " + self.carNumber)
car1 = Car("Hyundai","i20", "grey", "1234567")
car2 = Car("Audi","Q7", "black", "876543")
car1.getCar()
car2.getcarNumber()