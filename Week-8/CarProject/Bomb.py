from Car import Car

class Bomb(Car):

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        return 0