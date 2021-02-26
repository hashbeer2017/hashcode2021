class InputData:
    def __init__(self, time, streets, cars):
        self.time = time
        self.streets = streets
        self.cars = cars


def load(file_path):
    with open(file_path, mode='r') as f:
        lines = f.readlines()

    header = lines[0]
    total_time, num_intersections, num_streets, num_cars = _process_first_line(header)

    street_lines = lines[1:num_streets + 1]
    streets = _process_streets(street_lines)

    car_lines = lines[num_streets + 1:]
    cars = _process_cars(car_lines)

    return InputData(time=total_time, streets=streets, cars=cars)


def _process_first_line(first_line):
    split_first_line = first_line.split(' ')
    total_time = int(split_first_line[0])
    num_intersections = int(split_first_line[1])
    num_streets = int(split_first_line[2])
    num_cars = int(split_first_line[3])
    return total_time, num_intersections, num_streets, num_cars


def _process_streets(street_lines):
    streets = dict()
    for line in street_lines:
        line = line[:-1]
        split_line = line.split(' ')
        start = int(split_line[0])
        end = int(split_line[1])
        name = split_line[2]
        length = int(split_line[3])
        streets[name] = {
            'start': start,
            'end': end,
            'length': length
        }
    return streets


def _process_cars(car_lines):
    cars = dict()
    for line in car_lines:
        line = line[:-1]
        split_line = line.split(' ')
        car_id = split_line[0]
        path = split_line[1:]
        cars[car_id] = path
    return cars
