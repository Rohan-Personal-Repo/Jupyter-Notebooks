itemDict = {}
total = 0
itemVal = 0
itemList = []

print( "Enter items in Order : Item Price Quantity or Q to quit - " )
while True:
    inputVal = input("Items-")
    if(inputVal != 'q') and (inputVal != 'Q'):
        ipSplit = inputVal.split( " " )
        itemVal = int(ipSplit[1]) * (int(ipSplit[2]))
        total = total + itemVal
        itemList.append(ipSplit[2])
        itemList.append(str(itemVal))
        itemDict[ipSplit[0]] = itemList
        itemList.clear()
    else:
        print("Thank you for shopping with us, please find your bill below:\n")
        print( "Item \t Quantity \t Price" )
        # for key, value in itemDict.items():
        #     print(key)
        #     print( type(value) , " = ", len(value) )
        #     print( key, "\t ", value[0], "\t ", value[1] )
        # for key in itemDict.keys():
        #     iList = itemDict.get(key);
        #     print( key, "\t ", iList[0], "\t ", iList[1] )
        for key in itemDict:
            print(itemDict[key])
        print( "Total= \t ", total)

