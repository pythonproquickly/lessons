# You are a python developer working for a building architect.
# For every building the architect designs it is always a
# challenge to estimate the correct number of elevators needed for
# the building.
# Your job is to build a simulation that will be used to develop
# a robust elevator estimating algorithm.
# The simulation will be used for exploratory testing to identify
# the data requirements that are needed to get the number of
# elevators right.
# When confident in the simulation, you will build the elevator
# estimation program.


from dataclasses import dataclass


@dataclass
class Time:
    """
    A class that represents the time and the day of the week.
    Not necessary to implement holidays/weekends (interested in time of the greatest traffic).
    """

    busy: bool = False
    hour: int = 0  # 0-8 representing hour of workday


@dataclass
class Elevator:
    """
    A class that represents a device to move people vertically through a building.
    Are expensive and almost impossible to add to existing building.
    """

    # A standard elevator typically can hold between 1,000 and 6,000
    # pounds
    max_weight: int
    # how much weight elevator is holding at a given moment
    current_weight: int = 0

    def update_weight(self):
        """
        Changes current weight of elevator (adds or subtracts based on
        load of elevator).
        Makes sure current_weight <= max_weight at any given moment.
        """
        pass


@dataclass
class Building:
    """
    A class that represents the location of the Elevator.
    """

    num_floors: int
    floors: list


@dataclass
class Floor:
    """
    A class that represents the floor of a building.
    """

    pass


@dataclass
class Passenger:
    """
    A class that represents a living thing that can ride an elevator.
    """

    weight: float
