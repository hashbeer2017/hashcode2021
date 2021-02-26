import get_data
import hashcode
import os

for file in os.listdir('input'):
    for div_fact in [128]: # [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
        out_dir = 'output-div=' + str(div_fact)
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        data = get_data.load(os.path.join('input', file))
        light_stats = hashcode.build_car_load(data)
        res = hashcode.play(light_stats, streets=data.streets, total_time=data.time, division_factor=div_fact, sort_lights=True)
        hashcode.write_res(res, out_path=os.path.join(out_dir, file))
