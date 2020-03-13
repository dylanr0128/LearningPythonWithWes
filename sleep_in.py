def sleep_in(userEntryA, userEntryB):

    if (userEntryA == "true"):
        weekday = True
    else:
        weekday = False
    
    if (userEntryB == "True"):
        vacation = True
    else:
        vacation = False

    if (weekday == True and vacation == False):
        print("false")
    print("true")

