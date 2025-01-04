
import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right paddle (computer controlled)
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Scoreboard
left_score = 0
right_score = 0
scoreboard = turtle.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))

# Move the left paddle
def move_left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += 20
    left_paddle.sety(y)

def move_left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        y -= 20
    left_paddle.sety(y)

# Keyboard bindings for left paddle
screen.listen()
screen.onkey(move_left_paddle_up, "w")
screen.onkey(move_left_paddle_down, "s")

# Move the ball and check for collisions
def move_ball():
    global left_score, right_score

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with top and bottom walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball collision with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Ball out of bounds
    if ball.xcor() > 390:
        left_score += 1
        update_scoreboard()
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        right_score += 1
        update_scoreboard()
        ball.goto(0, 0)
        ball.dx *= -1

    # Move the right paddle (AI)
    if right_paddle.ycor() < ball.ycor() and abs(right_paddle.ycor() - ball.ycor()) > 10:
        right_paddle.sety(right_paddle.ycor() + 1)
    elif right_paddle.ycor() > ball.ycor() and abs(right_paddle.ycor() - ball.ycor()) > 10:
        right_paddle.sety(right_paddle.ycor() - 1)

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Left: {left_score}  Right: {right_score}", align="center", font=("Courier", 24, "normal"))

# Main game loop
while True:
    screen.update()
    move_ball()

import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right paddle (computer controlled)
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Scoreboard
left_score = 0
right_score = 0
scoreboard = turtle.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))

# Move the left paddle
def move_left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += 20
    left_paddle.sety(y)

def move_left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        y -= 20
    left_paddle.sety(y)

# Keyboard bindings for left paddle
screen.listen()
screen.onkey(move_left_paddle_up, "w")
screen.onkey(move_left_paddle_down, "s")

# Move the ball and check for collisions
def move_ball():
    global left_score, right_score

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with top and bottom walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Ball collision with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Ball out of bounds
    if ball.xcor() > 390:
        left_score += 1
        update_scoreboard()
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        right_score += 1
        update_scoreboard()
        ball.goto(0, 0)
        ball.dx *= -1

    # Move the right paddle (AI)
    if right_paddle.ycor() < ball.ycor() and abs(right_paddle.ycor() - ball.ycor()) > 10:
        right_paddle.sety(right_paddle.ycor() + 1)
    elif right_paddle.ycor() > ball.ycor() and abs(right_paddle.ycor() - ball.ycor()) > 10:
        right_paddle.sety(right_paddle.ycor() - 1)

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Left: {left_score}  Right: {right_score}", align="center", font=("Courier", 24, "normal"))

# Main game loop
while True:
    screen.update()
    move_ball()