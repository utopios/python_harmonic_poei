import os
import csv


cdef void cython_folder_analysis(char* folder):
    cdef:
        int i = 0
    directory_list = [x[0] for x in os.walk(folder)]
    for sub in directory_list:
        csv_list = [a for a in os.listdir(sub) if a.endswith(b'.csv')]
        index = 0
        lines = []
        for file in csv_list:
            with open(bytes("{}/{}".format(sub.decode("utf-8"), file.decode("utf-8")), encoding='utf8'), 'r') as f:
                csv_reader = csv.reader(f, delimiter=";")
                for line in csv_reader:
                    print(line)
                    lines.append(line)
                    index += 1

            with open(bytes("{}/csv_pack.csv".format(sub.decode("utf-8")), encoding='utf8'), 'w') as f:
                csv_writer = csv.writer(f, delimiter=";")
                i = 0
                while i < index:
                    csv_writer.writerow(lines[i])
                    i += 1





def run_cython_analysis(folder):
    cython_folder_analysis(folder)