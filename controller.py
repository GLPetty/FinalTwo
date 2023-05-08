# Import modules for UI and number generation
from PyQt5.QtWidgets import *
from view import *
import math
import random

# Line 9-10 for uniform display across devices
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    # Inititalization, UI setup, one global variable, 4 functional buttons (BASE STATE)
    def __init__(self, *args, **kwargs):
        # Global var bet provided to many functions, default setting as none
        global bet
        bet = 'none'
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.betTopButton.clicked.connect(self.betTop)
        self.betBottomButton.clicked.connect(self.betBottom)
        self.addCreditsButton.clicked.connect(self.addButtonCredits)
        self.playButton.clicked.connect(self.playAction)
        

    def addButtonCredits(self):
        # Add 5 credits button, can be clicked anytime, LCD display used for current credit count
        credits = self.creditCountLCD.intValue()
        credits = credits + 5
        self.creditCountLCD.display(credits)

        # Must select a top or bottom bet before PLAY button becomes functional
        if bet == 'top' or bet == 'bottom':
            self.playButton.setText('PLAY')
        else:
            self.playButton.setText('You must select a bet \n top or bottom')
        
    
    def changeCredits(self, newCredits):
        # Add/subtract credits, newCredits can be positive or negative (-1 for non-winning play)
        # Winning deals place amount won as newCredits argument
        credits = self.creditCountLCD.intValue()
        credits = newCredits + credits
        self.creditCountLCD.display(credits)


    def creditCheck(self):
        # If user credits = 0, screen is reverted to base state
        # Global bet used maintain PLAY button functionality
        global bet
        credits = self.creditCountLCD.intValue()
        if credits == 0:
            self.removeBottom()
            self.removeTop()
            self.clearCallNums()
            self.playButton.setText('Add credits to play!')
            bet = 'none'

    
    def playAction(self):
        # When play button is clicked, use global variable bet to process
        # Global bet determines top or bottom for comparison to called numbers
        topList = list(range(1,41))
        bottomList = list(range(41,81))

        # Random generated list of 20 call numbers within Keno range (1-80)
        callList = random.sample(range(1,81), 20)

        # Available credits retrieved from LCD display
        credits = self.creditCountLCD.intValue()

        # Establish int variable win at default 0
        win = 0

        # Establish int variable matches at default 0
        matches = 0

        # If credit is available, compare called numbers to user bet (top or bottom)
        # to determine winnings. Check credit upon completion, if 0, return UI to base state
        if credits > 0:
            if bet == 'top':
                self.changeCredits(-1)
                callBet = set(callList).intersection(topList)
                self.displayCallNums(callList, callBet)
                matches = len(callBet)
                self.winLoss(matches)
                self.creditCheck()

            elif bet == 'bottom':
                self.changeCredits(-1)
                callBet = set(callList).intersection(bottomList)
                self.displayCallNums(callList, callBet)
                matches = len(callBet)
                self.winLoss(matches)
                self.creditCheck()
            else:
                # If not bet estabished, PLAY button reminder to select bet
                self.playButton.setText('You must select a bet \n top or bottom')
        else:
            # If no credit available, PLAY button reminder to add credits
            self.playButton.setText('You need credits!')
        
    def winLoss(self, matches):
        # Make comparison of bet vs called numbers, use odds to determine winning, if any
        # Update total credits if win, display amount won to user via handWin label
        if matches == 0 or matches == 20:
            win = 12500
            self.handWin.setText(str(win))
            self.changeCredits(win)
        elif matches == 1 or matches == 19:
            win = 5000
            self.handWin.setText(str(win))
            self.changeCredits(win)
        elif matches == 2 or matches == 18:
            win = 492
            self.handWin.setText(str(win))
            self.changeCredits(win)
        elif matches == 3 or matches == 17:
            win = 122
            self.handWin.setText(str(win))
            self.changeCredits(win)
        elif matches == 4 or matches == 16:
            win = 28
            self.handWin.setText(str(win))
            self.changeCredits(win)
        elif matches == 5 or matches == 15:
            win = 11
            self.handWin.setText(str(win))
            self.changeCredits(win)
        elif matches == 6 or matches == 14:
            win = 3
            self.handWin.setText(str(win))
            self.changeCredits(win)
        elif matches == 7 or matches == 13:
            win = 2
            self.handWin.setText(str(win))
            self.changeCredits(win)
        elif matches == 12:
            win = 1
            self.handWin.setText(str(win))
            self.changeCredits(win)
        else:
            win = 0
            self.handWin.setText(str(win))

        
            
    def displayCallNums(self, callList, callBet):
        # Display randomly generated call numbers to numCall buttons via callList
        # If number is part of bet, numCall button turns blue.
        # If not part of bet, numCall button turns red.

        self.numCall1.setText(str(callList[0]))
        if callList[0] in callBet:
            self.numCall1.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall1.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall2.setText(str(callList[1]))
        if callList[1] in callBet:
            self.numCall2.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall2.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall3.setText(str(callList[2]))
        if callList[2] in callBet:
            self.numCall3.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall3.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall4.setText(str(callList[3]))
        if callList[3] in callBet:
            self.numCall4.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall4.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall5.setText(str(callList[4]))
        if callList[4] in callBet:
            self.numCall5.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall5.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall6.setText(str(callList[5]))
        if callList[5] in callBet:
            self.numCall6.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall6.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall7.setText(str(callList[6]))
        if callList[6] in callBet:
            self.numCall7.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall7.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall8.setText(str(callList[7]))
        if callList[7] in callBet:
            self.numCall8.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall8.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall9.setText(str(callList[8]))
        if callList[8] in callBet:
            self.numCall9.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall9.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall10.setText(str(callList[9]))
        if callList[9] in callBet:
            self.numCall10.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall10.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall11.setText(str(callList[10]))
        if callList[10] in callBet:
            self.numCall11.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall11.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall12.setText(str(callList[11]))
        if callList[11] in callBet:
            self.numCall12.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall12.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall13.setText(str(callList[12]))
        if callList[12] in callBet:
            self.numCall13.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall13.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall14.setText(str(callList[13]))
        if callList[13] in callBet:
            self.numCall14.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall14.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall15.setText(str(callList[14]))
        if callList[14] in callBet:
            self.numCall15.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall15.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall16.setText(str(callList[15]))
        if callList[15] in callBet:
            self.numCall16.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall16.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall17.setText(str(callList[16]))
        if callList[16] in callBet:
            self.numCall17.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall17.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall18.setText(str(callList[17]))
        if callList[17] in callBet:
            self.numCall18.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall18.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall19.setText(str(callList[18]))
        if callList[18] in callBet:
            self.numCall19.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall19.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        self.numCall20.setText(str(callList[19]))
        if callList[19] in callBet:
            self.numCall20.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        else:
            self.numCall20.setStyleSheet("QPushButton" "{" "background-color: red;" "}")
        
        
        
        

        
        
    def betTop(self):
        # Player bets top range (1-40), global variable bet changed
        global bet
        bet = 'top'

        # Check credit via credit LCD display
        # If no availble credits, PLAY button reminder to add credits
        credits = self.creditCountLCD.intValue()
        if credits > 0:
            self.playButton.setText('PLAY')
        else:
            self.playButton.setText('You need credits!')

        # If bottom previously selected, gray bottom buttons
        self.removeBottom()

        # Bet top button and number 1-40 buttons turn blue
        self.betTopButton.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num1.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num2.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num3.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num4.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num5.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num6.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num7.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num8.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num9.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num10.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num11.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num12.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num13.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num14.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num15.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num16.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num17.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num18.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num19.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num20.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num21.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num22.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num23.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num24.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num25.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num26.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num27.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num28.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num29.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num30.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num31.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num32.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num33.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num34.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num35.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num36.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num37.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num38.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num39.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num40.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        
    def betBottom(self):
        # Player bets bottom range (41-80), global variable bet changed
        global bet
        bet = 'bottom'

        # Check credit via credit LCD display
        # If no availble credits, PLAY button reminder to add credits
        credits = self.creditCountLCD.intValue()
        if credits > 0:
            self.playButton.setText('PLAY')
        else:
            self.playButton.setText('You need credits!')

        # If top previously bet, gray those buttons
        self.removeTop()

        # Bet bottom and num range (41-80) turn blue
        self.betBottomButton.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num41.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num42.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num43.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num44.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num45.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num46.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num47.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num48.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num49.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num50.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num51.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num52.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num53.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num54.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num55.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num56.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num57.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num58.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num59.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num60.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num61.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num62.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num63.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num64.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num65.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num66.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num67.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num68.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num69.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num70.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num71.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num72.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num73.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num74.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num75.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num76.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num77.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num78.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num79.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        self.num80.setStyleSheet("QPushButton" "{" "background-color: blue;" "}")
        
    def removeTop(self):
        # Graying of bet top button and number range 1-40, return to base state
        self.betTopButton.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num1.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num2.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num3.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num4.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num5.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num6.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num7.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num8.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num9.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num10.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num11.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num12.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num13.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num14.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num15.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num16.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num17.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num18.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num19.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num20.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num21.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num22.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num23.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num24.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num25.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num26.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num27.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num28.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num29.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num30.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num31.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num32.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num33.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num34.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num35.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num36.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num37.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num38.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num39.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num40.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        
    def removeBottom(self):
        # Greying of bet bottom and number range 41-80, return to base state
        self.betBottomButton.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num41.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num42.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num43.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num44.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num45.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num46.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num47.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num48.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num49.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num50.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num51.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num52.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num53.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num54.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num55.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num56.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num57.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num58.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num59.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num60.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num61.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num62.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num63.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num64.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num65.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num66.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num67.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num68.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num69.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num70.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num71.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num72.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num73.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num74.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num75.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num76.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num77.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num78.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num79.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.num80.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")

    def clearCallNums(self):
        # Clear call num buttons to base state
        self.numCall1.setText('')
        self.numCall1.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall2.setText('')
        self.numCall2.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall3.setText('')
        self.numCall3.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall4.setText('')
        self.numCall4.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall5.setText('')
        self.numCall5.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall6.setText('')
        self.numCall6.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall7.setText('')
        self.numCall7.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall8.setText('')
        self.numCall8.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall9.setText('')
        self.numCall9.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall10.setText('')
        self.numCall10.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall11.setText('')
        self.numCall11.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall12.setText('')
        self.numCall12.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall13.setText('')
        self.numCall13.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall14.setText('')
        self.numCall14.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall15.setText('')
        self.numCall15.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall16.setText('')
        self.numCall16.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall17.setText('')
        self.numCall17.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall18.setText('')
        self.numCall18.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall19.setText('')
        self.numCall19.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")
        self.numCall20.setText('')
        self.numCall20.setStyleSheet("QPushButton" "{" "background-color: light gray;" "}")