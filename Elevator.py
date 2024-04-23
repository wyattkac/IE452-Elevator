from sortedcontainers import SortedList

import Globals
from Direction import direction
from Event import event
from People import people

class elevator():
    """A class used to manage the kinematics of an elevator

    Attributes
    ----------
    self.TOTALFLOORS : int
        the total number of floors in the building
    self.currFloor : int
        the current floor the elevator is on
    self.TOTALCAP : int
        the maximum capacity of the elevator (max number of people in elevator)
    self.currCap : int
        the current capacity of the elevator (number of people in elevator)
    self.SPEED : double[]
        an array of how long it takes the elevator to move
        [additional time to accelerate, time at max speed between floors, additional time to decelerate, time at each floor]
    self.dir : direction (enum)
        the direction the elevator is moving in
    self.people : SortedList([people()])
        a list of the people currently in the elevator
    
    Methods
    -------
    move(floor)
        tells the elevator what floor to move to
    unload()
        removes people from the elevator
    load(people)
        tries to put people in the elevator
    """

    def __init__(self, TOTALFLOORS, TOTALCAP, name):
        """
        Parameters
        ----------
        TOTALFLOORS : str
            the total number of floors in the building
        TOTALCAP : str
            the maximum capacity of the elevator
        """
        self.name = name
        self.TOTALFLOORS = TOTALFLOORS
        self.currFloor = 0
        self.TOTALCAP = TOTALCAP
        self.currCap = 0
        self.dir = direction.Idle
        self.people = SortedList()
        self.speed = [2.5, 5, 2.5, 14] # time to add for accel, time between floors (at max speed), time to add for decel
        self.FEL = SortedList()
        self.floors = SortedList()
        self.toGoFloor = 0

    def move(self, floor):
        """
        Parameters
        ----------
        floor : int
            floor the elevator will move to
        """
        print("\tElevator is moving")
        if(self.currFloor==floor):
            raise Exception("Error:Attempting to move to the same floor!")
        diffFloor = abs(self.currFloor-floor)-1
        travelTime = self.speed[0] + self.speed[1]*diffFloor + self.speed[2]
        Globals.objectiveFunc = Globals.objectiveFunc + Globals.elevatorMoving*travelTime
        eve = event(Globals.currTime+travelTime, self)
        Globals.FEL.add(eve)
        self.toGoFloor = floor

    def tallyWait(self):
        for i in self.FEL:
            Globals.objectiveFunc = Globals.objectiveFunc + Globals.peopleWaiting*(Globals.currTime-Globals.prevTime)
            Globals.waitTime = Globals.waitTime + Globals.currTime-Globals.prevTime
        Globals.prevTime = Globals.currTime

    def load(self, person):
        
        """
        Parameters
        ----------
        person : people()
            people to attempt to load into the elevator
        """
        self.tallyWait()
        self.floors.add(person.currFloor)
        self.FEL.add(person)
        if(self.currFloor>person.currFloor):
            self.dir=direction.Down
        else:
            self.dir=direction.Up
        self.action()
    
    def action(self):
        self.tallyWait()
        self.currFloor = self.toGoFloor # TODO: THIS MUST BE CHANGED TO WORK WELL
        didSomthing = False
        # Remove current floor from list of floors to stop at
        if(self.dir==direction.Up):
            while(self.floors != SortedList([]) and self.floors[0] == self.currFloor):
                self.floors.__delitem__(0)
        if(self.dir==direction.Down):
            while(self.floors != SortedList([]) and self.floors[-1] == self.currFloor):
                self.floors.__delitem__(-1)
        # Start by unloading people that want off
        if(self.people != SortedList([])):
            if(self.dir==direction.Up):
                while(self.people != SortedList([]) and self.people[0].desFloor == self.currFloor):
                    self.currCap = self.currCap - self.people[0].numPeople
                    self.people.__delitem__(0)
                    didSomthing = True
                    print("\tI unloaded a person")
            if(self.dir==direction.Down):
                while(self.people != SortedList([]) and self.people[-1].desFloor == self.currFloor):
                    self.currCap = self.currCap - self.people[-1].numPeople
                    self.people.__delitem__(-1)
                    didSomthing = True
                    print("\tI unloaded a person")
        # If people want on, let them on


        if(self.FEL != SortedList([])):
            if(self.dir==direction.Up):
                while(self.FEL != SortedList([]) and self.FEL[0].currFloor == self.currFloor):
                    if(self.FEL[0].numPeople+self.currCap > self.TOTALCAP):
                        break
                    self.currCap = self.currCap + self.FEL[0].numPeople
                    self.floors.add(self.FEL[0].desFloor)
                    if(self.currFloor>self.FEL[0].desFloor):
                        self.dir=direction.Down
                    else:
                        self.dir=direction.Up
                    self.people.add(self.FEL[0])
                    self.FEL.__delitem__(0)
                    didSomthing = True
                    print("\tI loaded a person")
            if(self.dir==direction.Down):
                while(self.FEL != SortedList([]) and self.FEL[-1].currFloor == self.currFloor):
                    if(self.FEL[0].numPeople+self.currCap > self.TOTALCAP):
                        break
                    self.currCap = self.currCap + self.FEL[-1].numPeople
                    self.floors.add(self.FEL[-1].desFloor)
                    if(self.currFloor>self.FEL[0].desFloor):
                        self.dir=direction.Down
                    else:
                        self.dir=direction.Up
                    self.people.add(self.FEL[-1])
                    self.FEL.__delitem__(-1)
                    didSomthing = True
                    print("\tI loaded a person")
        # If loaded/unloaded people, keep doors open for a time
        if(didSomthing == True):
            eve = event(Globals.currTime+self.speed[3], self)
            Globals.FEL.add(eve)
        # If didn't load/unload people either move or become idle
        if(didSomthing == False):
            # Move if more floors to stop on
            if(self.floors != SortedList([]) and self.dir==direction.Up):
                self.move(self.floors[0])
            if(self.floors != SortedList([]) and self.dir==direction.Down):
                self.move(self.floors[-1])
            # If no more floors to stop on, become idle
            if(self.floors==SortedList([])):
                self.dir=direction.Idle
                #if(self.currFloor != Globals.wait):
                #    self.move(4)
