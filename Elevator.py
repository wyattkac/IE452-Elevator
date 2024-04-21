from sortedcontainers import SortedList
import numpy

import Globals
from Direction import direction
from Event import event

class elevator():
    """A class used to manage the kinematics of an elevator

    Attributes
    ----------
    self.TOTALFLOORS : int
        the total number of floors in the building
    self.currFloor : int
        the current floor the elevator is on
    self.prevFloor : int
        the floor the elevator previously moved to
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
        self.TOTALFLOORS = TOTALFLOORS-1
        self.currFloor = 0
        self.prevFloor = 0
        self.TOTALCAP = TOTALCAP
        self.currCap = 0
        self.dir = direction.Idle
        self.people = SortedList()
        self.speed = [1.5, 2.5, 1.7, 11.4] # time to add for accel, time between floors (at max speed), time to add for decel

    #TODO: write this method
    def move(self, floor):
        """
        Parameters
        ----------
        floor : int
            floor the elevator will move to
        """
        return -1
    
    #TODO: write this method
    def unload(self):

        return -1

    #TODO: write this method
    def load(self, person):
        
        """
        Parameters
        ----------
        person : people()
            people to attempt to load into the elevator
        """
        self.people.add(person) #TODO
        if(self.dir==direction.Idle):
            if(self.currFloor>person.desFloor):
                self.dir=direction.Down
            else:
                self.dir=direction.Up
        diffFloor = abs(self.currFloor-person.desFloor)-1
        travelTime = self.speed[0] + self.speed[1]*diffFloor + self.speed[2]
        eve = event(Globals.currTime+travelTime, self)
        
        Globals.FEL.add(eve)
        
        print(self.dir)
