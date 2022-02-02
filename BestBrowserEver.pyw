from sqlite3 import Row
from turtle import position
import webbrowser
import random
#from tkinter import *
import tkinter as tk
import nltk
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import time

loadedText = ''
pulledText = ''
formattedHtml = ''






class error():

        def urlError():
                errorWindow = tk.Toplevel()
                errorWindow.title("Error")

                windowWidth = errorWindow.winfo_reqwidth()
                windowHeight = errorWindow.winfo_reqheight()
                positionRight = int(errorWindow.winfo_screenwidth()/2 - windowWidth/2)
                positionDown = int(errorWindow.winfo_screenheight()/2 - windowHeight/2)
                errorWindow.geometry("+{}+{}".format(positionRight, positionDown))
                errorWindow.resizable(False, False)

                errorMessageHeader = tk.Label(errorWindow, text = "URL Error!", pady=5)
                errorMessageHeader.config(font=('Helvatical bold',15))
                errorMessageHeader.pack()

                errorMessageBody = tk.Label(errorWindow, text = " It looks like you've entered an invalid URL. \nPlease enter a valid URL and try again.", pady=5)
                errorMessageBody.config(font=('Grotesk', 10))
                errorMessageBody.pack()

                closeButton = tk.Button(errorWindow, text="OK", command=errorWindow.destroy)
                closeButton.pack(pady=15)
        
        def jokeError(errorHeader, errorBody, buttonText1, buttonText2):
                errorWindow = tk.Toplevel()
                errorWindow.title(errorHeader)

                x = random.randint(1, 2560)
                y = random.randint(1, 1440)
                
                errorWindow.geometry("+{}+{}".format(x, y))
                errorWindow.resizable(False, False)

                errorMessageHeader = tk.Label(errorWindow, text = errorHeader, pady=5)
                errorMessageHeader.config(font=('Helvatical bold',15))
                errorMessageHeader.grid(column=1, row=0, columnspan=2)

                errorMessageBody = tk.Label(errorWindow, text = errorBody, pady=5)
                errorMessageBody.config(font=('Grotesk', 10))
                errorMessageBody.grid(column=1, row=1, columnspan=2)

                closeButton1 = tk.Button(errorWindow, text=buttonText1, command=errorWindow.destroy)
                closeButton1.grid(pady=15, column=1, row=2)

                closeButton2 = tk.Button(errorWindow, text=buttonText2, command=errorWindow.destroy)
                closeButton2.grid(pady=15, column=2, row=2)





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
        


##inserts history
def insert():
        history.delete(1.0, tk.END)
        history.insert(1.0, pulledText)

##the first load of the history
def loadHistory():
        pullHistory()
        history.insert(1.0, pulledText)


def htmlFormatter(fullLink):
        global formattedHtml
        req = urllib.request.Request(fullLink, headers={'User-Agent': 'Mozilla/5.0'})
        try:
                rawHtml = urllib.request.urlopen(req,timeout=2).read()
        except urllib.error.URLError as e: error.urlError()
        souped = BeautifulSoup(rawHtml, features="html.parser")
        for script in souped(["script", "style"]):
                script.extract()
        soupedHtml = souped.get_text()
        linedHtml = (line.strip() for line in soupedHtml.splitlines())
        chunkedHtml = (phrase.strip() for line in linedHtml for phrase in line.split("  "))
        formattedHtml = '\n \n'.join(chunk for chunk in chunkedHtml if chunk)



##pulls and displays HTML of search into BestBrowserEver
def loadBrowser(fullLink):
        const = ["https://", "http://"]
        if any(const in fullLink for const in const ): htmlFormatter(fullLink)
        elif "www." in fullLink: 
                        fullLink = "https://" + fullLink
                        htmlFormatter(fullLink)
        #try:
                #if any(const in fullLink for const in const ): htmlFormatter(fullLink)
                #elif "www." in fullLink: 
                        #fullLink = "https://" + fullLink
                        #htmlFormatter(fullLink)
                #else: error.urlError()

        #except: error.urlError()
        
        ##formattedHtml = nltk.clean_html(rawHtml)
        #htmlFormatter(fullLink)
        browserBox.insert(1.0, formattedHtml)


##pulls and formats text entry, and opens web browser with link
def searchBar():
    textInput = searchBox.get(1.0, "end-1c")
    replaceSpace = textInput.replace(" ", "+")
    replaceAmpersand = replaceSpace.replace("&", "and")
    textToSave = textInput
    saveText(textToSave)
    #addHistory(textToSave)
    #const = "https://google.com/search?q="
    const = ""
    fullLink = const+replaceAmpersand
    f = random.randint(1,100)
    historyUpdate(textToSave)
    if f == 100: 
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
            for x in range(1,300):
                error.jokeError("lol", "get rick rolled", "yes", "no")
    else:
            loadBrowser(fullLink)
                 #try:
                        #loadBrowser(fullLink)

                 #except:
                         #error.urlError()  
        #webbrowser.open(fullLink)

##clears history
def clearHistory():
        history.delete(1.0, tk.END)
        with open('history.txt', 'w') as clear:
                pass


##window config
window = tk.Tk()

window.title("BestBrowserEver v0.1.1")

window.geometry("1920x1080")
window.resizable(False, False)
window.configure(bg="#202124")


##header label config
header = tk.Label(window, text = "Welcome to BestBrowserEver!" )
header.config(fg="white", bg="#202124")
header.config(font=('Helvatical bold',20))
header.grid(column=2, row=0)


##subheader label config
subHeader = tk.Label(window, text = "Enter a URL above and hit the Go! button below to load a website!")
subHeader.config(fg="white", bg="#202124")
subHeader.config(font=('Helvatical bold',10))
subHeader.grid(column=2, row=4)


##history label config
historyHeader = tk.Label(window, text = "Your search history:")
historyHeader.config(fg="white", bg="#202124")
historyHeader.config(font=('Helvatical bold',10))
historyHeader.grid(column=4, row=0)


##history text box config
history = tk.Text(window, wrap=tk.WORD)
history.config(wrap=tk.WORD)
history.config(height=60, width=30)
history.grid(column=4, row=1)
history.insert(1.0, pulledText)


##loads history
loadHistory()


##tries to load last serach term into search box, and search box config
load()
if load() == True:
        searchBox = tk.Text(window)
        searchBox.config(height=1, width=135)
        searchBox.grid(column=2, row=2)
        searchBox.insert(1.0, loadedText) 
else: searchBox = tk.Text(window)
searchBox.config(wrap=tk.WORD)
searchBox.grid(column=2, row=3)





##main browser window & scroll bar config
scrollbar = tk.Scrollbar(window, orient='vertical')
browserBox = tk.Text(window, yscrollcommand=scrollbar.set)
scrollbar.config(command=browserBox.yview)
scrollbar.grid(column=3, row=1, sticky=tk.N+tk.S)
browserBox.config(wrap=tk.WORD, bg='#666464', fg='white')
browserBox.config(height=60, width=205)
browserBox.grid(column=2, row=1, columnspan=1)




##button configs
button = tk.Button(window, text = "Go!", command= searchBar)
button.grid(column=2, row=5)

clearHistory = tk.Button(window, text = "Clear", command= clearHistory)
clearHistory.grid(column=4, row=3)

##header.pack()
##history.pack()
##textBox.pack()
##subHeader.pack()
##button.pack()


window.mainloop()