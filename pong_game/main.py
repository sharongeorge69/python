"""
Pong Game in Python 🕹️
-----------------------

This is a classic Pong game implementation using the `turtle` graphics module in Python.

Key Features:
- Two-player support: 
    - Right paddle controlled with Up/Down arrow keys.
    - Left paddle controlled with W/S keys.
- Ball movement with realistic bounce effects.
- Score tracking for both players.
- Game loop with smooth animation and speed control.

Modules Used:
- `paddle.py`: Defines the Paddle class for paddle movement.
- `ball.py`: Defines the Ball class with movement and collision logic.
- `scoreboard.py`: Handles score updates and display.
- `main.py`: Initializes the game screen, controls game logic, and runs the main loop.

Perfect for beginners learning Python OOP and basic game development using turtle graphics.

Author: Sharon George K
"""
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong_game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >288 or ball.ycor()<-288:
         ball.bounce_y()

    #Detect collison with right paddle

    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() > -330 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
