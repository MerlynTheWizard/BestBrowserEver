import webbrowser
import random
from tkinter import *

loadedText = ''

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

##pulls and formats text entry, and opens web browser with link
def browser():
    textInput = textBox.get(1.0, "end-1c")
    replaceSpace = textInput.replace(" ", "+")
    replaceAmpersand = replaceSpace.replace("&", "and")
    textToSave = textInput
    saveText(textToSave)
    const = "https://google.com/search?q="
    fullLink = const+replaceAmpersand
    f = random.randint(1,5)


    if f == 3: 
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ")

    else: 
        webbrowser.open(fullLink)



window = Tk()

window.title("BestBrowserEver v0.0.3")

window.geometry("720x480")
window.configure(bg="#202124")

header = Label(window, text = "What would you like to find out?" )
header.config(fg="white", bg="#202124")
header.config(font=('Helvatical bold',20))

subHeader = Label(window, text = "Enter your text above, and hit the Go! button below to search!")
subHeader.config(fg="white", bg="#202124")
subHeader.config(font=('Helvatical bold',10))

load()
if load() == True:
        textBox = Text(window, )
        textBox.insert(1.0, loadedText) 
else: textBox = Text(window)

button = Button(window, text = "Go!", command= browser)

header.pack()
textBox.pack()
subHeader.pack()
button.pack()

window.mainloop()