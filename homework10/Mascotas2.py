from Mascotas import Mascota, Perro, Ave, Pez


class MascotasCreator(Perro, Ave, Pez, Mascota):

    @staticmethod
    def create_animal(name: str, weight: int, age: int):
        return Mascota(name, weight, age)

    @staticmethod
    def create_bird(name: str, weight: int, age: int, bird_type: str, sound: str):
        return Ave(name, weight, age, bird_type, sound)

    @staticmethod
    def create_dog(name: str, weight: int, age: int, dog_type: str):
        return Perro(name, weight, age, dog_type)

    @staticmethod
    def create_fish(name: str, weight: int, age: int, fish_type: str):
        return Pez(name, weight, age, fish_type)

if __name__ == '__main__':
    Pachuchi = MascotasCreator.create_dog('Pachuchi', 5, 2, 'Bolonka')
    print(Pachuchi)
    Akula = MascotasCreator.create_fish('Akulka', 15, 7, 'Kit')
    print(Akula)
    mascotka = MascotasCreator.create_animal('Ballena', 70, 7)
    print(mascotka)