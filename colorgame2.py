# Mini Project
# COLOR GAME
# 609 Monali Borekar
# 611 Felicia Carvalho
# 613 Charu Tiwari
# 614 Vedika Chavan

from tkinter import *#importing tkinter
import tkinter.font as font
import random#importing random

#list to store colors
colors = ["Red", "White", "Black", "Green", "Blue", "Purple", "Cyan", "Yellow", "Pink"]

#global variables
timer = 30  #timer
score = 0   #score
displayed_word_color = ''  #displaying words

#This fuction will be called when start button is clicked
def startGame():
    global displayed_word_color

    if(timer == 30):
        startCountDown() #calling startCountDown to start the countdown
        displayed_word_color = random.choice(colors).lower() #changes the word on screen
        display_words.config(text=random.choice(colors), fg=displayed_word_color) #changes color of text on screen
        color_entry.bind('<Return>', displayNextWord) #on tapping enter, next word is displayed

#This function is to reset the game
def resetGame():
    global timer, score, displayed_word_color
    timer = 30 #initializing score to 30 sec
    score = 0  #initial score is zero
    displayed_word_color = ''
    game_score.config(text = "Your Score : " + str(score)) #displaying score
    display_words.config(text = '')
    time_left.config(text="Game Ends in : -") #show remaining time
    color_entry.delete(0, END) #clears the entry widget

#This function will start count down
def startCountDown():
    global timer
    if(timer >= 0):#till timer is greater or equal to 0
        time_left.config(text = "Game Ends in : " + str(timer) + "s") #sow remaining time
        timer -= 1 #decrement timer by 1 sec
        time_left.after(1000,startCountDown) #function call(1000ms)
        if (timer == -1): #time over
            time_left.config(text="Game Over!!!")

#This function to display random words
def displayNextWord(event):
    global displayed_word_color
    global score
    if(timer > 0):
        if(displayed_word_color == color_entry.get().lower()):
            score += 1  #increment score
            game_score.config(text = "Your Score : " + str(score))#show score
        color_entry.delete(0, END) 
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text = random.choice(colors), fg = displayed_word_color)

my_window = Tk()
my_window.title("Color Game")#Title
my_window.geometry("500x200")#geometry

app_font = font.Font(family='Helvetica', size = 12)#font

game_desp = "Game Description: Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself"
myFont = font.Font(family='Helvetica') #game description

game_description = Label(my_window, text = game_desp, font = app_font, fg= "grey")
game_description.pack()

game_score = Label(my_window, text = "Your Score : " + str(score), font = (font.Font(size=16)), fg = "green")
game_score.pack()#label for score

display_words = Label(my_window , font = (font.Font(size=28)), pady = 10)
display_words.pack() 

#label for time left
time_left = Label(my_window, text = "Game Ends in : -", font = (font.Font(size=14)), fg = "orange")
time_left.pack()

color_entry = Entry(my_window, width = 30)
color_entry.pack(pady = 10)

btn_frame = Frame(my_window, width= 80, height = 40, bg= 'red')
btn_frame.pack(side = BOTTOM)

#Start button
start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "pink", bd = 0,padx = 20, pady = 10 , command = startGame)
start_button.grid(row=0, column= 0)

#Reset button
reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "light blue", bd = 0,padx = 20, pady = 10 , command = resetGame)
reset_button.grid(row=0, column= 1)

my_window.geometry('600x300')
my_window.mainloop()#run the event