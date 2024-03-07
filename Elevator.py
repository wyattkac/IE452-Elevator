import numpy

class Elevator():
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
        [additional time to accelerate, time at max speed between floors, additional time to decelerate]
    
    Methods
    -------
    move(floor)
        tells the elevator what floor to move to
    unload()
        removes people from the elevator
    load(people)
        tries to put people in the elevator
    """

    def __init__(self, TOTALFLOORS, TOTALCAP):
        """
        Parameters
        ----------
        TOTALFLOORS : str
            the total number of floors in the building
        TOTALCAP : str
            the maximum capacity of the elevator
        """
        self.TOTALFLOORS = TOTALFLOORS
        self.currFloor = 0
        self.prevFloor = 0
        self.TOTALCAP = TOTALCAP
        self.currCap = 0
        #TODO: add people[], buttons[]
        self.speed = [.1, 1, .1] # time to add for accel, time between floors (at max speed), time to add for decel

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
    def load(self, people):
        """
        Parameters
        ----------
        people : TODO
            people to attempt to load into the elevator
        """
        return -1

E1 = Elevator(10, 5)
print(E1.TOTALFLOORS)
