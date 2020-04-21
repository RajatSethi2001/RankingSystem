from graphics import *
import random

width = 800
height = 500
gap = 20
rectHeight = 100

fileName = input("Enter the file name: ");
try:
    myList = open(fileName, 'r')
except NameError:
    print("File name does not exist!");
    exit()
    


win = GraphWin("Ranking Simulator", width, height)
win.setBackground('white')
optionOne = Rectangle(Point(gap, gap), Point(width - gap, gap + rectHeight))
optionTwo = Rectangle(Point(gap, gap * 2 + rectHeight), Point(width - gap, gap * 2 + rectHeight * 2))
optionThree = Rectangle(Point(gap, gap * 3 + rectHeight * 2), Point(width - gap, gap * 3 + rectHeight * 3))

optionOne.setFill('green')
optionTwo.setFill('green')
optionThree.setFill('green')

optionOne.draw(win)
optionTwo.draw(win)
optionThree.draw(win)

TextOne = Text(Point(width / 2, gap + rectHeight / 2), '')
TextTwo = Text(Point(width / 2, gap * 2 + rectHeight * 1.5), 'Skip!')
TextThree = Text(Point(width / 2, gap * 3 + rectHeight * 2.5), '')

TextOne.setSize(18)
TextTwo.setSize(18)
TextThree.setSize(18)

TextOne.setStyle('bold')
TextTwo.setStyle('bold')
TextThree.setStyle('bold')

TextOne.draw(win)
TextTwo.draw(win)
TextThree.draw(win)

ExitSign = Rectangle(Point(width * 0.75, gap * 4 + rectHeight * 3), Point(width - gap, height - gap))
ExitSign.setFill('red')
ExitSign.draw(win)

ExitText = Text(Point((width * 0.75 + (width - gap)) / 2, (gap * 4 + rectHeight * 3 + height - gap) / 2), "RANK!")
ExitText.setSize(18)
ExitText.setFill('white')
ExitText.setStyle('bold')
ExitText.draw(win)

InstructText = Text(Point(width * 3 / 8, (gap * 4 + rectHeight * 3 + height - gap) / 2), "Select A Winner!")
InstructText.setSize(18)
InstructText.setStyle('bold')
InstructText.draw(win)

readList = myList.readlines()

for i in range(len(readList)):
    readList[i] = readList[i].replace('\n', '');
    
rankingList = readList.copy()
pointList = []

for i in range(len(readList)):
    pointList.append(0);

NotFinished = True

while(NotFinished):
    rankingList = readList.copy()
    while (len(rankingList) > 1):
        choiceOne = random.randint(0, len(rankingList) - 1)
        choiceOneName = rankingList[choiceOne]
        choiceOneIndex = readList.index(choiceOneName)
        rankingList.remove(choiceOneName)
    
        choiceTwo = random.randint(0, len(rankingList) - 1)
        choiceTwoName = rankingList[choiceTwo]
        choiceTwoIndex = readList.index(choiceTwoName)
        rankingList.remove(choiceTwoName)
        
        TextOne.setText(choiceOneName)
        #TextOne.draw(win)
        
        TextThree.setText(choiceTwoName)
        #TextThree.draw(win)
        
        NoOptionPicked = True
        while(NoOptionPicked):
            CP = win.getMouse()
            if (CP.getX() >= gap and CP.getX() <= width - gap and CP.getY() >= gap and CP.getY() <= gap + rectHeight):
                if (choiceOneIndex > choiceTwoIndex):
                    readList[choiceOneIndex] = choiceTwoName
                    readList[choiceTwoIndex] = choiceOneName
                NoOptionPicked = False
                
            elif (CP.getX() >= gap and CP.getX() <= width - gap and CP.getY() >= gap * 2 + rectHeight and CP.getY() <= gap * 2 + rectHeight * 2):
                NoOptionPicked = False
                
            elif (CP.getX() >= gap and CP.getX() <= width - gap and CP.getY() >= gap * 3 + rectHeight * 2 and CP.getY() <= gap * 3 + rectHeight * 3):
                if (choiceTwoIndex > choiceOneIndex):
                    readList[choiceOneIndex] = choiceTwoName
                    readList[choiceTwoIndex] = choiceOneName
                NoOptionPicked = False
                
            elif (CP.getX() >= width * 0.75 and CP.getX() <= width - gap and CP.getY() >= gap * 4 + rectHeight * 3 and CP.getY() <= height - gap):
                NoOptionPicked = False
                NotFinished = False
        
        if (NotFinished == False):
            win.close()
            break

output = open(fileName, 'w')

for i in range(len(readList)):
    rankStr = readList[i] + "\n"
    output.write(rankStr)

output.close()
myList.close()