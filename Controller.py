import Globals
from Direction import direction
from Event import event

# Get Working?
def simpleControl(person):
    """An extremely simple application of a controller
    This controller assignes people to an idle elevator
    If no elevators are idle, it waits 10 seconds and tries again

    Parameters
    ----------
    person : people()
        the people that are calling an elevator
    """
    if(Globals.elevator1.dir == direction.Idle):
        Globals.elevator1.load(person)
        print("\tAssigned them to Elevator 1")
    elif(Globals.elevator2.dir == direction.Idle):
        Globals.elevator2.load(person)
        print("\tAssigned them to Elevator 2")
    elif(Globals.elevator3.dir == direction.Idle):
        Globals.elevator3.load(person)
        print("\tAssigned them to Elevator 3")
    else:
        eve = event(Globals.currTime+10, person)
        Globals.FEL.add(eve)
        Globals.objectiveFunc = Globals.objectiveFunc + Globals.peopleWaiting*10
        Globals.waitTime = Globals.waitTime + 10
        print("\tThey Have to Wait")

def stagedControl(person):
    """An extremely simple application of a controller
    This controller assignes people to an idle elevator
    If no elevators are idle, it waits 10 seconds and tries again

    Parameters
    ----------
    person : people()
        the people that are calling an elevator
    """
    if(Globals.elevator1.dir == direction.Idle and person.currFloor < 3):
        Globals.elevator1.load(person)
        print("\tAssigned them to Elevator 1")
    elif(Globals.elevator2.dir == direction.Idle and person.currFloor < 6):
        Globals.elevator2.load(person)
        print("\tAssigned them to Elevator 2")
    elif(Globals.elevator3.dir == direction.Idle):
        Globals.elevator3.load(person)
        print("\tAssigned them to Elevator 3")
    else:
        eve = event(Globals.currTime+10, person)
        Globals.FEL.add(eve)
        Globals.objectiveFunc = Globals.objectiveFunc + Globals.peopleWaiting*10
        Globals.waitTime = Globals.waitTime + 10
        print("\tThey Have to Wait")
