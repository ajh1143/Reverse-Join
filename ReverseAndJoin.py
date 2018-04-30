class ReverseAndJoin(object):

"""
Program that takes input integer N, which dictates N lines of input sentences. 
Program will reverse each word in each sentence, returning a joined result. 
"""
    
    def getInput(self):
        #Get User Input
        N = int(input("Enter a number"))
        if N.isnumeric():
            return N
        else:
            raise ValueError("Please enter an integer value")
            getInput()

    def processInputLines(self, N):
        #For N+1 lines read
        for each in range(1, N+1):
        #Read Line
            line = sys.stdin.readline()
        #Tokenize sentence, strip whitespaces and split on space
            tokens = line.strip().split(" ")
            #Reverse Chars in each word via List Comprehension
            reversedLine = [token[::-1] for token in tokens]
            #Join reversed elements
            reversedJoin = " ".join(reversedLine)
            #Print Results
            print(reversedJoin)
            
            
if __name__ == "__main__":
    initiate = ReverseAndJoin()
    numberOfLines = initiate.getInput()
    initiate.processInputLines(numberOfLines)
