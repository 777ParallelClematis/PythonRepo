class Car:
    SPEED_LIMIT_KM: float = 140

    def __init__(self, brand: str) -> None:
        self.brand = brand

    def drive(self, speed: float) -> None:
        if speed > self.SPEED_LIMIT_KM:
            print(f'Limiter activated: Driving at {self.SPEED_LIMIT_KM} km/hr')
        else:
            print(f'Driving at {speed} km/hr')

def main() -> None:
    toyota: Car = Car('Toyota')
    bmw: Car = Car('BMW')

    toyota.drive(200)
    bmw.drive(210)

    Car.SPEED_LIMIT_KM = 99
    toyota.drive(200)
    toyota.drive(210)





if __name__ == '__main__':
    main()
