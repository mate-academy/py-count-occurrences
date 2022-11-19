class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __int__(self, distance_from_city_center: int,
                clean_power: int,
                average_rating: float,
                count_of_ratings: int
                ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings


def serve_cars(car: Car, wash_station: CarWashStation) -> None:
    if Car(car.clean_mark) < CarWashStation(wash_station.clean_power):
        return CarWashStation(wash_station.average_rating.round)


def calculate_washing_price(car: Car, wash_station: CarWashStation) -> None:
    price = Car(car.comfort_class) *\
        (CarWashStation(wash_station.clean_power) - Car(car.clean_mark)) *\
        CarWashStation(wash_station.average_rating) /\
        CarWashStation(wash_station.distance_from_city_center)
    return price.round


def wash_single_car(car: Car, wash_station: CarWashStation) -> None:
    if CarWashStation(wash_station.clean_power) > Car(car.clean_mark):
        Car(car.clean_mark) == CarWashStation(wash_station.clean_power)


def rate_service(wash_station: CarWashStation) -> None:
    for i in range:
        CarWashStation(wash_station.average_rating) + [i]
        CarWashStation(wash_station.count_of_ratings) + [i]
