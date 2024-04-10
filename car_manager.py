from turtle import Turtle
import random

car_colour = ["blue", "red", "yellow", "white", "purple"]
increment_speed = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.increment_speed = 5

    def car_spawn(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(car_colour))
            car_starting_ycor = random.randrange(-200, 200)
            new_car.goto(x=300, y=car_starting_ycor)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.increment_speed)

    def increase_speed(self):
        self.increment_speed += 5
