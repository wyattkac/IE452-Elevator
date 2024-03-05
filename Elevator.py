import numpy

class Elevator():
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
        #TODO: How should this be written? What if someone else wants to use the elevator while it's moving?
    
    Methods
    -------
    move(floor)
        tells the elevator what floor to move to
    load(people)
        puts people in the elevator
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
        self.TOTALCAP = TOTALCAP
        self.currCap = 0
        #TODO: What's the best way to do this? (see note in docstring)
        self.speed = [0, 1, 2]


E1 = Elevator(10, 5)
