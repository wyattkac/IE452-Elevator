class event():
    """A class used to store events

    Attributes
    ----------
    self.time : int
        time the event happens at (in sec)
    self.event : obj (people or elevator)
        the event to happen
    """

    def __init__(self, time, event):
        """
        Parameters
        ----------
        time : int
            time the event happens at (in sec)
        event : obj (people or elevator)
            the event to happen
        """
        self.time = time
        self.event = event
    
    def __lt__(self, other):
        """Designed to use SortedList to sort passengers
        """
        return self.time > other.time
