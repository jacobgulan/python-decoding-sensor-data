import glob
import csv
import os

def load_sensor_data():
    sensor_data: list = []
    sensor_files: list[str] = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))

    for sensor_file in sensor_files:
        with open(sensor_file, 'r', encoding='utf-8') as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            for row in data_file:
                sensor_data.append(row)

    return sensor_data
