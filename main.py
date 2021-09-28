import tkinter as tk
from tkinter import *

class startApp:
    def __init__(self, root):
        self.root = root
        self.titleText = Label(text='Simple Cellular Automata', font=("Courier", 24), bg='lightblue')
        self.titleText.pack()
        self.labelOne = Label(text='Width:', font='Courier', bg='lightblue')
        self.labelOne.pack()
        self.entryOne = Entry(bd=1, font='Courier')
        self.entryOne.pack()
        self.labelTwo = Label(text='Height:', font='Courier', bg='lightblue')
        self.labelTwo.pack()
        self.entryTwo = Entry(bd=1, font='Courier')
        self.entryTwo.pack()
        self.labelThree = Label(text='Size of a square:', font='Courier', bg='lightblue')
        self.labelThree.pack()
        self.entryThree = Entry(bd=1, font='Courier')
        self.entryThree.pack()
        self.defButton = Button(text='Default settings', command=lambda: self.setDefContents())
        self.defButton.place(x=195, y=210, height=30, width=100)
        self.newButton = Button(text='New automaton', command=lambda: self.makeNewAuto(Automata))
        self.newButton.place(x=305, y=210, height=30, width=100)
        self.labelFour = Label(font=('Courier', 10), bg='lightblue')
        self.labelFour.place(y=240)
        self.labelFive = Label(text='Press Enter to step to next generation', font=('Courier', 10), bg='lightblue')
        self.labelFive.place(y=260)
        self.max_value = 20
        self.min_value = 5
    def setDefContents(self):
        self.entryOne.delete(0, 'end')
        self.entryTwo.delete(0, 'end')
        self.entryThree.delete(0, 'end')
        self.entryOne.insert(0, '10')
        self.entryTwo.insert(0, '10')
        self.entryThree.insert(0, '50')
    def makeNewAuto(self, _class):
        self.xCellCount = self.entryOne.get()
        self.yCellCount = self.entryTwo.get()
        self.cellSize = self.entryThree.get()
        if self.xCellCount.isdigit() and self.yCellCount.isdigit() and self.cellSize.isdigit():
            self.labelFour['text'] = ''
            self.xCellCount = int(self.xCellCount)
            self.yCellCount = int(self.yCellCount)
            self.cellSize = int(self.cellSize)
            try:
                if self.new.state() == "normal":
                    self.new.focus()
            except:
                self.new = tk.Toplevel(self.root)
                _class(self.new, max(min(self.xCellCount, self.max_value), self.min_value), max(min(self.yCellCount, self.max_value), self.min_value), self.cellSize)
        else:
            self.labelFour['text'] = 'Please only enter NUMBERS!'

