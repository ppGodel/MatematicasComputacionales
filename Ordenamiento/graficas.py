import random
import copy
def bubbleSort(alist):
    contador = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            contador +=1
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return contador

def selectionSort(alist):
    contador = 0
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            contador +=1
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return contador

def insertionSort(alist):
    contador = 0
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        contador += 1
        while position>0 and alist[position-1]>currentvalue:            
            contador += 1
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
    return contador

def quickSort(arr):
    global qc
    if len(arr) < 2:
        return arr # base case
    p = arr.pop(0)
    menores, mayores = list(), list()
    for c in arr:
        qc += 1
        if c <= p:
            menores.append(c)
        elif c > p:
            mayores.append(c)
    return quickSort(menores) + [p] + quickSort(mayores)     

def rndar(lon):
    arr = []
    for r in range(lon):
        arr.append(random.randint(0, lon))
    return arr


l = 4
print("L","B","S","I", "Q")
while l < 1100:
    for replica in range(30):
        arr = rndar(l)
        a1, a2, a3, a4 =  copy.deepcopy(arr), copy.deepcopy(arr), copy.deepcopy(arr), copy.deepcopy(arr)
        bc = bubbleSort(a1)
        sc = selectionSort(a2)
        ic = insertionSort(a3)
        qc = 0
        r4 = quickSort(a4)
        print(l, bc, sc, ic, qc)
        #print(arr)
        #print(a1)
        #print(a2)
        #print(a3)
        #print(r4)
    l *= 2
