import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

screen.listen()
scoreboard = Scoreboard()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()

    if player.ycor() > 280:
        player.restart()
        car.speed_incer()
        scoreboard.update_screen()

    for cars in car.all_cars:
        if cars.distance(player) < 30:
            car.reset()
            player.restart()
            scoreboard.reset()

screen.exitonclick()
