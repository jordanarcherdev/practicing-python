#testing my hotel code
#import date
import datetime
#todays date
today = datetime.date.today().strftime("%d/%m/%Y")
#functions
def getDate(): #ensures the date is in correct format
    global arrival
    validDate = False
    while not validDate:
        arrival = input("Date of arrival dd/mm/yyyy: ")
        try:
            datetime.datetime.strptime(arrival, "%d/%m/%Y")
            validDate = True
        except:
            print("Please enter date in this format dd/mm/yyyy: ")

def isFuture(): #resets variables for multiple wrong entries
    global d1, d2
    d1 = datetime.datetime.strptime(arrival, "%d/%m/%Y").date()
    d2 = datetime.datetime.strptime(today, "%d/%m/%Y").date()

def isNumber(question): #ensures input is a number
    while True:
        try:
            i = int(input(question))
        except ValueError:
            print("Please enter a number: ")
            continue
        else:
            return i
            break
def roomReq(): #enquire how many rooms are needed
    global singleReq, doubleReq, familyReq, totalRooms
    singleReq = isNumber("How many single rooms are required? ")
    doubleReq = isNumber("How many double rooms are required? ")
    familyReq = isNumber("How many family rooms are required? ")
    totalRooms = singleReq + doubleReq + familyReq
#set room prices
singleCost = int(47)
doubleCost = int(90)
familyCost = int(250)
#main code
name = input("Please enter booking name: ")
getDate()
isFuture() #defines variables
while d2>d1:
    print("Please pick a date in the future! ")
    getDate()
    isFuture() #resets variables
lengthOfStay = isNumber("How many nights is your stay? ")
while lengthOfStay > 14 or lengthOfStay < 1:
    print("Stay must be between 1 and 14 nights")
    lengthOfStay = isNumber("How many nights is your stay? ")
roomReq()

while totalRooms > 4:
    print("Maximum amount of rooms is 4")
    roomReq()
    
perNightCost = singleCost*singleReq + doubleCost*doubleReq + familyCost*familyReq
totalExVat = perNightCost * lengthOfStay
#discount
if totalRooms >= 3 and lengthOfStay >= 7:
    discount = totalExVat/100*10
else:
    discount = 0
discountedExVat = totalExVat - discount
#vat
vat = discountedExVat/100*20
totalCost = discountedExVat + vat
#output
print (totalRooms)   
