print("hello".rjust(20,"-"))
#Solo se puede rellenar con un caracter
#rcenter,rjust


def printItemsPlayer(itemsDict, leftWidth,rightWidth):
    print("PLAYER ITEMS".center(leftWidth+rightWidth,"-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth,".")+str(v).rjust(rightWidth," "))


Items={"Monedas":4,"Llaves":12,"Poción Curativa":4}
printItemsPlayer(Items,10,5)
printItemsPlayer(Items,20,6)
printItemsPlayer(Items,54,20)
printItemsPlayer(Items,20,10)