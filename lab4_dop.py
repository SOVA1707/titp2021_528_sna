#1
class Soda:

    def __init__(self, dobavka):
        self.add = str(dobavka)
    
    def show_my_drink(self):
        if self.add == '':
            print('Обычная газировка')
        else:
            print('Газировка ' + self.add)


soda = Soda('Виноград')
soda.show_my_drink()

soda = Soda('')
soda.show_my_drink()

#2
class TriangleChecker:
    @staticmethod
    def is_triangle(num1, num2, num3):
        if not(type(num1) == int or type(num1) == float) or not(type(num2) == int or type(num2) == float) or not(type(num3) == int or type(num2) == float):
            print('Нужно вводить только числа!')
            return
        if num1 < 0 or num2 < 0 or num3 < 0:
            print('С отрицательным числами ничего не выйдет!')
            return
        if (num1 + num2 > num3) and (num2 + num3 > num1) and (num1 + num3 > num2):
            print('Ура, можно построить треугольник!')
            return
        else:
            print('Жаль, но из этого треугольник не сделать.')

TriangleChecker.is_triangle(200, 200, 500)
TriangleChecker.is_triangle('text', 200, 500)
TriangleChecker.is_triangle(200, 200, 200)
TriangleChecker.is_triangle(200, 200, -500)

#3
class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg
        print('Масса: ' + str(kg))
        
    def to_pounds(self):
        return self.__kg * 2.205
    
    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
        
    def get_kg(self):
        return self.__kg
    
    kg = property(get_kg, set_kg)

kg1 = KgToPounds(10)
print(kg1.to_pounds())
kg1.kg = 20
print(kg1.to_pounds())
