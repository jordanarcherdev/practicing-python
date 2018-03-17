import tkinter

okToPressReturn = True

hunger = 100
day = 0

def startGame(event):

    global okToPressReturn

    if okToPressReturn == False:
        pass

    else:
        startLabel.config(text="")
        updateHunger()
        updateDay()
        updateDisplay()

        okToPressReturn = False

def updateDisplay():

    global hunger
    global day

    if hunger <= 50:
        catPic.config(image = hungryphoto)
    else:
        catPic.config(image = normalphoto)

    hungerLabel.config(text="Hunger: " + str(hunger))
    dayLabel.config(text="Day: " + str(day))
    catPic.after(100, updateDisplay)

def updateHunger():

    global hunger
    hunger -= 1

    if isAlive():
        hungerLabel.after(500, updateHunger)

def updateDay():

    global day
    day += 1

    if isAlive():
        dayLabel.after(5000, updateDay)

def feed():

    global hunger

    if isAlive():
        if hunger <= 95:
            hunger += 20
        else:
            hunger -= 20

def isAlive():

    global hunger

    if hunger <= 0:
        startLabel.config(text="GAME OVER! YOU KILLED IT")
        return False
    else:
        return True

root = tkinter.Tk()
root.title("Keep Kitty Alive")
root.geometry("500x300")

startLabel = tkinter.Label(root, text="Press enter to start! ", font=('Helvetica',12))
startLabel.pack()

hungerLabel = tkinter.Label(root, text="Hunger: " + str(hunger), font=('Helvetica',12))
hungerLabel.pack()

dayLabel = tkinter.Label(root, text="Day: " + str(day), font=('Helvetica'))
dayLabel.pack()

hungryphoto = tkinter.PhotoImage(file="hungry.gif")
normalphoto = tkinter.PhotoImage(file="normal.gif")

catPic = tkinter.Label(root, image=normalphoto)
catPic.pack()

btnFeed = tkinter.Button(root, text="Feed Me", command=feed)
btnFeed.pack()

root.bind('<Return>', startGame)

root.mainloop()
