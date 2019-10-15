import random

class Player(object):

    def __init__(self,name):

        self.name = name
        self.number = 0

    def guess(self):
        self.number = int(random.random()*10)
        print("I'm guessing ", self.number)


class GuessName(object):
    def __init__(self):
        pass

    def startGame():
        p1 = Player("P1")
        p2 = Player("P2")
        p3 = Player("P3")

        guessP1 = guessP2 = guessP3 = 0
        p1IsRight = p2IsRight = p3IsRight = False
        targetNumber = int(random.random()*10)
        print("Thinking a number between 1-10")

        while True:
            print("number to guess is: ", targetNumber)
            p1.guess()
            p2.guess()
            p3.guess()

            guessP1 = p1.number
            print("P1 guessed: ", guessP1)

            guessP2 = p2.number
            print("P2 guessed: ", guessP2)

            guessP3 = p3.number
            print("P3 guessed: ", guessP3)

            if guessP1 == targetNumber:
                p1IsRight = True

            if guessP2 == targetNumber:
                p2IsRight = True

            if guessP3 == targetNumber:
                p3IsRight = True

            if p1IsRight or p2IsRight or p3IsRight:
                print("We got a winner")
                print("P1 got it ", p1IsRight)
                print("P2 got it ", p2IsRight)
                print("P3 got it ", p3IsRight)
                break
            else:
                print("Play one more round")


GuessName.startGame()
