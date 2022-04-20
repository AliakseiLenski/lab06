class Apartment:
    
    def __init__(self, rent = 0,  metersFromUCSB = 0, condition = "N/A"):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.rent, self.metersFromUCSB, self.condition)

    def __eq__(self, other):
        return (self.rent == other.rent) and (self.metersFromUCSB == other.metersFromUCSB) and (self.condition == other.condition)
        
    def __gt__(self, other):
        if (self.rent > other.rent):
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB > other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                if len(self.condition) > len(other.condition):
                   return False
                else:
                    return True
            else:
                return False
        else:
            return False
                
          
    def __lt__(self, other):
        if (self.rent < other.rent):
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                if len(self.condition) < len(other.condition):
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

'''    
a0 = Apartment(1204, 200, "bad")
a1 = Apartment(1204, 200, "average")
a2 = Apartment(1204, 200, "excellent")
print(a0.getApartmentDetails())
assert a0.getApartmentDetails() == "(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad"
print(a1.condition)
print(a2.condition)
print(a0.condition)
assert (a1 > a0) == True
assert (a2 > a0) == True
'''


