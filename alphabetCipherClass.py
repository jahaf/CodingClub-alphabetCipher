alphaNum_dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10, \
            'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19, \
                't':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
numAlpha_dict={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j', \
            11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s', \
                20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
ALPHACOUNT = 26



class alphabetCipher():
    
    def __init__(self):
        pass
            
    def encodeTheMessage(self, inputMessage, keyword):
        self.__setTheKeyword(keyword)
        self.__setTheMessage(inputMessage)
        self.__projectTheKeyword()
        encodedMsg = ''
        for iLetter,iKey in zip(self.message,self.projectedKeyword):
            encodedMsg = encodedMsg + self.__encodeSingleLetter(iLetter,iKey)
        return encodedMsg
        
    def decodeTheMessage(self, encodedMessage, keyword):
        self.__setEncodedMessage(encodedMessage)
        self.__setTheKeyword(keyword)
        self.__projectTheKeyword()
        decodedMsg = ''
        for iLetter,iKey in zip(self.encodedMessage,self.projectedKeyword):
            decodedMsg = decodedMsg + self.__decodeSingleLetter(iLetter,iKey)
        return decodedMsg

        
    # Private methods
    
    def __setTheKeyword(self,keyword):
        self.keyword = keyword
        
    
    def __setTheMessage(self,message):
        self.message = message
        
   
    def __setEncodedMessage(self,encodedMessage):
        self.encodedMessage = encodedMessage
        
        
    def __determineDesiredLength(self):
        if not hasattr(self,'message') and not hasattr(self,'encodedMessage'):
            raise Exception('No message has been entered!')
        
        if hasattr(self,'message'):
            desiredLength = len(self.message)
        else:
            desiredLength = len(self.encodedMessage)
        self.desiredLength = desiredLength
        
        
    def __projectTheKeyword(self):
        projectedKeyword = ''
        self.__determineDesiredLength()
        keywordLength = len(self.keyword)
        keyIdx = 0
        counter = 0
        while counter < self.desiredLength:
            projectedKeyword = projectedKeyword+self.keyword[keyIdx]
            keyIdx += 1
            counter += 1
            if keyIdx>=keywordLength:
                keyIdx = 0
        self.projectedKeyword = projectedKeyword

    
    def __encodeSingleLetter(self, inputLetter,keyLetter):
        tempNum = alphaNum_dict[inputLetter] + alphaNum_dict[keyLetter] - 1
        if tempNum>ALPHACOUNT:
            tempNum -= ALPHACOUNT
        return numAlpha_dict[tempNum]
     
        
    def __decodeSingleLetter(self, inputLetter,keyLetter):
        tempNum = alphaNum_dict[inputLetter] + 1 - alphaNum_dict[keyLetter]
        if tempNum <= 0:
            tempNum += ALPHACOUNT
        return numAlpha_dict[tempNum]
                    
   