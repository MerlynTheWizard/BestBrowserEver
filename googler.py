import webbrowser
import random
from tkinter import *

def browser():
    textInput = textBox.get(1.0, "end-1c")
    replaceSpace = textInput.replace(" ", "+")
    replaceAmpersand = replaceSpace.replace("&", "and")
    const = "https://google.com/search?q="
    fullLink = const+replaceAmpersand
    f = random.randint(1,5)


    if f == 3: 
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ")

    else: 
        webbrowser.open(fullLink)


window = Tk()

window.title("BestBrowserEver v0.0.2")

window.geometry("720x480")
window.configure(bg="#202124")

header = Label(window, text = "What would you like to find out?" )
header.config(fg="white", bg="#202124")
header.config(font=('Helvatical bold',20))

subHeader = Label(window, text = "Enter your text above, and hit the Go! button below to search!")
subHeader.config(fg="white", bg="#202124")
subHeader.config(font=('Helvatical bold',10))

textBox = Text(window)

button = Button(window, text = "Go!", command= browser)

header.pack()
textBox.pack()
subHeader.pack()
button.pack()

window.mainloop()