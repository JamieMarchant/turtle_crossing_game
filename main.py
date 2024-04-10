import time
from turtle import Screen, Turtle
from player import Player
from car_manager import Car
from scoreboard import Scoreboard


# Screen settings
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("grey")
screen.title("Turtle Crossing Game")
screen.tracer(0)

# Road decor
road_decor_top = Turtle()
road_decor_top.penup()
road_decor_top.shape("square")
road_decor_top.color("white")
road_decor_top.goto(300, 220)
road_decor_top.shapesize(stretch_wid=1, stretch_len=400)

road_decor_bottom = Turtle()
road_decor_bottom.penup()
road_decor_bottom.shape("square")
road_decor_bottom.color("white")
road_decor_bottom.goto(300, -220)
road_decor_bottom.shapesize(stretch_wid=1, stretch_len=400)

# Class imports
player = Player()
car = Car()
scoreboard = Scoreboard()

# Key settings
screen.listen()
screen.onkey(player.move, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.car_spawn()
    car.move_car()

    # Detect collision with cars
    for enemy_car in car.all_cars:
        if player.distance(enemy_car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect colison with goal and increase the speed of cars
    if player.ycor() > 290:
        player.next_level()
        car.increase_speed()
        scoreboard.point()
        scoreboard.update_scoreboard()


# Close the game
screen.exitonclick()
