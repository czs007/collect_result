import datetime
import json
import os
import sys

from parse import  parse_args

input_path = "./"
output_path = "./"
valid_files = ["proxy.benchmark", "proxy2pulsar.benchmark","query_node_insert.txt",
               "reader_get_pulsar.txt","write_node_insert.txt","writer_get_pulsar.txt"]


result_file = "results.txt"
results = {}


def define_result(path, file, role):
    f = open(path + "/" + file, 'r')
    line = json.loads(f.readline())
    for key in line:
        results[role][key] = []


def collect_result(path, file, role):
    f = open(path + "/" + file, 'r')
    i = 0
    for line in f.readlines():
        if i == 0:
            i += 1
            continue
        line_str = json.loads(line)
        for key in line_str:
            if key == "InsertTime":
                time = line_str[key].replace(line_str[key].split('T')[0] + "T", "").replace('.' + line_str[key].split('.')[-1], "")
                results[role][key].append(time)
                continue
            results[role][key].append(line_str[key])


if __name__ == "__main__":
    input_path, output_path = parse_args(sys.argv)
    result_file = os.path.join(output_path, result_file)

    files = os.listdir(input_path)
    print("Files:", files)
    for file in files:
        if not (file in valid_files): continue
        print(file)
        role = file.replace(".txt", "")
        results[role] = {}
        if not os.path.isdir(file):
            define_result(input_path, file, role)
            collect_result(input_path, file, role)
        duration = 0
        for duration_time in results[role]["DurationInMilliseconds"]:
            duration += duration_time
        if "benchmark" not in file:
            results[role]["AvgSpeed"] = results[role]["NumSince"][-1] / duration * 1000
        else:
            num_record = 0
            for record in results[role]["NumRecords"]:
                num_record += record
            results[role]["AvgSpeed"] = num_record / duration * 1000

    print(results)
    with open(result_file, "w+") as f:
        f.write(json.dumps(results, sort_keys=True))
