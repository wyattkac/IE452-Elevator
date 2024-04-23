from sortedcontainers import SortedList

# FEL, currTime, and prevTime need to be accessible from all functions
FEL = SortedList()
prevTime = 0
currTime = 0

# Elevators need to be accessible from all functions
elevator1 = None
elevator2 = None
elevator3 = None

# Objective Function (For Opt)
peopleWaiting = -50
elevatorMoving = -1
objectiveFunc = 0
waitTime = 0
