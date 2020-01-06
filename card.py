import numpy as np
import random

class Card:
    def __init__(self, array, typeOfClass): 
        array = array.astype(str)
        typedCard = np.array([])   
        for card in array:
            card = card + " " + typeOfClass
            typedCard = np.append(typedCard, card)
        self.array = typedCard
        print("\n", typeOfClass, "Cards have been created!:", typedCard)
    
    def printFunc(self):
        print("\nCards have been printed!:", self.array)

    def getOrder(self):
        cardArray = self.array
        numbers = np.array([])
        words = np.array([])
        for card in cardArray:
            card = card.split()
            numbers = np.append(numbers, card[0])  
            words = np.append(words, card[1])
        print("\n", numbers)
        numbers = numbers.astype(int)
        for i in range(len(numbers)):
            minimum = i
        
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[minimum]:
                    minimum = j

            numbers[minimum], numbers[i] = numbers[i], numbers[minimum]
        print("\n", numbers)
        numbers = numbers.astype(str)
        sortedCards = np.array([])
        sortedCards = sortedCards.astype(str)
        for i in range(len(numbers)):
            temp = numbers[i] + " " + words[i]
            sortedCards = np.insert(sortedCards, i, temp)

        print("\nCards have been sorted!:", sortedCards)

    def getMixed(self):
        cardArray = self.array
        for i in range(6, 13):
            randomNumber = random.randint(0, 6)
            cardArray[i], cardArray[randomNumber] = cardArray[randomNumber], cardArray[i]
        print("\nCards have been mixed!:", cardArray)
        
    
    class Karo:
        def __init__(self, array):
            Card.__init__(self, array, "KARO")

        def printFunc(self):
            Card.printFunc(self)
        
        def getOrder(self):
            Card.getOrder(self)

        def getMixed(self):
            Card.getMixed(self)

    class Kupa:
        def __init__(self, array):
            Card.__init__(self, array, "KUPA")

        def printFunc(self):
            Card.printFunc(self)
        
        def getOrder(self):
            Card.getOrder(self)

        def getMixed(self):
            Card.getMixed(self)
        
    class Maca:
        def __init__(self, array):
            Card.__init__(self, array, "MACA")

        def printFunc(self):
            Card.printFunc(self)
        
        def getOrder(self):
            Card.getOrder(self)

        def getMixed(self):
            Card.getMixed(self)

    class Sinek:
        def __init__(self, array):
            Card.__init__(self, array, "SİNEK")

        def printFunc(self):
            Card.printFunc(self)
        
        def getOrder(self):
            Card.getOrder(self)

        def getMixed(self):
            Card.getMixed(self)

####################################################################################

cards = np.arange(1,14)

Karo = Card.Karo(cards)
Karo.printFunc()
Karo.getMixed()
Karo.getOrder()
Karo.getMixed()
Sinek = Card.Sinek(cards)
Sinek.printFunc()
Sinek.getMixed()