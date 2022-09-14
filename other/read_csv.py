import csv


import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

@timeit
def convert_csv_data(file_path):
    data = {'col_1':[],
            'col_2':[]}

    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:

                line_count += 1
                continue
            else:
                data['col_1'].append(row[0])
                data['col_2'].append(row[1])
    return data

d = convert_csv_data('our_wine.csv')

print('Total objects:', len(d['col_1']))
