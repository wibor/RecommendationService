import csv
import os


def csv_head_reader(foldername):
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), foldername)
    for _, _, files in os.walk(folder):
        for file in files:
            file_name = r".\food\{}".format(file)
            with open(file_name, newline='', encoding='utf-8') as f:
                csv_reader = csv.reader(f, delimiter=',')
                print('\n\t' + file)
                headers = next(csv_reader)
                row = next(csv_reader)
                for item in zip(headers, row):
                    print(item[0] + ': ' + item[1])



