class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self) -> None:
        if Car(self.clean_mark) < CarWashStation(self.clean_power):
            return CarWashStation(self.average_rating.round)

    def calculate_washing_price(self) -> None:
        price = Car(self.comfort_class) *\
            (CarWashStation(self.clean_power) - Car(self.clean_mark)) *\
            CarWashStation(self.average_rating) /\
            CarWashStation(self.distance_from_city_center)
        return price.round

    def wash_single_car(self) -> None:
        if CarWashStation(self.clean_power) > Car(self.clean_mark):
            Car(self.clean_mark) == CarWashStation(self.clean_power)

    def rate_service(self) -> None:
        for i in range:
            CarWashStation(self.average_rating) + [i]
            CarWashStation(self.count_of_ratings) + [i]


bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=2, brand='Audi')

print(bmw.clean_mark)  # 3
print(audi.clean_mark) # 2

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars

print(income)

print(bmw.clean_mark)
print(audi.clean_mark)
