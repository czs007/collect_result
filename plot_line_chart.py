import json
import numpy
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

result_file = "./results.txt"


def plot_line_chart(x, y, label, title):
    # plt.plot(x, y, 'r--', label=label)
    plt.scatter(x, y)
    plt.title(title)
    xlabel = 'Order'
    ylabel = 'Speed MB/s'
    if title == 'write_node_insert':
        ylabel = ' Million Ops'
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # plt.legend()
    plt.savefig('./' + title + '.jpg')
#    print(dir(plt))
    #plt.show()
    plt.close()


def cal_logic_order(ts):
    return [ str(i) for i in range(len(ts))]

def cal_to_mb(nums, key):
    if key == 'write_node_insert':
        return  [ (float(x)/1000000.0) for x in nums]
    return  [ (float(x)/500.0) for x in nums]

def cal_proxy_mb(nums, key):
    if key == 'write_node_insert':
        return  [ (float(x)/1000000.0) for x in nums]
    return nums


def cal_avg(durs, nums, key):
    dur = sum([float(d) for d in durs])
    num = sum([float(n) for n in nums])
    avg = num / dur * 1000
    return avg

if __name__ == "__main__":
    f = open(result_file, "r")
    line = f.readline()
    result_str = json.loads(line)
    for key in result_str:
        if key in ["query_node_insert", "reader_get_pulsar", "write_node_insert", "writer_get_pulsar"]:
            plot_line_chart(cal_logic_order(result_str[key]["InsertTime"]), cal_to_mb(result_str[key]["Speed"], key), "insert", key)
            print(key, " ", cal_to_mb([result_str[key]["AvgSpeed"]], key)[0])
            #print(key, " ", cal_avg(result_str[key]["DurationInMilliseconds"], result_str[key]["MsgLength"], key))
        else:
            plot_line_chart(cal_logic_order(result_str[key]["InsertTime"]), result_str[key]["ThroughputInMB"], "insert", key)
            print(key, " ", cal_to_mb([result_str[key]["AvgSpeed"]], key)[0])
            #print(key, " ", result_str[key]["AvgSpeed"])
