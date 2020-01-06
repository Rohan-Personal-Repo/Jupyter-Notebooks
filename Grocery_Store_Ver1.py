itemDict = {}
total = 0
itemVal = 0

print( "Enter items in Order : Item Price Quantity or Q to quit - " )
while True:
    inputVal = input("Items-")
    if(inputVal != 'q') and (inputVal != 'Q'):
        ipSplit = inputVal.split( " " )
        itemVal = int(ipSplit[1]) * (int(ipSplit[2]))
        total = total + itemVal
        itemDict[ipSplit[0]] = itemVal
    else:
        print("Thank you for shopping with us, please find your bill below:\n")
        print( "Item \t Price" )
        for key in itemDict.keys():
            print( key ,"\t ", itemDict.get(key) )
        print( "Total= \t ", total)
        break

