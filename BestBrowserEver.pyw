import webbrowser
import random
from tkinter import *

loadedText = ''
pulledText = ''

##saves your most recent search for the next time you open the app
def saveText(textToSave):
        with open('save.txt', 'w+') as save:
                save.write(textToSave)


##tries to load any saved text
def load():
        global loadedText
        try:
                with open('save.txt', 'r') as load:
                        loadedText = load.read()
                        return True
        except:
                return False

##adds to your history 
def addHistory(textToSave):
        with open('history.txt', 'a') as history:
                history.write("\n")
                history.write(textToSave)


##tries to pull history
def pullHistory():
        global pulledText
        try:
                with open('history.txt', 'r') as pull:
                        pulledText = pull.read()
                        return True
        except:
                return False


##updates history in the app
def historyUpdate(textToSave):
        with open('history.txt', 'a') as history:
                history.write("\n")
                history.write(textToSave)
        pullHistory()
        insert()
        #history.delete(1.0, END)
        #history.insert(1.0, pulledText)
        

def insert():
        history.delete(1.0, END)
        history.insert(1.0, pulledText)

##the first load of the history
def loadHistory():
        pullHistory()
        history.insert(1.0, pulledText)

##pulls and formats text entry, and opens web browser with link
def browser():
    textInput = textBox.get(1.0, "end-1c")
    replaceSpace = textInput.replace(" ", "+")
    replaceAmpersand = replaceSpace.replace("&", "and")
    textToSave = textInput
    saveText(textToSave)
    #addHistory(textToSave)
    const = "https://google.com/search?q="
    fullLink = const+replaceAmpersand
    f = random.randint(1,5)
    historyUpdate(textToSave)


    if f == 3: 
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ")

    else: 
        webbrowser.open(fullLink)


def clearHistory():
        history.delete(1.0, END)
        with open('history.txt', 'w') as clear:
                pass

window = Tk()

window.title("BestBrowserEver v0.1.1")

window.geometry("780x480")
window.configure(bg="#202124")

header = Label(window, text = "What would you like to find out?" )
header.config(fg="white", bg="#202124")
header.config(font=('Helvatical bold',20))
header.grid(column=1, row=0)

subHeader = Label(window, text = "Enter your text above, and hit the Go! button below to search!")
subHeader.config(fg="white", bg="#202124")
subHeader.config(font=('Helvatical bold',10))
subHeader.grid(column=1, row=2)

historyHeader = Label(window, text = "Your search history:")
historyHeader.config(fg="white", bg="#202124")
historyHeader.config(font=('Helvatical bold',10))
historyHeader.grid(column=2, row=0)

history = Text(window)
history.config(height=24, width=14)
history.grid(column=2, row=1)
history.insert(1.0, pulledText)

loadHistory()

load()
if load() == True:
        textBox = Text(window)
        textBox.grid(column=1, row=0)
        textBox.insert(1.0, loadedText) 
else: textBox = Text(window)
textBox.grid(column=1, row=1)

button = Button(window, text = "Go!", command= browser)
button.grid(column=1, row=3)

clearHistory = Button(window, text = "Clear", command= clearHistory)
clearHistory.grid(column=2, row=2)

##header.pack()
##history.pack()
##textBox.pack()
##subHeader.pack()
##button.pack()


window.mainloop()