import datetime
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


        
today = datetime.date.today().strftime("%d/%m/%Y")
aYearAway = datetime.datetime.now().strftime("%d/%m/%Y") + datetime.timedelta(days=365)
def isFuture():
    global d1, d2, d3
    d1 = datetime.datetime.strptime(arrival, "%d/%m/%Y").date()
    d2 = datetime.datetime.strptime(today, "%d/%m/%Y").date()
    d3 = datetime.datetime.strptime(aYearAway, "%d/%m/%Y").date()

getDate()
isFuture()

while d2>d1 and d1<d3:
    print("date cant be passed")
    getDate()
    isFuture()

getDate()
isFuture()