class Automata:
    def __init__(self, root, xCellCount, yCellCount, cellSize):
        self.onScreen = []
        self.nextOnScreen = []
        self.neighbours = []
        self.buttons = []
        self.death = True
        self.syntaxErrorFixer = 0
        self.root = root
        self.root.title('New Cellular Automaton')
        self.xCellCount = int(xCellCount)
        self.yCellCount = int(yCellCount)
        self.cellSize = int(cellSize)
        self.windowX = self.xCellCount*self.cellSize
        self.windowY = self.yCellCount*self.cellSize
        self.root.geometry(str(self.windowX) + 'x' + str(self.windowY))
        self.root.resizable(width=0, height=0)
        self.root.focus()
        self.root.bind('<Return>', self.step)
        self.makeData()
        self.drawGrid()
    def makeData(self):
        self.makeOnScreen()
        self.makeNextOnScreen()
        self.makeNeighbours()
        self.printData()
    def makeOnScreen(self):
        self.onScreen=[]
        for i in range(0, self.yCellCount, 1):
            self.onScreen.append([])
            for j in range(0, self.xCellCount, 1):
                self.onScreen[i].append(0)
    def makeNextOnScreen(self):
        self.nextOnScreen=[]
        for i in range(0, self.yCellCount, 1):
            self.nextOnScreen.append([])
            for j in range(0, self.xCellCount, 1):
                self.nextOnScreen[i].append(0)
    def makeNeighbours(self):
        self.neighbours=[]
        for i in range(0, self.yCellCount, 1):
            self.neighbours.append([])
            for j in range(0, self.xCellCount, 1):
                self.neighbours[i].append(0)
    def drawGrid(self):
        for i in range(0, self.yCellCount, 1):
            self.buttons.append([])
            for j in range(0, self.xCellCount, 1):
                self.createMyButton(i, j)
    def createMyButton(self, i, j):
        yCoord = i*self.cellSize
        xCoord = j*self.cellSize
        b = tk.Button(self.root, text='')
        b['command']= lambda: self.switchCol(b, i, j)
        self.assignBg(b, i, j)
        b.pack()
        b.place(height=self.cellSize, width=self.cellSize, x=xCoord, y=yCoord)
        self.buttons[i].append(b)
    def switchCol(self, button, i, j):
        if self.onScreen[i][j] == 0:
            self.onScreen[i][j] = 1
        elif self.onScreen[i][j] == 1:
            self.onScreen[i][j] = 0
        self.assignBg(button, i , j)
    def assignBg(self, button, i, j):
        if self.onScreen[i][j] == 0:
            bgCol = 'white'
        elif self.onScreen[i][j] == 1:
            bgCol = 'black'
        button.configure(bg=bgCol)
    def printData(self):
        print('OnScreen:')
        for i in range(0, len(self.onScreen), 1):
            print(self.onScreen[i])
        print('NextOnScreen:')
        for i in range(0, len(self.nextOnScreen), 1):
            print(self.nextOnScreen[i])
        print('Neighbours:')
        for i in range(0, len(self.neighbours), 1):
            print(self.neighbours[i])
        print('')
    def neighbourCounter(self, i, j):
        if i != 0:
            if j != 0:
                try:
                    if self.onScreen[i-1][j-1] == 1:
                        self.neighbours[i][j] += 1
                except:
                    self.syntaxErrorFixer = 0 #replacing this with a comment or removing "except" causes errors, however the "try"ing operation might fail
            try:
                if self.onScreen[i-1][j] == 1:
                    self.neighbours[i][j] += 1
            except:
                self.syntaxErrorFixer = 0
            try:
                if self.onScreen[i-1][j+1] == 1:
                    self.neighbours[i][j] += 1
            except:
                self.syntaxErrorFixer = 0
        if j != 0:
            try:
                if self.onScreen[i][j-1] == 1:
                    self.neighbours[i][j] += 1
            except:
                self.syntaxErrorFixer = 0
        try:
            if self.onScreen[i][j+1] == 1:
                self.neighbours[i][j] += 1
        except:
            self.syntaxErrorFixer = 0
        if j != 0:
            try:
                if self.onScreen[i+1][j-1] == 1:
                    self.neighbours[i][j] += 1
            except:
                self.syntaxErrorFixer = 0
        try:
            if self.onScreen[i+1][j] == 1:
                self.neighbours[i][j] += 1
        except:
            self.syntaxErrorFixer = 0
        try:
            if self.onScreen[i+1][j+1] == 1:
                self.neighbours[i][j] += 1
        except:
            self.syntaxErrorFixer = 0
    def step(self, event):
        self.makeNeighbours()
        for i in range(0, len(self.onScreen), 1):
            for j in range(0, len(self.onScreen[i]), 1):
                self.neighbourCounter(i, j)
        for i in range(0, len(self.onScreen), 1):
            for j in range(0, len(self.onScreen[i]), 1):
                self.genStepper(i, j)
        self.onScreen = self.nextOnScreen
        self.makeNextOnScreen()
        self.massAssignBg()
        self.printData()
    def genStepper(self, i, j):
        if self.onScreen[i][j] == 0:
            #dead
            if self.neighbours[i][j] == 3:
                self.nextOnScreen[i][j] = 1
                #now it lives!
            else:
                #it shouldnt get here, but to be sure..
                self.nextOnScreen[i][j] = 0
        if self.onScreen[i][j] == 1:
            if self.death == True:
                #lives
                if self.neighbours[i][j] == 2:
                    self.nextOnScreen[i][j] = 1
                    #survives
                elif self.neighbours[i][j] == 3:
                    self.nextOnScreen[i][j] = 1
                    #survives
                else:
                    self.nextOnScreen[i][j] = 0
                    #dies :(
            else:
                self.nextOnScreen[i][j] = 1
    def massAssignBg(self):
        for i in range(0, len(self.onScreen), 1):
            for j in range(0, len(self.onScreen[i]), 1):
                if self.onScreen[i][j] == 0:
                    bgCol = 'white'
                elif self.onScreen[i][j] == 1:
                    bgCol = 'black'
                self.buttons[i][j].configure(bg=bgCol)
root = Tk()
root.geometry("600x300")
root.resizable(width=0, height=0)
root.title('SCA')
root['bg']='lightblue'

startApp = startApp(root)

root.mainloop()