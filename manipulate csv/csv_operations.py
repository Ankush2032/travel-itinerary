import os, csv
from pprint import pprint


def save_to_csv(data, filename, print_data=False):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', encoding='utf-8', newline='') as fx:
        writer = csv.DictWriter(fx, fieldnames=list(data.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    if print_data:
        pprint(data)


def read_csv_to_dict_list(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data