#Computer guesses a users number

#Range 1 - 1000

def getUserFeedback():
    global guessResult
    feedback = input("Am I too high, too low or did I win? ")
    #Get the users input
    #If the input contains any of the keywords count it
    while True:
        if "high" in feedback.lower():
            guessResult = "high"
            break
        elif "low" in feedback.lower():
            guessResult = "low"
            break
        elif "win" in feedback.lower() or "won" in feedback.lower():
            guessResult = "win"
            break
        feedback = input("Error! Please use 'high', 'low' or 'win / won' in your response:\n")
        
def makeANewGuess(high, low):
        #If the guess is too high set the max guess to prev guess
        if guessResult == "high":
            high[0] = computerGuess
        #If the guess is too low set the min guess to prev guess
        elif guessResult == "low":
            low[0] = computerGuess + 1
        #If the user wins do nothing but otherwise would throw error
        elif guessResult == "win":
            return
        #Just in case anything bad happens
        else:
            print("I do not know how you got here...")
       
        #Calculate new guess
        return calculateNewGuess(low,high)
    
def calculateNewGuess(low, high):
     return (low[0]+high[0])//2
    
def getInflectionOfNum(num):
    lastDigit = num % 10
    if lastDigit == 1:
        return "{}st".format(num)
    elif lastDigit == 2:
        return "{}nd".format(num)
    elif lastDigit == 3:
        return "{}rd".format(num)
    else:
        return "{}th".format(num)

    
#Global Variable
guessResult = ""

#Regular Variable
#computerGuess = 0
#guessCounter = 0
keepPlaying = "y"
#Put these into lists to pass by reference
#high = []
#low = []
while "y" in keepPlaying.lower():
    guessResult = ""

    #These will go out of scope so they reset for next game
    computerGuess = 500
    guessCounter = 1
    high = [1000]
    low = [1]

    while guessResult != "win":
        if guessCounter > 10:
            print("hmmmm... looks like your number doesnt exist. Try playing again")
            break
        print("My {} guess is {}".format(getInflectionOfNum(guessCounter) ,computerGuess))
        getUserFeedback()
        computerGuess = makeANewGuess(high,low)
        guessCounter += 1
    if guessResult == "win":
        keepPlaying = input("Great game! Would you like to play again? ")
    else:
        keepPlaying = input("Oh man! Well.. would you like to try again? ")
