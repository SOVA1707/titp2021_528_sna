#1
print("Задание №1")
class ThreeStates:

    def __init__(self):
        self.__state = 0

    def hasstate(self):
        if self.__state == 1:
            self.__state = 2
        elif self.__state == 2:
            self.__state = 3
        else:
            self.__state = 1
        print("State №", self.__state)

three_state = ThreeStates()
three_state.hasstate()
three_state.hasstate()
three_state.hasstate()
three_state.hasstate()
three_state.hasstate()
three_state.hasstate()

#2
print("Задание №2")
class Volume:

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def calc(self):
        return self._length * self._width * self._height

volume = Volume(10,20,30)
print(volume.calc())

volume = Volume(11, 3, 3)
print(volume.calc())

#3
print("Задание №3")
class Employee:

    def __init__(self, name, patronymic, surname, wage, bonus):
        self.name = str(name)
        self.patronymic = str(patronymic)
        self.surname = str(surname)
        self._salary = {"wage": float(wage), "bonus": float(bonus)}

class Salary(Employee):

    def get_full_name(self):
        return self.surname + " " + self.name + " " + self.patronymic

    def get_total_income(self):
        return self._salary["wage"] + self._salary["bonus"]

sal = Salary("Адам", "Адамович", "Шишка", 50000, 10000)
print(sal.get_full_name())
print(sal.get_total_income())

#4
print("Задание №4")
class Airplane():

    def __init__(self, speed, color, name, is_jet):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_jet = is_jet

    def go(self):
        self.is_jet = True
        print("Cамолёт", self.name, "полетел") 

    def stop(self):
        self.is_jet = False
        print("Cамолёт", self.name, "остановился") 

    def direction(self):
        print("Самолёт", self.name, "повернул")

    def show_speed(self):
        print("Самолёт движется со скоростью", self.speed)

class FastAirplane(Airplane):

    def show_speed(self):
        if self.speed > 1300:
            print("Быстрый самолёт", self.name, "имеет свурхзвуковую скорость", self.speed)
        else:
            print("Быстрый самолёт", self.name, "имеет скорость", self.speed)

class Biplane(Airplane):

    def show_speed(self):
        print("Биплан движется со скоростью", self.speed)

class ArmyAirplane(Airplane):

    def show_speed(self):
        print("Военный самолёт движется со скоростью", self.speed)


fast1 = FastAirplane(1400, "blue", "Air-1", True)
fast2 = FastAirplane(800, "black", "Air-2", False)
bip = Biplane(200, "white", "Cloud-9", False)
army = ArmyAirplane(900, "black", "Understar", True)

bip.go()
bip.direction()
bip.stop()
bip.show_speed()

army.show_speed()

fast1.show_speed()
fast1.speed = 400
fast1.show_speed()
fast2.show_speed()


