from enum import Enum
 
class Direction(Enum):
    """An Enum to define going up or down"""
    Up = True
    Down = False

class people():
    """A class used to manage the kinematics of an elevator

    Attributes
    ----------
    self.numPeople : int
        the number of people in this group
    self.currFloor : int
        the current floor the people are on
    self.desFloor : int
        the floor the people want to go to
    self.dir : enum
        the direction the person wants to go
    """

    def __init__(self, numPeople, currFloor, desFloor):
        """
        Parameters
        ----------
        numPeople : int
            the number of people in the party
        currFloor : int
            the floor the person is on
        desFloor: int
            the floor the person wants to go to
        """
        self.numPeople = numPeople
        self.currFloor = currFloor
        self.desFloor = desFloor
        if(desFloor > currFloor):
            self.dir = Direction.Up
        elif(desFloor < currFloor):
            self.dir = Direction.Down
        else:
            raise Exception("Error:People:currFloor==desFloor")
