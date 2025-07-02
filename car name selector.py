# building a car company program
car_companies = [
    'toyota', 'TOYOTA', 'Toyota',
    'honda', 'HONDA', 'Honda',
    'suzuki', 'SUZUKI', 'Suzuki',
    'daihatsu', 'DAIHATSU', 'Daihatsu',
    'nissan', 'NISSAN', 'Nissan',
    'kia', 'KIA', 'Kia',
    'hyundai', 'HYUNDAI', 'Hyundai',
    'changan', 'CHANGAN', 'Changan',
    'haval', 'HAVAL', 'Haval',
    'mg', 'MG', 'Mg',
    'baic', 'BAIC', 'Baic',
    'dfsk', 'DFSK', 'Dfsk',
    'prince', 'PRINCE', 'Prince',
    'faw', 'FAW', 'Faw',
    'chevrolet', 'CHEVROLET', 'Chevrolet',
    'bmw', 'BMW', 'Bmw',
    'mercedes-benz', 'MERCEDES-BENZ', 'Mercedes-Benz',
    'audi', 'AUDI', 'Audi'
]

car = input("what type of car do you wnat sir: ").lower()
if car not in car_companies:
        print(f"let's see if we could find a {car.title()} for you!")
else:
        while car in car_companies:
                print("i asked you about the car not the company")
                message = input("what type of car do you wnat sir: ")
                if message not in car_companies:
                        print(f"let's see if we could find a {message.title()} for you!")
                        break


