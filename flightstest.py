def menuDest():
    print("1. Rome")
    print("2. Paris")
    print("3. Florida")
    global dest
    dest = int(input("Please choose destination by number: "))
    global choice
    if dest == 1:
        choice = str("Rome")
    elif dest == 2:
        choice = str("Paris")
    elif dest == 3:
        choice = str("Florida")
    else:
        print("Invalid destination selected")
    return choice

adultTickets = int(input("How many adult tickets are needed?: "))
childTickets = int(input("How many child tickets are needed?: "))

def ticketCost():
    if dest == 1:
        price = int(400)
    elif dest == 2:
        price = int(250)
    elif dest == 3:
        price = int(600)
    else:
        print("invalid destination selected")

    adultCost = adultTickets * price
    childCost = childTickets * price/2
    total = adultCost + childCost
    return total

menuDest()
print("You have chosen " + str(adultTickets) + " adults and " + str(childTickets) + " children flying to " + choice + " costing a total of £" + str(ticketCost()))

