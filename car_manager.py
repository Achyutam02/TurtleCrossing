from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):

        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.cars_speed)

    def speed_incer(self):
        print(self.cars_speed)
        self.cars_speed += MOVE_INCREMENT


    def reset(self):

        for i in self.all_cars:
            i.goto(1000, 1000)

        self.all_cars.clear()
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.create_cars()

