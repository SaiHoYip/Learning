#pip install pyinputplus
#insures user input is what it should be
import pyinputplus
#inp = pyinputplus.inputNum("Input a number: ")
#inp = pyinputplus.inputNum('Enter a num: ', lessThan=5)
#inp = pyinputplus.inputNum(blank = True) #If you want blank inputs available
#inp = pyinputplus.inputNum("Put a number in: ",limit=2, default=1) #Will stop asking for input after 2 trys and default input to 1
#inp = pyinputplus.inputNum(allowRegexes=[r'(I|V|L)+',r'zero']) #can choose what is allowed/accepted
inp = pyinputplus.inputNum(blockRegexes=[r'[2478]$']) #can choose what responses are to not be accepted

