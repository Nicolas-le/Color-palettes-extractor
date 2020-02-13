import colorAnalysis
import os
from tkinter import *
from tkinter import filedialog


class Gui:
    def __init__(self,master):

        self.master = master
        master.title("color analytics")

        frame = Frame(master, relief="ridge", borderwidth=3, bg= "white")                                   #master frame
        frame.pack(fill="both",expand=50)

        self.label = Label(frame, bg="white", text="You want to analyse?")
        self.label.pack(expand=5)

        self.button = Button(frame, text="run",command=lambda: showColor())                                    #button with lambda to execute only when pressed
        self.button.pack(side="top")                                                                        #output function is running


        def output():
            T = Text(frame, height=10, width=100)                                           #output function that runs the color fuction
            T.pack()
            T.insert(END, colorAnalysis.howmany() + " The most used colors are:\n")
            T.insert(END, colorAnalysis.berechne())

        def createRectangle(a):                                                                             #Erzeugt farbige Rechtecke per Canvas mit dem übergebenen hex code a
            w = Canvas(frame, width=50, height=50)
            w.pack()
            w.create_rectangle(0, 0, 50, 50, fill= a)

        def showColor():                                                                                    #zeigt aktuell 5 Farben
            rounds = 5
            for i in range(rounds):
                createRectangle(colorAnalysis.readList(i))                                                     #ruft die Auslesefunktion auf, welche die Bilder auswertet


    def setPath():                                                                                          #returned Verzeichnis als String
        filename = filedialog.askdirectory()
        return filename

if __name__ == "__main__":

    root = Tk()                                                                                                 #root refers to Tk()
    folder_path = StringVar()
    os.chdir(Gui.setPath())                                                                                     #belegt den Pfad des Ordners mit setPath()
    my_gui = Gui(root)                                                                                          #instance of frame
    root.mainloop()