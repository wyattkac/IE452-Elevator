from sortedcontainers import SortedList

import Globals
from Controller import simpleControl
from Elevator import elevator
from Event import event
from People import people

def main():
    # Create FEL (people that will want elevators)
    pep1 = people(1,1,8)
    eve1 = event(5, pep1)
    Globals.FEL.add(eve1)
    pep2 = people(1,1,9)
    eve2 = event(6, pep2)
    Globals.FEL.add(eve2)

    # Create Elevators
    Globals.elevator1 = elevator(10,10,1)
    Globals.elevator2 = elevator(10,10,2)
    Globals.elevator3 = elevator(10,10,3)

    # Main Loop
    loop = True
    while(loop):
        # Pull an event off the FEL, and set Time
        eve = Globals.FEL.pop()
        Globals.currTime = eve.time
        print("Time", Globals.currTime)
        # If event is a person, pass them to the controller to assign to an elevator
        if(type(eve.event) is people):
            print("\tI Found A Person")
            simpleControl(eve.event) # Pass the person to the controller
        # If event is an elevator, do elevator stuff
        if(type(eve.event) is elevator):
            print("\tElevator", eve.event.name)
            #TODO Do somthing with the people to remove them from the elevator
        # When FEL is empty, quit
        if(Globals.FEL==SortedList([])):
            loop = False
        print("")
        Globals.prevTime = Globals.currTime

    #FEL.clear()
    #FEL.add(pep1)
    #FEL.add(pep2)
    #print(FEL.pop(0).desFloor) # Use 0 to remove lower (when going up), -1 to remove upper (when going down)
    #print(FEL[0].desFloor)

main()