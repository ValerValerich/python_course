# Решить задания, которые не успели решить на семинаре.
# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики

from sem10 import Dog, Cat, Fish

# Я что-то сделал, но не понял(

class AnimalFactory():
    def create_animal(self, *args, **kwargs):

        if self == 'Dog':
            return Dog(*args, **kwargs)
        if self == 'Cat':
            return Cat(*args, **kwargs)
        if self == 'Fish':
            return Fish(*args, **kwargs)



dog = AnimalFactory.create_animal("Dog", "Gagngster", 12, breed="woof")
cat = AnimalFactory.create_animal("Cat", 'Maffin', 7, color='Empty')

print(dog.special)
print(dog.name)

print(cat.special)