import random
from turtle import Turtle, Screen

is_race_on = False
bet_again = True
winner = ""

canvas = Screen()

screen_width = 500
screen_height = 400
canvas.setup(width = screen_width, height = screen_height)

bot_list = []
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [90, 60, 30, 0, -30, -60, -90]

while bet_again:
    user_bet = canvas.textinput(title="Make a bet", prompt="Which turtle is gonna win? Enter color: ")
    for turtle_index in range(7):
        bot = Turtle(shape = "turtle")
        bot_color = random.choice(colors)
        colors.remove(bot_color)
        bot.color(bot_color)
        bot.penup()
        bot.goto(x = -230, y = y_positions[turtle_index])
        bot_list.append(bot)

    if user_bet:
        is_race_on = True
    """
    Size of turtle is 40X40 pixels, so finish line has to be 250-(40/2) == (canvawidth/2) - (40/2), here 230, as in turtle graphics 
    coordinates of the turtle are of its center. Logically for a finish line we need to map with coordinates of head at the end-point(here
    end of canvas).
    """
    while is_race_on:
        for turtle in bot_list:
            if turtle.xcor() >= 230:
                is_race_on = False
                winner = turtle.color()[0]
                canvas.clearscreen()
            random_distance = random.randint(0,10)
            turtle.fd(random_distance)
    
    colors += ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    bot_list = []
    
    if user_bet.lower() == winner:
        print(f"The winner is {winner}. You win the bet, Lucky🤑")
    else:
        print(f"The winner is {winner}. You Lost the bet, Better Luck Next Time😭")

    play_again = canvas.textinput(title = "Continue Betting...", prompt = "Do you want to bet again? Yes or No")
    if play_again.lower() == "yes":
        bet_again = True
    else:
        bet_again = False
        canvas.bye()