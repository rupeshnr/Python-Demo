# OPPs
class Car:
    carType="manuel" # global feature
    def _init_(self, year, speed):
        self.year=year # instance feature
        self.speed=speed
    @staticmethod
    def welcome():
        print("Welcome to the car showroom")
    @classmethod
    def type(cls):
        print(print("These cars", cls.carType))
    def getSpeed(self):
        print("Maximum speed is", self. speed)
