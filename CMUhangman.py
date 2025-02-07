import random

Rect(0,0,400,400, fill=rgb(240,255,240))
Label('HANGMAN',200,30, font="monospace", size = 35)

# messages
welcome=Group(
    Label("Welcome to Hangman!", 200, 255, size= 13, font = "montserrat"),
    Label("You have to guess the mystery word in 5 guesses or less.", 200, 270, size = 13, font="montserrat")
    )
welcome.visible = True
correct = Label("THAT IS CORRECT!", 200, 285, font="montserrat", visible = False)
incorrect = Label("THAT IS INCORRECT", 200, 288, font="montserrat", visible = False)
won = Label("yay YOU WON", 200, 280, font = "montserrat", size=17, visible = False)
lost = Label("oh no YOU LOST", 200, 280, font = "montserrat", size=17, visible = False)
answerWas = Label("The word was", 200, 315, font = "montserrat", size=13, visible = False)

#rod
rod1 = Line(0, 55, 200, 55, lineWidth = 4)
rod2 = Line(200, 53, 200, 75, lineWidth = 4)
# hangman       
head = Circle(200,105,30, fill= None, borderWidth= 2, border='black', visible = False)
body = Line(200, 135, 200,205, visible = False)
arm1 = Line(175,175,200,150, visible = False)
arm2 = Line(225, 175, 200, 150, visible = False)
leg1 = Line(200, 205, 175, 235, visible = False)
leg2 = Line(200,205,225,235, visible = False)

#word graphic
wordLine3 = Line(175,370,225,370)
wordLine2 = Line(110,370,165,370)
wordLine1 = Line(50,370,100,370)
wordLine4 = Line(235,370,290,370)
wordLine5 = Line(300,370,350,370)

correctLetters = []
inputLetters = []

wordList = ["ARISE", "HONEY", "COMET", "FLARE", "GLOBE"]
randomWord = random.choice(wordList)
correctLetters = list(randomWord)

letter1 = Label(correctLetters[0], 75, 355, size = 30, font = "monospace", visible = False)
letter2 = Label(correctLetters[1], 137, 355, size = 30, font = "monospace", visible = False)
letter3 = Label(correctLetters[2], 200, 355, size = 30, font = "monospace", visible = False)
letter4 = Label(correctLetters[3], 260, 355, size = 30, font = "monospace", visible = False)
letter5 = Label(correctLetters[4], 325, 355, size = 30, font = "monospace", visible = False)

correctLabels = [letter1, letter2, letter3, letter4, letter5]

guessNumber = 5
correctCount = 0
wrongCount = 0
correctGuess = False
guessesLeft = Label("You have " + str(guessNumber) + " guesses", 200, 300, font = "montserrat")
inputtedLetters = Label("Here are the letters you have guessed so far: " + " ".join(inputLetters), 200, 315, font = "montserrat")

while guessNumber >= 1:
    userInput = app.getTextInput("What letter do you want to guess?").upper()
    welcome.visible = False
    guessNumber -= 1
    guessesLeft.value = "You have " + str(guessNumber) + " guesses left"
    inputLetters.append(userInput)
    inputLetters.sort()
    inputtedLetters.value = "Here are the letters you have guessed so far: " + " ".join(inputLetters)
    for letter in correctLabels:
        if letter.value == userInput:
            letter.visible = True
            correct.visible = True
            incorrect.visible = False
            correctCount += 1
            correctGuess = True
            break
        else:
            incorrect.visible = True
            correct.visible = False
    if correctGuess == False:
        wrongCount += 1
        if wrongCount == 1:
            head.visible = True
        elif wrongCount == 2:
            body.visible = True
        elif wrongCount == 3:
            arm1.visible = True
        elif wrongCount == 4:
            arm2.visible = True
        elif wrongCount == 5:
            leg2.visible = True
            leg1.visible = True
    correctGuess = False
                
correct.visible = False
incorrect.visible = False
guessesLeft.visible = False
inputtedLetters.visible = False
            
if correctCount == len(randomWord):
    won.visible = True
else:
    lost.visible = True
    answerWas.visible = True
    letter1.visible = True
    letter2.visible = True
    letter3.visible = True
    letter4.visible = True
    letter5.visible = True
    
