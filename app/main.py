class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        for car in cars:
            if car.clean_mark < self.clean_power:
                return self.calculate_washing_price(cars)

    def calculate_washing_price(self, cars: Car) -> float:
        return cars.comfort_class * (self.clean_power - cars.clean_mark) *\
            self.count_of_ratings / self.distance_from_city_center

    def wash_single_car(self, cars: Car) -> float:
        if self.clean_power > cars.clean_mark:
            cars.clean_mark = self.clean_power
            return cars
