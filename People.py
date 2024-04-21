from Direction import direction

class people():
    """A class used to store information on groups of people

    Attributes
    ----------
    self.numPeople : int
        the number of people in this group
    self.currFloor : int
        the current floor the people are on
    self.desFloor : int
        the floor the people want to go to
    self.dir : direction (enum)
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
            self.dir = direction.Up
        elif(desFloor < currFloor):
            self.dir = direction.Down
        else:
            raise Exception("Error:People:currFloor==desFloor")

    def __lt__(self, other):
        """Designed to use SortedList to return the lower floor
        """
        return self.desFloor < other.desFloor
