myList = ["Yusuf", 39, True, 3.9]
print(myList)
print(type(myList))
print(type(myList[0]))
print(type(myList[1]))
print(type(myList[2]))
print(type(myList[3]))

myList.append("wise Quarter")
myList.append(39)
myList.append("none")
print(myList)

if 3.9 in myList: 
    print("Yes, sir")
else:
    print("Non, monsieur")

del myList[2]
del myList[1]
print(myList)
#print(sorted(myList))

yeniListe = list(range(10,50))
print(yeniListe)
urunler = ["Bilgisayar", "Zil", "Laptop", "Monitor"]
print(sorted(urunler))

yeniurunler=[]
print(type(yeniurunler))