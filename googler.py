import webbrowser
import random
a = input ("'What would you like to find out?' ")
b = a.replace(" ", "+")
c = b.replace("&", "and")
d = "https://google.com/search?q="
e = d+c
f = random.randint(1,5)
print (f)
if f == 3: 
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
else: 
    print (e)
    webbrowser.open(e)
g = input("Open the above link, and press a key to close this window. ")