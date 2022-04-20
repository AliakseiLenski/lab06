from Apartment import Apartment
from lab06 import mergesort, ensureSortedAscending, getNthApartment, getTopThreeApartments

def test_apartmentMethods():
    a0 = Apartment(1204, 200, "bad")
    a1 = Apartment(1204, 0, "excellent")
    a2 = Apartment()
    a3 = Apartment(0, 0, "average")

    assert a0.getApartmentDetails() == "(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad"
    assert a1.getApartmentDetails() == "(Apartment) Rent: $1204, Distance From UCSB: 0m, Condition: excellent"
    assert a2.getApartmentDetails() == "(Apartment) Rent: $0, Distance From UCSB: 0m, Condition: N/A"
    assert a3.getApartmentDetails() == "(Apartment) Rent: $0, Distance From UCSB: 0m, Condition: average"

    a4 = Apartment(1204, 200, "bad")
    a5 = Apartment(1204, 200, "average")
    a6 = Apartment(1204, 200, "excellent")
    assert (a5.getApartmentDetails() == a4.getApartmentDetails()) == False
    assert (a6.getApartmentDetails() > a4.getApartmentDetails()) == True
    assert (a4.getApartmentDetails() < a6.getApartmentDetails()) == True

    a8 = Apartment(1200, 200, "average")
    a9 = Apartment(1200, 200, "excellent")
    a10 = Apartment(1000, 100, "average")
    a11 = Apartment(1000, 215, "excellent")
    a12 = Apartment(700, 315, "bad")
    a13 = Apartment(800, 250, "excellent")
    assert (a10.getApartmentDetails() > a13.getApartmentDetails()) == False
    assert (a8.getApartmentDetails() < a11.getApartmentDetails()) == False
    assert (a9.getApartmentDetails() < a8.getApartmentDetails()) == False
    assert (a10.getApartmentDetails() == a11.getApartmentDetails()) == False
    assert (a12.getApartmentDetails() > a13.getApartmentDetails()) == False

def test_mergesortAscending():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")

    apartmentList = [a0, a1, a2, a3, a4, a5]
    length = len(apartmentList)

    mergesort(apartmentList)

    assert ensureSortedAscending(apartmentList) == True
    assert getNthApartment(apartmentList, 0) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    assert getNthApartment(apartmentList, 10) == "(Apartment) DNE"
    assert getNthApartment(apartmentList, 5) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    assert getTopThreeApartments(apartmentList) == "1st: (Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad\
                                                    2nd: (Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent\
                                                    3rd: (Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average"

    
    
    
    
