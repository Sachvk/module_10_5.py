import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time.time()
for i in filenames:
    read_info(i)
end_time = time.time()
print(end_time - start_time)

# Многопроцессный
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    start_time = time.time()
    pool.map(read_info, filenames)
    end_time = time.time()
    print(end_time - start_time)
