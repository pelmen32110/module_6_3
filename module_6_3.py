import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,speed):
        _cords = [0, 0, 0]
        self.speed = speed

    def move(self,dx,dy,dz):
        self.dx = dx
        self.dy = dy
        if dz < 0:
            print("Это слишком глубоко, я не могу там плавать :(")
        else:
            self.dz = dz
        _cords = [self.dx, self.dy, self.dz]

    def get_cords(self):
        return print(f'X: {self.dx  * self.speed}, Y: {self.dy  * self.speed}, Z: {self.dz  * self.speed}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Сорян, я мирный :)")
        else:
            print("Готовься, я нападаю на тебя О_О")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        random_eggs = random.randint(1,4)
        if random_eggs > 1:
            print(f'Здесь {random_eggs} яйца для тебя')
        else:
            print(f'Здесь {random_eggs} яйцо для тебя')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self,_dz):
        self._dz = abs(_dz)/2
        super().move(self.dx,self.dz,int(self.dz - self._dz))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird,PoisonousAnimal,AquaticAnimal):
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

