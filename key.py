#init
class Key:
    def __init__(self):
        self.char = ['a','b','c','d','e','f','g',
                     'h','i','j','k','l','m','n',
                     'o','p','q','r','s','t','u',
                     'v','w','x','y','z']

        self.key = self.generateKey()

    def generateCharSequence(self):
        from random import randint
        
        sequence = ""
        
        for i in range(0,15):
            arrayChoice = randint(0,1)
            if arrayChoice == 1:
                sequence += self.selectRandomChar()
            else:
                sequence += str(randint(0,9))
        return sequence

    def selectRandomChar(self):
        from random import randint
        
        charChoice = randint(0,25)
        charUpperChoice = randint(0,1)
        if charUpperChoice == 1:
            return self.char[charChoice]
        else:
            return self.char[charChoice].upper()

    def generateKey(self):
        import datetime
        import hashlib
        
        sand = str(datetime.datetime.now())[20:26]
        string = self.generateCharSequence()+ sand
        
        key = hashlib.md5(string.encode("utf-8")).hexdigest().upper()
        return key[5:11]

    def getKey(self):
        return self.key
