itemDict = {}
total = 0
itemVal = 0
quanList = []
quanSum = 0

print( "Enter items in Order : Item Price Quantity or Q to quit - " )
while True:
    inputVal = input("Items-")
    if(inputVal != 'q') and (inputVal != 'Q'):
        ipSplit = inputVal.split( " " )
        itemVal = int(ipSplit[1]) * (int(ipSplit[2]))
        total = total + itemVal
        itemDict[ipSplit[0]] = itemVal
        quanList.append(ipSplit[2])
        quanSum = quanSum + int(ipSplit[2])
    else:
        print("Thank you for shopping with us, please find your bill below:\n")
        print("Item \t Quantity \t Price")
        i = 0;
        for key in itemDict.keys():
            print(key, " \t ", quanList[i], "\t\t ", itemDict.get(key))
            i = i+1
        print("Total", " \t ", quanSum, "\t\t ", total)
        break