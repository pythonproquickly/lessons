import main


def test_time():
    time = main.Time()
    assert time.hour == 0


def test_increment_time():
    time = main.Time()
    initial_time = time.hour
    time.hour += 1
    assert time.hour > initial_time


def start_simulation():
    time = main.Time()
    building = main.Building
    elevators = create_elevators(num_elevators=2, max_weight=1000)
    floors = create_floors(num_floors=5)


def create_elevators(num_elevators, max_weight) -> list:
    elevators = []
    for i in range(num_elevators):
        elevators.append(main.Elevator(max_weight))
    return elevators


def create_floors(num_floors) -> list:
    floors = []
    for i in range(num_floors):
        floors.append(main.Floor())
    return floors
