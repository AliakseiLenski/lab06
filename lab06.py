from Apartment import Apartment
'''
def mergesort(apartmentList):
    print("Splitting ",apartmentList)
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                apartmentList[k]=lefthalf[i]
                i = i + 1
            else:
                apartmentList[k]=righthalf[j]
                j = j + 1
            k=k+1

        while i < len(lefthalf):
            apartmentList[k]=lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            apartmentList[k]=righthalf[j]
            j = j + 1
            k = k + 1
'''

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList)//2
        L = apartmentList[:mid]
        R = apartmentList[mid:]
  
        mergesort(L)
        mergesort(R)
  
        i = j = k = 0
  
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                apartmentList[k] = L[i]
                i += 1
            else:
                apartmentList[k] = R[j]
                j += 1
            k += 1
  
        while i < len(L):
            apartmentList[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            apartmentList[k] = R[j]
            j += 1
            k += 1
        
  
    
def ensureSortedAscending(apartmentList):
    for n in range(len(apartmentList)-1):
        if apartmentList[n] < apartmentList[n+1]:
            return True
        else:
            return False

def getNthApartment(apartmentList, n):
    if n > len(apartmentList):
        return "(Apartment) DNE"
    return apartmentList[n].getApartmentDetails()
    

def getTopThreeApartments(apartmentList):
    mergesort(apartmentList)
    length = len(apartmentList)
    string = ""
    if length >= 3:
        string += "1st: " + apartmentList[0].getApartmentDetails() + "\n"
        string += "2nd: " + apartmentList[1].getApartmentDetails() + "\n"
        string += "3rd: " + apartmentList[2].getApartmentDetails()
    elif length == 2:
        string += "1st: " + apartmentList[0].getApartmentDetails() + "\n"
        string += "2nd: " + apartmentList[1].getApartmentDetails()
    elif length == 1:
        string += "1st: " + apartmentList[0].getApartmentDetails()
    else:
        return string
       
    return string



'''
a0 = Apartment(1200, 200, "average")
a1 = Apartment(1200, 200, "excellent")
a2 = Apartment(1000, 100, "average")
a3 = Apartment(1000, 215, "excellent")
a4 = Apartment(700, 315, "bad")
a5 = Apartment(800, 250, "excellent")

apartmentList = [a0, a1, a2, a3, a4, a5]
length = len(apartmentList)
mergesort(apartmentList)
#print(apartmentList)
#assert ensureSortedAscending(apartmentList) == True
#print(getNthApartment(apartmentList, 0))
#print(getNthApartment(apartmentList, 5))
#print(getNthApartment(apartmentList, 10))
print(getTopThreeApartments(apartmentList))
'''

    
