import os


def build_car_load(data):
    traffic_lights = {}
    lights_id = {}

    for street in data.streets:
        lights_id[street] = data.streets[street]['end']

    for car in data.cars:
        for street in data.cars[car]:
            end_dict = traffic_lights.get(lights_id[street], {})
            end_dict[street] = end_dict.get(street, 0) + 1
            traffic_lights[lights_id[street]] = end_dict

    return traffic_lights


def play(lights_stats, total_time, division_factor=1, sort_lights=True):
    if isinstance(division_factor, int):
        division_factor = division_factor if division_factor <= total_time else 2
        division_factor = [division_factor] * len(lights_stats)
    assert len(division_factor) == len(lights_stats)
    out = []

    for i, (cross, lights) in enumerate(lights_stats.items()):
        lights = [(k, v) for k, v in lights.items()]

        # print('-', cross, lights)
        if len(lights) == 1:
            out_tuple = (cross, [(lights[0][0], total_time)])
        else:
            total_w = sum([l[1] for l in lights])
            lights_times = []
            for l in lights:
                t = min(total_time, round((l[1] / total_w) * (total_time / division_factor[i])))
                if t == 0:
                    continue
                lights_times.append((l[0], t))
            if sort_lights:
                lights_times = sorted(lights_times, key=lambda tup: tup[1], reverse=True)

            out_tuple = (cross, lights_times)

        out.append(out_tuple)

    return out


def write_res(res, out_path='out.txt'):
    f = open(out_path, "w")
    f.write('{}\n'.format(len(res)))  # num of light schedules

    for cross_id, lights in res:
        f.write('{}\n'.format(cross_id))  # intersection id
        f.write('{}\n'.format(len(lights)))  # num light schedules
        for light_name, time in lights:
            f.write('{} {}\n'.format(light_name, time))  # light time

    f.close()
