from tkinter import *
import wikipedia
import wolframalpha

import speech_recognition
import pyttsx

root = Tk()
root.title("Python Virtual Assistant")

def retrive_input(event =None):
    inputx = textBox.get("1.0" , "end-1c")
    tex = Text()
    try:
        app_id='R57UY3-QHE4A3G4WK'
        client = wolframalpha.Client(app_id)
        res = client.query(inputx)
        answer = next(res.results).text
        tex.insert(END, answer)
        tex.see(END)
        tex.pack()
        
    except:
        inputx = list(inputx.strip().split(" "))
        inputx = inputx[2:]
        result = wikipedia.summary(''.join(inputx) , sentences = 4)
        tex.insert(END, answer)
        tex.see(END)
        tex.pack()
    
textBox =Text(root , height=2 , width=40)
textBox.bind('<Return>' , retrive_input)
textBox.pack()

buttonCommit = Button(root , height = 2 , width =10 , text = "Commit",  command = lambda : retrive_input())
buttonCommit.pack()

mainloop()


